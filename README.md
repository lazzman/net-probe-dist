# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-27 06:31:49](https://img.shields.io/badge/updated-2026--08--27_06%3A31%3A49-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9471.6s](https://img.shields.io/badge/elapsed-9471.6s-lightgrey)
![profiles: 1855](https://img.shields.io/badge/profiles-1855-blue)
![live_hits: 1856](https://img.shields.io/badge/live__hits-1856-brightgreen)
![live_fail: 70786](https://img.shields.io/badge/live__fail-70786-orange)
![kept: 1141](https://img.shields.io/badge/kept-1141-blue)
![new: 715](https://img.shields.io/badge/new-715-success)
![dropped: 997](https://img.shields.io/badge/dropped-997-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-27 06:31:49 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9471.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `435221` |
| **Live PASS (pool hits)** | `1856` |
| **Live FAIL** | `70786` |
| **History retained** | `1141` |
| **New PASS** | `715` |
| **History dropped** | `997` |
| **Previous public** | `2138` |
| **Published profiles (deduped)** | `1855` |
| **Share links (exportable)** | `1423` |
| **YAML proxies (exportable)** | `1423` |
| **Protocol mix** | `{"vless": 815, "vmess": 53, "hysteria2": 213, "shadowsocks": 311, "trojan": 31}` |
| **Country mix** | `{"DE": 109, "US": 220, "SG": 63, "TR": 10, "PL": 34, "CA": 226, "JP": 34, "DZ": 11, "RU": 34, "GB": 62, "FI": 31, "NL": 253, "SE": 11, "CH": 7, "TW": 9, "ZA": 4, "FR": 36, "IN": 10, "ES": 11, "LT": 13, "AL": 2, "RO": 6, "HK": 30, "TH": 6, "KR": 26, "CN": 8, "IE": 11, "IT": 8, "AT": 4, "EE": 16, "NO": 12, "KZ": 11, "CZ": 5, "BY": 2, "AE": 2, "CO": 14, "SK": 2, "LV": 15, "DK": 1, "BR": 12, "UA": 7, "AU": 6, "BG": 8, "SC": 6, "MX": 1, "GR": 4, "KG": 1, "PE": 1, "HU": 1, "SA": 1, "AM": 1, "MY": 2, "ZZ": 1, "AF": 1, "CY": 1}` |
| **Line type mix** | `{"home": 156, "proxy": 438, "dc": 817, "mobile": 11, "unknown": 1}` |

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
