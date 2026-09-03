# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-03 14:00:54](https://img.shields.io/badge/updated-2026--09--03_14%3A00%3A54-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9699.5s](https://img.shields.io/badge/elapsed-9699.5s-lightgrey)
![profiles: 3916](https://img.shields.io/badge/profiles-3916-blue)
![live_hits: 3916](https://img.shields.io/badge/live__hits-3916-brightgreen)
![live_fail: 71237](https://img.shields.io/badge/live__fail-71237-orange)
![kept: 1252](https://img.shields.io/badge/kept-1252-blue)
![new: 2664](https://img.shields.io/badge/new-2664-success)
![dropped: 133](https://img.shields.io/badge/dropped-133-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-03 14:00:54 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9699.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `425318` |
| **Live PASS (pool hits)** | `3916` |
| **Live FAIL** | `71237` |
| **History retained** | `1252` |
| **New PASS** | `2664` |
| **History dropped** | `133` |
| **Previous public** | `1385` |
| **Published profiles (deduped)** | `3916` |
| **Share links (exportable)** | `2240` |
| **YAML proxies (exportable)** | `2240` |
| **Protocol mix** | `{"vless": 1616, "hysteria2": 195, "shadowsocks": 271, "trojan": 83, "vmess": 75}` |
| **Country mix** | `{"CA": 844, "KR": 34, "US": 332, "SG": 76, "NL": 230, "JP": 63, "PL": 31, "IT": 12, "RU": 57, "FI": 34, "DZ": 19, "GB": 90, "DE": 104, "LV": 9, "SE": 11, "TW": 22, "ID": 1, "ZA": 5, "AL": 4, "FR": 29, "NO": 21, "RO": 3, "IR": 5, "ES": 9, "HK": 42, "TH": 6, "MY": 4, "CN": 5, "AT": 5, "KZ": 12, "EE": 10, "IN": 10, "AE": 2, "BR": 12, "TR": 8, "BZ": 5, "UA": 5, "GR": 3, "UZ": 3, "SK": 1, "LT": 12, "SC": 13, "CH": 4, "SA": 1, "AU": 7, "PH": 3, "CO": 1, "JE": 1, "AR": 2, "CZ": 5, "BG": 7, "MX": 3, "CR": 2, "PT": 1, "CY": 2, "MD": 1, "EG": 1, "AM": 1, "HU": 1, "CW": 2, "BY": 1, "IE": 1}` |
| **Line type mix** | `{"dc": 1581, "proxy": 519, "home": 138, "mobile": 12}` |

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
