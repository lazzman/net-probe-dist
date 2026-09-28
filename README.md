# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-28 23:57:19](https://img.shields.io/badge/updated-2026--09--28_23%3A57%3A19-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10288.6s](https://img.shields.io/badge/elapsed-10288.6s-lightgrey)
![profiles: 1324](https://img.shields.io/badge/profiles-1324-blue)
![live_hits: 1324](https://img.shields.io/badge/live__hits-1324-brightgreen)
![live_fail: 77896](https://img.shields.io/badge/live__fail-77896-orange)
![kept: 998](https://img.shields.io/badge/kept-998-blue)
![new: 326](https://img.shields.io/badge/new-326-success)
![dropped: 1035](https://img.shields.io/badge/dropped-1035-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-28 23:57:19 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10288.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `433082` |
| **Live PASS (pool hits)** | `1324` |
| **Live FAIL** | `77896` |
| **History retained** | `998` |
| **New PASS** | `326` |
| **History dropped** | `1035` |
| **Previous public** | `2033` |
| **Published profiles (deduped)** | `1324` |
| **Share links (exportable)** | `1172` |
| **YAML proxies (exportable)** | `1172` |
| **Protocol mix** | `{"vless": 652, "shadowsocks": 287, "trojan": 30, "vmess": 78, "hysteria2": 125}` |
| **Country mix** | `{"US": 228, "PL": 29, "NL": 155, "CA": 229, "ZA": 15, "ES": 9, "GB": 51, "CZ": 5, "DE": 63, "RU": 31, "TW": 6, "ID": 1, "SG": 45, "FR": 29, "RO": 6, "CH": 8, "IT": 13, "JP": 37, "SE": 12, "KR": 30, "AT": 2, "FI": 15, "AE": 2, "KZ": 5, "TH": 2, "IN": 12, "HK": 34, "EE": 8, "GE": 2, "AU": 5, "UA": 3, "AD": 1, "LT": 11, "MY": 1, "NO": 1, "IR": 2, "SA": 1, "DZ": 28, "AL": 2, "SC": 3, "LV": 12, "TR": 3, "CW": 1, "GT": 1, "CO": 1, "GR": 1, "AM": 1, "IL": 2, "BE": 1, "MX": 1, "VN": 1, "BG": 5, "CR": 1}` |
| **Line type mix** | `{"proxy": 387, "dc": 685, "mobile": 19, "home": 82}` |

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
