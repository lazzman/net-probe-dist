# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-08 21:34:06](https://img.shields.io/badge/updated-2026--09--08_21%3A34%3A06-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10085.8s](https://img.shields.io/badge/elapsed-10085.8s-lightgrey)
![profiles: 1925](https://img.shields.io/badge/profiles-1925-blue)
![live_hits: 1926](https://img.shields.io/badge/live__hits-1926-brightgreen)
![live_fail: 74949](https://img.shields.io/badge/live__fail-74949-orange)
![kept: 1136](https://img.shields.io/badge/kept-1136-blue)
![new: 790](https://img.shields.io/badge/new-790-success)
![dropped: 872](https://img.shields.io/badge/dropped-872-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-08 21:34:06 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10085.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `433224` |
| **Live PASS (pool hits)** | `1926` |
| **Live FAIL** | `74949` |
| **History retained** | `1136` |
| **New PASS** | `790` |
| **History dropped** | `872` |
| **Previous public** | `2008` |
| **Published profiles (deduped)** | `1925` |
| **Share links (exportable)** | `1332` |
| **YAML proxies (exportable)** | `1332` |
| **Protocol mix** | `{"vless": 810, "shadowsocks": 268, "hysteria2": 149, "trojan": 36, "vmess": 69}` |
| **Country mix** | `{"CA": 377, "ZA": 5, "PL": 32, "GB": 70, "RU": 24, "IN": 7, "FI": 12, "DZ": 19, "IT": 13, "DE": 47, "NL": 205, "SG": 49, "ID": 1, "JP": 46, "FR": 25, "US": 187, "NO": 22, "LT": 8, "RO": 3, "ES": 9, "CN": 5, "MY": 4, "IE": 2, "KR": 24, "KZ": 7, "JE": 1, "EE": 5, "SE": 9, "TW": 16, "HK": 45, "BR": 2, "LV": 15, "GR": 2, "TH": 1, "SK": 1, "AT": 4, "TR": 4, "EG": 1, "SA": 1, "HU": 1, "CH": 3, "SC": 2, "AR": 2, "UZ": 1, "AU": 3, "AE": 1, "UA": 2, "GT": 1, "PH": 1, "CZ": 2, "AM": 1, "IR": 1, "DK": 1, "VN": 1, "BG": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 862, "proxy": 375, "home": 87, "mobile": 11}` |

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
