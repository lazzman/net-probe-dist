# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-27 12:45:04](https://img.shields.io/badge/updated-2026--11--27_12%3A45%3A04-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11479.7s](https://img.shields.io/badge/elapsed-11479.7s-lightgrey)
![profiles: 1499](https://img.shields.io/badge/profiles-1499-blue)
![live_hits: 1499](https://img.shields.io/badge/live__hits-1499-brightgreen)
![live_fail: 88346](https://img.shields.io/badge/live__fail-88346-orange)
![kept: 917](https://img.shields.io/badge/kept-917-blue)
![new: 582](https://img.shields.io/badge/new-582-success)
![dropped: 145](https://img.shields.io/badge/dropped-145-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-27 12:45:04 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11479.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `400893` |
| **Live PASS (pool hits)** | `1499` |
| **Live FAIL** | `88346` |
| **History retained** | `917` |
| **New PASS** | `582` |
| **History dropped** | `145` |
| **Previous public** | `1062` |
| **Published profiles (deduped)** | `1499` |
| **Share links (exportable)** | `1346` |
| **YAML proxies (exportable)** | `1346` |
| **Protocol mix** | `{"hysteria2": 76, "shadowsocks": 428, "vless": 607, "trojan": 96, "vmess": 139}` |
| **Country mix** | `{"AE": 5, "IT": 20, "US": 308, "DE": 79, "HK": 37, "SG": 43, "NL": 123, "FR": 46, "AL": 3, "NO": 1, "AT": 2, "CA": 246, "TR": 34, "ZA": 5, "GB": 40, "ES": 31, "JP": 119, "PL": 16, "LT": 11, "BG": 11, "KR": 16, "RU": 29, "FI": 8, "SE": 11, "IN": 4, "CH": 19, "BR": 11, "KZ": 4, "BY": 6, "CZ": 2, "VN": 2, "NE": 5, "RO": 5, "CN": 1, "TW": 3, "AU": 5, "IL": 3, "LV": 8, "GR": 1, "SK": 3, "TH": 1, "MY": 2, "IR": 4, "IE": 2, "CR": 4, "EE": 5, "SA": 1, "SC": 2, "UA": 1}` |
| **Line type mix** | `{"dc": 706, "proxy": 424, "mobile": 100, "home": 118}` |

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
