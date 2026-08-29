# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-30 07:13:57](https://img.shields.io/badge/updated-2026--08--30_07%3A13%3A57-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9544.0s](https://img.shields.io/badge/elapsed-9544.0s-lightgrey)
![profiles: 1786](https://img.shields.io/badge/profiles-1786-blue)
![live_hits: 1786](https://img.shields.io/badge/live__hits-1786-brightgreen)
![live_fail: 70862](https://img.shields.io/badge/live__fail-70862-orange)
![kept: 1188](https://img.shields.io/badge/kept-1188-blue)
![new: 598](https://img.shields.io/badge/new-598-success)
![dropped: 269](https://img.shields.io/badge/dropped-269-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-30 07:13:57 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9544.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `418792` |
| **Live PASS (pool hits)** | `1786` |
| **Live FAIL** | `70862` |
| **History retained** | `1188` |
| **New PASS** | `598` |
| **History dropped** | `269` |
| **Previous public** | `1457` |
| **Published profiles (deduped)** | `1786` |
| **Share links (exportable)** | `1427` |
| **YAML proxies (exportable)** | `1427` |
| **Protocol mix** | `{"vless": 854, "shadowsocks": 296, "hysteria2": 187, "trojan": 24, "vmess": 66}` |
| **Country mix** | `{"CA": 228, "NL": 220, "KR": 25, "MD": 3, "PL": 23, "DE": 103, "DZ": 10, "IT": 7, "RU": 28, "GB": 68, "US": 230, "FI": 28, "SG": 98, "SE": 9, "TW": 27, "ID": 1, "IE": 9, "FR": 37, "LT": 13, "NO": 16, "RO": 3, "ES": 10, "ZA": 3, "HK": 34, "MY": 5, "TH": 4, "CN": 10, "JP": 74, "EE": 6, "IN": 8, "TR": 7, "KZ": 10, "CZ": 4, "DK": 1, "AT": 3, "UA": 4, "CH": 4, "AU": 5, "LV": 12, "BR": 12, "BG": 6, "AM": 1, "PH": 1, "SC": 1, "AE": 1, "SK": 1, "AL": 3, "AR": 2, "BY": 1, "PE": 1, "CO": 2, "GR": 2, "VN": 1, "SA": 1, "MX": 2}` |
| **Line type mix** | `{"dc": 915, "proxy": 399, "home": 104, "mobile": 10}` |

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
