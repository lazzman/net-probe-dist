# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-12 20:57:28](https://img.shields.io/badge/updated-2026--09--12_20%3A57%3A28-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9689.0s](https://img.shields.io/badge/elapsed-9689.0s-lightgrey)
![profiles: 1883](https://img.shields.io/badge/profiles-1883-blue)
![live_hits: 1884](https://img.shields.io/badge/live__hits-1884-brightgreen)
![live_fail: 73714](https://img.shields.io/badge/live__fail-73714-orange)
![kept: 1258](https://img.shields.io/badge/kept-1258-blue)
![new: 626](https://img.shields.io/badge/new-626-success)
![dropped: 1061](https://img.shields.io/badge/dropped-1061-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-12 20:57:28 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9689.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `421933` |
| **Live PASS (pool hits)** | `1884` |
| **Live FAIL** | `73714` |
| **History retained** | `1258` |
| **New PASS** | `626` |
| **History dropped** | `1061` |
| **Previous public** | `2319` |
| **Published profiles (deduped)** | `1883` |
| **Share links (exportable)** | `1459` |
| **YAML proxies (exportable)** | `1459` |
| **Protocol mix** | `{"vless": 963, "vmess": 63, "hysteria2": 144, "trojan": 54, "shadowsocks": 235}` |
| **Country mix** | `{"PL": 34, "GB": 76, "JP": 32, "NL": 206, "CA": 479, "SG": 37, "DE": 61, "AU": 4, "RU": 18, "IN": 8, "DZ": 24, "FI": 24, "TW": 16, "ID": 1, "AE": 2, "US": 190, "NO": 8, "FR": 31, "RO": 6, "ES": 13, "MY": 4, "KR": 32, "IT": 14, "DK": 1, "AT": 5, "HR": 1, "KZ": 7, "EE": 7, "HK": 48, "UA": 4, "GR": 2, "TH": 2, "GT": 1, "SE": 12, "LT": 15, "TR": 2, "CZ": 3, "SA": 1, "AM": 1, "UZ": 2, "ZA": 3, "CL": 1, "SC": 2, "BG": 1, "CH": 1, "BZ": 1, "LV": 7, "CO": 1, "IE": 1, "CN": 2, "ZZ": 1, "VG": 1, "CY": 1, "IR": 1, "AL": 1, "CR": 1}` |
| **Line type mix** | `{"proxy": 388, "dc": 985, "home": 79, "mobile": 7, "unknown": 1}` |

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
