# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-15 17:36:49](https://img.shields.io/badge/updated-2026--08--15_17%3A36%3A49-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10245.5s](https://img.shields.io/badge/elapsed-10245.5s-lightgrey)
![profiles: 3472](https://img.shields.io/badge/profiles-3472-blue)
![live_hits: 3472](https://img.shields.io/badge/live__hits-3472-brightgreen)
![live_fail: 91588](https://img.shields.io/badge/live__fail-91588-orange)
![kept: 1755](https://img.shields.io/badge/kept-1755-blue)
![new: 1717](https://img.shields.io/badge/new-1717-success)
![dropped: 653](https://img.shields.io/badge/dropped-653-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-15 17:36:49 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10245.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `442554` |
| **Live PASS (pool hits)** | `3472` |
| **Live FAIL** | `91588` |
| **History retained** | `1755` |
| **New PASS** | `1717` |
| **History dropped** | `653` |
| **Previous public** | `2408` |
| **Published profiles (deduped)** | `3472` |
| **Share links (exportable)** | `2065` |
| **YAML proxies (exportable)** | `2065` |
| **Protocol mix** | `{"vless": 1268, "shadowsocks": 213, "hysteria2": 110, "vmess": 82, "trojan": 392}` |
| **Country mix** | `{"US": 235, "CA": 583, "NL": 233, "AU": 14, "SE": 11, "DE": 110, "TH": 4, "GB": 76, "JP": 174, "DZ": 1, "FI": 34, "FR": 45, "ZZ": 5, "RU": 119, "TW": 7, "PL": 31, "NO": 3, "IN": 10, "ZA": 4, "RO": 7, "SG": 63, "CO": 1, "KR": 104, "IR": 2, "IT": 9, "HK": 51, "IE": 15, "ES": 9, "SC": 8, "KZ": 12, "PT": 1, "EE": 13, "LV": 9, "CH": 3, "BG": 8, "AE": 3, "LT": 6, "AT": 5, "CZ": 5, "TR": 8, "MD": 1, "AM": 1, "MY": 1, "ID": 2, "PH": 1, "CY": 2, "DK": 2, "AZ": 1, "UA": 1, "AL": 1, "CN": 5, "BZ": 2, "CW": 2, "HU": 1, "SA": 1, "KG": 1, "GR": 1, "CR": 2, "KH": 1}` |
| **Line type mix** | `{"dc": 1336, "proxy": 566, "home": 152, "unknown": 5, "mobile": 11}` |

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
