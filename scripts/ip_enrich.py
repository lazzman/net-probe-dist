#!/usr/bin/env python3
"""解析节点 server → IP，查询归属地/ASN，并粗分线路类型（机房/家宽/移动/代理）。

默认使用 ip-api.com batch（免费，含 mobile/proxy/hosting 字段）。
结果缓存到 analysis/findings/_ip_cache.json，可跨 run 复用。
"""
from __future__ import annotations

import argparse
import ipaddress
import json
import os
import re
import socket
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

CST = timezone(timedelta(hours=8))
UA = "net-probe-dist-ip-enrich/1.0"
IP_API_BATCH = "http://ip-api.com/batch"
IP_API_FIELDS = (
    "status,message,query,country,countryCode,regionName,city,isp,org,as,asname,"
    "mobile,proxy,hosting,lat,lon,timezone"
)

# 机房/云厂商关键词（org/isp/asname）
DC_KEYWORDS = re.compile(
    r"(cloudflare|amazon|aws|google|gcp|microsoft|azure|digitalocean|linode|akamai|"
    r"fastly|ovh|hetzner|vultr|contabo|oracle|alibaba|aliyun|tencent|huawei|ucloud|"
    r"bandwagon|vultr|choopa|leaseweb|softlayer|ibm\s*cloud|colocation|data\s*center|"
    r"datacenter|hosting|server|vps|dedicated|cdn|edgecast|rackspace|scaleway|"
    r"m247|psychz|quadranet|cogent|hurricane|linode|droplet)",
    re.I,
)
MOBILE_KEYWORDS = re.compile(
    r"(mobile|cellular|lte|5g|4g|cmcc|china\s*mobile|china\s*unicom|china\s*telecom|"
    r"verizon\s*wireless|t-mobile|vodafone|orange\s*mobile|att\s*mobility)",
    re.I,
)
# 常见家宽 ISP 关键词（弱启发，仅 hosting/mobile 都为 false 时辅助）
HOME_KEYWORDS = re.compile(
    r"(broadband|cable|comcast|charter|spectrum|verizon\s*fios|bt\s*broadband|"
    r"telecom|unicom|chinanet|dial-?up|residential|fiber\s*home|home\s*network|"
    r"dynamic|pppoe|adsl|docsis)",
    re.I,
)


def is_ip(host: str) -> bool:
    try:
        ipaddress.ip_address(host)
        return True
    except Exception:
        return False


def resolve_host(host: str, timeout: float = 3.0) -> str | None:
    host = (host or "").strip().strip("[]")
    if not host:
        return None
    if is_ip(host):
        return host
    try:
        socket.setdefaulttimeout(timeout)
        infos = socket.getaddrinfo(host, None)
        # prefer IPv4
        v4 = [x[4][0] for x in infos if x[0] == socket.AF_INET]
        if v4:
            return v4[0]
        if infos:
            return infos[0][4][0]
    except Exception:
        return None
    return None


def classify_type(info: dict[str, Any]) -> str:
    """返回线路类型 code：dc / home / mobile / proxy / unknown。"""
    if not info or info.get("status") == "fail":
        return "unknown"
    blob = " ".join(
        str(info.get(k) or "")
        for k in ("isp", "org", "as", "asname", "country", "city")
    )
    if info.get("proxy") is True:
        return "proxy"
    if info.get("mobile") is True or MOBILE_KEYWORDS.search(blob):
        return "mobile"
    if info.get("hosting") is True or DC_KEYWORDS.search(blob):
        return "dc"
    if HOME_KEYWORDS.search(blob):
        return "home"
    # 默认：非 hosting 视为家宽/接入网（公共库常见分法）
    if info.get("hosting") is False and info.get("mobile") is False:
        return "home"
    return "unknown"


TYPE_LABELS = {
    "dc": "datacenter",
    "home": "residential",
    "mobile": "mobile",
    "proxy": "proxy",
    "unknown": "unknown",
}

TYPE_LABELS_ZH = {
    "dc": "机房",
    "home": "家宽",
    "mobile": "移动",
    "proxy": "代理",
    "unknown": "未知",
}


def http_json(url: str, data: bytes | None = None, timeout: float = 30) -> Any:
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "User-Agent": UA,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST" if data is not None else "GET",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", "replace"))


def lookup_batch(ips: list[str], pauses: float = 1.6) -> dict[str, dict[str, Any]]:
    """ip-api batch，每批最多 100；免费约 45 req/min，批间稍作停顿。"""
    out: dict[str, dict[str, Any]] = {}
    if not ips:
        return out
    uniq = []
    seen = set()
    for ip in ips:
        if ip and ip not in seen:
            seen.add(ip)
            uniq.append(ip)
    for i in range(0, len(uniq), 100):
        chunk = uniq[i : i + 100]
        body = json.dumps([{"query": ip, "fields": IP_API_FIELDS} for ip in chunk]).encode()
        # retry
        for attempt in range(4):
            try:
                rows = http_json(IP_API_BATCH, data=body)
                if not isinstance(rows, list):
                    raise RuntimeError(f"unexpected batch response: {type(rows)}")
                for row in rows:
                    if not isinstance(row, dict):
                        continue
                    q = row.get("query")
                    if q:
                        out[str(q)] = row
                break
            except Exception as e:
                wait = pauses * (attempt + 1)
                print(f"[!] ip-api batch fail attempt={attempt+1}: {e}; sleep {wait:.1f}s", flush=True)
                time.sleep(wait)
        # rate limit soft
        if i + 100 < len(uniq):
            time.sleep(pauses)
        print(f"[*] ip-api progress {min(i+100, len(uniq))}/{len(uniq)}", flush=True)
    return out


def enrich_outbounds(
    obs: list[dict[str, Any]],
    cache: dict[str, Any],
    resolve_workers: int = 32,
    force: bool = False,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """就地写入 o['_meta']['ip']，返回 (obs, stats)。cache 结构见文件。"""
    now = datetime.now(CST).isoformat()
    host_to_ip: dict[str, str | None] = {}
    hosts = []
    for o in obs:
        if not isinstance(o, dict):
            continue
        host = str(o.get("server") or "").strip()
        if host and host not in host_to_ip:
            hosts.append(host)
            host_to_ip[host] = None

    # resolve DNS parallel
    def _res(h: str) -> tuple[str, str | None]:
        return h, resolve_host(h)

    with ThreadPoolExecutor(max_workers=max(4, resolve_workers)) as ex:
        futs = [ex.submit(_res, h) for h in hosts]
        for fut in as_completed(futs):
            h, ip = fut.result()
            host_to_ip[h] = ip

    # decide which IPs need API
    need_ips: list[str] = []
    ip_cache: dict[str, Any] = dict(cache.get("ips") or {})
    for ip in host_to_ip.values():
        if not ip:
            continue
        if force or ip not in ip_cache or not ip_cache[ip].get("status"):
            need_ips.append(ip)

    print(
        f"[*] resolve hosts={len(hosts)} with_ip={sum(1 for v in host_to_ip.values() if v)} "
        f"lookup_need={len(set(need_ips))} cache_hit={len(ip_cache)}",
        flush=True,
    )
    fresh = lookup_batch(sorted(set(need_ips)))
    for ip, row in fresh.items():
        row = dict(row)
        row["fetched_at"] = now
        row["line_type"] = classify_type(row)
        row["line_type_label"] = TYPE_LABELS.get(row["line_type"], "unknown")
        row["line_type_zh"] = TYPE_LABELS_ZH.get(row["line_type"], "未知")
        ip_cache[ip] = row

    # attach to outbounds
    stats = {
        "total": 0,
        "resolved": 0,
        "unresolved": 0,
        "by_country": {},
        "by_type": {},
    }
    for o in obs:
        if not isinstance(o, dict):
            continue
        stats["total"] += 1
        host = str(o.get("server") or "").strip()
        ip = host_to_ip.get(host)
        meta = dict(o.get("_meta") or {})
        ipinfo: dict[str, Any]
        if not ip:
            stats["unresolved"] += 1
            ipinfo = {
                "host": host,
                "ip": None,
                "status": "fail",
                "message": "resolve failed",
                "countryCode": "ZZ",
                "country": "Unknown",
                "line_type": "unknown",
                "line_type_label": "unknown",
                "line_type_zh": "未知",
            }
        else:
            stats["resolved"] += 1
            base = dict(ip_cache.get(ip) or {})
            if not base:
                base = {"status": "fail", "message": "no lookup", "query": ip}
                base["line_type"] = "unknown"
                base["line_type_label"] = "unknown"
                base["line_type_zh"] = "未知"
            if base.get("status") != "success":
                base.setdefault("countryCode", "ZZ")
                base.setdefault("country", "Unknown")
                base["line_type"] = classify_type(base)
                base["line_type_label"] = TYPE_LABELS.get(base["line_type"], "unknown")
                base["line_type_zh"] = TYPE_LABELS_ZH.get(base["line_type"], "未知")
            else:
                # ensure classification present
                if not base.get("line_type"):
                    base["line_type"] = classify_type(base)
                    base["line_type_label"] = TYPE_LABELS.get(base["line_type"], "unknown")
                    base["line_type_zh"] = TYPE_LABELS_ZH.get(base["line_type"], "未知")
            ipinfo = {
                "host": host,
                "ip": ip,
                "status": base.get("status"),
                "country": base.get("country"),
                "countryCode": (base.get("countryCode") or "ZZ").upper(),
                "regionName": base.get("regionName"),
                "city": base.get("city"),
                "isp": base.get("isp"),
                "org": base.get("org"),
                "as": base.get("as"),
                "asname": base.get("asname"),
                "mobile": base.get("mobile"),
                "proxy": base.get("proxy"),
                "hosting": base.get("hosting"),
                "line_type": base.get("line_type") or "unknown",
                "line_type_label": base.get("line_type_label") or "unknown",
                "line_type_zh": base.get("line_type_zh") or "未知",
                "lat": base.get("lat"),
                "lon": base.get("lon"),
                "timezone": base.get("timezone"),
            }
        meta["ip"] = ipinfo
        o["_meta"] = meta
        cc = ipinfo.get("countryCode") or "ZZ"
        lt = ipinfo.get("line_type") or "unknown"
        stats["by_country"][cc] = stats["by_country"].get(cc, 0) + 1
        stats["by_type"][lt] = stats["by_type"].get(lt, 0) + 1

    cache_out = {
        "updated_at": now,
        "provider": "ip-api.com",
        "ips": ip_cache,
        "stats_last_run": stats,
    }
    return obs, {"stats": stats, "cache": cache_out}


def main() -> int:
    ap = argparse.ArgumentParser(description="为 outbounds 做 IP 归属地/类型 enrichment")
    ap.add_argument("--workspace", type=Path, default=Path("."))
    ap.add_argument("--in", dest="infile", type=Path, default=None)
    ap.add_argument("--out", dest="outfile", type=Path, default=None, help="写回 enrichment 后的 outbounds")
    ap.add_argument("--cache", type=Path, default=None)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--resolve-workers", type=int, default=32)
    args = ap.parse_args()
    ws = args.workspace.resolve()
    infile = (args.infile or (ws / "nodes/sing-box/outbounds.json")).resolve()
    cache_path = (args.cache or (ws / "analysis/findings/_ip_cache.json")).resolve()
    outfile = (args.outfile or infile).resolve()
    if not infile.exists():
        print(f"missing {infile}", file=sys.stderr)
        return 1
    obs = json.loads(infile.read_text(encoding="utf-8"))
    if not isinstance(obs, list):
        print("outbounds must be a list", file=sys.stderr)
        return 2
    cache: dict[str, Any] = {}
    if cache_path.exists():
        try:
            cache = json.loads(cache_path.read_text(encoding="utf-8"))
        except Exception:
            cache = {}
    obs2, result = enrich_outbounds(obs, cache, resolve_workers=args.resolve_workers, force=args.force)
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(result["cache"], ensure_ascii=False) + "\n", encoding="utf-8")
    outfile.parent.mkdir(parents=True, exist_ok=True)
    # 持久化时去掉巨大 validation 细节可保留 _meta.ip
    outfile.write_text(json.dumps(obs2, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary_path = ws / "analysis/findings/_ip_enrich_summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(
        json.dumps(result["stats"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result["stats"], ensure_ascii=False, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
