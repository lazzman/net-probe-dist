# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-20 21:34:54](https://img.shields.io/badge/updated-2026--09--20_21%3A34%3A54-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9933.0s](https://img.shields.io/badge/elapsed-9933.0s-lightgrey)
![profiles: 2068](https://img.shields.io/badge/profiles-2068-blue)
![live_hits: 2070](https://img.shields.io/badge/live__hits-2070-brightgreen)
![live_fail: 75328](https://img.shields.io/badge/live__fail-75328-orange)
![kept: 1302](https://img.shields.io/badge/kept-1302-blue)
![new: 768](https://img.shields.io/badge/new-768-success)
![dropped: 1076](https://img.shields.io/badge/dropped-1076-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-20 21:34:54 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9933.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `420014` |
| **Live PASS (pool hits)** | `2070` |
| **Live FAIL** | `75328` |
| **History retained** | `1302` |
| **New PASS** | `768` |
| **History dropped** | `1076` |
| **Previous public** | `2378` |
| **Published profiles (deduped)** | `2068` |
| **Share links (exportable)** | `1521` |
| **YAML proxies (exportable)** | `1521` |
| **Protocol mix** | `{"hysteria2": 135, "vmess": 60, "vless": 1026, "shadowsocks": 264, "trojan": 36}` |
| **Country mix** | `{"RU": 28, "ES": 10, "GB": 55, "CA": 480, "DK": 3, "US": 235, "KR": 33, "DE": 67, "PL": 24, "SE": 13, "NL": 192, "AL": 4, "TW": 19, "ID": 1, "FR": 30, "SG": 35, "ZA": 3, "CH": 6, "JP": 42, "IT": 11, "FI": 27, "HK": 41, "UZ": 2, "AE": 2, "TH": 2, "RO": 3, "IN": 13, "CR": 2, "GR": 2, "SA": 11, "CZ": 11, "CY": 8, "KZ": 14, "ZZ": 1, "AM": 2, "ME": 2, "EE": 7, "NO": 3, "DZ": 25, "SC": 3, "TR": 5, "AT": 3, "AU": 6, "LT": 8, "CL": 2, "BG": 7, "GT": 1, "IR": 2, "BZ": 8, "MD": 1, "IE": 1, "LV": 9, "MY": 1}` |
| **Line type mix** | `{"dc": 1035, "proxy": 412, "home": 71, "mobile": 7, "unknown": 1}` |

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
