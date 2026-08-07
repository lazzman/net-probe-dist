# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-07 18:11:39](https://img.shields.io/badge/updated-2026--08--07_18%3A11%3A39-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10022.4s](https://img.shields.io/badge/elapsed-10022.4s-lightgrey)
![profiles: 2650](https://img.shields.io/badge/profiles-2650-blue)
![live_hits: 2650](https://img.shields.io/badge/live__hits-2650-brightgreen)
![live_fail: 90241](https://img.shields.io/badge/live__fail-90241-orange)
![kept: 1379](https://img.shields.io/badge/kept-1379-blue)
![new: 1271](https://img.shields.io/badge/new-1271-success)
![dropped: 979](https://img.shields.io/badge/dropped-979-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-07 18:11:39 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10022.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `451984` |
| **Live PASS (pool hits)** | `2650` |
| **Live FAIL** | `90241` |
| **History retained** | `1379` |
| **New PASS** | `1271` |
| **History dropped** | `979` |
| **Previous public** | `2358` |
| **Published profiles (deduped)** | `2650` |
| **Share links (exportable)** | `1558` |
| **YAML proxies (exportable)** | `1558` |
| **Protocol mix** | `{"vmess": 82, "hysteria2": 96, "vless": 1072, "shadowsocks": 192, "trojan": 116}` |
| **Country mix** | `{"US": 166, "GB": 72, "NL": 221, "FR": 48, "AU": 3, "IT": 5, "DE": 100, "SE": 7, "HK": 41, "RO": 6, "FI": 38, "IE": 5, "TW": 10, "IN": 6, "ES": 10, "TH": 2, "JP": 52, "CA": 501, "TR": 5, "PL": 11, "BG": 4, "SA": 3, "SG": 31, "SC": 9, "RU": 68, "PT": 1, "EE": 8, "CH": 2, "CR": 2, "KR": 37, "HU": 1, "CO": 25, "KZ": 7, "MD": 1, "PH": 12, "LV": 4, "CN": 4, "AT": 3, "ZA": 2, "NO": 1, "AE": 4, "MY": 1, "AZ": 1, "ZZ": 2, "BR": 6, "BZ": 1, "UA": 1, "BE": 1, "DK": 2, "AM": 1, "VN": 1, "LT": 2, "KH": 1, "IR": 1, "GR": 1, "AF": 1, "CY": 1}` |
| **Line type mix** | `{"dc": 934, "proxy": 523, "home": 98, "mobile": 5, "unknown": 2}` |

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
