# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-04 14:03:19](https://img.shields.io/badge/updated-2026--09--04_14%3A03%3A19-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9710.4s](https://img.shields.io/badge/elapsed-9710.4s-lightgrey)
![profiles: 4496](https://img.shields.io/badge/profiles-4496-blue)
![live_hits: 4498](https://img.shields.io/badge/live__hits-4498-brightgreen)
![live_fail: 70803](https://img.shields.io/badge/live__fail-70803-orange)
![kept: 1224](https://img.shields.io/badge/kept-1224-blue)
![new: 3274](https://img.shields.io/badge/new-3274-success)
![dropped: 102](https://img.shields.io/badge/dropped-102-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-04 14:03:19 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9710.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `427219` |
| **Live PASS (pool hits)** | `4498` |
| **Live FAIL** | `70803` |
| **History retained** | `1224` |
| **New PASS** | `3274` |
| **History dropped** | `102` |
| **Previous public** | `1326` |
| **Published profiles (deduped)** | `4496` |
| **Share links (exportable)** | `2421` |
| **YAML proxies (exportable)** | `2421` |
| **Protocol mix** | `{"hysteria2": 170, "vless": 1819, "shadowsocks": 281, "trojan": 86, "vmess": 65}` |
| **Country mix** | `{"SG": 70, "DE": 104, "US": 313, "FR": 31, "NL": 241, "IT": 16, "LV": 11, "PL": 31, "FI": 33, "AU": 7, "CA": 1024, "GB": 105, "DZ": 22, "IN": 10, "RU": 41, "SE": 17, "TW": 23, "ZA": 5, "NO": 24, "RO": 3, "ES": 12, "IE": 5, "MY": 3, "JP": 68, "CN": 5, "KR": 38, "AT": 4, "SC": 13, "KZ": 10, "EE": 10, "BR": 12, "TR": 13, "IR": 4, "BZ": 4, "AL": 2, "UA": 5, "GR": 2, "HK": 37, "SK": 1, "LT": 11, "CZ": 4, "SA": 1, "UZ": 2, "TH": 3, "ID": 1, "HU": 1, "CH": 2, "JE": 1, "AR": 2, "AE": 3, "PT": 1, "BG": 5, "CO": 1, "BY": 1, "PH": 1, "EG": 1, "AM": 1, "NZ": 1, "CW": 3, "CY": 3, "ME": 1, "CR": 2, "MX": 2}` |
| **Line type mix** | `{"proxy": 534, "dc": 1746, "home": 141, "mobile": 12}` |

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
