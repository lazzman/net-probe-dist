# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-29 23:09:28](https://img.shields.io/badge/updated-2026--08--29_23%3A09%3A28-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9581.2s](https://img.shields.io/badge/elapsed-9581.2s-lightgrey)
![profiles: 2032](https://img.shields.io/badge/profiles-2032-blue)
![live_hits: 2034](https://img.shields.io/badge/live__hits-2034-brightgreen)
![live_fail: 70847](https://img.shields.io/badge/live__fail-70847-orange)
![kept: 1261](https://img.shields.io/badge/kept-1261-blue)
![new: 773](https://img.shields.io/badge/new-773-success)
![dropped: 790](https://img.shields.io/badge/dropped-790-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-29 23:09:28 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9581.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `416755` |
| **Live PASS (pool hits)** | `2034` |
| **Live FAIL** | `70847` |
| **History retained** | `1261` |
| **New PASS** | `773` |
| **History dropped** | `790` |
| **Previous public** | `2051` |
| **Published profiles (deduped)** | `2032` |
| **Share links (exportable)** | `1457` |
| **YAML proxies (exportable)** | `1457` |
| **Protocol mix** | `{"vless": 913, "hysteria2": 188, "shadowsocks": 279, "vmess": 66, "trojan": 11}` |
| **Country mix** | `{"CH": 6, "DE": 97, "NL": 240, "PL": 25, "CA": 287, "DZ": 11, "RU": 25, "KR": 22, "GB": 76, "FI": 23, "SG": 93, "US": 224, "SE": 10, "TW": 24, "IE": 6, "AL": 2, "FR": 40, "NO": 18, "LT": 11, "ES": 9, "ZA": 3, "JP": 65, "HK": 24, "TH": 3, "MY": 5, "CN": 4, "IT": 8, "EE": 6, "IN": 7, "TR": 6, "KZ": 12, "CZ": 5, "DK": 1, "LV": 14, "BR": 13, "UA": 4, "MD": 2, "SA": 1, "SC": 2, "RO": 3, "AR": 2, "AU": 5, "BG": 5, "IR": 1, "AE": 1, "BY": 1, "PE": 1, "CO": 1, "SK": 1, "AT": 1, "GR": 2, "AM": 1, "MX": 2}` |
| **Line type mix** | `{"dc": 944, "home": 107, "proxy": 401, "mobile": 9}` |

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
