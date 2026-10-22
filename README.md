# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-22 22:21:24](https://img.shields.io/badge/updated-2026--10--22_22%3A21%3A24-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10935.5s](https://img.shields.io/badge/elapsed-10935.5s-lightgrey)
![profiles: 1227](https://img.shields.io/badge/profiles-1227-blue)
![live_hits: 1227](https://img.shields.io/badge/live__hits-1227-brightgreen)
![live_fail: 85335](https://img.shields.io/badge/live__fail-85335-orange)
![kept: 848](https://img.shields.io/badge/kept-848-blue)
![new: 379](https://img.shields.io/badge/new-379-success)
![dropped: 531](https://img.shields.io/badge/dropped-531-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-22 22:21:24 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10935.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `412191` |
| **Live PASS (pool hits)** | `1227` |
| **Live FAIL** | `85335` |
| **History retained** | `848` |
| **New PASS** | `379` |
| **History dropped** | `531` |
| **Previous public** | `1379` |
| **Published profiles (deduped)** | `1227` |
| **Share links (exportable)** | `1025` |
| **YAML proxies (exportable)** | `1025` |
| **Protocol mix** | `{"shadowsocks": 256, "hysteria2": 97, "trojan": 106, "vless": 505, "vmess": 61}` |
| **Country mix** | `{"IT": 19, "NL": 160, "US": 148, "GB": 37, "SE": 8, "HK": 37, "NO": 1, "IE": 2, "DE": 69, "RO": 6, "ZA": 2, "CH": 36, "JP": 30, "RU": 20, "KR": 26, "IN": 11, "CA": 213, "TH": 2, "PL": 14, "LV": 13, "ES": 12, "CR": 2, "AT": 1, "SC": 3, "ME": 3, "FR": 28, "FI": 17, "EE": 1, "SG": 45, "IR": 2, "TR": 8, "AE": 3, "IL": 1, "CZ": 2, "MY": 3, "UA": 2, "DK": 1, "AM": 2, "TW": 3, "CN": 2, "CL": 1, "KZ": 4, "BY": 6, "AU": 3, "AL": 4, "BG": 3, "CW": 1, "RS": 1, "GR": 1, "MD": 1, "BR": 2, "SA": 1, "LT": 4}` |
| **Line type mix** | `{"dc": 560, "proxy": 328, "home": 92, "mobile": 47}` |

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
