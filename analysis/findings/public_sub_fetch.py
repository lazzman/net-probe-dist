#!/usr/bin/env python3
"""公开订阅源全量抓取（Sherd/NovaLink 等硬编码公开订阅 + 补充源）。

默认：去重后的全部链接都进入 nodes，**不做抽样**。
每条节点带 source_urls（出现过的订阅源），便于按源汇总候选/可用。
可用性必须经 sing-box check + live 实测。
"""
from __future__ import annotations

import argparse
import base64
import json
import re
import ssl
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

# 公开订阅源（HTTP 可达 + 可解析出 share link 才保留；2026-08-06 复核）
# 优先：活跃维护 / 多协议 / 跨项目去重有增量；超大全量文件每项目取 1 个入口
SOURCES = [
    # --- barry-far/V2ray-Config ---
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/vless.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/ss.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/vmess.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/trojan.txt",
    # --- Epodonios/v2ray-configs ---
    "https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt",
    "https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/ss.txt",
    "https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vmess.txt",
    "https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/trojan.txt",
    # --- 0xRadikal/Free-v2ray-Configs ---
    "https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/all/configs.txt",
    "https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt",
    "https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/protocols/vless.txt",
    "https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/protocols/shadowsocks.txt",
    "https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/protocols/hysteria2.txt",
    "https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/protocols/trojan.txt",
    # --- MatinGhanbari/v2ray-configs ---
    "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/all_sub.txt",
    "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt",
    "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/ss.txt",
    "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vmess.txt",
    "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/trojan.txt",
    "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/hysteria2.txt",
    # --- Surfboardv2ray ---
    "https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/python/vless",
    "https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/python/ss",
    "https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/python/hy2",
    "https://raw.githubusercontent.com/Surfboardv2ray/Proxy-sorter/main/output/converted.txt",
    # --- 大型聚合（单入口） ---
    "https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/main/all_extracted_configs.txt",
    "https://raw.githubusercontent.com/mheidari98/.proxy/main/all",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/all_configs.txt",
    "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge_base64.txt",
    "https://raw.githubusercontent.com/Delta-Kronecker/V2ray-Config/main/config/all_configs.txt",
    "https://raw.githubusercontent.com/sakha1370/OpenRay/main/output/all_valid_proxies.txt",
    "https://raw.githubusercontent.com/yitong2333/proxy-minging/main/v2ray.txt",
    "https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/protocols/vl.txt",
    "https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/protocols/ss.txt",
    "https://raw.githubusercontent.com/Argh94/V2RayAutoConfig/main/configs/Vless.txt",
    "https://raw.githubusercontent.com/Argh94/V2RayAutoConfig/main/configs/ShadowSocks.txt",
    "https://raw.githubusercontent.com/Argh94/V2RayAutoConfig/main/configs/Hysteria2.txt",
    "https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/1.txt",
    "https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/vless",
    "https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/ss",
    "https://raw.githubusercontent.com/Leon406/SubCrawler/main/sub/share/hysteria2",
    "https://raw.githubusercontent.com/LalatinaHub/Mineral/master/result/nodes",
    "https://raw.githubusercontent.com/10ium/ScrapeAndCategorize/main/output_configs/Vless.txt",
    "https://cdn.jsdelivr.net/gh/xiaoji235/airport-free/v2ray.txt",
    # --- 中小型 / 补充协议覆盖 ---
    "https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt",
    "https://raw.githubusercontent.com/Au1rxx/free-vpn-subscriptions/main/output/v2ray-base64.txt",
    "https://raw.githubusercontent.com/4n0nymou3/multi-proxy-config-fetcher/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/DiDiten/HiN-VPN/main/subscription/hiddify/mix",
    "https://raw.githubusercontent.com/wuqb2i4f/xray-config-toolkit/main/output/base64/mix-uri",
    "https://raw.githubusercontent.com/Mahdi0024/ProxyCollector/master/sub/proxies.txt",
    "https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/mixed_iran.txt",
    "https://raw.githubusercontent.com/chengaopan/AutoMergePublicNodes/master/list_raw.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/V2RAY_RAW.txt",
    "https://raw.githubusercontent.com/free18/v2ray/main/v.txt",
    "https://raw.githubusercontent.com/CidVpn/cid-vpn-config/main/general.txt",
    "https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt",
    "https://raw.githubusercontent.com/Kwinshadow/TelegramV2rayCollector/main/sublinks/mix.txt",
    "https://raw.githubusercontent.com/acymz/AutoVPN/main/data/V2.txt",
    "https://raw.githubusercontent.com/Ruk1ng001/freeSub/main/v2ray",
    "https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription1",
    "https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription2",
    "https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/v2ray.txt",
    "https://raw.githubusercontent.com/Mosifree/-FREE2CONFIG/main/SS",
    "https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/v2rayshare.txt",
    "https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/nodefree.txt",
    "https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/wenode.txt",
    "https://raw.githubusercontent.com/ripaojiedian/freenode/main/sub",
    "https://raw.githubusercontent.com/hans-thomas/v2ray-subscription/master/servers.txt",
    "https://raw.githubusercontent.com/mfuu/v2ray/master/v2ray",
    "https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list_raw.txt",
    "https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub",
    "https://kuajing-tools.vip/free-subscriptions/latest/v2ray-all.txt",
    "https://imtaqin.id/api/vpn/sub/ss",
    "https://imtaqin.id/api/vpn/sub/vmess",
    "https://imtaqin.id/api/vpn/sub/trojan",
    "https://freeproxydb.com/api/proxy/subscribe?count=100&subscribe_format=original&protocol=vmess%2Cvless%2Ctrojan%2Chysteria2%2Css",
]
LINK_RE = re.compile(r"(?:vless|vmess|trojan|ss|hysteria2?|hy2|tuic)://[^\s<>\"']+", re.I)
UA = "node-harvester-public-sub/0.3"


def source_project(url: str) -> str:
    """从订阅 URL 提取项目键：owner/repo 或域名。"""
    m = re.search(r"raw\.githubusercontent\.com/([^/]+/[^/]+)/", url)
    if m:
        return m.group(1)
    m = re.search(r"github\.com/([^/]+/[^/]+)/", url)
    if m:
        return m.group(1)
    try:
        return urlparse(url).netloc or url
    except Exception:
        return url


def fetch(url: str, timeout: float = 20.0) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ssl.create_default_context()) as resp:
            return resp.status, resp.read(32_000_000).decode("utf-8", "replace")
    except Exception as e:
        code = getattr(e, "code", 0) or 0
        return code, str(e)


def extract_links(text: str) -> list[str]:
    links = LINK_RE.findall(text)
    if links:
        return links
    compact = "".join(text.strip().split())
    try:
        dec = base64.b64decode(compact + "===").decode("utf-8", "ignore")
        links = LINK_RE.findall(dec)
        if links:
            return links
    except Exception:
        pass
    out: list[str] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if "://" in line:
            out += LINK_RE.findall(line)
            continue
        try:
            dec = base64.b64decode(line + "===").decode("utf-8", "ignore")
            out += LINK_RE.findall(dec)
        except Exception:
            pass
    return out


def sample_links(links: list[str], per_scheme: dict[str, int] | None = None) -> list[str]:
    """仅显式 per_scheme 时限额；默认全量流程不应调用。"""
    if not per_scheme:
        return list(links)
    by: dict[str, list[str]] = {}
    for L in links:
        by.setdefault(L.split("://", 1)[0].lower(), []).append(L)
    out: list[str] = []
    for sch, q in per_scheme.items():
        arr = by.get(sch) or []
        hosts: set[str] = set()
        n = 0
        for L in arr:
            m = re.search(r"@([^:/?\s]+):(\d+)", L)
            host = m.group(1) if m else None
            if host and host in hosts:
                continue
            if host:
                hosts.add(host)
            out.append(L)
            n += 1
            if n >= q:
                break
    return out


def collect(per_scheme: dict[str, int] | None = None, *, full: bool = True) -> dict:
    """默认 full=True：全部去重链接，不抽样。"""
    # url -> links (source-local order)
    per_url: dict[str, list[str]] = {}
    meta = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(lambda u=u: fetch(u, 20.0)): u for u in SOURCES}
        for fut in as_completed(futs):
            u = futs[fut]
            try:
                st, body = fut.result()
            except Exception as e:
                st, body = 0, f"{type(e).__name__}: {e}"
            links = extract_links(body) if st == 200 else []
            # source-local dedup keep order
            seen_l: set[str] = set()
            uniq_l: list[str] = []
            for L in links:
                if L in seen_l:
                    continue
                seen_l.add(L)
                uniq_l.append(L)
            per_url[u] = uniq_l
            meta.append(
                {
                    "url": u,
                    "project": source_project(u),
                    "status": st,
                    "links": len(links),
                    "uniq_in_source": len(uniq_l),
                }
            )

    # 全局去重 + 归属：first_source 按 SOURCES 顺序；all sources 收集
    link_first: dict[str, str] = {}
    link_all: dict[str, list[str]] = {}
    for u in SOURCES:
        for L in per_url.get(u) or []:
            link_all.setdefault(L, [])
            if u not in link_all[L]:
                link_all[L].append(u)
            if L not in link_first:
                link_first[L] = u

    uniq = list(link_first.keys())
    if full or not per_scheme:
        selected = uniq
        mode = "full"
    else:
        selected = sample_links(uniq, per_scheme)
        mode = "sampled"

    # 按源首次贡献
    first_touch: dict[str, int] = {u: 0 for u in SOURCES}
    for L in selected:
        fs = link_first.get(L)
        if fs:
            first_touch[fs] = first_touch.get(fs, 0) + 1
    for m in meta:
        m["unique_first_touch"] = first_touch.get(m["url"], 0)
        m["overlap_only"] = max(0, int(m.get("uniq_in_source") or 0) - int(m["unique_first_touch"]))

    nodes = []
    for i, L in enumerate(selected):
        sch = L.split("://", 1)[0].lower()
        m = re.search(r"@([^:/?\s]+):(\d+)", L)
        srcs = link_all.get(L) or []
        first = link_first.get(L)
        nodes.append(
            {
                "id": f"public-{i}",
                "name": f"{sch}-{i}",
                "protocol": sch.replace("hy2", "hysteria2"),
                "uri": L,
                "share_link": L,
                "host": m.group(1) if m else None,
                "port": int(m.group(2)) if m else None,
                "source_urls": srcs,
                "first_source": first,
                "first_project": source_project(first) if first else None,
                "raw": {
                    "share_link": L,
                    "source": "public_sub",
                    "source_urls": srcs,
                    "first_source": first,
                    "first_project": source_project(first) if first else None,
                },
            }
        )

    # 项目聚合
    by_project: dict[str, dict] = {}
    for mrow in meta:
        proj = mrow["project"]
        bp = by_project.setdefault(
            proj,
            {"project": proj, "raw": 0, "uniq_in_source_sum": 0, "unique_first_touch": 0, "urls": []},
        )
        bp["raw"] += int(mrow.get("links") or 0)
        bp["uniq_in_source_sum"] += int(mrow.get("uniq_in_source") or 0)
        bp["unique_first_touch"] += int(mrow.get("unique_first_touch") or 0)
        bp["urls"].append(mrow["url"])

    return {
        "provider": "public_sub",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "sources": sorted(meta, key=lambda x: int(x.get("unique_first_touch") or 0), reverse=True),
        "by_project": sorted(by_project.values(), key=lambda x: int(x["unique_first_touch"]), reverse=True),
        "total_unique": len(uniq),
        "selected": len(selected),
        "sampled": len(selected),
        "mode": mode,
        "nodes": nodes,
        "notes": [
            "默认全量去重，不做抽样" if mode == "full" else f"限额抽样 per_scheme={per_scheme}",
            "unique_first_touch=按 SOURCES 顺序首次出现计入该源",
            "必须经 sing-box check + live 才算可用",
        ],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="公开订阅全量抓取（默认不抽样）")
    ap.add_argument("--out", type=Path, default=Path("analysis/findings/_public_sub_nodes.json"))
    ap.add_argument("--sample", action="store_true", help="不推荐：启用旧版按协议限额抽样")
    ap.add_argument("--summary-out", type=Path, default=Path("analysis/findings/_public_sub_by_source.json"))
    args = ap.parse_args()
    data = collect(full=not args.sample)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    summary = {
        "fetched_at": data["fetched_at"],
        "mode": data["mode"],
        "total_unique": data["total_unique"],
        "selected": data["selected"],
        "generated_note": "unique_first_touch=按 SOURCES 顺序首次出现时计入该源（去重归属）",
        "by_project": data.get("by_project") or [],
        "sources": data.get("sources") or [],
    }
    args.summary_out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "ok": True,
                "mode": data["mode"],
                "total_unique": data["total_unique"],
                "selected": data["selected"],
                "out": str(args.out),
                "summary": str(args.summary_out),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
