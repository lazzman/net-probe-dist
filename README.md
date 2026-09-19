# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-19 14:21:50](https://img.shields.io/badge/updated-2026--09--19_14%3A21%3A50-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9951.8s](https://img.shields.io/badge/elapsed-9951.8s-lightgrey)
![profiles: 4477](https://img.shields.io/badge/profiles-4477-blue)
![live_hits: 4479](https://img.shields.io/badge/live__hits-4479-brightgreen)
![live_fail: 73031](https://img.shields.io/badge/live__fail-73031-orange)
![kept: 1213](https://img.shields.io/badge/kept-1213-blue)
![new: 3266](https://img.shields.io/badge/new-3266-success)
![dropped: 132](https://img.shields.io/badge/dropped-132-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-19 14:21:50 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9951.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `421953` |
| **Live PASS (pool hits)** | `4479` |
| **Live FAIL** | `73031` |
| **History retained** | `1213` |
| **New PASS** | `3266` |
| **History dropped** | `132` |
| **Previous public** | `1345` |
| **Published profiles (deduped)** | `4477` |
| **Share links (exportable)** | `2520` |
| **YAML proxies (exportable)** | `2520` |
| **Protocol mix** | `{"vless": 1920, "trojan": 62, "hysteria2": 124, "shadowsocks": 291, "vmess": 123}` |
| **Country mix** | `{"CA": 1125, "US": 321, "RU": 42, "AU": 6, "GB": 115, "DE": 121, "SE": 21, "NL": 250, "SG": 37, "TW": 22, "ID": 1, "FR": 44, "IE": 1, "RO": 4, "PL": 26, "ZA": 3, "CH": 4, "ES": 15, "JP": 42, "IN": 12, "AT": 4, "EE": 13, "FI": 27, "UZ": 2, "AE": 4, "TH": 6, "HK": 37, "UA": 7, "BG": 8, "CR": 2, "GR": 3, "IT": 17, "AL": 3, "SA": 11, "CZ": 13, "PK": 1, "CY": 11, "KZ": 11, "TR": 7, "ME": 2, "NO": 6, "AM": 2, "LV": 14, "SC": 7, "KR": 35, "DZ": 24, "CL": 1, "DK": 4, "MO": 2, "LT": 5, "BE": 4, "IR": 4, "NZ": 1, "PT": 1, "CN": 2, "BZ": 6, "BR": 1, "CW": 4, "GT": 1, "QA": 2, "BA": 1, "VG": 1, "MY": 2}` |
| **Line type mix** | `{"dc": 1889, "proxy": 526, "home": 109, "mobile": 7}` |

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
