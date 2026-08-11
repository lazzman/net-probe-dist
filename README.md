# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-12 05:56:18](https://img.shields.io/badge/updated-2026--08--12_05%3A56%3A18-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10223.7s](https://img.shields.io/badge/elapsed-10223.7s-lightgrey)
![profiles: 1444](https://img.shields.io/badge/profiles-1444-blue)
![live_hits: 1444](https://img.shields.io/badge/live__hits-1444-brightgreen)
![live_fail: 93380](https://img.shields.io/badge/live__fail-93380-orange)
![kept: 876](https://img.shields.io/badge/kept-876-blue)
![new: 568](https://img.shields.io/badge/new-568-success)
![dropped: 302](https://img.shields.io/badge/dropped-302-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-12 05:56:18 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10223.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `445422` |
| **Live PASS (pool hits)** | `1444` |
| **Live FAIL** | `93380` |
| **History retained** | `876` |
| **New PASS** | `568` |
| **History dropped** | `302` |
| **Previous public** | `1178` |
| **Published profiles (deduped)** | `1444` |
| **Share links (exportable)** | `1135` |
| **YAML proxies (exportable)** | `1135` |
| **Protocol mix** | `{"vmess": 82, "vless": 715, "hysteria2": 89, "shadowsocks": 177, "trojan": 72}` |
| **Country mix** | `{"US": 173, "CA": 159, "FR": 45, "NL": 210, "PL": 22, "DE": 84, "TH": 3, "AU": 5, "HK": 41, "GB": 40, "RO": 5, "RU": 70, "SG": 25, "FI": 45, "TW": 9, "IN": 6, "JP": 49, "ZA": 2, "TR": 6, "IE": 3, "KR": 31, "ES": 9, "SC": 5, "AT": 3, "KZ": 8, "EE": 10, "CH": 4, "CZ": 3, "BG": 4, "DK": 1, "SE": 7, "IT": 3, "MD": 1, "AZ": 2, "PH": 11, "LT": 2, "SA": 3, "PT": 1, "HU": 1, "AE": 2, "NO": 1, "CO": 4, "AM": 1, "CN": 7, "AL": 2, "IR": 1, "LV": 3, "AF": 1, "GR": 1, "CR": 1, "CY": 1, "KH": 1}` |
| **Line type mix** | `{"dc": 591, "proxy": 432, "home": 104, "mobile": 10}` |

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
