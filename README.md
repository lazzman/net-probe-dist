# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-13 18:22:38](https://img.shields.io/badge/updated-2026--08--13_18%3A22%3A38-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10065.5s](https://img.shields.io/badge/elapsed-10065.5s-lightgrey)
![profiles: 2861](https://img.shields.io/badge/profiles-2861-blue)
![live_hits: 2861](https://img.shields.io/badge/live__hits-2861-brightgreen)
![live_fail: 91405](https://img.shields.io/badge/live__fail-91405-orange)
![kept: 1375](https://img.shields.io/badge/kept-1375-blue)
![new: 1486](https://img.shields.io/badge/new-1486-success)
![dropped: 725](https://img.shields.io/badge/dropped-725-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-13 18:22:38 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10065.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `445667` |
| **Live PASS (pool hits)** | `2861` |
| **Live FAIL** | `91405` |
| **History retained** | `1375` |
| **New PASS** | `1486` |
| **History dropped** | `725` |
| **Previous public** | `2100` |
| **Published profiles (deduped)** | `2861` |
| **Share links (exportable)** | `1728` |
| **YAML proxies (exportable)** | `1728` |
| **Protocol mix** | `{"vless": 1141, "hysteria2": 87, "shadowsocks": 204, "vmess": 76, "trojan": 220}` |
| **Country mix** | `{"NL": 197, "GB": 67, "US": 205, "AU": 8, "CA": 487, "TH": 4, "ZZ": 1, "JP": 115, "IN": 10, "FR": 47, "FI": 36, "PL": 29, "TR": 10, "DE": 109, "SG": 40, "TW": 10, "NO": 1, "RO": 9, "ES": 5, "ZA": 2, "IT": 12, "KR": 77, "BG": 5, "HK": 49, "IE": 8, "KZ": 10, "EE": 10, "RU": 115, "SE": 12, "CH": 2, "AT": 4, "MD": 1, "PH": 1, "LT": 5, "BR": 1, "AZ": 1, "IR": 2, "CO": 3, "CN": 2, "AL": 3, "PT": 1, "SC": 3, "CZ": 2, "AE": 1, "UA": 1, "BZ": 1, "LV": 3, "HU": 1, "BY": 1, "SA": 1, "AF": 1, "AM": 1, "CR": 2, "CY": 1, "KH": 1}` |
| **Line type mix** | `{"proxy": 513, "dc": 1104, "home": 113, "unknown": 1, "mobile": 5}` |

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
