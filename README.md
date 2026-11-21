# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-21 17:02:21](https://img.shields.io/badge/updated-2026--11--21_17%3A02%3A21-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11466.4s](https://img.shields.io/badge/elapsed-11466.4s-lightgrey)
![profiles: 1347](https://img.shields.io/badge/profiles-1347-blue)
![live_hits: 1347](https://img.shields.io/badge/live__hits-1347-brightgreen)
![live_fail: 88544](https://img.shields.io/badge/live__fail-88544-orange)
![kept: 1010](https://img.shields.io/badge/kept-1010-blue)
![new: 337](https://img.shields.io/badge/new-337-success)
![dropped: 437](https://img.shields.io/badge/dropped-437-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-21 17:02:21 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11466.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `405500` |
| **Live PASS (pool hits)** | `1347` |
| **Live FAIL** | `88544` |
| **History retained** | `1010` |
| **New PASS** | `337` |
| **History dropped** | `437` |
| **Previous public** | `1447` |
| **Published profiles (deduped)** | `1347` |
| **Share links (exportable)** | `1204` |
| **YAML proxies (exportable)** | `1204` |
| **Protocol mix** | `{"hysteria2": 78, "vmess": 118, "shadowsocks": 395, "vless": 517, "trojan": 96}` |
| **Country mix** | `{"US": 306, "AT": 2, "IT": 20, "DE": 109, "BY": 7, "SG": 53, "HK": 24, "NL": 136, "CN": 2, "IE": 1, "FI": 13, "NO": 1, "CA": 119, "ZA": 3, "CH": 15, "TR": 29, "JP": 50, "GB": 39, "ES": 26, "PL": 45, "LT": 7, "KR": 14, "FR": 33, "CL": 1, "BR": 15, "AU": 5, "SE": 17, "IN": 3, "EE": 13, "KZ": 4, "RU": 37, "UA": 2, "LV": 11, "LU": 1, "GR": 1, "AE": 3, "VN": 2, "CR": 1, "IR": 5, "RO": 2, "TW": 6, "LY": 1, "NE": 4, "BG": 7, "SK": 3, "MY": 1, "TH": 1, "CZ": 1, "DK": 1, "IL": 1, "NG": 1, "AL": 1, "SA": 1}` |
| **Line type mix** | `{"dc": 528, "proxy": 461, "mobile": 92, "home": 125}` |

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
