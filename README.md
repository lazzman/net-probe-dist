# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-23 01:24:53](https://img.shields.io/badge/updated-2026--11--23_01%3A24%3A53-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11551.0s](https://img.shields.io/badge/elapsed-11551.0s-lightgrey)
![profiles: 1175](https://img.shields.io/badge/profiles-1175-blue)
![live_hits: 1175](https://img.shields.io/badge/live__hits-1175-brightgreen)
![live_fail: 88965](https://img.shields.io/badge/live__fail-88965-orange)
![kept: 915](https://img.shields.io/badge/kept-915-blue)
![new: 260](https://img.shields.io/badge/new-260-success)
![dropped: 269](https://img.shields.io/badge/dropped-269-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-23 01:24:53 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11551.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `404319` |
| **Live PASS (pool hits)** | `1175` |
| **Live FAIL** | `88965` |
| **History retained** | `915` |
| **New PASS** | `260` |
| **History dropped** | `269` |
| **Previous public** | `1184` |
| **Published profiles (deduped)** | `1175` |
| **Share links (exportable)** | `1056` |
| **YAML proxies (exportable)** | `1056` |
| **Protocol mix** | `{"shadowsocks": 377, "hysteria2": 78, "vless": 415, "vmess": 133, "trojan": 53}` |
| **Country mix** | `{"IT": 20, "BY": 7, "DE": 92, "US": 259, "AT": 2, "SG": 50, "NL": 129, "CN": 1, "AL": 5, "NO": 1, "FI": 8, "CA": 77, "ZA": 3, "JP": 45, "GB": 31, "PL": 61, "LT": 8, "BG": 7, "ES": 22, "KR": 17, "IN": 4, "CH": 16, "SE": 11, "FR": 35, "CL": 1, "TW": 5, "HK": 30, "LV": 8, "EE": 8, "RU": 25, "TR": 21, "LU": 1, "MY": 2, "BR": 15, "CY": 1, "AE": 3, "DK": 1, "SK": 4, "UA": 1, "IR": 4, "RO": 3, "PH": 1, "KZ": 1, "AU": 5, "IE": 1, "ID": 1, "VN": 1, "NE": 2, "TH": 1, "IL": 1}` |
| **Line type mix** | `{"proxy": 453, "dc": 435, "mobile": 57, "home": 113}` |

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
