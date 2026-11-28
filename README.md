# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-29 02:23:49](https://img.shields.io/badge/updated-2026--11--29_02%3A23%3A49-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11534.7s](https://img.shields.io/badge/elapsed-11534.7s-lightgrey)
![profiles: 1130](https://img.shields.io/badge/profiles-1130-blue)
![live_hits: 1130](https://img.shields.io/badge/live__hits-1130-brightgreen)
![live_fail: 88543](https://img.shields.io/badge/live__fail-88543-orange)
![kept: 883](https://img.shields.io/badge/kept-883-blue)
![new: 247](https://img.shields.io/badge/new-247-success)
![dropped: 601](https://img.shields.io/badge/dropped-601-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-29 02:23:49 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11534.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `398682` |
| **Live PASS (pool hits)** | `1130` |
| **Live FAIL** | `88543` |
| **History retained** | `883` |
| **New PASS** | `247` |
| **History dropped** | `601` |
| **Previous public** | `1484` |
| **Published profiles (deduped)** | `1130` |
| **Share links (exportable)** | `1001` |
| **YAML proxies (exportable)** | `1001` |
| **Protocol mix** | `{"vless": 423, "hysteria2": 69, "shadowsocks": 387, "vmess": 115, "trojan": 7}` |
| **Country mix** | `{"US": 231, "NL": 117, "AE": 8, "CA": 82, "IT": 20, "DE": 69, "HK": 19, "FR": 42, "AT": 2, "NO": 1, "SG": 39, "ZA": 4, "IE": 1, "ES": 19, "TR": 24, "JP": 98, "GB": 37, "PL": 18, "BG": 10, "LV": 6, "LT": 4, "KR": 15, "RU": 25, "FI": 16, "SE": 9, "CH": 6, "BY": 8, "IN": 6, "CZ": 3, "GR": 1, "IR": 5, "VN": 2, "EE": 6, "SK": 4, "RO": 5, "SA": 2, "BR": 11, "CN": 1, "MY": 1, "KZ": 3, "TW": 4, "TH": 2, "AU": 3, "CY": 1, "IL": 1, "CR": 1, "NE": 4, "NG": 2, "AL": 2, "ID": 1}` |
| **Line type mix** | `{"proxy": 377, "dc": 497, "home": 98, "mobile": 29}` |

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
