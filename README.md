# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-25 12:01:40](https://img.shields.io/badge/updated-2026--08--25_12%3A01%3A40-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9274.8s](https://img.shields.io/badge/elapsed-9274.8s-lightgrey)
![profiles: 4507](https://img.shields.io/badge/profiles-4507-blue)
![live_hits: 4507](https://img.shields.io/badge/live__hits-4507-brightgreen)
![live_fail: 66560](https://img.shields.io/badge/live__fail-66560-orange)
![kept: 1282](https://img.shields.io/badge/kept-1282-blue)
![new: 3225](https://img.shields.io/badge/new-3225-success)
![dropped: 194](https://img.shields.io/badge/dropped-194-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-25 12:01:40 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9274.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `428310` |
| **Live PASS (pool hits)** | `4507` |
| **Live FAIL** | `66560` |
| **History retained** | `1282` |
| **New PASS** | `3225` |
| **History dropped** | `194` |
| **Previous public** | `1476` |
| **Published profiles (deduped)** | `4507` |
| **Share links (exportable)** | `2822` |
| **YAML proxies (exportable)** | `2822` |
| **Protocol mix** | `{"vless": 2136, "trojan": 82, "shadowsocks": 347, "hysteria2": 193, "vmess": 64}` |
| **Country mix** | `{"US": 356, "AU": 9, "GB": 145, "DE": 172, "NL": 338, "JP": 49, "PL": 42, "CA": 1013, "RU": 90, "SG": 87, "FI": 51, "SE": 18, "CH": 12, "TW": 10, "FR": 40, "IN": 13, "LT": 12, "ES": 8, "ZA": 3, "HK": 80, "IE": 8, "TH": 8, "CN": 6, "KR": 23, "IT": 23, "AT": 3, "EE": 14, "LV": 16, "KZ": 19, "BE": 1, "TR": 11, "NO": 10, "AL": 4, "SC": 19, "DK": 2, "VN": 1, "CO": 4, "IR": 2, "MD": 1, "MY": 2, "BZ": 9, "CY": 3, "BR": 20, "PT": 1, "CZ": 4, "PH": 2, "RO": 4, "CL": 1, "UA": 9, "HU": 3, "BG": 10, "AE": 3, "PE": 1, "CW": 5, "GE": 1, "SK": 1, "ME": 1, "AM": 1, "ZZ": 1, "DZ": 7, "CR": 8, "VI": 2, "NZ": 1, "BY": 2, "AF": 1, "VG": 1}` |
| **Line type mix** | `{"dc": 1874, "proxy": 667, "home": 273, "mobile": 12, "unknown": 1}` |

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
