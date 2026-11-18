# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-18 11:53:08](https://img.shields.io/badge/updated-2026--11--18_11%3A53%3A08-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11405.7s](https://img.shields.io/badge/elapsed-11405.7s-lightgrey)
![profiles: 1758](https://img.shields.io/badge/profiles-1758-blue)
![live_hits: 1758](https://img.shields.io/badge/live__hits-1758-brightgreen)
![live_fail: 87799](https://img.shields.io/badge/live__fail-87799-orange)
![kept: 928](https://img.shields.io/badge/kept-928-blue)
![new: 830](https://img.shields.io/badge/new-830-success)
![dropped: 86](https://img.shields.io/badge/dropped-86-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-18 11:53:08 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11405.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `405175` |
| **Live PASS (pool hits)** | `1758` |
| **Live FAIL** | `87799` |
| **History retained** | `928` |
| **New PASS** | `830` |
| **History dropped** | `86` |
| **Previous public** | `1014` |
| **Published profiles (deduped)** | `1758` |
| **Share links (exportable)** | `1530` |
| **YAML proxies (exportable)** | `1530` |
| **Protocol mix** | `{"hysteria2": 67, "shadowsocks": 383, "vmess": 131, "trojan": 124, "vless": 825}` |
| **Country mix** | `{"DE": 114, "TR": 47, "US": 335, "AT": 3, "NL": 132, "HK": 35, "CA": 343, "GB": 45, "FR": 41, "NO": 1, "AL": 2, "ZA": 5, "PL": 51, "IT": 22, "JP": 53, "ES": 31, "LT": 11, "BG": 9, "KR": 15, "FI": 14, "MX": 1, "CH": 18, "IN": 5, "SG": 61, "BR": 8, "CL": 1, "AU": 5, "SE": 20, "EE": 8, "RU": 24, "IR": 6, "LU": 1, "CZ": 2, "BY": 8, "GR": 1, "SK": 3, "AE": 3, "VN": 2, "KZ": 3, "RO": 2, "TW": 8, "MY": 3, "LV": 15, "NE": 3, "NG": 2, "BH": 1, "TH": 1, "VG": 1, "LY": 1, "IL": 1, "CR": 3, "DK": 1, "UA": 1, "MD": 2, "SA": 1, "SC": 2}` |
| **Line type mix** | `{"dc": 808, "proxy": 482, "home": 143, "mobile": 104}` |

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
