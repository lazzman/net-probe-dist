# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-12 07:18:26](https://img.shields.io/badge/updated-2026--09--12_07%3A18%3A26-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9642.0s](https://img.shields.io/badge/elapsed-9642.0s-lightgrey)
![profiles: 1538](https://img.shields.io/badge/profiles-1538-blue)
![live_hits: 1538](https://img.shields.io/badge/live__hits-1538-brightgreen)
![live_fail: 73998](https://img.shields.io/badge/live__fail-73998-orange)
![kept: 1095](https://img.shields.io/badge/kept-1095-blue)
![new: 443](https://img.shields.io/badge/new-443-success)
![dropped: 135](https://img.shields.io/badge/dropped-135-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-12 07:18:26 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9642.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `422022` |
| **Live PASS (pool hits)** | `1538` |
| **Live FAIL** | `73998` |
| **History retained** | `1095` |
| **New PASS** | `443` |
| **History dropped** | `135` |
| **Previous public** | `1230` |
| **Published profiles (deduped)** | `1538` |
| **Share links (exportable)** | `1225` |
| **YAML proxies (exportable)** | `1225` |
| **Protocol mix** | `{"shadowsocks": 267, "vless": 701, "hysteria2": 147, "vmess": 87, "trojan": 23}` |
| **Country mix** | `{"IE": 10, "NL": 199, "DE": 53, "CA": 318, "AU": 4, "SG": 35, "DZ": 24, "IN": 9, "RU": 27, "GB": 64, "FI": 15, "TW": 15, "AL": 1, "ZA": 4, "FR": 31, "NO": 3, "US": 179, "PL": 27, "ID": 1, "ES": 9, "RO": 5, "MY": 3, "JP": 31, "IT": 8, "HR": 1, "AT": 1, "SE": 6, "LT": 12, "KZ": 5, "EE": 7, "HK": 53, "AE": 2, "UA": 3, "TR": 3, "GR": 1, "LV": 10, "TH": 2, "GT": 1, "UZ": 2, "SA": 1, "AM": 1, "CN": 2, "KR": 27, "DK": 2, "CZ": 2, "PT": 3, "SC": 2, "BE": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 803, "proxy": 356, "home": 61, "mobile": 6}` |

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
