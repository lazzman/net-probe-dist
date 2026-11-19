# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-19 11:14:15](https://img.shields.io/badge/updated-2026--11--19_11%3A14%3A15-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11463.5s](https://img.shields.io/badge/elapsed-11463.5s-lightgrey)
![profiles: 1987](https://img.shields.io/badge/profiles-1987-blue)
![live_hits: 1987](https://img.shields.io/badge/live__hits-1987-brightgreen)
![live_fail: 87628](https://img.shields.io/badge/live__fail-87628-orange)
![kept: 1003](https://img.shields.io/badge/kept-1003-blue)
![new: 984](https://img.shields.io/badge/new-984-success)
![dropped: 144](https://img.shields.io/badge/dropped-144-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-19 11:14:15 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11463.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `406040` |
| **Live PASS (pool hits)** | `1987` |
| **Live FAIL** | `87628` |
| **History retained** | `1003` |
| **New PASS** | `984` |
| **History dropped** | `144` |
| **Previous public** | `1147` |
| **Published profiles (deduped)** | `1987` |
| **Share links (exportable)** | `1664` |
| **YAML proxies (exportable)** | `1664` |
| **Protocol mix** | `{"vmess": 139, "hysteria2": 63, "shadowsocks": 389, "trojan": 123, "vless": 950}` |
| **Country mix** | `{"AT": 5, "HK": 45, "RU": 15, "DE": 123, "US": 358, "GB": 53, "NL": 143, "TR": 44, "CA": 380, "AL": 2, "FR": 41, "ZA": 5, "IT": 22, "JP": 72, "ES": 33, "BG": 8, "LT": 11, "KR": 13, "MX": 1, "FI": 17, "IN": 5, "SG": 83, "CH": 15, "CL": 1, "AU": 6, "BR": 15, "TW": 7, "SE": 18, "EE": 11, "BY": 6, "PL": 42, "NE": 5, "IR": 4, "LU": 2, "CZ": 4, "GR": 1, "KZ": 6, "VN": 3, "MY": 5, "NO": 1, "LV": 5, "AE": 2, "BH": 1, "SK": 2, "IE": 3, "TH": 1, "RO": 2, "IL": 2, "DK": 2, "UA": 4, "LY": 1, "NG": 2, "CR": 3, "VG": 2, "MD": 2, "SA": 1, "SC": 2, "BZ": 2}` |
| **Line type mix** | `{"proxy": 497, "dc": 929, "home": 142, "mobile": 102}` |

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
