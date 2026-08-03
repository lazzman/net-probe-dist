#!/usr/bin/env python3
"""从 nodes/sing-box/outbounds.json 导出客户端订阅（分享链 / base64 / Clash / WG conf）。

仅包含此前 sing-box live PASS 的节点。不是 sing-box config.json。
"""
from __future__ import annotations

import argparse
import base64
import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.parse import quote, urlencode

ROOT_DEFAULT = Path(__file__).resolve().parents[1]
CST = timezone(timedelta(hours=8))


def q(v: object) -> str:
    return quote(str(v), safe="")


def vless_uri(o: dict) -> str | None:
    uuid, host, port = o.get("uuid"), o.get("server"), o.get("server_port")
    if not (uuid and host and port):
        return None
    tls = o.get("tls") or {}
    transport = o.get("transport") or {}
    params: dict[str, str] = {"encryption": "none", "type": transport.get("type") or "tcp"}
    if transport.get("type") == "ws":
        params["type"] = "ws"
        if transport.get("path"):
            params["path"] = transport["path"]
        host_h = (transport.get("headers") or {}).get("Host")
        if host_h:
            params["host"] = host_h
    elif transport.get("type") == "grpc":
        params["type"] = "grpc"
        if transport.get("service_name"):
            params["serviceName"] = transport["service_name"]
    if tls.get("enabled"):
        reality = tls.get("reality") or {}
        if reality.get("enabled"):
            params["security"] = "reality"
            if reality.get("public_key"):
                params["pbk"] = reality["public_key"]
            params["sid"] = reality.get("short_id") or ""
            if tls.get("server_name"):
                params["sni"] = tls["server_name"]
            fp = (tls.get("utls") or {}).get("fingerprint")
            if fp:
                params["fp"] = fp
        else:
            params["security"] = "tls"
            if tls.get("server_name"):
                params["sni"] = tls["server_name"]
            fp = (tls.get("utls") or {}).get("fingerprint")
            if fp:
                params["fp"] = fp
            if tls.get("insecure"):
                params["allowInsecure"] = "1"
    else:
        params["security"] = "none"
    if o.get("flow"):
        params["flow"] = o["flow"]
    name = o.get("tag") or f"{host}:{port}"
    return f"vless://{uuid}@{host}:{port}?{urlencode(params, quote_via=quote)}#{q(name)}"


def ss_uri(o: dict) -> str | None:
    method, password, host, port = o.get("method"), o.get("password"), o.get("server"), o.get("server_port")
    if not (method and password and host and port):
        return None
    userinfo = base64.urlsafe_b64encode(f"{method}:{password}".encode()).decode().rstrip("=")
    return f"ss://{userinfo}@{host}:{port}#{q(o.get('tag') or f'{host}:{port}')}"


def trojan_uri(o: dict) -> str | None:
    password, host, port = o.get("password"), o.get("server"), o.get("server_port")
    if not (password and host and port):
        return None
    tls = o.get("tls") or {}
    transport = o.get("transport") or {}
    params = {
        "security": "tls" if tls.get("enabled", True) else "none",
        "type": transport.get("type") or "tcp",
    }
    if tls.get("server_name"):
        params["sni"] = tls["server_name"]
    if transport.get("type") == "ws":
        params["type"] = "ws"
        if transport.get("path"):
            params["path"] = transport["path"]
        host_h = (transport.get("headers") or {}).get("Host")
        if host_h:
            params["host"] = host_h
    return (
        f"trojan://{q(password)}@{host}:{port}?{urlencode(params, quote_via=quote)}"
        f"#{q(o.get('tag') or f'{host}:{port}')}"
    )


def vmess_uri(o: dict) -> str | None:
    host, port, uuid = o.get("server"), o.get("server_port"), o.get("uuid")
    if not (host and port and uuid):
        return None
    tls = o.get("tls") or {}
    transport = o.get("transport") or {}
    conf = {
        "v": "2",
        "ps": o.get("tag") or f"{host}:{port}",
        "add": host,
        "port": str(port),
        "id": uuid,
        "aid": str(o.get("alter_id") or 0),
        "scy": o.get("security") or "auto",
        "net": transport.get("type") or "tcp",
        "type": "none",
        "host": (transport.get("headers") or {}).get("Host") or "",
        "path": transport.get("path") or "",
        "tls": "tls" if tls.get("enabled") else "",
        "sni": tls.get("server_name") or "",
    }
    raw = base64.b64encode(json.dumps(conf, ensure_ascii=False, separators=(",", ":")).encode()).decode()
    return f"vmess://{raw}"


def hysteria2_uri(o: dict) -> str | None:
    """回写 hysteria2/hy2 分享链，供 fsl64 等通用订阅使用。"""
    host, port = o.get("server"), o.get("server_port")
    password = o.get("password")
    if not (host and port and password is not None and str(password) != ""):
        return None
    tls = o.get("tls") or {}
    params: dict[str, str] = {}
    sni = tls.get("server_name") or host
    if sni:
        params["sni"] = str(sni)
    if tls.get("insecure"):
        params["insecure"] = "1"
    obfs = o.get("obfs") or {}
    if isinstance(obfs, dict) and obfs.get("type"):
        params["obfs"] = str(obfs.get("type"))
        if obfs.get("password") is not None and str(obfs.get("password")) != "":
            params["obfs-password"] = str(obfs.get("password"))
    # 兼容部分客户端字段
    if o.get("up_mbps") is not None:
        params["upmbps"] = str(o.get("up_mbps"))
    if o.get("down_mbps") is not None:
        params["downmbps"] = str(o.get("down_mbps"))
    name = o.get("tag") or f"{host}:{port}"
    query = f"?{urlencode(params, quote_via=quote)}" if params else ""
    return f"hysteria2://{q(password)}@{host}:{port}{query}#{q(name)}"


def to_uri(o: dict) -> str | None:
    t = o.get("type")
    if t == "vless":
        return vless_uri(o)
    if t == "shadowsocks":
        return ss_uri(o)
    if t == "trojan":
        return trojan_uri(o)
    if t == "vmess":
        return vmess_uri(o)
    if t in ("hysteria2", "hy2"):
        return hysteria2_uri(o)
    return None


def clash_proxy(o: dict) -> dict | None:
    name = o.get("tag") or f"{o.get('server')}:{o.get('server_port')}"
    t = o.get("type")
    if t == "vless":
        p: dict = {
            "name": name,
            "type": "vless",
            "server": o.get("server"),
            "port": o.get("server_port"),
            "uuid": o.get("uuid"),
            "network": (o.get("transport") or {}).get("type") or "tcp",
            "tls": bool((o.get("tls") or {}).get("enabled")),
            "udp": True,
            "packet-encoding": o.get("packet_encoding") or "xudp",
        }
        tls = o.get("tls") or {}
        if tls.get("server_name"):
            p["servername"] = tls["server_name"]
        fp = (tls.get("utls") or {}).get("fingerprint")
        if fp:
            p["client-fingerprint"] = fp
        reality = tls.get("reality") or {}
        if reality.get("enabled"):
            p["reality-opts"] = {
                "public-key": reality.get("public_key"),
                "short-id": reality.get("short_id") or "",
            }
        tr = o.get("transport") or {}
        if tr.get("type") == "ws":
            p["network"] = "ws"
            p["ws-opts"] = {"path": tr.get("path") or "/", "headers": tr.get("headers") or {}}
        if o.get("flow"):
            p["flow"] = o["flow"]
        return p
    if t == "shadowsocks":
        return {
            "name": name,
            "type": "ss",
            "server": o.get("server"),
            "port": o.get("server_port"),
            "cipher": o.get("method"),
            "password": o.get("password"),
            "udp": True,
        }
    if t == "trojan":
        p = {
            "name": name,
            "type": "trojan",
            "server": o.get("server"),
            "port": o.get("server_port"),
            "password": o.get("password"),
            "udp": True,
        }
        tls = o.get("tls") or {}
        if tls.get("server_name"):
            p["sni"] = tls["server_name"]
        tr = o.get("transport") or {}
        if tr.get("type") == "ws":
            p["network"] = "ws"
            p["ws-opts"] = {"path": tr.get("path") or "/", "headers": tr.get("headers") or {}}
        return p
    if t == "vmess":
        p = {
            "name": name,
            "type": "vmess",
            "server": o.get("server"),
            "port": o.get("server_port"),
            "uuid": o.get("uuid"),
            "alterId": o.get("alter_id") or 0,
            "cipher": o.get("security") or "auto",
            "udp": True,
        }
        tls = o.get("tls") or {}
        tr = o.get("transport") or {}
        if tls.get("enabled"):
            p["tls"] = True
            if tls.get("server_name"):
                p["servername"] = tls["server_name"]
        if tr.get("type") == "ws":
            p["network"] = "ws"
            p["ws-opts"] = {"path": tr.get("path") or "/", "headers": tr.get("headers") or {}}
        return p
    if t in ("hysteria2", "hy2"):
        # Clash Meta / mihomo
        p = {
            "name": name,
            "type": "hysteria2",
            "server": o.get("server"),
            "port": o.get("server_port"),
            "password": o.get("password"),
            "udp": True,
        }
        tls = o.get("tls") or {}
        if tls.get("server_name"):
            p["sni"] = tls["server_name"]
        if tls.get("insecure"):
            p["skip-cert-verify"] = True
        obfs = o.get("obfs") or {}
        if isinstance(obfs, dict) and obfs.get("type"):
            p["obfs"] = obfs.get("type")
            if obfs.get("password") is not None and str(obfs.get("password")) != "":
                p["obfs-password"] = obfs.get("password")
        if o.get("up_mbps") is not None:
            p["up"] = o.get("up_mbps")
        if o.get("down_mbps") is not None:
            p["down"] = o.get("down_mbps")
        return p
    if t == "wireguard":
        addrs = o.get("local_address") or []
        ip = ipv6 = None
        for a in addrs if isinstance(addrs, list) else [addrs]:
            a0 = str(a).split("/")[0]
            if ":" in a0:
                ipv6 = a0
            else:
                ip = a0
        p = {
            "name": name,
            "type": "wireguard",
            "server": o.get("server"),
            "port": o.get("server_port"),
            "private-key": o.get("private_key"),
            "public-key": o.get("peer_public_key"),
            "udp": True,
            "mtu": o.get("mtu") or 1280,
        }
        if ip:
            p["ip"] = ip
        if ipv6:
            p["ipv6"] = ipv6
        return p
    return None



def clash_proxy_legacy(o: dict) -> dict | None:
    """老版 Clash 兼容：仅 ss / vmess / trojan，去掉 Meta 专有字段。"""
    t = o.get("type")
    name = o.get("tag") or f"{o.get('server')}:{o.get('server_port')}"
    if t == "shadowsocks":
        return {
            "name": name,
            "type": "ss",
            "server": o.get("server"),
            "port": o.get("server_port"),
            "cipher": o.get("method"),
            "password": o.get("password"),
            "udp": True,
        }
    if t == "trojan":
        p = {
            "name": name,
            "type": "trojan",
            "server": o.get("server"),
            "port": o.get("server_port"),
            "password": o.get("password"),
            "udp": True,
        }
        tls = o.get("tls") or {}
        if tls.get("server_name"):
            p["sni"] = tls["server_name"]
        tr = o.get("transport") or {}
        if tr.get("type") == "ws":
            p["network"] = "ws"
            p["ws-opts"] = {"path": tr.get("path") or "/", "headers": tr.get("headers") or {}}
        return p
    if t == "vmess":
        p = {
            "name": name,
            "type": "vmess",
            "server": o.get("server"),
            "port": o.get("server_port"),
            "uuid": o.get("uuid"),
            "alterId": o.get("alter_id") or 0,
            "cipher": o.get("security") or "auto",
            "udp": True,
        }
        tls = o.get("tls") or {}
        tr = o.get("transport") or {}
        if tls.get("enabled"):
            p["tls"] = True
            if tls.get("server_name"):
                p["servername"] = tls["server_name"]
        if (tr.get("type") or "tcp") == "ws":
            p["network"] = "ws"
            p["ws-opts"] = {"path": tr.get("path") or "/", "headers": tr.get("headers") or {}}
        else:
            p["network"] = "tcp"
        return p
    return None


def build_singbox_subscription(obs: list) -> dict:
    """生成可直接使用的 sing-box 配置 JSON（订阅用）。"""
    outbounds = []
    tags = []
    for o in obs:
        if not isinstance(o, dict):
            continue
        if o.get("type") == "wireguard":
            continue
        clean = {k: v for k, v in o.items() if not str(k).startswith("_")}
        if clean.get("tag") and clean.get("type"):
            outbounds.append(clean)
            tags.append(clean["tag"])
    if not tags:
        tags = ["direct"]
    return {
        "log": {"level": "info"},
        "inbounds": [
            {
                "type": "mixed",
                "tag": "mixed-in",
                "listen": "127.0.0.1",
                "listen_port": 2080,
            }
        ],
        "outbounds": outbounds
        + [
            {
                "type": "selector",
                "tag": "proxy",
                "outbounds": ["auto", *tags, "direct"],
                "default": "auto",
            },
            {
                "type": "urltest",
                "tag": "auto",
                "outbounds": tags,
                "url": "https://www.gstatic.com/generate_204",
                "interval": "5m",
            },
            {"type": "direct", "tag": "direct"},
            {"type": "block", "tag": "block"},
        ],
        "route": {"final": "proxy"},
    }


def yaml_escape(s: object) -> str:
    s = str(s)
    if any(c in s for c in ":#{}[]&*!|>'\"%@`") or s == "" or s.strip() != s:
        return json.dumps(s, ensure_ascii=False)
    return s


def dump_val(v: object, indent: int = 0) -> str:
    sp = "  " * indent
    if isinstance(v, dict):
        lines = []
        for k, val in v.items():
            if isinstance(val, (dict, list)):
                lines.append(f"{sp}{k}:")
                lines.append(dump_val(val, indent + 1))
            else:
                if isinstance(val, bool):
                    vv = "true" if val else "false"
                elif val is None:
                    vv = "null"
                else:
                    vv = yaml_escape(val)
                lines.append(f"{sp}{k}: {vv}")
        return "\n".join(lines)
    if isinstance(v, list):
        lines = []
        for item in v:
            if isinstance(item, dict):
                keys = list(item.items())
                if not keys:
                    lines.append(f"{sp}- {{}}")
                    continue
                k0, v0 = keys[0]
                if isinstance(v0, (dict, list)):
                    lines.append(f"{sp}- {k0}:")
                    lines.append(dump_val(v0, indent + 2))
                    rest = dict(keys[1:])
                    if rest:
                        lines.append(dump_val(rest, indent + 1))
                else:
                    vv = "true" if v0 is True else "false" if v0 is False else yaml_escape(v0)
                    lines.append(f"{sp}- {k0}: {vv}")
                    rest = dict(keys[1:])
                    if rest:
                        lines.append(dump_val(rest, indent + 1))
            else:
                lines.append(f"{sp}- {yaml_escape(item)}")
        return "\n".join(lines)
    return f"{sp}{yaml_escape(v)}"


def main() -> int:
    ap = argparse.ArgumentParser(description="导出订阅文件（分享链/base64/Clash/WG），非 sing-box config")
    ap.add_argument("--workspace", type=Path, default=ROOT_DEFAULT)
    ap.add_argument("--out-dir", type=Path, default=None)
    ap.add_argument("--no-wireguard-files", action="store_true", help="不写出含私钥的 wireguard/*.conf（公开仓推荐）")
    ap.add_argument("--strip-wireguard-from-singbox", action="store_true", help="fslsb/config 中排除 wireguard 私钥节点")
    args = ap.parse_args()
    ws = args.workspace.resolve()
    out = (args.out_dir or (ws / "nodes" / "subscription")).resolve()
    out.mkdir(parents=True, exist_ok=True)
    src = ws / "nodes" / "sing-box" / "outbounds.json"
    if not src.exists():
        print(f"missing {src}", file=sys.stderr)
        return 1
    obs = json.loads(src.read_text(encoding="utf-8"))
    if args.strip_wireguard_from_singbox:
        obs = [o for o in obs if not (isinstance(o, dict) and o.get("type") == "wireguard")]
    # merge endpoints-only WG if needed
    cfg_path = ws / "nodes" / "sing-box" / "config.json"
    if cfg_path.exists():
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
        tags = {o.get("tag") for o in obs}
        for e in cfg.get("endpoints") or []:
            if e.get("tag") in tags:
                continue
            peer = (e.get("peers") or [{}])[0]
            obs.append(
                {
                    "type": "wireguard",
                    "tag": e.get("tag"),
                    "server": peer.get("address"),
                    "server_port": peer.get("port"),
                    "private_key": e.get("private_key"),
                    "peer_public_key": peer.get("public_key"),
                    "local_address": e.get("address"),
                    "mtu": e.get("mtu") or 1280,
                }
            )

    uris: list[str] = []
    by: dict[str, list[str]] = {}
    skipped: list[dict] = []
    for o in obs:
        if o.get("type") == "wireguard":
            skipped.append({"tag": o.get("tag"), "reason": "wireguard→conf/clash，不进通用分享链"})
            continue
        uri = to_uri(o)
        if not uri:
            reason = "uri build failed (%s)" % (o.get("type") or "unknown")
            skipped.append({"tag": o.get("tag"), "type": o.get("type"), "reason": reason})
            continue
        uris.append(uri)
        by.setdefault(str(o.get("type") or "other"), []).append(uri)

    raw = "\n".join(uris) + "\n"
    (out / "verified.txt").write_text(raw, encoding="utf-8")
    (out / "verified_base64.txt").write_text(base64.b64encode(raw.encode()).decode() + "\n", encoding="utf-8")
    for t, arr in by.items():
        (out / f"verified_{t}.txt").write_text("\n".join(arr) + "\n", encoding="utf-8")
        (out / f"verified_{t}_base64.txt").write_text(
            base64.b64encode(("\n".join(arr) + "\n").encode()).decode() + "\n", encoding="utf-8"
        )

    proxies = []
    names = []
    for o in obs:
        p = clash_proxy(o)
        if not p:
            continue
        proxies.append(p)
        names.append(p["name"])
    clash = {
        "mixed-port": 7890,
        "allow-lan": False,
        "mode": "rule",
        "log-level": "info",
        "proxies": proxies,
        "proxy-groups": [
            {"name": "PROXY", "type": "select", "proxies": ["auto", *names, "DIRECT"]},
            {
                "name": "auto",
                "type": "url-test",
                "proxies": names,
                "url": "https://www.gstatic.com/generate_204",
                "interval": 300,
            },
        ],
        "rules": ["MATCH,PROXY"],
    }
    now = datetime.now(CST).isoformat()
    (out / "verified_clash.yaml").write_text(
        f"# verified subscription / clash meta\n# generated_at: {now}\n# count: {len(proxies)}\n"
        + dump_val(clash)
        + "\n",
        encoding="utf-8",
    )


    # ---- 多格式别名：订阅 URL 中替换 fsl64 即可切换格式 ----
    # fsl64 / fslyaml / fslsb / fslyamlcomp
    (out / "fsl64").write_text(base64.b64encode(raw.encode()).decode() + "\n", encoding="utf-8")

    fslyaml_body = (
        f"# Clash Meta / fslyaml\n# generated_at: {now}\n# count: {len(proxies)}\n"
        + dump_val(clash)
        + "\n"
    )
    (out / "fslyaml").write_text(fslyaml_body, encoding="utf-8")

    legacy_proxies: list[dict] = []
    legacy_names: list[str] = []
    for o in obs:
        lp = clash_proxy_legacy(o)
        if not lp:
            continue
        legacy_proxies.append(lp)
        legacy_names.append(lp["name"])
    if not legacy_names:
        legacy_names = ["DIRECT"]
    clash_legacy = {
        "port": 7890,
        "socks-port": 7891,
        "allow-lan": False,
        "mode": "rule",
        "log-level": "info",
        "proxies": legacy_proxies,
        "proxy-groups": [
            {"name": "PROXY", "type": "select", "proxies": ["auto", *legacy_names, "DIRECT"]},
            {
                "name": "auto",
                "type": "url-test",
                "proxies": legacy_names if legacy_proxies else ["DIRECT"],
                "url": "http://www.gstatic.com/generate_204",
                "interval": 300,
            },
        ],
        "rules": ["MATCH,PROXY"],
    }
    fslyamlcomp_body = (
        f"# Clash 老版兼容 / fslyamlcomp\n# generated_at: {now}\n# count: {len(legacy_proxies)}\n"
        + dump_val(clash_legacy)
        + "\n"
    )
    (out / "fslyamlcomp").write_text(fslyamlcomp_body, encoding="utf-8")
    (out / "verified_clash_legacy.yaml").write_text(fslyamlcomp_body, encoding="utf-8")

    sb_cfg = None
    if cfg_path.exists() and not args.strip_wireguard_from_singbox:
        try:
            cand = json.loads(cfg_path.read_text(encoding="utf-8"))
            if isinstance(cand, dict) and cand.get("outbounds") is not None:
                sb_cfg = cand
        except Exception:
            sb_cfg = None
    if sb_cfg is None:
        sb_cfg = build_singbox_subscription(obs)
    elif args.strip_wireguard_from_singbox:
        # 即使读了 config 也要剥 WG
        sb_cfg = build_singbox_subscription(obs)
    fslsb_body = json.dumps(sb_cfg, ensure_ascii=False, indent=2) + "\n"
    (out / "fslsb").write_text(fslsb_body, encoding="utf-8")
    (out / "verified_singbox.json").write_text(fslsb_body, encoding="utf-8")

    wg_dir = out / "wireguard"
    wg_count = 0
    if args.no_wireguard_files:
        # 公开仓库禁止落盘私钥 conf
        if wg_dir.exists():
            for old in wg_dir.glob("*.conf"):
                old.unlink()
    else:
        wg_dir.mkdir(exist_ok=True)
        for old in wg_dir.glob("*.conf"):
            old.unlink()
    _wg_iter = [] if args.no_wireguard_files else obs
    for o in _wg_iter:
        if o.get("type") != "wireguard":
            continue
        addrs = o.get("local_address") or []
        addr_line = ", ".join(addrs) if isinstance(addrs, list) else str(addrs)
        conf = (
            f"# {o.get('tag')}\n"
            f"[Interface]\nPrivateKey = {o.get('private_key')}\nAddress = {addr_line}\n"
            f"DNS = 1.1.1.1\nMTU = {o.get('mtu') or 1280}\n\n"
            f"[Peer]\nPublicKey = {o.get('peer_public_key')}\n"
            f"AllowedIPs = 0.0.0.0/0, ::/0\nEndpoint = {o.get('server')}:{o.get('server_port')}\n"
            f"PersistentKeepalive = 25\n"
        )
        safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in (o.get("tag") or f"wg{wg_count}"))
        (wg_dir / f"{safe}.conf").write_text(conf, encoding="utf-8")
        wg_count += 1

    man = {
        "generated_at": now,
        "source": "nodes/sing-box/outbounds.json (仅 live PASS)",
        "share_link_count": len(uris),
        "clash_proxy_count": len(proxies),
        "wireguard_conf_count": wg_count,
        "by_protocol": {k: len(v) for k, v in by.items()},
        "skipped": skipped,
        "files": {
            "raw": str(out / "verified.txt"),
            "base64": str(out / "verified_base64.txt"),
            "clash": str(out / "verified_clash.yaml"),
            "fsl64": str(out / "fsl64"),
            "fslyaml": str(out / "fslyaml"),
            "fslsb": str(out / "fslsb"),
            "fslyamlcomp": str(out / "fslyamlcomp"),
            "wireguard_dir": str(wg_dir),
        },
        "formats": {
            "fsl64": "通用 base64 分享链订阅",
            "fslyaml": "Clash Meta YAML",
            "fslsb": "sing-box JSON 配置",
            "fslyamlcomp": "老版 Clash 兼容 YAML（ss/vmess/trojan）",
        },
        "usage": {
            "v2rayN_etc": "订阅 URL 使用 .../fsl64 或 verified_base64.txt",
            "clash_meta": "将 URL 中 fsl64 换成 fslyaml",
            "singbox": "将 URL 中 fsl64 换成 fslsb",
            "clash_legacy": "将 URL 中 fsl64 换成 fslyamlcomp",
            "wireguard": "wireguard/*.conf",
        },
        "legacy_clash_proxy_count": len(legacy_proxies),
    }
    (out / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "README.md").write_text(
        f"""# 可用节点订阅（仅 live 实测 PASS）

生成时间：{now}

## 文件

| 文件 | 说明 |
| --- | --- |
| `verified.txt` | 分享链明文 |
| `verified_base64.txt` | 通用 base64 订阅 |
| `verified_clash.yaml` / `fslyaml` | Clash Meta |
| `fsl64` | 通用 base64（URL 关键字） |
| `fslyaml` | Clash Meta（URL 关键字） |
| `fslsb` | sing-box JSON（URL 关键字） |
| `fslyamlcomp` | 老版 Clash 兼容（URL 关键字） |
| `verified_<协议>.txt` | 按协议拆分 |
| `wireguard/*.conf` | WG 节点 |

数量：分享链 {len(uris)}；Clash {len(proxies)}；WG conf {wg_count}
""",
        encoding="utf-8",
    )
    print(json.dumps(man, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
