# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-08 12:36:59](https://img.shields.io/badge/updated-2026--08--08_12%3A36%3A59-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9998.3s](https://img.shields.io/badge/elapsed-9998.3s-lightgrey)
![profiles: 3680](https://img.shields.io/badge/profiles-3680-blue)
![live_hits: 3680](https://img.shields.io/badge/live__hits-3680-brightgreen)
![live_fail: 90050](https://img.shields.io/badge/live__fail-90050-orange)
![kept: 922](https://img.shields.io/badge/kept-922-blue)
![new: 2758](https://img.shields.io/badge/new-2758-success)
![dropped: 147](https://img.shields.io/badge/dropped-147-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-08 12:36:59 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9998.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `446736` |
| **Live PASS (pool hits)** | `3680` |
| **Live FAIL** | `90050` |
| **History retained** | `922` |
| **New PASS** | `2758` |
| **History dropped** | `147` |
| **Previous public** | `1069` |
| **Published profiles (deduped)** | `3680` |
| **Share links (exportable)** | `2282` |
| **YAML proxies (exportable)** | `2282` |
| **Protocol mix** | `{"vless": 1764, "vmess": 91, "shadowsocks": 210, "hysteria2": 103, "trojan": 114}` |
| **Country mix** | `{"NL": 245, "US": 324, "CA": 736, "FR": 126, "FI": 32, "ES": 10, "DE": 124, "GB": 94, "AU": 9, "IT": 12, "SE": 13, "SG": 42, "HK": 47, "TW": 8, "KR": 55, "RO": 5, "NO": 1, "ZA": 2, "IR": 6, "TH": 4, "JP": 70, "BG": 8, "PL": 8, "IE": 4, "SA": 3, "SC": 16, "KZ": 8, "PT": 1, "EE": 9, "RU": 89, "CH": 3, "AE": 6, "CR": 4, "ZZ": 2, "TR": 6, "AM": 1, "MD": 1, "BE": 2, "LT": 5, "PH": 51, "MY": 2, "IN": 9, "CN": 9, "AT": 5, "BZ": 13, "CY": 4, "NZ": 2, "HU": 6, "UA": 6, "ID": 1, "CW": 10, "CO": 15, "AZ": 1, "MT": 1, "BR": 7, "LV": 5, "ME": 1, "GR": 1, "AF": 1, "DK": 1, "KH": 1}` |
| **Line type mix** | `{"home": 118, "dc": 1424, "proxy": 738, "mobile": 11, "unknown": 2}` |

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
