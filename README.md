# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-23 17:19:58](https://img.shields.io/badge/updated-2026--08--23_17%3A19%3A58-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9015.0s](https://img.shields.io/badge/elapsed-9015.0s-lightgrey)
![profiles: 3364](https://img.shields.io/badge/profiles-3364-blue)
![live_hits: 3364](https://img.shields.io/badge/live__hits-3364-brightgreen)
![live_fail: 65620](https://img.shields.io/badge/live__fail-65620-orange)
![kept: 1821](https://img.shields.io/badge/kept-1821-blue)
![new: 1543](https://img.shields.io/badge/new-1543-success)
![dropped: 895](https://img.shields.io/badge/dropped-895-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-23 17:19:58 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9015.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `421432` |
| **Live PASS (pool hits)** | `3364` |
| **Live FAIL** | `65620` |
| **History retained** | `1821` |
| **New PASS** | `1543` |
| **History dropped** | `895` |
| **Previous public** | `2716` |
| **Published profiles (deduped)** | `3364` |
| **Share links (exportable)** | `2142` |
| **YAML proxies (exportable)** | `2142` |
| **Protocol mix** | `{"shadowsocks": 352, "vless": 1431, "vmess": 64, "hysteria2": 185, "trojan": 110}` |
| **Country mix** | `{"US": 286, "NL": 299, "DE": 151, "AU": 18, "PL": 57, "JP": 45, "FR": 42, "RU": 52, "SG": 76, "SE": 22, "FI": 38, "HK": 67, "GB": 86, "BR": 28, "TW": 17, "TR": 20, "CA": 588, "IN": 13, "LT": 13, "ZA": 3, "ES": 8, "TH": 5, "CN": 6, "IT": 18, "KR": 26, "AT": 2, "EE": 14, "BE": 1, "CH": 11, "KZ": 12, "UA": 5, "VN": 3, "GR": 2, "PE": 2, "IR": 3, "HU": 2, "LV": 16, "CO": 7, "SK": 1, "MD": 2, "DK": 2, "ZZ": 3, "SC": 15, "BZ": 4, "AL": 5, "NO": 5, "SI": 8, "PH": 2, "RO": 3, "BG": 10, "CZ": 3, "AE": 3, "BY": 1, "AZ": 1, "AM": 1, "CR": 1, "CW": 1, "GE": 1, "NZ": 1, "PT": 1, "AF": 1, "DZ": 2, "MY": 1, "IE": 4, "CY": 1}` |
| **Line type mix** | `{"proxy": 586, "dc": 1321, "home": 226, "mobile": 11, "unknown": 3}` |

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
