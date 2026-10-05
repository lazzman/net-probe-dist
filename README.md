# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-05 15:17:39](https://img.shields.io/badge/updated-2026--10--05_15%3A17%3A39-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10306.8s](https://img.shields.io/badge/elapsed-10306.8s-lightgrey)
![profiles: 3257](https://img.shields.io/badge/profiles-3257-blue)
![live_hits: 3258](https://img.shields.io/badge/live__hits-3258-brightgreen)
![live_fail: 77016](https://img.shields.io/badge/live__fail-77016-orange)
![kept: 1081](https://img.shields.io/badge/kept-1081-blue)
![new: 2177](https://img.shields.io/badge/new-2177-success)
![dropped: 124](https://img.shields.io/badge/dropped-124-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-05 15:17:39 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10306.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `433082` |
| **Live PASS (pool hits)** | `3258` |
| **Live FAIL** | `77016` |
| **History retained** | `1081` |
| **New PASS** | `2177` |
| **History dropped** | `124` |
| **Previous public** | `1205` |
| **Published profiles (deduped)** | `3257` |
| **Share links (exportable)** | `1867` |
| **YAML proxies (exportable)** | `1867` |
| **Protocol mix** | `{"shadowsocks": 274, "vless": 1263, "vmess": 101, "hysteria2": 106, "trojan": 123}` |
| **Country mix** | `{"NL": 173, "GB": 48, "US": 261, "FI": 16, "ZA": 4, "CA": 744, "RU": 28, "DE": 94, "SG": 42, "FR": 33, "NO": 2, "RO": 6, "CH": 9, "HK": 67, "ES": 15, "JP": 58, "KR": 40, "IE": 6, "AT": 2, "HU": 1, "EE": 10, "AE": 4, "NZ": 1, "UA": 3, "LT": 12, "PL": 23, "IT": 21, "SE": 13, "IN": 10, "CL": 12, "SA": 1, "ID": 3, "SC": 5, "TW": 5, "BR": 2, "TR": 5, "AU": 8, "LV": 9, "KZ": 5, "TH": 4, "BZ": 4, "IR": 2, "BG": 13, "CW": 3, "CY": 1, "CR": 2, "GT": 1, "GR": 1, "AL": 2, "MY": 9, "AM": 2, "PT": 1, "ME": 1, "CZ": 14, "CN": 15}` |
| **Line type mix** | `{"proxy": 448, "dc": 1307, "home": 105, "mobile": 16}` |

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
