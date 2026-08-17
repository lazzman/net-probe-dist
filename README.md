# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-17 12:21:41](https://img.shields.io/badge/updated-2026--08--17_12%3A21%3A41-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10227.8s](https://img.shields.io/badge/elapsed-10227.8s-lightgrey)
![profiles: 4869](https://img.shields.io/badge/profiles-4869-blue)
![live_hits: 4869](https://img.shields.io/badge/live__hits-4869-brightgreen)
![live_fail: 90896](https://img.shields.io/badge/live__fail-90896-orange)
![kept: 1540](https://img.shields.io/badge/kept-1540-blue)
![new: 3329](https://img.shields.io/badge/new-3329-success)
![dropped: 140](https://img.shields.io/badge/dropped-140-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-17 12:21:41 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10227.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `451983` |
| **Live PASS (pool hits)** | `4869` |
| **Live FAIL** | `90896` |
| **History retained** | `1540` |
| **New PASS** | `3329` |
| **History dropped** | `140` |
| **Previous public** | `1680` |
| **Published profiles (deduped)** | `4869` |
| **Share links (exportable)** | `2980` |
| **YAML proxies (exportable)** | `2980` |
| **Protocol mix** | `{"vless": 2036, "hysteria2": 167, "vmess": 83, "shadowsocks": 213, "trojan": 481}` |
| **Country mix** | `{"CA": 766, "NL": 330, "US": 360, "PL": 46, "AT": 7, "AU": 16, "SG": 108, "DE": 170, "FI": 61, "SE": 27, "IN": 13, "GB": 137, "FR": 54, "DZ": 3, "HK": 83, "TR": 13, "EE": 19, "HU": 4, "RO": 9, "ZA": 4, "NO": 8, "JP": 225, "IT": 12, "IE": 17, "KR": 122, "ES": 19, "SC": 17, "KZ": 16, "PT": 1, "RU": 202, "IR": 7, "BG": 9, "CH": 8, "LV": 7, "CZ": 5, "LT": 8, "TW": 7, "KG": 1, "BY": 2, "GR": 2, "MD": 2, "TH": 4, "CN": 5, "ID": 1, "PH": 2, "CY": 5, "BZ": 8, "CO": 1, "AE": 4, "IL": 1, "NZ": 2, "CW": 5, "UA": 9, "BR": 3, "AL": 3, "SA": 1, "MY": 1, "DK": 2, "ME": 1, "AM": 1, "AF": 1, "CR": 2, "SK": 1, "KH": 1}` |
| **Line type mix** | `{"dc": 1982, "proxy": 763, "home": 235, "mobile": 11}` |

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
