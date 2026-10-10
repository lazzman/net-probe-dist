# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-10 15:23:19](https://img.shields.io/badge/updated-2026--10--10_15%3A23%3A19-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9977.2s](https://img.shields.io/badge/elapsed-9977.2s-lightgrey)
![profiles: 2617](https://img.shields.io/badge/profiles-2617-blue)
![live_hits: 2617](https://img.shields.io/badge/live__hits-2617-brightgreen)
![live_fail: 75423](https://img.shields.io/badge/live__fail-75423-orange)
![kept: 988](https://img.shields.io/badge/kept-988-blue)
![new: 1629](https://img.shields.io/badge/new-1629-success)
![dropped: 380](https://img.shields.io/badge/dropped-380-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-10 15:23:19 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9977.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `410651` |
| **Live PASS (pool hits)** | `2617` |
| **Live FAIL** | `75423` |
| **History retained** | `988` |
| **New PASS** | `1629` |
| **History dropped** | `380` |
| **Previous public** | `1368` |
| **Published profiles (deduped)** | `2617` |
| **Share links (exportable)** | `1701` |
| **YAML proxies (exportable)** | `1701` |
| **Protocol mix** | `{"vless": 1055, "shadowsocks": 284, "hysteria2": 129, "trojan": 161, "vmess": 72}` |
| **Country mix** | `{"US": 217, "CA": 594, "NL": 180, "RU": 37, "GB": 42, "SG": 60, "DE": 106, "FR": 27, "ZA": 6, "IN": 13, "CH": 9, "RO": 5, "FI": 16, "JP": 63, "KR": 53, "IE": 5, "PL": 20, "ES": 17, "SC": 7, "HK": 51, "SE": 8, "TR": 6, "EE": 9, "IT": 21, "KZ": 6, "MY": 11, "LV": 25, "AM": 1, "ID": 3, "TW": 4, "TH": 3, "NO": 1, "IL": 2, "AU": 7, "AE": 4, "NZ": 1, "PT": 1, "CY": 3, "BZ": 5, "IR": 2, "BG": 12, "CW": 3, "GR": 1, "AL": 3, "VN": 1, "AT": 3, "CZ": 2, "LT": 11, "UA": 2, "ME": 1, "BE": 1, "VG": 1, "SA": 1, "MX": 1, "CR": 2, "CN": 15}` |
| **Line type mix** | `{"dc": 1140, "proxy": 460, "home": 104, "mobile": 7}` |

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
