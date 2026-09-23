# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-24 03:06:39](https://img.shields.io/badge/updated-2026--09--24_03%3A06%3A39-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10108.9s](https://img.shields.io/badge/elapsed-10108.9s-lightgrey)
![profiles: 1573](https://img.shields.io/badge/profiles-1573-blue)
![live_hits: 1573](https://img.shields.io/badge/live__hits-1573-brightgreen)
![live_fail: 76983](https://img.shields.io/badge/live__fail-76983-orange)
![kept: 1077](https://img.shields.io/badge/kept-1077-blue)
![new: 496](https://img.shields.io/badge/new-496-success)
![dropped: 385](https://img.shields.io/badge/dropped-385-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-24 03:06:39 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10108.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `434652` |
| **Live PASS (pool hits)** | `1573` |
| **Live FAIL** | `76983` |
| **History retained** | `1077` |
| **New PASS** | `496` |
| **History dropped** | `385` |
| **Previous public** | `1462` |
| **Published profiles (deduped)** | `1573` |
| **Share links (exportable)** | `1202` |
| **YAML proxies (exportable)** | `1202` |
| **Protocol mix** | `{"shadowsocks": 279, "vless": 706, "trojan": 36, "hysteria2": 107, "vmess": 74}` |
| **Country mix** | `{"GB": 34, "US": 223, "ZA": 3, "DE": 61, "KR": 28, "HK": 31, "BR": 2, "CH": 7, "SE": 18, "NL": 162, "RU": 25, "CA": 313, "TW": 9, "ID": 1, "FR": 28, "NO": 2, "ES": 9, "JP": 32, "MX": 1, "IN": 16, "DK": 1, "PL": 25, "FI": 20, "TR": 4, "SG": 29, "TH": 4, "BG": 10, "AT": 3, "IT": 15, "AL": 1, "RO": 3, "MD": 1, "AM": 1, "IQ": 1, "MY": 2, "IR": 2, "CZ": 2, "DZ": 25, "SC": 3, "EE": 8, "AU": 6, "AE": 2, "KZ": 4, "CL": 5, "GT": 1, "UA": 1, "LT": 8, "LV": 8, "CO": 1, "SA": 1, "CR": 1}` |
| **Line type mix** | `{"proxy": 352, "dc": 776, "home": 60, "mobile": 15}` |

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
