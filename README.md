# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-11 14:07:28](https://img.shields.io/badge/updated-2026--09--11_14%3A07%3A28-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9666.4s](https://img.shields.io/badge/elapsed-9666.4s-lightgrey)
![profiles: 4114](https://img.shields.io/badge/profiles-4114-blue)
![live_hits: 4115](https://img.shields.io/badge/live__hits-4115-brightgreen)
![live_fail: 71836](https://img.shields.io/badge/live__fail-71836-orange)
![kept: 1008](https://img.shields.io/badge/kept-1008-blue)
![new: 3107](https://img.shields.io/badge/new-3107-success)
![dropped: 94](https://img.shields.io/badge/dropped-94-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-11 14:07:28 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9666.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `424032` |
| **Live PASS (pool hits)** | `4115` |
| **Live FAIL** | `71836` |
| **History retained** | `1008` |
| **New PASS** | `3107` |
| **History dropped** | `94` |
| **Previous public** | `1102` |
| **Published profiles (deduped)** | `4114` |
| **Share links (exportable)** | `2317` |
| **YAML proxies (exportable)** | `2317` |
| **Protocol mix** | `{"vless": 1713, "vmess": 107, "hysteria2": 155, "trojan": 77, "shadowsocks": 265}` |
| **Country mix** | `{"GB": 77, "CA": 1094, "US": 267, "PL": 38, "JP": 38, "NL": 215, "DE": 96, "SG": 44, "AU": 6, "IN": 10, "DZ": 22, "RU": 34, "FI": 25, "TW": 16, "ID": 1, "FR": 35, "NO": 3, "RO": 4, "ES": 8, "IE": 9, "MY": 4, "CN": 6, "IT": 18, "HR": 1, "LV": 13, "KZ": 12, "EE": 11, "SE": 13, "TR": 10, "SC": 8, "AE": 4, "CH": 5, "HK": 77, "GR": 2, "SK": 1, "ZZ": 3, "EG": 1, "SA": 1, "LT": 14, "KR": 29, "TH": 2, "UZ": 2, "ZA": 3, "DK": 2, "BG": 6, "UA": 5, "IR": 2, "NZ": 1, "PT": 4, "BZ": 3, "CW": 5, "GT": 1, "ME": 1, "PH": 1, "CZ": 2, "AT": 3, "AM": 1, "BE": 1, "CY": 1, "BR": 1, "CR": 2, "VG": 1}` |
| **Line type mix** | `{"dc": 1749, "home": 106, "proxy": 457, "mobile": 10, "unknown": 3}` |

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
