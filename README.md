# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-19 17:27:06](https://img.shields.io/badge/updated-2026--11--19_17%3A27%3A06-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11397.2s](https://img.shields.io/badge/elapsed-11397.2s-lightgrey)
![profiles: 1264](https://img.shields.io/badge/profiles-1264-blue)
![live_hits: 1264](https://img.shields.io/badge/live__hits-1264-brightgreen)
![live_fail: 88356](https://img.shields.io/badge/live__fail-88356-orange)
![kept: 1046](https://img.shields.io/badge/kept-1046-blue)
![new: 218](https://img.shields.io/badge/new-218-success)
![dropped: 618](https://img.shields.io/badge/dropped-618-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-19 17:27:06 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11397.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `405341` |
| **Live PASS (pool hits)** | `1264` |
| **Live FAIL** | `88356` |
| **History retained** | `1046` |
| **New PASS** | `218` |
| **History dropped** | `618` |
| **Previous public** | `1664` |
| **Published profiles (deduped)** | `1264` |
| **Share links (exportable)** | `1156` |
| **YAML proxies (exportable)** | `1156` |
| **Protocol mix** | `{"shadowsocks": 355, "hysteria2": 62, "vless": 522, "vmess": 121, "trojan": 96}` |
| **Country mix** | `{"US": 311, "DE": 90, "NL": 123, "AT": 2, "HK": 17, "GB": 52, "JP": 50, "CA": 121, "IE": 2, "ZA": 3, "FI": 15, "IT": 20, "ES": 18, "PL": 34, "LT": 9, "BG": 8, "KR": 11, "MX": 1, "RU": 16, "FR": 35, "SG": 55, "CH": 15, "BR": 15, "CL": 1, "AU": 5, "TW": 6, "SE": 17, "IN": 3, "TR": 36, "EE": 14, "BY": 7, "NE": 3, "LV": 8, "IR": 5, "LU": 2, "CZ": 2, "GR": 1, "AE": 2, "VN": 2, "KZ": 3, "NO": 1, "RO": 2, "NG": 2, "BH": 1, "SK": 3, "AL": 1, "MY": 1, "TH": 1, "IL": 1, "DK": 1, "LY": 1, "CR": 1, "SA": 1}` |
| **Line type mix** | `{"proxy": 425, "dc": 504, "home": 138, "mobile": 90}` |

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
