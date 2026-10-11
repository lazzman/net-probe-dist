# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-11 15:08:37](https://img.shields.io/badge/updated-2026--10--11_15%3A08%3A37-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9917.0s](https://img.shields.io/badge/elapsed-9917.0s-lightgrey)
![profiles: 2766](https://img.shields.io/badge/profiles-2766-blue)
![live_hits: 2766](https://img.shields.io/badge/live__hits-2766-brightgreen)
![live_fail: 75134](https://img.shields.io/badge/live__fail-75134-orange)
![kept: 951](https://img.shields.io/badge/kept-951-blue)
![new: 1815](https://img.shields.io/badge/new-1815-success)
![dropped: 137](https://img.shields.io/badge/dropped-137-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-11 15:08:37 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9917.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `408933` |
| **Live PASS (pool hits)** | `2766` |
| **Live FAIL** | `75134` |
| **History retained** | `951` |
| **New PASS** | `1815` |
| **History dropped** | `137` |
| **Previous public** | `1088` |
| **Published profiles (deduped)** | `2766` |
| **Share links (exportable)** | `1786` |
| **YAML proxies (exportable)** | `1786` |
| **Protocol mix** | `{"vless": 1144, "shadowsocks": 268, "hysteria2": 145, "trojan": 168, "vmess": 61}` |
| **Country mix** | `{"US": 209, "CA": 654, "NL": 187, "ZA": 3, "GB": 44, "SG": 66, "TR": 7, "DE": 90, "FR": 30, "IN": 13, "RO": 2, "IE": 7, "CH": 38, "JP": 66, "KR": 52, "IT": 22, "HK": 46, "PL": 22, "FI": 21, "ES": 14, "SE": 14, "AT": 4, "LV": 14, "RU": 32, "EE": 12, "TH": 5, "KZ": 4, "MY": 10, "AM": 1, "ID": 6, "SC": 5, "TW": 2, "NO": 1, "SA": 1, "AU": 8, "ME": 4, "CZ": 2, "AE": 5, "UA": 6, "BR": 1, "NZ": 1, "BZ": 5, "IR": 2, "CW": 4, "CY": 2, "LT": 11, "GR": 1, "AL": 3, "VN": 1, "IL": 2, "DK": 1, "CN": 17, "VG": 1, "BG": 10, "PT": 1, "CR": 2}` |
| **Line type mix** | `{"dc": 1200, "proxy": 448, "home": 111, "mobile": 35}` |

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
