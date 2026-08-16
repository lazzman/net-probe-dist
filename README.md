# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-16 12:20:30](https://img.shields.io/badge/updated-2026--08--16_12%3A20%3A30-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10130.2s](https://img.shields.io/badge/elapsed-10130.2s-lightgrey)
![profiles: 4455](https://img.shields.io/badge/profiles-4455-blue)
![live_hits: 4458](https://img.shields.io/badge/live__hits-4458-brightgreen)
![live_fail: 91246](https://img.shields.io/badge/live__fail-91246-orange)
![kept: 1429](https://img.shields.io/badge/kept-1429-blue)
![new: 3029](https://img.shields.io/badge/new-3029-success)
![dropped: 120](https://img.shields.io/badge/dropped-120-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-16 12:20:30 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10130.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `446378` |
| **Live PASS (pool hits)** | `4458` |
| **Live FAIL** | `91246` |
| **History retained** | `1429` |
| **New PASS** | `3029` |
| **History dropped** | `120` |
| **Previous public** | `1549` |
| **Published profiles (deduped)** | `4455` |
| **Share links (exportable)** | `2719` |
| **YAML proxies (exportable)** | `2719` |
| **Protocol mix** | `{"shadowsocks": 211, "vless": 1886, "vmess": 95, "hysteria2": 123, "trojan": 404}` |
| **Country mix** | `{"US": 335, "CA": 790, "GB": 133, "AU": 17, "NL": 280, "TH": 4, "DE": 147, "FI": 47, "JP": 193, "SE": 18, "IN": 12, "DZ": 1, "KR": 112, "HK": 76, "FR": 55, "EE": 12, "BR": 3, "ZA": 4, "PL": 35, "NO": 5, "RO": 8, "SG": 74, "IE": 15, "ES": 16, "SC": 16, "KZ": 14, "PT": 1, "RU": 165, "IR": 4, "LV": 11, "CH": 7, "LT": 9, "KG": 1, "BG": 9, "AT": 8, "IT": 11, "CZ": 4, "MD": 1, "TR": 13, "SA": 1, "ID": 1, "TW": 6, "BZ": 8, "CY": 5, "CO": 1, "AE": 4, "IL": 1, "AL": 2, "MY": 1, "CN": 8, "PH": 1, "BA": 1, "OM": 1, "CW": 4, "HU": 2, "ME": 1, "AF": 1, "BY": 1, "AM": 1, "UA": 3, "NZ": 1, "CR": 2, "GR": 2, "KH": 1, "DK": 1}` |
| **Line type mix** | `{"proxy": 717, "dc": 1792, "home": 210, "mobile": 8}` |

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
