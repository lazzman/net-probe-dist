# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-07 23:56:27](https://img.shields.io/badge/updated-2026--08--07_23%3A56%3A27-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10142.5s](https://img.shields.io/badge/elapsed-10142.5s-lightgrey)
![profiles: 1553](https://img.shields.io/badge/profiles-1553-blue)
![live_hits: 1553](https://img.shields.io/badge/live__hits-1553-brightgreen)
![live_fail: 91652](https://img.shields.io/badge/live__fail-91652-orange)
![kept: 959](https://img.shields.io/badge/kept-959-blue)
![new: 594](https://img.shields.io/badge/new-594-success)
![dropped: 599](https://img.shields.io/badge/dropped-599-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-07 23:56:27 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10142.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `444403` |
| **Live PASS (pool hits)** | `1553` |
| **Live FAIL** | `91652` |
| **History retained** | `959` |
| **New PASS** | `594` |
| **History dropped** | `599` |
| **Previous public** | `1558` |
| **Published profiles (deduped)** | `1553` |
| **Share links (exportable)** | `1146` |
| **YAML proxies (exportable)** | `1146` |
| **Protocol mix** | `{"vless": 689, "vmess": 78, "hysteria2": 95, "shadowsocks": 187, "trojan": 97}` |
| **Country mix** | `{"US": 149, "GB": 43, "FR": 48, "DE": 79, "FI": 36, "AU": 3, "NL": 203, "IT": 5, "SE": 7, "SG": 25, "KR": 41, "HK": 36, "TW": 8, "RO": 6, "IE": 5, "IN": 5, "ES": 7, "ZA": 2, "JP": 49, "CA": 228, "PL": 6, "BG": 3, "SC": 8, "PT": 1, "EE": 8, "RU": 53, "AE": 2, "CH": 3, "TR": 5, "CR": 2, "KZ": 6, "AT": 3, "MD": 1, "LT": 3, "DK": 3, "PH": 7, "CN": 3, "SA": 2, "CO": 21, "AZ": 1, "TH": 1, "MY": 3, "ZZ": 1, "BR": 4, "HU": 1, "LV": 2, "BE": 2, "AM": 1, "GR": 1, "AF": 1, "CY": 1, "UA": 1, "KH": 1}` |
| **Line type mix** | `{"dc": 587, "proxy": 467, "home": 86, "mobile": 5, "unknown": 1}` |

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
