# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-07 22:32:55](https://img.shields.io/badge/updated-2026--09--07_22%3A32%3A55-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9869.0s](https://img.shields.io/badge/elapsed-9869.0s-lightgrey)
![profiles: 1947](https://img.shields.io/badge/profiles-1947-blue)
![live_hits: 1947](https://img.shields.io/badge/live__hits-1947-brightgreen)
![live_fail: 74583](https://img.shields.io/badge/live__fail-74583-orange)
![kept: 1170](https://img.shields.io/badge/kept-1170-blue)
![new: 777](https://img.shields.io/badge/new-777-success)
![dropped: 1088](https://img.shields.io/badge/dropped-1088-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-07 22:32:55 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9869.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `439151` |
| **Live PASS (pool hits)** | `1947` |
| **Live FAIL** | `74583` |
| **History retained** | `1170` |
| **New PASS** | `777` |
| **History dropped** | `1088` |
| **Previous public** | `2258` |
| **Published profiles (deduped)** | `1947` |
| **Share links (exportable)** | `1340` |
| **YAML proxies (exportable)** | `1340` |
| **Protocol mix** | `{"trojan": 24, "vless": 829, "hysteria2": 166, "shadowsocks": 252, "vmess": 69}` |
| **Country mix** | `{"US": 200, "GB": 71, "JP": 53, "SG": 59, "SK": 1, "KR": 24, "FR": 29, "IN": 6, "AU": 4, "RU": 14, "FI": 17, "DZ": 23, "NL": 214, "DE": 57, "CA": 330, "TW": 16, "ID": 1, "ZA": 4, "IE": 3, "PL": 36, "ES": 8, "CN": 3, "MY": 3, "IT": 10, "HR": 1, "AT": 5, "KZ": 7, "NO": 19, "EE": 8, "ZZ": 7, "TR": 5, "IR": 1, "JE": 1, "HK": 47, "LV": 7, "SE": 7, "LT": 8, "EG": 1, "GR": 1, "TH": 3, "HU": 2, "SC": 2, "CH": 2, "AR": 2, "CZ": 1, "UZ": 1, "AE": 1, "BR": 2, "UA": 1, "CO": 1, "BY": 1, "PH": 1, "RO": 3, "BG": 4, "SA": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 838, "home": 111, "proxy": 375, "mobile": 9, "unknown": 7}` |

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
