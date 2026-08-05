# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-05 17:00:41](https://img.shields.io/badge/updated-2026--08--05_17%3A00%3A41-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 1519.7s](https://img.shields.io/badge/elapsed-1519.7s-lightgrey)
![profiles: 1425](https://img.shields.io/badge/profiles-1425-blue)
![live_hits: 1431](https://img.shields.io/badge/live__hits-1431-brightgreen)
![live_fail: 9208](https://img.shields.io/badge/live__fail-9208-orange)
![kept: 1066](https://img.shields.io/badge/kept-1066-blue)
![new: 365](https://img.shields.io/badge/new-365-success)
![dropped: 342](https://img.shields.io/badge/dropped-342-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-05 17:00:41 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `1519.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `29396` |
| **Live PASS (pool hits)** | `1431` |
| **Live FAIL** | `9208` |
| **History retained** | `1066` |
| **New PASS** | `365` |
| **History dropped** | `342` |
| **Previous public** | `1408` |
| **Published profiles (deduped)** | `1425` |
| **Share links (exportable)** | `1175` |
| **YAML proxies (exportable)** | `1175` |
| **Protocol mix** | `{"vless": 742, "shadowsocks": 199, "vmess": 63, "trojan": 96, "hysteria2": 75}` |
| **Country mix** | `{"US": 164, "CA": 321, "PT": 1, "FI": 19, "RU": 49, "NL": 164, "HK": 34, "DE": 72, "GB": 34, "EE": 6, "SE": 19, "PL": 11, "CH": 1, "TW": 9, "HU": 1, "SG": 21, "PA": 1, "ES": 10, "LV": 10, "KZ": 4, "FR": 36, "TR": 5, "JP": 42, "KR": 45, "DK": 3, "IT": 19, "CO": 6, "MD": 1, "PH": 12, "LT": 3, "CR": 1, "SC": 4, "IN": 4, "NO": 1, "AU": 3, "BG": 4, "ZA": 2, "IE": 4, "MY": 1, "BH": 1, "AZ": 1, "RO": 3, "BR": 11, "IR": 1, "AE": 1, "MX": 1, "CN": 2, "CZ": 1, "AT": 3, "IL": 1, "TH": 2, "KH": 1, "SA": 3}` |
| **Line type mix** | `{"home": 66, "dc": 661, "proxy": 447, "mobile": 5}` |

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
