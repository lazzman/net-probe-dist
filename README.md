# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-05 04:02:44](https://img.shields.io/badge/updated-2026--08--05_04%3A02%3A44-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 1517.5s](https://img.shields.io/badge/elapsed-1517.5s-lightgrey)
![profiles: 1202](https://img.shields.io/badge/profiles-1202-blue)
![live_hits: 1206](https://img.shields.io/badge/live__hits-1206-brightgreen)
![live_fail: 9268](https://img.shields.io/badge/live__fail-9268-orange)
![kept: 766](https://img.shields.io/badge/kept-766-blue)
![new: 440](https://img.shields.io/badge/new-440-success)
![dropped: 185](https://img.shields.io/badge/dropped-185-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-05 04:02:44 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `1517.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `29032` |
| **Live PASS (pool hits)** | `1206` |
| **Live FAIL** | `9268` |
| **History retained** | `766` |
| **New PASS** | `440` |
| **History dropped** | `185` |
| **Previous public** | `951` |
| **Published profiles (deduped)** | `1202` |
| **Share links (exportable)** | `998` |
| **YAML proxies (exportable)** | `998` |
| **Protocol mix** | `{"vless": 577, "shadowsocks": 178, "vmess": 67, "trojan": 104, "hysteria2": 72}` |
| **Country mix** | `{"US": 155, "CA": 200, "PT": 1, "NL": 150, "RU": 47, "FI": 17, "EE": 4, "HK": 41, "DE": 65, "FR": 38, "IT": 19, "GB": 25, "PL": 12, "CH": 1, "TW": 12, "HU": 1, "SG": 22, "PA": 1, "LV": 7, "KZ": 3, "TR": 6, "JP": 45, "KR": 38, "SE": 15, "CO": 3, "IR": 3, "MD": 1, "ES": 6, "CZ": 1, "SA": 2, "SC": 5, "PH": 8, "LT": 2, "TH": 3, "CR": 1, "IE": 4, "NO": 1, "IN": 4, "ZA": 2, "AU": 3, "BG": 2, "CN": 4, "BR": 3, "BH": 1, "RO": 4, "AZ": 1, "AT": 4, "MY": 1, "AE": 1, "KH": 1, "DK": 3, "IL": 1}` |
| **Line type mix** | `{"dc": 516, "home": 54, "proxy": 425, "mobile": 5}` |

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
