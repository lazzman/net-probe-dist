#!/usr/bin/env python3
"""根据 STATUS.json / dist/manifest.json 渲染 README（含更新时间、worker 状态与 Badge）。"""
from __future__ import annotations

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

    updated = status.get("updated_at") or man.get("generated_at") or datetime.now(CST).isoformat()
    updated_display = str(updated)
    # 短时间用于 badge（避免特殊字符）
    updated_short = updated_display.replace("+08:00", " CST").replace("T", " ")[:19]

    verified = sb.get("verified")
    public_unique = sb.get("public_unique")
    public_pass = sb.get("public_new_pass")
    public_fail = sb.get("public_fail")
    mode = sb.get("mode") or "full_no_sample"
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

    def fmt(v):
        return "—" if v is None or v == "" else v

    elapsed_s = f"{elapsed}s" if elapsed is not None else "—"
    conc_color = {
        "success": "brightgreen",
        "failure": "red",
        "cancelled": "lightgrey",
        "skipped": "yellow",
    }.get(str(conclusion).lower(), "blue")

    # dynamic status badges (static shields from current STATUS)
    b_update = shield("updated", updated_short, "informational", "github")
    b_workers = shield("workers", str(fmt(workers)), "blueviolet", "//")
    b_result = shield("result", str(conclusion), conc_color, "githubactions")
    b_profiles = shield("profiles", str(fmt(verified)), "blue")
    b_pass = shield("live_pass", str(fmt(public_pass)), "brightgreen")
    b_fail = shield("live_fail", str(fmt(public_fail)), "orange")
    b_elapsed = shield("elapsed", elapsed_s.replace(" ", ""), "lightgrey")

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
"""

    readme = f"""# net-probe-dist

{badges}

Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `{updated_display}` |
| **Workflow result** | `{fmt(conclusion)}` |
| **Workers** | `{fmt(workers)}` |
| **Elapsed** | `{elapsed_s}` |
| **Probe mode** | `{fmt(mode)}` |
| **Candidates (unique)** | `{fmt(public_unique)}` |
| **Live PASS (raw)** | `{fmt(public_pass)}` |
| **Live FAIL** | `{fmt(public_fail)}` |
| **Published profiles** | `{fmt(verified)}` |
| **Share links** | `{fmt(share_n)}` |
| **YAML proxies** | `{fmt(clash_n)}` |
| **Protocol mix** | `{json.dumps(by_proto, ensure_ascii=False)}` |

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

**Last update:** `{updated_display}`  
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
