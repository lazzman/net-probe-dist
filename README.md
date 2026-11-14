# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-14 10:29:18](https://img.shields.io/badge/updated-2026--11--14_10%3A29%3A18-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11283.4s](https://img.shields.io/badge/elapsed-11283.4s-lightgrey)
![profiles: 1399](https://img.shields.io/badge/profiles-1399-blue)
![live_hits: 1399](https://img.shields.io/badge/live__hits-1399-brightgreen)
![live_fail: 87693](https://img.shields.io/badge/live__fail-87693-orange)
![kept: 895](https://img.shields.io/badge/kept-895-blue)
![new: 504](https://img.shields.io/badge/new-504-success)
![dropped: 139](https://img.shields.io/badge/dropped-139-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-14 10:29:18 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11283.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `401948` |
| **Live PASS (pool hits)** | `1399` |
| **Live FAIL** | `87693` |
| **History retained** | `895` |
| **New PASS** | `504` |
| **History dropped** | `139` |
| **Previous public** | `1034` |
| **Published profiles (deduped)** | `1399` |
| **Share links (exportable)** | `1199` |
| **YAML proxies (exportable)** | `1199` |
| **Protocol mix** | `{"hysteria2": 128, "shadowsocks": 378, "trojan": 107, "vless": 477, "vmess": 109}` |
| **Country mix** | `{"FI": 13, "PL": 51, "US": 261, "DE": 86, "IR": 4, "CA": 177, "NL": 140, "HK": 27, "BG": 12, "GB": 40, "FR": 41, "NO": 1, "AT": 4, "ZA": 6, "RO": 4, "UA": 4, "IT": 24, "SE": 19, "JP": 31, "ES": 30, "MX": 2, "RU": 22, "SG": 44, "CH": 56, "IN": 6, "KR": 15, "EE": 2, "TR": 6, "LY": 1, "CZ": 2, "BY": 5, "CR": 2, "AE": 3, "IL": 2, "GR": 1, "KZ": 3, "AL": 3, "TW": 3, "AU": 4, "LV": 11, "VN": 2, "NE": 1, "SK": 2, "MY": 2, "BR": 2, "TH": 3, "CN": 1, "LT": 8, "SA": 1, "IE": 3, "BZ": 2, "MD": 1, "DK": 1, "CW": 1, "GE": 1}` |
| **Line type mix** | `{"dc": 523, "home": 81, "proxy": 462, "mobile": 133}` |

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
