# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-05 20:51:21](https://img.shields.io/badge/updated-2026--09--05_20%3A51%3A21-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9787.4s](https://img.shields.io/badge/elapsed-9787.4s-lightgrey)
![profiles: 1908](https://img.shields.io/badge/profiles-1908-blue)
![live_hits: 1909](https://img.shields.io/badge/live__hits-1909-brightgreen)
![live_fail: 73490](https://img.shields.io/badge/live__fail-73490-orange)
![kept: 1134](https://img.shields.io/badge/kept-1134-blue)
![new: 775](https://img.shields.io/badge/new-775-success)
![dropped: 1047](https://img.shields.io/badge/dropped-1047-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-05 20:51:21 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9787.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `427203` |
| **Live PASS (pool hits)** | `1909` |
| **Live FAIL** | `73490` |
| **History retained** | `1134` |
| **New PASS** | `775` |
| **History dropped** | `1047` |
| **Previous public** | `2181` |
| **Published profiles (deduped)** | `1908` |
| **Share links (exportable)** | `1255` |
| **YAML proxies (exportable)** | `1255` |
| **Protocol mix** | `{"hysteria2": 157, "vless": 744, "shadowsocks": 250, "trojan": 39, "vmess": 65}` |
| **Country mix** | `{"KR": 24, "SG": 55, "LV": 12, "GB": 75, "IN": 8, "AU": 5, "DZ": 19, "FI": 17, "RU": 20, "DE": 68, "SE": 15, "US": 187, "NL": 223, "TW": 17, "RO": 4, "ID": 1, "PL": 26, "FR": 21, "CA": 265, "ZA": 4, "LT": 5, "NO": 19, "ES": 8, "CZ": 3, "TH": 4, "MY": 4, "CN": 5, "JP": 49, "IT": 8, "TR": 6, "KZ": 7, "EE": 8, "IR": 2, "AL": 1, "GR": 2, "HK": 29, "SK": 1, "UZ": 2, "IE": 6, "AT": 3, "AM": 1, "HU": 1, "CH": 3, "SC": 2, "AR": 2, "JE": 1, "AE": 1, "UA": 1, "BY": 1, "PH": 1, "EG": 1, "CO": 1, "CR": 1, "BG": 1, "BR": 1}` |
| **Line type mix** | `{"dc": 762, "proxy": 375, "home": 110, "mobile": 10}` |

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
