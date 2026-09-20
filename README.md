# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-20 14:38:32](https://img.shields.io/badge/updated-2026--09--20_14%3A38%3A32-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10026.4s](https://img.shields.io/badge/elapsed-10026.4s-lightgrey)
![profiles: 4312](https://img.shields.io/badge/profiles-4312-blue)
![live_hits: 4312](https://img.shields.io/badge/live__hits-4312-brightgreen)
![live_fail: 73533](https://img.shields.io/badge/live__fail-73533-orange)
![kept: 1229](https://img.shields.io/badge/kept-1229-blue)
![new: 3083](https://img.shields.io/badge/new-3083-success)
![dropped: 125](https://img.shields.io/badge/dropped-125-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-20 14:38:32 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10026.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `423156` |
| **Live PASS (pool hits)** | `4312` |
| **Live FAIL** | `73533` |
| **History retained** | `1229` |
| **New PASS** | `3083` |
| **History dropped** | `125` |
| **Previous public** | `1354` |
| **Published profiles (deduped)** | `4312` |
| **Share links (exportable)** | `2378` |
| **YAML proxies (exportable)** | `2378` |
| **Protocol mix** | `{"vmess": 68, "vless": 1824, "hysteria2": 135, "shadowsocks": 284, "trojan": 67}` |
| **Country mix** | `{"GB": 132, "CA": 1057, "AU": 9, "KR": 33, "US": 298, "NL": 214, "RU": 37, "DE": 98, "SE": 22, "AL": 4, "ID": 1, "FR": 39, "RO": 5, "PL": 25, "SG": 37, "ZA": 3, "CH": 5, "IR": 5, "ES": 11, "JP": 45, "IT": 15, "FI": 30, "AT": 3, "HK": 46, "UZ": 2, "TW": 22, "AE": 2, "TH": 5, "CY": 15, "BG": 11, "IN": 13, "CR": 2, "GR": 2, "ZZ": 2, "SA": 11, "CZ": 11, "KZ": 14, "BZ": 9, "EE": 10, "AM": 2, "TR": 5, "ME": 3, "NO": 4, "SC": 9, "DZ": 25, "DK": 2, "BR": 2, "MX": 1, "CL": 2, "LT": 10, "PT": 1, "GT": 1, "MD": 1, "LV": 10, "VG": 1, "MY": 2, "UA": 2}` |
| **Line type mix** | `{"proxy": 522, "dc": 1763, "home": 93, "mobile": 8, "unknown": 2}` |

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
