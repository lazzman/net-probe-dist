# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-22 14:32:26](https://img.shields.io/badge/updated-2026--09--22_14%3A32%3A26-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10050.6s](https://img.shields.io/badge/elapsed-10050.6s-lightgrey)
![profiles: 4340](https://img.shields.io/badge/profiles-4340-blue)
![live_hits: 4340](https://img.shields.io/badge/live__hits-4340-brightgreen)
![live_fail: 73944](https://img.shields.io/badge/live__fail-73944-orange)
![kept: 1324](https://img.shields.io/badge/kept-1324-blue)
![new: 3016](https://img.shields.io/badge/new-3016-success)
![dropped: 386](https://img.shields.io/badge/dropped-386-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-22 14:32:26 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10050.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `428168` |
| **Live PASS (pool hits)** | `4340` |
| **Live FAIL** | `73944` |
| **History retained** | `1324` |
| **New PASS** | `3016` |
| **History dropped** | `386` |
| **Previous public** | `1710` |
| **Published profiles (deduped)** | `4340` |
| **Share links (exportable)** | `2417` |
| **YAML proxies (exportable)** | `2417` |
| **Protocol mix** | `{"hysteria2": 108, "vless": 1882, "vmess": 78, "shadowsocks": 256, "trojan": 93}` |
| **Country mix** | `{"ES": 15, "KR": 38, "CA": 1114, "GB": 75, "US": 338, "DK": 4, "RU": 26, "SE": 25, "DE": 91, "NL": 178, "SG": 47, "TW": 10, "ID": 1, "ZA": 4, "FR": 39, "RO": 5, "CH": 7, "JP": 55, "MX": 2, "IN": 15, "FI": 30, "AT": 4, "PL": 27, "TR": 5, "TH": 6, "CL": 3, "BG": 10, "IT": 25, "HK": 54, "AL": 1, "CY": 11, "KZ": 14, "IR": 3, "BZ": 14, "SC": 10, "IE": 3, "LU": 1, "BE": 2, "HU": 3, "EE": 9, "AM": 2, "MY": 8, "BR": 4, "CN": 1, "NO": 4, "DZ": 25, "AU": 6, "CZ": 2, "AE": 3, "LT": 8, "NZ": 1, "PT": 2, "CW": 4, "UA": 3, "GT": 1, "ME": 1, "LV": 11, "RS": 1, "MD": 2, "BY": 1, "IS": 1, "GR": 1, "SK": 3, "UZ": 2, "ZZ": 1, "IQ": 1, "SA": 1, "VG": 1, "CR": 2}` |
| **Line type mix** | `{"dc": 1789, "proxy": 525, "home": 96, "mobile": 16, "unknown": 1}` |

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
