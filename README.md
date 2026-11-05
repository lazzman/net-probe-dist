# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-05 16:29:41](https://img.shields.io/badge/updated-2026--11--05_16%3A29%3A41-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11069.8s](https://img.shields.io/badge/elapsed-11069.8s-lightgrey)
![profiles: 1230](https://img.shields.io/badge/profiles-1230-blue)
![live_hits: 1230](https://img.shields.io/badge/live__hits-1230-brightgreen)
![live_fail: 86748](https://img.shields.io/badge/live__fail-86748-orange)
![kept: 893](https://img.shields.io/badge/kept-893-blue)
![new: 337](https://img.shields.io/badge/new-337-success)
![dropped: 298](https://img.shields.io/badge/dropped-298-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-05 16:29:41 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11069.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `403858` |
| **Live PASS (pool hits)** | `1230` |
| **Live FAIL** | `86748` |
| **History retained** | `893` |
| **New PASS** | `337` |
| **History dropped** | `298` |
| **Previous public** | `1191` |
| **Published profiles (deduped)** | `1230` |
| **Share links (exportable)** | `1017` |
| **YAML proxies (exportable)** | `1017` |
| **Protocol mix** | `{"shadowsocks": 302, "hysteria2": 154, "trojan": 98, "vless": 390, "vmess": 73}` |
| **Country mix** | `{"ES": 15, "DE": 58, "PL": 25, "US": 235, "HK": 27, "BY": 9, "NL": 151, "SE": 11, "NO": 1, "AT": 1, "RO": 3, "ZA": 2, "SG": 52, "GB": 26, "JP": 27, "CA": 148, "IN": 10, "IT": 19, "KR": 20, "PH": 1, "CH": 54, "MX": 4, "FR": 35, "TR": 5, "EE": 5, "RU": 23, "UA": 1, "CZ": 2, "FI": 9, "IR": 2, "AE": 2, "MY": 2, "TW": 3, "AU": 2, "IL": 2, "BR": 1, "LV": 3, "BG": 6, "RS": 1, "GR": 1, "VN": 1, "TH": 1, "CN": 1, "SA": 1, "LT": 9, "CR": 2, "SC": 1, "AL": 1}` |
| **Line type mix** | `{"proxy": 351, "mobile": 126, "dc": 480, "home": 64}` |

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
