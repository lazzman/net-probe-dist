# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-11 01:38:05](https://img.shields.io/badge/updated-2026--11--11_01%3A38%3A05-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11374.7s](https://img.shields.io/badge/elapsed-11374.7s-lightgrey)
![profiles: 1263](https://img.shields.io/badge/profiles-1263-blue)
![live_hits: 1263](https://img.shields.io/badge/live__hits-1263-brightgreen)
![live_fail: 87316](https://img.shields.io/badge/live__fail-87316-orange)
![kept: 895](https://img.shields.io/badge/kept-895-blue)
![new: 368](https://img.shields.io/badge/new-368-success)
![dropped: 476](https://img.shields.io/badge/dropped-476-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-11 01:38:05 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11374.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `400746` |
| **Live PASS (pool hits)** | `1263` |
| **Live FAIL** | `87316` |
| **History retained** | `895` |
| **New PASS** | `368` |
| **History dropped** | `476` |
| **Previous public** | `1371` |
| **Published profiles (deduped)** | `1263` |
| **Share links (exportable)** | `1115` |
| **YAML proxies (exportable)** | `1115` |
| **Protocol mix** | `{"hysteria2": 143, "shadowsocks": 368, "trojan": 85, "vless": 406, "vmess": 113}` |
| **Country mix** | `{"DE": 69, "JP": 18, "CA": 90, "BY": 8, "US": 262, "LV": 4, "PL": 73, "NL": 144, "HK": 23, "NO": 1, "AT": 4, "IE": 1, "RO": 5, "ZA": 2, "ES": 21, "GB": 44, "BG": 16, "KR": 28, "RU": 23, "FR": 41, "SG": 58, "IT": 27, "CH": 56, "IN": 5, "BR": 3, "CL": 1, "IL": 1, "TH": 2, "SE": 21, "AE": 2, "TR": 7, "LT": 11, "FI": 9, "EE": 4, "CR": 1, "UA": 1, "TW": 4, "MX": 3, "AU": 4, "KZ": 3, "AL": 3, "NG": 1, "IR": 5, "GR": 1, "HU": 1, "DK": 1, "MY": 1, "ID": 1, "SA": 1}` |
| **Line type mix** | `{"dc": 444, "proxy": 463, "home": 88, "mobile": 120}` |

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
