# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-21 14:35:58](https://img.shields.io/badge/updated-2026--10--21_14%3A35%3A58-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10813.2s](https://img.shields.io/badge/elapsed-10813.2s-lightgrey)
![profiles: 1708](https://img.shields.io/badge/profiles-1708-blue)
![live_hits: 1710](https://img.shields.io/badge/live__hits-1710-brightgreen)
![live_fail: 84508](https://img.shields.io/badge/live__fail-84508-orange)
![kept: 939](https://img.shields.io/badge/kept-939-blue)
![new: 771](https://img.shields.io/badge/new-771-success)
![dropped: 239](https://img.shields.io/badge/dropped-239-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-21 14:35:58 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10813.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `410708` |
| **Live PASS (pool hits)** | `1710` |
| **Live FAIL** | `84508` |
| **History retained** | `939` |
| **New PASS** | `771` |
| **History dropped** | `239` |
| **Previous public** | `1178` |
| **Published profiles (deduped)** | `1708` |
| **Share links (exportable)** | `1347` |
| **YAML proxies (exportable)** | `1347` |
| **Protocol mix** | `{"shadowsocks": 246, "hysteria2": 90, "trojan": 153, "vless": 790, "vmess": 68}` |
| **Country mix** | `{"US": 181, "SE": 7, "NL": 187, "IT": 23, "GB": 51, "CH": 40, "HK": 38, "NO": 1, "IE": 2, "DE": 96, "ZA": 4, "RO": 4, "JP": 52, "KR": 28, "IN": 11, "IR": 5, "CA": 373, "TH": 4, "ZZ": 1, "PL": 14, "ES": 7, "CR": 1, "AT": 1, "ME": 8, "RU": 18, "TW": 5, "AE": 4, "FR": 23, "SG": 53, "FI": 14, "BZ": 3, "LT": 6, "KZ": 6, "IL": 1, "CZ": 4, "SA": 1, "DK": 2, "AM": 2, "SC": 6, "CL": 1, "TR": 7, "AU": 5, "BR": 2, "AL": 1, "EE": 3, "MX": 1, "BY": 4, "LV": 12, "NZ": 1, "CY": 3, "CW": 4, "BG": 6, "GR": 1, "MD": 4, "VN": 2, "MY": 1, "ID": 2, "UA": 2, "PT": 1}` |
| **Line type mix** | `{"proxy": 368, "dc": 811, "home": 117, "mobile": 53, "unknown": 1}` |

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
