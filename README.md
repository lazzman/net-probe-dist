# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-08 14:13:45](https://img.shields.io/badge/updated-2026--09--08_14%3A13%3A45-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9843.9s](https://img.shields.io/badge/elapsed-9843.9s-lightgrey)
![profiles: 3840](https://img.shields.io/badge/profiles-3840-blue)
![live_hits: 3840](https://img.shields.io/badge/live__hits-3840-brightgreen)
![live_fail: 73019](https://img.shields.io/badge/live__fail-73019-orange)
![kept: 1138](https://img.shields.io/badge/kept-1138-blue)
![new: 2702](https://img.shields.io/badge/new-2702-success)
![dropped: 128](https://img.shields.io/badge/dropped-128-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-08 14:13:45 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9843.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `434660` |
| **Live PASS (pool hits)** | `3840` |
| **Live FAIL** | `73019` |
| **History retained** | `1138` |
| **New PASS** | `2702` |
| **History dropped** | `128` |
| **Previous public** | `1266` |
| **Published profiles (deduped)** | `3840` |
| **Share links (exportable)** | `2008` |
| **YAML proxies (exportable)** | `2008` |
| **Protocol mix** | `{"vless": 1444, "trojan": 75, "hysteria2": 160, "shadowsocks": 259, "vmess": 70}` |
| **Country mix** | `{"GB": 99, "CA": 786, "HR": 1, "DZ": 21, "RU": 26, "FI": 24, "NL": 223, "DE": 75, "TW": 17, "ID": 1, "ZA": 7, "FR": 34, "US": 283, "RO": 3, "PL": 38, "SG": 56, "ES": 10, "JP": 54, "MY": 5, "CN": 5, "IE": 2, "IT": 12, "IN": 9, "KZ": 9, "JE": 1, "EE": 14, "NO": 21, "BR": 3, "HK": 46, "HU": 3, "LV": 7, "SE": 10, "GR": 2, "KR": 26, "TR": 5, "AU": 7, "LT": 9, "EG": 1, "TH": 3, "SA": 1, "AM": 1, "SC": 5, "AE": 3, "AT": 3, "CH": 3, "AR": 2, "UZ": 1, "BG": 9, "CR": 7, "ZZ": 1, "UA": 4, "NZ": 1, "PT": 1, "BZ": 3, "CW": 2, "GT": 1, "SK": 1, "PH": 1, "CY": 1, "IR": 1, "VG": 1}` |
| **Line type mix** | `{"dc": 1420, "proxy": 464, "home": 114, "mobile": 12, "unknown": 1}` |

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
