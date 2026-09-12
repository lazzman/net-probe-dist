# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-12 14:12:17](https://img.shields.io/badge/updated-2026--09--12_14%3A12%3A17-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9621.7s](https://img.shields.io/badge/elapsed-9621.7s-lightgrey)
![profiles: 4133](https://img.shields.io/badge/profiles-4133-blue)
![live_hits: 4134](https://img.shields.io/badge/live__hits-4134-brightgreen)
![live_fail: 71514](https://img.shields.io/badge/live__fail-71514-orange)
![kept: 1117](https://img.shields.io/badge/kept-1117-blue)
![new: 3017](https://img.shields.io/badge/new-3017-success)
![dropped: 108](https://img.shields.io/badge/dropped-108-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-12 14:12:17 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9621.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `420825` |
| **Live PASS (pool hits)** | `4134` |
| **Live FAIL** | `71514` |
| **History retained** | `1117` |
| **New PASS** | `3017` |
| **History dropped** | `108` |
| **Previous public** | `1225` |
| **Published profiles (deduped)** | `4133` |
| **Share links (exportable)** | `2319` |
| **YAML proxies (exportable)** | `2319` |
| **Protocol mix** | `{"hysteria2": 148, "vmess": 110, "vless": 1711, "trojan": 99, "shadowsocks": 251}` |
| **Country mix** | `{"DE": 96, "GB": 102, "JP": 38, "CA": 1083, "NL": 226, "SG": 43, "AU": 6, "IN": 9, "DZ": 24, "RU": 32, "FI": 32, "TW": 15, "US": 280, "ID": 1, "AE": 5, "ZA": 3, "NO": 6, "FR": 35, "RO": 8, "PL": 33, "ES": 11, "KZ": 8, "MY": 4, "IT": 14, "AT": 5, "HR": 1, "EE": 12, "TR": 6, "HK": 64, "TH": 3, "IL": 1, "GR": 2, "GT": 1, "UZ": 2, "SE": 10, "LT": 15, "CZ": 3, "SA": 1, "CN": 3, "KR": 32, "SC": 7, "DK": 2, "BG": 5, "CH": 1, "BZ": 4, "UA": 6, "IR": 4, "NZ": 1, "PT": 2, "BR": 1, "CW": 3, "CR": 2, "AM": 1, "VG": 1, "LV": 11, "CY": 2, "ME": 1, "IE": 1, "AL": 1}` |
| **Line type mix** | `{"dc": 1732, "proxy": 487, "home": 104, "mobile": 8}` |

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
