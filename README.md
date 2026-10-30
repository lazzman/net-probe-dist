# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-30 23:24:55](https://img.shields.io/badge/updated-2026--10--30_23%3A24%3A55-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11196.1s](https://img.shields.io/badge/elapsed-11196.1s-lightgrey)
![profiles: 1155](https://img.shields.io/badge/profiles-1155-blue)
![live_hits: 1155](https://img.shields.io/badge/live__hits-1155-brightgreen)
![live_fail: 86550](https://img.shields.io/badge/live__fail-86550-orange)
![kept: 841](https://img.shields.io/badge/kept-841-blue)
![new: 314](https://img.shields.io/badge/new-314-success)
![dropped: 467](https://img.shields.io/badge/dropped-467-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-30 23:24:55 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11196.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `424053` |
| **Live PASS (pool hits)** | `1155` |
| **Live FAIL** | `86550` |
| **History retained** | `841` |
| **New PASS** | `314` |
| **History dropped** | `467` |
| **Previous public** | `1308` |
| **Published profiles (deduped)** | `1155` |
| **Share links (exportable)** | `1010` |
| **YAML proxies (exportable)** | `1010` |
| **Protocol mix** | `{"shadowsocks": 247, "trojan": 151, "hysteria2": 103, "vless": 444, "vmess": 65}` |
| **Country mix** | `{"IT": 17, "CA": 212, "NL": 152, "DE": 61, "US": 182, "GB": 26, "FI": 15, "NO": 1, "UA": 2, "ZA": 3, "CH": 54, "JP": 26, "SG": 35, "LT": 11, "FR": 30, "IN": 9, "MX": 4, "CL": 1, "ES": 9, "HK": 25, "HU": 1, "CR": 2, "LV": 8, "IL": 3, "RU": 27, "KZ": 6, "SE": 7, "BY": 7, "AE": 3, "PL": 15, "BR": 4, "TR": 4, "SA": 1, "AM": 1, "EE": 2, "KR": 17, "MY": 2, "CN": 1, "AU": 4, "BG": 8, "AL": 1, "RO": 2, "TH": 1, "SC": 2, "GR": 1, "ZZ": 1, "DK": 1, "CZ": 1, "VN": 1, "ID": 1, "IR": 2}` |
| **Line type mix** | `{"dc": 539, "proxy": 269, "home": 81, "mobile": 122, "unknown": 1}` |

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
