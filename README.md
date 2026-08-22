# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-22 17:18:25](https://img.shields.io/badge/updated-2026--08--22_17%3A18%3A25-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 8971.9s](https://img.shields.io/badge/elapsed-8971.9s-lightgrey)
![profiles: 3407](https://img.shields.io/badge/profiles-3407-blue)
![live_hits: 3407](https://img.shields.io/badge/live__hits-3407-brightgreen)
![live_fail: 65589](https://img.shields.io/badge/live__fail-65589-orange)
![kept: 1752](https://img.shields.io/badge/kept-1752-blue)
![new: 1655](https://img.shields.io/badge/new-1655-success)
![dropped: 602](https://img.shields.io/badge/dropped-602-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-22 17:18:25 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `8971.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `438871` |
| **Live PASS (pool hits)** | `3407` |
| **Live FAIL** | `65589` |
| **History retained** | `1752` |
| **New PASS** | `1655` |
| **History dropped** | `602` |
| **Previous public** | `2354` |
| **Published profiles (deduped)** | `3407` |
| **Share links (exportable)** | `2107` |
| **YAML proxies (exportable)** | `2107` |
| **Protocol mix** | `{"shadowsocks": 333, "vless": 1409, "vmess": 73, "hysteria2": 159, "trojan": 133}` |
| **Country mix** | `{"US": 279, "NL": 314, "CA": 588, "AU": 20, "GB": 70, "FR": 40, "BG": 15, "DE": 165, "PL": 43, "HK": 77, "SG": 75, "RU": 37, "FI": 39, "SE": 15, "BR": 24, "IN": 16, "ES": 9, "ZA": 4, "JP": 35, "CN": 7, "AT": 6, "LV": 16, "TW": 17, "IT": 13, "KZ": 16, "BE": 1, "TR": 11, "IL": 1, "CH": 15, "EE": 18, "VN": 2, "KG": 1, "CO": 11, "MD": 2, "DK": 4, "SK": 1, "LT": 13, "SC": 11, "TH": 6, "KR": 26, "PT": 1, "HR": 1, "IR": 4, "AL": 3, "UA": 3, "NO": 4, "MY": 2, "PH": 2, "RO": 5, "AZ": 1, "CZ": 4, "AE": 2, "BZ": 3, "HU": 1, "ME": 2, "IE": 2, "SA": 1, "AM": 1, "CW": 1, "CR": 1, "JE": 1, "BY": 1, "AF": 1, "CY": 1, "DZ": 1}` |
| **Line type mix** | `{"proxy": 587, "dc": 1279, "home": 234, "mobile": 12}` |

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
