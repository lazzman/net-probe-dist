# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-19 05:13:02](https://img.shields.io/badge/updated-2026--08--19_05%3A13%3A02-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 8786.4s](https://img.shields.io/badge/elapsed-8786.4s-lightgrey)
![profiles: 2930](https://img.shields.io/badge/profiles-2930-blue)
![live_hits: 2930](https://img.shields.io/badge/live__hits-2930-brightgreen)
![live_fail: 63796](https://img.shields.io/badge/live__fail-63796-orange)
![kept: 1566](https://img.shields.io/badge/kept-1566-blue)
![new: 1364](https://img.shields.io/badge/new-1364-success)
![dropped: 307](https://img.shields.io/badge/dropped-307-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-19 05:13:02 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `8786.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `429443` |
| **Live PASS (pool hits)** | `2930` |
| **Live FAIL** | `63796` |
| **History retained** | `1566` |
| **New PASS** | `1364` |
| **History dropped** | `307` |
| **Previous public** | `1873` |
| **Published profiles (deduped)** | `2930` |
| **Share links (exportable)** | `1841` |
| **YAML proxies (exportable)** | `1841` |
| **Protocol mix** | `{"hysteria2": 215, "vless": 778, "vmess": 58, "shadowsocks": 264, "trojan": 526}` |
| **Country mix** | `{"AT": 6, "US": 249, "NL": 263, "SE": 20, "AU": 19, "FR": 58, "DZ": 5, "GB": 34, "DE": 129, "KR": 130, "FI": 26, "BR": 7, "SG": 141, "HK": 65, "PL": 45, "CA": 165, "IN": 10, "JP": 248, "AL": 5, "IE": 18, "ES": 8, "RU": 45, "TR": 10, "PT": 1, "KZ": 11, "IT": 3, "LV": 10, "EE": 11, "CH": 4, "CZ": 4, "GR": 3, "TW": 8, "KG": 1, "NO": 5, "SK": 1, "MD": 1, "RO": 3, "LT": 2, "AM": 1, "PH": 3, "SC": 8, "ZA": 3, "TH": 3, "PE": 2, "CO": 3, "IR": 1, "UA": 6, "CN": 22, "BG": 3, "AE": 2, "VN": 2, "BE": 2, "HU": 1, "SA": 1, "BY": 1, "DK": 1, "MY": 3, "ID": 1}` |
| **Line type mix** | `{"dc": 1120, "proxy": 515, "home": 183, "mobile": 25}` |

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
