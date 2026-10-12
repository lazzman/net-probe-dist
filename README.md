# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-12 15:31:43](https://img.shields.io/badge/updated-2026--10--12_15%3A31%3A43-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10049.0s](https://img.shields.io/badge/elapsed-10049.0s-lightgrey)
![profiles: 3200](https://img.shields.io/badge/profiles-3200-blue)
![live_hits: 3201](https://img.shields.io/badge/live__hits-3201-brightgreen)
![live_fail: 75110](https://img.shields.io/badge/live__fail-75110-orange)
![kept: 1055](https://img.shields.io/badge/kept-1055-blue)
![new: 2146](https://img.shields.io/badge/new-2146-success)
![dropped: 268](https://img.shields.io/badge/dropped-268-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-12 15:31:43 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10049.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `412803` |
| **Live PASS (pool hits)** | `3201` |
| **Live FAIL** | `75110` |
| **History retained** | `1055` |
| **New PASS** | `2146` |
| **History dropped** | `268` |
| **Previous public** | `1323` |
| **Published profiles (deduped)** | `3200` |
| **Share links (exportable)** | `1851` |
| **YAML proxies (exportable)** | `1851` |
| **Protocol mix** | `{"vless": 1194, "shadowsocks": 271, "hysteria2": 144, "trojan": 184, "vmess": 58}` |
| **Country mix** | `{"US": 194, "CA": 687, "LV": 17, "GB": 40, "ZA": 6, "RU": 37, "NL": 202, "HK": 44, "TR": 4, "DE": 99, "FR": 34, "SG": 55, "NO": 1, "IE": 6, "RO": 9, "CH": 49, "JP": 71, "KR": 51, "IN": 13, "AT": 2, "ME": 6, "FI": 25, "PL": 22, "SE": 13, "AE": 7, "EE": 12, "GR": 2, "KZ": 6, "IT": 20, "ZZ": 1, "AM": 2, "MY": 11, "ID": 5, "TW": 6, "CN": 14, "SC": 7, "ES": 11, "SA": 1, "BR": 3, "CZ": 2, "TH": 4, "AU": 7, "UA": 3, "IR": 2, "NZ": 1, "BZ": 4, "CW": 3, "LT": 12, "BG": 8, "AL": 3, "VN": 1, "DK": 1, "MX": 1, "BE": 1, "VG": 1, "CY": 3, "CR": 2, "IL": 1}` |
| **Line type mix** | `{"dc": 1221, "proxy": 446, "home": 145, "mobile": 42, "unknown": 1}` |

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
