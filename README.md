# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-18 14:21:20](https://img.shields.io/badge/updated-2026--10--18_14%3A21%3A20-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10796.1s](https://img.shields.io/badge/elapsed-10796.1s-lightgrey)
![profiles: 1671](https://img.shields.io/badge/profiles-1671-blue)
![live_hits: 1671](https://img.shields.io/badge/live__hits-1671-brightgreen)
![live_fail: 85614](https://img.shields.io/badge/live__fail-85614-orange)
![kept: 837](https://img.shields.io/badge/kept-837-blue)
![new: 834](https://img.shields.io/badge/new-834-success)
![dropped: 136](https://img.shields.io/badge/dropped-136-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-18 14:21:20 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10796.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `467034` |
| **Live PASS (pool hits)** | `1671` |
| **Live FAIL** | `85614` |
| **History retained** | `837` |
| **New PASS** | `834` |
| **History dropped** | `136` |
| **Previous public** | `973` |
| **Published profiles (deduped)** | `1671` |
| **Share links (exportable)** | `1380` |
| **YAML proxies (exportable)** | `1380` |
| **Protocol mix** | `{"vless": 826, "shadowsocks": 233, "hysteria2": 109, "trojan": 144, "vmess": 68}` |
| **Country mix** | `{"US": 199, "ZA": 5, "RU": 41, "CA": 331, "GB": 52, "CH": 38, "HK": 35, "AU": 6, "NL": 185, "DE": 84, "RO": 3, "JP": 45, "MX": 1, "CZ": 3, "IN": 10, "KR": 34, "IT": 16, "PL": 27, "SG": 65, "ES": 11, "CR": 1, "AT": 1, "ME": 8, "FI": 17, "LV": 14, "TW": 5, "HU": 5, "KH": 1, "FR": 31, "BY": 6, "SE": 7, "TH": 5, "LT": 8, "MD": 4, "AE": 6, "IL": 1, "PH": 6, "AM": 2, "EE": 5, "CL": 1, "NO": 1, "TR": 11, "UA": 4, "SC": 6, "IR": 2, "KZ": 6, "ID": 3, "NZ": 1, "CY": 3, "BZ": 3, "BG": 7, "CW": 4, "GR": 1, "VN": 1, "MY": 2, "BR": 2, "DK": 1, "UZ": 1, "SA": 1, "PT": 1}` |
| **Line type mix** | `{"dc": 820, "proxy": 399, "home": 128, "mobile": 39}` |

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
