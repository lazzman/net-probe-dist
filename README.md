# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-19 11:54:02](https://img.shields.io/badge/updated-2026--08--19_11%3A54%3A02-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 8641.7s](https://img.shields.io/badge/elapsed-8641.7s-lightgrey)
![profiles: 5434](https://img.shields.io/badge/profiles-5434-blue)
![live_hits: 5439](https://img.shields.io/badge/live__hits-5439-brightgreen)
![live_fail: 61413](https://img.shields.io/badge/live__fail-61413-orange)
![kept: 1668](https://img.shields.io/badge/kept-1668-blue)
![new: 3771](https://img.shields.io/badge/new-3771-success)
![dropped: 173](https://img.shields.io/badge/dropped-173-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-19 11:54:02 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `8641.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `424220` |
| **Live PASS (pool hits)** | `5439` |
| **Live FAIL** | `61413` |
| **History retained** | `1668` |
| **New PASS** | `3771` |
| **History dropped** | `173` |
| **Previous public** | `1841` |
| **Published profiles (deduped)** | `5434` |
| **Share links (exportable)** | `3151` |
| **YAML proxies (exportable)** | `3151` |
| **Protocol mix** | `{"vless": 2036, "shadowsocks": 286, "vmess": 60, "hysteria2": 178, "trojan": 591}` |
| **Country mix** | `{"US": 404, "NL": 325, "AU": 23, "AT": 8, "SE": 30, "CA": 839, "FR": 63, "DZ": 6, "KR": 134, "DE": 184, "FI": 45, "SG": 151, "GB": 166, "TR": 13, "PL": 54, "IN": 11, "RO": 5, "AL": 6, "ZA": 3, "JP": 260, "IE": 20, "ES": 18, "HK": 99, "RU": 67, "IT": 12, "SC": 23, "EE": 17, "KZ": 14, "LV": 9, "CH": 8, "UA": 10, "BY": 2, "GR": 3, "TW": 7, "KG": 1, "NO": 8, "CZ": 5, "SK": 1, "MD": 2, "TH": 5, "SA": 1, "CN": 22, "CY": 6, "BZ": 7, "LT": 8, "AE": 4, "AZ": 1, "CO": 4, "BR": 6, "MY": 2, "IR": 5, "PE": 1, "PT": 2, "BG": 8, "IL": 1, "VN": 1, "BE": 2, "NZ": 2, "CW": 4, "HU": 2, "PH": 1, "ME": 1, "AM": 1, "CR": 1, "DK": 1, "VG": 1}` |
| **Line type mix** | `{"dc": 2127, "proxy": 774, "home": 229, "mobile": 26}` |

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
