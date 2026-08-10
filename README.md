# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-11 00:04:22](https://img.shields.io/badge/updated-2026--08--11_00%3A04%3A22-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10286.9s](https://img.shields.io/badge/elapsed-10286.9s-lightgrey)
![profiles: 1649](https://img.shields.io/badge/profiles-1649-blue)
![live_hits: 1649](https://img.shields.io/badge/live__hits-1649-brightgreen)
![live_fail: 93521](https://img.shields.io/badge/live__fail-93521-orange)
![kept: 1010](https://img.shields.io/badge/kept-1010-blue)
![new: 639](https://img.shields.io/badge/new-639-success)
![dropped: 674](https://img.shields.io/badge/dropped-674-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-11 00:04:22 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10286.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `451748` |
| **Live PASS (pool hits)** | `1649` |
| **Live FAIL** | `93521` |
| **History retained** | `1010` |
| **New PASS** | `639` |
| **History dropped** | `674` |
| **Previous public** | `1684` |
| **Published profiles (deduped)** | `1649` |
| **Share links (exportable)** | `1261` |
| **YAML proxies (exportable)** | `1261` |
| **Protocol mix** | `{"vless": 823, "vmess": 79, "shadowsocks": 197, "hysteria2": 87, "trojan": 75}` |
| **Country mix** | `{"US": 159, "NL": 220, "DE": 83, "AU": 5, "TH": 2, "CA": 229, "SE": 20, "HK": 38, "RU": 90, "RO": 6, "GB": 41, "FR": 58, "FI": 20, "ES": 7, "ZA": 2, "JP": 48, "TR": 11, "BG": 3, "IT": 5, "IE": 3, "PL": 16, "KR": 49, "SA": 3, "EE": 19, "BE": 7, "CH": 3, "CZ": 1, "SG": 24, "KZ": 6, "ZZ": 1, "CO": 3, "TW": 8, "MD": 1, "LT": 2, "LV": 11, "PH": 15, "MY": 4, "IN": 7, "AT": 4, "SC": 4, "NO": 1, "PT": 1, "AZ": 1, "AE": 2, "AM": 1, "CN": 5, "AL": 2, "IR": 1, "BR": 2, "HU": 2, "AF": 1, "UA": 1, "KH": 1, "ID": 1, "CR": 2, "CY": 1}` |
| **Line type mix** | `{"dc": 656, "home": 116, "proxy": 485, "mobile": 5, "unknown": 1}` |

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
