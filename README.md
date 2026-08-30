# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-31 02:55:35](https://img.shields.io/badge/updated-2026--08--31_02%3A55%3A35-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9599.1s](https://img.shields.io/badge/elapsed-9599.1s-lightgrey)
![profiles: 1981](https://img.shields.io/badge/profiles-1981-blue)
![live_hits: 1981](https://img.shields.io/badge/live__hits-1981-brightgreen)
![live_fail: 71712](https://img.shields.io/badge/live__fail-71712-orange)
![kept: 1265](https://img.shields.io/badge/kept-1265-blue)
![new: 716](https://img.shields.io/badge/new-716-success)
![dropped: 211](https://img.shields.io/badge/dropped-211-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-31 02:55:35 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9599.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `419811` |
| **Live PASS (pool hits)** | `1981` |
| **Live FAIL** | `71712` |
| **History retained** | `1265` |
| **New PASS** | `716` |
| **History dropped** | `211` |
| **Previous public** | `1476` |
| **Published profiles (deduped)** | `1981` |
| **Share links (exportable)** | `1408` |
| **YAML proxies (exportable)** | `1408` |
| **Protocol mix** | `{"vless": 868, "hysteria2": 180, "shadowsocks": 281, "trojan": 25, "vmess": 54}` |
| **Country mix** | `{"FR": 30, "MD": 4, "NL": 229, "CA": 237, "DE": 96, "IT": 7, "RU": 34, "FI": 26, "GB": 69, "SG": 88, "US": 222, "CH": 6, "DZ": 13, "SE": 7, "BR": 15, "JP": 68, "PL": 25, "NO": 16, "ID": 1, "LT": 14, "RO": 4, "ES": 10, "TW": 23, "HK": 33, "TH": 3, "MY": 5, "CN": 7, "KZ": 10, "EE": 5, "IN": 6, "TR": 5, "IR": 1, "AE": 1, "UA": 3, "AT": 3, "AL": 4, "LV": 11, "KR": 25, "IE": 5, "ZA": 3, "CZ": 5, "DK": 1, "SK": 1, "PH": 1, "SC": 5, "AR": 2, "AU": 3, "BG": 5, "BY": 2, "PE": 1, "CO": 3, "GR": 1, "AM": 1, "SA": 1, "MX": 2}` |
| **Line type mix** | `{"dc": 901, "proxy": 390, "home": 108, "mobile": 9}` |

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
