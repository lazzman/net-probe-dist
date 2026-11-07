# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-07 09:58:02](https://img.shields.io/badge/updated-2026--11--07_09%3A58%3A02-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11198.7s](https://img.shields.io/badge/elapsed-11198.7s-lightgrey)
![profiles: 1597](https://img.shields.io/badge/profiles-1597-blue)
![live_hits: 1597](https://img.shields.io/badge/live__hits-1597-brightgreen)
![live_fail: 86041](https://img.shields.io/badge/live__fail-86041-orange)
![kept: 868](https://img.shields.io/badge/kept-868-blue)
![new: 729](https://img.shields.io/badge/new-729-success)
![dropped: 98](https://img.shields.io/badge/dropped-98-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-07 09:58:02 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11198.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `398503` |
| **Live PASS (pool hits)** | `1597` |
| **Live FAIL** | `86041` |
| **History retained** | `868` |
| **New PASS** | `729` |
| **History dropped** | `98` |
| **Previous public** | `966` |
| **Published profiles (deduped)** | `1597` |
| **Share links (exportable)** | `1367` |
| **YAML proxies (exportable)** | `1367` |
| **Protocol mix** | `{"hysteria2": 144, "shadowsocks": 323, "trojan": 111, "vless": 676, "vmess": 113}` |
| **Country mix** | `{"HK": 33, "PL": 31, "CA": 280, "NL": 159, "DE": 71, "US": 301, "ES": 36, "AL": 1, "AT": 5, "NO": 1, "ZA": 2, "RO": 4, "JP": 29, "GB": 47, "MX": 2, "IN": 4, "KR": 25, "IT": 27, "SE": 16, "SG": 72, "FR": 39, "CH": 57, "BR": 3, "CL": 1, "AU": 4, "PH": 1, "UA": 8, "RU": 21, "EE": 6, "BY": 8, "FI": 11, "TR": 7, "TW": 4, "KZ": 2, "SA": 1, "BG": 8, "TH": 4, "IL": 1, "LV": 3, "AE": 3, "GR": 2, "DK": 2, "VN": 2, "MY": 2, "ID": 2, "CN": 1, "LT": 8, "GE": 1, "IE": 1, "BZ": 4, "IR": 1, "VG": 1, "HU": 1, "SC": 1, "CZ": 1, "CW": 1}` |
| **Line type mix** | `{"dc": 704, "proxy": 450, "home": 85, "mobile": 130}` |

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
