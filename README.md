# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-04 17:01:06](https://img.shields.io/badge/updated-2026--08--04_17%3A01%3A06-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 1502.9s](https://img.shields.io/badge/elapsed-1502.9s-lightgrey)
![profiles: 1572](https://img.shields.io/badge/profiles-1572-blue)
![live_hits: 1582](https://img.shields.io/badge/live__hits-1582-brightgreen)
![live_fail: 9025](https://img.shields.io/badge/live__fail-9025-orange)
![kept: 1199](https://img.shields.io/badge/kept-1199-blue)
![new: 383](https://img.shields.io/badge/new-383-success)
![dropped: 347](https://img.shields.io/badge/dropped-347-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-04 17:01:06 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `1502.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `28053` |
| **Live PASS (pool hits)** | `1582` |
| **Live FAIL** | `9025` |
| **History retained** | `1199` |
| **New PASS** | `383` |
| **History dropped** | `347` |
| **Previous public** | `1546` |
| **Published profiles (deduped)** | `1572` |
| **Share links (exportable)** | `1305` |
| **YAML proxies (exportable)** | `1305` |
| **Protocol mix** | `{"vless": 911, "shadowsocks": 176, "trojan": 91, "vmess": 60, "hysteria2": 67}` |
| **Country mix** | `{"US": 175, "DE": 67, "CA": 403, "NL": 181, "RU": 45, "FI": 24, "GB": 20, "IT": 15, "FR": 35, "AT": 5, "PL": 16, "BE": 2, "CH": 1, "HK": 33, "TW": 11, "HU": 1, "SG": 23, "SE": 19, "PA": 1, "ES": 8, "KZ": 3, "JP": 48, "ID": 1, "CO": 18, "TR": 6, "SC": 7, "MD": 1, "EE": 3, "LV": 7, "PH": 43, "LT": 1, "CR": 2, "IN": 4, "BG": 4, "IE": 1, "ZA": 2, "NO": 1, "KR": 39, "MY": 1, "BH": 1, "CN": 2, "RO": 3, "IS": 4, "AZ": 1, "AE": 1, "AU": 4, "BR": 5, "KH": 1, "SA": 3, "TH": 1, "DK": 2, "IL": 1, "IR": 1}` |
| **Line type mix** | `{"dc": 763, "home": 68, "proxy": 471, "mobile": 5}` |

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
