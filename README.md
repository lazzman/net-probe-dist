# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-05 01:03:58](https://img.shields.io/badge/updated-2026--11--05_01%3A03%3A58-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11305.9s](https://img.shields.io/badge/elapsed-11305.9s-lightgrey)
![profiles: 1168](https://img.shields.io/badge/profiles-1168-blue)
![live_hits: 1168](https://img.shields.io/badge/live__hits-1168-brightgreen)
![live_fail: 86806](https://img.shields.io/badge/live__fail-86806-orange)
![kept: 857](https://img.shields.io/badge/kept-857-blue)
![new: 311](https://img.shields.io/badge/new-311-success)
![dropped: 350](https://img.shields.io/badge/dropped-350-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-05 01:03:58 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11305.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `402905` |
| **Live PASS (pool hits)** | `1168` |
| **Live FAIL** | `86806` |
| **History retained** | `857` |
| **New PASS** | `311` |
| **History dropped** | `350` |
| **Previous public** | `1207` |
| **Published profiles (deduped)** | `1168` |
| **Share links (exportable)** | `970` |
| **YAML proxies (exportable)** | `970` |
| **Protocol mix** | `{"shadowsocks": 311, "vless": 361, "hysteria2": 150, "trojan": 90, "vmess": 58}` |
| **Country mix** | `{"IT": 17, "DE": 53, "BY": 9, "NL": 165, "PL": 26, "GB": 29, "IE": 1, "HK": 29, "AT": 1, "US": 221, "ZA": 2, "CA": 107, "JP": 22, "RU": 26, "IN": 11, "TR": 7, "SG": 47, "CH": 57, "MX": 2, "BR": 2, "AU": 2, "IL": 3, "SE": 10, "ES": 12, "FR": 31, "EE": 4, "UA": 1, "FI": 11, "KR": 20, "AE": 1, "MY": 2, "KZ": 2, "TW": 3, "NO": 1, "PH": 1, "AL": 1, "LV": 3, "BG": 12, "CZ": 1, "RS": 1, "GR": 1, "GE": 1, "TH": 2, "CN": 1, "LT": 9, "AM": 1, "SA": 1}` |
| **Line type mix** | `{"dc": 432, "mobile": 119, "proxy": 354, "home": 67}` |

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
