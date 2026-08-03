#!/usr/bin/env python3
"""公开订阅全量 live 验证：不抽样，全部去重链接并行实测。"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from typing import Any


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


def fp(o: dict[str, Any]) -> str:
    t = (o.get("type") or "").lower()
    return f"{t}:{(o.get('server') or '')}:{(o.get('server_port') or '')}:{(o.get('uuid') or o.get('password') or o.get('method') or '')}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", type=Path, default=Path("."))
    ap.add_argument(
        "--workers",
        type=int,
        default=0,
        help="并行 live 探测数；0=自动（约 CPU*3，上限 48，GitHub Actions 建议 16~24）",
    )
    ap.add_argument("--resume", action="store_true", help="跳过已在 outbounds.json 的指纹")
    ap.add_argument("--progress-every", type=int, default=50)
    ap.add_argument("--nodes-json", type=Path, default=None, help="已有全量 nodes JSON，跳过重新抓取")
    ap.add_argument("--fresh", action="store_true", help="忽略已有 outbounds，本轮 PASS 全量覆盖 public 结果")
    args = ap.parse_args()
    if not args.workers or args.workers <= 0:
        import os
        cpu = os.cpu_count() or 4
        # I/O/进程型：可高于核数；单任务会起 sing-box 子进程，需防 OOM
        args.workers = max(8, min(48, cpu * 3))
    ws = args.workspace.resolve()
    export = load(ws / "scripts/export_singbox.py", "export_singbox")
    pub = load(ws / "analysis/findings/public_sub_fetch.py", "public_sub_fetch")
    bin_path = export.resolve_singbox_bin(None)
    if not bin_path:
        print("未找到 sing-box", file=sys.stderr)
        return 2

    out_dir = ws / "nodes/sing-box"
    out_dir.mkdir(parents=True, exist_ok=True)
    state_path = out_dir / "full_public_live_state.json"
    prev = []
    if (out_dir / "outbounds.json").exists():
        prev = json.loads((out_dir / "outbounds.json").read_text(encoding="utf-8"))
    if args.fresh:
        prev = [o for o in prev if not str(o.get("tag") or "").startswith("public_sub")]
        # fresh：仍可保留非 public（yptun/free_vpn）；public 仅本轮 PASS
        prev_fp = set()
    else:
        prev_fp = {fp(o) for o in prev} if args.resume else set()

    t0 = time.time()
    if args.nodes_json and args.nodes_json.exists():
        print(f"[*] load existing full nodes: {args.nodes_json}", flush=True)
        data = json.loads(args.nodes_json.read_text(encoding="utf-8"))
    else:
        print("[*] collect public_sub FULL (no sample)", flush=True)
        data = pub.collect(full=True)
        (ws / "analysis/findings/_public_sub_nodes.json").write_text(
            json.dumps(data, ensure_ascii=False), encoding="utf-8"
        )
    (ws / "analysis/findings/_public_sub_nodes_full.json").write_text(
        json.dumps(
            {
                **{k: v for k, v in data.items() if k != "nodes"},
                "nodes_count": len(data.get("nodes") or []),
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(
        f"    unique={data.get('total_unique')} selected={data.get('selected') or len(data.get('nodes') or [])} "
        f"mode={data.get('mode', 'full')} load_s={time.time()-t0:.1f}",
        flush=True,
    )

    report = {
        "providers": [
            {
                "provider": "public_sub",
                "app": "Public subscription FULL",
                "nodes": data.get("nodes") or [],
                "http_status": 200,
            }
        ]
    }
    print("[*] convert share links -> outbounds", flush=True)
    cands, _, notes = export.collect_from_report(report, ws / "analysis/findings")
    print(f"    convertible={len(cands)} notes={len(notes)}", flush=True)

    to_test = []
    skipped = 0
    for ob in cands:
        if args.resume and fp(ob) in prev_fp:
            skipped += 1
            continue
        to_test.append(ob)
    print(f"[*] to_test={len(to_test)} resume_skip={skipped} workers={args.workers}", flush=True)

    passed: list[dict[str, Any]] = []
    failed: list[dict[str, Any]] = []
    done = 0
    lock_stats = {"pass": 0, "fail": 0}

    def probe_one(ob: dict[str, Any]) -> tuple[bool, dict[str, Any], dict[str, Any]]:
        ok, info = export.singbox_live_probe(bin_path, ob)
        return ok, ob, info

    t1 = time.time()
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as ex:
        futs = {ex.submit(probe_one, ob): ob for ob in to_test}
        for fut in as_completed(futs):
            ok, ob, info = fut.result()
            done += 1
            tag = ob.get("tag")
            meta = dict(ob.get("_meta") or {})
            meta["singbox_validation"] = info
            ob2 = dict(ob)
            ob2["_meta"] = meta
            if ok:
                passed.append(ob2)
                lock_stats["pass"] += 1
                print(f"[{done}/{len(to_test)}] PASS {tag} http={info.get('http_code')}", flush=True)
            else:
                failed.append(
                    {
                        "tag": tag,
                        "provider": meta.get("provider"),
                        "validation": {
                            "stage": info.get("stage"),
                            "http_code": info.get("http_code"),
                            "detail": str(info.get("detail") or "")[:200],
                        },
                    }
                )
                lock_stats["fail"] += 1
                if done % args.progress_every == 0 or done == len(to_test):
                    rate = done / max(time.time() - t1, 1)
                    eta = (len(to_test) - done) / max(rate, 0.01)
                    print(
                        f"[{done}/{len(to_test)}] progress pass={lock_stats['pass']} fail={lock_stats['fail']} "
                        f"{rate:.2f}/s eta={eta/60:.1f}m",
                        flush=True,
                    )
            if done % 200 == 0:
                state = {
                    "done": done,
                    "total": len(to_test),
                    "pass": lock_stats["pass"],
                    "fail": lock_stats["fail"],
                    "updated_at": datetime.now().astimezone().isoformat(),
                }
                state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # merge with previous non-public kept + new passes + previous public that still wanted
    # Keep all previous verified (yptun/free_vpn/public), add new public passes
    merged: list[dict[str, Any]] = []
    seen_fp: set[str] = set()
    seen_tag: set[str] = set()
    keep_prev = prev
    if args.fresh:
        keep_prev = [o for o in prev if not str(o.get("tag") or "").startswith("public_sub")]
    for o in export.strip_meta(passed) + keep_prev:
        f = fp(o)
        tg = o.get("tag")
        if not tg or f in seen_fp or tg in seen_tag:
            continue
        seen_fp.add(f)
        seen_tag.add(tg)
        merged.append(o)

    config = export.build_singbox_config(merged, mixed_port=2080)
    (out_dir / "config.json").write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    ok, msg = export.singbox_check(bin_path, out_dir / "config.json")
    print(f"[*] final check {'PASS' if ok else 'FAIL'}", flush=True)
    if not ok:
        print(msg[-500:], file=sys.stderr)
        return 3
    (out_dir / "outbounds.json").write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "outbounds.failed.full_public.json").write_text(
        json.dumps(failed, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    man = {
        "generated_at": datetime.now().astimezone().isoformat(),
        "source": "full_public_live_verify",
        "mode": "full_no_sample",
        "public_unique": data.get("total_unique"),
        "public_selected": data.get("selected"),
        "convertible": len(cands),
        "tested": len(to_test),
        "resume_skip": skipped,
        "public_new_pass": lock_stats["pass"],
        "public_fail": lock_stats["fail"],
        "previous_verified": len(prev),
        "singbox_outbounds_verified": len(merged),
        "outbound_tags": [o.get("tag") for o in merged],
        "outbound_types": sorted({o.get("type") for o in merged if o.get("type")}),
        "final_config_check": True,
        "workers": args.workers,
        "elapsed_sec": round(time.time() - t0, 1),
        "test_url": "https://www.gstatic.com/generate_204",
    }
    (out_dir / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: man[k] for k in man if k != "outbound_tags"}, ensure_ascii=False, indent=2), flush=True)

    # 按源汇总候选/可用 + 导出订阅
    try:
        import subprocess
        sum_script = ws / "scripts/summarize_public_sub_sources.py"
        if sum_script.exists():
            print("[*] summarize public_sub by source", flush=True)
            subprocess.run([sys.executable, str(sum_script), "--workspace", str(ws)], check=False)
        sub_script = ws / "scripts/export_subscription.py"
        if sub_script.exists():
            print("[*] export subscription", flush=True)
            subprocess.run([sys.executable, str(sub_script), "--workspace", str(ws)], check=False)
    except Exception as e:
        print(f"[!] post steps: {e}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
