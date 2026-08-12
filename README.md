# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-13 05:57:40](https://img.shields.io/badge/updated-2026--08--13_05%3A57%3A40-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10197.3s](https://img.shields.io/badge/elapsed-10197.3s-lightgrey)
![profiles: 1432](https://img.shields.io/badge/profiles-1432-blue)
![live_hits: 1432](https://img.shields.io/badge/live__hits-1432-brightgreen)
![live_fail: 92994](https://img.shields.io/badge/live__fail-92994-orange)
![kept: 851](https://img.shields.io/badge/kept-851-blue)
![new: 581](https://img.shields.io/badge/new-581-success)
![dropped: 320](https://img.shields.io/badge/dropped-320-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-13 05:57:40 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10197.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `446147` |
| **Live PASS (pool hits)** | `1432` |
| **Live FAIL** | `92994` |
| **History retained** | `851` |
| **New PASS** | `581` |
| **History dropped** | `320` |
| **Previous public** | `1171` |
| **Published profiles (deduped)** | `1432` |
| **Share links (exportable)** | `1096` |
| **YAML proxies (exportable)** | `1096` |
| **Protocol mix** | `{"vless": 662, "shadowsocks": 193, "vmess": 89, "hysteria2": 85, "trojan": 67}` |
| **Country mix** | `{"US": 166, "CA": 155, "GB": 53, "AU": 5, "NL": 183, "DE": 77, "TH": 3, "FR": 40, "HK": 47, "KR": 42, "RO": 8, "FI": 29, "PL": 25, "TR": 7, "JP": 41, "ZA": 3, "NO": 7, "SG": 32, "ES": 5, "TW": 8, "IT": 9, "BG": 2, "IE": 2, "KZ": 8, "PT": 1, "RU": 78, "EE": 10, "CH": 5, "AE": 2, "SE": 7, "MD": 1, "SA": 2, "IN": 5, "LT": 2, "AZ": 1, "IR": 1, "CZ": 1, "CO": 4, "BY": 1, "AT": 2, "AM": 1, "CN": 6, "AL": 2, "UA": 1, "LV": 2, "HU": 1, "AF": 1, "CR": 1, "CY": 1, "KH": 1}` |
| **Line type mix** | `{"dc": 569, "proxy": 432, "home": 86, "mobile": 10}` |

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
