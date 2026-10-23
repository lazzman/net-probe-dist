# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-23 22:13:41](https://img.shields.io/badge/updated-2026--10--23_22%3A13%3A41-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10995.1s](https://img.shields.io/badge/elapsed-10995.1s-lightgrey)
![profiles: 1183](https://img.shields.io/badge/profiles-1183-blue)
![live_hits: 1183](https://img.shields.io/badge/live__hits-1183-brightgreen)
![live_fail: 85662](https://img.shields.io/badge/live__fail-85662-orange)
![kept: 860](https://img.shields.io/badge/kept-860-blue)
![new: 323](https://img.shields.io/badge/new-323-success)
![dropped: 483](https://img.shields.io/badge/dropped-483-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-23 22:13:41 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10995.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `413054` |
| **Live PASS (pool hits)** | `1183` |
| **Live FAIL** | `85662` |
| **History retained** | `860` |
| **New PASS** | `323` |
| **History dropped** | `483` |
| **Previous public** | `1343` |
| **Published profiles (deduped)** | `1183` |
| **Share links (exportable)** | `988` |
| **YAML proxies (exportable)** | `988` |
| **Protocol mix** | `{"shadowsocks": 240, "hysteria2": 98, "trojan": 92, "vless": 491, "vmess": 67}` |
| **Country mix** | `{"GB": 36, "IT": 14, "US": 139, "NL": 157, "PL": 8, "DE": 68, "SE": 6, "HK": 40, "NO": 1, "ZA": 2, "CH": 37, "CA": 212, "JP": 31, "CZ": 3, "RU": 18, "KR": 21, "IN": 9, "SG": 44, "TH": 2, "LV": 13, "AT": 1, "ME": 2, "FR": 27, "EE": 2, "TW": 7, "FI": 13, "BY": 6, "IR": 3, "BG": 6, "AE": 3, "ES": 9, "UA": 3, "AM": 2, "KZ": 4, "CL": 1, "RO": 4, "AL": 1, "AU": 4, "BR": 2, "PT": 1, "IE": 2, "SC": 3, "MY": 3, "CW": 1, "TR": 4, "RS": 1, "GR": 1, "MD": 2, "VN": 1, "ID": 1, "IL": 2, "DK": 1, "LT": 6, "SA": 1}` |
| **Line type mix** | `{"mobile": 48, "dc": 555, "proxy": 304, "home": 84}` |

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
