# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-13 11:06:15](https://img.shields.io/badge/updated-2026--10--13_11%3A06%3A15-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10097.6s](https://img.shields.io/badge/elapsed-10097.6s-lightgrey)
![profiles: 3668](https://img.shields.io/badge/profiles-3668-blue)
![live_hits: 3668](https://img.shields.io/badge/live__hits-3668-brightgreen)
![live_fail: 75141](https://img.shields.io/badge/live__fail-75141-orange)
![kept: 894](https://img.shields.io/badge/kept-894-blue)
![new: 2774](https://img.shields.io/badge/new-2774-success)
![dropped: 169](https://img.shields.io/badge/dropped-169-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-13 11:06:15 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10097.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `414722` |
| **Live PASS (pool hits)** | `3668` |
| **Live FAIL** | `75141` |
| **History retained** | `894` |
| **New PASS** | `2774` |
| **History dropped** | `169` |
| **Previous public** | `1063` |
| **Published profiles (deduped)** | `3668` |
| **Share links (exportable)** | `2056` |
| **YAML proxies (exportable)** | `2056` |
| **Protocol mix** | `{"vless": 1435, "shadowsocks": 280, "hysteria2": 117, "trojan": 169, "vmess": 55}` |
| **Country mix** | `{"CA": 862, "US": 226, "ZA": 7, "GB": 46, "RU": 41, "NL": 190, "HK": 59, "DE": 96, "FR": 33, "IE": 7, "RO": 3, "CH": 41, "SG": 59, "JP": 78, "IN": 11, "KR": 49, "IT": 22, "AT": 2, "FI": 16, "LV": 13, "TW": 5, "EE": 11, "PL": 22, "AE": 5, "TH": 5, "SE": 15, "ES": 11, "KZ": 6, "IL": 1, "MY": 9, "SA": 1, "ME": 7, "LT": 12, "AM": 1, "ID": 3, "CN": 3, "SC": 8, "GR": 2, "CR": 4, "ZZ": 1, "NO": 1, "UA": 6, "MX": 2, "TR": 5, "CZ": 2, "AU": 7, "IR": 5, "BR": 5, "NZ": 1, "BZ": 7, "CW": 4, "CY": 4, "BG": 11, "AL": 3, "VN": 2, "UZ": 1, "BE": 1, "DK": 1, "VG": 1, "PT": 1, "MD": 1}` |
| **Line type mix** | `{"dc": 1428, "proxy": 465, "home": 126, "mobile": 44, "unknown": 1}` |

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
