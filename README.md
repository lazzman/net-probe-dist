# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-27 14:57:40](https://img.shields.io/badge/updated-2026--09--27_14%3A57%3A40-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10233.3s](https://img.shields.io/badge/elapsed-10233.3s-lightgrey)
![profiles: 3814](https://img.shields.io/badge/profiles-3814-blue)
![live_hits: 3814](https://img.shields.io/badge/live__hits-3814-brightgreen)
![live_fail: 74954](https://img.shields.io/badge/live__fail-74954-orange)
![kept: 1014](https://img.shields.io/badge/kept-1014-blue)
![new: 2800](https://img.shields.io/badge/new-2800-success)
![dropped: 107](https://img.shields.io/badge/dropped-107-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-27 14:57:40 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10233.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `432219` |
| **Live PASS (pool hits)** | `3814` |
| **Live FAIL** | `74954` |
| **History retained** | `1014` |
| **New PASS** | `2800` |
| **History dropped** | `107` |
| **Previous public** | `1121` |
| **Published profiles (deduped)** | `3814` |
| **Share links (exportable)** | `2062` |
| **YAML proxies (exportable)** | `2062` |
| **Protocol mix** | `{"trojan": 55, "vmess": 79, "shadowsocks": 295, "vless": 1511, "hysteria2": 122}` |
| **Country mix** | `{"US": 300, "CA": 917, "NL": 162, "CZ": 5, "DE": 80, "PL": 29, "ES": 10, "GB": 68, "RU": 40, "TW": 7, "ID": 1, "FR": 41, "SE": 27, "RO": 4, "ZA": 12, "CH": 8, "JP": 48, "IN": 17, "IT": 19, "AT": 5, "UA": 6, "CY": 5, "FI": 22, "SG": 41, "EE": 10, "AE": 4, "TH": 4, "HK": 31, "KZ": 6, "BG": 14, "CN": 2, "GT": 1, "MX": 3, "LT": 9, "NO": 4, "IR": 3, "SA": 1, "MY": 1, "KR": 32, "DZ": 28, "DK": 2, "LV": 10, "TR": 1, "SC": 4, "AU": 4, "NZ": 1, "BZ": 4, "BR": 1, "CW": 5, "GR": 1, "AL": 2, "AM": 1, "PT": 1, "AD": 1, "VG": 1, "CR": 2}` |
| **Line type mix** | `{"dc": 1498, "mobile": 17, "proxy": 458, "home": 95}` |

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
