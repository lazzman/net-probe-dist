# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-22 05:11:58](https://img.shields.io/badge/updated-2026--08--22_05%3A11%3A58-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 8991.7s](https://img.shields.io/badge/elapsed-8991.7s-lightgrey)
![profiles: 2772](https://img.shields.io/badge/profiles-2772-blue)
![live_hits: 2772](https://img.shields.io/badge/live__hits-2772-brightgreen)
![live_fail: 66286](https://img.shields.io/badge/live__fail-66286-orange)
![kept: 1558](https://img.shields.io/badge/kept-1558-blue)
![new: 1214](https://img.shields.io/badge/new-1214-success)
![dropped: 299](https://img.shields.io/badge/dropped-299-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-22 05:11:58 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `8991.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `438219` |
| **Live PASS (pool hits)** | `2772` |
| **Live FAIL** | `66286` |
| **History retained** | `1558` |
| **New PASS** | `1214` |
| **History dropped** | `299` |
| **Previous public** | `1857` |
| **Published profiles (deduped)** | `2772` |
| **Share links (exportable)** | `1762` |
| **YAML proxies (exportable)** | `1762` |
| **Protocol mix** | `{"shadowsocks": 283, "vless": 889, "vmess": 66, "hysteria2": 161, "trojan": 363}` |
| **Country mix** | `{"US": 236, "AU": 19, "CA": 201, "DE": 153, "FR": 57, "PL": 41, "SG": 80, "FI": 35, "JP": 246, "NL": 289, "SE": 12, "TW": 18, "IN": 13, "HK": 65, "ES": 8, "KR": 17, "CN": 7, "IE": 18, "LV": 15, "AT": 2, "KZ": 12, "IT": 12, "EE": 14, "RU": 36, "GB": 40, "BG": 9, "CH": 11, "LT": 11, "VN": 2, "CZ": 3, "CO": 2, "BR": 15, "SC": 6, "MD": 2, "DK": 3, "PH": 2, "TR": 7, "SK": 1, "TH": 5, "ZA": 3, "BE": 2, "IL": 1, "UA": 4, "RO": 4, "NO": 5, "PE": 2, "AL": 3, "AE": 1, "HU": 1, "SA": 1, "BZ": 1, "CR": 1, "BY": 2, "OM": 1, "AF": 1, "ZZ": 1, "MY": 2, "ID": 1, "CY": 1}` |
| **Line type mix** | `{"proxy": 553, "dc": 972, "home": 225, "mobile": 12, "unknown": 1}` |

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
