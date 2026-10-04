# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-04 15:35:47](https://img.shields.io/badge/updated-2026--10--04_15%3A35%3A47-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10355.6s](https://img.shields.io/badge/elapsed-10355.6s-lightgrey)
![profiles: 3163](https://img.shields.io/badge/profiles-3163-blue)
![live_hits: 3163](https://img.shields.io/badge/live__hits-3163-brightgreen)
![live_fail: 77341](https://img.shields.io/badge/live__fail-77341-orange)
![kept: 986](https://img.shields.io/badge/kept-986-blue)
![new: 2177](https://img.shields.io/badge/new-2177-success)
![dropped: 166](https://img.shields.io/badge/dropped-166-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-04 15:35:47 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10355.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `434206` |
| **Live PASS (pool hits)** | `3163` |
| **Live FAIL** | `77341` |
| **History retained** | `986` |
| **New PASS** | `2177` |
| **History dropped** | `166` |
| **Previous public** | `1152` |
| **Published profiles (deduped)** | `3163` |
| **Share links (exportable)** | `1758` |
| **YAML proxies (exportable)** | `1758` |
| **Protocol mix** | `{"vless": 1185, "trojan": 93, "shadowsocks": 266, "vmess": 104, "hysteria2": 110}` |
| **Country mix** | `{"GB": 43, "US": 253, "ZA": 6, "NL": 165, "DE": 68, "CA": 712, "RU": 23, "SG": 51, "TR": 3, "ID": 3, "IE": 5, "FR": 30, "ES": 11, "CH": 9, "RO": 6, "JP": 57, "IN": 12, "KR": 39, "HU": 1, "HK": 52, "TW": 6, "FI": 12, "TH": 4, "IT": 21, "EE": 12, "GR": 3, "LU": 2, "PL": 19, "ZZ": 2, "SE": 16, "CL": 11, "BR": 2, "SC": 2, "NO": 2, "SA": 1, "LV": 4, "AE": 3, "KZ": 5, "IR": 2, "AU": 5, "BZ": 3, "CW": 2, "CY": 1, "LT": 10, "UA": 2, "BG": 13, "CR": 2, "AL": 2, "MY": 9, "AM": 2, "CN": 16, "PT": 1, "GT": 1, "CZ": 13, "NZ": 1, "IL": 1}` |
| **Line type mix** | `{"dc": 1232, "proxy": 420, "mobile": 22, "home": 86, "unknown": 2}` |

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
