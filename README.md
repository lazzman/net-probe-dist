# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-23 03:16:24](https://img.shields.io/badge/updated-2026--09--23_03%3A16%3A24-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10027.9s](https://img.shields.io/badge/elapsed-10027.9s-lightgrey)
![profiles: 1829](https://img.shields.io/badge/profiles-1829-blue)
![live_hits: 1830](https://img.shields.io/badge/live__hits-1830-brightgreen)
![live_fail: 76065](https://img.shields.io/badge/live__fail-76065-orange)
![kept: 1236](https://img.shields.io/badge/kept-1236-blue)
![new: 594](https://img.shields.io/badge/new-594-success)
![dropped: 433](https://img.shields.io/badge/dropped-433-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-23 03:16:24 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10027.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `423751` |
| **Live PASS (pool hits)** | `1830` |
| **Live FAIL** | `76065` |
| **History retained** | `1236` |
| **New PASS** | `594` |
| **History dropped** | `433` |
| **Previous public** | `1669` |
| **Published profiles (deduped)** | `1829` |
| **Share links (exportable)** | `1428` |
| **YAML proxies (exportable)** | `1428` |
| **Protocol mix** | `{"hysteria2": 105, "vless": 947, "shadowsocks": 257, "trojan": 42, "vmess": 77}` |
| **Country mix** | `{"ES": 16, "US": 250, "KR": 33, "RU": 24, "CA": 387, "DK": 4, "DE": 69, "NL": 170, "SE": 15, "GB": 43, "TW": 14, "ID": 2, "ZA": 4, "FR": 32, "CH": 10, "MX": 2, "CL": 5, "IN": 15, "AT": 4, "PL": 26, "FI": 31, "TR": 3, "SG": 34, "JP": 38, "IT": 17, "AL": 1, "CY": 10, "BE": 4, "KZ": 12, "BZ": 8, "IR": 2, "LU": 1, "IE": 3, "HU": 3, "RO": 4, "EE": 8, "MD": 2, "AM": 3, "BR": 3, "HK": 34, "NO": 3, "DZ": 25, "SC": 3, "ZZ": 2, "TH": 4, "AU": 4, "AE": 2, "BG": 8, "GT": 1, "CO": 1, "RS": 1, "IS": 2, "BY": 1, "PT": 1, "UA": 1, "MY": 4, "GR": 2, "SK": 3, "UZ": 2, "LT": 6, "LV": 7, "EG": 1, "SA": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 937, "home": 79, "proxy": 398, "mobile": 16, "unknown": 2}` |

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
