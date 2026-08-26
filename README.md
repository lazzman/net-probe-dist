# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-26 17:33:33](https://img.shields.io/badge/updated-2026--08--26_17%3A33%3A33-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9308.4s](https://img.shields.io/badge/elapsed-9308.4s-lightgrey)
![profiles: 3131](https://img.shields.io/badge/profiles-3131-blue)
![live_hits: 3132](https://img.shields.io/badge/live__hits-3132-brightgreen)
![live_fail: 68870](https://img.shields.io/badge/live__fail-68870-orange)
![kept: 1837](https://img.shields.io/badge/kept-1837-blue)
![new: 1295](https://img.shields.io/badge/new-1295-success)
![dropped: 1200](https://img.shields.io/badge/dropped-1200-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-26 17:33:33 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9308.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `428739` |
| **Live PASS (pool hits)** | `3132` |
| **Live FAIL** | `68870` |
| **History retained** | `1837` |
| **New PASS** | `1295` |
| **History dropped** | `1200` |
| **Previous public** | `3037` |
| **Published profiles (deduped)** | `3131` |
| **Share links (exportable)** | `2138` |
| **YAML proxies (exportable)** | `2138` |
| **Protocol mix** | `{"hysteria2": 201, "vmess": 54, "shadowsocks": 308, "trojan": 44, "vless": 1531}` |
| **Country mix** | `{"DE": 160, "US": 274, "PL": 38, "CA": 603, "JP": 41, "RU": 51, "DZ": 10, "GB": 113, "NL": 281, "SE": 21, "FI": 47, "TW": 9, "ZA": 4, "FR": 43, "LT": 10, "IN": 13, "RO": 5, "HK": 53, "ES": 7, "SG": 72, "TH": 5, "KR": 25, "AT": 10, "SC": 8, "CH": 13, "EE": 26, "KZ": 17, "TR": 12, "NO": 11, "HU": 3, "VI": 2, "VN": 1, "PH": 1, "SK": 3, "BG": 15, "DK": 5, "GE": 2, "CZ": 10, "IT": 5, "ZZ": 2, "MD": 1, "LV": 23, "BY": 3, "UA": 6, "MY": 4, "IR": 18, "AL": 3, "BR": 15, "CN": 2, "MX": 1, "AE": 1, "KG": 2, "PE": 1, "AU": 5, "IS": 1, "RS": 1, "BE": 3, "AM": 2, "SI": 1, "SA": 1, "CR": 4, "BZ": 1, "CW": 1, "AF": 1, "IE": 10, "CY": 1}` |
| **Line type mix** | `{"home": 220, "dc": 1372, "proxy": 540, "mobile": 9, "unknown": 2}` |

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
