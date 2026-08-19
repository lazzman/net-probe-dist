# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-20 05:13:55](https://img.shields.io/badge/updated-2026--08--20_05%3A13%3A55-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 8936.0s](https://img.shields.io/badge/elapsed-8936.0s-lightgrey)
![profiles: 2857](https://img.shields.io/badge/profiles-2857-blue)
![live_hits: 2857](https://img.shields.io/badge/live__hits-2857-brightgreen)
![live_fail: 65464](https://img.shields.io/badge/live__fail-65464-orange)
![kept: 1494](https://img.shields.io/badge/kept-1494-blue)
![new: 1363](https://img.shields.io/badge/new-1363-success)
![dropped: 299](https://img.shields.io/badge/dropped-299-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-20 05:13:55 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `8936.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `427225` |
| **Live PASS (pool hits)** | `2857` |
| **Live FAIL** | `65464` |
| **History retained** | `1494` |
| **New PASS** | `1363` |
| **History dropped** | `299` |
| **Previous public** | `1793` |
| **Published profiles (deduped)** | `2857` |
| **Share links (exportable)** | `1776` |
| **YAML proxies (exportable)** | `1776` |
| **Protocol mix** | `{"shadowsocks": 251, "vmess": 59, "hysteria2": 184, "vless": 848, "trojan": 434}` |
| **Country mix** | `{"AU": 19, "US": 253, "FR": 60, "NL": 269, "SG": 144, "CA": 178, "SE": 26, "DE": 129, "DZ": 5, "FI": 33, "PL": 50, "IN": 9, "ES": 6, "JP": 264, "CN": 17, "RU": 41, "IT": 6, "GB": 26, "HK": 65, "TR": 9, "IE": 18, "EE": 12, "LV": 10, "CH": 9, "GE": 1, "CZ": 2, "TW": 9, "VN": 2, "BY": 1, "NO": 8, "KR": 29, "CO": 3, "SK": 1, "KZ": 5, "AT": 3, "SC": 3, "MD": 2, "RO": 4, "DK": 2, "PH": 3, "LT": 3, "ZA": 3, "IR": 1, "TH": 4, "BE": 3, "AL": 3, "BR": 7, "UA": 6, "PT": 1, "BG": 1, "AE": 1, "IL": 2, "HU": 1, "SA": 1, "AM": 1, "AF": 1, "MY": 1, "CY": 1}` |
| **Line type mix** | `{"proxy": 517, "dc": 1072, "home": 168, "mobile": 20}` |

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
