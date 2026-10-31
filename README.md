# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-31 15:24:12](https://img.shields.io/badge/updated-2026--10--31_15%3A24%3A12-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10938.1s](https://img.shields.io/badge/elapsed-10938.1s-lightgrey)
![profiles: 1323](https://img.shields.io/badge/profiles-1323-blue)
![live_hits: 1323](https://img.shields.io/badge/live__hits-1323-brightgreen)
![live_fail: 85947](https://img.shields.io/badge/live__fail-85947-orange)
![kept: 984](https://img.shields.io/badge/kept-984-blue)
![new: 339](https://img.shields.io/badge/new-339-success)
![dropped: 347](https://img.shields.io/badge/dropped-347-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-31 15:24:12 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10938.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `403013` |
| **Live PASS (pool hits)** | `1323` |
| **Live FAIL** | `85947` |
| **History retained** | `984` |
| **New PASS** | `339` |
| **History dropped** | `347` |
| **Previous public** | `1331` |
| **Published profiles (deduped)** | `1323` |
| **Share links (exportable)** | `1163` |
| **YAML proxies (exportable)** | `1163` |
| **Protocol mix** | `{"shadowsocks": 258, "trojan": 168, "hysteria2": 135, "vless": 535, "vmess": 67}` |
| **Country mix** | `{"IT": 17, "NL": 179, "US": 198, "DE": 67, "CA": 279, "GB": 24, "PL": 18, "FI": 13, "NO": 1, "RO": 4, "ZA": 2, "AL": 2, "JP": 27, "SG": 41, "BG": 11, "IN": 8, "CH": 53, "MX": 3, "BR": 3, "CL": 2, "IL": 5, "AU": 3, "ES": 14, "SE": 7, "TH": 2, "HU": 1, "CR": 2, "AT": 2, "HK": 29, "LV": 8, "RU": 29, "BY": 8, "MD": 4, "KR": 23, "AE": 3, "FR": 34, "EE": 5, "UA": 3, "AM": 1, "TW": 3, "SC": 3, "LT": 6, "ID": 2, "TR": 3, "KZ": 2, "IR": 2, "CY": 1, "DK": 1, "CZ": 1, "VN": 1, "MY": 2, "CN": 1, "VG": 1, "SA": 1}` |
| **Line type mix** | `{"dc": 653, "proxy": 297, "mobile": 128, "home": 87}` |

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
