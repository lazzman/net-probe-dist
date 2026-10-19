# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-19 14:34:29](https://img.shields.io/badge/updated-2026--10--19_14%3A34%3A29-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10907.4s](https://img.shields.io/badge/elapsed-10907.4s-lightgrey)
![profiles: 1579](https://img.shields.io/badge/profiles-1579-blue)
![live_hits: 1579](https://img.shields.io/badge/live__hits-1579-brightgreen)
![live_fail: 85057](https://img.shields.io/badge/live__fail-85057-orange)
![kept: 809](https://img.shields.io/badge/kept-809-blue)
![new: 770](https://img.shields.io/badge/new-770-success)
![dropped: 138](https://img.shields.io/badge/dropped-138-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-19 14:34:29 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10907.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `413982` |
| **Live PASS (pool hits)** | `1579` |
| **Live FAIL** | `85057` |
| **History retained** | `809` |
| **New PASS** | `770` |
| **History dropped** | `138` |
| **Previous public** | `947` |
| **Published profiles (deduped)** | `1579` |
| **Share links (exportable)** | `1287` |
| **YAML proxies (exportable)** | `1287` |
| **Protocol mix** | `{"shadowsocks": 224, "vless": 770, "trojan": 132, "hysteria2": 98, "vmess": 63}` |
| **Country mix** | `{"NL": 178, "CA": 321, "RU": 25, "GB": 44, "ZA": 3, "US": 189, "HK": 31, "SG": 49, "DE": 91, "RO": 6, "IE": 1, "CH": 39, "TR": 8, "MX": 1, "IN": 13, "CZ": 3, "JP": 43, "PL": 22, "IT": 16, "KR": 27, "TH": 5, "ES": 9, "CR": 2, "AT": 2, "ME": 8, "FI": 21, "KH": 1, "FR": 29, "TW": 4, "BY": 4, "AE": 5, "LV": 12, "HU": 3, "MD": 3, "SA": 1, "LT": 6, "AM": 2, "CL": 1, "KZ": 6, "NO": 1, "CY": 3, "SE": 10, "EE": 4, "AL": 2, "UA": 2, "SC": 6, "IR": 3, "ID": 2, "NZ": 1, "PT": 1, "BZ": 3, "CW": 4, "BG": 6, "VN": 1, "MY": 2, "DK": 1, "AU": 3, "CN": 2, "IL": 1}` |
| **Line type mix** | `{"proxy": 385, "dc": 746, "home": 119, "mobile": 42}` |

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
