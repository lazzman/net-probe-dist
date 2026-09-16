# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-16 14:28:02](https://img.shields.io/badge/updated-2026--09--16_14%3A28%3A02-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9752.4s](https://img.shields.io/badge/elapsed-9752.4s-lightgrey)
![profiles: 4080](https://img.shields.io/badge/profiles-4080-blue)
![live_hits: 4080](https://img.shields.io/badge/live__hits-4080-brightgreen)
![live_fail: 72516](https://img.shields.io/badge/live__fail-72516-orange)
![kept: 1043](https://img.shields.io/badge/kept-1043-blue)
![new: 3037](https://img.shields.io/badge/new-3037-success)
![dropped: 197](https://img.shields.io/badge/dropped-197-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-16 14:28:02 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9752.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `422067` |
| **Live PASS (pool hits)** | `4080` |
| **Live FAIL** | `72516` |
| **History retained** | `1043` |
| **New PASS** | `3037` |
| **History dropped** | `197` |
| **Previous public** | `1240` |
| **Published profiles (deduped)** | `4080` |
| **Share links (exportable)** | `2201` |
| **YAML proxies (exportable)** | `2201` |
| **Protocol mix** | `{"vless": 1688, "trojan": 86, "hysteria2": 145, "vmess": 59, "shadowsocks": 223}` |
| **Country mix** | `{"DE": 75, "US": 311, "JP": 38, "NL": 205, "GB": 114, "IN": 13, "RU": 30, "CH": 4, "CA": 1036, "SE": 15, "TW": 19, "AL": 1, "ZA": 4, "ID": 1, "RO": 3, "PL": 25, "ES": 6, "FI": 22, "DK": 1, "IT": 14, "AT": 3, "HR": 1, "EE": 8, "UZ": 2, "CZ": 5, "FR": 30, "SC": 10, "AE": 2, "TH": 5, "SG": 35, "HK": 35, "CR": 2, "GR": 2, "GT": 1, "LT": 9, "TR": 1, "KZ": 7, "SA": 3, "MY": 3, "NO": 4, "AM": 1, "CN": 3, "ZZ": 1, "KR": 27, "DZ": 24, "UA": 3, "BG": 7, "IR": 4, "AU": 5, "NZ": 1, "PT": 1, "CY": 4, "BZ": 4, "BR": 1, "CW": 4, "ME": 1, "IE": 2, "LV": 11, "VG": 1, "MO": 1}` |
| **Line type mix** | `{"dc": 1637, "proxy": 478, "home": 87, "mobile": 8, "unknown": 1}` |

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
