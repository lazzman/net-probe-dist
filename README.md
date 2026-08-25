# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-25 23:23:38](https://img.shields.io/badge/updated-2026--08--25_23%3A23%3A38-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9228.5s](https://img.shields.io/badge/elapsed-9228.5s-lightgrey)
![profiles: 1967](https://img.shields.io/badge/profiles-1967-blue)
![live_hits: 1976](https://img.shields.io/badge/live__hits-1976-brightgreen)
![live_fail: 69580](https://img.shields.io/badge/live__fail-69580-orange)
![kept: 1353](https://img.shields.io/badge/kept-1353-blue)
![new: 623](https://img.shields.io/badge/new-623-success)
![dropped: 858](https://img.shields.io/badge/dropped-858-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-25 23:23:38 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9228.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `425103` |
| **Live PASS (pool hits)** | `1976` |
| **Live FAIL** | `69580` |
| **History retained** | `1353` |
| **New PASS** | `623` |
| **History dropped** | `858` |
| **Previous public** | `2211` |
| **Published profiles (deduped)** | `1967` |
| **Share links (exportable)** | `1597` |
| **YAML proxies (exportable)** | `1597` |
| **Protocol mix** | `{"hysteria2": 196, "vmess": 57, "vless": 966, "shadowsocks": 329, "trojan": 49}` |
| **Country mix** | `{"GB": 74, "US": 227, "DE": 134, "CA": 328, "PL": 27, "JP": 33, "DZ": 8, "RU": 37, "NL": 312, "SG": 64, "FI": 26, "SE": 16, "CH": 11, "IE": 10, "FR": 34, "NO": 11, "RO": 3, "ES": 7, "IN": 11, "LT": 6, "HK": 35, "KR": 27, "TH": 5, "CN": 4, "IT": 7, "AT": 2, "LV": 17, "EE": 14, "BE": 1, "AL": 3, "HU": 2, "KZ": 14, "CZ": 4, "AE": 1, "SC": 8, "TW": 9, "VI": 2, "VN": 1, "SK": 1, "MD": 1, "MY": 2, "ZA": 3, "TR": 8, "AU": 5, "BR": 10, "UA": 3, "DK": 2, "IS": 1, "CO": 5, "IR": 6, "PH": 1, "BG": 4, "PE": 1, "GE": 1, "SA": 1, "AM": 1, "KG": 1, "CR": 4, "BZ": 1, "AF": 1, "CY": 1}` |
| **Line type mix** | `{"dc": 948, "home": 203, "proxy": 437, "mobile": 11}` |

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
