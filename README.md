# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-18 14:20:09](https://img.shields.io/badge/updated-2026--09--18_14%3A20%3A09-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9734.3s](https://img.shields.io/badge/elapsed-9734.3s-lightgrey)
![profiles: 4185](https://img.shields.io/badge/profiles-4185-blue)
![live_hits: 4186](https://img.shields.io/badge/live__hits-4186-brightgreen)
![live_fail: 72584](https://img.shields.io/badge/live__fail-72584-orange)
![kept: 1096](https://img.shields.io/badge/kept-1096-blue)
![new: 3090](https://img.shields.io/badge/new-3090-success)
![dropped: 190](https://img.shields.io/badge/dropped-190-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-18 14:20:09 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9734.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `419353` |
| **Live PASS (pool hits)** | `4186` |
| **Live FAIL** | `72584` |
| **History retained** | `1096` |
| **New PASS** | `3090` |
| **History dropped** | `190` |
| **Previous public** | `1286` |
| **Published profiles (deduped)** | `4185` |
| **Share links (exportable)** | `2295` |
| **YAML proxies (exportable)** | `2295` |
| **Protocol mix** | `{"hysteria2": 138, "trojan": 91, "vmess": 60, "vless": 1733, "shadowsocks": 273}` |
| **Country mix** | `{"DE": 107, "US": 295, "IN": 15, "CA": 1119, "ES": 10, "GB": 105, "AU": 5, "DK": 2, "RU": 28, "SE": 16, "NL": 196, "SG": 34, "TW": 19, "ID": 1, "FR": 33, "PL": 25, "ZA": 3, "RO": 4, "JP": 38, "IT": 15, "AT": 3, "EE": 10, "FI": 22, "TR": 7, "UZ": 2, "AE": 3, "TH": 7, "HK": 31, "BG": 5, "CR": 2, "GR": 3, "GT": 1, "SA": 9, "CY": 10, "KZ": 8, "CH": 5, "LT": 5, "NO": 4, "MY": 3, "KR": 38, "DZ": 24, "UA": 2, "SC": 5, "IR": 2, "PT": 1, "CN": 2, "BZ": 3, "BR": 2, "CW": 3, "ME": 2, "CZ": 2, "BE": 1, "MO": 2, "AM": 1, "ZZ": 1, "VN": 2, "LV": 8, "NZ": 1, "VG": 1, "IE": 1}` |
| **Line type mix** | `{"dc": 1749, "proxy": 459, "home": 96, "mobile": 9, "unknown": 1}` |

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
