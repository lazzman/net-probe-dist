# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-26 12:04:47](https://img.shields.io/badge/updated-2026--08--26_12%3A04%3A47-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9303.6s](https://img.shields.io/badge/elapsed-9303.6s-lightgrey)
![profiles: 4611](https://img.shields.io/badge/profiles-4611-blue)
![live_hits: 4612](https://img.shields.io/badge/live__hits-4612-brightgreen)
![live_fail: 67403](https://img.shields.io/badge/live__fail-67403-orange)
![kept: 1410](https://img.shields.io/badge/kept-1410-blue)
![new: 3202](https://img.shields.io/badge/new-3202-success)
![dropped: 155](https://img.shields.io/badge/dropped-155-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-26 12:04:47 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9303.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `427369` |
| **Live PASS (pool hits)** | `4612` |
| **Live FAIL** | `67403` |
| **History retained** | `1410` |
| **New PASS** | `3202` |
| **History dropped** | `155` |
| **Previous public** | `1565` |
| **Published profiles (deduped)** | `4611` |
| **Share links (exportable)** | `3037` |
| **YAML proxies (exportable)** | `3037` |
| **Protocol mix** | `{"hysteria2": 201, "vmess": 59, "vless": 2379, "shadowsocks": 329, "trojan": 69}` |
| **Country mix** | `{"PL": 37, "US": 405, "DE": 175, "HU": 3, "CA": 1139, "NL": 341, "JP": 51, "DZ": 9, "RU": 61, "GB": 151, "FI": 57, "SE": 27, "BR": 20, "TW": 11, "IE": 10, "ZA": 4, "FR": 43, "IN": 14, "LT": 12, "ES": 9, "HK": 64, "KR": 32, "TH": 8, "SG": 76, "IT": 13, "AT": 7, "LV": 25, "CH": 10, "KZ": 17, "EE": 30, "TR": 14, "NO": 13, "SC": 13, "DK": 5, "UA": 10, "VI": 2, "VN": 1, "PH": 2, "SK": 2, "BG": 17, "CZ": 10, "GE": 2, "IR": 20, "MD": 1, "CN": 7, "CY": 4, "BZ": 9, "AL": 3, "BY": 2, "PT": 1, "IS": 1, "CO": 3, "BE": 3, "MY": 4, "AM": 1, "RO": 4, "MX": 1, "AE": 3, "PE": 1, "AU": 6, "NZ": 2, "CW": 6, "ME": 1, "SI": 1, "CR": 11, "AF": 1}` |
| **Line type mix** | `{"dc": 2075, "home": 286, "proxy": 677, "mobile": 10}` |

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
