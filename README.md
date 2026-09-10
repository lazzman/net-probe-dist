# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-10 14:12:05](https://img.shields.io/badge/updated-2026--09--10_14%3A12%3A05-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9729.4s](https://img.shields.io/badge/elapsed-9729.4s-lightgrey)
![profiles: 3900](https://img.shields.io/badge/profiles-3900-blue)
![live_hits: 3900](https://img.shields.io/badge/live__hits-3900-brightgreen)
![live_fail: 72024](https://img.shields.io/badge/live__fail-72024-orange)
![kept: 1010](https://img.shields.io/badge/kept-1010-blue)
![new: 2890](https://img.shields.io/badge/new-2890-success)
![dropped: 168](https://img.shields.io/badge/dropped-168-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-10 14:12:05 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9729.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `424908` |
| **Live PASS (pool hits)** | `3900` |
| **Live FAIL** | `72024` |
| **History retained** | `1010` |
| **New PASS** | `2890` |
| **History dropped** | `168` |
| **Previous public** | `1178` |
| **Published profiles (deduped)** | `3900` |
| **Share links (exportable)** | `2064` |
| **YAML proxies (exportable)** | `2064` |
| **Protocol mix** | `{"vless": 1515, "vmess": 72, "hysteria2": 155, "shadowsocks": 257, "trojan": 65}` |
| **Country mix** | `{"DE": 84, "US": 247, "JP": 41, "GB": 82, "CA": 874, "DZ": 20, "RU": 36, "FI": 32, "NL": 216, "SG": 47, "TW": 17, "ID": 1, "AL": 1, "AE": 3, "FR": 32, "RO": 6, "PL": 35, "ES": 13, "CN": 5, "MY": 4, "IE": 6, "IN": 8, "IT": 18, "KR": 33, "AT": 4, "HR": 1, "SC": 9, "KZ": 9, "NO": 15, "EE": 8, "CZ": 3, "TR": 10, "LV": 13, "CH": 4, "JE": 1, "HK": 52, "GR": 2, "IR": 3, "UZ": 2, "SK": 1, "AU": 6, "SE": 13, "LT": 15, "EG": 1, "SA": 1, "TH": 4, "ZA": 4, "DK": 1, "AR": 2, "UA": 6, "PT": 1, "BZ": 4, "GT": 1, "PH": 1, "AM": 1, "BG": 5, "NZ": 1, "CW": 2, "CY": 1, "CR": 2, "VG": 1}` |
| **Line type mix** | `{"dc": 1462, "home": 124, "proxy": 474, "mobile": 11}` |

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
