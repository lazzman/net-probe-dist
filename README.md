# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-14 22:44:16](https://img.shields.io/badge/updated-2026--09--14_22%3A44%3A16-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9774.5s](https://img.shields.io/badge/elapsed-9774.5s-lightgrey)
![profiles: 1429](https://img.shields.io/badge/profiles-1429-blue)
![live_hits: 1431](https://img.shields.io/badge/live__hits-1431-brightgreen)
![live_fail: 74606](https://img.shields.io/badge/live__fail-74606-orange)
![kept: 1094](https://img.shields.io/badge/kept-1094-blue)
![new: 337](https://img.shields.io/badge/new-337-success)
![dropped: 1220](https://img.shields.io/badge/dropped-1220-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-14 22:44:16 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9774.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `424715` |
| **Live PASS (pool hits)** | `1431` |
| **Live FAIL** | `74606` |
| **History retained** | `1094` |
| **New PASS** | `337` |
| **History dropped** | `1220` |
| **Previous public** | `2314` |
| **Published profiles (deduped)** | `1429` |
| **Share links (exportable)** | `1228` |
| **YAML proxies (exportable)** | `1228` |
| **Protocol mix** | `{"trojan": 50, "vmess": 56, "hysteria2": 149, "vless": 745, "shadowsocks": 228}` |
| **Country mix** | `{"US": 180, "CA": 368, "DE": 47, "SG": 28, "GB": 53, "NL": 195, "DZ": 24, "RU": 23, "IN": 12, "JP": 33, "SE": 8, "ID": 1, "ZA": 4, "TR": 6, "PL": 23, "ES": 7, "FI": 13, "MX": 1, "IT": 9, "DK": 1, "KR": 27, "AT": 1, "HR": 1, "TW": 17, "EE": 8, "UZ": 2, "HK": 53, "AE": 1, "FR": 25, "UA": 3, "GR": 2, "TH": 4, "GT": 1, "LT": 12, "RO": 2, "CZ": 3, "SA": 1, "MY": 3, "NO": 4, "AM": 2, "AL": 1, "SC": 3, "CH": 2, "KZ": 5, "AU": 3, "CN": 1, "LV": 8, "CR": 1}` |
| **Line type mix** | `{"dc": 810, "proxy": 343, "home": 73, "mobile": 6}` |

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
| `fsl64` | encoded blob | https://github.com/lazzman/net-probe-dist/releases/latest/download/fsl64 |
| `fslyaml` | YAML pack | https://github.com/lazzman/net-probe-dist/releases/latest/download/fslyaml |
| `fslsb` | JSON runtime pack | https://github.com/lazzman/net-probe-dist/releases/latest/download/fslsb |
| `fslyamlcomp` | legacy YAML pack | https://github.com/lazzman/net-probe-dist/releases/latest/download/fslyamlcomp |
| manifest | build metadata | https://github.com/lazzman/net-probe-dist/releases/latest/download/manifest.json |

Release page: https://github.com/lazzman/net-probe-dist/releases/latest

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
