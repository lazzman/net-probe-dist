# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-30 15:46:05](https://img.shields.io/badge/updated-2026--10--30_15%3A46%3A05-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11062.9s](https://img.shields.io/badge/elapsed-11062.9s-lightgrey)
![profiles: 1523](https://img.shields.io/badge/profiles-1523-blue)
![live_hits: 1523](https://img.shields.io/badge/live__hits-1523-brightgreen)
![live_fail: 86253](https://img.shields.io/badge/live__fail-86253-orange)
![kept: 928](https://img.shields.io/badge/kept-928-blue)
![new: 595](https://img.shields.io/badge/new-595-success)
![dropped: 360](https://img.shields.io/badge/dropped-360-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-30 15:46:05 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11062.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `422679` |
| **Live PASS (pool hits)** | `1523` |
| **Live FAIL** | `86253` |
| **History retained** | `928` |
| **New PASS** | `595` |
| **History dropped** | `360` |
| **Previous public** | `1288` |
| **Published profiles (deduped)** | `1523` |
| **Share links (exportable)** | `1308` |
| **YAML proxies (exportable)** | `1308` |
| **Protocol mix** | `{"shadowsocks": 256, "hysteria2": 105, "trojan": 165, "vless": 714, "vmess": 68}` |
| **Country mix** | `{"IT": 19, "DE": 69, "NL": 181, "US": 218, "GB": 42, "BG": 10, "NO": 1, "FI": 19, "UA": 4, "ZA": 3, "RO": 3, "CH": 51, "AL": 2, "CA": 354, "JP": 21, "LT": 13, "IN": 10, "PL": 13, "SG": 49, "MX": 6, "ES": 10, "HU": 1, "AT": 1, "LV": 8, "HK": 33, "RU": 22, "FR": 36, "TH": 2, "SE": 8, "BY": 7, "AE": 5, "CY": 2, "KZ": 6, "BR": 5, "SA": 1, "CR": 3, "IL": 5, "AM": 1, "EE": 4, "TR": 4, "KR": 22, "AU": 7, "SC": 3, "BZ": 4, "CW": 4, "TW": 1, "GR": 1, "DK": 1, "VN": 1, "MY": 2, "IR": 7, "VG": 2, "CZ": 2, "PT": 1, "MD": 1, "ID": 1, "NZ": 1}` |
| **Line type mix** | `{"dc": 767, "mobile": 117, "proxy": 331, "home": 98}` |

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
