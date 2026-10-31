# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-01 04:03:55](https://img.shields.io/badge/updated-2026--11--01_04%3A03%3A55-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11147.9s](https://img.shields.io/badge/elapsed-11147.9s-lightgrey)
![profiles: 1162](https://img.shields.io/badge/profiles-1162-blue)
![live_hits: 1162](https://img.shields.io/badge/live__hits-1162-brightgreen)
![live_fail: 86242](https://img.shields.io/badge/live__fail-86242-orange)
![kept: 855](https://img.shields.io/badge/kept-855-blue)
![new: 307](https://img.shields.io/badge/new-307-success)
![dropped: 181](https://img.shields.io/badge/dropped-181-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-01 04:03:55 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11147.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `403206` |
| **Live PASS (pool hits)** | `1162` |
| **Live FAIL** | `86242` |
| **History retained** | `855` |
| **New PASS** | `307` |
| **History dropped** | `181` |
| **Previous public** | `1036` |
| **Published profiles (deduped)** | `1162` |
| **Share links (exportable)** | `1022` |
| **YAML proxies (exportable)** | `1022` |
| **Protocol mix** | `{"shadowsocks": 249, "hysteria2": 132, "trojan": 143, "vless": 432, "vmess": 66}` |
| **Country mix** | `{"IT": 13, "NL": 152, "DE": 58, "BG": 12, "GB": 22, "US": 197, "NO": 1, "UA": 3, "ZA": 2, "RO": 3, "RU": 28, "AL": 2, "JP": 24, "CA": 220, "IN": 5, "SG": 37, "PL": 18, "MX": 3, "BR": 2, "AU": 2, "CH": 50, "SE": 7, "ES": 11, "AT": 1, "LT": 12, "LV": 3, "IL": 3, "FR": 32, "FI": 13, "KZ": 5, "KR": 22, "HK": 22, "CZ": 1, "VN": 1, "AM": 1, "TW": 3, "CO": 1, "TH": 2, "PH": 2, "SC": 2, "BY": 8, "TR": 5, "AE": 2, "DK": 1, "EE": 2, "ID": 2, "MY": 2, "SI": 1, "CN": 2, "IR": 1, "SA": 1}` |
| **Line type mix** | `{"dc": 554, "proxy": 273, "mobile": 120, "home": 78}` |

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
