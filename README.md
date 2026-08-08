# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-08 17:48:41](https://img.shields.io/badge/updated-2026--08--08_17%3A48%3A41-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10053.6s](https://img.shields.io/badge/elapsed-10053.6s-lightgrey)
![profiles: 2796](https://img.shields.io/badge/profiles-2796-blue)
![live_hits: 2798](https://img.shields.io/badge/live__hits-2798-brightgreen)
![live_fail: 90684](https://img.shields.io/badge/live__fail-90684-orange)
![kept: 1387](https://img.shields.io/badge/kept-1387-blue)
![new: 1411](https://img.shields.io/badge/new-1411-success)
![dropped: 895](https://img.shields.io/badge/dropped-895-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-08 17:48:41 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10053.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `444672` |
| **Live PASS (pool hits)** | `2798` |
| **Live FAIL** | `90684` |
| **History retained** | `1387` |
| **New PASS** | `1411` |
| **History dropped** | `895` |
| **Previous public** | `2282` |
| **Published profiles (deduped)** | `2796` |
| **Share links (exportable)** | `1657` |
| **YAML proxies (exportable)** | `1657` |
| **Protocol mix** | `{"vless": 1159, "shadowsocks": 202, "hysteria2": 101, "vmess": 82, "trojan": 113}` |
| **Country mix** | `{"GB": 57, "NL": 230, "US": 170, "CA": 502, "DE": 112, "AU": 4, "ES": 9, "PL": 9, "IT": 12, "SE": 17, "SG": 38, "KR": 51, "HK": 42, "TW": 7, "RO": 5, "FI": 47, "ZA": 2, "FR": 64, "JP": 52, "BG": 5, "TR": 5, "IE": 4, "RU": 84, "KZ": 5, "PT": 1, "EE": 14, "CH": 4, "CZ": 2, "AE": 3, "CR": 4, "BZ": 3, "MD": 1, "BE": 2, "TH": 3, "LT": 10, "PH": 18, "IN": 6, "CN": 7, "NO": 1, "UA": 1, "DK": 2, "AZ": 1, "MY": 2, "AT": 2, "ID": 1, "MT": 1, "CW": 2, "CO": 11, "SC": 5, "LV": 15, "SA": 2, "BR": 1, "HU": 2, "IR": 2, "AM": 1, "VN": 1, "GR": 1, "AF": 1, "CY": 1, "KH": 1}` |
| **Line type mix** | `{"dc": 1022, "proxy": 526, "home": 116, "mobile": 4}` |

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
