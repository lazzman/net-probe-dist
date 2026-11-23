# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-23 17:12:56](https://img.shields.io/badge/updated-2026--11--23_17%3A12%3A56-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11398.5s](https://img.shields.io/badge/elapsed-11398.5s-lightgrey)
![profiles: 1318](https://img.shields.io/badge/profiles-1318-blue)
![live_hits: 1318](https://img.shields.io/badge/live__hits-1318-brightgreen)
![live_fail: 88991](https://img.shields.io/badge/live__fail-88991-orange)
![kept: 998](https://img.shields.io/badge/kept-998-blue)
![new: 320](https://img.shields.io/badge/new-320-success)
![dropped: 240](https://img.shields.io/badge/dropped-240-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-23 17:12:56 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11398.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `404977` |
| **Live PASS (pool hits)** | `1318` |
| **Live FAIL** | `88991` |
| **History retained** | `998` |
| **New PASS** | `320` |
| **History dropped** | `240` |
| **Previous public** | `1238` |
| **Published profiles (deduped)** | `1318` |
| **Share links (exportable)** | `1157` |
| **YAML proxies (exportable)** | `1157` |
| **Protocol mix** | `{"shadowsocks": 392, "hysteria2": 64, "vless": 477, "vmess": 132, "trojan": 92}` |
| **Country mix** | `{"FR": 35, "GB": 43, "IT": 21, "US": 276, "DE": 98, "AT": 2, "BY": 7, "JP": 44, "HK": 26, "SG": 45, "CN": 1, "NL": 127, "AL": 5, "KR": 14, "ZA": 5, "FI": 9, "NO": 1, "CA": 123, "PL": 60, "ES": 27, "BG": 9, "LV": 11, "LT": 10, "IE": 2, "RU": 24, "CH": 16, "SE": 14, "CL": 1, "AU": 5, "TW": 3, "ID": 1, "SA": 2, "TR": 23, "UA": 2, "EE": 9, "BR": 15, "GR": 1, "CY": 2, "DK": 1, "SK": 4, "VN": 2, "IR": 4, "KZ": 2, "RO": 8, "MY": 2, "IN": 4, "AE": 1, "NE": 4, "TH": 1, "IL": 1, "HU": 1, "NG": 2, "CR": 2}` |
| **Line type mix** | `{"dc": 493, "home": 127, "proxy": 471, "mobile": 67}` |

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
