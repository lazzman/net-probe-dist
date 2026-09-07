# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-08 07:58:28](https://img.shields.io/badge/updated-2026--09--08_07%3A58%3A28-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9803.3s](https://img.shields.io/badge/elapsed-9803.3s-lightgrey)
![profiles: 1828](https://img.shields.io/badge/profiles-1828-blue)
![live_hits: 1828](https://img.shields.io/badge/live__hits-1828-brightgreen)
![live_fail: 74574](https://img.shields.io/badge/live__fail-74574-orange)
![kept: 1146](https://img.shields.io/badge/kept-1146-blue)
![new: 682](https://img.shields.io/badge/new-682-success)
![dropped: 141](https://img.shields.io/badge/dropped-141-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-08 07:58:28 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9803.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `430792` |
| **Live PASS (pool hits)** | `1828` |
| **Live FAIL** | `74574` |
| **History retained** | `1146` |
| **New PASS** | `682` |
| **History dropped** | `141` |
| **Previous public** | `1287` |
| **Published profiles (deduped)** | `1828` |
| **Share links (exportable)** | `1266` |
| **YAML proxies (exportable)** | `1266` |
| **Protocol mix** | `{"trojan": 24, "vless": 760, "hysteria2": 153, "shadowsocks": 256, "vmess": 73}` |
| **Country mix** | `{"HR": 1, "CA": 304, "DZ": 17, "GB": 66, "RU": 17, "IN": 7, "US": 189, "DE": 51, "FI": 16, "NL": 205, "TW": 15, "ID": 1, "FR": 28, "ZA": 6, "LT": 8, "IE": 2, "RO": 3, "NO": 20, "PL": 36, "ES": 10, "MY": 2, "CN": 5, "JP": 53, "IT": 9, "AT": 2, "JE": 1, "KZ": 6, "EE": 8, "SG": 59, "CZ": 2, "KR": 29, "BR": 3, "IR": 1, "HK": 39, "HU": 2, "TR": 5, "LV": 7, "GR": 2, "SK": 1, "SE": 7, "EG": 1, "TH": 3, "SA": 1, "AU": 3, "AM": 1, "AR": 2, "AE": 1, "UA": 2, "GT": 1, "PH": 1, "SC": 1, "CY": 1, "CH": 1, "CR": 1, "BG": 5}` |
| **Line type mix** | `{"proxy": 373, "dc": 787, "home": 100, "mobile": 10}` |

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
