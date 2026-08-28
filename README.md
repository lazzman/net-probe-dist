# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-28 20:39:28](https://img.shields.io/badge/updated-2026--08--28_20%3A39%3A28-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9785.6s](https://img.shields.io/badge/elapsed-9785.6s-lightgrey)
![profiles: 2064](https://img.shields.io/badge/profiles-2064-blue)
![live_hits: 2064](https://img.shields.io/badge/live__hits-2064-brightgreen)
![live_fail: 72132](https://img.shields.io/badge/live__fail-72132-orange)
![kept: 980](https://img.shields.io/badge/kept-980-blue)
![new: 1084](https://img.shields.io/badge/new-1084-success)
![dropped: 453](https://img.shields.io/badge/dropped-453-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-28 20:39:28 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9785.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `420087` |
| **Live PASS (pool hits)** | `2064` |
| **Live FAIL** | `72132` |
| **History retained** | `980` |
| **New PASS** | `1084` |
| **History dropped** | `453` |
| **Previous public** | `1433` |
| **Published profiles (deduped)** | `2064` |
| **Share links (exportable)** | `1395` |
| **YAML proxies (exportable)** | `1395` |
| **Protocol mix** | `{"hysteria2": 175, "shadowsocks": 288, "vless": 802, "vmess": 113, "trojan": 17}` |
| **Country mix** | `{"PL": 24, "RU": 22, "NL": 209, "DE": 93, "CA": 344, "DZ": 9, "GB": 63, "FI": 30, "SG": 95, "US": 184, "BR": 11, "TW": 12, "ZA": 4, "FR": 27, "LT": 8, "HK": 40, "JP": 37, "ES": 3, "TH": 4, "MY": 2, "LV": 14, "IE": 8, "CN": 5, "IT": 6, "NO": 16, "IN": 10, "TR": 7, "KZ": 14, "SE": 3, "GR": 2, "AU": 5, "AE": 1, "MD": 1, "AT": 2, "CH": 5, "EE": 5, "KR": 25, "BG": 6, "CZ": 12, "UA": 4, "RO": 2, "SC": 1, "AR": 2, "MX": 3, "DK": 2, "PE": 1, "IR": 1, "AL": 2, "CO": 4, "AM": 1, "VN": 1, "SA": 1, "ID": 1, "GE": 1}` |
| **Line type mix** | `{"dc": 876, "proxy": 379, "home": 130, "mobile": 10}` |

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
