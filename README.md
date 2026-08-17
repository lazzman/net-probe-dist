# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-17 18:00:54](https://img.shields.io/badge/updated-2026--08--17_18%3A00%3A54-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10403.3s](https://img.shields.io/badge/elapsed-10403.3s-lightgrey)
![profiles: 4151](https://img.shields.io/badge/profiles-4151-blue)
![live_hits: 4152](https://img.shields.io/badge/live__hits-4152-brightgreen)
![live_fail: 91948](https://img.shields.io/badge/live__fail-91948-orange)
![kept: 2150](https://img.shields.io/badge/kept-2150-blue)
![new: 2002](https://img.shields.io/badge/new-2002-success)
![dropped: 830](https://img.shields.io/badge/dropped-830-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-17 18:00:54 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10403.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `454446` |
| **Live PASS (pool hits)** | `4152` |
| **Live FAIL** | `91948` |
| **History retained** | `2150` |
| **New PASS** | `2002` |
| **History dropped** | `830` |
| **Previous public** | `2980` |
| **Published profiles (deduped)** | `4151` |
| **Share links (exportable)** | `2484` |
| **YAML proxies (exportable)** | `2484` |
| **Protocol mix** | `{"vless": 1518, "shadowsocks": 216, "hysteria2": 169, "vmess": 73, "trojan": 508}` |
| **Country mix** | `{"US": 257, "AU": 16, "NL": 321, "GB": 56, "CA": 570, "AT": 6, "IN": 12, "SG": 112, "FI": 52, "FR": 65, "DZ": 4, "HK": 65, "PL": 49, "DE": 152, "SE": 28, "TR": 12, "RU": 158, "RO": 8, "NO": 8, "TH": 2, "JP": 221, "ZA": 3, "IE": 17, "IT": 7, "KR": 125, "EE": 19, "KZ": 16, "AL": 4, "IR": 4, "LV": 12, "CH": 9, "CZ": 7, "BG": 11, "ES": 13, "LT": 7, "TW": 11, "KG": 1, "GR": 1, "MD": 3, "SA": 1, "AM": 1, "SC": 10, "UA": 6, "BY": 2, "PH": 3, "AE": 4, "CN": 2, "CO": 1, "PT": 1, "IL": 1, "BZ": 3, "CW": 2, "ME": 1, "DK": 3, "HU": 1, "AF": 1, "BR": 1, "BE": 2, "CR": 2, "CY": 1, "KH": 1}` |
| **Line type mix** | `{"dc": 1604, "proxy": 653, "home": 228, "mobile": 9}` |

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
