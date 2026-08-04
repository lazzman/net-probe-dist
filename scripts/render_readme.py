#!/usr/bin/env python3
"""根据 STATUS.json / dist/manifest.json 渲染 README（含更新时间、worker 状态与 Badge）。"""
from __future__ import annotations

import sys
from pathlib import Path as _PathForSys
sys.path.insert(0, str(_PathForSys(__file__).resolve().parent))

import argparse
import json
import os
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.parse import quote

CST = timezone(timedelta(hours=8))
REPO_DEFAULT = "lazzman/net-probe-dist"


def shield(label: str, message: str, color: str = "blue", logo: str | None = None) -> str:
    """生成 shields.io static badge Markdown。"""
    # shields 用 -- 转义
    def esc(s: str) -> str:
        return (
            str(s)
            .replace("-", "--")
            .replace("_", "__")
            .replace(" ", "_")
        )

    path = f"{esc(label)}-{esc(message)}-{color}"
    url = f"https://img.shields.io/badge/{quote(path, safe='-._')}"
    # quote may over-encode; shields prefers simple encoding
    # Use manual path for reliability
    from urllib.parse import quote as q

    lab = q(str(label).replace("-", "--").replace("_", "__").replace(" ", "_"), safe="")
    msg = q(str(message).replace("-", "--").replace("_", "__").replace(" ", "_"), safe="")
    url = f"https://img.shields.io/badge/{lab}-{msg}-{color}"
    if logo:
        url += f"?logo={logo}&logoColor=white"
    return f"![{label}: {message}]({url})"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", type=Path, default=Path("."))
    ap.add_argument("--repo", default=REPO_DEFAULT, help="owner/name")
    args = ap.parse_args()
    ws = args.workspace.resolve()
    repo = os.environ.get("GITHUB_REPOSITORY") or args.repo
    base = f"https://github.com/{repo}/releases/latest/download"
    rel = f"https://github.com/{repo}/releases/latest"
    actions = f"https://github.com/{repo}/actions/workflows/publish-dist.yml"
    badge_workflow = f"https://github.com/{repo}/actions/workflows/publish-dist.yml/badge.svg"
    badge_release = f"https://img.shields.io/github/v/release/{repo}?style=flat-square&label=release"
    badge_rel_date = f"https://img.shields.io/github/release-date/{repo}?style=flat-square&label=released"
    badge_downloads = f"https://img.shields.io/github/downloads/{repo}/total?style=flat-square&label=downloads"

    status_path = ws / "STATUS.json"
    status: dict = {}
    if status_path.exists():
        try:
            status = json.loads(status_path.read_text(encoding="utf-8"))
        except Exception:
            status = {}

    man: dict = {}
    for cand in (ws / "dist" / "manifest.json", ws / "nodes" / "subscription" / "manifest.json"):
        if cand.exists():
            try:
                man = json.loads(cand.read_text(encoding="utf-8"))
                break
            except Exception:
                pass

    sb = status.get("singbox") or {}
    sub = status.get("subscription") or {}
    worker = status.get("worker") or {}

    raw_updated = status.get("updated_at") or man.get("generated_at") or None
    try:
        from timeutil import to_shanghai_iso, to_shanghai_display, to_shanghai_badge, now_iso
        updated_display = to_shanghai_iso(raw_updated) if raw_updated else now_iso()
        updated_human = to_shanghai_display(raw_updated)
        updated_short = to_shanghai_badge(raw_updated)
    except Exception:
        updated = raw_updated or datetime.now(CST).isoformat(timespec="seconds")
        updated_display = str(updated)
        updated_human = updated_display.replace("+08:00", " CST").replace("+00:00", " UTC").replace("T", " ")[:19] + " (→请用上海时区)"
        # 尽力把 +00:00 转 +8
        try:
            s = str(updated).replace("Z", "+00:00")
            dt = datetime.fromisoformat(s)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            dt = dt.astimezone(CST)
            updated_display = dt.isoformat(timespec="seconds")
            updated_human = dt.strftime("%Y-%m-%d %H:%M:%S CST")
            updated_short = dt.strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            updated_short = updated_display.replace("T", " ")[:19]

    verified = sb.get("verified")
    public_unique = sb.get("public_unique")
    public_pass = sb.get("public_new_pass")
    public_fail = sb.get("public_fail")
    mode = sb.get("mode") or "accumulate_full_no_sample"
    retained_hist = sb.get("retained_history_pass")
    new_pass = sb.get("new_pass")
    hist_dropped = sb.get("history_dropped")
    prev_public = sb.get("previous_public")
    workers = worker.get("workers") or worker.get("count") or sb.get("workers")
    elapsed = worker.get("elapsed_sec") if worker.get("elapsed_sec") is not None else sb.get("elapsed_sec")
    conclusion = worker.get("conclusion") or status.get("conclusion") or "success"

    share_n = sub.get("share_link_count")
    if share_n is None:
        share_n = man.get("share_link_count")
    clash_n = sub.get("clash_proxy_count")
    if clash_n is None:
        clash_n = man.get("clash_proxy_count")
    by_proto = sub.get("by_protocol") or man.get("by_protocol") or {}
    by_country = sub.get("by_country") or (man.get("ip_enrich") or {}).get("by_country") or {}
    by_line_type = sub.get("by_line_type") or (man.get("ip_enrich") or {}).get("by_type") or {}

    def fmt(v):
        return "—" if v is None or v == "" else v

    def badge_val(v, suffix=""):
        if v is None or v == "" or v == "—":
            return "n/a"
        return f"{v}{suffix}"

    elapsed_s = f"{elapsed}s" if elapsed is not None else "n/a"
    conc_color = {
        "success": "brightgreen",
        "failure": "red",
        "cancelled": "lightgrey",
        "skipped": "yellow",
    }.get(str(conclusion).lower(), "blue")

    # dynamic status badges (static shields from current STATUS)
    b_update = shield("updated", updated_short, "informational", "github")
    b_workers = shield("workers", badge_val(workers), "blueviolet")
    b_result = shield("result", str(conclusion), conc_color, "githubactions")
    b_profiles = shield("profiles", badge_val(verified), "blue")
    b_pass = shield("live_hits", badge_val(public_pass), "brightgreen")
    b_fail = shield("live_fail", badge_val(public_fail), "orange")
    b_retained = shield("kept", badge_val(retained_hist), "blue")
    b_new = shield("new", badge_val(new_pass), "success")
    b_drop = shield("dropped", badge_val(hist_dropped), "important")
    b_elapsed = shield("elapsed", elapsed_s.replace(" ", "_"), "lightgrey")

    badges = f"""[![publish-dist]({badge_workflow})]({actions})
[![release]({badge_release})]({rel})
[![release-date]({badge_rel_date})]({rel})
[![downloads]({badge_downloads})]({rel})
{b_update}
{b_result}
{b_workers}
{b_elapsed}
{b_profiles}
{b_pass}
{b_fail}
{b_retained}
{b_new}
{b_drop}
"""

    readme = f"""# net-probe-dist

{badges}

Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `{updated_human}` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `{fmt(conclusion)}` |
| **Workers** | `{fmt(workers)}` |
| **Elapsed** | `{elapsed_s}` |
| **Probe mode** | `{fmt(mode)}` |
| **Candidates (unique)** | `{fmt(public_unique)}` |
| **Live PASS (pool hits)** | `{fmt(public_pass)}` |
| **Live FAIL** | `{fmt(public_fail)}` |
| **History retained** | `{fmt(retained_hist)}` |
| **New PASS** | `{fmt(new_pass)}` |
| **History dropped** | `{fmt(hist_dropped)}` |
| **Previous public** | `{fmt(prev_public)}` |
| **Published profiles (deduped)** | `{fmt(verified)}` |
| **Share links (exportable)** | `{fmt(share_n)}` |
| **YAML proxies (exportable)** | `{fmt(clash_n)}` |
| **Protocol mix** | `{json.dumps(by_proto, ensure_ascii=False)}` |
| **Country mix** | `{json.dumps(by_country, ensure_ascii=False)}` |
| **Line type mix** | `{json.dumps(by_line_type, ensure_ascii=False)}` |

### Number funnel

These fields are **not** the same quantity:

1. **Candidates (unique)** — 本轮公开订阅去重候选  
2. **Pool** — 候选 ∪ 历史 public（累积）；历史节点**每轮复测**  
3. **Live PASS / FAIL** — 对本轮 pool 的测活结果  
4. **History retained / New PASS / History dropped** — 累积账本：留下的老节点 / 新通过 / 被淘汰的老节点  
5. **Published profiles** — 指纹去重后的最终 outbound（`fslsb` / `outbounds.json`）  
6. **Share links / YAML** — 可导出分享链的节点（vless/ss/trojan/vmess/hysteria2）

Mode: **accumulate**（默认）= 累积 + 历史复测；`--fresh` = 仅本轮、不累积。

## Latest packages

| Code | Package | Latest link |
| --- | --- | --- |
| `fsl64` | encoded blob | {base}/fsl64 |
| `fslyaml` | YAML pack | {base}/fslyaml |
| `fslsb` | JSON runtime pack | {base}/fslsb |
| `fslyamlcomp` | legacy YAML pack | {base}/fslyamlcomp |
| manifest | build metadata | {base}/manifest.json |

Release page: {rel}

Swap the filename (`fsl64` → other code) to switch format.

### Split packages (geo / line type)

IP enrichment classifies each live node, then emits extra packs:

| Kind | Example asset | Meaning |
| --- | --- | --- |
| all | `fsl64` | everything |
| by country | `geo-US-fsl64` | countryCode=US |
| by type | `type-dc-fsl64` | datacenter/机房 |
| by type | `type-home-fsl64` | residential/家宽 |
| by type | `type-mobile-fsl64` | mobile |
| by type | `type-proxy-fsl64` | proxy |
| index | `splits.json` / `SPLITS.md` | full list + counts |

Same swap rule: `geo-US-fsl64` → `geo-US-fslyaml` / `geo-US-fslsb`.


## Automation

- Workflow: `publish-dist` (every 6 hours + manual)
- Uploads/clobbers assets on release tag `dist`
- Each run refreshes **Last update** + **Workers** badges/table on this README
- Git tree keeps code + status pointers only (no large blobs)

## Local

```bash
python3 scripts/ci_public_sub_pipeline.py --workspace . --workers 24
python3 scripts/render_readme.py --workspace .
# outputs under ./dist ; publish with:
#   gh release upload dist dist/fsl64 dist/fslyaml dist/fslsb dist/fslyamlcomp dist/manifest.json --clobber
```

## Safety

- No WireGuard private key files in releases
- Lab/CI artifacts only; may go stale
"""
    (ws / "README.md").write_text(readme, encoding="utf-8")

    dist_readme = f"""# dist (build output)

{b_update} {b_result} {b_workers}

Generated on the Actions runner / locally. **Published to GitHub Release**, not committed.

**Last update:** `{updated_human}`  
**Workers:** `{fmt(workers)}` · **Result:** `{fmt(conclusion)}`

Latest downloads:

- {base}/fsl64
- {base}/fslyaml
- {base}/fslsb
- {base}/fslyamlcomp
- {base}/manifest.json
"""
    dist = ws / "dist"
    dist.mkdir(parents=True, exist_ok=True)
    (dist / "README.md").write_text(dist_readme, encoding="utf-8")
    print(
        json.dumps(
            {
                "ok": True,
                "updated_at": updated_display,
                "workers": workers,
                "conclusion": conclusion,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
