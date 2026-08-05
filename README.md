# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-05 22:34:06](https://img.shields.io/badge/updated-2026--08--05_22%3A34%3A06-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 1559.1s](https://img.shields.io/badge/elapsed-1559.1s-lightgrey)
![profiles: 1311](https://img.shields.io/badge/profiles-1311-blue)
![live_hits: 1318](https://img.shields.io/badge/live__hits-1318-brightgreen)
![live_fail: 9476](https://img.shields.io/badge/live__fail-9476-orange)
![kept: 910](https://img.shields.io/badge/kept-910-blue)
![new: 408](https://img.shields.io/badge/new-408-success)
![dropped: 265](https://img.shields.io/badge/dropped-265-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-05 22:34:06 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `1559.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `29372` |
| **Live PASS (pool hits)** | `1318` |
| **Live FAIL** | `9476` |
| **History retained** | `910` |
| **New PASS** | `408` |
| **History dropped** | `265` |
| **Previous public** | `1175` |
| **Published profiles (deduped)** | `1311` |
| **Share links (exportable)** | `1072` |
| **YAML proxies (exportable)** | `1072` |
| **Protocol mix** | `{"vless": 641, "shadowsocks": 193, "vmess": 67, "trojan": 90, "hysteria2": 81}` |
| **Country mix** | `{"GB": 29, "US": 166, "CA": 237, "PT": 2, "NL": 160, "ES": 10, "RU": 56, "SE": 15, "FI": 24, "EE": 5, "HK": 35, "DE": 57, "PL": 10, "LT": 3, "CH": 1, "AT": 5, "CZ": 1, "TW": 9, "FR": 42, "SG": 24, "PA": 1, "LV": 7, "JP": 42, "KZ": 4, "TR": 2, "KR": 47, "HU": 1, "DK": 3, "IT": 20, "CO": 9, "MD": 1, "SA": 3, "CN": 4, "PH": 5, "CR": 1, "IN": 4, "RO": 2, "TH": 2, "BG": 2, "ZA": 2, "NO": 1, "IE": 4, "BH": 1, "AZ": 1, "AE": 1, "MX": 1, "MY": 1, "IR": 1, "AU": 3, "BR": 8, "KH": 1}` |
| **Line type mix** | `{"dc": 562, "home": 56, "proxy": 453, "mobile": 5}` |

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
