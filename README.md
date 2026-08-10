# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-10 12:47:03](https://img.shields.io/badge/updated-2026--08--10_12%3A47%3A03-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10037.2s](https://img.shields.io/badge/elapsed-10037.2s-lightgrey)
![profiles: 4051](https://img.shields.io/badge/profiles-4051-blue)
![live_hits: 4051](https://img.shields.io/badge/live__hits-4051-brightgreen)
![live_fail: 90325](https://img.shields.io/badge/live__fail-90325-orange)
![kept: 1088](https://img.shields.io/badge/kept-1088-blue)
![new: 2963](https://img.shields.io/badge/new-2963-success)
![dropped: 143](https://img.shields.io/badge/dropped-143-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-10 12:47:03 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10037.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `451365` |
| **Live PASS (pool hits)** | `4051` |
| **Live FAIL** | `90325` |
| **History retained** | `1088` |
| **New PASS** | `2963` |
| **History dropped** | `143` |
| **Previous public** | `1231` |
| **Published profiles (deduped)** | `4051` |
| **Share links (exportable)** | `2453` |
| **YAML proxies (exportable)** | `2453` |
| **Protocol mix** | `{"vless": 1966, "vmess": 81, "shadowsocks": 196, "hysteria2": 92, "trojan": 118}` |
| **Country mix** | `{"US": 265, "NL": 260, "GB": 122, "DE": 132, "AU": 7, "IT": 12, "TH": 5, "SE": 22, "FR": 143, "RO": 6, "BR": 4, "FI": 77, "IN": 7, "ZA": 2, "ES": 8, "JP": 77, "CA": 728, "PL": 18, "KR": 46, "BG": 6, "SG": 32, "SA": 3, "HK": 51, "IE": 4, "RU": 211, "KZ": 7, "PT": 1, "TR": 13, "EE": 23, "BE": 6, "CH": 3, "MD": 2, "CO": 5, "TW": 7, "IR": 2, "LV": 6, "SC": 10, "AE": 6, "LT": 5, "PH": 62, "CN": 2, "BZ": 7, "CY": 3, "AZ": 1, "NO": 1, "ID": 1, "AL": 3, "MY": 3, "UA": 7, "AT": 8, "AM": 1, "HU": 3, "CW": 4, "ME": 1, "AF": 1, "GR": 1, "KH": 1, "NZ": 1, "CZ": 1, "CR": 2}` |
| **Line type mix** | `{"dc": 1454, "proxy": 808, "home": 188, "mobile": 8}` |

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
