# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-17 12:53:44](https://img.shields.io/badge/updated-2026--11--17_12%3A53%3A44-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11353.7s](https://img.shields.io/badge/elapsed-11353.7s-lightgrey)
![profiles: 1649](https://img.shields.io/badge/profiles-1649-blue)
![live_hits: 1649](https://img.shields.io/badge/live__hits-1649-brightgreen)
![live_fail: 87908](https://img.shields.io/badge/live__fail-87908-orange)
![kept: 945](https://img.shields.io/badge/kept-945-blue)
![new: 704](https://img.shields.io/badge/new-704-success)
![dropped: 203](https://img.shields.io/badge/dropped-203-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-17 12:53:44 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11353.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `403316` |
| **Live PASS (pool hits)** | `1649` |
| **Live FAIL** | `87908` |
| **History retained** | `945` |
| **New PASS** | `704` |
| **History dropped** | `203` |
| **Previous public** | `1148` |
| **Published profiles (deduped)** | `1649` |
| **Share links (exportable)** | `1442` |
| **YAML proxies (exportable)** | `1442` |
| **Protocol mix** | `{"hysteria2": 67, "vmess": 124, "vless": 759, "shadowsocks": 385, "trojan": 107}` |
| **Country mix** | `{"TR": 49, "NL": 139, "US": 330, "AT": 2, "SE": 25, "DE": 99, "HK": 32, "CA": 286, "GB": 48, "FR": 44, "AL": 2, "ZA": 4, "PL": 55, "FI": 15, "IT": 19, "JP": 49, "ES": 29, "BG": 9, "KR": 15, "MX": 1, "RU": 22, "CH": 15, "SG": 53, "CL": 1, "EE": 10, "BY": 10, "AE": 2, "LY": 1, "AU": 5, "IR": 4, "VG": 1, "NG": 4, "DK": 1, "NO": 1, "GR": 1, "LT": 12, "TW": 4, "NE": 3, "BR": 2, "IN": 5, "RO": 3, "LV": 12, "BE": 1, "GE": 1, "TH": 2, "PT": 1, "MY": 2, "VN": 1, "SK": 3, "KZ": 1, "IL": 2, "CR": 3, "CZ": 1, "UA": 1, "MD": 1, "SA": 1, "SC": 1}` |
| **Line type mix** | `{"dc": 736, "proxy": 484, "home": 131, "mobile": 95}` |

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
