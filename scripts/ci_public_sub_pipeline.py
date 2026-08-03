#!/usr/bin/env python3
"""CI/定时：全量公开订阅抓取 → live 验证 → 多格式订阅 → 根目录 dist/ 发布副本。

供 GitHub Actions 每 6 小时调用；本地也可：
  python3 scripts/ci_public_sub_pipeline.py --workspace .
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def run(cmd: list[str], cwd: Path) -> None:
    print("+", " ".join(cmd), flush=True)
    r = subprocess.run(cmd, cwd=str(cwd))
    if r.returncode != 0:
        raise SystemExit(r.returncode)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", type=Path, default=Path("."))
    ap.add_argument("--workers", type=int, default=24)
    ap.add_argument("--skip-live", action="store_true", help="仅重导出（调试）")
    args = ap.parse_args()
    ws = args.workspace.resolve()
    py = sys.executable

    # 1) 全量抓取
    run(
        [
            py,
            str(ws / "analysis/findings/public_sub_fetch.py"),
            "--out",
            str(ws / "analysis/findings/_public_sub_nodes.json"),
            "--summary-out",
            str(ws / "analysis/findings/_public_sub_by_source.json"),
        ],
        ws,
    )

    # 2) 全量 live（fresh 覆盖 public）
    if not args.skip_live:
        run(
            [
                py,
                str(ws / "scripts/full_public_live_verify.py"),
                "--workspace",
                str(ws),
                "--workers",
                str(args.workers),
                "--fresh",
                "--nodes-json",
                str(ws / "analysis/findings/_public_sub_nodes.json"),
            ],
            ws,
        )

    # 3) 订阅导出
    run([py, str(ws / "scripts/export_subscription.py"), "--workspace", str(ws), "--no-wireguard-files", "--strip-wireguard-from-singbox"], ws)

    # 4) 按源汇总
    sum_script = ws / "scripts/summarize_public_sub_sources.py"
    if sum_script.exists():
        run([py, str(sum_script), "--workspace", str(ws)], ws)

    # 5) 发布到仓库根 dist/（方便 raw 订阅链接）
    src = ws / "nodes/subscription"
    dst = ws / "dist"
    dst.mkdir(parents=True, exist_ok=True)
    mapping = {
        # 对外只暴露中性关键字，避免订阅/协议观感
        "fsl64": "fsl64",
        "fslyaml": "fslyaml",
        "fslsb": "fslsb",
        "fslyamlcomp": "fslyamlcomp",
        "manifest.json": "manifest.json",
    }
    for a, b in mapping.items():
        sp = src / a
        if sp.exists():
            shutil.copy2(sp, dst / b)
    # 公开仓禁止发布 wireguard 私钥 conf
    wg_dst = dst / "wireguard"
    if wg_dst.exists():
        shutil.rmtree(wg_dst)

    # 发布说明
    man = {}
    mp = src / "manifest.json"
    if mp.exists():
        man = json.loads(mp.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc).astimezone().isoformat()
    readme = f"""# Probe export packages

Automated **reachability probe** exports for lab/CI use.

Refresh: about every 6 hours via GitHub Actions.

## Profile codes

Base:

```text
https://raw.githubusercontent.com/<OWNER>/<REPO>/main/dist/fsl64
```

| Code | Package |
| --- | --- |
| `fsl64` | encoded profile blob |
| `fslyaml` | YAML profile pack |
| `fslsb` | JSON runtime pack |
| `fslyamlcomp` | legacy YAML pack |

Swap the last path segment (`fsl64` → other code) to switch package type.

## Notes

- Outputs are machine-generated connectivity check artifacts.
- No WireGuard private key files are published.
- Stability is not guaranteed; lab use only.
"""
    (dst / "README.md").write_text(readme, encoding="utf-8")

    # 根 STATUS
    sb_man = {}
    smp = ws / "nodes/sing-box/manifest.json"
    if smp.exists():
        sb_man = json.loads(smp.read_text(encoding="utf-8"))
    status = {
        "updated_at": now,
        "conclusion": "success",
        "subscription": {
            "share_link_count": man.get("share_link_count"),
            "clash_proxy_count": man.get("clash_proxy_count"),
            "by_protocol": man.get("by_protocol"),
        },
        "singbox": {
            "verified": sb_man.get("singbox_outbounds_verified"),
            "public_unique": sb_man.get("public_unique"),
            "public_new_pass": sb_man.get("public_new_pass"),
            "public_fail": sb_man.get("public_fail"),
            "mode": sb_man.get("mode"),
            "source": sb_man.get("source"),
            "tested": sb_man.get("tested"),
            "elapsed_sec": sb_man.get("elapsed_sec"),
            "workers": sb_man.get("workers"),
        },
        "worker": {
            "workers": sb_man.get("workers") if sb_man.get("workers") is not None else args.workers,
            "elapsed_sec": sb_man.get("elapsed_sec"),
            "tested": sb_man.get("tested"),
            "pass": sb_man.get("public_new_pass"),
            "fail": sb_man.get("public_fail"),
            "conclusion": "success",
        },
    }
    (ws / "STATUS.json").write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # 刷新 README 更新时间与 worker 状态
    render = ws / "scripts" / "render_readme.py"
    if render.exists():
        subprocess.run([py, str(render), "--workspace", str(ws)], check=False)
    print(json.dumps(status, ensure_ascii=False, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
