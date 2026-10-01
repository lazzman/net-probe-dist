# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-01 23:29:04](https://img.shields.io/badge/updated-2026--10--01_23%3A29%3A04-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10324.7s](https://img.shields.io/badge/elapsed-10324.7s-lightgrey)
![profiles: 1572](https://img.shields.io/badge/profiles-1572-blue)
![live_hits: 1573](https://img.shields.io/badge/live__hits-1573-brightgreen)
![live_fail: 78199](https://img.shields.io/badge/live__fail-78199-orange)
![kept: 1083](https://img.shields.io/badge/kept-1083-blue)
![new: 490](https://img.shields.io/badge/new-490-success)
![dropped: 858](https://img.shields.io/badge/dropped-858-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-01 23:29:04 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10324.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `436336` |
| **Live PASS (pool hits)** | `1573` |
| **Live FAIL** | `78199` |
| **History retained** | `1083` |
| **New PASS** | `490` |
| **History dropped** | `858` |
| **Previous public** | `1941` |
| **Published profiles (deduped)** | `1572` |
| **Share links (exportable)** | `1297` |
| **YAML proxies (exportable)** | `1297` |
| **Protocol mix** | `{"vless": 745, "trojan": 56, "vmess": 93, "hysteria2": 119, "shadowsocks": 284}` |
| **Country mix** | `{"US": 249, "GB": 53, "DE": 80, "NL": 146, "CA": 298, "FR": 34, "ID": 3, "NO": 1, "ZA": 3, "RO": 4, "CH": 9, "IE": 3, "ES": 14, "SG": 48, "JP": 38, "HK": 47, "IN": 11, "HU": 1, "AT": 1, "SE": 14, "RU": 37, "FI": 13, "TW": 8, "PL": 25, "KR": 32, "IT": 14, "GR": 2, "TR": 4, "EE": 4, "SC": 4, "MY": 13, "LT": 10, "GT": 1, "KZ": 4, "PT": 1, "PH": 1, "CO": 1, "AL": 2, "AE": 2, "TH": 2, "AU": 6, "CW": 1, "QA": 2, "IR": 3, "CZ": 8, "AM": 2, "SK": 2, "CN": 7, "BR": 1, "UA": 2, "GE": 1, "BE": 3, "MX": 1, "CY": 1, "SA": 1, "LV": 14, "BG": 4, "IL": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 799, "proxy": 399, "mobile": 26, "home": 74}` |

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
