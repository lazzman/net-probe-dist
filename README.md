# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-05 07:10:24](https://img.shields.io/badge/updated-2026--09--05_07%3A10%3A24-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9758.9s](https://img.shields.io/badge/elapsed-9758.9s-lightgrey)
![profiles: 2049](https://img.shields.io/badge/profiles-2049-blue)
![live_hits: 2049](https://img.shields.io/badge/live__hits-2049-brightgreen)
![live_fail: 73823](https://img.shields.io/badge/live__fail-73823-orange)
![kept: 1210](https://img.shields.io/badge/kept-1210-blue)
![new: 839](https://img.shields.io/badge/new-839-success)
![dropped: 162](https://img.shields.io/badge/dropped-162-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-05 07:10:24 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9758.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `428502` |
| **Live PASS (pool hits)** | `2049` |
| **Live FAIL** | `73823` |
| **History retained** | `1210` |
| **New PASS** | `839` |
| **History dropped** | `162` |
| **Previous public** | `1372` |
| **Published profiles (deduped)** | `2049` |
| **Share links (exportable)** | `1365` |
| **YAML proxies (exportable)** | `1365` |
| **Protocol mix** | `{"vless": 823, "shadowsocks": 286, "hysteria2": 161, "trojan": 34, "vmess": 61}` |
| **Country mix** | `{"US": 204, "DE": 86, "IE": 7, "SG": 58, "CA": 262, "IT": 8, "AU": 5, "GB": 71, "IN": 5, "DZ": 19, "FI": 22, "RU": 31, "SE": 12, "NL": 232, "TW": 21, "RO": 5, "JP": 59, "PL": 30, "FR": 30, "ID": 1, "ES": 9, "ZA": 4, "MY": 3, "CN": 4, "TH": 5, "AT": 5, "TR": 6, "KZ": 10, "EE": 10, "CZ": 4, "NO": 23, "HK": 27, "AE": 1, "IR": 1, "AL": 2, "LV": 12, "UA": 3, "GR": 2, "KR": 33, "UZ": 3, "SK": 1, "LT": 6, "SA": 1, "BR": 6, "AM": 1, "HU": 1, "CH": 2, "AR": 2, "JE": 1, "PH": 2, "SC": 2, "BY": 1, "EG": 1, "CR": 1, "BG": 1, "MX": 2}` |
| **Line type mix** | `{"dc": 846, "home": 110, "proxy": 399, "mobile": 11}` |

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
