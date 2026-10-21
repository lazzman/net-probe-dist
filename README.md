# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-21 22:20:19](https://img.shields.io/badge/updated-2026--10--21_22%3A20%3A19-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10865.7s](https://img.shields.io/badge/elapsed-10865.7s-lightgrey)
![profiles: 1236](https://img.shields.io/badge/profiles-1236-blue)
![live_hits: 1236](https://img.shields.io/badge/live__hits-1236-brightgreen)
![live_fail: 85210](https://img.shields.io/badge/live__fail-85210-orange)
![kept: 873](https://img.shields.io/badge/kept-873-blue)
![new: 363](https://img.shields.io/badge/new-363-success)
![dropped: 474](https://img.shields.io/badge/dropped-474-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-21 22:20:19 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10865.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `411921` |
| **Live PASS (pool hits)** | `1236` |
| **Live FAIL** | `85210` |
| **History retained** | `873` |
| **New PASS** | `363` |
| **History dropped** | `474` |
| **Previous public** | `1347` |
| **Published profiles (deduped)** | `1236` |
| **Share links (exportable)** | `1068` |
| **YAML proxies (exportable)** | `1068` |
| **Protocol mix** | `{"shadowsocks": 239, "hysteria2": 95, "trojan": 132, "vless": 534, "vmess": 68}` |
| **Country mix** | `{"IT": 17, "GB": 46, "NL": 170, "US": 150, "SE": 4, "HK": 32, "NO": 1, "IE": 3, "DE": 76, "ZA": 2, "CH": 40, "RO": 4, "JP": 37, "KR": 24, "IN": 11, "IR": 5, "CA": 245, "PL": 12, "ES": 7, "CR": 1, "AT": 1, "SC": 6, "LV": 15, "ME": 2, "RU": 21, "FR": 28, "SG": 41, "AE": 4, "FI": 10, "BY": 6, "KZ": 3, "CZ": 4, "SA": 1, "LT": 2, "DK": 3, "AM": 1, "TW": 4, "EE": 3, "BR": 2, "AL": 1, "TR": 7, "MX": 2, "UA": 3, "BG": 3, "AU": 4, "GR": 1, "MD": 4, "MY": 1, "ID": 1, "CN": 1, "IL": 1}` |
| **Line type mix** | `{"dc": 628, "proxy": 309, "home": 84, "mobile": 52}` |

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
