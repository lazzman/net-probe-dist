# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-28 04:41:48](https://img.shields.io/badge/updated-2026--10--28_04%3A41%3A48-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11059.0s](https://img.shields.io/badge/elapsed-11059.0s-lightgrey)
![profiles: 1263](https://img.shields.io/badge/profiles-1263-blue)
![live_hits: 1263](https://img.shields.io/badge/live__hits-1263-brightgreen)
![live_fail: 86056](https://img.shields.io/badge/live__fail-86056-orange)
![kept: 979](https://img.shields.io/badge/kept-979-blue)
![new: 284](https://img.shields.io/badge/new-284-success)
![dropped: 245](https://img.shields.io/badge/dropped-245-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-28 04:41:48 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11059.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `413879` |
| **Live PASS (pool hits)** | `1263` |
| **Live FAIL** | `86056` |
| **History retained** | `979` |
| **New PASS** | `284` |
| **History dropped** | `245` |
| **Previous public** | `1224` |
| **Published profiles (deduped)** | `1263` |
| **Share links (exportable)** | `1111` |
| **YAML proxies (exportable)** | `1111` |
| **Protocol mix** | `{"shadowsocks": 252, "hysteria2": 131, "trojan": 112, "vless": 557, "vmess": 59}` |
| **Country mix** | `{"DE": 62, "NL": 174, "IT": 12, "GB": 25, "US": 194, "PL": 8, "TR": 15, "NO": 1, "ZA": 4, "RO": 3, "IR": 3, "SG": 44, "JP": 29, "RU": 26, "IN": 8, "CA": 239, "ES": 18, "HK": 33, "AT": 2, "LV": 3, "CR": 1, "FR": 30, "MX": 3, "FI": 21, "KZ": 5, "AE": 3, "MD": 1, "VN": 1, "SI": 4, "SA": 1, "IL": 6, "BG": 8, "SC": 4, "TH": 2, "KR": 18, "TW": 1, "CH": 46, "UA": 2, "SE": 11, "GR": 1, "CZ": 1, "MY": 4, "BY": 9, "EE": 3, "AL": 1, "BR": 1, "CL": 1, "AU": 5, "MK": 1, "LU": 1, "DK": 1, "IE": 1, "ID": 1, "AZ": 1, "AM": 1, "CN": 1, "LT": 8}` |
| **Line type mix** | `{"mobile": 95, "proxy": 282, "dc": 650, "home": 86}` |

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
