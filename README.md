# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-09 16:03:40](https://img.shields.io/badge/updated-2026--11--09_16%3A03%3A40-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11283.1s](https://img.shields.io/badge/elapsed-11283.1s-lightgrey)
![profiles: 1491](https://img.shields.io/badge/profiles-1491-blue)
![live_hits: 1491](https://img.shields.io/badge/live__hits-1491-brightgreen)
![live_fail: 86837](https://img.shields.io/badge/live__fail-86837-orange)
![kept: 910](https://img.shields.io/badge/kept-910-blue)
![new: 581](https://img.shields.io/badge/new-581-success)
![dropped: 291](https://img.shields.io/badge/dropped-291-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-09 16:03:40 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11283.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `398955` |
| **Live PASS (pool hits)** | `1491` |
| **Live FAIL** | `86837` |
| **History retained** | `910` |
| **New PASS** | `581` |
| **History dropped** | `291` |
| **Previous public** | `1201` |
| **Published profiles (deduped)** | `1491` |
| **Share links (exportable)** | `1152` |
| **YAML proxies (exportable)** | `1152` |
| **Protocol mix** | `{"shadowsocks": 336, "hysteria2": 140, "trojan": 103, "vless": 454, "vmess": 119}` |
| **Country mix** | `{"ES": 24, "GB": 36, "US": 275, "FR": 40, "DE": 61, "CA": 148, "PL": 22, "BY": 9, "NL": 148, "HK": 36, "SE": 24, "RU": 28, "IR": 2, "AT": 3, "AL": 1, "ZA": 3, "RO": 4, "JP": 35, "IN": 7, "SG": 56, "CH": 56, "IT": 25, "KR": 30, "MX": 2, "IL": 1, "TH": 2, "AU": 5, "UA": 3, "EE": 6, "AE": 2, "NO": 2, "TR": 6, "FI": 10, "SK": 1, "BG": 11, "IS": 1, "DK": 1, "LV": 5, "TW": 4, "GR": 1, "VN": 1, "MY": 1, "KZ": 1, "BR": 1, "LT": 10, "MD": 1, "NG": 1, "IE": 1, "CZ": 1, "SA": 1, "CN": 1, "CW": 1}` |
| **Line type mix** | `{"proxy": 430, "mobile": 128, "dc": 520, "home": 79}` |

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
