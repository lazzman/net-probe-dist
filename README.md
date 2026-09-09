# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-09 21:37:33](https://img.shields.io/badge/updated-2026--09--09_21%3A37%3A33-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9719.1s](https://img.shields.io/badge/elapsed-9719.1s-lightgrey)
![profiles: 1720](https://img.shields.io/badge/profiles-1720-blue)
![live_hits: 1720](https://img.shields.io/badge/live__hits-1720-brightgreen)
![live_fail: 73778](https://img.shields.io/badge/live__fail-73778-orange)
![kept: 984](https://img.shields.io/badge/kept-984-blue)
![new: 736](https://img.shields.io/badge/new-736-success)
![dropped: 725](https://img.shields.io/badge/dropped-725-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-09 21:37:33 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9719.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `424500` |
| **Live PASS (pool hits)** | `1720` |
| **Live FAIL** | `73778` |
| **History retained** | `984` |
| **New PASS** | `736` |
| **History dropped** | `725` |
| **Previous public** | `1709` |
| **Published profiles (deduped)** | `1720` |
| **Share links (exportable)** | `1146` |
| **YAML proxies (exportable)** | `1146` |
| **Protocol mix** | `{"vless": 638, "hysteria2": 167, "vmess": 65, "shadowsocks": 256, "trojan": 20}` |
| **Country mix** | `{"CA": 213, "KR": 18, "SG": 41, "JP": 40, "FR": 27, "GB": 70, "DZ": 19, "RU": 28, "IN": 9, "AU": 4, "NL": 209, "FI": 19, "US": 157, "TW": 17, "DE": 53, "ID": 1, "ZA": 4, "PL": 33, "NO": 21, "ES": 8, "MY": 3, "IE": 4, "CN": 3, "IT": 9, "HR": 1, "KZ": 7, "EE": 4, "CZ": 3, "SE": 5, "JE": 1, "HK": 49, "LV": 15, "GR": 2, "UZ": 2, "TR": 5, "SK": 1, "LT": 11, "EG": 1, "SA": 1, "AM": 1, "TH": 4, "AE": 1, "AL": 1, "DK": 2, "AT": 2, "AR": 2, "UA": 3, "GT": 1, "PH": 1, "RO": 4, "SC": 1, "IR": 1, "HU": 1, "CH": 2, "CR": 1}` |
| **Line type mix** | `{"dc": 676, "proxy": 360, "home": 101, "mobile": 9}` |

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
