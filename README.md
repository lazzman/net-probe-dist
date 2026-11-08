# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-08 15:53:59](https://img.shields.io/badge/updated-2026--11--08_15%3A53%3A59-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11256.5s](https://img.shields.io/badge/elapsed-11256.5s-lightgrey)
![profiles: 1556](https://img.shields.io/badge/profiles-1556-blue)
![live_hits: 1556](https://img.shields.io/badge/live__hits-1556-brightgreen)
![live_fail: 86784](https://img.shields.io/badge/live__fail-86784-orange)
![kept: 992](https://img.shields.io/badge/kept-992-blue)
![new: 564](https://img.shields.io/badge/new-564-success)
![dropped: 276](https://img.shields.io/badge/dropped-276-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-08 15:53:59 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11256.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `398476` |
| **Live PASS (pool hits)** | `1556` |
| **Live FAIL** | `86784` |
| **History retained** | `992` |
| **New PASS** | `564` |
| **History dropped** | `276` |
| **Previous public** | `1268` |
| **Published profiles (deduped)** | `1556` |
| **Share links (exportable)** | `1229` |
| **YAML proxies (exportable)** | `1229` |
| **Protocol mix** | `{"hysteria2": 145, "shadowsocks": 326, "trojan": 114, "vless": 527, "vmess": 117}` |
| **Country mix** | `{"NL": 153, "PL": 26, "ES": 32, "US": 278, "GB": 42, "BY": 10, "CA": 193, "DE": 70, "FR": 49, "HK": 31, "FI": 10, "AL": 2, "AT": 5, "RO": 5, "NO": 1, "ZA": 3, "JP": 36, "BG": 10, "IT": 24, "SE": 18, "SG": 67, "CH": 54, "RU": 20, "IN": 6, "MX": 2, "BR": 2, "KR": 25, "PH": 1, "UA": 3, "EE": 6, "AE": 2, "LV": 4, "TR": 5, "VN": 1, "SK": 3, "KZ": 2, "TW": 4, "AU": 5, "TH": 2, "IE": 1, "IL": 2, "GR": 1, "MY": 1, "SA": 1, "CN": 1, "IR": 1, "CY": 1, "LT": 9, "MD": 1, "CR": 1, "CZ": 1, "CW": 1}` |
| **Line type mix** | `{"proxy": 444, "dc": 581, "mobile": 125, "home": 84}` |

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
