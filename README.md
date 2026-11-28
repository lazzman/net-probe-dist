# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-28 12:27:58](https://img.shields.io/badge/updated-2026--11--28_12%3A27%3A58-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11488.8s](https://img.shields.io/badge/elapsed-11488.8s-lightgrey)
![profiles: 1791](https://img.shields.io/badge/profiles-1791-blue)
![live_hits: 1791](https://img.shields.io/badge/live__hits-1791-brightgreen)
![live_fail: 87969](https://img.shields.io/badge/live__fail-87969-orange)
![kept: 809](https://img.shields.io/badge/kept-809-blue)
![new: 982](https://img.shields.io/badge/new-982-success)
![dropped: 105](https://img.shields.io/badge/dropped-105-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-28 12:27:58 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11488.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `401133` |
| **Live PASS (pool hits)** | `1791` |
| **Live FAIL** | `87969` |
| **History retained** | `809` |
| **New PASS** | `982` |
| **History dropped** | `105` |
| **Previous public** | `914` |
| **Published profiles (deduped)** | `1791` |
| **Share links (exportable)** | `1484` |
| **YAML proxies (exportable)** | `1484` |
| **Protocol mix** | `{"hysteria2": 67, "shadowsocks": 440, "vless": 824, "vmess": 141, "trojan": 12}` |
| **Country mix** | `{"AE": 8, "NL": 136, "US": 286, "IT": 19, "HK": 44, "DE": 93, "GB": 48, "FR": 52, "AL": 2, "AT": 3, "NO": 2, "CA": 308, "ZA": 4, "IE": 3, "TR": 35, "JP": 138, "PL": 18, "ES": 27, "LV": 9, "BG": 10, "LT": 10, "KR": 16, "RU": 31, "FI": 14, "SE": 15, "SG": 51, "CH": 10, "IN": 6, "BY": 7, "KZ": 4, "GR": 1, "CR": 5, "VN": 2, "SK": 3, "RO": 4, "SA": 1, "MY": 2, "BR": 10, "CN": 1, "TW": 5, "TH": 1, "IR": 8, "NE": 3, "EE": 10, "AU": 4, "IL": 2, "MX": 1, "BZ": 2, "UA": 4, "LY": 1, "MD": 3, "BE": 3, "AM": 1, "SC": 2, "DK": 1, "AR": 1, "CY": 1}` |
| **Line type mix** | `{"dc": 895, "proxy": 439, "home": 127, "mobile": 30}` |

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
