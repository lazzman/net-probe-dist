# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-18 03:10:46](https://img.shields.io/badge/updated-2026--09--18_03%3A10%3A46-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9891.5s](https://img.shields.io/badge/elapsed-9891.5s-lightgrey)
![profiles: 1552](https://img.shields.io/badge/profiles-1552-blue)
![live_hits: 1554](https://img.shields.io/badge/live__hits-1554-brightgreen)
![live_fail: 75103](https://img.shields.io/badge/live__fail-75103-orange)
![kept: 1040](https://img.shields.io/badge/kept-1040-blue)
![new: 514](https://img.shields.io/badge/new-514-success)
![dropped: 388](https://img.shields.io/badge/dropped-388-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-18 03:10:46 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9891.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `422187` |
| **Live PASS (pool hits)** | `1554` |
| **Live FAIL** | `75103` |
| **History retained** | `1040` |
| **New PASS** | `514` |
| **History dropped** | `388` |
| **Previous public** | `1428` |
| **Published profiles (deduped)** | `1552` |
| **Share links (exportable)** | `1197` |
| **YAML proxies (exportable)** | `1197` |
| **Protocol mix** | `{"hysteria2": 140, "vless": 709, "shadowsocks": 262, "vmess": 56, "trojan": 30}` |
| **Country mix** | `{"IN": 11, "AU": 3, "DE": 54, "CA": 315, "US": 204, "JP": 38, "GB": 55, "RU": 25, "SE": 10, "NL": 198, "SG": 24, "TW": 20, "AL": 1, "FR": 26, "PL": 22, "ZA": 3, "RO": 4, "ES": 9, "IT": 8, "AT": 2, "EE": 9, "FI": 13, "UZ": 2, "AE": 3, "HK": 27, "GR": 2, "TH": 3, "TR": 4, "SA": 11, "CY": 6, "KZ": 7, "LT": 4, "NO": 4, "LV": 8, "MY": 2, "KR": 23, "IE": 1, "CH": 4, "MO": 1, "AM": 1, "DZ": 23, "DK": 2, "SC": 2, "CO": 1, "CZ": 2, "BZ": 1, "ME": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 780, "proxy": 337, "home": 77, "mobile": 6}` |

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
