# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-03 02:52:47](https://img.shields.io/badge/updated-2026--09--03_02%3A52%3A47-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9752.3s](https://img.shields.io/badge/elapsed-9752.3s-lightgrey)
![profiles: 1999](https://img.shields.io/badge/profiles-1999-blue)
![live_hits: 2000](https://img.shields.io/badge/live__hits-2000-brightgreen)
![live_fail: 73048](https://img.shields.io/badge/live__fail-73048-orange)
![kept: 1227](https://img.shields.io/badge/kept-1227-blue)
![new: 773](https://img.shields.io/badge/new-773-success)
![dropped: 381](https://img.shields.io/badge/dropped-381-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-03 02:52:47 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9752.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `425910` |
| **Live PASS (pool hits)** | `2000` |
| **Live FAIL** | `73048` |
| **History retained** | `1227` |
| **New PASS** | `773` |
| **History dropped** | `381` |
| **Previous public** | `1608` |
| **Published profiles (deduped)** | `1999` |
| **Share links (exportable)** | `1372` |
| **YAML proxies (exportable)** | `1372` |
| **Protocol mix** | `{"hysteria2": 190, "shadowsocks": 250, "vless": 846, "trojan": 15, "vmess": 71}` |
| **Country mix** | `{"JP": 63, "FI": 18, "SG": 67, "KR": 23, "NL": 231, "PL": 29, "CA": 224, "LT": 12, "DZ": 17, "GB": 68, "US": 241, "RU": 28, "SE": 9, "DE": 85, "TW": 21, "FR": 29, "ES": 7, "RO": 3, "TH": 4, "CN": 11, "IT": 10, "KZ": 15, "CH": 7, "EE": 6, "NO": 16, "IN": 9, "LV": 10, "HK": 39, "IR": 3, "BR": 8, "UA": 3, "UZ": 3, "AU": 5, "TR": 3, "GR": 3, "AL": 3, "SA": 1, "MY": 2, "ZA": 4, "PH": 2, "CO": 1, "ID": 1, "IE": 3, "JE": 1, "AR": 2, "SC": 4, "MX": 3, "BG": 2, "CZ": 3, "AE": 4, "MD": 1, "SK": 1, "AT": 2, "EG": 1, "AM": 1, "BY": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 845, "home": 134, "proxy": 384, "mobile": 11}` |

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
