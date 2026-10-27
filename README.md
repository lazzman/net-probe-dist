# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-27 22:50:56](https://img.shields.io/badge/updated-2026--10--27_22%3A50%3A56-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11184.2s](https://img.shields.io/badge/elapsed-11184.2s-lightgrey)
![profiles: 1401](https://img.shields.io/badge/profiles-1401-blue)
![live_hits: 1401](https://img.shields.io/badge/live__hits-1401-brightgreen)
![live_fail: 85858](https://img.shields.io/badge/live__fail-85858-orange)
![kept: 968](https://img.shields.io/badge/kept-968-blue)
![new: 433](https://img.shields.io/badge/new-433-success)
![dropped: 450](https://img.shields.io/badge/dropped-450-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-27 22:50:56 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11184.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `414538` |
| **Live PASS (pool hits)** | `1401` |
| **Live FAIL** | `85858` |
| **History retained** | `968` |
| **New PASS** | `433` |
| **History dropped** | `450` |
| **Previous public** | `1418` |
| **Published profiles (deduped)** | `1401` |
| **Share links (exportable)** | `1224` |
| **YAML proxies (exportable)** | `1224` |
| **Protocol mix** | `{"hysteria2": 134, "shadowsocks": 268, "vless": 649, "trojan": 114, "vmess": 59}` |
| **Country mix** | `{"GB": 32, "IT": 16, "FI": 25, "DE": 80, "US": 201, "NL": 189, "TR": 22, "NO": 1, "ZA": 3, "CH": 46, "RO": 3, "IR": 2, "JP": 27, "RU": 37, "KR": 20, "CA": 245, "IN": 10, "PL": 14, "HK": 40, "ES": 19, "MX": 2, "AT": 6, "CR": 1, "LV": 4, "SG": 53, "FR": 36, "SE": 12, "GR": 1, "MD": 1, "AU": 6, "VN": 1, "MY": 2, "BG": 12, "IL": 6, "SC": 3, "TW": 1, "UA": 2, "BY": 8, "SA": 1, "TH": 2, "KZ": 4, "AL": 1, "BR": 1, "CL": 1, "EE": 3, "MK": 1, "AE": 3, "LU": 1, "RS": 1, "DK": 1, "IE": 1, "SI": 4, "ID": 1, "PH": 1, "AM": 2, "AZ": 1, "LT": 9, "CN": 1}` |
| **Line type mix** | `{"proxy": 314, "dc": 729, "mobile": 96, "home": 90}` |

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
