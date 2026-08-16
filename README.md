# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-17 05:29:34](https://img.shields.io/badge/updated-2026--08--17_05%3A29%3A34-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10335.7s](https://img.shields.io/badge/elapsed-10335.7s-lightgrey)
![profiles: 2344](https://img.shields.io/badge/profiles-2344-blue)
![live_hits: 2344](https://img.shields.io/badge/live__hits-2344-brightgreen)
![live_fail: 93102](https://img.shields.io/badge/live__fail-93102-orange)
![kept: 1465](https://img.shields.io/badge/kept-1465-blue)
![new: 879](https://img.shields.io/badge/new-879-success)
![dropped: 403](https://img.shields.io/badge/dropped-403-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-17 05:29:34 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10335.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `449363` |
| **Live PASS (pool hits)** | `2344` |
| **Live FAIL** | `93102` |
| **History retained** | `1465` |
| **New PASS** | `879` |
| **History dropped** | `403` |
| **Previous public** | `1868` |
| **Published profiles (deduped)** | `2344` |
| **Share links (exportable)** | `1680` |
| **YAML proxies (exportable)** | `1680` |
| **Protocol mix** | `{"vless": 894, "vmess": 86, "shadowsocks": 208, "hysteria2": 145, "trojan": 347}` |
| **Country mix** | `{"US": 215, "CA": 162, "AU": 14, "NL": 284, "AT": 6, "SG": 63, "DE": 109, "PL": 38, "SE": 18, "IN": 12, "HK": 61, "DZ": 2, "FR": 50, "FI": 47, "GB": 33, "EE": 12, "HU": 3, "RU": 130, "NO": 7, "RO": 6, "ZA": 3, "JP": 175, "KR": 101, "IT": 5, "IE": 14, "LV": 9, "CH": 8, "KZ": 10, "CZ": 3, "BG": 6, "LT": 5, "ES": 10, "CN": 7, "GR": 1, "TR": 11, "MD": 2, "SC": 8, "PH": 2, "ID": 1, "TW": 5, "TH": 2, "AE": 1, "OM": 1, "BR": 1, "AL": 2, "SA": 1, "CO": 1, "PT": 1, "UA": 4, "AF": 1, "BY": 1, "AM": 1, "DK": 2, "IL": 1, "CR": 1, "CY": 1, "KH": 1}` |
| **Line type mix** | `{"dc": 967, "proxy": 521, "home": 184, "mobile": 9}` |

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
