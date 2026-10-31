# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-31 22:54:30](https://img.shields.io/badge/updated-2026--10--31_22%3A54%3A30-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11049.7s](https://img.shields.io/badge/elapsed-11049.7s-lightgrey)
![profiles: 1196](https://img.shields.io/badge/profiles-1196-blue)
![live_hits: 1196](https://img.shields.io/badge/live__hits-1196-brightgreen)
![live_fail: 86166](https://img.shields.io/badge/live__fail-86166-orange)
![kept: 908](https://img.shields.io/badge/kept-908-blue)
![new: 288](https://img.shields.io/badge/new-288-success)
![dropped: 255](https://img.shields.io/badge/dropped-255-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-31 22:54:30 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11049.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `402721` |
| **Live PASS (pool hits)** | `1196` |
| **Live FAIL** | `86166` |
| **History retained** | `908` |
| **New PASS** | `288` |
| **History dropped** | `255` |
| **Previous public** | `1163` |
| **Published profiles (deduped)** | `1196` |
| **Share links (exportable)** | `1036` |
| **YAML proxies (exportable)** | `1036` |
| **Protocol mix** | `{"shadowsocks": 246, "trojan": 152, "hysteria2": 136, "vless": 443, "vmess": 59}` |
| **Country mix** | `{"IT": 15, "NL": 172, "CA": 219, "DE": 58, "US": 197, "GB": 24, "NO": 1, "UA": 3, "ZA": 2, "JP": 24, "BG": 10, "IN": 7, "FR": 34, "SG": 35, "PL": 13, "CH": 52, "MX": 4, "IL": 3, "ES": 10, "SE": 6, "KR": 17, "TH": 1, "HU": 1, "AT": 2, "HK": 29, "LT": 9, "LV": 5, "RU": 26, "BY": 8, "KZ": 4, "AE": 3, "FI": 12, "BR": 2, "AM": 2, "CN": 1, "TW": 2, "AU": 2, "AL": 1, "RO": 2, "PH": 1, "SC": 2, "TR": 4, "CZ": 2, "DK": 1, "EE": 3, "MY": 2, "ID": 1, "SI": 1, "IR": 2, "LU": 1, "SA": 1}` |
| **Line type mix** | `{"dc": 562, "proxy": 274, "home": 80, "mobile": 123}` |

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
