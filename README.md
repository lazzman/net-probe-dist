# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-20 14:43:18](https://img.shields.io/badge/updated-2026--10--20_14%3A43%3A18-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10818.2s](https://img.shields.io/badge/elapsed-10818.2s-lightgrey)
![profiles: 1505](https://img.shields.io/badge/profiles-1505-blue)
![live_hits: 1505](https://img.shields.io/badge/live__hits-1505-brightgreen)
![live_fail: 84015](https://img.shields.io/badge/live__fail-84015-orange)
![kept: 930](https://img.shields.io/badge/kept-930-blue)
![new: 575](https://img.shields.io/badge/new-575-success)
![dropped: 256](https://img.shields.io/badge/dropped-256-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-20 14:43:18 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10818.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `412842` |
| **Live PASS (pool hits)** | `1505` |
| **Live FAIL** | `84015` |
| **History retained** | `930` |
| **New PASS** | `575` |
| **History dropped** | `256` |
| **Previous public** | `1186` |
| **Published profiles (deduped)** | `1505` |
| **Share links (exportable)** | `1272` |
| **YAML proxies (exportable)** | `1272` |
| **Protocol mix** | `{"vless": 729, "shadowsocks": 238, "trojan": 146, "hysteria2": 90, "vmess": 69}` |
| **Country mix** | `{"NL": 174, "US": 176, "GB": 45, "DE": 78, "CA": 342, "ZA": 4, "NO": 1, "RO": 6, "IE": 1, "CH": 40, "SG": 61, "JP": 42, "IN": 11, "PL": 21, "TH": 4, "KR": 28, "CR": 2, "AT": 1, "ME": 6, "RU": 19, "TW": 4, "TR": 6, "FR": 28, "BY": 6, "FI": 16, "HK": 33, "HU": 4, "MD": 4, "SE": 6, "HR": 1, "AE": 4, "IT": 17, "CZ": 3, "IL": 1, "SA": 1, "LT": 7, "AM": 2, "SC": 7, "ZZ": 1, "MY": 2, "CL": 1, "AL": 1, "UA": 1, "ES": 7, "IR": 2, "EE": 2, "LV": 8, "KZ": 5, "AU": 5, "ID": 2, "NZ": 1, "CY": 2, "BZ": 3, "BG": 7, "CW": 4, "BR": 2, "GR": 2, "VN": 1, "CN": 4, "DK": 1}` |
| **Line type mix** | `{"proxy": 360, "dc": 759, "home": 111, "mobile": 45, "unknown": 1}` |

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
