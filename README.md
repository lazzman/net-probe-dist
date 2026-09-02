# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-02 14:00:02](https://img.shields.io/badge/updated-2026--09--02_14%3A00%3A02-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9610.2s](https://img.shields.io/badge/elapsed-9610.2s-lightgrey)
![profiles: 4595](https://img.shields.io/badge/profiles-4595-blue)
![live_hits: 4595](https://img.shields.io/badge/live__hits-4595-brightgreen)
![live_fail: 70417](https://img.shields.io/badge/live__fail-70417-orange)
![kept: 1296](https://img.shields.io/badge/kept-1296-blue)
![new: 3299](https://img.shields.io/badge/new-3299-success)
![dropped: 165](https://img.shields.io/badge/dropped-165-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-02 14:00:02 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9610.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `426422` |
| **Live PASS (pool hits)** | `4595` |
| **Live FAIL** | `70417` |
| **History retained** | `1296` |
| **New PASS** | `3299` |
| **History dropped** | `165` |
| **Previous public** | `1461` |
| **Published profiles (deduped)** | `4595` |
| **Share links (exportable)** | `2507` |
| **YAML proxies (exportable)** | `2507` |
| **Protocol mix** | `{"vless": 1874, "shadowsocks": 273, "hysteria2": 196, "trojan": 88, "vmess": 76}` |
| **Country mix** | `{"IT": 16, "FR": 34, "NL": 257, "KR": 41, "US": 355, "SG": 89, "RU": 43, "PL": 30, "CA": 924, "FI": 37, "DZ": 17, "GB": 113, "DE": 118, "SE": 18, "TW": 22, "ID": 2, "RO": 5, "IE": 4, "ZA": 4, "ES": 14, "MY": 3, "TH": 7, "CN": 8, "JP": 80, "CO": 5, "PH": 2, "AT": 5, "KZ": 15, "NO": 21, "EE": 10, "IN": 10, "LV": 14, "TR": 3, "CH": 9, "CZ": 4, "IR": 4, "AE": 5, "HK": 67, "AL": 4, "BR": 12, "UA": 6, "LT": 17, "SC": 9, "BG": 8, "GR": 3, "SA": 1, "UZ": 2, "AM": 1, "DK": 1, "HR": 1, "AR": 2, "JE": 1, "AU": 7, "MX": 3, "BZ": 7, "NZ": 1, "PT": 1, "CY": 2, "CW": 1, "SK": 1, "EG": 1, "ME": 1, "CR": 2}` |
| **Line type mix** | `{"dc": 1771, "proxy": 559, "home": 167, "mobile": 13}` |

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
