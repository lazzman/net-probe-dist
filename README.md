# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-02 15:51:39](https://img.shields.io/badge/updated-2026--11--02_15%3A51%3A39-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11119.2s](https://img.shields.io/badge/elapsed-11119.2s-lightgrey)
![profiles: 1559](https://img.shields.io/badge/profiles-1559-blue)
![live_hits: 1559](https://img.shields.io/badge/live__hits-1559-brightgreen)
![live_fail: 86184](https://img.shields.io/badge/live__fail-86184-orange)
![kept: 944](https://img.shields.io/badge/kept-944-blue)
![new: 615](https://img.shields.io/badge/new-615-success)
![dropped: 352](https://img.shields.io/badge/dropped-352-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-02 15:51:39 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11119.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `403485` |
| **Live PASS (pool hits)** | `1559` |
| **Live FAIL** | `86184` |
| **History retained** | `944` |
| **New PASS** | `615` |
| **History dropped** | `352` |
| **Previous public** | `1296` |
| **Published profiles (deduped)** | `1559` |
| **Share links (exportable)** | `1222` |
| **YAML proxies (exportable)** | `1222` |
| **Protocol mix** | `{"shadowsocks": 265, "vless": 638, "hysteria2": 149, "trojan": 99, "vmess": 71}` |
| **Country mix** | `{"IT": 19, "NL": 182, "DE": 60, "MX": 4, "BY": 9, "US": 212, "GB": 28, "IE": 1, "ZA": 2, "TR": 7, "RO": 4, "CA": 310, "SG": 45, "JP": 24, "BG": 14, "IR": 3, "CO": 1, "IN": 7, "PH": 2, "PL": 22, "EG": 1, "KR": 17, "CH": 51, "BR": 3, "AU": 3, "CL": 2, "IL": 6, "ES": 13, "SE": 10, "FR": 27, "RU": 26, "UA": 3, "FI": 11, "EE": 6, "HK": 36, "AE": 3, "CZ": 2, "VN": 1, "ID": 3, "AM": 1, "CN": 2, "TW": 3, "AT": 1, "NO": 1, "TH": 3, "LV": 3, "CR": 3, "NZ": 1, "BZ": 4, "CW": 4, "CY": 1, "RS": 1, "GR": 1, "DK": 1, "MY": 3, "LT": 11, "MD": 1, "SI": 1, "SA": 1, "KZ": 1, "SC": 1}` |
| **Line type mix** | `{"dc": 698, "proxy": 318, "mobile": 123, "home": 90}` |

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
