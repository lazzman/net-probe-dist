# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-23 07:48:45](https://img.shields.io/badge/updated-2026--09--23_07%3A48%3A45-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9940.0s](https://img.shields.io/badge/elapsed-9940.0s-lightgrey)
![profiles: 1717](https://img.shields.io/badge/profiles-1717-blue)
![live_hits: 1718](https://img.shields.io/badge/live__hits-1718-brightgreen)
![live_fail: 76206](https://img.shields.io/badge/live__fail-76206-orange)
![kept: 1212](https://img.shields.io/badge/kept-1212-blue)
![new: 506](https://img.shields.io/badge/new-506-success)
![dropped: 216](https://img.shields.io/badge/dropped-216-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-23 07:48:45 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9940.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `421815` |
| **Live PASS (pool hits)** | `1718` |
| **Live FAIL** | `76206` |
| **History retained** | `1212` |
| **New PASS** | `506` |
| **History dropped** | `216` |
| **Previous public** | `1428` |
| **Published profiles (deduped)** | `1717` |
| **Share links (exportable)** | `1345` |
| **YAML proxies (exportable)** | `1345` |
| **Protocol mix** | `{"shadowsocks": 251, "vless": 888, "hysteria2": 102, "vmess": 83, "trojan": 21}` |
| **Country mix** | `{"DE": 62, "US": 254, "RU": 27, "KR": 31, "GB": 39, "CA": 321, "SE": 16, "CH": 11, "NL": 165, "ZA": 5, "ID": 2, "FR": 35, "ES": 11, "SG": 27, "JP": 40, "DK": 2, "IN": 17, "CL": 5, "PL": 24, "HK": 42, "FI": 31, "TR": 3, "TW": 12, "TH": 4, "IT": 16, "AL": 1, "AT": 3, "CY": 10, "BE": 4, "KZ": 12, "BZ": 8, "LU": 1, "IE": 3, "HU": 2, "EE": 8, "RO": 3, "MD": 2, "AM": 2, "BR": 3, "NO": 4, "IR": 4, "RS": 2, "DZ": 25, "AU": 5, "AE": 2, "BG": 8, "ZZ": 3, "IS": 2, "BY": 1, "PT": 1, "MX": 1, "UA": 1, "MY": 4, "GR": 2, "SK": 3, "LT": 4, "UZ": 2, "CZ": 1, "SC": 1, "LV": 6, "EG": 1, "SA": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 856, "home": 87, "proxy": 389, "mobile": 14, "unknown": 3}` |

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
