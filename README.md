# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-26 03:33:54](https://img.shields.io/badge/updated-2026--09--26_03%3A33%3A54-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10120.3s](https://img.shields.io/badge/elapsed-10120.3s-lightgrey)
![profiles: 1265](https://img.shields.io/badge/profiles-1265-blue)
![live_hits: 1265](https://img.shields.io/badge/live__hits-1265-brightgreen)
![live_fail: 77241](https://img.shields.io/badge/live__fail-77241-orange)
![kept: 978](https://img.shields.io/badge/kept-978-blue)
![new: 287](https://img.shields.io/badge/new-287-success)
![dropped: 220](https://img.shields.io/badge/dropped-220-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-26 03:33:54 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10120.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `435568` |
| **Live PASS (pool hits)** | `1265` |
| **Live FAIL** | `77241` |
| **History retained** | `978` |
| **New PASS** | `287` |
| **History dropped** | `220` |
| **Previous public** | `1198` |
| **Published profiles (deduped)** | `1265` |
| **Share links (exportable)** | `1128` |
| **YAML proxies (exportable)** | `1128` |
| **Protocol mix** | `{"shadowsocks": 272, "vless": 639, "vmess": 83, "hysteria2": 108, "trojan": 26}` |
| **Country mix** | `{"ZA": 3, "US": 221, "SG": 35, "DE": 60, "CA": 218, "GB": 57, "KR": 27, "CZ": 2, "NL": 151, "TW": 8, "FR": 32, "ID": 1, "CH": 6, "ES": 7, "JP": 43, "SE": 18, "DK": 2, "IN": 13, "CL": 3, "PL": 22, "AT": 5, "UA": 1, "TR": 4, "FI": 13, "RU": 25, "SI": 1, "TH": 2, "IT": 20, "AL": 1, "RO": 4, "LT": 8, "IL": 6, "EE": 6, "AM": 1, "MY": 2, "HK": 31, "CN": 1, "BR": 1, "NO": 2, "DZ": 26, "SC": 3, "KZ": 5, "AE": 3, "AU": 2, "GT": 1, "CY": 1, "IR": 2, "VN": 2, "MD": 1, "LV": 10, "BG": 8, "GR": 1, "SA": 1, "CR": 1}` |
| **Line type mix** | `{"proxy": 383, "home": 65, "dc": 668, "mobile": 14}` |

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
