# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-14 12:53:53](https://img.shields.io/badge/updated-2026--08--14_12%3A53%3A53-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10168.1s](https://img.shields.io/badge/elapsed-10168.1s-lightgrey)
![profiles: 3657](https://img.shields.io/badge/profiles-3657-blue)
![live_hits: 3657](https://img.shields.io/badge/live__hits-3657-brightgreen)
![live_fail: 91580](https://img.shields.io/badge/live__fail-91580-orange)
![kept: 1131](https://img.shields.io/badge/kept-1131-blue)
![new: 2526](https://img.shields.io/badge/new-2526-success)
![dropped: 207](https://img.shields.io/badge/dropped-207-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-14 12:53:53 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10168.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `447252` |
| **Live PASS (pool hits)** | `3657` |
| **Live FAIL** | `91580` |
| **History retained** | `1131` |
| **New PASS** | `2526` |
| **History dropped** | `207` |
| **Previous public** | `1338` |
| **Published profiles (deduped)** | `3657` |
| **Share links (exportable)** | `2205` |
| **YAML proxies (exportable)** | `2205` |
| **Protocol mix** | `{"vless": 1537, "shadowsocks": 216, "vmess": 85, "hysteria2": 105, "trojan": 262}` |
| **Country mix** | `{"US": 275, "NL": 219, "CA": 703, "FR": 48, "AU": 11, "JP": 132, "TH": 6, "GB": 101, "FI": 56, "TR": 11, "DE": 116, "TW": 8, "ZA": 3, "PL": 23, "IN": 7, "RO": 8, "SG": 59, "ES": 12, "KZ": 10, "IR": 4, "IT": 15, "KR": 82, "IE": 8, "HK": 54, "AT": 6, "EE": 12, "RU": 136, "SE": 10, "LV": 9, "CH": 2, "CO": 5, "SC": 12, "MD": 1, "BG": 7, "BZ": 6, "CY": 3, "LT": 3, "PT": 1, "CZ": 4, "MY": 2, "AZ": 1, "NO": 1, "AE": 2, "BR": 2, "UA": 4, "AF": 1, "AL": 3, "HU": 3, "CW": 4, "ME": 1, "SA": 1, "AM": 1, "CR": 2, "NZ": 1, "KH": 1}` |
| **Line type mix** | `{"dc": 1426, "proxy": 640, "home": 146, "mobile": 6}` |

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
