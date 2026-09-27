# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-27 22:20:20](https://img.shields.io/badge/updated-2026--09--27_22%3A20%3A20-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10086.3s](https://img.shields.io/badge/elapsed-10086.3s-lightgrey)
![profiles: 1398](https://img.shields.io/badge/profiles-1398-blue)
![live_hits: 1399](https://img.shields.io/badge/live__hits-1399-brightgreen)
![live_fail: 77488](https://img.shields.io/badge/live__fail-77488-orange)
![kept: 1028](https://img.shields.io/badge/kept-1028-blue)
![new: 371](https://img.shields.io/badge/new-371-success)
![dropped: 1034](https://img.shields.io/badge/dropped-1034-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-27 22:20:20 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10086.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `433900` |
| **Live PASS (pool hits)** | `1399` |
| **Live FAIL** | `77488` |
| **History retained** | `1028` |
| **New PASS** | `371` |
| **History dropped** | `1034` |
| **Previous public** | `2062` |
| **Published profiles (deduped)** | `1398` |
| **Share links (exportable)** | `1188` |
| **YAML proxies (exportable)** | `1188` |
| **Protocol mix** | `{"trojan": 28, "vmess": 77, "shadowsocks": 287, "vless": 677, "hysteria2": 119}` |
| **Country mix** | `{"US": 221, "ES": 9, "CZ": 4, "GB": 41, "DE": 56, "PL": 27, "UA": 2, "CA": 292, "NL": 149, "TW": 6, "FR": 32, "ID": 1, "RO": 6, "ZA": 12, "CH": 8, "JP": 45, "IN": 15, "DK": 1, "SE": 19, "FI": 18, "TR": 1, "RU": 25, "SG": 33, "EE": 10, "AE": 2, "TH": 2, "IR": 2, "KZ": 5, "GT": 1, "HK": 32, "MX": 2, "IT": 11, "ZZ": 3, "NO": 3, "AM": 1, "KR": 28, "MD": 1, "AT": 1, "SA": 1, "DZ": 28, "AL": 2, "AU": 3, "CN": 2, "BE": 1, "CW": 1, "AD": 1, "SC": 1, "LT": 7, "LV": 10, "RS": 1, "BG": 3, "CR": 1, "HU": 1}` |
| **Line type mix** | `{"dc": 738, "mobile": 14, "proxy": 364, "home": 71, "unknown": 3}` |

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
