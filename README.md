# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-07 14:04:03](https://img.shields.io/badge/updated-2026--09--07_14%3A04%3A03-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9831.6s](https://img.shields.io/badge/elapsed-9831.6s-lightgrey)
![profiles: 4025](https://img.shields.io/badge/profiles-4025-blue)
![live_hits: 4025](https://img.shields.io/badge/live__hits-4025-brightgreen)
![live_fail: 72456](https://img.shields.io/badge/live__fail-72456-orange)
![kept: 1202](https://img.shields.io/badge/kept-1202-blue)
![new: 2823](https://img.shields.io/badge/new-2823-success)
![dropped: 120](https://img.shields.io/badge/dropped-120-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-07 14:04:03 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9831.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `436604` |
| **Live PASS (pool hits)** | `4025` |
| **Live FAIL** | `72456` |
| **History retained** | `1202` |
| **New PASS** | `2823` |
| **History dropped** | `120` |
| **Previous public** | `1322` |
| **Published profiles (deduped)** | `4025` |
| **Share links (exportable)** | `2258` |
| **YAML proxies (exportable)** | `2258` |
| **Protocol mix** | `{"trojan": 73, "hysteria2": 174, "vless": 1640, "shadowsocks": 301, "vmess": 70}` |
| **Country mix** | `{"US": 305, "SG": 65, "GB": 105, "SK": 1, "JP": 60, "KR": 34, "FR": 30, "DZ": 23, "RU": 27, "IN": 7, "AU": 8, "FI": 26, "NL": 222, "DE": 94, "CA": 946, "TW": 19, "ZA": 4, "ID": 1, "NO": 22, "IE": 9, "PL": 39, "ES": 10, "TR": 5, "TH": 3, "CN": 6, "MY": 4, "IT": 19, "AT": 7, "HR": 1, "JE": 1, "KZ": 9, "EE": 11, "CZ": 3, "IR": 2, "AE": 4, "BZ": 4, "HK": 38, "LV": 16, "GR": 2, "UZ": 1, "SE": 14, "LT": 7, "EG": 1, "SA": 1, "SC": 9, "HU": 1, "CH": 2, "AR": 2, "BR": 3, "UA": 4, "NZ": 1, "PT": 1, "BG": 11, "CW": 2, "CY": 2, "CO": 1, "BY": 1, "PH": 1, "AM": 1, "RO": 2, "ZZ": 4, "CR": 2, "GT": 1}` |
| **Line type mix** | `{"dc": 1611, "home": 129, "proxy": 511, "mobile": 12, "unknown": 4}` |

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
