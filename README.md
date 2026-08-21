# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-21 11:59:00](https://img.shields.io/badge/updated-2026--08--21_11%3A59%3A00-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9096.9s](https://img.shields.io/badge/elapsed-9096.9s-lightgrey)
![profiles: 5152](https://img.shields.io/badge/profiles-5152-blue)
![live_hits: 5152](https://img.shields.io/badge/live__hits-5152-brightgreen)
![live_fail: 64468](https://img.shields.io/badge/live__fail-64468-orange)
![kept: 1566](https://img.shields.io/badge/kept-1566-blue)
![new: 3586](https://img.shields.io/badge/new-3586-success)
![dropped: 185](https://img.shields.io/badge/dropped-185-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-21 11:59:00 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9096.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `433664` |
| **Live PASS (pool hits)** | `5152` |
| **Live FAIL** | `64468` |
| **History retained** | `1566` |
| **New PASS** | `3586` |
| **History dropped** | `185` |
| **Previous public** | `1751` |
| **Published profiles (deduped)** | `5152` |
| **Share links (exportable)** | `2976` |
| **YAML proxies (exportable)** | `2976` |
| **Protocol mix** | `{"vless": 1956, "shadowsocks": 385, "vmess": 59, "hysteria2": 167, "trojan": 409}` |
| **Country mix** | `{"US": 402, "AU": 24, "CA": 856, "HK": 89, "DE": 192, "FR": 73, "SE": 30, "SG": 70, "JP": 258, "FI": 47, "NL": 322, "GB": 117, "BR": 10, "ZA": 4, "PL": 48, "NO": 5, "IN": 12, "RO": 5, "RU": 54, "ES": 11, "CN": 42, "IT": 23, "IE": 18, "AT": 3, "LV": 19, "EE": 19, "TW": 10, "KZ": 18, "TR": 11, "SK": 3, "SC": 22, "CH": 10, "LT": 17, "VN": 2, "KG": 1, "MD": 2, "DK": 3, "CY": 4, "BZ": 9, "KR": 33, "TH": 7, "BE": 6, "IR": 3, "UA": 9, "PT": 2, "BG": 15, "SI": 1, "MY": 3, "CZ": 3, "SA": 1, "PH": 2, "PE": 2, "AL": 3, "AE": 3, "NZ": 2, "CW": 6, "HU": 2, "CO": 1, "ME": 1, "AM": 1, "DZ": 4, "CR": 2, "AF": 1, "ZZ": 1, "VG": 1, "ID": 1}` |
| **Line type mix** | `{"dc": 1915, "proxy": 768, "home": 250, "mobile": 47, "unknown": 1}` |

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
