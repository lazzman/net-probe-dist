# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-18 11:50:25](https://img.shields.io/badge/updated-2026--08--18_11%3A50%3A25-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 8577.4s](https://img.shields.io/badge/elapsed-8577.4s-lightgrey)
![profiles: 5203](https://img.shields.io/badge/profiles-5203-blue)
![live_hits: 5203](https://img.shields.io/badge/live__hits-5203-brightgreen)
![live_fail: 61040](https://img.shields.io/badge/live__fail-61040-orange)
![kept: 1639](https://img.shields.io/badge/kept-1639-blue)
![new: 3564](https://img.shields.io/badge/new-3564-success)
![dropped: 221](https://img.shields.io/badge/dropped-221-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-18 11:50:25 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `8577.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `413873` |
| **Live PASS (pool hits)** | `5203` |
| **Live FAIL** | `61040` |
| **History retained** | `1639` |
| **New PASS** | `3564` |
| **History dropped** | `221` |
| **Previous public** | `1860` |
| **Published profiles (deduped)** | `5203` |
| **Share links (exportable)** | `2976` |
| **YAML proxies (exportable)** | `2976` |
| **Protocol mix** | `{"vmess": 85, "vless": 1941, "shadowsocks": 213, "hysteria2": 208, "trojan": 529}` |
| **Country mix** | `{"US": 391, "AU": 17, "AT": 7, "NL": 331, "CA": 815, "HK": 98, "SE": 25, "IN": 11, "FR": 63, "DZ": 7, "JP": 247, "KR": 120, "DE": 171, "FI": 49, "SG": 132, "PL": 38, "NO": 7, "ZA": 3, "TH": 5, "PH": 1, "GB": 162, "CO": 10, "IT": 12, "IE": 16, "EE": 17, "KZ": 16, "RU": 62, "AL": 3, "LV": 7, "SC": 19, "CH": 6, "CZ": 3, "LT": 7, "TW": 8, "KG": 1, "GR": 3, "UA": 8, "MD": 1, "RO": 4, "CN": 5, "BR": 5, "MY": 1, "ES": 9, "BZ": 8, "CY": 6, "TR": 8, "BY": 2, "PT": 2, "DK": 2, "BG": 9, "AE": 4, "NZ": 2, "CW": 5, "HU": 2, "ME": 1, "IR": 3, "SA": 1, "AM": 1, "AF": 1, "KH": 1, "BE": 1}` |
| **Line type mix** | `{"dc": 2036, "proxy": 730, "home": 207, "mobile": 9}` |

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
