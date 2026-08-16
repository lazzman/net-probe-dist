# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-16 17:40:51](https://img.shields.io/badge/updated-2026--08--16_17%3A40%3A51-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10207.5s](https://img.shields.io/badge/elapsed-10207.5s-lightgrey)
![profiles: 3886](https://img.shields.io/badge/profiles-3886-blue)
![live_hits: 3886](https://img.shields.io/badge/live__hits-3886-brightgreen)
![live_fail: 91293](https://img.shields.io/badge/live__fail-91293-orange)
![kept: 2105](https://img.shields.io/badge/kept-2105-blue)
![new: 1781](https://img.shields.io/badge/new-1781-success)
![dropped: 614](https://img.shields.io/badge/dropped-614-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-16 17:40:51 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10207.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `447228` |
| **Live PASS (pool hits)** | `3886` |
| **Live FAIL** | `91293` |
| **History retained** | `2105` |
| **New PASS** | `1781` |
| **History dropped** | `614` |
| **Previous public** | `2719` |
| **Published profiles (deduped)** | `3886` |
| **Share links (exportable)** | `2346` |
| **YAML proxies (exportable)** | `2346` |
| **Protocol mix** | `{"vless": 1520, "hysteria2": 140, "vmess": 86, "shadowsocks": 212, "trojan": 388}` |
| **Country mix** | `{"NL": 291, "US": 280, "CA": 630, "AU": 16, "GB": 65, "AT": 9, "DE": 145, "TH": 5, "IN": 13, "FI": 49, "DZ": 3, "SE": 19, "HK": 60, "TW": 6, "FR": 51, "PL": 44, "EE": 12, "RO": 8, "SG": 65, "ES": 12, "JP": 178, "CO": 1, "IT": 12, "KR": 107, "IE": 13, "SC": 8, "KZ": 13, "RU": 130, "IR": 4, "CH": 8, "LV": 10, "OM": 1, "AE": 4, "BG": 8, "KG": 1, "CZ": 5, "MD": 2, "TR": 11, "LT": 9, "AM": 1, "ID": 1, "MY": 2, "BZ": 5, "ZA": 2, "PH": 1, "BR": 2, "CN": 4, "PT": 1, "BA": 1, "UA": 2, "CW": 3, "AL": 2, "GR": 1, "NO": 6, "HU": 2, "SA": 1, "AF": 1, "BY": 1, "DK": 2, "IL": 1, "CR": 2, "CY": 1, "KH": 1}` |
| **Line type mix** | `{"proxy": 608, "dc": 1564, "home": 175, "mobile": 7}` |

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
