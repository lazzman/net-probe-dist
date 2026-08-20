# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-21 05:16:19](https://img.shields.io/badge/updated-2026--08--21_05%3A16%3A19-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9054.8s](https://img.shields.io/badge/elapsed-9054.8s-lightgrey)
![profiles: 2759](https://img.shields.io/badge/profiles-2759-blue)
![live_hits: 2759](https://img.shields.io/badge/live__hits-2759-brightgreen)
![live_fail: 66599](https://img.shields.io/badge/live__fail-66599-orange)
![kept: 1532](https://img.shields.io/badge/kept-1532-blue)
![new: 1227](https://img.shields.io/badge/new-1227-success)
![dropped: 250](https://img.shields.io/badge/dropped-250-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-21 05:16:19 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9054.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `433931` |
| **Live PASS (pool hits)** | `2759` |
| **Live FAIL** | `66599` |
| **History retained** | `1532` |
| **New PASS** | `1227` |
| **History dropped** | `250` |
| **Previous public** | `1782` |
| **Published profiles (deduped)** | `2759` |
| **Share links (exportable)** | `1751` |
| **YAML proxies (exportable)** | `1751` |
| **Protocol mix** | `{"vless": 897, "vmess": 55, "shadowsocks": 290, "hysteria2": 147, "trojan": 362}` |
| **Country mix** | `{"US": 272, "DE": 148, "AU": 19, "HK": 60, "FR": 65, "SE": 19, "SG": 60, "JP": 246, "NL": 288, "FI": 40, "GB": 38, "BR": 15, "ZA": 4, "TR": 13, "PL": 40, "CA": 185, "IN": 11, "RO": 5, "ES": 8, "CN": 3, "RU": 38, "IE": 18, "LV": 12, "EE": 11, "IT": 9, "TW": 9, "BE": 2, "CH": 10, "KZ": 8, "AE": 1, "IL": 1, "LT": 5, "VN": 2, "KG": 1, "NO": 8, "KR": 27, "CZ": 3, "CO": 2, "SK": 1, "MD": 2, "DK": 3, "AM": 1, "PH": 3, "SC": 9, "TH": 5, "PT": 1, "AL": 3, "AT": 1, "SA": 1, "UA": 3, "PE": 2, "BG": 1, "BY": 1, "HU": 1, "DZ": 2, "BZ": 1, "CR": 1, "AF": 1, "ZZ": 1, "CY": 1, "MY": 1}` |
| **Line type mix** | `{"dc": 1027, "proxy": 521, "home": 194, "mobile": 9, "unknown": 1}` |

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
