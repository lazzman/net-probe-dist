# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-22 16:35:29](https://img.shields.io/badge/updated-2026--11--22_16%3A35%3A29-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11485.2s](https://img.shields.io/badge/elapsed-11485.2s-lightgrey)
![profiles: 1339](https://img.shields.io/badge/profiles-1339-blue)
![live_hits: 1339](https://img.shields.io/badge/live__hits-1339-brightgreen)
![live_fail: 88927](https://img.shields.io/badge/live__fail-88927-orange)
![kept: 990](https://img.shields.io/badge/kept-990-blue)
![new: 349](https://img.shields.io/badge/new-349-success)
![dropped: 436](https://img.shields.io/badge/dropped-436-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-22 16:35:29 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11485.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `406534` |
| **Live PASS (pool hits)** | `1339` |
| **Live FAIL** | `88927` |
| **History retained** | `990` |
| **New PASS** | `349` |
| **History dropped** | `436` |
| **Previous public** | `1426` |
| **Published profiles (deduped)** | `1339` |
| **Share links (exportable)** | `1184` |
| **YAML proxies (exportable)** | `1184` |
| **Protocol mix** | `{"hysteria2": 76, "shadowsocks": 390, "vless": 490, "vmess": 135, "trojan": 93}` |
| **Country mix** | `{"DE": 99, "IT": 19, "RU": 29, "US": 288, "CH": 19, "AT": 2, "BY": 7, "SG": 50, "GB": 35, "NL": 139, "CN": 2, "AL": 3, "FI": 13, "CA": 125, "NO": 1, "ZA": 4, "FR": 33, "JP": 43, "ES": 31, "PL": 58, "BG": 9, "LV": 12, "LT": 6, "KR": 14, "IN": 3, "CL": 2, "AU": 6, "TW": 7, "HK": 36, "AE": 2, "EE": 8, "TR": 16, "NG": 2, "UA": 2, "SE": 13, "GR": 1, "DK": 1, "KZ": 2, "SK": 6, "MY": 2, "BR": 15, "TH": 2, "NE": 2, "LY": 1, "ID": 1, "VN": 2, "PH": 1, "IR": 3, "ZZ": 1, "RO": 1, "IL": 1, "IE": 1, "CY": 2, "CR": 2}` |
| **Line type mix** | `{"dc": 505, "proxy": 484, "home": 104, "mobile": 91, "unknown": 1}` |

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
