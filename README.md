# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-09 23:44:22](https://img.shields.io/badge/updated-2026--08--09_23%3A44%3A22-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10088.5s](https://img.shields.io/badge/elapsed-10088.5s-lightgrey)
![profiles: 1663](https://img.shields.io/badge/profiles-1663-blue)
![live_hits: 1663](https://img.shields.io/badge/live__hits-1663-brightgreen)
![live_fail: 92375](https://img.shields.io/badge/live__fail-92375-orange)
![kept: 999](https://img.shields.io/badge/kept-999-blue)
![new: 664](https://img.shields.io/badge/new-664-success)
![dropped: 576](https://img.shields.io/badge/dropped-576-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-09 23:44:22 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10088.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `448670` |
| **Live PASS (pool hits)** | `1663` |
| **Live FAIL** | `92375` |
| **History retained** | `999` |
| **New PASS** | `664` |
| **History dropped** | `576` |
| **Previous public** | `1575` |
| **Published profiles (deduped)** | `1663` |
| **Share links (exportable)** | `1251` |
| **YAML proxies (exportable)** | `1251` |
| **Protocol mix** | `{"vless": 792, "shadowsocks": 184, "vmess": 77, "hysteria2": 105, "trojan": 93}` |
| **Country mix** | `{"US": 150, "NL": 215, "GB": 37, "ZZ": 1, "ES": 8, "AU": 3, "FR": 50, "TH": 4, "DE": 92, "IT": 5, "SE": 14, "JP": 51, "KR": 35, "RO": 6, "HK": 36, "FI": 23, "TW": 7, "NO": 1, "ZA": 2, "CA": 215, "PL": 14, "TR": 5, "BG": 4, "IE": 4, "SA": 3, "RU": 151, "PT": 1, "EE": 8, "BE": 5, "CH": 2, "SG": 33, "CO": 4, "KZ": 5, "SC": 6, "LT": 4, "AE": 3, "PH": 16, "IN": 6, "AZ": 1, "CZ": 1, "AT": 2, "MD": 1, "MY": 1, "HU": 2, "AL": 2, "BR": 1, "LV": 5, "AF": 1, "CN": 1, "AM": 1, "UA": 1, "KH": 1, "GR": 1, "DK": 1, "CR": 1, "CY": 1}` |
| **Line type mix** | `{"dc": 653, "home": 130, "proxy": 462, "unknown": 1, "mobile": 8}` |

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
