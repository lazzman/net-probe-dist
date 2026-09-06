# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-07 06:55:09](https://img.shields.io/badge/updated-2026--09--07_06%3A55%3A09-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9901.0s](https://img.shields.io/badge/elapsed-9901.0s-lightgrey)
![profiles: 1920](https://img.shields.io/badge/profiles-1920-blue)
![live_hits: 1920](https://img.shields.io/badge/live__hits-1920-brightgreen)
![live_fail: 74426](https://img.shields.io/badge/live__fail-74426-orange)
![kept: 1185](https://img.shields.io/badge/kept-1185-blue)
![new: 735](https://img.shields.io/badge/new-735-success)
![dropped: 149](https://img.shields.io/badge/dropped-149-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-07 06:55:09 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9901.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `435194` |
| **Live PASS (pool hits)** | `1920` |
| **Live FAIL** | `74426` |
| **History retained** | `1185` |
| **New PASS** | `735` |
| **History dropped** | `149` |
| **Previous public** | `1334` |
| **Published profiles (deduped)** | `1920` |
| **Share links (exportable)** | `1322` |
| **YAML proxies (exportable)** | `1322` |
| **Protocol mix** | `{"hysteria2": 184, "vless": 761, "trojan": 17, "shadowsocks": 300, "vmess": 60}` |
| **Country mix** | `{"JP": 57, "SE": 9, "US": 195, "SG": 56, "KR": 31, "CA": 260, "GB": 79, "FR": 28, "AU": 6, "IN": 6, "DZ": 23, "RU": 20, "FI": 34, "DE": 58, "NL": 221, "TW": 17, "IE": 10, "PL": 41, "RO": 3, "ES": 6, "TH": 5, "CN": 4, "MY": 4, "IT": 13, "HR": 1, "AT": 6, "KZ": 9, "NO": 21, "EE": 6, "CZ": 4, "IR": 2, "JE": 1, "LV": 15, "GR": 2, "HK": 31, "UZ": 2, "LT": 7, "TR": 4, "SA": 1, "AM": 1, "ZA": 4, "AE": 1, "HU": 1, "CH": 2, "AR": 2, "UA": 2, "CO": 1, "BY": 1, "PH": 1, "BR": 2, "EG": 1, "SC": 1, "BG": 5}` |
| **Line type mix** | `{"dc": 803, "proxy": 399, "home": 111, "mobile": 10}` |

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
