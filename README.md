# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-19 17:17:18](https://img.shields.io/badge/updated-2026--08--19_17%3A17%3A18-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 8706.2s](https://img.shields.io/badge/elapsed-8706.2s-lightgrey)
![profiles: 4470](https://img.shields.io/badge/profiles-4470-blue)
![live_hits: 4474](https://img.shields.io/badge/live__hits-4474-brightgreen)
![live_fail: 63200](https://img.shields.io/badge/live__fail-63200-orange)
![kept: 2244](https://img.shields.io/badge/kept-2244-blue)
![new: 2230](https://img.shields.io/badge/new-2230-success)
![dropped: 907](https://img.shields.io/badge/dropped-907-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-19 17:17:18 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `8706.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `428824` |
| **Live PASS (pool hits)** | `4474` |
| **Live FAIL** | `63200` |
| **History retained** | `2244` |
| **New PASS** | `2230` |
| **History dropped** | `907` |
| **Previous public** | `3151` |
| **Published profiles (deduped)** | `4470` |
| **Share links (exportable)** | `2569` |
| **YAML proxies (exportable)** | `2569` |
| **Protocol mix** | `{"hysteria2": 174, "vmess": 54, "shadowsocks": 279, "vless": 1380, "trojan": 682}` |
| **Country mix** | `{"SG": 144, "US": 293, "AU": 20, "NL": 290, "SE": 27, "GB": 56, "DE": 158, "CA": 600, "FR": 57, "AT": 7, "DZ": 5, "FI": 37, "KR": 126, "PL": 44, "IN": 13, "RO": 4, "ZA": 3, "AL": 5, "JP": 258, "ES": 10, "CN": 20, "RU": 48, "HK": 65, "IT": 10, "TR": 12, "IE": 19, "ZZ": 96, "SC": 15, "EE": 12, "KZ": 13, "BR": 7, "LV": 10, "CH": 8, "AE": 3, "NO": 7, "UA": 6, "BY": 2, "TW": 6, "GR": 3, "KG": 1, "SK": 1, "MD": 2, "CZ": 3, "TH": 4, "LT": 8, "CO": 4, "AZ": 1, "AM": 1, "IR": 3, "SA": 1, "PH": 2, "BE": 3, "PT": 1, "BG": 6, "IL": 1, "BZ": 3, "PE": 1, "HU": 1, "DK": 2, "GE": 1, "VN": 2, "MK": 1, "MY": 1, "CY": 1}` |
| **Line type mix** | `{"dc": 1633, "home": 187, "proxy": 632, "mobile": 26, "unknown": 96}` |

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
