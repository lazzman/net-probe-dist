#!/usr/bin/env python3
"""将 nodes 收割结果导出为 sing-box 可用配置。

可直接转换：
  - vless / vmess / trojan / ss / hysteria2 / tuic 分享链
  - Clash/Mihomo YAML proxies（若提供文件或节点 raw）
  - WireGuard（需 private_key + peer public_key；仅 endpoint 不够）

不可原生转换：
  - OpenVPN → 写入 nodes/sing-box/openvpn/ 并在 manifest 标明需外部客户端
"""

from __future__ import annotations

import argparse
import shutil
import time
import tempfile
import subprocess
import socket
import signal
import os
import base64
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, unquote, urlparse


ROOT_DEFAULT = Path(__file__).resolve().parents[1]


def tag_safe(name: str, used: set[str]) -> str:
    base = re.sub(r"[^\w.\-一-龥]+", "_", (name or "node").strip()) or "node"
    base = base[:48]
    t = base
    i = 2
    while t in used:
        t = f"{base}_{i}"
        i += 1
    used.add(t)
    return t


def parse_vless(uri: str, tag: str) -> dict[str, Any] | None:
    if not uri.lower().startswith("vless://"):
        return None
    u = urlparse(uri)
    uuid = unquote(u.username or "")
    host = u.hostname
    port = u.port
    if not uuid or not host or not port:
        return None
    q = {k: v[0] for k, v in parse_qs(u.query).items()}
    security = q.get("security", "none")
    network = q.get("type", "tcp")
    outbound: dict[str, Any] = {
        "type": "vless",
        "tag": tag,
        "server": host,
        "server_port": int(port),
        "uuid": uuid,
        "packet_encoding": "xudp",
    }
    flow = q.get("flow")
    if flow:
        outbound["flow"] = flow
    tls: dict[str, Any] | None = None
    if security in ("reality", "tls"):
        tls = {
            "enabled": True,
            "server_name": q.get("sni") or q.get("host") or host,
            "utls": {"enabled": True, "fingerprint": q.get("fp") or "chrome"},
        }
        if security == "reality":
            tls["reality"] = {
                "enabled": True,
                "public_key": q.get("pbk") or "",
                "short_id": q.get("sid") or "",
            }
        outbound["tls"] = tls
    # transport
    if network == "ws":
        outbound["transport"] = {
            "type": "ws",
            "path": q.get("path") or "/",
            "headers": {"Host": q.get("host") or q.get("sni") or host},
        }
    elif network == "grpc":
        outbound["transport"] = {
            "type": "grpc",
            "service_name": q.get("serviceName") or q.get("servicename") or "",
        }
    elif network == "http":
        outbound["transport"] = {
            "type": "http",
            "host": [q.get("host") or host],
            "path": q.get("path") or "/",
        }
    # tcp + header type none is default
    return outbound


def parse_vmess(uri: str, tag: str) -> dict[str, Any] | None:
    if not uri.lower().startswith("vmess://"):
        return None
    raw = uri[8:]
    pad = "=" * ((4 - len(raw) % 4) % 4)
    try:
        data = json.loads(base64.urlsafe_b64decode(raw + pad).decode("utf-8", "replace"))
    except Exception:
        try:
            data = json.loads(base64.b64decode(raw + pad).decode("utf-8", "replace"))
        except Exception:
            return None
    host = data.get("add") or data.get("host")
    port = int(data.get("port") or 0)
    uuid = data.get("id")
    if not host or not port or not uuid:
        return None
    network = data.get("net") or "tcp"
    outbound: dict[str, Any] = {
        "type": "vmess",
        "tag": tag,
        "server": host,
        "server_port": port,
        "uuid": uuid,
        "security": data.get("scy") or data.get("security") or "auto",
        "alter_id": int(data.get("aid") or 0),
    }
    tls_flag = str(data.get("tls") or "").lower()
    if tls_flag in ("tls", "reality"):
        outbound["tls"] = {
            "enabled": True,
            "server_name": data.get("sni") or data.get("host") or host,
        }
    if network == "ws":
        outbound["transport"] = {
            "type": "ws",
            "path": data.get("path") or "/",
            "headers": {"Host": data.get("host") or host},
        }
    elif network == "grpc":
        outbound["transport"] = {"type": "grpc", "service_name": data.get("path") or ""}
    return outbound


def parse_trojan(uri: str, tag: str) -> dict[str, Any] | None:
    if not uri.lower().startswith("trojan://"):
        return None
    u = urlparse(uri)
    password = unquote(u.username or "")
    host = u.hostname
    port = u.port or 443
    if not password or not host:
        return None
    q = {k: v[0] for k, v in parse_qs(u.query).items()}
    outbound: dict[str, Any] = {
        "type": "trojan",
        "tag": tag,
        "server": host,
        "server_port": int(port),
        "password": password,
        "tls": {
            "enabled": True,
            "server_name": q.get("sni") or q.get("peer") or host,
        },
    }
    if q.get("type") == "ws":
        outbound["transport"] = {
            "type": "ws",
            "path": q.get("path") or "/",
            "headers": {"Host": q.get("host") or host},
        }
    return outbound


def parse_ss(uri: str, tag: str) -> dict[str, Any] | None:
    if not uri.lower().startswith("ss://"):
        return None
    # ss://base64(method:pass)@host:port#name  or ss://base64(method:pass@host:port)
    body = uri[5:]
    name = ""
    if "#" in body:
        body, name = body.split("#", 1)
        name = unquote(name)
    try:
        if "@" in body:
            userinfo, hostport = body.rsplit("@", 1)
            if not re.match(r"^[\w-]+\:", userinfo):
                pad = "=" * ((4 - len(userinfo) % 4) % 4)
                userinfo = base64.urlsafe_b64decode(userinfo + pad).decode("utf-8", "replace")
            method, password = userinfo.split(":", 1)
            host, port_s = hostport.rsplit(":", 1)
        else:
            pad = "=" * ((4 - len(body) % 4) % 4)
            decoded = base64.urlsafe_b64decode(body + pad).decode("utf-8", "replace")
            # method:pass@host:port
            userinfo, hostport = decoded.rsplit("@", 1)
            method, password = userinfo.split(":", 1)
            host, port_s = hostport.rsplit(":", 1)
        return {
            "type": "shadowsocks",
            "tag": tag,
            "server": host,
            "server_port": int(port_s),
            "method": method,
            "password": password,
        }
    except Exception:
        return None


def parse_hysteria2(uri: str, tag: str) -> dict[str, Any] | None:
    low = uri.lower()
    if not (low.startswith("hysteria2://") or low.startswith("hy2://")):
        return None
    u = urlparse(uri.replace("hy2://", "hysteria2://", 1))
    password = unquote(u.username or "")
    host = u.hostname
    port = u.port or 443
    if not host:
        return None
    q = {k: v[0] for k, v in parse_qs(u.query).items()}
    outbound: dict[str, Any] = {
        "type": "hysteria2",
        "tag": tag,
        "server": host,
        "server_port": int(port),
        "password": password,
        "tls": {
            "enabled": True,
            "server_name": q.get("sni") or host,
            "insecure": q.get("insecure") in ("1", "true", "True"),
        },
    }
    if q.get("obfs"):
        outbound["obfs"] = {"type": q.get("obfs"), "password": q.get("obfs-password") or q.get("obfs_password") or ""}
    return outbound


def parse_share_link(uri: str, tag: str) -> dict[str, Any] | None:
    uri = (uri or "").strip()
    if not uri:
        return None
    for parser in (parse_vless, parse_vmess, parse_trojan, parse_ss, parse_hysteria2):
        try:
            out = parser(uri, tag)
        except Exception:
            out = None
        if out:
            return out
    return None


def clash_proxy_to_outbound(p: dict[str, Any], tag: str) -> dict[str, Any] | None:
    """Minimal Clash Meta proxy → sing-box outbound."""
    t = (p.get("type") or "").lower()
    name = tag
    server = p.get("server")
    port = p.get("port")
    if not server or not port:
        return None
    port = int(port)
    if t in ("ss", "shadowsocks"):
        return {
            "type": "shadowsocks",
            "tag": name,
            "server": server,
            "server_port": port,
            "method": p.get("cipher") or p.get("method"),
            "password": p.get("password"),
        }
    if t == "vmess":
        out: dict[str, Any] = {
            "type": "vmess",
            "tag": name,
            "server": server,
            "server_port": port,
            "uuid": p.get("uuid"),
            "security": p.get("cipher") or "auto",
            "alter_id": int(p.get("alterId") or p.get("alter_id") or 0),
        }
        if p.get("tls"):
            out["tls"] = {"enabled": True, "server_name": p.get("servername") or p.get("sni") or server}
        net = (p.get("network") or p.get("net") or "tcp").lower()
        if net == "ws":
            ws = p.get("ws-opts") or p.get("ws_opts") or {}
            out["transport"] = {
                "type": "ws",
                "path": ws.get("path") or p.get("path") or "/",
                "headers": ws.get("headers") or {"Host": p.get("host") or server},
            }
        return out
    if t == "vless":
        out = {
            "type": "vless",
            "tag": name,
            "server": server,
            "server_port": port,
            "uuid": p.get("uuid"),
        }
        if p.get("flow"):
            out["flow"] = p["flow"]
        if p.get("tls") or (p.get("reality-opts") or p.get("reality_opts")):
            tls: dict[str, Any] = {
                "enabled": True,
                "server_name": p.get("servername") or p.get("sni") or server,
                "utls": {"enabled": True, "fingerprint": p.get("client-fingerprint") or p.get("fp") or "chrome"},
            }
            reality = p.get("reality-opts") or p.get("reality_opts") or {}
            if reality or str(p.get("tls") or "").lower() == "reality":
                tls["reality"] = {
                    "enabled": True,
                    "public_key": reality.get("public-key") or reality.get("public_key") or p.get("pbk") or "",
                    "short_id": reality.get("short-id") or reality.get("short_id") or p.get("sid") or "",
                }
            out["tls"] = tls
        return out
    if t == "trojan":
        return {
            "type": "trojan",
            "tag": name,
            "server": server,
            "server_port": port,
            "password": p.get("password"),
            "tls": {
                "enabled": True,
                "server_name": p.get("sni") or p.get("servername") or server,
            },
        }
    if t in ("hysteria2", "hy2"):
        return {
            "type": "hysteria2",
            "tag": name,
            "server": server,
            "server_port": port,
            "password": p.get("password") or p.get("auth"),
            "tls": {
                "enabled": True,
                "server_name": p.get("sni") or server,
                "insecure": bool(p.get("skip-cert-verify")),
            },
        }
    if t == "wireguard":
        # clash wireguard fields vary
        priv = p.get("private-key") or p.get("private_key")
        peer = p.get("public-key") or p.get("public_key")
        if not priv or not peer:
            return None
        ip = p.get("ip") or p.get("ipv6")
        local_address = []
        if isinstance(ip, str):
            local_address = [ip if "/" in ip else f"{ip}/32"]
        elif isinstance(ip, list):
            local_address = ip
        return {
            "type": "wireguard",
            "tag": name,
            "server": server,
            "server_port": port,
            "local_address": local_address or ["10.0.0.2/32"],
            "private_key": priv,
            "peer_public_key": peer,
            "pre_shared_key": p.get("pre-shared-key") or p.get("preshared-key") or "",
            "mtu": int(p.get("mtu") or 1408),
        }
    return None


def wireguard_from_dict(n: dict[str, Any], tag: str) -> dict[str, Any] | None:
    """Build WG outbound if keys present in node/raw。

    兼容 free_vpn 的 raw.config = {interface, peers:[...]} 结构（含 pre_shared_key）。
    """
    raw = n.get("raw") if isinstance(n.get("raw"), dict) else {}
    conf = raw.get("config") if isinstance(raw.get("config"), dict) else {}
    iface = conf.get("interface") if isinstance(conf.get("interface"), dict) else {}
    peers = conf.get("peers") if isinstance(conf.get("peers"), list) else []
    p0 = peers[0] if peers and isinstance(peers[0], dict) else {}

    priv = (
        n.get("private_key")
        or raw.get("private_key")
        or raw.get("privateKey")
        or iface.get("private_key")
    )
    pub = (
        n.get("peer_public_key")
        or raw.get("peer_public_key")
        or raw.get("public_key")
        or raw.get("publicKey")
        or p0.get("public_key")
    )
    psk = (
        n.get("pre_shared_key")
        or raw.get("pre_shared_key")
        or raw.get("preshared_key")
        or p0.get("pre_shared_key")
        or p0.get("preshared_key")
        or ""
    )
    host = n.get("host")
    port = n.get("port")
    if not host or not port:
        ep = n.get("endpoint") or p0.get("endpoint") or raw.get("endpoint") or ""
        if ":" in str(ep):
            host, port_s = str(ep).rsplit(":", 1)
            try:
                port = int(port_s)
            except ValueError:
                port = None
    if not (priv and pub and host and port):
        return None
    local = (
        n.get("local_address")
        or raw.get("local_address")
        or raw.get("address")
        or iface.get("address")
        or ["10.0.0.2/32"]
    )
    if isinstance(local, str):
        local = [local]
    mtu = n.get("mtu") or raw.get("mtu") or iface.get("mtu") or 1408
    keepalive = (
        n.get("persistent_keepalive_interval")
        or n.get("persistent_keepalive")
        or p0.get("persistent_keepalive")
        or 25
    )
    return {
        "type": "wireguard",
        "tag": tag,
        "server": host,
        "server_port": int(port),
        "local_address": local,
        "private_key": priv,
        "peer_public_key": pub,
        "pre_shared_key": psk or "",
        "mtu": int(mtu),
        "persistent_keepalive_interval": int(keepalive or 25),
    }



def fetch_text(url: str, timeout: float = 20.0) -> str | None:
    import ssl
    import urllib.request
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "node-harvester-singbox/0.1"})
        ctx = ssl.create_default_context()
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return resp.read().decode("utf-8", "replace")
    except Exception:
        return None

def decode_ovpn_b64(b64: str) -> str | None:
    try:
        pad = "=" * ((4 - len(b64) % 4) % 4)
        return base64.b64decode(b64 + pad).decode("utf-8", "replace")
    except Exception:
        try:
            return base64.urlsafe_b64decode(b64 + pad).decode("utf-8", "replace")
        except Exception:
            return None


def load_nodes_report(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def collect_from_report(report: dict[str, Any], findings_dir: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str]]:
    """Returns outbounds, openvpn_archives, skip_notes."""
    outbounds: list[dict[str, Any]] = []
    openvpn_files: list[dict[str, Any]] = []
    notes: list[str] = []
    used_tags: set[str] = set()

    # Enrich cyberforget with full config if available
    cf_full = findings_dir / "_cyberforget_nodes_full.json"
    cf_by_id: dict[str, dict] = {}
    if cf_full.exists():
        try:
            cfd = json.loads(cf_full.read_text(encoding="utf-8"))
            for n in cfd.get("nodes") or []:
                cf_by_id[str(n.get("id"))] = n
        except Exception:
            pass

    for p in report.get("providers") or []:
        provider = p.get("provider") or "unknown"
        for n in p.get("nodes") or []:
            name = n.get("name") or n.get("id") or provider
            tag = tag_safe(f"{provider}_{name}", used_tags)
            proto = (n.get("protocol") or "").lower()
            uri = n.get("uri") or n.get("share_link") or (n.get("raw") or {}).get("share_link") if isinstance(n.get("raw"), dict) else None
            raw = n.get("raw") if isinstance(n.get("raw"), dict) else {}

            # 1) share link
            if uri:
                try:
                    ob = parse_share_link(str(uri), tag)
                except Exception:
                    ob = None
                if ob:
                    meta = {
                        "provider": provider,
                        "source": "share_link",
                        "reachable": n.get("reachable"),
                        "share_link": str(uri),
                    }
                    if n.get("first_source") or raw.get("first_source"):
                        meta["first_source"] = n.get("first_source") or raw.get("first_source")
                    if n.get("first_project") or raw.get("first_project"):
                        meta["first_project"] = n.get("first_project") or raw.get("first_project")
                    if n.get("source_urls") or raw.get("source_urls"):
                        meta["source_urls"] = n.get("source_urls") or raw.get("source_urls")
                    ob["_meta"] = meta
                    outbounds.append(ob)
                    continue

            # 2) clash proxy object
            if raw.get("type") and raw.get("server"):
                ob = clash_proxy_to_outbound(raw, tag)
                if ob:
                    ob["_meta"] = {"provider": provider, "source": "clash_proxy", "reachable": n.get("reachable")}
                    outbounds.append(ob)
                    continue

            # 3) wireguard with keys
            if proto == "wireguard" or provider in ("free_vpn_mac", "yptun"):
                ob = wireguard_from_dict(n, tag)
                if ob:
                    ob["_meta"] = {"provider": provider, "source": "wireguard", "reachable": n.get("reachable")}
                    outbounds.append(ob)
                    continue
                notes.append(f"skip {provider}/{name}: WireGuard 缺 private_key/peer_public_key（仅有 endpoint）")
                continue

            # 4) openvpn → archive only
            if proto == "openvpn" or provider in ("cyberforget", "serverstream"):
                b64 = raw.get("config_b64") or n.get("config_b64")
                if not b64 and provider == "cyberforget":
                    b64 = (cf_by_id.get(str(n.get("id"))) or {}).get("config_b64")
                ovpn_text = None
                if b64:
                    ovpn_text = decode_ovpn_b64(b64)
                # serverstream: may need download from url - store url reference
                url = n.get("url") or raw.get("url")
                if not ovpn_text and url and str(url).endswith(".ovpn"):
                    ovpn_text = fetch_text(str(url))
                openvpn_files.append(
                    {
                        "tag": tag,
                        "provider": provider,
                        "name": name,
                        "endpoint": n.get("endpoint"),
                        "host": n.get("host"),
                        "port": n.get("port"),
                        "url": url,
                        "auth_user_pass": n.get("auth_user_pass") or raw.get("auth_user_pass"),
                        "ovpn": ovpn_text,
                        "reachable": n.get("reachable"),
                        "note": "sing-box 不原生支持 OpenVPN；请用 OpenVPN 客户端或外部 core",
                    }
                )
                continue

            notes.append(f"skip {provider}/{name}: 协议 {proto or '?'} 无法转换为 sing-box outbound")

    return outbounds, openvpn_files, notes


def strip_meta(outbounds: list[dict[str, Any]]) -> list[dict[str, Any]]:
    clean = []
    for o in outbounds:
        c = {k: v for k, v in o.items() if not k.startswith("_")}
        clean.append(c)
    return clean



def wireguard_to_endpoint(ob: dict[str, Any]) -> dict[str, Any] | None:
    """sing-box 1.11+：WireGuard 从 outbound 迁移为 endpoint。"""
    if (ob.get("type") or "").lower() != "wireguard":
        return None
    tag = ob.get("tag") or "wg"
    priv = ob.get("private_key")
    pub = ob.get("peer_public_key")
    host = ob.get("server")
    port = ob.get("server_port")
    local = ob.get("local_address") or ["10.0.0.2/32"]
    if isinstance(local, str):
        local = [x.strip() for x in re.split(r"[\s,]+", local) if x.strip()]
    local2: list[str] = []
    for a in local:
        if "/" not in a:
            a = a + ("/128" if ":" in a else "/32")
        local2.append(a)
    if not (priv and pub and host and port):
        return None
    peer = {
        "address": host,
        "port": int(port),
        "public_key": pub,
        "allowed_ips": ["0.0.0.0/0", "::/0"],
        "persistent_keepalive_interval": int(ob.get("persistent_keepalive_interval") or 25),
    }
    psk = ob.get("pre_shared_key") or ""
    if psk:
        peer["pre_shared_key"] = psk
    return {
        "type": "wireguard",
        "tag": tag,
        "system": False,
        "mtu": int(ob.get("mtu") or 1280),
        "address": local2,
        "private_key": priv,
        "peers": [peer],
    }


def split_wireguard_endpoints(
    outbounds: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """把 type=wireguard 的 outbound 转成 endpoints，其余保持 outbound。"""
    endpoints: list[dict[str, Any]] = []
    rest: list[dict[str, Any]] = []
    for ob in outbounds:
        clean = {k: v for k, v in ob.items() if not k.startswith("_")}
        if (clean.get("type") or "").lower() == "wireguard":
            ep = wireguard_to_endpoint(clean)
            if ep:
                endpoints.append(ep)
            else:
                rest.append(clean)
        else:
            rest.append(clean)
    return endpoints, rest


def build_singbox_config(outbounds: list[dict[str, Any]], mixed_port: int = 2080) -> dict[str, Any]:
    """生成兼容 sing-box 1.12+/1.13 的配置（WireGuard 走 endpoints）。"""
    endpoints, clean = split_wireguard_endpoints(outbounds)
    # 非 WG outbound + endpoint tag 都可被 urltest/selector 引用
    tags = [o["tag"] for o in clean if o.get("tag")] + [e["tag"] for e in endpoints if e.get("tag")]
    selector_tag = "proxy"
    auto_tag = "auto"

    out_list: list[dict[str, Any]] = [
        {"type": "direct", "tag": "direct"},
        {"type": "block", "tag": "block"},
    ]
    out_list.extend(clean)
    if tags:
        out_list.append(
            {
                "type": "urltest",
                "tag": auto_tag,
                "outbounds": tags,
                "url": "https://www.gstatic.com/generate_204",
                "interval": "5m",
                "tolerance": 100,
            }
        )
        out_list.append(
            {
                "type": "selector",
                "tag": selector_tag,
                "outbounds": [auto_tag, *tags, "direct"],
                "default": auto_tag,
            }
        )
        final = selector_tag
    else:
        final = "direct"

    cfg: dict[str, Any] = {
        "log": {"level": "info", "timestamp": True},
        "inbounds": [
            {
                "type": "mixed",
                "tag": "mixed-in",
                "listen": "127.0.0.1",
                "listen_port": mixed_port,
            }
        ],
        "outbounds": out_list,
        "route": {
            "rules": [
                {"action": "sniff"},
                {"ip_is_private": True, "outbound": "direct"},
            ],
            "final": final,
            "auto_detect_interface": True,
        },
    }
    if endpoints:
        cfg["endpoints"] = endpoints
    return cfg



def build_probe_config(outbound: dict[str, Any], listen_port: int) -> dict[str, Any]:
    ob = {k: v for k, v in outbound.items() if not k.startswith("_")}
    tag = ob["tag"]
    cfg: dict[str, Any] = {
        "log": {"level": "warn"},
        "inbounds": [
            {
                "type": "mixed",
                "tag": "mixed-in",
                "listen": "127.0.0.1",
                "listen_port": listen_port,
            }
        ],
        "route": {
            "rules": [{"action": "sniff"}],
            "final": tag,
        },
    }
    # sing-box 1.11+ WireGuard 使用 endpoints
    if (ob.get("type") or "").lower() == "wireguard":
        ep = wireguard_to_endpoint(ob)
        if ep is None:
            # 让 check 阶段失败并带上原因
            cfg["outbounds"] = [ob, {"type": "direct", "tag": "direct"}]
        else:
            cfg["endpoints"] = [ep]
            cfg["outbounds"] = [{"type": "direct", "tag": "direct"}]
    else:
        cfg["outbounds"] = [ob, {"type": "direct", "tag": "direct"}]
    return cfg


def find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return int(s.getsockname()[1])


def resolve_singbox_bin(explicit: str | None = None) -> str | None:
    if explicit:
        p = Path(explicit)
        if p.exists():
            return str(p)
    return shutil.which("sing-box")


def singbox_check(bin_path: str, config_path: Path, timeout: float = 15.0) -> tuple[bool, str]:
    try:
        proc = subprocess.run(
            [bin_path, "check", "-c", str(config_path)],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        msg = ((proc.stderr or "") + (proc.stdout or "")).strip()
        return proc.returncode == 0, msg
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"


def singbox_live_probe(
    bin_path: str,
    outbound: dict[str, Any],
    *,
    test_url: str = "https://www.gstatic.com/generate_204",
    connect_timeout: float = 10.0,
    max_time: float = 18.0,
    boot_wait: float = 1.0,
) -> tuple[bool, dict[str, Any]]:
    """启动临时 sing-box，经 mixed 代理访问 test_url，验证 outbound 真实可用。"""
    port = find_free_port()
    cfg = build_probe_config(outbound, port)
    with tempfile.TemporaryDirectory(prefix="sb-probe-") as td:
        td_path = Path(td)
        cfg_path = td_path / "config.json"
        log_path = td_path / "run.log"
        cfg_path.write_text(json.dumps(cfg, ensure_ascii=False, indent=2), encoding="utf-8")

        ok_check, check_msg = singbox_check(bin_path, cfg_path)
        if not ok_check:
            return False, {
                "stage": "check",
                "ok": False,
                "detail": check_msg[-800:],
                "http_code": None,
                "listen_port": port,
            }

        with open(log_path, "w", encoding="utf-8") as logf:
            try:
                proc = subprocess.Popen(
                    [bin_path, "run", "-c", str(cfg_path)],
                    stdout=logf,
                    stderr=subprocess.STDOUT,
                )
            except Exception as e:
                return False, {"stage": "start", "ok": False, "detail": str(e), "http_code": None}

            try:
                time.sleep(boot_wait)
                if proc.poll() is not None:
                    detail = log_path.read_text(encoding="utf-8", errors="replace")[-800:]
                    return False, {
                        "stage": "start",
                        "ok": False,
                        "detail": detail or f"sing-box exited {proc.returncode}",
                        "http_code": None,
                        "listen_port": port,
                    }

                curl = subprocess.run(
                    [
                        "curl",
                        "-sS",
                        "-o",
                        "/dev/null",
                        "-w",
                        "%{http_code}",
                        "--connect-timeout",
                        str(int(connect_timeout)),
                        "--max-time",
                        str(int(max_time)),
                        "-x",
                        f"http://127.0.0.1:{port}",
                        test_url,
                    ],
                    capture_output=True,
                    text=True,
                )
                code = (curl.stdout or "").strip()
                live_ok = code in {"204", "200"}
                detail = {
                    "http_code": code or None,
                    "curl_stderr": (curl.stderr or "")[-300:],
                    "log_tail": log_path.read_text(encoding="utf-8", errors="replace")[-600:],
                    "listen_port": port,
                    "test_url": test_url,
                }
                if live_ok:
                    return True, {"stage": "live", "ok": True, **detail}
                return False, {
                    "stage": "live",
                    "ok": False,
                    "detail": f"http_code={code}",
                    **detail,
                }
            finally:
                if proc.poll() is None:
                    proc.send_signal(signal.SIGTERM)
                    try:
                        proc.wait(timeout=3)
                    except Exception:
                        proc.kill()


def validate_outbounds(
    outbounds: list[dict[str, Any]],
    bin_path: str,
    *,
    test_url: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    passed: list[dict[str, Any]] = []
    failed: list[dict[str, Any]] = []
    for ob in outbounds:
        tag = ob.get("tag")
        print(f"[*] sing-box 验证 outbound `{tag}` ...", flush=True)
        ok, info = singbox_live_probe(bin_path, ob, test_url=test_url)
        ob2 = dict(ob)
        meta = dict(ob2.get("_meta") or {})
        meta["singbox_validation"] = info
        ob2["_meta"] = meta
        if ok:
            print(f"    PASS http={info.get('http_code')}", flush=True)
            passed.append(ob2)
        else:
            print(
                f"    FAIL stage={info.get('stage')} detail={str(info.get('detail'))[:160]}",
                flush=True,
            )
            failed.append(ob2)
    return passed, failed


def write_openvpn_archive(items: list[dict[str, Any]], out_dir: Path) -> list[dict[str, Any]]:
    out_dir.mkdir(parents=True, exist_ok=True)
    index = []
    for it in items:
        tag = it["tag"]
        entry = {
            "tag": tag,
            "provider": it.get("provider"),
            "name": it.get("name"),
            "endpoint": it.get("endpoint"),
            "url": it.get("url"),
            "auth_user_pass": it.get("auth_user_pass"),
            "reachable": it.get("reachable"),
            "note": it.get("note"),
            "singbox_native": False,
        }
        if it.get("ovpn"):
            fp = out_dir / f"{tag}.ovpn"
            fp.write_text(it["ovpn"], encoding="utf-8")
            entry["file"] = str(fp.name)
        index.append(entry)
    (out_dir / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return index


def main() -> int:
    ap = argparse.ArgumentParser(description="导出并经 sing-box 实测过滤的配置")
    ap.add_argument("--workspace", type=Path, default=ROOT_DEFAULT)
    ap.add_argument("--nodes-json", type=Path, default=None)
    ap.add_argument("--out-dir", type=Path, default=None)
    ap.add_argument("--mixed-port", type=int, default=2080)
    ap.add_argument("--only-reachable", action="store_true")
    ap.add_argument("--fetch-openvpn-configs", action="store_true")
    ap.add_argument("--sing-box-bin", default=None)
    ap.add_argument(
        "--skip-singbox-verify",
        action="store_true",
        help="危险：跳过实测（默认必须实测通过才写入可用 config）",
    )
    ap.add_argument("--allow-empty", action="store_true", help="无可用节点时 exit 0")
    ap.add_argument("--test-url", default="https://www.gstatic.com/generate_204")
    args = ap.parse_args()

    workspace = args.workspace.resolve()
    nodes_json = (args.nodes_json or (workspace / "nodes" / "nodes.json")).resolve()
    out_dir = (args.out_dir or (workspace / "nodes" / "sing-box")).resolve()
    findings_dir = workspace / "analysis" / "findings"

    if not nodes_json.exists():
        print(f"缺少 {nodes_json}，请先运行 harvest_nodes.py", file=sys.stderr)
        return 2

    bin_path = resolve_singbox_bin(args.sing_box_bin)
    if not args.skip_singbox_verify and not bin_path:
        print(
            "未找到 sing-box，无法做可用性验证。请安装：brew install sing-box\n"
            "或传入 --sing-box-bin /path/to/sing-box\n"
            "若仅想生成未验证配置，显式加 --skip-singbox-verify（不推荐）",
            file=sys.stderr,
        )
        return 3

    if args.fetch_openvpn_configs:
        script = findings_dir / "cyberforget_fetch.py"
        if script.exists():
            subprocess.run(
                [
                    sys.executable,
                    str(script),
                    "--app-like",
                    "--limit",
                    "15",
                    "--out",
                    str(findings_dir / "_cyberforget_nodes_full.json"),
                ],
                check=False,
            )

    report = load_nodes_report(nodes_json)
    if args.only_reachable:
        for p in report.get("providers") or []:
            p["nodes"] = [n for n in (p.get("nodes") or []) if n.get("reachable") is not False]

    candidates, openvpn_items, notes = collect_from_report(report, findings_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    verified: list[dict[str, Any]] = []
    failed: list[dict[str, Any]] = []

    if args.skip_singbox_verify:
        print("[!] 跳过 sing-box 实测（--skip-singbox-verify）", flush=True)
        verified = candidates
    else:
        assert bin_path
        print(f"[*] 使用 sing-box: {bin_path}", flush=True)
        print(
            f"[*] 候选 outbound: {len(candidates)}，开始 check+连通验证（{args.test_url}）",
            flush=True,
        )
        verified, failed = validate_outbounds(candidates, bin_path, test_url=args.test_url)

    config = build_singbox_config(verified, mixed_port=args.mixed_port)
    config_path = out_dir / "config.json"
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    final_check_ok = None
    final_check_msg = ""
    if bin_path and verified:
        final_check_ok, final_check_msg = singbox_check(bin_path, config_path)
        print(f"[*] 最终 config check: {'PASS' if final_check_ok else 'FAIL'}", flush=True)
        if not final_check_ok:
            for ob in verified:
                meta = dict(ob.get("_meta") or {})
                meta["singbox_validation"] = {
                    "stage": "final_config_check",
                    "ok": False,
                    "detail": final_check_msg[-500:],
                }
                ob["_meta"] = meta
                failed.append(ob)
            verified = []
            config = build_singbox_config([], mixed_port=args.mixed_port)
            config_path.write_text(
                json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )

    outbounds_only = strip_meta(verified)
    (out_dir / "outbounds.json").write_text(
        json.dumps(outbounds_only, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    failed_dump = []
    for o in failed:
        item = {k: v for k, v in o.items() if not k.startswith("_")}
        meta = o.get("_meta") or {}
        item["provider"] = meta.get("provider")
        item["validation"] = meta.get("singbox_validation")
        failed_dump.append(item)
    (out_dir / "outbounds.failed.json").write_text(
        json.dumps(failed_dump, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    ovpn_index = write_openvpn_archive(openvpn_items, out_dir / "openvpn")

    def rel(p: Path) -> str:
        try:
            return str(p.resolve().relative_to(workspace))
        except Exception:
            return str(p)

    manifest = {
        "generated_at": datetime.now().astimezone().isoformat(),
        "source": rel(nodes_json),
        "singbox_bin": bin_path,
        "verification_required": not args.skip_singbox_verify,
        "test_url": args.test_url,
        "candidates": len(candidates),
        "singbox_outbounds_verified": len(outbounds_only),
        "singbox_outbounds_failed": len(failed_dump),
        "openvpn_profiles": len(ovpn_index),
        "outbound_tags": [o.get("tag") for o in outbounds_only],
        "outbound_types": sorted({o.get("type") for o in outbounds_only if o.get("type")}),
        "failed_tags": [o.get("tag") for o in failed_dump],
        "final_config_check": final_check_ok,
        "final_config_check_msg": (final_check_msg or "")[-500:],
        "config": rel(config_path),
        "notes": notes,
        "usage": {
            "sing_box": f"sing-box run -c {config_path}",
            "mixed_proxy": f"127.0.0.1:{args.mixed_port}",
            "openvpn": "见 openvpn/ 目录；sing-box 不原生支持，未计入 verified",
        },
    }
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    md = [
        "# sing-box 导出（仅含实测可用节点）",
        "",
        f"> 生成时间：{manifest['generated_at']}",
        "",
        f"- 候选 outbound：{manifest['candidates']}",
        f"- **sing-box 实测通过：{manifest['singbox_outbounds_verified']}**（类型：{', '.join(manifest['outbound_types']) or '无'}）",
        f"- sing-box 实测失败：{manifest['singbox_outbounds_failed']}",
        f"- OpenVPN 归档：{manifest['openvpn_profiles']}（非 sing-box 原生，未计入可用）",
        f"- 主配置：`{manifest['config']}`",
        f"- 验证：`sing-box check` + `sing-box run` 经 mixed 访问 `{args.test_url}`，HTTP 200/204 才算通过",
        f"- 最终 config check：{manifest['final_config_check']}",
        "",
        "## 使用",
        "",
        "```bash",
        f"sing-box check -c {config_path}",
        f"sing-box run -c {config_path}",
        "```",
        "",
        "## 已验证 Outbounds",
        "",
        "| tag | type | provider |",
        "| --- | --- | --- |",
    ]
    for o in verified:
        meta = o.get("_meta") or {}
        md.append(f"| `{o.get('tag')}` | {o.get('type')} | {meta.get('provider', '-')} |")
    if not verified:
        md.append("| （无） | - | 当前无节点通过 sing-box 实测 |")

    md += ["", "## 实测失败", ""]
    if failed_dump:
        md += ["| tag | type | provider | stage | detail |", "| --- | --- | --- | --- | --- |"]
        for o in failed_dump:
            val = o.get("validation") or {}
            detail = str(val.get("detail") or val.get("http_code") or "")[:80].replace("|", "/")
            md.append(
                f"| `{o.get('tag')}` | {o.get('type')} | {o.get('provider')} | {val.get('stage')} | {detail} |"
            )
    else:
        md.append("- 无")

    md += ["", "## 跳过/限制", ""]
    if notes:
        for n in notes[:40]:
            md.append(f"- {n}")
        if len(notes) > 40:
            md.append(f"- … 另有 {len(notes) - 40} 条")
    else:
        md.append("- 无")
    md += [
        "",
        "## OpenVPN",
        "",
        "sing-box 不包含 OpenVPN。相关配置仅归档在 `openvpn/`，**不算** sing-box 可用节点。",
        "",
    ]
    (out_dir / "README.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    summary = {
        "ok": bool(verified) or args.allow_empty or args.skip_singbox_verify,
        "verified": len(verified),
        "failed": len(failed_dump),
        "candidates": len(candidates),
        "openvpn_profiles": len(ovpn_index),
        "config": str(config_path),
        "types": manifest["outbound_types"],
        "tags": manifest["outbound_tags"],
        "failed_tags": manifest["failed_tags"],
        "final_config_check": final_check_ok,
        "verification_required": not args.skip_singbox_verify,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if not verified and not args.skip_singbox_verify and not args.allow_empty:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
