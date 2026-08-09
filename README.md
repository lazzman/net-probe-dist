# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-09 17:55:01](https://img.shields.io/badge/updated-2026--08--09_17%3A55%3A01-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10179.8s](https://img.shields.io/badge/elapsed-10179.8s-lightgrey)
![profiles: 2632](https://img.shields.io/badge/profiles-2632-blue)
![live_hits: 2632](https://img.shields.io/badge/live__hits-2632-brightgreen)
![live_fail: 91079](https://img.shields.io/badge/live__fail-91079-orange)
![kept: 1298](https://img.shields.io/badge/kept-1298-blue)
![new: 1334](https://img.shields.io/badge/new-1334-success)
![dropped: 877](https://img.shields.io/badge/dropped-877-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-09 17:55:01 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10179.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `445961` |
| **Live PASS (pool hits)** | `2632` |
| **Live FAIL** | `91079` |
| **History retained** | `1298` |
| **New PASS** | `1334` |
| **History dropped** | `877` |
| **Previous public** | `2175` |
| **Published profiles (deduped)** | `2632` |
| **Share links (exportable)** | `1575` |
| **YAML proxies (exportable)** | `1575` |
| **Protocol mix** | `{"vless": 1087, "vmess": 72, "shadowsocks": 203, "hysteria2": 116, "trojan": 97}` |
| **Country mix** | `{"US": 173, "NL": 217, "AU": 4, "DE": 111, "ES": 7, "FR": 41, "TH": 3, "GB": 50, "IT": 9, "KR": 50, "SE": 14, "HK": 38, "RO": 6, "BR": 3, "JP": 53, "FI": 45, "TW": 7, "IN": 6, "ZA": 2, "CA": 475, "BG": 5, "IE": 4, "PL": 16, "SA": 3, "AT": 3, "PT": 1, "TR": 6, "EE": 7, "RU": 133, "AE": 4, "BE": 5, "CH": 2, "CZ": 1, "HU": 1, "SG": 28, "CO": 7, "KZ": 4, "LT": 3, "PH": 3, "CN": 6, "SC": 2, "NO": 1, "UA": 2, "AZ": 1, "MD": 1, "AL": 2, "BZ": 1, "LV": 5, "AF": 1, "AM": 1, "VN": 1, "IR": 1, "GR": 1, "DK": 1, "CR": 2, "CY": 1, "KH": 1}` |
| **Line type mix** | `{"dc": 918, "proxy": 516, "home": 137, "mobile": 10}` |

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
