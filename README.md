# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-09 09:48:53](https://img.shields.io/badge/updated-2026--10--09_09%3A48%3A53-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9944.9s](https://img.shields.io/badge/elapsed-9944.9s-lightgrey)
![profiles: 1630](https://img.shields.io/badge/profiles-1630-blue)
![live_hits: 1630](https://img.shields.io/badge/live__hits-1630-brightgreen)
![live_fail: 76053](https://img.shields.io/badge/live__fail-76053-orange)
![kept: 871](https://img.shields.io/badge/kept-871-blue)
![new: 759](https://img.shields.io/badge/new-759-success)
![dropped: 208](https://img.shields.io/badge/dropped-208-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-09 09:48:53 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9944.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `412235` |
| **Live PASS (pool hits)** | `1630` |
| **Live FAIL** | `76053` |
| **History retained** | `871` |
| **New PASS** | `759` |
| **History dropped** | `208` |
| **Previous public** | `1079` |
| **Published profiles (deduped)** | `1630` |
| **Share links (exportable)** | `1342` |
| **YAML proxies (exportable)** | `1342` |
| **Protocol mix** | `{"shadowsocks": 279, "vless": 780, "hysteria2": 106, "trojan": 106, "vmess": 71}` |
| **Country mix** | `{"ZA": 5, "US": 186, "CA": 289, "NL": 180, "GB": 36, "ID": 3, "DE": 104, "IE": 6, "FR": 38, "RO": 6, "CH": 11, "SG": 54, "FI": 26, "JP": 61, "IN": 9, "IT": 22, "KR": 42, "AT": 2, "EE": 14, "TW": 4, "TR": 16, "SE": 6, "PL": 18, "HK": 54, "UZ": 1, "RU": 25, "MY": 11, "LV": 26, "AM": 1, "ES": 12, "AU": 5, "TH": 3, "SC": 4, "BE": 2, "PT": 1, "GR": 3, "AL": 3, "KZ": 5, "AE": 3, "VN": 3, "BG": 10, "CZ": 2, "LT": 9, "UA": 2, "IS": 1, "SA": 1, "CN": 15, "IL": 1, "BZ": 1, "ME": 2, "CR": 1, "MD": 1, "BR": 1, "SK": 1}` |
| **Line type mix** | `{"dc": 840, "proxy": 384, "home": 115, "mobile": 9}` |

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
