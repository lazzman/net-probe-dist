# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-13 07:00:46](https://img.shields.io/badge/updated-2026--09--13_07%3A00%3A46-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9624.4s](https://img.shields.io/badge/elapsed-9624.4s-lightgrey)
![profiles: 1544](https://img.shields.io/badge/profiles-1544-blue)
![live_hits: 1544](https://img.shields.io/badge/live__hits-1544-brightgreen)
![live_fail: 73933](https://img.shields.io/badge/live__fail-73933-orange)
![kept: 1123](https://img.shields.io/badge/kept-1123-blue)
![new: 421](https://img.shields.io/badge/new-421-success)
![dropped: 152](https://img.shields.io/badge/dropped-152-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-13 07:00:46 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9624.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `420817` |
| **Live PASS (pool hits)** | `1544` |
| **Live FAIL** | `73933` |
| **History retained** | `1123` |
| **New PASS** | `421` |
| **History dropped** | `152` |
| **Previous public** | `1275` |
| **Published profiles (deduped)** | `1544` |
| **Share links (exportable)** | `1239` |
| **YAML proxies (exportable)** | `1239` |
| **Protocol mix** | `{"trojan": 35, "hysteria2": 143, "vmess": 59, "vless": 774, "shadowsocks": 228}` |
| **Country mix** | `{"US": 174, "LT": 12, "CA": 347, "DE": 50, "GB": 68, "DZ": 24, "RU": 26, "JP": 33, "FI": 20, "SG": 29, "NL": 193, "NO": 7, "FR": 26, "ID": 1, "PL": 34, "ES": 12, "RO": 6, "MX": 1, "DK": 1, "IT": 10, "HR": 1, "TW": 14, "EE": 6, "IN": 4, "HK": 48, "AE": 3, "TH": 4, "UA": 5, "TR": 3, "GR": 2, "SE": 10, "CZ": 2, "GT": 1, "UZ": 2, "SA": 1, "MY": 3, "AM": 1, "KR": 22, "ZA": 4, "KZ": 7, "BR": 1, "SC": 2, "CH": 2, "LV": 5, "AU": 3, "CO": 1, "PT": 3, "IE": 2, "AT": 1, "ZZ": 1, "AL": 1, "CL": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 803, "proxy": 359, "home": 72, "mobile": 6, "unknown": 1}` |

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
