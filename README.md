# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-24 11:56:06](https://img.shields.io/badge/updated-2026--08--24_11%3A56%3A06-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9052.7s](https://img.shields.io/badge/elapsed-9052.7s-lightgrey)
![profiles: 4339](https://img.shields.io/badge/profiles-4339-blue)
![live_hits: 4341](https://img.shields.io/badge/live__hits-4341-brightgreen)
![live_fail: 65681](https://img.shields.io/badge/live__fail-65681-orange)
![kept: 1294](https://img.shields.io/badge/kept-1294-blue)
![new: 3047](https://img.shields.io/badge/new-3047-success)
![dropped: 230](https://img.shields.io/badge/dropped-230-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-24 11:56:06 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9052.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `423608` |
| **Live PASS (pool hits)** | `4341` |
| **Live FAIL** | `65681` |
| **History retained** | `1294` |
| **New PASS** | `3047` |
| **History dropped** | `230` |
| **Previous public** | `1524` |
| **Published profiles (deduped)** | `4339` |
| **Share links (exportable)** | `2626` |
| **YAML proxies (exportable)** | `2626` |
| **Protocol mix** | `{"shadowsocks": 332, "vless": 1993, "vmess": 54, "hysteria2": 186, "trojan": 61}` |
| **Country mix** | `{"US": 339, "NL": 305, "AU": 8, "DE": 166, "PL": 28, "JP": 55, "SG": 91, "RU": 51, "FI": 41, "SE": 24, "BR": 26, "TW": 14, "TR": 11, "FR": 38, "CA": 995, "NO": 5, "ZZ": 3, "IN": 14, "LT": 12, "ES": 9, "ZA": 3, "TH": 6, "HK": 51, "IE": 3, "GB": 112, "CN": 13, "AT": 3, "EE": 15, "KZ": 16, "BE": 1, "AL": 5, "SC": 19, "CH": 10, "IT": 21, "LV": 14, "GR": 3, "VN": 2, "SK": 1, "MD": 2, "DK": 3, "AM": 1, "KR": 28, "CY": 4, "BZ": 8, "IR": 5, "UA": 6, "PT": 1, "GE": 1, "VI": 1, "PH": 1, "RO": 3, "BG": 10, "CZ": 3, "AE": 4, "PE": 1, "NZ": 1, "CW": 4, "HU": 1, "ME": 1, "SA": 1, "BY": 2, "CR": 4, "AF": 1, "DZ": 4, "MY": 1}` |
| **Line type mix** | `{"proxy": 647, "home": 252, "dc": 1717, "unknown": 3, "mobile": 16}` |

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
