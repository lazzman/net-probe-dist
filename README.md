# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-11 21:30:14](https://img.shields.io/badge/updated-2026--09--11_21%3A30%3A14-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9688.8s](https://img.shields.io/badge/elapsed-9688.8s-lightgrey)
![profiles: 1847](https://img.shields.io/badge/profiles-1847-blue)
![live_hits: 1847](https://img.shields.io/badge/live__hits-1847-brightgreen)
![live_fail: 73611](https://img.shields.io/badge/live__fail-73611-orange)
![kept: 1218](https://img.shields.io/badge/kept-1218-blue)
![new: 629](https://img.shields.io/badge/new-629-success)
![dropped: 1099](https://img.shields.io/badge/dropped-1099-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-11 21:30:14 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9688.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `420998` |
| **Live PASS (pool hits)** | `1847` |
| **Live FAIL** | `73611` |
| **History retained** | `1218` |
| **New PASS** | `629` |
| **History dropped** | `1099` |
| **Previous public** | `2317` |
| **Published profiles (deduped)** | `1847` |
| **Share links (exportable)** | `1402` |
| **YAML proxies (exportable)** | `1402` |
| **Protocol mix** | `{"vmess": 88, "vless": 861, "hysteria2": 148, "shadowsocks": 253, "trojan": 52}` |
| **Country mix** | `{"US": 173, "CA": 476, "JP": 30, "PL": 31, "IE": 11, "DE": 71, "SG": 35, "IN": 12, "AU": 4, "DZ": 23, "RU": 19, "NL": 197, "FI": 18, "GB": 63, "TW": 15, "ID": 2, "FR": 27, "NO": 3, "RO": 3, "ES": 6, "IT": 8, "HR": 1, "KZ": 8, "EE": 8, "TR": 6, "HK": 57, "GR": 2, "SK": 1, "SE": 9, "LT": 11, "SA": 1, "MY": 2, "CN": 1, "KR": 29, "TH": 3, "UZ": 2, "ZA": 3, "DK": 2, "CL": 1, "CH": 3, "LV": 8, "AE": 4, "UA": 3, "GT": 1, "PT": 3, "SC": 2, "BE": 1, "CZ": 2, "MX": 1, "AT": 1, "IR": 1, "CR": 1, "BG": 1}` |
| **Line type mix** | `{"home": 79, "dc": 965, "proxy": 355, "mobile": 7}` |

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
