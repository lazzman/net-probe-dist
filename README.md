# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-08 04:13:19](https://img.shields.io/badge/updated-2026--09--08_04%3A13%3A19-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9994.6s](https://img.shields.io/badge/elapsed-9994.6s-lightgrey)
![profiles: 1857](https://img.shields.io/badge/profiles-1857-blue)
![live_hits: 1857](https://img.shields.io/badge/live__hits-1857-brightgreen)
![live_fail: 74874](https://img.shields.io/badge/live__fail-74874-orange)
![kept: 1140](https://img.shields.io/badge/kept-1140-blue)
![new: 717](https://img.shields.io/badge/new-717-success)
![dropped: 200](https://img.shields.io/badge/dropped-200-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-08 04:13:19 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9994.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `439349` |
| **Live PASS (pool hits)** | `1857` |
| **Live FAIL** | `74874` |
| **History retained** | `1140` |
| **New PASS** | `717` |
| **History dropped** | `200` |
| **Previous public** | `1340` |
| **Published profiles (deduped)** | `1857` |
| **Share links (exportable)** | `1287` |
| **YAML proxies (exportable)** | `1287` |
| **Protocol mix** | `{"trojan": 13, "hysteria2": 163, "vless": 790, "shadowsocks": 262, "vmess": 59}` |
| **Country mix** | `{"US": 196, "SG": 55, "CA": 295, "JP": 55, "GB": 65, "FI": 15, "RU": 22, "DZ": 23, "NL": 212, "TW": 17, "DE": 50, "ZA": 5, "ID": 1, "FR": 36, "IE": 2, "PL": 37, "ES": 10, "MY": 2, "CN": 3, "IT": 10, "KR": 26, "HR": 1, "KZ": 6, "JE": 1, "NO": 20, "EE": 10, "IN": 4, "IR": 1, "HK": 40, "LV": 7, "GR": 2, "TR": 6, "SE": 8, "AT": 2, "LT": 9, "EG": 1, "TH": 2, "SA": 1, "AM": 1, "UA": 2, "HU": 2, "AR": 2, "CZ": 2, "UZ": 1, "AU": 2, "BR": 2, "GT": 1, "BY": 1, "SK": 1, "PH": 1, "SC": 1, "RO": 2, "CH": 2, "CY": 1, "BG": 5, "CR": 1}` |
| **Line type mix** | `{"dc": 789, "home": 115, "proxy": 375, "mobile": 9}` |

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
