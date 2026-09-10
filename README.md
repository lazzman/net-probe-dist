# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-10 21:32:47](https://img.shields.io/badge/updated-2026--09--10_21%3A32%3A47-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9757.3s](https://img.shields.io/badge/elapsed-9757.3s-lightgrey)
![profiles: 1769](https://img.shields.io/badge/profiles-1769-blue)
![live_hits: 1769](https://img.shields.io/badge/live__hits-1769-brightgreen)
![live_fail: 74277](https://img.shields.io/badge/live__fail-74277-orange)
![kept: 1076](https://img.shields.io/badge/kept-1076-blue)
![new: 693](https://img.shields.io/badge/new-693-success)
![dropped: 988](https://img.shields.io/badge/dropped-988-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-10 21:32:47 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9757.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `432520` |
| **Live PASS (pool hits)** | `1769` |
| **Live FAIL** | `74277` |
| **History retained** | `1076` |
| **New PASS** | `693` |
| **History dropped** | `988` |
| **Previous public** | `2064` |
| **Published profiles (deduped)** | `1769` |
| **Share links (exportable)** | `1277` |
| **YAML proxies (exportable)** | `1277` |
| **Protocol mix** | `{"hysteria2": 157, "vmess": 65, "vless": 741, "shadowsocks": 248, "trojan": 66}` |
| **Country mix** | `{"DZ": 21, "GB": 47, "RU": 35, "IT": 16, "JP": 40, "FI": 18, "DE": 60, "US": 177, "NL": 193, "SG": 37, "TW": 15, "ID": 1, "FR": 25, "CA": 355, "PL": 37, "ES": 11, "MY": 5, "IE": 7, "CN": 2, "IN": 8, "KR": 25, "AT": 5, "HR": 1, "SC": 4, "KZ": 8, "CZ": 3, "LV": 14, "TR": 7, "CH": 6, "HK": 40, "GR": 2, "UZ": 2, "SK": 1, "SE": 10, "LT": 10, "ZZ": 1, "EG": 1, "NO": 3, "SA": 1, "ZA": 3, "EE": 6, "RO": 3, "CL": 1, "DK": 1, "UA": 1, "BG": 2, "AU": 2, "TH": 2, "GT": 1, "PH": 1, "AM": 1, "BY": 1, "BR": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 811, "proxy": 364, "home": 98, "mobile": 7, "unknown": 1}` |

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
