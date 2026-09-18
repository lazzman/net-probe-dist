# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-19 07:20:03](https://img.shields.io/badge/updated-2026--09--19_07%3A20%3A03-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9900.7s](https://img.shields.io/badge/elapsed-9900.7s-lightgrey)
![profiles: 1738](https://img.shields.io/badge/profiles-1738-blue)
![live_hits: 1739](https://img.shields.io/badge/live__hits-1739-brightgreen)
![live_fail: 75702](https://img.shields.io/badge/live__fail-75702-orange)
![kept: 1145](https://img.shields.io/badge/kept-1145-blue)
![new: 594](https://img.shields.io/badge/new-594-success)
![dropped: 145](https://img.shields.io/badge/dropped-145-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-19 07:20:03 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9900.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `422297` |
| **Live PASS (pool hits)** | `1739` |
| **Live FAIL** | `75702` |
| **History retained** | `1145` |
| **New PASS** | `594` |
| **History dropped** | `145` |
| **Previous public** | `1290` |
| **Published profiles (deduped)** | `1738` |
| **Share links (exportable)** | `1345` |
| **YAML proxies (exportable)** | `1345` |
| **Protocol mix** | `{"hysteria2": 133, "vless": 810, "shadowsocks": 267, "trojan": 19, "vmess": 116}` |
| **Country mix** | `{"RU": 37, "CA": 329, "DE": 77, "DK": 4, "ES": 9, "US": 207, "GB": 52, "SE": 11, "NL": 207, "SG": 30, "ZA": 4, "FR": 31, "IE": 2, "ID": 1, "PL": 23, "TW": 19, "RO": 4, "CH": 4, "JP": 36, "EE": 10, "FI": 20, "UZ": 2, "IN": 11, "AE": 3, "HK": 43, "GR": 2, "TH": 3, "GT": 1, "IT": 11, "AL": 3, "SA": 11, "CY": 10, "KZ": 14, "UA": 2, "TR": 5, "LT": 2, "AT": 1, "ME": 1, "NO": 5, "LV": 14, "KR": 28, "DZ": 24, "CN": 3, "AU": 4, "CZ": 12, "IR": 2, "BZ": 2, "QA": 1, "MO": 1, "AM": 1, "SC": 1, "BA": 1, "BE": 1, "MY": 2, "IL": 1, "BG": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 855, "proxy": 401, "home": 84, "mobile": 7}` |

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
