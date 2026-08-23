# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-23 12:02:48](https://img.shields.io/badge/updated-2026--08--23_12%3A02%3A48-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9141.0s](https://img.shields.io/badge/elapsed-9141.0s-lightgrey)
![profiles: 4445](https://img.shields.io/badge/profiles-4445-blue)
![live_hits: 4446](https://img.shields.io/badge/live__hits-4446-brightgreen)
![live_fail: 65152](https://img.shields.io/badge/live__fail-65152-orange)
![kept: 1362](https://img.shields.io/badge/kept-1362-blue)
![new: 3084](https://img.shields.io/badge/new-3084-success)
![dropped: 183](https://img.shields.io/badge/dropped-183-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-23 12:02:48 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9141.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `424617` |
| **Live PASS (pool hits)** | `4446` |
| **Live FAIL** | `65152` |
| **History retained** | `1362` |
| **New PASS** | `3084` |
| **History dropped** | `183` |
| **Previous public** | `1545` |
| **Published profiles (deduped)** | `4445` |
| **Share links (exportable)** | `2716` |
| **YAML proxies (exportable)** | `2716` |
| **Protocol mix** | `{"vmess": 70, "vless": 1980, "shadowsocks": 317, "hysteria2": 193, "trojan": 156}` |
| **Country mix** | `{"US": 382, "NL": 315, "AU": 22, "DE": 170, "FR": 53, "GB": 138, "BG": 12, "PL": 48, "JP": 62, "SG": 79, "RU": 54, "FI": 40, "SE": 25, "HK": 79, "BR": 26, "TW": 18, "TR": 18, "CA": 884, "IN": 14, "LT": 14, "ES": 8, "ZA": 4, "TH": 7, "CN": 25, "ZZ": 3, "AT": 3, "EE": 18, "KZ": 18, "BE": 1, "SC": 24, "IT": 20, "CH": 11, "DK": 3, "VN": 2, "HU": 3, "LV": 15, "NO": 4, "CO": 7, "SK": 1, "MD": 2, "KR": 20, "CY": 4, "BZ": 9, "PT": 2, "IR": 3, "UA": 8, "CZ": 4, "NZ": 3, "AZ": 1, "AL": 4, "RO": 3, "UZ": 1, "PE": 2, "AE": 3, "CW": 6, "PH": 1, "ME": 1, "BY": 2, "CR": 2, "IE": 4, "AF": 1, "DZ": 2, "VG": 1, "MY": 1}` |
| **Line type mix** | `{"dc": 1742, "home": 247, "proxy": 717, "mobile": 11, "unknown": 3}` |

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
