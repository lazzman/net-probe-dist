# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-08 05:46:24](https://img.shields.io/badge/updated-2026--08--08_05%3A46%3A24-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9952.4s](https://img.shields.io/badge/elapsed-9952.4s-lightgrey)
![profiles: 1427](https://img.shields.io/badge/profiles-1427-blue)
![live_hits: 1428](https://img.shields.io/badge/live__hits-1428-brightgreen)
![live_fail: 91999](https://img.shields.io/badge/live__fail-91999-orange)
![kept: 878](https://img.shields.io/badge/kept-878-blue)
![new: 550](https://img.shields.io/badge/new-550-success)
![dropped: 268](https://img.shields.io/badge/dropped-268-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-08 05:46:24 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9952.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `444423` |
| **Live PASS (pool hits)** | `1428` |
| **Live FAIL** | `91999` |
| **History retained** | `878` |
| **New PASS** | `550` |
| **History dropped** | `268` |
| **Previous public** | `1146` |
| **Published profiles (deduped)** | `1427` |
| **Share links (exportable)** | `1069` |
| **YAML proxies (exportable)** | `1069` |
| **Protocol mix** | `{"vmess": 83, "vless": 634, "shadowsocks": 187, "hysteria2": 89, "trojan": 76}` |
| **Country mix** | `{"US": 148, "CA": 167, "FR": 45, "NL": 208, "GB": 43, "AU": 4, "IT": 4, "FI": 23, "DE": 85, "SG": 23, "SE": 10, "TW": 9, "HK": 33, "KR": 41, "RO": 5, "IE": 5, "IN": 5, "ES": 3, "ZA": 2, "BR": 6, "JP": 47, "BG": 3, "SA": 3, "PL": 9, "RU": 54, "KZ": 5, "PT": 1, "EE": 3, "AE": 3, "CH": 2, "CZ": 1, "HU": 1, "CR": 1, "TR": 4, "CO": 22, "MD": 1, "SC": 1, "BE": 1, "LT": 4, "DK": 3, "PH": 10, "CN": 7, "MY": 2, "NO": 1, "AZ": 1, "TH": 1, "AT": 2, "MX": 1, "LV": 2, "AM": 1, "GR": 1, "AF": 1, "CY": 1, "UA": 1, "KH": 1}` |
| **Line type mix** | `{"proxy": 432, "dc": 553, "home": 82, "mobile": 4}` |

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
