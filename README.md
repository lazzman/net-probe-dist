# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-13 01:51:53](https://img.shields.io/badge/updated-2026--09--13_01%3A51%3A53-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9655.2s](https://img.shields.io/badge/elapsed-9655.2s-lightgrey)
![profiles: 1608](https://img.shields.io/badge/profiles-1608-blue)
![live_hits: 1610](https://img.shields.io/badge/live__hits-1610-brightgreen)
![live_fail: 73781](https://img.shields.io/badge/live__fail-73781-orange)
![kept: 1152](https://img.shields.io/badge/kept-1152-blue)
![new: 458](https://img.shields.io/badge/new-458-success)
![dropped: 307](https://img.shields.io/badge/dropped-307-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-13 01:51:53 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9655.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `420915` |
| **Live PASS (pool hits)** | `1610` |
| **Live FAIL** | `73781` |
| **History retained** | `1152` |
| **New PASS** | `458` |
| **History dropped** | `307` |
| **Previous public** | `1459` |
| **Published profiles (deduped)** | `1608` |
| **Share links (exportable)** | `1275` |
| **YAML proxies (exportable)** | `1275` |
| **Protocol mix** | `{"vless": 797, "hysteria2": 143, "vmess": 64, "shadowsocks": 231, "trojan": 40}` |
| **Country mix** | `{"JP": 32, "IN": 9, "AU": 5, "DE": 60, "GB": 73, "RU": 18, "FI": 23, "DZ": 24, "SG": 33, "NL": 202, "CA": 349, "TW": 15, "ID": 1, "FR": 23, "NO": 7, "PL": 37, "ES": 12, "US": 180, "KR": 25, "IT": 10, "AT": 3, "HR": 1, "KZ": 6, "EE": 7, "HK": 51, "AE": 1, "TH": 4, "UA": 3, "GR": 2, "SE": 8, "CZ": 2, "GT": 1, "TR": 5, "LT": 12, "ZZ": 2, "RO": 5, "SA": 1, "MY": 3, "AM": 1, "UZ": 2, "ZA": 3, "BR": 1, "CL": 1, "SC": 2, "CH": 2, "PT": 1, "IE": 1, "AL": 1, "LV": 6, "CR": 1}` |
| **Line type mix** | `{"proxy": 375, "dc": 822, "home": 72, "mobile": 6, "unknown": 2}` |

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
