# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-17 21:55:36](https://img.shields.io/badge/updated-2026--09--17_21%3A55%3A36-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9864.2s](https://img.shields.io/badge/elapsed-9864.2s-lightgrey)
![profiles: 1973](https://img.shields.io/badge/profiles-1973-blue)
![live_hits: 1973](https://img.shields.io/badge/live__hits-1973-brightgreen)
![live_fail: 74795](https://img.shields.io/badge/live__fail-74795-orange)
![kept: 1213](https://img.shields.io/badge/kept-1213-blue)
![new: 760](https://img.shields.io/badge/new-760-success)
![dropped: 1116](https://img.shields.io/badge/dropped-1116-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-17 21:55:36 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9864.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `422959` |
| **Live PASS (pool hits)** | `1973` |
| **Live FAIL** | `74795` |
| **History retained** | `1213` |
| **New PASS** | `760` |
| **History dropped** | `1116` |
| **Previous public** | `2329` |
| **Published profiles (deduped)** | `1973` |
| **Share links (exportable)** | `1428` |
| **YAML proxies (exportable)** | `1428` |
| **Protocol mix** | `{"shadowsocks": 261, "vmess": 120, "hysteria2": 154, "vless": 850, "trojan": 43}` |
| **Country mix** | `{"IE": 2, "GB": 57, "CA": 469, "US": 194, "DE": 80, "JP": 38, "IN": 14, "RU": 27, "NL": 211, "SE": 11, "SG": 27, "TW": 18, "ID": 1, "AL": 1, "PL": 24, "RO": 4, "FR": 29, "ES": 7, "IT": 9, "EE": 10, "TR": 3, "UZ": 2, "FI": 22, "HK": 39, "GR": 2, "TH": 4, "KR": 23, "SA": 11, "CY": 6, "CH": 4, "LT": 5, "AT": 1, "MO": 2, "NO": 4, "AM": 1, "LV": 12, "CN": 1, "ZA": 3, "DZ": 24, "DK": 4, "HU": 1, "SC": 2, "KZ": 6, "AU": 3, "AE": 3, "GT": 1, "CO": 1, "CZ": 3, "BA": 1, "BE": 1, "IR": 1, "BZ": 1, "CR": 1, "MY": 1}` |
| **Line type mix** | `{"dc": 977, "proxy": 355, "home": 93, "mobile": 7}` |

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
