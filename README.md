# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-08 23:43:07](https://img.shields.io/badge/updated-2026--08--08_23%3A43%3A07-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10092.5s](https://img.shields.io/badge/elapsed-10092.5s-lightgrey)
![profiles: 1812](https://img.shields.io/badge/profiles-1812-blue)
![live_hits: 1812](https://img.shields.io/badge/live__hits-1812-brightgreen)
![live_fail: 91992](https://img.shields.io/badge/live__fail-91992-orange)
![kept: 976](https://img.shields.io/badge/kept-976-blue)
![new: 836](https://img.shields.io/badge/new-836-success)
![dropped: 681](https://img.shields.io/badge/dropped-681-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-08 23:43:07 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10092.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `446788` |
| **Live PASS (pool hits)** | `1812` |
| **Live FAIL** | `91992` |
| **History retained** | `976` |
| **New PASS** | `836` |
| **History dropped** | `681` |
| **Previous public** | `1657` |
| **Published profiles (deduped)** | `1812` |
| **Share links (exportable)** | `1226` |
| **YAML proxies (exportable)** | `1226` |
| **Protocol mix** | `{"vmess": 65, "vless": 756, "shadowsocks": 197, "hysteria2": 106, "trojan": 102}` |
| **Country mix** | `{"US": 140, "AU": 4, "FR": 62, "NL": 212, "DE": 95, "GB": 41, "ES": 8, "JP": 46, "IT": 5, "SG": 30, "SE": 18, "HK": 37, "KR": 42, "TW": 8, "RO": 5, "FI": 28, "ZA": 2, "BR": 3, "TH": 3, "BG": 2, "CA": 239, "IE": 4, "PL": 13, "KZ": 6, "PT": 1, "EE": 15, "RU": 74, "AE": 2, "CH": 4, "CZ": 2, "LT": 10, "TR": 5, "CO": 6, "MD": 1, "BE": 2, "PH": 10, "LV": 14, "CN": 3, "IN": 5, "SA": 3, "AZ": 1, "SC": 2, "HU": 2, "AM": 1, "VN": 1, "IR": 2, "GR": 1, "AF": 1, "DK": 2, "UA": 1, "CR": 2, "CY": 1, "KH": 1}` |
| **Line type mix** | `{"dc": 667, "proxy": 457, "home": 100, "mobile": 4}` |

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
