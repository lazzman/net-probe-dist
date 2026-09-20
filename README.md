# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-21 02:25:37](https://img.shields.io/badge/updated-2026--09--21_02%3A25%3A37-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9985.5s](https://img.shields.io/badge/elapsed-9985.5s-lightgrey)
![profiles: 1863](https://img.shields.io/badge/profiles-1863-blue)
![live_hits: 1863](https://img.shields.io/badge/live__hits-1863-brightgreen)
![live_fail: 75730](https://img.shields.io/badge/live__fail-75730-orange)
![kept: 1231](https://img.shields.io/badge/kept-1231-blue)
![new: 632](https://img.shields.io/badge/new-632-success)
![dropped: 290](https://img.shields.io/badge/dropped-290-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-21 02:25:37 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9985.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `421628` |
| **Live PASS (pool hits)** | `1863` |
| **Live FAIL** | `75730` |
| **History retained** | `1231` |
| **New PASS** | `632` |
| **History dropped** | `290` |
| **Previous public** | `1521` |
| **Published profiles (deduped)** | `1863` |
| **Share links (exportable)** | `1449` |
| **YAML proxies (exportable)** | `1449` |
| **Protocol mix** | `{"vless": 942, "trojan": 28, "vmess": 64, "hysteria2": 124, "shadowsocks": 291}` |
| **Country mix** | `{"CA": 347, "NL": 203, "US": 239, "GB": 52, "DE": 74, "KR": 33, "RU": 20, "ES": 12, "DK": 3, "SE": 14, "TW": 22, "AL": 4, "FR": 34, "ID": 1, "RO": 4, "SG": 36, "CH": 5, "JP": 48, "IN": 13, "FI": 28, "AT": 3, "PL": 23, "HK": 68, "IT": 13, "TR": 5, "UZ": 2, "ZZ": 1, "TH": 3, "GR": 2, "CZ": 12, "SA": 11, "CY": 8, "KZ": 14, "EE": 7, "ME": 2, "NO": 3, "AM": 1, "IQ": 1, "MY": 3, "IM": 1, "ZA": 3, "BG": 8, "AE": 2, "HU": 1, "DZ": 25, "AU": 5, "CL": 2, "GT": 1, "IR": 2, "BZ": 8, "LT": 4, "MD": 1, "SC": 1, "LV": 9, "UA": 2, "CR": 1}` |
| **Line type mix** | `{"dc": 962, "home": 79, "proxy": 403, "unknown": 1, "mobile": 5}` |

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
