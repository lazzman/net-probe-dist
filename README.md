# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-03 22:20:14](https://img.shields.io/badge/updated-2026--08--03_22%3A20%3A14-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 32](https://img.shields.io/badge/workers-32-blueviolet)
![elapsed: 2891.0s](https://img.shields.io/badge/elapsed-2891.0s-lightgrey)
![profiles: 1401](https://img.shields.io/badge/profiles-1401-blue)
![live_hits: 5732](https://img.shields.io/badge/live__hits-5732-brightgreen)
![live_fail: 22810](https://img.shields.io/badge/live__fail-22810-orange)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-03T22:20:14.186270+08:00` |
| **Workflow result** | `success` |
| **Workers** | `32` |
| **Elapsed** | `2891.0s` |
| **Probe mode** | `full_no_sample` |
| **Candidates (unique)** | `28663` |
| **Live PASS (raw hits)** | `5732` |
| **Live FAIL** | `22810` |
| **Published profiles (deduped)** | `1401` |
| **Share links (exportable)** | `1401` |
| **YAML proxies (exportable)** | `1401` |
| **Protocol mix** | `{"vless": 990, "shadowsocks": 195, "trojan": 41, "vmess": 86, "hysteria2": 89}` |

### Number funnel

These fields are **not** the same quantity:

1. **Candidates (unique)** — 公开订阅去重后的候选链接数  
2. **Live PASS (raw hits)** — 探测过程中判 PASS 的**次数**（同一 endpoint 多条链接会重复计数）  
3. **Published profiles (deduped)** — 按 `type:server:port:凭证` 指纹去重后的最终 outbound 数（`fslsb` 接近此值）  
4. **Share links / YAML proxies** — 能导出为通用分享链 / Clash 的节点（现含 vless/ss/trojan/vmess/**hysteria2**）

所以常见现象：Live PASS 五千多，最终订阅一千多——主要是重复 endpoint 被合并，而不是探测结果被丢弃。

## Latest packages

| Code | Package | Latest link |
| --- | --- | --- |
| `fsl64` | encoded blob | https://github.com/lazzman/net-probe-dist/releases/latest/download/fsl64 |
| `fslyaml` | YAML pack | https://github.com/lazzman/net-probe-dist/releases/latest/download/fslyaml |
| `fslsb` | JSON runtime pack | https://github.com/lazzman/net-probe-dist/releases/latest/download/fslsb |
| `fslyamlcomp` | legacy YAML pack | https://github.com/lazzman/net-probe-dist/releases/latest/download/fslyamlcomp |
| manifest | build metadata | https://github.com/lazzman/net-probe-dist/releases/latest/download/manifest.json |

Release page: https://github.com/lazzman/net-probe-dist/releases/latest

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
