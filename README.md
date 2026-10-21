# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-22 03:49:07](https://img.shields.io/badge/updated-2026--10--22_03%3A49%3A07-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10974.4s](https://img.shields.io/badge/elapsed-10974.4s-lightgrey)
![profiles: 1125](https://img.shields.io/badge/profiles-1125-blue)
![live_hits: 1125](https://img.shields.io/badge/live__hits-1125-brightgreen)
![live_fail: 85490](https://img.shields.io/badge/live__fail-85490-orange)
![kept: 850](https://img.shields.io/badge/kept-850-blue)
![new: 275](https://img.shields.io/badge/new-275-success)
![dropped: 218](https://img.shields.io/badge/dropped-218-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-22 03:49:07 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10974.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `413195` |
| **Live PASS (pool hits)** | `1125` |
| **Live FAIL** | `85490` |
| **History retained** | `850` |
| **New PASS** | `275` |
| **History dropped** | `218` |
| **Previous public** | `1068` |
| **Published profiles (deduped)** | `1125` |
| **Share links (exportable)** | `962` |
| **YAML proxies (exportable)** | `962` |
| **Protocol mix** | `{"vless": 434, "shadowsocks": 247, "hysteria2": 97, "trojan": 120, "vmess": 64}` |
| **Country mix** | `{"NL": 165, "IT": 18, "GB": 32, "TR": 3, "US": 151, "SE": 8, "HK": 30, "NO": 1, "IE": 4, "DE": 68, "ZA": 2, "RO": 5, "CH": 40, "JP": 37, "KR": 20, "MX": 2, "RU": 15, "CA": 192, "IN": 9, "PL": 14, "LV": 16, "AT": 1, "ME": 3, "SC": 5, "CR": 1, "FR": 22, "AE": 3, "SG": 33, "FI": 10, "GR": 1, "EE": 3, "KZ": 1, "IR": 1, "IL": 1, "CZ": 4, "MY": 1, "SA": 1, "DK": 1, "AM": 1, "CN": 2, "TW": 5, "TH": 1, "AL": 1, "ES": 6, "UA": 3, "BY": 4, "BG": 5, "AU": 3, "MD": 4, "VN": 1, "ID": 1, "LT": 2, "BR": 1}` |
| **Line type mix** | `{"proxy": 304, "dc": 533, "home": 76, "mobile": 51}` |

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
