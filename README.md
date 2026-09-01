# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-01 22:03:13](https://img.shields.io/badge/updated-2026--09--01_22%3A03%3A13-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9802.2s](https://img.shields.io/badge/elapsed-9802.2s-lightgrey)
![profiles: 2433](https://img.shields.io/badge/profiles-2433-blue)
![live_hits: 2433](https://img.shields.io/badge/live__hits-2433-brightgreen)
![live_fail: 72989](https://img.shields.io/badge/live__fail-72989-orange)
![kept: 1397](https://img.shields.io/badge/kept-1397-blue)
![new: 1036](https://img.shields.io/badge/new-1036-success)
![dropped: 1084](https://img.shields.io/badge/dropped-1084-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-01 22:03:13 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9802.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `428963` |
| **Live PASS (pool hits)** | `2433` |
| **Live FAIL** | `72989` |
| **History retained** | `1397` |
| **New PASS** | `1036` |
| **History dropped** | `1084` |
| **Previous public** | `2481` |
| **Published profiles (deduped)** | `2433` |
| **Share links (exportable)** | `1637` |
| **YAML proxies (exportable)** | `1637` |
| **Protocol mix** | `{"hysteria2": 187, "shadowsocks": 257, "vless": 1105, "trojan": 20, "vmess": 68}` |
| **Country mix** | `{"PL": 33, "FI": 30, "MD": 2, "US": 254, "IT": 10, "FR": 34, "DZ": 15, "NL": 249, "GB": 78, "DE": 91, "SE": 14, "TW": 23, "CA": 391, "NO": 17, "ES": 13, "ZA": 3, "TH": 5, "MY": 3, "JP": 61, "RU": 38, "CN": 4, "KZ": 12, "EE": 5, "KR": 27, "IN": 6, "TR": 4, "SG": 84, "CH": 7, "HK": 31, "IR": 1, "DK": 1, "LV": 13, "UA": 2, "GR": 3, "UZ": 3, "BG": 5, "LT": 12, "AL": 3, "RO": 3, "ID": 1, "IE": 6, "CZ": 5, "PH": 2, "CO": 4, "HR": 1, "AT": 3, "AR": 2, "JE": 1, "AU": 6, "BR": 9, "AE": 1, "SC": 2, "SK": 1, "EG": 1, "AM": 1, "SA": 1, "CR": 1, "MX": 2}` |
| **Line type mix** | `{"proxy": 416, "home": 134, "dc": 1081, "mobile": 9}` |

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
