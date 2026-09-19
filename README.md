# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-19 21:18:17](https://img.shields.io/badge/updated-2026--09--19_21%3A18%3A17-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9993.1s](https://img.shields.io/badge/elapsed-9993.1s-lightgrey)
![profiles: 2144](https://img.shields.io/badge/profiles-2144-blue)
![live_hits: 2145](https://img.shields.io/badge/live__hits-2145-brightgreen)
![live_fail: 75466](https://img.shields.io/badge/live__fail-75466-orange)
![kept: 1304](https://img.shields.io/badge/kept-1304-blue)
![new: 841](https://img.shields.io/badge/new-841-success)
![dropped: 1216](https://img.shields.io/badge/dropped-1216-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-19 21:18:17 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9993.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `424157` |
| **Live PASS (pool hits)** | `2145` |
| **Live FAIL** | `75466` |
| **History retained** | `1304` |
| **New PASS** | `841` |
| **History dropped** | `1216` |
| **Previous public** | `2520` |
| **Published profiles (deduped)** | `2144` |
| **Share links (exportable)** | `1577` |
| **YAML proxies (exportable)** | `1577` |
| **Protocol mix** | `{"hysteria2": 126, "vmess": 61, "shadowsocks": 268, "vless": 1082, "trojan": 40}` |
| **Country mix** | `{"RU": 28, "GB": 63, "US": 225, "CA": 517, "KR": 27, "DE": 72, "NL": 206, "SE": 19, "SG": 29, "TW": 21, "FR": 32, "ID": 2, "IE": 1, "PL": 22, "ZA": 4, "CH": 6, "ES": 12, "JP": 43, "IN": 12, "AT": 2, "EE": 5, "UZ": 2, "AE": 2, "RO": 3, "FI": 23, "HK": 39, "GR": 2, "TH": 4, "IT": 12, "AL": 3, "SA": 11, "CZ": 12, "CY": 9, "KZ": 13, "UA": 3, "BR": 1, "ME": 2, "TR": 5, "NO": 5, "AM": 2, "MY": 3, "LV": 12, "DZ": 24, "DK": 2, "IL": 2, "AU": 5, "CL": 2, "SC": 3, "BE": 4, "BG": 5, "MX": 3, "IR": 2, "BZ": 3, "QA": 2, "MD": 1, "LT": 6, "CR": 1}` |
| **Line type mix** | `{"dc": 1081, "proxy": 420, "home": 74, "mobile": 6}` |

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
