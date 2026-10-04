# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-04 22:48:56](https://img.shields.io/badge/updated-2026--10--04_22%3A48%3A56-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10446.6s](https://img.shields.io/badge/elapsed-10446.6s-lightgrey)
![profiles: 1404](https://img.shields.io/badge/profiles-1404-blue)
![live_hits: 1404](https://img.shields.io/badge/live__hits-1404-brightgreen)
![live_fail: 78991](https://img.shields.io/badge/live__fail-78991-orange)
![kept: 999](https://img.shields.io/badge/kept-999-blue)
![new: 405](https://img.shields.io/badge/new-405-success)
![dropped: 759](https://img.shields.io/badge/dropped-759-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-04 22:48:56 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10446.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `436936` |
| **Live PASS (pool hits)** | `1404` |
| **Live FAIL** | `78991` |
| **History retained** | `999` |
| **New PASS** | `405` |
| **History dropped** | `759` |
| **Previous public** | `1758` |
| **Published profiles (deduped)** | `1404` |
| **Share links (exportable)** | `1170` |
| **YAML proxies (exportable)** | `1170` |
| **Protocol mix** | `{"vless": 623, "trojan": 80, "shadowsocks": 263, "vmess": 96, "hysteria2": 108}` |
| **Country mix** | `{"US": 217, "FR": 27, "ZA": 5, "DE": 61, "CA": 257, "NL": 143, "GB": 32, "SG": 43, "RU": 20, "KR": 40, "ID": 3, "IE": 5, "NO": 2, "ES": 12, "CH": 9, "JP": 55, "CL": 13, "HK": 47, "TW": 5, "AE": 2, "TH": 2, "IN": 8, "FI": 12, "IT": 16, "GR": 3, "LU": 2, "RO": 6, "EE": 8, "LV": 6, "SE": 7, "KZ": 5, "PL": 18, "AM": 2, "TR": 5, "MY": 10, "CN": 17, "BR": 1, "AU": 4, "CW": 1, "GT": 1, "CO": 1, "AL": 2, "SC": 3, "CZ": 14, "LT": 10, "BG": 9, "SA": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 711, "proxy": 368, "mobile": 20, "home": 74}` |

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
