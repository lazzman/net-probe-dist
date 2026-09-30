# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-30 22:56:34](https://img.shields.io/badge/updated-2026--09--30_22%3A56%3A34-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10278.9s](https://img.shields.io/badge/elapsed-10278.9s-lightgrey)
![profiles: 1423](https://img.shields.io/badge/profiles-1423-blue)
![live_hits: 1423](https://img.shields.io/badge/live__hits-1423-brightgreen)
![live_fail: 78016](https://img.shields.io/badge/live__fail-78016-orange)
![kept: 1050](https://img.shields.io/badge/kept-1050-blue)
![new: 373](https://img.shields.io/badge/new-373-success)
![dropped: 939](https://img.shields.io/badge/dropped-939-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-30 22:56:34 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10278.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `432176` |
| **Live PASS (pool hits)** | `1423` |
| **Live FAIL** | `78016` |
| **History retained** | `1050` |
| **New PASS** | `373` |
| **History dropped** | `939` |
| **Previous public** | `1989` |
| **Published profiles (deduped)** | `1423` |
| **Share links (exportable)** | `1272` |
| **YAML proxies (exportable)** | `1272` |
| **Protocol mix** | `{"vless": 762, "vmess": 85, "trojan": 41, "shadowsocks": 261, "hysteria2": 123}` |
| **Country mix** | `{"US": 233, "CA": 297, "ES": 13, "IE": 4, "GB": 54, "NL": 155, "FR": 32, "SG": 43, "DE": 73, "ID": 3, "NO": 3, "ZA": 3, "RO": 4, "CH": 10, "JP": 40, "SE": 16, "IN": 15, "AT": 3, "FI": 17, "RU": 21, "LT": 12, "HK": 45, "AE": 3, "TH": 1, "PL": 18, "IT": 16, "UA": 3, "MY": 7, "SK": 2, "TW": 8, "KR": 36, "KZ": 5, "AD": 1, "DZ": 28, "SC": 2, "LV": 2, "EE": 3, "TR": 2, "AU": 4, "GE": 1, "CW": 1, "GT": 1, "GR": 1, "MX": 1, "AL": 2, "CZ": 8, "AM": 2, "CN": 1, "HU": 1, "ZZ": 4, "SA": 1, "BG": 5, "BR": 1, "CR": 1, "CL": 1, "BE": 1, "IR": 2}` |
| **Line type mix** | `{"proxy": 380, "dc": 791, "mobile": 22, "home": 75, "unknown": 4}` |

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
