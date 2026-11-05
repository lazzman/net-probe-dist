# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-05 10:25:10](https://img.shields.io/badge/updated-2026--11--05_10%3A25%3A10-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11125.9s](https://img.shields.io/badge/elapsed-11125.9s-lightgrey)
![profiles: 1444](https://img.shields.io/badge/profiles-1444-blue)
![live_hits: 1444](https://img.shields.io/badge/live__hits-1444-brightgreen)
![live_fail: 86566](https://img.shields.io/badge/live__fail-86566-orange)
![kept: 834](https://img.shields.io/badge/kept-834-blue)
![new: 610](https://img.shields.io/badge/new-610-success)
![dropped: 136](https://img.shields.io/badge/dropped-136-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-05 10:25:10 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11125.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `404838` |
| **Live PASS (pool hits)** | `1444` |
| **Live FAIL** | `86566` |
| **History retained** | `834` |
| **New PASS** | `610` |
| **History dropped** | `136` |
| **Previous public** | `970` |
| **Published profiles (deduped)** | `1444` |
| **Share links (exportable)** | `1191` |
| **YAML proxies (exportable)** | `1191` |
| **Protocol mix** | `{"shadowsocks": 312, "hysteria2": 155, "vless": 539, "trojan": 101, "vmess": 84}` |
| **Country mix** | `{"DE": 77, "CA": 199, "US": 262, "BY": 9, "PL": 27, "NL": 159, "SE": 11, "IE": 1, "BG": 12, "HK": 38, "AT": 1, "ZA": 3, "EG": 1, "GB": 41, "JP": 31, "SA": 2, "RU": 24, "KR": 23, "IN": 12, "SG": 53, "IT": 18, "BR": 2, "FR": 37, "CH": 56, "MX": 1, "ES": 17, "TR": 7, "EE": 6, "UA": 2, "FI": 11, "CZ": 2, "IR": 3, "AE": 2, "VN": 1, "RO": 3, "TH": 4, "MY": 2, "TW": 2, "AU": 2, "PH": 1, "NO": 1, "AL": 1, "IL": 1, "LV": 3, "RS": 1, "GR": 1, "DK": 1, "CN": 1, "KZ": 2, "LT": 9, "SC": 3, "NZ": 1, "BZ": 1, "CW": 2}` |
| **Line type mix** | `{"mobile": 133, "dc": 587, "proxy": 405, "home": 68}` |

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
