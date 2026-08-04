#!/usr/bin/env python3
"""公开订阅全量 live 验证：不抽样。

默认 **accumulate（累积 + 历史复测）**：
- 本轮公开订阅全量候选
- 并入上一轮已验证 public 节点（本地 outbounds 或 Release 种子）
- **历史 PASS 每轮重新测活**；不通则淘汰，通则保留
- 新 PASS 并入累积池

`--fresh`：忽略历史 public，仅本轮 PASS（旧行为）。
`--resume`：跳过已有指纹（不复测，仅调试加速；CI 不用）。
"""
from __future__ import annotations

import sys
from pathlib import Path as _PathForSys
sys.path.insert(0, str(_PathForSys(__file__).resolve().parent))

import argparse
import importlib.util
import json
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any


def _now_sh() -> str:
    try:
        from timeutil import now_iso
        return now_iso()
    except Exception:
        return datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


def fp(o: dict[str, Any]) -> str:
    t = (o.get("type") or "").lower()
    return (
        f"{t}:{(o.get('server') or '')}:{(o.get('server_port') or '')}:"
        f"{(o.get('uuid') or o.get('password') or o.get('method') or '')}"
    )


def is_public_outbound(o: dict[str, Any]) -> bool:
    tag = str(o.get("tag") or "")
    provider = str((o.get("_meta") or {}).get("provider") or "")
    return tag.startswith("public_sub") or provider == "public_sub"


def clean_outbound(o: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in o.items() if not str(k).startswith("_")}


def load_seed_outbounds(url: str) -> list[dict[str, Any]]:
    """从上一轮 Release 的 fslsb/outbounds 种子加载历史 PASS。"""
    print(f"[*] seed previous verified from: {url}", flush=True)
    req = urllib.request.Request(url, headers={"User-Agent": "net-probe-dist-accumulate/1.0"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        raw = resp.read()
    # outbounds.json 纯列表，或 fslsb 配置
    data = json.loads(raw.decode("utf-8", "replace"))
    skip_types = {"selector", "urltest", "direct", "block", "dns"}
    if isinstance(data, list):
        obs = data
    elif isinstance(data, dict):
        obs = list(data.get("outbounds") or [])
    else:
        obs = []
    out: list[dict[str, Any]] = []
    for o in obs:
        if not isinstance(o, dict):
            continue
        if o.get("type") in skip_types:
            continue
        if not o.get("server"):
            continue
        out.append(clean_outbound(o))
    print(f"    seed_outbounds={len(out)}", flush=True)
    return out


def default_seed_url() -> str | None:
    repo = os.environ.get("GITHUB_REPOSITORY") or "lazzman/net-probe-dist"
    # 优先专用 outbounds 资产；没有则用 fslsb
    return f"https://github.com/{repo}/releases/latest/download/outbounds.json"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", type=Path, default=Path("."))
    ap.add_argument(
        "--workers",
        type=int,
        default=0,
        help="并行 live 探测数；0=自动（约 CPU*3，上限 48，GitHub Actions 建议 16~32）",
    )
    ap.add_argument("--resume", action="store_true", help="跳过已在 outbounds.json 的指纹（不复测；CI 勿用）")
    ap.add_argument("--progress-every", type=int, default=50)
    ap.add_argument("--nodes-json", type=Path, default=None, help="已有全量 nodes JSON，跳过重新抓取")
    ap.add_argument(
        "--fresh",
        action="store_true",
        help="忽略历史 public，仅保留本轮 PASS（非累积）",
    )
    ap.add_argument(
        "--accumulate",
        action="store_true",
        default=False,
        help="累积模式（默认）：历史 public 并入候选并复测",
    )
    ap.add_argument(
        "--no-seed-release",
        action="store_true",
        help="不从 GitHub Release 拉取历史 PASS 种子（仅用本地 outbounds）",
    )
    ap.add_argument(
        "--seed-url",
        default=None,
        help="历史 PASS 种子 URL（默认 latest/outbounds.json，失败再试 fslsb）",
    )
    args = ap.parse_args()

    # 默认累积；显式 --fresh 则非累积
    mode = "fresh" if args.fresh else "accumulate"
    if args.accumulate:
        mode = "accumulate"
    if args.resume and mode == "accumulate":
        print("[!] --resume 与累积复测冲突：累积模式下忽略 resume，强制复测历史", flush=True)
        args.resume = False

    if not args.workers or args.workers <= 0:
        cpu = os.cpu_count() or 4
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

    prev: list[dict[str, Any]] = []
    if (out_dir / "outbounds.json").exists():
        try:
            prev = json.loads((out_dir / "outbounds.json").read_text(encoding="utf-8"))
            if not isinstance(prev, list):
                prev = []
        except Exception:
            prev = []

    # 累积模式：CI 无本地历史时，从 Release 种子回填上一轮 PASS
    seed_count = 0
    if mode == "accumulate" and not args.no_seed_release:
        local_public = [o for o in prev if isinstance(o, dict) and is_public_outbound(o)]
        if len(local_public) < 10:
            urls: list[str] = []
            if args.seed_url:
                urls.append(args.seed_url)
            else:
                repo = os.environ.get("GITHUB_REPOSITORY") or "lazzman/net-probe-dist"
                urls.append(f"https://github.com/{repo}/releases/latest/download/outbounds.json")
                urls.append(f"https://github.com/{repo}/releases/latest/download/fslsb")
            seeded: list[dict[str, Any]] = []
            for u in urls:
                try:
                    seeded = load_seed_outbounds(u)
                    if seeded:
                        break
                except Exception as e:
                    print(f"    seed failed {u}: {e}", flush=True)
            if seeded:
                # 标记为 public 以便 is_public；保留原 tag
                for o in seeded:
                    if not str(o.get("tag") or "").startswith("public_sub"):
                        # 来自 fslsb 的 public 通常已是 public_sub_*
                        pass
                    meta = dict(o.get("_meta") or {})
                    meta.setdefault("provider", "public_sub")
                    meta["seeded_from_release"] = True
                    o["_meta"] = meta
                # 合并进 prev（按 fp，本地优先）
                by = {fp(o): o for o in prev if isinstance(o, dict) and o.get("server")}
                for o in seeded:
                    f = fp(o)
                    if f not in by:
                        by[f] = o
                        seed_count += 1
                prev = list(by.values())
                print(f"[*] seeded_new_fps={seed_count} prev_total={len(prev)}", flush=True)

    if mode == "fresh":
        # 丢掉历史 public，仅保留非 public（若有）
        prev_keep_nonpublic = [o for o in prev if isinstance(o, dict) and not is_public_outbound(o)]
        prev_public: list[dict[str, Any]] = []
        prev = prev_keep_nonpublic
        prev_fp_skip: set[str] = set()
    else:
        prev_public = [o for o in prev if isinstance(o, dict) and is_public_outbound(o)]
        prev_fp_skip = {fp(o) for o in prev} if args.resume else set()

    prev_other = [o for o in prev if isinstance(o, dict) and not is_public_outbound(o)]
    prev_public_fps = {fp(o) for o in prev_public}

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
        f"fetch_mode={data.get('mode', 'full')} verify_mode={mode} load_s={time.time()-t0:.1f}",
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

    # 候选池：当前抓取 ∪ 历史 public（历史-only 也要复测）
    pool: dict[str, dict[str, Any]] = {}
    for ob in cands:
        if not isinstance(ob, dict):
            continue
        f = fp(ob)
        if not f or f.startswith(":"):
            continue
        pool[f] = ob  # 当前抓取优先

    hist_only = 0
    if mode == "accumulate":
        for ob in prev_public:
            f = fp(ob)
            if not f or f in pool:
                continue
            # 历史独有：用上一轮 outbound 结构复测
            ob2 = clean_outbound(ob)
            meta = {"provider": "public_sub", "source": "history_retest"}
            ob2["_meta"] = meta
            if not ob2.get("tag"):
                ob2["tag"] = f"public_sub_hist_{len(pool)}"
            pool[f] = ob2
            hist_only += 1

    to_test: list[dict[str, Any]] = []
    skipped = 0
    for f, ob in pool.items():
        if args.resume and f in prev_fp_skip:
            skipped += 1
            continue
        to_test.append(ob)

    print(
        f"[*] to_test={len(to_test)} pool={len(pool)} hist_only={hist_only} "
        f"prev_public={len(prev_public)} resume_skip={skipped} workers={args.workers} mode={mode}",
        flush=True,
    )

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
            meta["verified_at"] = _now_sh()
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
                        "fp": fp(ob),
                        "history": fp(ob) in prev_public_fps,
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
                    "mode": mode,
                    "updated_at": _now_sh(),
                }
                state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    passed_fps = {fp(o) for o in passed}
    retained_hist = sum(1 for f in passed_fps if f in prev_public_fps)
    new_pass = sum(1 for f in passed_fps if f not in prev_public_fps)
    hist_dropped = sum(1 for f in prev_public_fps if f not in passed_fps)

    # 公开节点：只保留本轮测活 PASS（含历史复测通过 + 新 PASS）
    # 非 public：仍原样保留（体量通常很小）
    merged: list[dict[str, Any]] = []
    seen_fp: set[str] = set()
    seen_tag: set[str] = set()
    for o in export.strip_meta(passed) + prev_other:
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

    # 写出纯 outbounds，供下轮累积种子 / Release 资产
    (out_dir / "outbounds.json").write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "outbounds.failed.full_public.json").write_text(
        json.dumps(failed, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    man = {
        "generated_at": _now_sh(),
        "source": "full_public_live_verify",
        "mode": f"{mode}_full_no_sample",
        "accumulate": mode == "accumulate",
        "public_unique": data.get("total_unique"),
        "public_selected": data.get("selected"),
        "convertible": len(cands),
        "pool_size": len(pool),
        "hist_only": hist_only,
        "seed_new_fps": seed_count,
        "tested": len(to_test),
        "resume_skip": skipped,
        "public_new_pass": lock_stats["pass"],  # 本轮测活通过次数（池内，已按 fp 去重候选）
        "public_fail": lock_stats["fail"],
        "previous_public": len(prev_public),
        "previous_verified": len(prev),
        "retained_history_pass": retained_hist,
        "new_pass": new_pass,
        "history_dropped": hist_dropped,
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
            subprocess.run([sys.executable, str(sum_script), "--workspace", str(ws)], check=False)
        sub = ws / "scripts/export_subscription.py"
        if sub.exists():
            subprocess.run(
                [
                    sys.executable,
                    str(sub),
                    "--workspace",
                    str(ws),
                    "--no-wireguard-files",
                    "--strip-wireguard-from-singbox",
                ],
                check=False,
            )
    except Exception as e:
        print(f"[!] post export warn: {e}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
