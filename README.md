# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-04 02:39:07](https://img.shields.io/badge/updated-2026--09--04_02%3A39%3A07-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9728.3s](https://img.shields.io/badge/elapsed-9728.3s-lightgrey)
![profiles: 1879](https://img.shields.io/badge/profiles-1879-blue)
![live_hits: 1879](https://img.shields.io/badge/live__hits-1879-brightgreen)
![live_fail: 73170](https://img.shields.io/badge/live__fail-73170-orange)
![kept: 1142](https://img.shields.io/badge/kept-1142-blue)
![new: 737](https://img.shields.io/badge/new-737-success)
![dropped: 236](https://img.shields.io/badge/dropped-236-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-04 02:39:07 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9728.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `424539` |
| **Live PASS (pool hits)** | `1879` |
| **Live FAIL** | `73170` |
| **History retained** | `1142` |
| **New PASS** | `737` |
| **History dropped** | `236` |
| **Previous public** | `1378` |
| **Published profiles (deduped)** | `1879` |
| **Share links (exportable)** | `1292` |
| **YAML proxies (exportable)** | `1292` |
| **Protocol mix** | `{"vless": 789, "hysteria2": 162, "shadowsocks": 259, "trojan": 22, "vmess": 60}` |
| **Country mix** | `{"FR": 28, "PL": 27, "US": 215, "FI": 18, "SG": 61, "CA": 231, "GB": 70, "DZ": 19, "RU": 31, "DE": 77, "LV": 10, "NL": 214, "TW": 23, "JP": 56, "ID": 1, "ES": 8, "ZA": 4, "NO": 21, "RO": 3, "TH": 4, "MY": 3, "CN": 3, "IT": 8, "KR": 35, "HR": 1, "IN": 7, "KZ": 9, "SE": 9, "EE": 6, "BR": 8, "TR": 10, "IR": 2, "AL": 1, "UA": 2, "GR": 2, "UZ": 2, "HK": 23, "AU": 3, "AT": 2, "LT": 8, "SC": 3, "SA": 1, "AM": 1, "HU": 1, "JE": 1, "AR": 2, "CZ": 4, "AE": 1, "CH": 2, "BY": 1, "SK": 1, "PH": 1, "EG": 1, "IE": 4, "CR": 1, "MX": 2}` |
| **Line type mix** | `{"proxy": 399, "home": 110, "dc": 775, "mobile": 8}` |

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
