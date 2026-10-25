# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-26 07:35:52](https://img.shields.io/badge/updated-2026--10--26_07%3A35%3A52-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11188.2s](https://img.shields.io/badge/elapsed-11188.2s-lightgrey)
![profiles: 1100](https://img.shields.io/badge/profiles-1100-blue)
![live_hits: 1100](https://img.shields.io/badge/live__hits-1100-brightgreen)
![live_fail: 86329](https://img.shields.io/badge/live__fail-86329-orange)
![kept: 837](https://img.shields.io/badge/kept-837-blue)
![new: 263](https://img.shields.io/badge/new-263-success)
![dropped: 126](https://img.shields.io/badge/dropped-126-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-26 07:35:52 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11188.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `417268` |
| **Live PASS (pool hits)** | `1100` |
| **Live FAIL** | `86329` |
| **History retained** | `837` |
| **New PASS** | `263` |
| **History dropped** | `126` |
| **Previous public** | `963` |
| **Published profiles (deduped)** | `1100` |
| **Share links (exportable)** | `963` |
| **YAML proxies (exportable)** | `963` |
| **Protocol mix** | `{"shadowsocks": 243, "hysteria2": 116, "trojan": 89, "vless": 456, "vmess": 59}` |
| **Country mix** | `{"GB": 33, "US": 132, "DE": 58, "NL": 169, "IT": 16, "HK": 30, "TR": 7, "RO": 3, "ZA": 4, "SG": 46, "BG": 9, "IN": 11, "SE": 10, "JP": 23, "CA": 167, "ES": 8, "HU": 1, "CR": 1, "ME": 3, "SC": 4, "AT": 2, "LV": 11, "FR": 31, "BY": 6, "RU": 45, "FI": 15, "KR": 16, "AE": 3, "PL": 12, "AU": 4, "MD": 1, "VN": 1, "CZ": 1, "IL": 1, "AM": 2, "CN": 1, "TW": 7, "CH": 45, "UA": 2, "NO": 1, "AL": 1, "EE": 2, "KZ": 3, "TH": 1, "RS": 1, "GR": 1, "MY": 2, "ID": 1, "PH": 1, "LT": 8, "SA": 1, "MX": 1}` |
| **Line type mix** | `{"mobile": 55, "proxy": 284, "dc": 541, "home": 85}` |

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
