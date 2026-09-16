# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-16 21:44:02](https://img.shields.io/badge/updated-2026--09--16_21%3A44%3A02-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9851.9s](https://img.shields.io/badge/elapsed-9851.9s-lightgrey)
![profiles: 1603](https://img.shields.io/badge/profiles-1603-blue)
![live_hits: 1604](https://img.shields.io/badge/live__hits-1604-brightgreen)
![live_fail: 75318](https://img.shields.io/badge/live__fail-75318-orange)
![kept: 1076](https://img.shields.io/badge/kept-1076-blue)
![new: 528](https://img.shields.io/badge/new-528-success)
![dropped: 1125](https://img.shields.io/badge/dropped-1125-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-16 21:44:02 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9851.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `425628` |
| **Live PASS (pool hits)** | `1604` |
| **Live FAIL** | `75318` |
| **History retained** | `1076` |
| **New PASS** | `528` |
| **History dropped** | `1125` |
| **Previous public** | `2201` |
| **Published profiles (deduped)** | `1603` |
| **Share links (exportable)** | `1304` |
| **YAML proxies (exportable)** | `1304` |
| **Protocol mix** | `{"trojan": 52, "vmess": 59, "hysteria2": 143, "vless": 821, "shadowsocks": 229}` |
| **Country mix** | `{"NL": 187, "US": 204, "CA": 389, "DE": 48, "IN": 12, "GB": 68, "JP": 36, "RU": 25, "CH": 4, "SE": 8, "ZA": 4, "ID": 1, "RO": 3, "PL": 25, "ES": 7, "FI": 13, "DK": 1, "IT": 8, "AT": 4, "HR": 1, "TW": 22, "EE": 5, "UZ": 2, "AE": 1, "TH": 3, "FR": 26, "SG": 32, "HK": 39, "GR": 2, "GT": 1, "TR": 2, "LT": 9, "KZ": 6, "CZ": 3, "SA": 11, "MY": 4, "NO": 4, "AM": 1, "KR": 31, "DZ": 24, "SC": 3, "AU": 3, "IR": 5, "CN": 2, "CY": 3, "IE": 1, "LV": 11, "CR": 1, "MO": 1, "BG": 1}` |
| **Line type mix** | `{"dc": 865, "proxy": 360, "home": 77, "mobile": 5}` |

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
