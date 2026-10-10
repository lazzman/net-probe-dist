# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-10 09:12:40](https://img.shields.io/badge/updated-2026--10--10_09%3A12%3A40-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10031.3s](https://img.shields.io/badge/elapsed-10031.3s-lightgrey)
![profiles: 1587](https://img.shields.io/badge/profiles-1587-blue)
![live_hits: 1587](https://img.shields.io/badge/live__hits-1587-brightgreen)
![live_fail: 76475](https://img.shields.io/badge/live__fail-76475-orange)
![kept: 903](https://img.shields.io/badge/kept-903-blue)
![new: 684](https://img.shields.io/badge/new-684-success)
![dropped: 117](https://img.shields.io/badge/dropped-117-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-10 09:12:40 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10031.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `414429` |
| **Live PASS (pool hits)** | `1587` |
| **Live FAIL** | `76475` |
| **History retained** | `903` |
| **New PASS** | `684` |
| **History dropped** | `117` |
| **Previous public** | `1020` |
| **Published profiles (deduped)** | `1587` |
| **Share links (exportable)** | `1368` |
| **YAML proxies (exportable)** | `1368` |
| **Protocol mix** | `{"vless": 757, "shadowsocks": 282, "hysteria2": 120, "trojan": 140, "vmess": 69}` |
| **Country mix** | `{"US": 192, "ZA": 7, "RU": 30, "CA": 260, "GB": 33, "NL": 185, "ID": 3, "SG": 62, "DE": 114, "FR": 33, "NO": 1, "IN": 10, "ES": 12, "CH": 10, "FI": 16, "JP": 76, "IT": 22, "TH": 2, "IE": 6, "KR": 57, "PL": 21, "AT": 2, "TW": 4, "HK": 73, "EE": 13, "TR": 8, "GR": 2, "KZ": 6, "IL": 2, "MY": 11, "LV": 23, "AM": 1, "CN": 19, "RO": 3, "AE": 3, "SC": 3, "AU": 5, "UA": 1, "IS": 1, "SE": 4, "AL": 3, "VN": 2, "CZ": 2, "LT": 11, "SA": 1, "IR": 1, "BG": 7, "BZ": 2, "CR": 1, "MD": 1, "BE": 1, "BR": 1, "ME": 2, "CY": 1}` |
| **Line type mix** | `{"dc": 855, "proxy": 389, "home": 120, "mobile": 8}` |

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
