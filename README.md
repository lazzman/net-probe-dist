# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-23 21:45:58](https://img.shields.io/badge/updated-2026--09--23_21%3A45%3A58-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9989.1s](https://img.shields.io/badge/elapsed-9989.1s-lightgrey)
![profiles: 1977](https://img.shields.io/badge/profiles-1977-blue)
![live_hits: 1977](https://img.shields.io/badge/live__hits-1977-brightgreen)
![live_fail: 76505](https://img.shields.io/badge/live__fail-76505-orange)
![kept: 1246](https://img.shields.io/badge/kept-1246-blue)
![new: 731](https://img.shields.io/badge/new-731-success)
![dropped: 1281](https://img.shields.io/badge/dropped-1281-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-23 21:45:58 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9989.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `434201` |
| **Live PASS (pool hits)** | `1977` |
| **Live FAIL** | `76505` |
| **History retained** | `1246` |
| **New PASS** | `731` |
| **History dropped** | `1281` |
| **Previous public** | `2527` |
| **Published profiles (deduped)** | `1977` |
| **Share links (exportable)** | `1462` |
| **YAML proxies (exportable)** | `1462` |
| **Protocol mix** | `{"vmess": 90, "shadowsocks": 267, "vless": 964, "hysteria2": 106, "trojan": 35}` |
| **Country mix** | `{"ES": 9, "ZA": 3, "US": 263, "KR": 29, "CA": 470, "CH": 8, "GB": 44, "DE": 62, "SG": 33, "SE": 18, "NL": 168, "RU": 27, "TW": 10, "FR": 39, "HK": 42, "JP": 34, "DK": 1, "CZ": 2, "CL": 6, "PL": 25, "FI": 20, "TR": 2, "TH": 4, "AT": 4, "IT": 16, "IN": 18, "AL": 2, "CY": 4, "KZ": 7, "BZ": 5, "BE": 2, "ME": 1, "RO": 5, "EE": 7, "MD": 1, "AM": 1, "MY": 2, "BR": 2, "NO": 2, "DZ": 25, "SC": 2, "AE": 2, "AU": 5, "BG": 10, "CW": 1, "GT": 1, "LT": 9, "LV": 11, "SA": 1, "CR": 1}` |
| **Line type mix** | `{"mobile": 16, "proxy": 389, "home": 69, "dc": 992}` |

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
