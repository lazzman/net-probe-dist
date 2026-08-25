# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-25 17:28:54](https://img.shields.io/badge/updated-2026--08--25_17%3A28%3A54-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9253.2s](https://img.shields.io/badge/elapsed-9253.2s-lightgrey)
![profiles: 3307](https://img.shields.io/badge/profiles-3307-blue)
![live_hits: 3309](https://img.shields.io/badge/live__hits-3309-brightgreen)
![live_fail: 68038](https://img.shields.io/badge/live__fail-68038-orange)
![kept: 1808](https://img.shields.io/badge/kept-1808-blue)
![new: 1501](https://img.shields.io/badge/new-1501-success)
![dropped: 1014](https://img.shields.io/badge/dropped-1014-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-25 17:28:54 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9253.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `428514` |
| **Live PASS (pool hits)** | `3309` |
| **Live FAIL** | `68038` |
| **History retained** | `1808` |
| **New PASS** | `1501` |
| **History dropped** | `1014` |
| **Previous public** | `2822` |
| **Published profiles (deduped)** | `3307` |
| **Share links (exportable)** | `2211` |
| **YAML proxies (exportable)** | `2211` |
| **Protocol mix** | `{"vless": 1520, "trojan": 68, "hysteria2": 197, "vmess": 67, "shadowsocks": 359}` |
| **Country mix** | `{"NL": 326, "DE": 155, "US": 271, "RU": 88, "GB": 103, "PL": 34, "JP": 39, "CA": 676, "DZ": 8, "SG": 85, "FI": 32, "SE": 16, "CH": 12, "TW": 12, "FR": 33, "IN": 12, "LT": 7, "ES": 4, "ZA": 3, "HK": 69, "TH": 5, "KR": 30, "AT": 4, "SC": 7, "LV": 17, "EE": 12, "KZ": 18, "BE": 1, "TR": 8, "AL": 3, "HU": 2, "IT": 14, "NO": 9, "DK": 2, "VI": 2, "VN": 1, "CO": 8, "MD": 1, "MY": 3, "ZZ": 1, "BR": 20, "UA": 4, "PT": 1, "IS": 1, "CZ": 3, "PH": 2, "AU": 5, "SK": 1, "BY": 1, "AM": 1, "RO": 3, "CL": 1, "IE": 8, "AE": 1, "BZ": 4, "BG": 5, "PE": 1, "CN": 5, "GE": 1, "SA": 1, "IR": 12, "CR": 2, "CY": 1}` |
| **Line type mix** | `{"home": 260, "dc": 1414, "proxy": 534, "mobile": 8, "unknown": 1}` |

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
