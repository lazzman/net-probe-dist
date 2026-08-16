# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-16 23:35:27](https://img.shields.io/badge/updated-2026--08--16_23%3A35%3A27-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10323.3s](https://img.shields.io/badge/elapsed-10323.3s-lightgrey)
![profiles: 2774](https://img.shields.io/badge/profiles-2774-blue)
![live_hits: 2774](https://img.shields.io/badge/live__hits-2774-brightgreen)
![live_fail: 92592](https://img.shields.io/badge/live__fail-92592-orange)
![kept: 1645](https://img.shields.io/badge/kept-1645-blue)
![new: 1129](https://img.shields.io/badge/new-1129-success)
![dropped: 701](https://img.shields.io/badge/dropped-701-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-16 23:35:27 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10323.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `448287` |
| **Live PASS (pool hits)** | `2774` |
| **Live FAIL** | `92592` |
| **History retained** | `1645` |
| **New PASS** | `1129` |
| **History dropped** | `701` |
| **Previous public** | `2346` |
| **Published profiles (deduped)** | `2774` |
| **Share links (exportable)** | `1868` |
| **YAML proxies (exportable)** | `1868` |
| **Protocol mix** | `{"vmess": 80, "vless": 1094, "shadowsocks": 202, "hysteria2": 138, "trojan": 354}` |
| **Country mix** | `{"US": 231, "CA": 357, "AU": 15, "AT": 7, "DE": 114, "NL": 277, "SG": 60, "SE": 18, "IN": 11, "FI": 38, "HK": 63, "FR": 48, "DZ": 2, "GB": 35, "EE": 13, "PL": 39, "NO": 6, "RO": 8, "AL": 3, "TH": 3, "JP": 171, "CO": 1, "KR": 104, "IT": 6, "IE": 13, "ES": 10, "SC": 10, "KZ": 14, "CN": 6, "RU": 115, "LV": 8, "IR": 4, "CH": 8, "TW": 5, "MD": 2, "TR": 10, "SA": 1, "PH": 2, "ID": 1, "LT": 3, "ZA": 2, "AE": 1, "OM": 1, "GR": 1, "MY": 1, "PT": 1, "UA": 3, "BG": 4, "CZ": 2, "HU": 2, "BR": 1, "AF": 1, "BY": 2, "AM": 1, "DK": 2, "IL": 1, "CR": 2, "CY": 1, "KH": 1}` |
| **Line type mix** | `{"dc": 1165, "proxy": 517, "home": 183, "mobile": 7}` |

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
