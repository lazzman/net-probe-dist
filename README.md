# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-07 01:52:01](https://img.shields.io/badge/updated-2026--09--07_01%3A52%3A01-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9876.8s](https://img.shields.io/badge/elapsed-9876.8s-lightgrey)
![profiles: 1975](https://img.shields.io/badge/profiles-1975-blue)
![live_hits: 1976](https://img.shields.io/badge/live__hits-1976-brightgreen)
![live_fail: 74392](https://img.shields.io/badge/live__fail-74392-orange)
![kept: 1197](https://img.shields.io/badge/kept-1197-blue)
![new: 779](https://img.shields.io/badge/new-779-success)
![dropped: 167](https://img.shields.io/badge/dropped-167-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-07 01:52:01 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9876.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `436083` |
| **Live PASS (pool hits)** | `1976` |
| **Live FAIL** | `74392` |
| **History retained** | `1197` |
| **New PASS** | `779` |
| **History dropped** | `167` |
| **Previous public** | `1364` |
| **Published profiles (deduped)** | `1975` |
| **Share links (exportable)** | `1334` |
| **YAML proxies (exportable)** | `1334` |
| **Protocol mix** | `{"trojan": 36, "vless": 783, "hysteria2": 165, "shadowsocks": 286, "vmess": 64}` |
| **Country mix** | `{"US": 201, "CA": 292, "GB": 73, "SE": 9, "SK": 1, "HR": 1, "FR": 32, "RU": 20, "DZ": 23, "AU": 6, "FI": 20, "DE": 57, "NL": 216, "SG": 58, "TW": 16, "ZA": 5, "ID": 1, "PL": 41, "NO": 23, "ES": 10, "JP": 52, "CZ": 4, "TH": 5, "MY": 3, "CN": 2, "IE": 9, "IN": 5, "IT": 13, "KZ": 8, "EE": 6, "KR": 26, "AE": 1, "IR": 2, "LV": 15, "GR": 2, "HK": 34, "LT": 6, "TR": 3, "SA": 1, "UZ": 2, "HU": 1, "AT": 6, "SC": 2, "CH": 2, "AR": 2, "JE": 1, "UA": 2, "BY": 1, "PH": 1, "EG": 1, "AM": 1, "RO": 2, "CO": 1, "BG": 6, "BR": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 818, "proxy": 404, "home": 105, "mobile": 8}` |

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
