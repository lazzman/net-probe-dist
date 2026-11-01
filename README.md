# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-01 15:45:45](https://img.shields.io/badge/updated-2026--11--01_15%3A45%3A45-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11018.9s](https://img.shields.io/badge/elapsed-11018.9s-lightgrey)
![profiles: 1981](https://img.shields.io/badge/profiles-1981-blue)
![live_hits: 1981](https://img.shields.io/badge/live__hits-1981-brightgreen)
![live_fail: 85385](https://img.shields.io/badge/live__fail-85385-orange)
![kept: 971](https://img.shields.io/badge/kept-971-blue)
![new: 1010](https://img.shields.io/badge/new-1010-success)
![dropped: 129](https://img.shields.io/badge/dropped-129-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-01 15:45:45 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11018.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `402602` |
| **Live PASS (pool hits)** | `1981` |
| **Live FAIL** | `85385` |
| **History retained** | `971` |
| **New PASS** | `1010` |
| **History dropped** | `129` |
| **Previous public** | `1100` |
| **Published profiles (deduped)** | `1981` |
| **Share links (exportable)** | `1465` |
| **YAML proxies (exportable)** | `1465` |
| **Protocol mix** | `{"shadowsocks": 262, "hysteria2": 132, "trojan": 221, "vless": 780, "vmess": 70}` |
| **Country mix** | `{"IT": 16, "DE": 82, "NL": 185, "US": 240, "GB": 39, "NO": 1, "ZA": 5, "UA": 5, "RO": 4, "CA": 422, "BG": 15, "JP": 34, "IN": 10, "PL": 18, "SG": 59, "CH": 52, "MX": 6, "CL": 2, "ES": 12, "SE": 12, "LT": 13, "LV": 6, "RU": 23, "IL": 6, "FR": 34, "BY": 7, "KZ": 10, "HK": 42, "FI": 14, "CZ": 1, "AE": 12, "AM": 2, "KR": 19, "CN": 2, "TW": 3, "AU": 4, "CO": 1, "AL": 1, "BR": 2, "TH": 3, "PH": 2, "SC": 3, "IR": 3, "TR": 5, "GR": 3, "DK": 1, "EE": 2, "AT": 2, "VN": 2, "ID": 3, "MY": 2, "SI": 1, "MD": 2, "EG": 1, "VG": 1, "HU": 2, "RS": 1, "PT": 1, "BZ": 3, "CW": 4, "CY": 1, "CR": 2, "SA": 1, "NZ": 1}` |
| **Line type mix** | `{"dc": 897, "mobile": 125, "proxy": 351, "home": 100}` |

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
