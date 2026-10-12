# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-13 01:27:04](https://img.shields.io/badge/updated-2026--10--13_01%3A27%3A04-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10135.0s](https://img.shields.io/badge/elapsed-10135.0s-lightgrey)
![profiles: 1334](https://img.shields.io/badge/profiles-1334-blue)
![live_hits: 1334](https://img.shields.io/badge/live__hits-1334-brightgreen)
![live_fail: 77215](https://img.shields.io/badge/live__fail-77215-orange)
![kept: 899](https://img.shields.io/badge/kept-899-blue)
![new: 435](https://img.shields.io/badge/new-435-success)
![dropped: 952](https://img.shields.io/badge/dropped-952-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-13 01:27:04 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10135.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `412632` |
| **Live PASS (pool hits)** | `1334` |
| **Live FAIL** | `77215` |
| **History retained** | `899` |
| **New PASS** | `435` |
| **History dropped** | `952` |
| **Previous public** | `1851` |
| **Published profiles (deduped)** | `1334` |
| **Share links (exportable)** | `1063` |
| **YAML proxies (exportable)** | `1063` |
| **Protocol mix** | `{"vless": 484, "shadowsocks": 255, "hysteria2": 120, "trojan": 145, "vmess": 59}` |
| **Country mix** | `{"US": 146, "CA": 163, "ZA": 5, "RU": 38, "GB": 28, "NL": 173, "HK": 44, "SG": 45, "DE": 66, "FR": 27, "IE": 7, "RO": 3, "CH": 40, "JP": 63, "IN": 13, "TH": 3, "KR": 48, "SC": 2, "FI": 16, "AT": 1, "PL": 19, "AE": 2, "EE": 8, "GR": 1, "KZ": 5, "IT": 15, "AM": 2, "IL": 1, "MY": 10, "ME": 3, "LV": 14, "ID": 3, "CN": 5, "TW": 3, "SE": 11, "ES": 5, "UA": 1, "TR": 3, "CZ": 1, "BR": 3, "AL": 3, "ZZ": 1, "LT": 9, "VN": 1, "AU": 5, "DK": 1, "SA": 1, "BG": 6}` |
| **Line type mix** | `{"dc": 585, "proxy": 335, "home": 105, "mobile": 47, "unknown": 1}` |

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
