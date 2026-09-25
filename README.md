# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-25 14:40:15](https://img.shields.io/badge/updated-2026--09--25_14%3A40%3A15-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10079.2s](https://img.shields.io/badge/elapsed-10079.2s-lightgrey)
![profiles: 3838](https://img.shields.io/badge/profiles-3838-blue)
![live_hits: 3838](https://img.shields.io/badge/live__hits-3838-brightgreen)
![live_fail: 74701](https://img.shields.io/badge/live__fail-74701-orange)
![kept: 1036](https://img.shields.io/badge/kept-1036-blue)
![new: 2802](https://img.shields.io/badge/new-2802-success)
![dropped: 104](https://img.shields.io/badge/dropped-104-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-25 14:40:15 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10079.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `433964` |
| **Live PASS (pool hits)** | `3838` |
| **Live FAIL** | `74701` |
| **History retained** | `1036` |
| **New PASS** | `2802` |
| **History dropped** | `104` |
| **Previous public** | `1140` |
| **Published profiles (deduped)** | `3838` |
| **Share links (exportable)** | `2102` |
| **YAML proxies (exportable)** | `2102` |
| **Protocol mix** | `{"vmess": 92, "vless": 1539, "shadowsocks": 289, "hysteria2": 115, "trojan": 67}` |
| **Country mix** | `{"GB": 103, "CA": 952, "US": 260, "SE": 24, "CZ": 2, "ZA": 3, "DE": 82, "SG": 42, "ES": 11, "HK": 49, "KR": 33, "NL": 183, "RU": 35, "ID": 1, "FR": 33, "NO": 2, "RO": 4, "CH": 7, "PL": 26, "JP": 48, "IN": 16, "DK": 1, "IT": 20, "AT": 3, "FI": 28, "TR": 3, "TH": 4, "EE": 11, "AU": 5, "CR": 2, "AL": 1, "LT": 11, "IL": 3, "AM": 1, "IQ": 1, "MY": 3, "TW": 8, "SC": 5, "KZ": 7, "BG": 14, "AE": 3, "DZ": 26, "CY": 3, "IR": 2, "NZ": 1, "PT": 1, "CN": 1, "BZ": 4, "BR": 1, "CW": 5, "UA": 3, "GT": 1, "CL": 1, "LV": 10, "GR": 1, "ME": 1, "SA": 1, "VG": 1}` |
| **Line type mix** | `{"proxy": 488, "dc": 1517, "mobile": 17, "home": 91}` |

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
