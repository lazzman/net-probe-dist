# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-20 17:27:48](https://img.shields.io/badge/updated-2026--08--20_17%3A27%3A48-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 8954.6s](https://img.shields.io/badge/elapsed-8954.6s-lightgrey)
![profiles: 4357](https://img.shields.io/badge/profiles-4357-blue)
![live_hits: 4357](https://img.shields.io/badge/live__hits-4357-brightgreen)
![live_fail: 64791](https://img.shields.io/badge/live__fail-64791-orange)
![kept: 2109](https://img.shields.io/badge/kept-2109-blue)
![new: 2248](https://img.shields.io/badge/new-2248-success)
![dropped: 700](https://img.shields.io/badge/dropped-700-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-20 17:27:48 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `8954.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `432987` |
| **Live PASS (pool hits)** | `4357` |
| **Live FAIL** | `64791` |
| **History retained** | `2109` |
| **New PASS** | `2248` |
| **History dropped** | `700` |
| **Previous public** | `2809` |
| **Published profiles (deduped)** | `4357` |
| **Share links (exportable)** | `2478` |
| **YAML proxies (exportable)** | `2478` |
| **Protocol mix** | `{"vmess": 59, "vless": 1451, "hysteria2": 159, "shadowsocks": 259, "trojan": 550}` |
| **Country mix** | `{"US": 302, "NL": 310, "SG": 151, "JP": 244, "CA": 614, "AU": 21, "FR": 61, "SE": 32, "DE": 158, "DZ": 5, "GB": 48, "FI": 46, "BR": 10, "ZA": 4, "PL": 41, "IN": 14, "RO": 5, "ES": 9, "CN": 9, "RU": 44, "KR": 33, "IE": 20, "ZZ": 76, "HK": 67, "AT": 2, "EE": 22, "IT": 8, "TW": 9, "BE": 2, "TR": 10, "LV": 11, "CH": 8, "KZ": 13, "AE": 1, "KG": 1, "VN": 2, "BY": 1, "NO": 8, "CZ": 2, "SK": 1, "MD": 2, "AM": 1, "UA": 6, "SC": 12, "LT": 7, "TH": 5, "AL": 3, "IL": 2, "CO": 2, "PT": 1, "BG": 6, "DK": 2, "BZ": 3, "HU": 1, "PH": 1, "IR": 2, "SA": 1, "CR": 1, "AF": 1, "CY": 1, "MY": 1}` |
| **Line type mix** | `{"home": 209, "dc": 1586, "proxy": 600, "mobile": 15, "unknown": 76}` |

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
