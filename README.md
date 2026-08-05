# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-05 10:54:12](https://img.shields.io/badge/updated-2026--08--05_10%3A54%3A12-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 1516.2s](https://img.shields.io/badge/elapsed-1516.2s-lightgrey)
![profiles: 2053](https://img.shields.io/badge/profiles-2053-blue)
![live_hits: 2072](https://img.shields.io/badge/live__hits-2072-brightgreen)
![live_fail: 9006](https://img.shields.io/badge/live__fail-9006-orange)
![kept: 903](https://img.shields.io/badge/kept-903-blue)
![new: 1169](https://img.shields.io/badge/new-1169-success)
![dropped: 95](https://img.shields.io/badge/dropped-95-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-05 10:54:12 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `1516.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `30166` |
| **Live PASS (pool hits)** | `2072` |
| **Live FAIL** | `9006` |
| **History retained** | `903` |
| **New PASS** | `1169` |
| **History dropped** | `95` |
| **Previous public** | `998` |
| **Published profiles (deduped)** | `2053` |
| **Share links (exportable)** | `1408` |
| **YAML proxies (exportable)** | `1408` |
| **Protocol mix** | `{"vless": 958, "shadowsocks": 196, "vmess": 71, "trojan": 109, "hysteria2": 74}` |
| **Country mix** | `{"US": 193, "CA": 425, "NL": 166, "PT": 2, "FI": 21, "RU": 72, "ES": 12, "DE": 88, "FR": 54, "IR": 3, "PL": 12, "HK": 34, "SE": 18, "EE": 7, "LT": 3, "CH": 1, "CN": 3, "TW": 13, "HU": 1, "CR": 1, "SG": 22, "GB": 39, "PA": 1, "BG": 5, "BR": 5, "LV": 7, "KZ": 4, "TR": 7, "JP": 51, "KR": 47, "DK": 3, "IT": 21, "CO": 3, "AT": 4, "MD": 1, "CZ": 1, "SC": 9, "PH": 27, "CY": 3, "BZ": 1, "IN": 4, "ZA": 2, "TH": 2, "NO": 1, "SA": 3, "MY": 2, "BH": 1, "IE": 3, "AZ": 1, "RO": 4, "AE": 1, "BE": 1, "IL": 1, "AU": 3, "KH": 1}` |
| **Line type mix** | `{"dc": 804, "home": 72, "proxy": 538, "mobile": 6}` |

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
