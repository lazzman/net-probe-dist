# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-30 15:16:00](https://img.shields.io/badge/updated-2026--09--30_15%3A16%3A00-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10282.7s](https://img.shields.io/badge/elapsed-10282.7s-lightgrey)
![profiles: 3512](https://img.shields.io/badge/profiles-3512-blue)
![live_hits: 3512](https://img.shields.io/badge/live__hits-3512-brightgreen)
![live_fail: 76111](https://img.shields.io/badge/live__fail-76111-orange)
![kept: 1121](https://img.shields.io/badge/kept-1121-blue)
![new: 2391](https://img.shields.io/badge/new-2391-success)
![dropped: 387](https://img.shields.io/badge/dropped-387-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-30 15:16:00 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10282.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `433655` |
| **Live PASS (pool hits)** | `3512` |
| **Live FAIL** | `76111` |
| **History retained** | `1121` |
| **New PASS** | `2391` |
| **History dropped** | `387` |
| **Previous public** | `1508` |
| **Published profiles (deduped)** | `3512` |
| **Share links (exportable)** | `1989` |
| **YAML proxies (exportable)** | `1989` |
| **Protocol mix** | `{"vless": 1465, "vmess": 81, "trojan": 38, "hysteria2": 122, "shadowsocks": 283}` |
| **Country mix** | `{"US": 281, "CA": 859, "GB": 89, "IE": 3, "ES": 9, "DE": 92, "NL": 164, "RU": 33, "FR": 34, "ID": 3, "NO": 4, "RO": 4, "ZA": 3, "CH": 8, "JP": 42, "SE": 19, "AT": 3, "FI": 24, "LV": 10, "SG": 40, "HK": 39, "KZ": 8, "AE": 3, "TH": 4, "IN": 10, "IT": 22, "EE": 6, "ZZ": 1, "PL": 22, "UA": 6, "AD": 1, "MY": 10, "LT": 12, "TW": 6, "KR": 34, "SC": 3, "CL": 1, "HU": 2, "SK": 2, "CR": 2, "DZ": 28, "CY": 2, "TR": 2, "AU": 6, "GE": 1, "IR": 1, "NZ": 1, "PT": 1, "BZ": 4, "BR": 1, "CW": 4, "GT": 1, "GR": 1, "MX": 1, "BG": 11, "AL": 2, "VG": 1, "AM": 2, "SA": 1, "CZ": 6, "CN": 1}` |
| **Line type mix** | `{"dc": 1400, "home": 89, "mobile": 22, "proxy": 484, "unknown": 1}` |

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
