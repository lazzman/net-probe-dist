#!/usr/bin/env python3
"""汇总公开订阅：每源/每项目 候选数 vs live 可用数。"""
from __future__ import annotations

import sys
from pathlib import Path as _PathForSys
sys.path.insert(0, str(_PathForSys(__file__).resolve().parent))

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


def _now_sh() -> str:
    try:
        from timeutil import now_iso
        return now_iso()
    except Exception:
        from datetime import datetime, timezone, timedelta
        return datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")


def project_of(url: str) -> str:
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


def outbound_key(o: dict[str, Any]) -> str | None:
    t = (o.get("type") or "").lower()
    server = o.get("server")
    port = o.get("server_port")
    if not server or not port:
        return None
    if t == "vless":
        return f"vless:{server}:{port}:{o.get('uuid') or ''}"
    if t == "trojan":
        return f"trojan:{server}:{port}:{o.get('password') or ''}"
    if t in ("ss", "shadowsocks"):
        return f"ss:{server}:{port}:{o.get('method') or ''}:{o.get('password') or ''}"
    if t == "vmess":
        return f"vmess:{server}:{port}:{o.get('uuid') or ''}"
    if t in ("hysteria2", "hysteria"):
        return f"hysteria2:{server}:{port}:{o.get('password') or ''}"
    return f"{t}:{server}:{port}"


def node_key(n: dict[str, Any]) -> str | None:
    """从 share_link/host 尽量对齐 outbound_key（粗匹配：host:port+proto）。"""
    uri = n.get("share_link") or n.get("uri") or ""
    proto = (n.get("protocol") or "").lower().replace("hy2", "hysteria2")
    host = n.get("host")
    port = n.get("port")
    if not host or not port:
        m = re.search(r"@([^:/?\s]+):(\d+)", uri)
        if m:
            host, port = m.group(1), int(m.group(2))
    if not host or not port:
        return None
    # 细匹配需要 uuid/password，从 URI 抽
    if proto == "vless" and uri.startswith("vless://"):
        user = uri[8:].split("@", 1)[0]
        return f"vless:{host}:{port}:{user}"
    if proto == "trojan" and "trojan://" in uri:
        user = uri.split("trojan://", 1)[1].split("@", 1)[0]
        return f"trojan:{host}:{port}:{user}"
    if proto in ("ss", "shadowsocks"):
        return f"ss:{host}:{port}:"  # method/password 在 outbound 更完整；下面用 hostport fallback
    if proto == "vmess":
        return f"vmess:{host}:{port}:"
    if proto in ("hysteria2", "hysteria"):
        user = ""
        if "://" in uri:
            user = uri.split("://", 1)[1].split("@", 1)[0]
        return f"hysteria2:{host}:{port}:{user}"
    return f"{proto}:{host}:{port}"


def hostport_key(proto: str, host: str, port: int) -> str:
    return f"{proto}:{host}:{port}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", type=Path, default=Path("."))
    ap.add_argument("--nodes-json", type=Path, default=None)
    ap.add_argument("--outbounds", type=Path, default=None)
    ap.add_argument("--out-json", type=Path, default=None)
    ap.add_argument("--out-md", type=Path, default=None)
    args = ap.parse_args()
    ws = args.workspace.resolve()
    nodes_path = (args.nodes_json or (ws / "analysis/findings/_public_sub_nodes.json")).resolve()
    ob_path = (args.outbounds or (ws / "nodes/sing-box/outbounds.json")).resolve()
    out_json = (args.out_json or (ws / "analysis/findings/_public_sub_source_availability.json")).resolve()
    out_md = (args.out_md or (ws / "analysis/findings/_public_sub_source_summary.md")).resolve()

    nodes_data = json.loads(nodes_path.read_text(encoding="utf-8")) if nodes_path.exists() else {}
    nodes = nodes_data.get("nodes") or []
    sources_meta = nodes_data.get("sources") or []
    by_project_meta = nodes_data.get("by_project") or []

    # 旧 nodes 可能无 first_source：回退 by_source 汇总文件
    by_source_path = ws / "analysis/findings/_public_sub_by_source.json"
    if (not any(n.get("first_source") for n in nodes[:50])) and by_source_path.exists():
        try:
            bs = json.loads(by_source_path.read_text(encoding="utf-8"))
            if bs.get("sources") and not sources_meta:
                sources_meta = bs["sources"]
            if bs.get("by_project") and not by_project_meta:
                by_project_meta = bs["by_project"]
            if bs.get("sources") and not any(n.get("first_source") for n in nodes[:20]):
                # 仅用 meta 填候选表；live 匹配仍尽量做
                pass
        except Exception:
            pass

    outbounds = json.loads(ob_path.read_text(encoding="utf-8")) if ob_path.exists() else []
    public_obs = [o for o in outbounds if str(o.get("tag") or "").startswith("public_sub")]

    # index outbounds
    ob_keys = {}
    ob_hostport = defaultdict(list)
    for o in public_obs:
        k = outbound_key(o)
        if k:
            ob_keys[k] = o
        t = (o.get("type") or "").lower()
        if t == "shadowsocks":
            t = "ss"
        if o.get("server") and o.get("server_port"):
            ob_hostport[hostport_key(t, str(o["server"]), int(o["server_port"]))].append(o)

    # per source / project stats
    src_cand = Counter()
    src_pass = Counter()
    proj_cand = Counter()
    proj_pass = Counter()
    matched_pass_tags = set()

    for n in nodes:
        srcs = n.get("source_urls") or ([n["first_source"]] if n.get("first_source") else [])
        first = n.get("first_source") or (srcs[0] if srcs else None)
        proj = n.get("first_project") or (project_of(first) if first else "unknown")
        if first:
            src_cand[first] += 1
        proj_cand[proj] += 1

        # match available
        proto = (n.get("protocol") or "").lower().replace("hy2", "hysteria2")
        if proto == "shadowsocks":
            proto = "ss"
        host, port = n.get("host"), n.get("port")
        hit = None
        nk = node_key(n)
        if nk and nk in ob_keys:
            hit = ob_keys[nk]
        elif nk:
            # ss/vmess partial key
            for ok, o in ob_keys.items():
                if ok.startswith(nk) or (host and port and ok.startswith(f"{proto}:{host}:{port}")):
                    hit = o
                    break
        if not hit and host and port:
            lst = ob_hostport.get(hostport_key(proto, str(host), int(port))) or []
            if len(lst) == 1:
                hit = lst[0]
            elif lst:
                hit = lst[0]
        if hit:
            tag = hit.get("tag")
            if tag not in matched_pass_tags:
                matched_pass_tags.add(tag)
            # 可用归属：计 first_source；也给所有 source_urls 记出现（可选只 first）
            if first:
                src_pass[first] += 1
            proj_pass[proj] += 1

    # merge with sources_meta for raw fields
    meta_by_url = {m.get("url"): m for m in sources_meta if m.get("url")}
    source_rows = []
    all_urls = set(src_cand) | set(meta_by_url)
    for u in all_urls:
        m = meta_by_url.get(u) or {}
        cand = src_cand.get(u, 0)
        if not cand:
            cand = int(m.get("unique_first_touch") or 0)
        source_rows.append(
            {
                "url": u,
                "project": m.get("project") or project_of(u),
                "status": m.get("status"),
                "raw": m.get("links") or m.get("raw"),
                "uniq_in_source": m.get("uniq_in_source"),
                "unique_first_touch": m.get("unique_first_touch", cand),
                "candidates": cand,
                "live_pass": src_pass.get(u, 0),
            }
        )
    source_rows.sort(key=lambda x: (int(x.get("live_pass") or 0), int(x.get("candidates") or 0)), reverse=True)

    project_rows = []
    # prefer by_project_meta candidacy
    proj_meta = {p["project"]: p for p in by_project_meta if p.get("project")}
    proj_keys = set(proj_cand) | set(proj_pass) | set(proj_meta)
    # 若节点无归属，用 meta 项目列表
    if not any(n.get("first_project") or n.get("first_source") for n in nodes[:30]):
        proj_keys |= set(proj_meta.keys())
    for proj in sorted(proj_keys, key=lambda p: -(proj_pass.get(p, 0) * 100000 + (proj_cand.get(p, 0) or int((proj_meta.get(p) or {}).get("unique_first_touch") or 0)))):
        pm = proj_meta.get(proj) or {}
        cand = proj_cand.get(proj, 0) or int(pm.get("unique_first_touch") or 0)
        project_rows.append(
            {
                "project": proj,
                "raw": pm.get("raw"),
                "unique_first_touch": pm.get("unique_first_touch", cand),
                "candidates": cand,
                "live_pass": proj_pass.get(proj, 0),
            }
        )

    # provider-level
    providers = {
        "public_sub": {
            "candidates": len(nodes) or nodes_data.get("total_unique"),
            "live_pass_matched": len(matched_pass_tags),
            "live_pass_outbounds_public_tags": len(public_obs),
        }
    }

    report = {
        "generated_at": (lambda: (__import__('timeutil', fromlist=['now_iso']).now_iso() if True else datetime.now().astimezone().isoformat()))(),
        "nodes_json": str(nodes_path),
        "outbounds": str(ob_path),
        "mode": nodes_data.get("mode"),
        "total_unique": nodes_data.get("total_unique") or len(nodes),
        "public_outbounds": len(public_obs),
        "matched_pass_tags": len(matched_pass_tags),
        "providers": providers,
        "by_project": project_rows,
        "by_source": source_rows,
        "note": "live_pass 按 first_source 归属；匹配依赖 host/port/凭证字段，可能略低于 public outbound 总数",
    }
    out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# 公开订阅：候选 vs 可用（按项目/源）",
        "",
        f"> 生成：{report['generated_at']}",
        f"> 模式：{report.get('mode')}；全局去重候选：**{report['total_unique']}**",
        f"> public outbound 可用标签：**{len(public_obs)}**（匹配归属 **{len(matched_pass_tags)}**）",
        "",
        "## 说明",
        "",
        "- 候选来自公开订阅镜像全量去重（**不抽样**）。",
        "- 入仓 App（Sherd/NovaLink）通常只是硬编码这些公开源，不是私有节点池。",
        "- `live_pass`：sing-box live 通过后，按 `first_source` 归属到源/项目。",
        "",
        "## 按项目（去重首次贡献 / 可用）",
        "",
        "| 项目 | 候选(首次) | live 可用 | raw约 |",
        "| --- | ---: | ---: | ---: |",
    ]
    for r in project_rows:
        lines.append(
            f"| `{r['project']}` | {r.get('candidates') or r.get('unique_first_touch') or 0} | {r.get('live_pass') or 0} | {r.get('raw') if r.get('raw') is not None else '-'} |"
        )
    lines += [
        "",
        "## 按订阅 URL",
        "",
        "| live可用 | 候选 | 源内去重 | 原始 | URL |",
        "| ---: | ---: | ---: | ---: | --- |",
    ]
    for r in source_rows:
        if not (r.get("candidates") or r.get("live_pass") or r.get("raw")):
            continue
        lines.append(
            f"| {r.get('live_pass') or 0} | {r.get('candidates') or 0} | {r.get('uniq_in_source') if r.get('uniq_in_source') is not None else '-'} | {r.get('raw') if r.get('raw') is not None else '-'} | `{r['url']}` |"
        )
    lines += [
        "",
        f"JSON：`{out_json}`",
        "",
    ]
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "ok": True,
                "total_unique": report["total_unique"],
                "public_outbounds": len(public_obs),
                "matched": len(matched_pass_tags),
                "out_json": str(out_json),
                "out_md": str(out_md),
                "top_projects": project_rows[:5],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
