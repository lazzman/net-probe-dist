# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-06 01:17:05](https://img.shields.io/badge/updated-2026--11--06_01%3A17%3A05-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11298.0s](https://img.shields.io/badge/elapsed-11298.0s-lightgrey)
![profiles: 1217](https://img.shields.io/badge/profiles-1217-blue)
![live_hits: 1217](https://img.shields.io/badge/live__hits-1217-brightgreen)
![live_fail: 86882](https://img.shields.io/badge/live__fail-86882-orange)
![kept: 806](https://img.shields.io/badge/kept-806-blue)
![new: 411](https://img.shields.io/badge/new-411-success)
![dropped: 211](https://img.shields.io/badge/dropped-211-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-06 01:17:05 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11298.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `402932` |
| **Live PASS (pool hits)** | `1217` |
| **Live FAIL** | `86882` |
| **History retained** | `806` |
| **New PASS** | `411` |
| **History dropped** | `211` |
| **Previous public** | `1017` |
| **Published profiles (deduped)** | `1217` |
| **Share links (exportable)** | `1026` |
| **YAML proxies (exportable)** | `1026` |
| **Protocol mix** | `{"vless": 398, "shadowsocks": 285, "hysteria2": 141, "trojan": 94, "vmess": 108}` |
| **Country mix** | `{"MX": 4, "ES": 11, "PL": 23, "DE": 58, "CA": 121, "BY": 8, "US": 284, "NL": 146, "NO": 1, "AT": 3, "RO": 3, "ZA": 2, "GB": 28, "JP": 26, "BG": 9, "RU": 17, "IT": 19, "IN": 6, "FR": 40, "SG": 50, "KR": 21, "CL": 1, "CH": 55, "SE": 11, "TR": 9, "UA": 2, "EE": 4, "FI": 10, "HK": 15, "AE": 2, "HU": 2, "MY": 2, "IR": 1, "TW": 3, "AU": 2, "PT": 1, "IL": 1, "BR": 3, "LV": 3, "KZ": 2, "CZ": 1, "GR": 1, "DK": 1, "VN": 1, "AL": 2, "TH": 1, "CR": 1, "SA": 1, "LT": 9}` |
| **Line type mix** | `{"dc": 450, "proxy": 376, "mobile": 120, "home": 81}` |

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
