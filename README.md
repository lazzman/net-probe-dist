# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-30 09:37:56](https://img.shields.io/badge/updated-2026--10--30_09%3A37%3A56-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11070.9s](https://img.shields.io/badge/elapsed-11070.9s-lightgrey)
![profiles: 1464](https://img.shields.io/badge/profiles-1464-blue)
![live_hits: 1464](https://img.shields.io/badge/live__hits-1464-brightgreen)
![live_fail: 86194](https://img.shields.io/badge/live__fail-86194-orange)
![kept: 834](https://img.shields.io/badge/kept-834-blue)
![new: 630](https://img.shields.io/badge/new-630-success)
![dropped: 182](https://img.shields.io/badge/dropped-182-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-30 09:37:56 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11070.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `421762` |
| **Live PASS (pool hits)** | `1464` |
| **Live FAIL** | `86194` |
| **History retained** | `834` |
| **New PASS** | `630` |
| **History dropped** | `182` |
| **Previous public** | `1016` |
| **Published profiles (deduped)** | `1464` |
| **Share links (exportable)** | `1288` |
| **YAML proxies (exportable)** | `1288` |
| **Protocol mix** | `{"shadowsocks": 279, "trojan": 132, "hysteria2": 103, "vless": 707, "vmess": 67}` |
| **Country mix** | `{"NL": 187, "CA": 299, "IT": 19, "DE": 76, "US": 228, "GB": 35, "PL": 10, "NO": 1, "UA": 5, "ZA": 4, "CH": 50, "RO": 2, "IR": 5, "SG": 56, "JP": 34, "IN": 9, "KR": 26, "MX": 5, "AU": 7, "ES": 12, "HU": 1, "CR": 2, "LT": 12, "HK": 37, "FR": 38, "FI": 17, "RU": 22, "BG": 12, "SE": 7, "BY": 7, "AE": 3, "DK": 1, "KZ": 5, "EE": 5, "TR": 7, "SA": 1, "PH": 2, "TH": 3, "IL": 5, "AM": 1, "CN": 1, "IE": 2, "AL": 2, "LV": 6, "ZZ": 1, "GR": 1, "VN": 2, "MY": 4, "BR": 1, "CL": 1, "CZ": 1, "ID": 1, "CW": 2, "AT": 1, "SC": 1, "BZ": 2, "VG": 1, "MD": 1}` |
| **Line type mix** | `{"proxy": 326, "dc": 756, "home": 94, "mobile": 112, "unknown": 1}` |

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
