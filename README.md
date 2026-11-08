# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-09 00:02:15](https://img.shields.io/badge/updated-2026--11--09_00%3A02%3A15-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11269.5s](https://img.shields.io/badge/elapsed-11269.5s-lightgrey)
![profiles: 1162](https://img.shields.io/badge/profiles-1162-blue)
![live_hits: 1162](https://img.shields.io/badge/live__hits-1162-brightgreen)
![live_fail: 87367](https://img.shields.io/badge/live__fail-87367-orange)
![kept: 864](https://img.shields.io/badge/kept-864-blue)
![new: 298](https://img.shields.io/badge/new-298-success)
![dropped: 365](https://img.shields.io/badge/dropped-365-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-09 00:02:15 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11269.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `400242` |
| **Live PASS (pool hits)** | `1162` |
| **Live FAIL** | `87367` |
| **History retained** | `864` |
| **New PASS** | `298` |
| **History dropped** | `365` |
| **Previous public** | `1229` |
| **Published profiles (deduped)** | `1162` |
| **Share links (exportable)** | `976` |
| **YAML proxies (exportable)** | `976` |
| **Protocol mix** | `{"shadowsocks": 326, "hysteria2": 149, "trojan": 87, "vless": 301, "vmess": 113}` |
| **Country mix** | `{"CA": 86, "BY": 11, "PL": 23, "US": 264, "ES": 23, "FR": 37, "NL": 139, "DE": 57, "HK": 21, "AT": 3, "RO": 4, "ZA": 4, "RU": 13, "GB": 28, "JP": 18, "MX": 2, "IN": 4, "IT": 24, "SG": 46, "CH": 55, "KR": 24, "IL": 1, "AU": 4, "PH": 1, "SE": 17, "EE": 6, "IR": 1, "UA": 2, "AE": 2, "FI": 7, "BG": 8, "TR": 6, "SK": 4, "KZ": 3, "BR": 1, "TW": 5, "TH": 2, "NO": 1, "CL": 1, "LV": 4, "NG": 1, "GR": 1, "VN": 1, "MY": 1, "SA": 1, "LT": 10}` |
| **Line type mix** | `{"proxy": 406, "dc": 400, "home": 58, "mobile": 113}` |

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
