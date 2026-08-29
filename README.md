# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-29 08:29:48](https://img.shields.io/badge/updated-2026--08--29_08%3A29%3A48-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9571.7s](https://img.shields.io/badge/elapsed-9571.7s-lightgrey)
![profiles: 2198](https://img.shields.io/badge/profiles-2198-blue)
![live_hits: 2201](https://img.shields.io/badge/live__hits-2201-brightgreen)
![live_fail: 70540](https://img.shields.io/badge/live__fail-70540-orange)
![kept: 1046](https://img.shields.io/badge/kept-1046-blue)
![new: 1155](https://img.shields.io/badge/new-1155-success)
![dropped: 349](https://img.shields.io/badge/dropped-349-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-29 08:29:48 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9571.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `418372` |
| **Live PASS (pool hits)** | `2201` |
| **Live FAIL** | `70540` |
| **History retained** | `1046` |
| **New PASS** | `1155` |
| **History dropped** | `349` |
| **Previous public** | `1395` |
| **Published profiles (deduped)** | `2198` |
| **Share links (exportable)** | `1642` |
| **YAML proxies (exportable)** | `1642` |
| **Protocol mix** | `{"shadowsocks": 303, "vmess": 97, "hysteria2": 192, "vless": 1025, "trojan": 25}` |
| **Country mix** | `{"NL": 251, "US": 241, "DE": 123, "KR": 37, "PL": 40, "CA": 314, "DZ": 12, "RU": 35, "GB": 78, "FI": 32, "SG": 94, "SE": 9, "CH": 12, "TW": 14, "ZA": 6, "FR": 38, "LT": 13, "ES": 14, "HK": 36, "JP": 42, "TH": 5, "MY": 3, "CN": 10, "IE": 12, "IT": 12, "EE": 9, "KZ": 13, "TR": 8, "IN": 9, "NO": 16, "DK": 3, "BY": 2, "LV": 17, "AE": 2, "MD": 4, "VN": 1, "AT": 3, "PH": 1, "AU": 6, "SC": 5, "RO": 6, "AR": 2, "BG": 7, "BR": 8, "CZ": 6, "IR": 2, "PE": 1, "UA": 5, "AL": 4, "SK": 2, "GR": 1, "AM": 1, "CY": 1, "SA": 1, "AF": 1, "BZ": 2, "CR": 1, "IL": 3, "VG": 1, "HU": 1, "KG": 1, "MX": 4, "DO": 1, "RS": 1, "CO": 1}` |
| **Line type mix** | `{"proxy": 453, "home": 165, "dc": 1019, "mobile": 9}` |

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
