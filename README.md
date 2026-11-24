# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-25 04:18:18](https://img.shields.io/badge/updated-2026--11--25_04%3A18%3A18-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11566.1s](https://img.shields.io/badge/elapsed-11566.1s-lightgrey)
![profiles: 1130](https://img.shields.io/badge/profiles-1130-blue)
![live_hits: 1130](https://img.shields.io/badge/live__hits-1130-brightgreen)
![live_fail: 88597](https://img.shields.io/badge/live__fail-88597-orange)
![kept: 856](https://img.shields.io/badge/kept-856-blue)
![new: 274](https://img.shields.io/badge/new-274-success)
![dropped: 230](https://img.shields.io/badge/dropped-230-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-25 04:18:18 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11566.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `395230` |
| **Live PASS (pool hits)** | `1130` |
| **Live FAIL** | `88597` |
| **History retained** | `856` |
| **New PASS** | `274` |
| **History dropped** | `230` |
| **Previous public** | `1086` |
| **Published profiles (deduped)** | `1130` |
| **Share links (exportable)** | `1018` |
| **YAML proxies (exportable)** | `1018` |
| **Protocol mix** | `{"hysteria2": 56, "shadowsocks": 368, "vless": 431, "vmess": 121, "trojan": 42}` |
| **Country mix** | `{"NL": 113, "IT": 20, "US": 245, "DE": 75, "BY": 7, "AT": 2, "JP": 46, "GB": 45, "HK": 21, "CN": 2, "SG": 53, "NO": 1, "AL": 3, "IE": 2, "ZA": 3, "CA": 89, "PL": 59, "LT": 11, "KR": 11, "FI": 8, "SE": 12, "IN": 5, "FR": 37, "CH": 15, "ES": 17, "ID": 1, "TR": 9, "LV": 5, "RU": 31, "RO": 9, "AE": 2, "NG": 2, "CY": 1, "VN": 2, "IR": 5, "BR": 9, "KZ": 2, "AU": 4, "TW": 3, "CZ": 1, "EE": 9, "TH": 1, "MY": 2, "IL": 2, "BG": 8, "CR": 1, "LY": 1, "NE": 4, "SK": 3, "SA": 1}` |
| **Line type mix** | `{"dc": 412, "proxy": 463, "home": 102, "mobile": 43}` |

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
