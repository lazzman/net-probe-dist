# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-27 03:45:48](https://img.shields.io/badge/updated-2026--11--27_03%3A45%3A48-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11563.2s](https://img.shields.io/badge/elapsed-11563.2s-lightgrey)
![profiles: 1121](https://img.shields.io/badge/profiles-1121-blue)
![live_hits: 1121](https://img.shields.io/badge/live__hits-1121-brightgreen)
![live_fail: 88661](https://img.shields.io/badge/live__fail-88661-orange)
![kept: 826](https://img.shields.io/badge/kept-826-blue)
![new: 295](https://img.shields.io/badge/new-295-success)
![dropped: 403](https://img.shields.io/badge/dropped-403-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-27 03:45:48 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11563.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `398420` |
| **Live PASS (pool hits)** | `1121` |
| **Live FAIL** | `88661` |
| **History retained** | `826` |
| **New PASS** | `295` |
| **History dropped** | `403` |
| **Previous public** | `1229` |
| **Published profiles (deduped)** | `1121` |
| **Share links (exportable)** | `1062` |
| **YAML proxies (exportable)** | `1062` |
| **Protocol mix** | `{"vmess": 132, "vless": 356, "hysteria2": 70, "shadowsocks": 419, "trojan": 85}` |
| **Country mix** | `{"AT": 2, "US": 269, "AE": 5, "PL": 58, "IT": 20, "DE": 55, "SG": 45, "HK": 33, "NL": 114, "CA": 71, "NO": 1, "ZA": 4, "ES": 31, "JP": 95, "GB": 39, "LT": 8, "IE": 1, "LV": 5, "KR": 13, "RU": 24, "SE": 10, "FR": 45, "CH": 13, "FI": 6, "BR": 11, "TR": 28, "BY": 6, "AL": 3, "BG": 7, "IN": 4, "CZ": 2, "VN": 2, "SK": 1, "TH": 3, "CN": 2, "TW": 2, "AU": 5, "KZ": 1, "LY": 1, "NG": 1, "NE": 3, "IR": 4, "RO": 2, "IL": 1, "EE": 4, "MD": 1, "MY": 1, "CL": 1}` |
| **Line type mix** | `{"proxy": 434, "dc": 432, "home": 100, "mobile": 97}` |

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
