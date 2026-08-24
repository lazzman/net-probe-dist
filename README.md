# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-24 17:36:39](https://img.shields.io/badge/updated-2026--08--24_17%3A36%3A39-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9074.2s](https://img.shields.io/badge/elapsed-9074.2s-lightgrey)
![profiles: 3438](https://img.shields.io/badge/profiles-3438-blue)
![live_hits: 3441](https://img.shields.io/badge/live__hits-3441-brightgreen)
![live_fail: 66876](https://img.shields.io/badge/live__fail-66876-orange)
![kept: 1719](https://img.shields.io/badge/kept-1719-blue)
![new: 1722](https://img.shields.io/badge/new-1722-success)
![dropped: 907](https://img.shields.io/badge/dropped-907-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-24 17:36:39 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9074.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `425157` |
| **Live PASS (pool hits)** | `3441` |
| **Live FAIL** | `66876` |
| **History retained** | `1719` |
| **New PASS** | `1722` |
| **History dropped** | `907` |
| **Previous public** | `2626` |
| **Published profiles (deduped)** | `3438` |
| **Share links (exportable)** | `2062` |
| **YAML proxies (exportable)** | `2062` |
| **Protocol mix** | `{"vmess": 54, "vless": 1428, "shadowsocks": 332, "hysteria2": 196, "trojan": 52}` |
| **Country mix** | `{"US": 242, "CA": 636, "NL": 309, "AU": 7, "DE": 157, "JP": 40, "PL": 29, "RU": 55, "SG": 75, "FI": 32, "SE": 21, "TW": 10, "TR": 10, "FR": 39, "IN": 14, "GB": 74, "ZA": 3, "LT": 10, "NO": 6, "HK": 81, "IE": 7, "TH": 4, "CN": 5, "KR": 23, "AT": 2, "BE": 1, "CH": 10, "AL": 5, "IT": 18, "KZ": 13, "VN": 1, "LV": 13, "BZ": 4, "MD": 2, "BR": 25, "DK": 2, "AM": 1, "SC": 13, "EE": 12, "BY": 2, "ES": 8, "UA": 5, "CZ": 4, "AE": 3, "RO": 3, "CL": 1, "BG": 8, "PE": 1, "HU": 1, "CO": 2, "PH": 1, "SK": 1, "IR": 3, "VI": 2, "CR": 6, "GE": 1, "AF": 1, "MY": 1, "DZ": 3, "CY": 1}` |
| **Line type mix** | `{"home": 226, "dc": 1311, "proxy": 522, "mobile": 10}` |

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
