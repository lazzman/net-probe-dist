# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-28 15:21:06](https://img.shields.io/badge/updated-2026--10--28_15%3A21%3A06-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10999.5s](https://img.shields.io/badge/elapsed-10999.5s-lightgrey)
![profiles: 1648](https://img.shields.io/badge/profiles-1648-blue)
![live_hits: 1648](https://img.shields.io/badge/live__hits-1648-brightgreen)
![live_fail: 85686](https://img.shields.io/badge/live__fail-85686-orange)
![kept: 964](https://img.shields.io/badge/kept-964-blue)
![new: 684](https://img.shields.io/badge/new-684-success)
![dropped: 284](https://img.shields.io/badge/dropped-284-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-28 15:21:06 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10999.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `414928` |
| **Live PASS (pool hits)** | `1648` |
| **Live FAIL** | `85686` |
| **History retained** | `964` |
| **New PASS** | `684` |
| **History dropped** | `284` |
| **Previous public** | `1248` |
| **Published profiles (deduped)** | `1648` |
| **Share links (exportable)** | `1333` |
| **YAML proxies (exportable)** | `1333` |
| **Protocol mix** | `{"shadowsocks": 255, "hysteria2": 143, "trojan": 130, "vless": 744, "vmess": 61}` |
| **Country mix** | `{"DE": 81, "US": 227, "NL": 202, "IT": 15, "GB": 39, "NO": 2, "UA": 4, "ZA": 4, "CH": 47, "TR": 5, "BG": 9, "JP": 33, "SE": 17, "CA": 283, "RU": 32, "IL": 7, "ES": 16, "IN": 10, "PL": 13, "MX": 3, "HU": 1, "CR": 3, "AT": 2, "MD": 2, "FR": 35, "BY": 11, "HK": 45, "AU": 7, "TH": 5, "AE": 5, "CW": 3, "FI": 25, "KR": 25, "GR": 1, "SG": 47, "VN": 2, "SA": 1, "AM": 1, "SC": 3, "MY": 4, "TW": 3, "RO": 2, "KZ": 7, "AL": 2, "CL": 1, "BR": 5, "EE": 5, "LV": 6, "LU": 1, "IE": 2, "NZ": 1, "BZ": 3, "RS": 1, "DK": 1, "ID": 2, "CN": 1, "LT": 9, "PT": 1, "IR": 1, "CY": 1, "VG": 1, "UZ": 1}` |
| **Line type mix** | `{"mobile": 92, "proxy": 370, "dc": 761, "home": 111}` |

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
