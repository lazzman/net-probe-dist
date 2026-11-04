# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-04 10:09:50](https://img.shields.io/badge/updated-2026--11--04_10%3A09%3A50-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11166.0s](https://img.shields.io/badge/elapsed-11166.0s-lightgrey)
![profiles: 1738](https://img.shields.io/badge/profiles-1738-blue)
![live_hits: 1738](https://img.shields.io/badge/live__hits-1738-brightgreen)
![live_fail: 86281](https://img.shields.io/badge/live__fail-86281-orange)
![kept: 882](https://img.shields.io/badge/kept-882-blue)
![new: 856](https://img.shields.io/badge/new-856-success)
![dropped: 116](https://img.shields.io/badge/dropped-116-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-04 10:09:50 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11166.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `403586` |
| **Live PASS (pool hits)** | `1738` |
| **Live FAIL** | `86281` |
| **History retained** | `882` |
| **New PASS** | `856` |
| **History dropped** | `116` |
| **Previous public** | `998` |
| **Published profiles (deduped)** | `1738` |
| **Share links (exportable)** | `1448` |
| **YAML proxies (exportable)** | `1448` |
| **Protocol mix** | `{"shadowsocks": 335, "hysteria2": 148, "trojan": 91, "vless": 790, "vmess": 84}` |
| **Country mix** | `{"IT": 16, "DE": 88, "NL": 197, "BY": 9, "PL": 23, "US": 276, "IE": 1, "HK": 46, "AT": 2, "ZA": 4, "RO": 3, "JP": 31, "GB": 46, "CA": 338, "BG": 14, "IN": 10, "CO": 1, "RU": 33, "KR": 28, "PH": 1, "TR": 7, "SG": 70, "CH": 56, "MX": 1, "IL": 2, "ES": 18, "SE": 17, "FR": 35, "UA": 8, "EE": 5, "FI": 11, "AE": 4, "VN": 1, "LT": 11, "CN": 2, "TW": 2, "AU": 4, "NO": 1, "BR": 1, "LV": 2, "GE": 1, "MY": 4, "ID": 1, "KZ": 1, "TH": 2, "SA": 1, "IR": 2, "SC": 2, "NZ": 1, "BZ": 4, "CW": 3, "VG": 1, "HU": 1, "MD": 1, "GR": 1}` |
| **Line type mix** | `{"dc": 822, "mobile": 124, "proxy": 421, "home": 84}` |

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
