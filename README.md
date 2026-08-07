# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-07 14:10:03](https://img.shields.io/badge/updated-2026--08--07_14%3A10%3A03-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10055.8s](https://img.shields.io/badge/elapsed-10055.8s-lightgrey)
![profiles: 3895](https://img.shields.io/badge/profiles-3895-blue)
![live_hits: 3895](https://img.shields.io/badge/live__hits-3895-brightgreen)
![live_fail: 89710](https://img.shields.io/badge/live__fail-89710-orange)
![kept: 2129](https://img.shields.io/badge/kept-2129-blue)
![new: 1766](https://img.shields.io/badge/new-1766-success)
![dropped: 453](https://img.shields.io/badge/dropped-453-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-07 14:10:03 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10055.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `453795` |
| **Live PASS (pool hits)** | `3895` |
| **Live FAIL** | `89710` |
| **History retained** | `2129` |
| **New PASS** | `1766` |
| **History dropped** | `453` |
| **Previous public** | `2582` |
| **Published profiles (deduped)** | `3895` |
| **Share links (exportable)** | `2358` |
| **YAML proxies (exportable)** | `2358` |
| **Protocol mix** | `{"vless": 1841, "vmess": 87, "shadowsocks": 205, "hysteria2": 103, "trojan": 122}` |
| **Country mix** | `{"FR": 186, "US": 285, "NL": 233, "GB": 97, "DE": 112, "AU": 5, "IT": 10, "SE": 11, "HK": 51, "RO": 5, "FI": 46, "SG": 45, "IN": 8, "ZA": 2, "TH": 5, "ES": 8, "CA": 823, "JP": 55, "BG": 6, "IE": 5, "PL": 19, "SC": 13, "PT": 2, "RU": 70, "AT": 6, "CH": 3, "CZ": 1, "EE": 11, "AE": 7, "TW": 9, "HU": 1, "CR": 3, "BR": 9, "CY": 5, "TR": 5, "KR": 43, "MD": 1, "CN": 7, "PH": 78, "LV": 5, "MY": 2, "KZ": 10, "BZ": 3, "SA": 3, "NO": 1, "AZ": 1, "CO": 25, "IR": 7, "NZ": 1, "DK": 2, "AM": 2, "KH": 1, "UA": 4, "LT": 1, "CW": 2, "GR": 1}` |
| **Line type mix** | `{"proxy": 751, "dc": 1496, "home": 110, "mobile": 5}` |

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
