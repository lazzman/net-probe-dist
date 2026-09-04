# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-05 02:41:20](https://img.shields.io/badge/updated-2026--09--05_02%3A41%3A20-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9834.1s](https://img.shields.io/badge/elapsed-9834.1s-lightgrey)
![profiles: 2039](https://img.shields.io/badge/profiles-2039-blue)
![live_hits: 2040](https://img.shields.io/badge/live__hits-2040-brightgreen)
![live_fail: 73705](https://img.shields.io/badge/live__fail-73705-orange)
![kept: 1194](https://img.shields.io/badge/kept-1194-blue)
![new: 846](https://img.shields.io/badge/new-846-success)
![dropped: 333](https://img.shields.io/badge/dropped-333-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-05 02:41:20 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9834.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `430446` |
| **Live PASS (pool hits)** | `2040` |
| **Live FAIL** | `73705` |
| **History retained** | `1194` |
| **New PASS** | `846` |
| **History dropped** | `333` |
| **Previous public** | `1527` |
| **Published profiles (deduped)** | `2039` |
| **Share links (exportable)** | `1372` |
| **YAML proxies (exportable)** | `1372` |
| **Protocol mix** | `{"vless": 843, "hysteria2": 170, "shadowsocks": 280, "trojan": 22, "vmess": 57}` |
| **Country mix** | `{"DE": 76, "US": 205, "SG": 57, "IT": 10, "NL": 233, "GB": 77, "DZ": 18, "IN": 7, "AU": 4, "RU": 32, "FI": 33, "SE": 13, "TW": 23, "JP": 59, "ZA": 5, "CA": 254, "PL": 30, "FR": 30, "ES": 7, "NO": 23, "RO": 3, "IE": 6, "TH": 3, "MY": 4, "CN": 2, "KR": 35, "AT": 4, "KZ": 9, "EE": 7, "IR": 2, "AL": 1, "TR": 16, "BR": 4, "GR": 2, "LV": 12, "UA": 2, "HK": 33, "CZ": 4, "SA": 1, "UZ": 2, "LT": 5, "ID": 1, "AM": 1, "HU": 1, "AR": 2, "JE": 1, "SC": 4, "AE": 1, "BY": 1, "SK": 1, "PH": 1, "EG": 1, "CH": 1, "CR": 1, "MX": 2}` |
| **Line type mix** | `{"dc": 853, "proxy": 400, "home": 110, "mobile": 9}` |

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
