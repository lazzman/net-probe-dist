# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-23 23:18:05](https://img.shields.io/badge/updated-2026--08--23_23%3A18%3A05-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9107.4s](https://img.shields.io/badge/elapsed-9107.4s-lightgrey)
![profiles: 2204](https://img.shields.io/badge/profiles-2204-blue)
![live_hits: 2206](https://img.shields.io/badge/live__hits-2206-brightgreen)
![live_fail: 67708](https://img.shields.io/badge/live__fail-67708-orange)
![kept: 1323](https://img.shields.io/badge/kept-1323-blue)
![new: 883](https://img.shields.io/badge/new-883-success)
![dropped: 819](https://img.shields.io/badge/dropped-819-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-23 23:18:05 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9107.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `421212` |
| **Live PASS (pool hits)** | `2206` |
| **Live FAIL** | `67708` |
| **History retained** | `1323` |
| **New PASS** | `883` |
| **History dropped** | `819` |
| **Previous public** | `2142` |
| **Published profiles (deduped)** | `2204` |
| **Share links (exportable)** | `1677` |
| **YAML proxies (exportable)** | `1677` |
| **Protocol mix** | `{"vless": 1063, "vmess": 68, "shadowsocks": 328, "hysteria2": 187, "trojan": 31}` |
| **Country mix** | `{"NL": 288, "US": 266, "AU": 8, "CA": 254, "DE": 143, "PL": 35, "JP": 64, "FR": 36, "RU": 53, "FI": 26, "SG": 68, "SE": 18, "GB": 66, "HK": 91, "BR": 24, "TW": 21, "TR": 14, "IN": 14, "RO": 4, "LT": 11, "ZA": 3, "TH": 4, "CN": 8, "ES": 7, "AT": 3, "EE": 13, "KZ": 13, "BE": 1, "NO": 6, "CH": 11, "IT": 16, "DK": 3, "VN": 3, "GR": 3, "HU": 2, "LV": 14, "SK": 1, "MD": 2, "KR": 15, "NZ": 1, "MY": 4, "SA": 1, "AM": 1, "PE": 2, "AL": 5, "MX": 1, "BG": 6, "CZ": 3, "AE": 1, "UA": 2, "IR": 1, "SC": 4, "PH": 1, "AZ": 1, "GE": 1, "BY": 2, "BZ": 1, "CR": 1, "AF": 1, "DZ": 4, "CY": 1, "IE": 1}` |
| **Line type mix** | `{"home": 235, "proxy": 486, "dc": 944, "mobile": 13}` |

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
