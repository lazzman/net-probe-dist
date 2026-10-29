# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-29 23:33:47](https://img.shields.io/badge/updated-2026--10--29_23%3A33%3A47-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11185.2s](https://img.shields.io/badge/elapsed-11185.2s-lightgrey)
![profiles: 1182](https://img.shields.io/badge/profiles-1182-blue)
![live_hits: 1182](https://img.shields.io/badge/live__hits-1182-brightgreen)
![live_fail: 86787](https://img.shields.io/badge/live__fail-86787-orange)
![kept: 821](https://img.shields.io/badge/kept-821-blue)
![new: 361](https://img.shields.io/badge/new-361-success)
![dropped: 432](https://img.shields.io/badge/dropped-432-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-29 23:33:47 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11185.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `424947` |
| **Live PASS (pool hits)** | `1182` |
| **Live FAIL** | `86787` |
| **History retained** | `821` |
| **New PASS** | `361` |
| **History dropped** | `432` |
| **Previous public** | `1253` |
| **Published profiles (deduped)** | `1182` |
| **Share links (exportable)** | `1016` |
| **YAML proxies (exportable)** | `1016` |
| **Protocol mix** | `{"shadowsocks": 263, "hysteria2": 103, "trojan": 147, "vless": 433, "vmess": 70}` |
| **Country mix** | `{"IT": 14, "NL": 172, "US": 183, "GB": 25, "PL": 10, "FI": 17, "RO": 3, "ZA": 3, "AL": 2, "DE": 54, "CA": 202, "JP": 19, "SG": 42, "BG": 12, "LT": 13, "FR": 29, "IN": 10, "KR": 24, "RU": 21, "MX": 5, "AU": 7, "ES": 6, "HU": 1, "CR": 1, "AT": 1, "SC": 3, "HK": 33, "UA": 3, "TH": 3, "TR": 4, "IL": 6, "SE": 4, "KZ": 5, "DK": 1, "BR": 2, "EE": 2, "MY": 2, "PH": 2, "CH": 44, "AM": 1, "CN": 1, "NO": 1, "LV": 6, "IR": 2, "BY": 6, "AE": 3, "LU": 1, "MD": 1, "VN": 1, "CZ": 1, "ID": 1, "SA": 1}` |
| **Line type mix** | `{"dc": 534, "proxy": 293, "home": 80, "mobile": 109}` |

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
