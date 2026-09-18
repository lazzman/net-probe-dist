# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-19 02:45:55](https://img.shields.io/badge/updated-2026--09--19_02%3A45%3A55-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9869.7s](https://img.shields.io/badge/elapsed-9869.7s-lightgrey)
![profiles: 1677](https://img.shields.io/badge/profiles-1677-blue)
![live_hits: 1677](https://img.shields.io/badge/live__hits-1677-brightgreen)
![live_fail: 75130](https://img.shields.io/badge/live__fail-75130-orange)
![kept: 1074](https://img.shields.io/badge/kept-1074-blue)
![new: 603](https://img.shields.io/badge/new-603-success)
![dropped: 465](https://img.shields.io/badge/dropped-465-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-19 02:45:55 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9869.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `421332` |
| **Live PASS (pool hits)** | `1677` |
| **Live FAIL** | `75130` |
| **History retained** | `1074` |
| **New PASS** | `603` |
| **History dropped** | `465` |
| **Previous public** | `1539` |
| **Published profiles (deduped)** | `1677` |
| **Share links (exportable)** | `1290` |
| **YAML proxies (exportable)** | `1290` |
| **Protocol mix** | `{"hysteria2": 130, "shadowsocks": 257, "vless": 818, "vmess": 61, "trojan": 24}` |
| **Country mix** | `{"DK": 3, "US": 201, "RU": 32, "CA": 356, "ES": 8, "IN": 10, "DE": 72, "GB": 52, "NL": 192, "SE": 12, "SG": 30, "TW": 18, "ZA": 4, "FR": 30, "ID": 1, "IE": 2, "PL": 22, "JP": 30, "IT": 7, "AT": 2, "EE": 7, "FI": 15, "UZ": 2, "AE": 1, "RO": 3, "HK": 38, "GR": 2, "TH": 2, "GT": 1, "AL": 3, "SA": 11, "CY": 12, "KZ": 12, "CH": 4, "LT": 2, "ME": 1, "NO": 4, "MY": 2, "KR": 20, "DZ": 24, "TR": 4, "MO": 2, "AU": 5, "CZ": 12, "IR": 2, "BZ": 3, "AM": 1, "LV": 9, "SC": 1, "CN": 4, "CR": 1, "CL": 1}` |
| **Line type mix** | `{"proxy": 378, "dc": 839, "home": 69, "mobile": 9}` |

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
