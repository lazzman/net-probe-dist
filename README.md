# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-09 12:43:22](https://img.shields.io/badge/updated-2026--08--09_12%3A43%3A22-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10104.8s](https://img.shields.io/badge/elapsed-10104.8s-lightgrey)
![profiles: 3577](https://img.shields.io/badge/profiles-3577-blue)
![live_hits: 3577](https://img.shields.io/badge/live__hits-3577-brightgreen)
![live_fail: 90481](https://img.shields.io/badge/live__fail-90481-orange)
![kept: 970](https://img.shields.io/badge/kept-970-blue)
![new: 2607](https://img.shields.io/badge/new-2607-success)
![dropped: 113](https://img.shields.io/badge/dropped-113-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-09 12:43:22 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10104.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `445116` |
| **Live PASS (pool hits)** | `3577` |
| **Live FAIL** | `90481` |
| **History retained** | `970` |
| **New PASS** | `2607` |
| **History dropped** | `113` |
| **Previous public** | `1083` |
| **Published profiles (deduped)** | `3577` |
| **Share links (exportable)** | `2175` |
| **YAML proxies (exportable)** | `2175` |
| **Protocol mix** | `{"vless": 1640, "vmess": 87, "shadowsocks": 201, "hysteria2": 110, "trojan": 137}` |
| **Country mix** | `{"FR": 155, "US": 246, "GB": 99, "AU": 5, "NL": 244, "ES": 13, "DE": 115, "JP": 75, "IT": 12, "HK": 45, "SE": 14, "KR": 53, "RO": 6, "FI": 54, "SG": 35, "TW": 8, "ZA": 2, "CA": 694, "PL": 16, "TR": 7, "BG": 5, "SA": 3, "IE": 4, "KZ": 8, "PT": 1, "EE": 12, "RU": 96, "LT": 6, "SC": 11, "CH": 3, "HU": 3, "AM": 2, "CO": 7, "AT": 2, "MD": 1, "BE": 2, "TH": 3, "PH": 60, "IN": 6, "CN": 8, "BZ": 6, "CY": 3, "NO": 1, "CZ": 2, "AZ": 1, "AE": 4, "MY": 1, "BR": 2, "AL": 2, "LV": 7, "ME": 1, "AF": 1, "GR": 1, "UA": 5, "NZ": 1, "CW": 2, "IR": 1, "CR": 2, "DK": 1, "KH": 1}` |
| **Line type mix** | `{"proxy": 729, "dc": 1309, "home": 140, "mobile": 8}` |

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
