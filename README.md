# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-25 07:26:07](https://img.shields.io/badge/updated-2026--10--25_07%3A26%3A07-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11010.6s](https://img.shields.io/badge/elapsed-11010.6s-lightgrey)
![profiles: 1076](https://img.shields.io/badge/profiles-1076-blue)
![live_hits: 1076](https://img.shields.io/badge/live__hits-1076-brightgreen)
![live_fail: 86089](https://img.shields.io/badge/live__fail-86089-orange)
![kept: 796](https://img.shields.io/badge/kept-796-blue)
![new: 280](https://img.shields.io/badge/new-280-success)
![dropped: 159](https://img.shields.io/badge/dropped-159-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-25 07:26:07 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11010.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `417075` |
| **Live PASS (pool hits)** | `1076` |
| **Live FAIL** | `86089` |
| **History retained** | `796` |
| **New PASS** | `280` |
| **History dropped** | `159` |
| **Previous public** | `955` |
| **Published profiles (deduped)** | `1076` |
| **Share links (exportable)** | `923` |
| **YAML proxies (exportable)** | `923` |
| **Protocol mix** | `{"shadowsocks": 253, "vless": 401, "hysteria2": 118, "trojan": 86, "vmess": 65}` |
| **Country mix** | `{"IT": 14, "NL": 150, "US": 143, "GB": 26, "CA": 169, "DE": 50, "HK": 29, "KR": 27, "RO": 3, "ZA": 3, "CH": 48, "IE": 3, "JP": 22, "DK": 1, "IN": 11, "TH": 2, "ES": 14, "HU": 1, "AT": 1, "LT": 10, "FR": 26, "RU": 19, "EE": 5, "SG": 44, "PL": 10, "TR": 6, "FI": 10, "SE": 4, "BY": 6, "AE": 3, "CZ": 2, "IL": 3, "CN": 3, "TW": 3, "UA": 3, "NO": 1, "AU": 4, "BG": 8, "IR": 8, "KZ": 2, "BR": 1, "ID": 2, "LV": 12, "AL": 1, "SC": 3, "MY": 2, "RS": 1, "GR": 1, "AM": 2, "SA": 1, "ME": 1}` |
| **Line type mix** | `{"dc": 501, "proxy": 298, "mobile": 58, "home": 67}` |

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
