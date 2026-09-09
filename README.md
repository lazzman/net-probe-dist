# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-09 14:14:14](https://img.shields.io/badge/updated-2026--09--09_14%3A14%3A14-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9911.7s](https://img.shields.io/badge/elapsed-9911.7s-lightgrey)
![profiles: 3038](https://img.shields.io/badge/profiles-3038-blue)
![live_hits: 3038](https://img.shields.io/badge/live__hits-3038-brightgreen)
![live_fail: 73209](https://img.shields.io/badge/live__fail-73209-orange)
![kept: 1032](https://img.shields.io/badge/kept-1032-blue)
![new: 2006](https://img.shields.io/badge/new-2006-success)
![dropped: 261](https://img.shields.io/badge/dropped-261-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-09 14:14:14 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9911.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `425689` |
| **Live PASS (pool hits)** | `3038` |
| **Live FAIL** | `73209` |
| **History retained** | `1032` |
| **New PASS** | `2006` |
| **History dropped** | `261` |
| **Previous public** | `1293` |
| **Published profiles (deduped)** | `3038` |
| **Share links (exportable)** | `1709` |
| **YAML proxies (exportable)** | `1709` |
| **Protocol mix** | `{"trojan": 55, "hysteria2": 158, "vless": 1134, "vmess": 100, "shadowsocks": 262}` |
| **Country mix** | `{"HR": 1, "KR": 31, "JP": 49, "GB": 78, "SE": 9, "NL": 208, "SG": 50, "CA": 594, "MK": 2, "FR": 30, "AU": 6, "DZ": 17, "RU": 32, "IN": 8, "FI": 25, "US": 215, "TW": 17, "ID": 1, "DE": 85, "ZA": 6, "NO": 22, "LT": 10, "PL": 37, "RO": 4, "ES": 9, "MY": 3, "CN": 6, "IE": 5, "IT": 9, "AE": 3, "KZ": 8, "EE": 6, "CZ": 5, "TR": 8, "JE": 1, "HK": 54, "LV": 13, "GR": 2, "UZ": 2, "SK": 1, "EG": 1, "SA": 1, "TH": 4, "SC": 6, "HU": 1, "CH": 3, "AR": 2, "UA": 4, "IR": 1, "BZ": 1, "BG": 3, "BR": 2, "CW": 1, "GT": 1, "PH": 1, "AM": 1, "BE": 1, "DK": 1, "CY": 2, "CR": 1, "VG": 1, "AL": 1, "AT": 1}` |
| **Line type mix** | `{"proxy": 426, "dc": 1157, "home": 118, "mobile": 12}` |

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
