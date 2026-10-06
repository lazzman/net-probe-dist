# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-06 10:50:40](https://img.shields.io/badge/updated-2026--10--06_10%3A50%3A40-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10250.9s](https://img.shields.io/badge/elapsed-10250.9s-lightgrey)
![profiles: 3751](https://img.shields.io/badge/profiles-3751-blue)
![live_hits: 3751](https://img.shields.io/badge/live__hits-3751-brightgreen)
![live_fail: 76480](https://img.shields.io/badge/live__fail-76480-orange)
![kept: 1034](https://img.shields.io/badge/kept-1034-blue)
![new: 2717](https://img.shields.io/badge/new-2717-success)
![dropped: 134](https://img.shields.io/badge/dropped-134-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-06 10:50:40 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10250.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `432448` |
| **Live PASS (pool hits)** | `3751` |
| **Live FAIL** | `76480` |
| **History retained** | `1034` |
| **New PASS** | `2717` |
| **History dropped** | `134` |
| **Previous public** | `1168` |
| **Published profiles (deduped)** | `3751` |
| **Share links (exportable)** | `2137` |
| **YAML proxies (exportable)** | `2137` |
| **Protocol mix** | `{"hysteria2": 95, "vless": 1568, "vmess": 100, "shadowsocks": 261, "trojan": 113}` |
| **Country mix** | `{"NL": 183, "US": 279, "GB": 54, "FR": 38, "DE": 121, "CA": 908, "IE": 7, "ZA": 4, "CH": 9, "RO": 5, "HK": 68, "ES": 15, "FI": 19, "JP": 68, "IN": 12, "KR": 37, "SG": 57, "HU": 1, "AT": 3, "EE": 12, "TW": 6, "RU": 28, "TH": 4, "PL": 21, "IT": 25, "SE": 7, "CL": 13, "SA": 1, "AM": 3, "ID": 5, "MY": 11, "BR": 3, "NO": 1, "LT": 12, "KZ": 5, "SC": 7, "TR": 4, "AE": 5, "AU": 6, "IR": 2, "PT": 1, "BZ": 7, "CW": 4, "CY": 3, "BG": 8, "GR": 1, "AL": 1, "VN": 1, "LV": 13, "UA": 5, "ME": 3, "VG": 1, "BY": 1, "CR": 2, "CN": 18, "UZ": 2, "DK": 1, "CZ": 1, "RS": 2, "IL": 1}` |
| **Line type mix** | `{"home": 112, "dc": 1540, "proxy": 473, "mobile": 20}` |

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
