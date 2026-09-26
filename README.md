# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-27 02:48:05](https://img.shields.io/badge/updated-2026--09--27_02%3A48%3A05-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10162.4s](https://img.shields.io/badge/elapsed-10162.4s-lightgrey)
![profiles: 1251](https://img.shields.io/badge/profiles-1251-blue)
![live_hits: 1251](https://img.shields.io/badge/live__hits-1251-brightgreen)
![live_fail: 77322](https://img.shields.io/badge/live__fail-77322-orange)
![kept: 944](https://img.shields.io/badge/kept-944-blue)
![new: 307](https://img.shields.io/badge/new-307-success)
![dropped: 245](https://img.shields.io/badge/dropped-245-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-27 02:48:05 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10162.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `434633` |
| **Live PASS (pool hits)** | `1251` |
| **Live FAIL** | `77322` |
| **History retained** | `944` |
| **New PASS** | `307` |
| **History dropped** | `245` |
| **Previous public** | `1189` |
| **Published profiles (deduped)** | `1251` |
| **Share links (exportable)** | `1113` |
| **YAML proxies (exportable)** | `1113` |
| **Protocol mix** | `{"shadowsocks": 280, "vless": 624, "hysteria2": 111, "vmess": 78, "trojan": 20}` |
| **Country mix** | `{"CZ": 3, "CA": 213, "KR": 30, "US": 217, "PL": 26, "DE": 60, "GB": 43, "ZA": 5, "NL": 145, "ID": 1, "FR": 33, "IE": 2, "NO": 4, "CH": 7, "ES": 11, "JP": 44, "SE": 22, "IT": 16, "CL": 11, "IN": 14, "AT": 4, "IR": 3, "UA": 2, "HK": 24, "FI": 22, "RU": 26, "TW": 7, "TR": 3, "SG": 27, "AE": 3, "EE": 8, "BG": 8, "DK": 2, "MX": 1, "RO": 3, "SA": 1, "MY": 1, "AL": 1, "DZ": 28, "SC": 2, "LV": 10, "KZ": 5, "AU": 2, "CY": 3, "AM": 1, "TH": 1, "LT": 7, "BV": 1, "ZZ": 1, "CR": 1}` |
| **Line type mix** | `{"proxy": 384, "dc": 658, "mobile": 13, "home": 59, "unknown": 1}` |

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
