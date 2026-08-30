# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-30 22:05:21](https://img.shields.io/badge/updated-2026--08--30_22%3A05%3A21-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9641.4s](https://img.shields.io/badge/elapsed-9641.4s-lightgrey)
![profiles: 2080](https://img.shields.io/badge/profiles-2080-blue)
![live_hits: 2083](https://img.shields.io/badge/live__hits-2083-brightgreen)
![live_fail: 71597](https://img.shields.io/badge/live__fail-71597-orange)
![kept: 1285](https://img.shields.io/badge/kept-1285-blue)
![new: 798](https://img.shields.io/badge/new-798-success)
![dropped: 820](https://img.shields.io/badge/dropped-820-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-30 22:05:21 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9641.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `421013` |
| **Live PASS (pool hits)** | `2083` |
| **Live FAIL** | `71597` |
| **History retained** | `1285` |
| **New PASS** | `798` |
| **History dropped** | `820` |
| **Previous public** | `2105` |
| **Published profiles (deduped)** | `2080` |
| **Share links (exportable)** | `1476` |
| **YAML proxies (exportable)** | `1476` |
| **Protocol mix** | `{"hysteria2": 183, "vless": 926, "shadowsocks": 269, "trojan": 32, "vmess": 66}` |
| **Country mix** | `{"MD": 3, "PL": 25, "KR": 21, "FR": 32, "IT": 6, "CA": 280, "NL": 226, "DE": 102, "DZ": 13, "RU": 44, "GB": 68, "US": 227, "FI": 27, "SG": 84, "SE": 10, "TW": 20, "ID": 1, "LT": 15, "NO": 17, "AL": 4, "ES": 11, "ZA": 3, "RO": 4, "HK": 38, "TH": 3, "CN": 9, "IE": 6, "JP": 76, "KZ": 12, "EE": 5, "IN": 7, "TR": 3, "CH": 5, "CZ": 4, "UA": 4, "AU": 3, "LV": 11, "BR": 16, "ZZ": 1, "AT": 4, "BG": 7, "PH": 1, "SC": 3, "DK": 1, "AE": 1, "SK": 1, "AR": 2, "BY": 1, "PE": 1, "MY": 4, "CO": 2, "GR": 1, "AM": 1, "SA": 1, "MX": 2}` |
| **Line type mix** | `{"dc": 954, "proxy": 393, "home": 120, "mobile": 11, "unknown": 1}` |

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
