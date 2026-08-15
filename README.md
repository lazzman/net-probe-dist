# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-16 05:26:03](https://img.shields.io/badge/updated-2026--08--16_05%3A26%3A03-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10331.9s](https://img.shields.io/badge/elapsed-10331.9s-lightgrey)
![profiles: 2124](https://img.shields.io/badge/profiles-2124-blue)
![live_hits: 2124](https://img.shields.io/badge/live__hits-2124-brightgreen)
![live_fail: 93402](https://img.shields.io/badge/live__fail-93402-orange)
![kept: 1287](https://img.shields.io/badge/kept-1287-blue)
![new: 837](https://img.shields.io/badge/new-837-success)
![dropped: 336](https://img.shields.io/badge/dropped-336-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-16 05:26:03 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10331.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `445816` |
| **Live PASS (pool hits)** | `2124` |
| **Live FAIL** | `93402` |
| **History retained** | `1287` |
| **New PASS** | `837` |
| **History dropped** | `336` |
| **Previous public** | `1623` |
| **Published profiles (deduped)** | `2124` |
| **Share links (exportable)** | `1549` |
| **YAML proxies (exportable)** | `1549` |
| **Protocol mix** | `{"vless": 780, "vmess": 90, "shadowsocks": 207, "hysteria2": 124, "trojan": 348}` |
| **Country mix** | `{"CA": 176, "US": 210, "AU": 13, "TH": 3, "NL": 239, "FI": 34, "HK": 58, "DZ": 1, "FR": 42, "JP": 173, "DE": 83, "EE": 12, "RU": 103, "GB": 57, "ZA": 4, "PL": 32, "IN": 7, "RO": 7, "ES": 10, "SE": 11, "PH": 2, "IE": 14, "KR": 106, "SG": 61, "SC": 4, "KZ": 9, "LV": 8, "CH": 6, "OM": 1, "TW": 5, "BG": 3, "KG": 1, "IT": 5, "CZ": 2, "TR": 9, "MD": 1, "SA": 1, "LT": 3, "ID": 1, "MY": 2, "DK": 1, "BR": 1, "CO": 3, "GR": 1, "AT": 4, "BA": 1, "NO": 4, "AL": 1, "BY": 1, "CN": 7, "PT": 1, "AE": 1, "UA": 1, "HU": 1, "AM": 1, "CR": 1, "CY": 1, "KH": 1, "IL": 1}` |
| **Line type mix** | `{"dc": 912, "proxy": 490, "home": 144, "mobile": 6}` |

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
