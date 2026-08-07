# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-07 10:58:48](https://img.shields.io/badge/updated-2026--08--07_10%3A58%3A48-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10043.5s](https://img.shields.io/badge/elapsed-10043.5s-lightgrey)
![profiles: 4210](https://img.shields.io/badge/profiles-4210-blue)
![live_hits: 4210](https://img.shields.io/badge/live__hits-4210-brightgreen)
![live_fail: 89298](https://img.shields.io/badge/live__fail-89298-orange)
![kept: 1186](https://img.shields.io/badge/kept-1186-blue)
![new: 3024](https://img.shields.io/badge/new-3024-success)
![dropped: 178](https://img.shields.io/badge/dropped-178-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-07 10:58:48 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10043.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `453856` |
| **Live PASS (pool hits)** | `4210` |
| **Live FAIL** | `89298` |
| **History retained** | `1186` |
| **New PASS** | `3024` |
| **History dropped** | `178` |
| **Previous public** | `1364` |
| **Published profiles (deduped)** | `4210` |
| **Share links (exportable)** | `2582` |
| **YAML proxies (exportable)** | `2582` |
| **Protocol mix** | `{"vless": 2087, "vmess": 90, "shadowsocks": 179, "hysteria2": 104, "trojan": 122}` |
| **Country mix** | `{"US": 325, "GB": 125, "FR": 186, "CA": 952, "AU": 6, "ES": 12, "DE": 139, "IT": 12, "NL": 239, "SE": 10, "HK": 59, "RO": 5, "FI": 51, "SG": 43, "IN": 6, "ZA": 2, "TH": 5, "JP": 62, "BG": 8, "IE": 4, "PL": 23, "SC": 14, "PT": 2, "RU": 74, "CH": 3, "CZ": 1, "EE": 10, "AE": 5, "TW": 10, "HU": 2, "CR": 3, "CY": 5, "BR": 4, "CW": 5, "TR": 3, "KR": 42, "MD": 1, "CN": 7, "PH": 74, "LV": 3, "AT": 5, "BZ": 6, "KZ": 7, "NO": 1, "SA": 3, "AZ": 1, "CO": 4, "AF": 1, "MY": 1, "NZ": 2, "ME": 1, "IR": 3, "VG": 1, "BE": 1, "DK": 2, "AM": 2, "LT": 2, "KH": 1, "UA": 5, "GR": 1}` |
| **Line type mix** | `{"dc": 1642, "proxy": 829, "home": 116, "mobile": 5}` |

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
