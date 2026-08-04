# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-04 10:54:15](https://img.shields.io/badge/updated-2026--08--04_10%3A54%3A15-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 1488.3s](https://img.shields.io/badge/elapsed-1488.3s-lightgrey)
![profiles: 2187](https://img.shields.io/badge/profiles-2187-blue)
![live_hits: 2194](https://img.shields.io/badge/live__hits-2194-brightgreen)
![live_fail: 8717](https://img.shields.io/badge/live__fail-8717-orange)
![kept: 962](https://img.shields.io/badge/kept-962-blue)
![new: 1232](https://img.shields.io/badge/new-1232-success)
![dropped: 212](https://img.shields.io/badge/dropped-212-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-04 10:54:15 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `1488.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `29022` |
| **Live PASS (pool hits)** | `2194` |
| **Live FAIL** | `8717` |
| **History retained** | `962` |
| **New PASS** | `1232` |
| **History dropped** | `212` |
| **Previous public** | `1174` |
| **Published profiles (deduped)** | `2187` |
| **Share links (exportable)** | `1546` |
| **YAML proxies (exportable)** | `1546` |
| **Protocol mix** | `{"vless": 1128, "shadowsocks": 198, "trojan": 92, "vmess": 64, "hysteria2": 64}` |
| **Country mix** | `{"US": 203, "CA": 498, "NL": 190, "DE": 82, "RU": 63, "FI": 27, "FR": 36, "GB": 36, "IT": 18, "AT": 5, "PL": 19, "CH": 1, "HK": 39, "HU": 1, "TW": 13, "SE": 18, "SG": 26, "PA": 1, "ES": 12, "KZ": 5, "LV": 12, "JP": 48, "KR": 41, "ID": 1, "CO": 10, "EE": 6, "MD": 1, "SC": 7, "LT": 3, "PH": 77, "IS": 4, "CR": 2, "CY": 3, "BZ": 1, "IN": 4, "AL": 1, "RO": 3, "ZA": 2, "TH": 1, "TR": 4, "SA": 2, "BG": 5, "MY": 2, "NO": 1, "CN": 1, "BH": 1, "AZ": 1, "AE": 1, "IR": 1, "BE": 2, "BY": 1, "AU": 4, "BR": 4, "IL": 2, "DK": 2, "KH": 1}` |
| **Line type mix** | `{"dc": 904, "home": 82, "proxy": 562, "mobile": 7}` |

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
