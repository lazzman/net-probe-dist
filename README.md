# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-19 23:17:11](https://img.shields.io/badge/updated-2026--08--19_23%3A17%3A11-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 8816.4s](https://img.shields.io/badge/elapsed-8816.4s-lightgrey)
![profiles: 2887](https://img.shields.io/badge/profiles-2887-blue)
![live_hits: 2887](https://img.shields.io/badge/live__hits-2887-brightgreen)
![live_fail: 64883](https://img.shields.io/badge/live__fail-64883-orange)
![kept: 1621](https://img.shields.io/badge/kept-1621-blue)
![new: 1266](https://img.shields.io/badge/new-1266-success)
![dropped: 948](https://img.shields.io/badge/dropped-948-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-19 23:17:11 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `8816.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `427584` |
| **Live PASS (pool hits)** | `2887` |
| **Live FAIL** | `64883` |
| **History retained** | `1621` |
| **New PASS** | `1266` |
| **History dropped** | `948` |
| **Previous public** | `2569` |
| **Published profiles (deduped)** | `2887` |
| **Share links (exportable)** | `1793` |
| **YAML proxies (exportable)** | `1793` |
| **Protocol mix** | `{"shadowsocks": 251, "vmess": 62, "vless": 860, "hysteria2": 169, "trojan": 451}` |
| **Country mix** | `{"AU": 19, "US": 236, "CA": 247, "FR": 60, "NL": 272, "SG": 141, "SE": 20, "DZ": 5, "DE": 127, "FI": 30, "PL": 38, "IN": 11, "RO": 5, "ZA": 3, "NO": 6, "JP": 253, "ES": 4, "PH": 2, "CN": 16, "RU": 29, "HK": 79, "IE": 19, "EE": 12, "IT": 5, "LV": 10, "CH": 7, "CZ": 4, "VN": 2, "BY": 2, "KG": 1, "GB": 22, "CO": 4, "SK": 1, "MD": 2, "TR": 10, "AL": 3, "DK": 2, "TH": 3, "AM": 1, "TW": 7, "KZ": 8, "LT": 5, "SC": 8, "KR": 30, "BE": 3, "UA": 5, "PT": 1, "GE": 1, "AT": 3, "IR": 1, "BG": 2, "AE": 1, "PE": 1, "HU": 2, "BR": 3, "SA": 1, "MY": 1, "CY": 1}` |
| **Line type mix** | `{"proxy": 516, "dc": 1086, "home": 173, "mobile": 22}` |

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
