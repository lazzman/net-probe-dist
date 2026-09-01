# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-02 02:59:33](https://img.shields.io/badge/updated-2026--09--02_02%3A59%3A33-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9811.9s](https://img.shields.io/badge/elapsed-9811.9s-lightgrey)
![profiles: 2118](https://img.shields.io/badge/profiles-2118-blue)
![live_hits: 2118](https://img.shields.io/badge/live__hits-2118-brightgreen)
![live_fail: 73149](https://img.shields.io/badge/live__fail-73149-orange)
![kept: 1286](https://img.shields.io/badge/kept-1286-blue)
![new: 832](https://img.shields.io/badge/new-832-success)
![dropped: 351](https://img.shields.io/badge/dropped-351-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-02 02:59:33 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9811.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `428614` |
| **Live PASS (pool hits)** | `2118` |
| **Live FAIL** | `73149` |
| **History retained** | `1286` |
| **New PASS** | `832` |
| **History dropped** | `351` |
| **Previous public** | `1637` |
| **Published profiles (deduped)** | `2118` |
| **Share links (exportable)** | `1480` |
| **YAML proxies (exportable)** | `1480` |
| **Protocol mix** | `{"hysteria2": 195, "vless": 928, "shadowsocks": 260, "trojan": 19, "vmess": 78}` |
| **Country mix** | `{"PL": 33, "FR": 31, "FI": 31, "NL": 242, "DZ": 16, "US": 247, "IT": 10, "RU": 31, "DE": 89, "GB": 69, "SE": 13, "SG": 81, "TW": 23, "CA": 241, "ES": 9, "ZA": 3, "RO": 7, "JP": 73, "TH": 5, "MY": 4, "CN": 6, "KR": 31, "KZ": 12, "EE": 5, "IN": 8, "CZ": 5, "NO": 17, "TR": 6, "HK": 36, "IR": 1, "DK": 1, "CH": 5, "LV": 14, "UA": 2, "GR": 3, "LT": 12, "MD": 1, "AL": 3, "PH": 3, "ID": 2, "IE": 6, "AU": 5, "BR": 10, "SA": 1, "CO": 5, "HR": 1, "SC": 5, "AR": 2, "JE": 1, "UZ": 2, "BG": 2, "AE": 1, "BY": 1, "SK": 1, "AT": 2, "EG": 1, "AM": 1, "CR": 1, "MX": 2}` |
| **Line type mix** | `{"proxy": 411, "dc": 930, "home": 130, "mobile": 10}` |

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
