# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-14 01:14:11](https://img.shields.io/badge/updated-2026--11--14_01%3A14%3A11-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11409.2s](https://img.shields.io/badge/elapsed-11409.2s-lightgrey)
![profiles: 1153](https://img.shields.io/badge/profiles-1153-blue)
![live_hits: 1153](https://img.shields.io/badge/live__hits-1153-brightgreen)
![live_fail: 87756](https://img.shields.io/badge/live__fail-87756-orange)
![kept: 887](https://img.shields.io/badge/kept-887-blue)
![new: 266](https://img.shields.io/badge/new-266-success)
![dropped: 159](https://img.shields.io/badge/dropped-159-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-14 01:14:11 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11409.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `400891` |
| **Live PASS (pool hits)** | `1153` |
| **Live FAIL** | `87756` |
| **History retained** | `887` |
| **New PASS** | `266` |
| **History dropped** | `159` |
| **Previous public** | `1046` |
| **Published profiles (deduped)** | `1153` |
| **Share links (exportable)** | `1034` |
| **YAML proxies (exportable)** | `1034` |
| **Protocol mix** | `{"shadowsocks": 380, "hysteria2": 129, "trojan": 92, "vless": 338, "vmess": 95}` |
| **Country mix** | `{"US": 238, "DE": 69, "CA": 98, "NL": 133, "IR": 4, "HK": 22, "GB": 34, "FR": 38, "AT": 4, "NO": 1, "AL": 2, "RO": 5, "ZA": 4, "UA": 3, "IT": 27, "ES": 22, "BG": 18, "JP": 26, "MX": 2, "RU": 19, "SG": 45, "FI": 9, "IN": 7, "CH": 56, "KR": 16, "BR": 3, "CL": 1, "BY": 5, "PL": 60, "SE": 13, "CZ": 1, "IL": 2, "GR": 1, "NE": 2, "TW": 3, "AU": 2, "LV": 12, "AE": 3, "EE": 1, "LT": 10, "VN": 1, "SK": 2, "MY": 2, "TR": 5, "TH": 1, "CN": 1, "SA": 1, "GE": 1}` |
| **Line type mix** | `{"proxy": 432, "dc": 421, "home": 60, "mobile": 122}` |

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
