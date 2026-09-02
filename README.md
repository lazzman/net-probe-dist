# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-02 21:34:43](https://img.shields.io/badge/updated-2026--09--02_21%3A34%3A43-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9729.1s](https://img.shields.io/badge/elapsed-9729.1s-lightgrey)
![profiles: 2422](https://img.shields.io/badge/profiles-2422-blue)
![live_hits: 2422](https://img.shields.io/badge/live__hits-2422-brightgreen)
![live_fail: 72536](https://img.shields.io/badge/live__fail-72536-orange)
![kept: 1386](https://img.shields.io/badge/kept-1386-blue)
![new: 1036](https://img.shields.io/badge/new-1036-success)
![dropped: 1121](https://img.shields.io/badge/dropped-1121-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-02 21:34:43 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9729.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `428134` |
| **Live PASS (pool hits)** | `2422` |
| **Live FAIL** | `72536` |
| **History retained** | `1386` |
| **New PASS** | `1036` |
| **History dropped** | `1121` |
| **Previous public** | `2507` |
| **Published profiles (deduped)** | `2422` |
| **Share links (exportable)** | `1608` |
| **YAML proxies (exportable)** | `1608` |
| **Protocol mix** | `{"hysteria2": 204, "shadowsocks": 261, "vless": 1041, "trojan": 26, "vmess": 76}` |
| **Country mix** | `{"PL": 27, "KR": 32, "FI": 32, "SG": 72, "CA": 370, "DZ": 18, "GB": 78, "US": 254, "RU": 42, "DE": 86, "SE": 11, "NL": 237, "TW": 22, "HK": 44, "FR": 30, "ZA": 4, "ES": 7, "TH": 4, "MY": 5, "CN": 7, "JP": 59, "IT": 9, "KZ": 12, "EE": 4, "NO": 20, "IN": 9, "LV": 17, "CH": 9, "CZ": 3, "IR": 3, "UA": 3, "TR": 3, "AE": 4, "LT": 13, "GR": 3, "AL": 4, "SA": 1, "UZ": 2, "RO": 6, "IE": 2, "ID": 1, "PH": 3, "CO": 4, "HR": 1, "AT": 2, "SC": 3, "JE": 1, "AR": 2, "BR": 9, "AU": 6, "MX": 3, "BG": 2, "MD": 1, "SK": 1, "EG": 1, "AM": 1, "ZZ": 1, "BY": 1, "CR": 1}` |
| **Line type mix** | `{"proxy": 427, "dc": 1040, "home": 136, "mobile": 8, "unknown": 1}` |

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
