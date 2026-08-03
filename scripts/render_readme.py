#!/usr/bin/env python3
"""根据 STATUS.json / dist/manifest.json 渲染 README（含更新时间与 worker 状态）。"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

CST = timezone(timedelta(hours=8))
REPO_DEFAULT = "lazzman/net-probe-dist"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", type=Path, default=Path("."))
    ap.add_argument("--repo", default=REPO_DEFAULT, help="owner/name")
    args = ap.parse_args()
    ws = args.workspace.resolve()
    import os
    repo = os.environ.get("GITHUB_REPOSITORY") or args.repo
    base = f"https://github.com/{repo}/releases/latest/download"
    rel = f"https://github.com/{repo}/releases/latest"

    status_path = ws / "STATUS.json"
    status = {}
    if status_path.exists():
        try:
            status = json.loads(status_path.read_text(encoding="utf-8"))
        except Exception:
            status = {}

    man = {}
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
    # 展示用：同时给 UTC 与 CST 若能解析
    updated_display = str(updated)

    verified = sb.get("verified")
    public_unique = sb.get("public_unique")
    public_pass = sb.get("public_new_pass")
    public_fail = sb.get("public_fail")
    mode = sb.get("mode") or "full_no_sample"
    source = sb.get("source") or "full_public_live_verify"
    workers = worker.get("workers") or worker.get("count")
    elapsed = worker.get("elapsed_sec")
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

    readme = f"""# net-probe-dist

Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `{updated_display}` |
| **Workflow result** | `{fmt(conclusion)}` |
| **Workers** | `{fmt(workers)}` |
| **Elapsed** | `{fmt(elapsed)}s` |
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
- Each run refreshes **Last update** + **Workers** on this README
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
    print(json.dumps({"ok": True, "updated_at": updated_display, "workers": workers, "conclusion": conclusion}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
