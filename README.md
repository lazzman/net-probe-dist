# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-15 23:34:27](https://img.shields.io/badge/updated-2026--08--15_23%3A34%3A27-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10244.2s](https://img.shields.io/badge/elapsed-10244.2s-lightgrey)
![profiles: 2349](https://img.shields.io/badge/profiles-2349-blue)
![live_hits: 2349](https://img.shields.io/badge/live__hits-2349-brightgreen)
![live_fail: 92887](https://img.shields.io/badge/live__fail-92887-orange)
![kept: 1362](https://img.shields.io/badge/kept-1362-blue)
![new: 987](https://img.shields.io/badge/new-987-success)
![dropped: 703](https://img.shields.io/badge/dropped-703-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-15 23:34:27 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10244.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `442126` |
| **Live PASS (pool hits)** | `2349` |
| **Live FAIL** | `92887` |
| **History retained** | `1362` |
| **New PASS** | `987` |
| **History dropped** | `703` |
| **Previous public** | `2065` |
| **Published profiles (deduped)** | `2349` |
| **Share links (exportable)** | `1623` |
| **YAML proxies (exportable)** | `1623` |
| **Protocol mix** | `{"vless": 838, "vmess": 87, "hysteria2": 134, "shadowsocks": 201, "trojan": 363}` |
| **Country mix** | `{"US": 197, "GB": 58, "NL": 213, "CA": 274, "AU": 13, "DE": 80, "JP": 173, "IN": 9, "TH": 4, "FI": 30, "DZ": 1, "KR": 105, "FR": 41, "HK": 59, "RU": 125, "BR": 3, "SG": 57, "TR": 10, "PL": 30, "NO": 3, "ZA": 4, "RO": 6, "CO": 3, "PH": 1, "IT": 5, "IE": 15, "ES": 11, "SC": 7, "KZ": 11, "IR": 2, "LV": 13, "CH": 1, "BG": 5, "AE": 1, "TW": 5, "EE": 10, "CZ": 3, "MD": 1, "AT": 3, "LT": 4, "AM": 1, "SE": 7, "ID": 1, "ZZ": 2, "AZ": 1, "AL": 1, "MY": 1, "CN": 4, "PT": 1, "OM": 1, "HU": 1, "SA": 1, "KG": 1, "GR": 1, "DK": 1, "CR": 2, "CY": 1, "IL": 1, "BA": 1, "KH": 1}` |
| **Line type mix** | `{"dc": 990, "proxy": 483, "home": 144, "mobile": 8, "unknown": 2}` |

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
