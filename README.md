# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-16 03:13:45](https://img.shields.io/badge/updated-2026--09--16_03%3A13%3A45-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9923.5s](https://img.shields.io/badge/elapsed-9923.5s-lightgrey)
![profiles: 1513](https://img.shields.io/badge/profiles-1513-blue)
![live_hits: 1513](https://img.shields.io/badge/live__hits-1513-brightgreen)
![live_fail: 75503](https://img.shields.io/badge/live__fail-75503-orange)
![kept: 1032](https://img.shields.io/badge/kept-1032-blue)
![new: 481](https://img.shields.io/badge/new-481-success)
![dropped: 252](https://img.shields.io/badge/dropped-252-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-16 03:13:45 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9923.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `438139` |
| **Live PASS (pool hits)** | `1513` |
| **Live FAIL** | `75503` |
| **History retained** | `1032` |
| **New PASS** | `481` |
| **History dropped** | `252` |
| **Previous public** | `1284` |
| **Published profiles (deduped)** | `1513` |
| **Share links (exportable)** | `1174` |
| **YAML proxies (exportable)** | `1174` |
| **Protocol mix** | `{"vless": 699, "hysteria2": 146, "trojan": 26, "vmess": 64, "shadowsocks": 239}` |
| **Country mix** | `{"DE": 48, "CA": 306, "JP": 29, "NL": 186, "SG": 30, "US": 197, "IN": 10, "GB": 60, "RU": 29, "CH": 3, "SE": 9, "TW": 18, "ID": 1, "FR": 28, "IE": 1, "NO": 3, "PL": 22, "ES": 5, "RO": 3, "FI": 15, "IT": 8, "KR": 26, "AT": 2, "HR": 1, "TR": 6, "EE": 7, "UZ": 2, "CZ": 4, "TH": 4, "HK": 31, "GR": 2, "GT": 1, "KZ": 7, "SA": 2, "MY": 3, "AM": 1, "LT": 10, "ZZ": 1, "ZA": 3, "DZ": 24, "BR": 1, "AL": 2, "CL": 1, "SC": 2, "AE": 2, "IR": 3, "AU": 3, "MO": 1, "LV": 10, "CY": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 728, "proxy": 365, "home": 76, "mobile": 5, "unknown": 1}` |

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
