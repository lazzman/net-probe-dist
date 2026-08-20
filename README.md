# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-20 11:52:11](https://img.shields.io/badge/updated-2026--08--20_11%3A52%3A11-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 8795.1s](https://img.shields.io/badge/elapsed-8795.1s-lightgrey)
![profiles: 5017](https://img.shields.io/badge/profiles-5017-blue)
![live_hits: 5018](https://img.shields.io/badge/live__hits-5018-brightgreen)
![live_fail: 62947](https://img.shields.io/badge/live__fail-62947-orange)
![kept: 1599](https://img.shields.io/badge/kept-1599-blue)
![new: 3419](https://img.shields.io/badge/new-3419-success)
![dropped: 177](https://img.shields.io/badge/dropped-177-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-20 11:52:11 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `8795.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `427043` |
| **Live PASS (pool hits)** | `5018` |
| **Live FAIL** | `62947` |
| **History retained** | `1599` |
| **New PASS** | `3419` |
| **History dropped** | `177` |
| **Previous public** | `1776` |
| **Published profiles (deduped)** | `5017` |
| **Share links (exportable)** | `2809` |
| **YAML proxies (exportable)** | `2809` |
| **Protocol mix** | `{"vless": 1854, "hysteria2": 159, "shadowsocks": 252, "vmess": 62, "trojan": 482}` |
| **Country mix** | `{"US": 368, "FR": 62, "CA": 759, "SG": 155, "NL": 347, "AU": 22, "DZ": 5, "SE": 43, "DE": 173, "FI": 49, "ZA": 4, "PL": 55, "IN": 13, "ES": 8, "RO": 3, "TH": 6, "JP": 263, "PH": 2, "GB": 85, "CN": 17, "RU": 53, "IT": 14, "HK": 77, "IE": 19, "AT": 5, "EE": 20, "TW": 9, "KZ": 14, "BE": 2, "LV": 11, "SC": 23, "CH": 8, "NO": 8, "VN": 2, "BY": 1, "SK": 1, "LT": 7, "TR": 8, "MD": 2, "DK": 3, "KR": 23, "BZ": 7, "CY": 3, "CO": 3, "CZ": 3, "AM": 1, "UA": 10, "AE": 3, "PT": 2, "MY": 2, "IR": 4, "AL": 3, "BG": 8, "BR": 7, "IL": 2, "NZ": 1, "CW": 3, "HU": 1, "ME": 1, "SA": 1, "CR": 2, "AF": 1, "VG": 1}` |
| **Line type mix** | `{"dc": 1854, "proxy": 731, "home": 211, "mobile": 22}` |

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
