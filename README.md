# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-21 17:29:58](https://img.shields.io/badge/updated-2026--08--21_17%3A29%3A58-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9077.8s](https://img.shields.io/badge/elapsed-9077.8s-lightgrey)
![profiles: 4280](https://img.shields.io/badge/profiles-4280-blue)
![live_hits: 4280](https://img.shields.io/badge/live__hits-4280-brightgreen)
![live_fail: 65289](https://img.shields.io/badge/live__fail-65289-orange)
![kept: 2115](https://img.shields.io/badge/kept-2115-blue)
![new: 2165](https://img.shields.io/badge/new-2165-success)
![dropped: 861](https://img.shields.io/badge/dropped-861-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-21 17:29:58 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9077.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `436842` |
| **Live PASS (pool hits)** | `4280` |
| **Live FAIL** | `65289` |
| **History retained** | `2115` |
| **New PASS** | `2165` |
| **History dropped** | `861` |
| **Previous public** | `2976` |
| **Published profiles (deduped)** | `4280` |
| **Share links (exportable)** | `2408` |
| **YAML proxies (exportable)** | `2408` |
| **Protocol mix** | `{"vmess": 67, "shadowsocks": 334, "vless": 1464, "hysteria2": 164, "trojan": 379}` |
| **Country mix** | `{"US": 282, "AU": 21, "DE": 170, "FR": 58, "SG": 78, "CA": 637, "HK": 86, "GB": 70, "JP": 251, "SE": 28, "NL": 292, "FI": 44, "BR": 8, "PL": 46, "IN": 16, "RO": 5, "RU": 45, "ES": 9, "TH": 5, "PH": 3, "CN": 7, "IT": 18, "IE": 18, "EE": 17, "TW": 17, "KZ": 15, "TR": 10, "LV": 18, "BG": 14, "CH": 10, "LT": 13, "VN": 2, "KG": 1, "SK": 1, "KR": 31, "MD": 2, "DK": 2, "AM": 1, "SC": 12, "ZA": 3, "BE": 2, "IR": 3, "AL": 2, "UA": 3, "CZ": 2, "CO": 4, "PT": 1, "AT": 1, "DZ": 4, "PE": 2, "AE": 1, "GR": 2, "NO": 3, "GE": 1, "BZ": 3, "CW": 3, "HU": 1, "SA": 1, "SI": 1, "TJ": 1, "CR": 1, "ID": 2, "AF": 1, "MY": 2, "CY": 1}` |
| **Line type mix** | `{"proxy": 627, "dc": 1536, "home": 238, "mobile": 13}` |

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
