# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-05 14:03:45](https://img.shields.io/badge/updated-2026--09--05_14%3A03%3A45-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9819.0s](https://img.shields.io/badge/elapsed-9819.0s-lightgrey)
![profiles: 4026](https://img.shields.io/badge/profiles-4026-blue)
![live_hits: 4026](https://img.shields.io/badge/live__hits-4026-brightgreen)
![live_fail: 71838](https://img.shields.io/badge/live__fail-71838-orange)
![kept: 1209](https://img.shields.io/badge/kept-1209-blue)
![new: 2817](https://img.shields.io/badge/new-2817-success)
![dropped: 156](https://img.shields.io/badge/dropped-156-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-05 14:03:45 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9819.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `430224` |
| **Live PASS (pool hits)** | `4026` |
| **Live FAIL** | `71838` |
| **History retained** | `1209` |
| **New PASS** | `2817` |
| **History dropped** | `156` |
| **Previous public** | `1365` |
| **Published profiles (deduped)** | `4026` |
| **Share links (exportable)** | `2181` |
| **YAML proxies (exportable)** | `2181` |
| **Protocol mix** | `{"shadowsocks": 271, "hysteria2": 158, "vless": 1588, "trojan": 88, "vmess": 76}` |
| **Country mix** | `{"NL": 247, "SG": 61, "DE": 95, "GB": 97, "DZ": 20, "AU": 7, "IN": 9, "FI": 37, "RU": 27, "LV": 12, "SE": 17, "US": 271, "TW": 20, "ID": 1, "CA": 899, "PL": 29, "FR": 33, "NO": 25, "CZ": 5, "JP": 58, "TH": 4, "CN": 7, "IT": 12, "AT": 5, "KZ": 10, "EE": 14, "LT": 10, "ES": 10, "IR": 5, "AL": 2, "GR": 2, "TR": 5, "KR": 29, "UZ": 3, "HK": 34, "SA": 1, "AM": 1, "MY": 3, "ZA": 5, "BR": 4, "SC": 7, "IE": 5, "BZ": 4, "UA": 3, "HU": 1, "CH": 3, "AR": 2, "JE": 1, "BG": 5, "AE": 2, "PT": 1, "CW": 3, "BY": 1, "SK": 1, "PH": 2, "EG": 1, "MX": 2, "RO": 3, "CY": 1, "CR": 2}` |
| **Line type mix** | `{"proxy": 479, "dc": 1567, "home": 127, "mobile": 13}` |

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
