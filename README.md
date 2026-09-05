# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-06 06:49:18](https://img.shields.io/badge/updated-2026--09--06_06%3A49%3A18-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9887.9s](https://img.shields.io/badge/elapsed-9887.9s-lightgrey)
![profiles: 1897](https://img.shields.io/badge/profiles-1897-blue)
![live_hits: 1897](https://img.shields.io/badge/live__hits-1897-brightgreen)
![live_fail: 74279](https://img.shields.io/badge/live__fail-74279-orange)
![kept: 1120](https://img.shields.io/badge/kept-1120-blue)
![new: 777](https://img.shields.io/badge/new-777-success)
![dropped: 193](https://img.shields.io/badge/dropped-193-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-06 06:49:18 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9887.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `439552` |
| **Live PASS (pool hits)** | `1897` |
| **Live FAIL** | `74279` |
| **History retained** | `1120` |
| **New PASS** | `777` |
| **History dropped** | `193` |
| **Previous public** | `1313` |
| **Published profiles (deduped)** | `1897` |
| **Share links (exportable)** | `1275` |
| **YAML proxies (exportable)** | `1275` |
| **Protocol mix** | `{"vless": 745, "trojan": 17, "hysteria2": 163, "shadowsocks": 282, "vmess": 68}` |
| **Country mix** | `{"CA": 257, "US": 195, "GB": 76, "NL": 222, "SE": 11, "JP": 54, "FR": 30, "DZ": 23, "FI": 18, "LV": 14, "DE": 61, "RU": 21, "SG": 58, "TW": 15, "PL": 30, "ZA": 4, "LT": 8, "ES": 7, "TH": 3, "CN": 4, "IE": 6, "IN": 7, "IT": 12, "EE": 6, "KZ": 7, "CZ": 4, "NO": 20, "HK": 35, "IR": 1, "TR": 4, "GR": 2, "KR": 26, "AU": 3, "SA": 1, "UZ": 2, "AE": 1, "AL": 1, "HU": 1, "SC": 2, "JE": 1, "AR": 2, "MY": 2, "BY": 1, "SK": 1, "PH": 1, "AT": 2, "EG": 1, "AM": 1, "RO": 2, "BR": 2, "BG": 6, "CH": 1}` |
| **Line type mix** | `{"dc": 764, "proxy": 396, "home": 105, "mobile": 10}` |

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
