# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-12 08:26:20](https://img.shields.io/badge/updated-2026--10--12_08%3A26%3A20-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10084.6s](https://img.shields.io/badge/elapsed-10084.6s-lightgrey)
![profiles: 1606](https://img.shields.io/badge/profiles-1606-blue)
![live_hits: 1606](https://img.shields.io/badge/live__hits-1606-brightgreen)
![live_fail: 76683](https://img.shields.io/badge/live__fail-76683-orange)
![kept: 949](https://img.shields.io/badge/kept-949-blue)
![new: 657](https://img.shields.io/badge/new-657-success)
![dropped: 224](https://img.shields.io/badge/dropped-224-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-12 08:26:20 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10084.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `413661` |
| **Live PASS (pool hits)** | `1606` |
| **Live FAIL** | `76683` |
| **History retained** | `949` |
| **New PASS** | `657` |
| **History dropped** | `224` |
| **Previous public** | `1173` |
| **Published profiles (deduped)** | `1606` |
| **Share links (exportable)** | `1323` |
| **YAML proxies (exportable)** | `1323` |
| **Protocol mix** | `{"vless": 702, "shadowsocks": 279, "hysteria2": 147, "trojan": 133, "vmess": 62}` |
| **Country mix** | `{"US": 170, "ZA": 6, "GB": 31, "NL": 194, "TR": 6, "CA": 220, "ID": 4, "DE": 99, "SG": 60, "FR": 33, "IE": 7, "IN": 11, "RO": 6, "NO": 1, "CH": 44, "JP": 69, "RU": 38, "KR": 53, "TH": 3, "HK": 63, "MX": 1, "UA": 1, "LV": 15, "ME": 6, "SE": 10, "EE": 11, "TW": 5, "PL": 23, "AE": 5, "FI": 21, "KZ": 6, "IT": 17, "IR": 7, "IL": 1, "MY": 12, "AM": 2, "BG": 8, "ES": 8, "SA": 1, "BR": 3, "CZ": 3, "AU": 4, "GR": 2, "AL": 2, "VN": 3, "LT": 12, "DK": 2, "AT": 2, "CN": 15, "CR": 1, "BZ": 1}` |
| **Line type mix** | `{"dc": 778, "proxy": 373, "home": 134, "mobile": 43}` |

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
