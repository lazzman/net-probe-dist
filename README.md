# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-29 15:31:54](https://img.shields.io/badge/updated-2026--09--29_15%3A31%3A54-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10297.9s](https://img.shields.io/badge/elapsed-10297.9s-lightgrey)
![profiles: 3643](https://img.shields.io/badge/profiles-3643-blue)
![live_hits: 3643](https://img.shields.io/badge/live__hits-3643-brightgreen)
![live_fail: 75814](https://img.shields.io/badge/live__fail-75814-orange)
![kept: 1450](https://img.shields.io/badge/kept-1450-blue)
![new: 2193](https://img.shields.io/badge/new-2193-success)
![dropped: 467](https://img.shields.io/badge/dropped-467-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-29 15:31:54 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10297.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `435628` |
| **Live PASS (pool hits)** | `3643` |
| **Live FAIL** | `75814` |
| **History retained** | `1450` |
| **New PASS** | `2193` |
| **History dropped** | `467` |
| **Previous public** | `1917` |
| **Published profiles (deduped)** | `3643` |
| **Share links (exportable)** | `2055` |
| **YAML proxies (exportable)** | `2055` |
| **Protocol mix** | `{"vless": 1480, "vmess": 80, "shadowsocks": 298, "hysteria2": 135, "trojan": 62}` |
| **Country mix** | `{"CA": 891, "US": 281, "CZ": 5, "NL": 159, "DE": 86, "GB": 90, "ES": 17, "SG": 54, "FR": 32, "ID": 2, "RO": 6, "ZA": 3, "CH": 9, "PL": 30, "FI": 21, "JP": 47, "SE": 20, "AT": 3, "RU": 38, "LV": 11, "LT": 13, "EE": 8, "HK": 41, "KZ": 6, "AE": 5, "UA": 8, "IL": 1, "IT": 24, "IN": 15, "HU": 2, "KR": 34, "AU": 7, "AD": 1, "SK": 2, "IE": 1, "TW": 6, "MY": 2, "CN": 2, "SC": 6, "NO": 2, "DZ": 29, "AL": 3, "TR": 3, "BG": 10, "TH": 4, "NZ": 1, "PT": 1, "BZ": 4, "BR": 1, "CW": 4, "GT": 1, "GR": 1, "AM": 1, "GE": 1, "MX": 1, "SA": 1, "VG": 1, "CY": 1, "IR": 1, "CR": 2, "OM": 1}` |
| **Line type mix** | `{"dc": 1472, "proxy": 470, "mobile": 21, "home": 100}` |

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
