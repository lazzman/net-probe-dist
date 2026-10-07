# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-07 23:33:09](https://img.shields.io/badge/updated-2026--10--07_23%3A33%3A09-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9964.6s](https://img.shields.io/badge/elapsed-9964.6s-lightgrey)
![profiles: 1257](https://img.shields.io/badge/profiles-1257-blue)
![live_hits: 1257](https://img.shields.io/badge/live__hits-1257-brightgreen)
![live_fail: 76023](https://img.shields.io/badge/live__fail-76023-orange)
![kept: 867](https://img.shields.io/badge/kept-867-blue)
![new: 390](https://img.shields.io/badge/new-390-success)
![dropped: 806](https://img.shields.io/badge/dropped-806-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-07 23:33:09 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9964.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `406469` |
| **Live PASS (pool hits)** | `1257` |
| **Live FAIL** | `76023` |
| **History retained** | `867` |
| **New PASS** | `390` |
| **History dropped** | `806` |
| **Previous public** | `1673` |
| **Published profiles (deduped)** | `1257` |
| **Share links (exportable)** | `1060` |
| **YAML proxies (exportable)** | `1060` |
| **Protocol mix** | `{"vless": 504, "shadowsocks": 268, "hysteria2": 107, "trojan": 107, "vmess": 74}` |
| **Country mix** | `{"US": 170, "CA": 141, "ZA": 3, "FR": 30, "GB": 32, "SG": 38, "NL": 168, "ZZ": 1, "ID": 4, "DE": 89, "IE": 6, "IN": 11, "RO": 5, "CH": 9, "ES": 9, "FI": 16, "JP": 52, "KR": 39, "PL": 22, "AT": 2, "SC": 3, "AE": 4, "HU": 1, "HK": 46, "RU": 20, "TW": 4, "SE": 8, "TH": 2, "IT": 15, "EE": 11, "KZ": 5, "IL": 1, "TR": 8, "CL": 11, "CN": 18, "NO": 1, "LT": 9, "AU": 5, "LV": 15, "BE": 1, "PT": 1, "AL": 4, "GR": 2, "UZ": 1, "VN": 1, "BG": 7, "MY": 8, "AM": 2, "CZ": 1, "SA": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 596, "proxy": 367, "unknown": 1, "home": 86, "mobile": 14}` |

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
