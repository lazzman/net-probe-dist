# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-03 05:28:50](https://img.shields.io/badge/updated-2026--10--03_05%3A28%3A50-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 13136.2s](https://img.shields.io/badge/elapsed-13136.2s-lightgrey)
![profiles: 1365](https://img.shields.io/badge/profiles-1365-blue)
![live_hits: 1365](https://img.shields.io/badge/live__hits-1365-brightgreen)
![live_fail: 93016](https://img.shields.io/badge/live__fail-93016-orange)
![kept: 951](https://img.shields.io/badge/kept-951-blue)
![new: 414](https://img.shields.io/badge/new-414-success)
![dropped: 257](https://img.shields.io/badge/dropped-257-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-03 05:28:50 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `13136.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `465344` |
| **Live PASS (pool hits)** | `1365` |
| **Live FAIL** | `93016` |
| **History retained** | `951` |
| **New PASS** | `414` |
| **History dropped** | `257` |
| **Previous public** | `1208` |
| **Published profiles (deduped)** | `1365` |
| **Share links (exportable)** | `1113` |
| **YAML proxies (exportable)** | `1113` |
| **Protocol mix** | `{"vmess": 96, "vless": 596, "hysteria2": 124, "shadowsocks": 267, "trojan": 30}` |
| **Country mix** | `{"ES": 12, "US": 212, "IE": 3, "GB": 30, "CA": 252, "NL": 152, "SG": 44, "DE": 68, "FR": 28, "NO": 1, "ZA": 5, "CH": 8, "JP": 35, "IN": 7, "PH": 1, "IT": 15, "AT": 1, "FI": 11, "RU": 24, "PL": 21, "GR": 2, "HK": 33, "TR": 5, "CZ": 18, "CL": 8, "MY": 13, "SA": 1, "AM": 1, "TW": 2, "KR": 26, "ID": 3, "MX": 4, "KZ": 4, "AE": 2, "CO": 1, "AL": 2, "LV": 7, "EE": 5, "AU": 4, "RO": 2, "BR": 2, "LT": 11, "GT": 1, "QA": 1, "TH": 2, "CN": 10, "SE": 7, "BG": 5, "CR": 1}` |
| **Line type mix** | `{"mobile": 22, "dc": 686, "home": 59, "proxy": 346}` |

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
