# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-01 09:02:57](https://img.shields.io/badge/updated-2026--10--01_09%3A02%3A57-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10281.5s](https://img.shields.io/badge/elapsed-10281.5s-lightgrey)
![profiles: 1845](https://img.shields.io/badge/profiles-1845-blue)
![live_hits: 1845](https://img.shields.io/badge/live__hits-1845-brightgreen)
![live_fail: 77772](https://img.shields.io/badge/live__fail-77772-orange)
![kept: 1074](https://img.shields.io/badge/kept-1074-blue)
![new: 771](https://img.shields.io/badge/new-771-success)
![dropped: 131](https://img.shields.io/badge/dropped-131-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-01 09:02:57 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10281.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `431784` |
| **Live PASS (pool hits)** | `1845` |
| **Live FAIL** | `77772` |
| **History retained** | `1074` |
| **New PASS** | `771` |
| **History dropped** | `131` |
| **Previous public** | `1205` |
| **Published profiles (deduped)** | `1845` |
| **Share links (exportable)** | `1561` |
| **YAML proxies (exportable)** | `1561` |
| **Protocol mix** | `{"trojan": 50, "vless": 1002, "shadowsocks": 274, "vmess": 105, "hysteria2": 130}` |
| **Country mix** | `{"US": 271, "IE": 3, "GB": 72, "CA": 439, "NL": 161, "FR": 34, "SE": 14, "DE": 88, "ID": 3, "NO": 2, "ES": 15, "ZA": 3, "CH": 11, "JP": 43, "IN": 13, "KR": 30, "PL": 14, "AT": 1, "HU": 1, "HK": 54, "RU": 34, "FI": 30, "AE": 4, "TH": 3, "SG": 53, "IT": 22, "EE": 7, "UA": 5, "AD": 1, "MY": 15, "TW": 4, "SC": 3, "LT": 11, "DZ": 29, "PH": 1, "CL": 2, "AU": 3, "GE": 1, "TR": 3, "KZ": 4, "AL": 2, "IR": 3, "CZ": 8, "AM": 2, "SK": 1, "CN": 17, "RO": 1, "PT": 1, "BE": 2, "SA": 1, "BG": 7, "BZ": 3, "CO": 1, "LV": 1, "CR": 1, "GR": 1, "BY": 1, "RS": 1, "DK": 1, "BR": 1, "AR": 1}` |
| **Line type mix** | `{"dc": 1007, "proxy": 419, "mobile": 41, "home": 97}` |

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
