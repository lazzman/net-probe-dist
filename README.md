# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-26 05:22:41](https://img.shields.io/badge/updated-2026--08--26_05%3A22%3A41-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9422.5s](https://img.shields.io/badge/elapsed-9422.5s-lightgrey)
![profiles: 1897](https://img.shields.io/badge/profiles-1897-blue)
![live_hits: 1905](https://img.shields.io/badge/live__hits-1905-brightgreen)
![live_fail: 69895](https://img.shields.io/badge/live__fail-69895-orange)
![kept: 1261](https://img.shields.io/badge/kept-1261-blue)
![new: 644](https://img.shields.io/badge/new-644-success)
![dropped: 336](https://img.shields.io/badge/dropped-336-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-26 05:22:41 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9422.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `425415` |
| **Live PASS (pool hits)** | `1905` |
| **Live FAIL** | `69895` |
| **History retained** | `1261` |
| **New PASS** | `644` |
| **History dropped** | `336` |
| **Previous public** | `1597` |
| **Published profiles (deduped)** | `1897` |
| **Share links (exportable)** | `1565` |
| **YAML proxies (exportable)** | `1565` |
| **Protocol mix** | `{"hysteria2": 186, "vmess": 64, "shadowsocks": 291, "trojan": 22, "vless": 1002}` |
| **Country mix** | `{"DE": 129, "US": 224, "PL": 29, "CA": 269, "JP": 31, "DZ": 7, "RU": 48, "GB": 77, "NL": 302, "FI": 29, "SE": 17, "BR": 8, "SG": 63, "IE": 9, "FR": 34, "ZZ": 5, "LT": 9, "TH": 5, "HK": 38, "ES": 5, "CN": 8, "KR": 13, "LV": 22, "EE": 20, "CH": 9, "NO": 12, "HU": 2, "TR": 10, "KZ": 15, "IN": 9, "TW": 12, "KG": 1, "SC": 3, "VI": 2, "VN": 1, "PH": 2, "BG": 9, "CZ": 5, "DK": 4, "GE": 2, "AT": 2, "MD": 1, "ZA": 4, "AL": 3, "AM": 1, "MY": 3, "IS": 1, "IR": 20, "SI": 1, "CO": 4, "RO": 3, "IT": 4, "UA": 3, "AE": 1, "BY": 2, "PE": 1, "SK": 1, "BE": 1, "AU": 4, "CR": 4, "BZ": 1, "AF": 1, "CY": 1}` |
| **Line type mix** | `{"home": 241, "dc": 880, "proxy": 430, "unknown": 5, "mobile": 10}` |

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
