# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-29 09:22:16](https://img.shields.io/badge/updated-2026--10--29_09%3A22%3A16-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11051.0s](https://img.shields.io/badge/elapsed-11051.0s-lightgrey)
![profiles: 1501](https://img.shields.io/badge/profiles-1501-blue)
![live_hits: 1501](https://img.shields.io/badge/live__hits-1501-brightgreen)
![live_fail: 86223](https://img.shields.io/badge/live__fail-86223-orange)
![kept: 832](https://img.shields.io/badge/kept-832-blue)
![new: 669](https://img.shields.io/badge/new-669-success)
![dropped: 293](https://img.shields.io/badge/dropped-293-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-29 09:22:16 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11051.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `423192` |
| **Live PASS (pool hits)** | `1501` |
| **Live FAIL** | `86223` |
| **History retained** | `832` |
| **New PASS** | `669` |
| **History dropped** | `293` |
| **Previous public** | `1125` |
| **Published profiles (deduped)** | `1501` |
| **Share links (exportable)** | `1308` |
| **YAML proxies (exportable)** | `1308` |
| **Protocol mix** | `{"shadowsocks": 277, "vless": 732, "hysteria2": 116, "trojan": 117, "vmess": 66}` |
| **Country mix** | `{"IT": 16, "RU": 31, "NL": 189, "US": 209, "GB": 39, "DE": 85, "ZA": 4, "AL": 2, "RO": 2, "CA": 270, "JP": 34, "BG": 16, "SE": 14, "FR": 30, "IN": 11, "KR": 24, "IL": 12, "AU": 8, "ES": 15, "MX": 7, "HU": 1, "AT": 3, "HK": 48, "LV": 6, "CH": 48, "FI": 25, "TR": 4, "SG": 64, "PL": 14, "TH": 4, "IR": 2, "KZ": 7, "AE": 3, "BR": 2, "LT": 11, "ID": 2, "PH": 1, "AM": 1, "UA": 8, "BY": 13, "NO": 1, "SC": 2, "EE": 4, "LU": 1, "GR": 1, "VN": 2, "MY": 3, "CL": 1, "SA": 1, "CW": 2, "BZ": 3, "VG": 2, "DK": 1}` |
| **Line type mix** | `{"dc": 769, "proxy": 347, "home": 105, "mobile": 88}` |

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
