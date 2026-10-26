# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-26 14:39:34](https://img.shields.io/badge/updated-2026--10--26_14%3A39%3A34-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11168.8s](https://img.shields.io/badge/elapsed-11168.8s-lightgrey)
![profiles: 1740](https://img.shields.io/badge/profiles-1740-blue)
![live_hits: 1740](https://img.shields.io/badge/live__hits-1740-brightgreen)
![live_fail: 85808](https://img.shields.io/badge/live__fail-85808-orange)
![kept: 829](https://img.shields.io/badge/kept-829-blue)
![new: 911](https://img.shields.io/badge/new-911-success)
![dropped: 134](https://img.shields.io/badge/dropped-134-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-26 14:39:34 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11168.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `417997` |
| **Live PASS (pool hits)** | `1740` |
| **Live FAIL** | `85808` |
| **History retained** | `829` |
| **New PASS** | `911` |
| **History dropped** | `134` |
| **Previous public** | `963` |
| **Published profiles (deduped)** | `1740` |
| **Share links (exportable)** | `1329` |
| **YAML proxies (exportable)** | `1329` |
| **Protocol mix** | `{"shadowsocks": 244, "hysteria2": 114, "trojan": 100, "vless": 799, "vmess": 72}` |
| **Country mix** | `{"IT": 21, "US": 185, "GB": 40, "NL": 188, "HK": 45, "DE": 87, "TR": 11, "ZA": 4, "RO": 3, "BG": 10, "JP": 37, "IN": 11, "SE": 8, "RU": 37, "CA": 360, "ES": 6, "CR": 1, "HU": 2, "AT": 6, "ME": 4, "SC": 7, "LV": 4, "PL": 13, "FR": 29, "FI": 18, "SG": 49, "AE": 4, "AU": 6, "CW": 3, "KR": 13, "MD": 1, "CZ": 1, "IL": 2, "AM": 2, "CN": 4, "TW": 5, "CH": 44, "UA": 4, "TH": 5, "BR": 1, "AL": 1, "EE": 4, "UZ": 1, "BY": 6, "KZ": 5, "MY": 3, "LU": 1, "NZ": 1, "PT": 1, "CY": 3, "BZ": 3, "IR": 1, "LT": 9, "RS": 1, "GR": 2, "VN": 2, "ID": 2, "MX": 2, "PH": 1, "SA": 1, "SI": 2}` |
| **Line type mix** | `{"dc": 816, "proxy": 347, "mobile": 61, "home": 109}` |

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
