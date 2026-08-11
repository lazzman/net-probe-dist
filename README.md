# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-11 12:41:47](https://img.shields.io/badge/updated-2026--08--11_12%3A41%3A47-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10215.4s](https://img.shields.io/badge/elapsed-10215.4s-lightgrey)
![profiles: 3630](https://img.shields.io/badge/profiles-3630-blue)
![live_hits: 3630](https://img.shields.io/badge/live__hits-3630-brightgreen)
![live_fail: 91376](https://img.shields.io/badge/live__fail-91376-orange)
![kept: 982](https://img.shields.io/badge/kept-982-blue)
![new: 2648](https://img.shields.io/badge/new-2648-success)
![dropped: 185](https://img.shields.io/badge/dropped-185-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-11 12:41:47 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10215.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `451826` |
| **Live PASS (pool hits)** | `3630` |
| **Live FAIL** | `91376` |
| **History retained** | `982` |
| **New PASS** | `2648` |
| **History dropped** | `185` |
| **Previous public** | `1167` |
| **Published profiles (deduped)** | `3630` |
| **Share links (exportable)** | `2199` |
| **YAML proxies (exportable)** | `2199` |
| **Protocol mix** | `{"vless": 1718, "shadowsocks": 194, "vmess": 77, "hysteria2": 87, "trojan": 123}` |
| **Country mix** | `{"US": 269, "NL": 228, "AU": 6, "FR": 105, "GB": 129, "TH": 3, "DE": 114, "RU": 110, "HK": 59, "RO": 5, "CA": 723, "TW": 6, "NO": 2, "TR": 12, "FI": 36, "ES": 9, "ZZ": 3, "KR": 55, "IT": 10, "PL": 20, "SG": 43, "IE": 4, "JP": 72, "SC": 11, "KZ": 8, "PT": 1, "EE": 12, "CH": 3, "CZ": 3, "CO": 7, "SE": 14, "MD": 1, "LT": 5, "LV": 10, "PH": 41, "MY": 3, "IN": 8, "AT": 6, "BZ": 7, "CY": 3, "ZA": 2, "UA": 4, "AZ": 1, "BG": 3, "BR": 4, "AE": 3, "ME": 1, "NZ": 2, "AM": 1, "AL": 2, "SA": 2, "IR": 2, "HU": 3, "CW": 4, "AF": 1, "CN": 1, "KH": 1, "GR": 1, "CR": 2}` |
| **Line type mix** | `{"dc": 1378, "proxy": 683, "home": 136, "unknown": 3, "mobile": 6}` |

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
