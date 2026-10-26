# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-26 23:28:24](https://img.shields.io/badge/updated-2026--10--26_23%3A28%3A24-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11010.6s](https://img.shields.io/badge/elapsed-11010.6s-lightgrey)
![profiles: 1193](https://img.shields.io/badge/profiles-1193-blue)
![live_hits: 1193](https://img.shields.io/badge/live__hits-1193-brightgreen)
![live_fail: 85495](https://img.shields.io/badge/live__fail-85495-orange)
![kept: 804](https://img.shields.io/badge/kept-804-blue)
![new: 389](https://img.shields.io/badge/new-389-success)
![dropped: 525](https://img.shields.io/badge/dropped-525-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-26 23:28:24 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11010.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `416611` |
| **Live PASS (pool hits)** | `1193` |
| **Live FAIL** | `85495` |
| **History retained** | `804` |
| **New PASS** | `389` |
| **History dropped** | `525` |
| **Previous public** | `1329` |
| **Published profiles (deduped)** | `1193` |
| **Share links (exportable)** | `1012` |
| **YAML proxies (exportable)** | `1012` |
| **Protocol mix** | `{"shadowsocks": 248, "hysteria2": 120, "trojan": 84, "vless": 493, "vmess": 67}` |
| **Country mix** | `{"IT": 13, "GB": 34, "US": 153, "DE": 68, "NL": 172, "HK": 32, "TR": 13, "ZA": 3, "RO": 2, "CH": 44, "BG": 9, "JP": 26, "AL": 1, "IN": 9, "CA": 206, "KR": 23, "AT": 7, "ME": 3, "LV": 4, "CR": 1, "LT": 8, "FR": 23, "PL": 14, "FI": 13, "SG": 36, "RU": 27, "TH": 2, "MD": 2, "AE": 3, "SE": 7, "CZ": 1, "IL": 1, "AM": 2, "TW": 4, "CL": 1, "MX": 3, "UA": 3, "KZ": 4, "NO": 1, "BY": 6, "ES": 6, "SC": 3, "EE": 6, "AU": 3, "LU": 1, "RS": 1, "GR": 1, "MY": 3, "ID": 1, "PH": 1, "CN": 2, "SA": 1}` |
| **Line type mix** | `{"dc": 590, "proxy": 286, "mobile": 61, "home": 76}` |

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
