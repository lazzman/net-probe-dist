# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-07 09:17:22](https://img.shields.io/badge/updated-2026--10--07_09%3A17%3A22-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10065.4s](https://img.shields.io/badge/elapsed-10065.4s-lightgrey)
![profiles: 1697](https://img.shields.io/badge/profiles-1697-blue)
![live_hits: 1697](https://img.shields.io/badge/live__hits-1697-brightgreen)
![live_fail: 76153](https://img.shields.io/badge/live__fail-76153-orange)
![kept: 1005](https://img.shields.io/badge/kept-1005-blue)
![new: 692](https://img.shields.io/badge/new-692-success)
![dropped: 162](https://img.shields.io/badge/dropped-162-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-07 09:17:22 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10065.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `409427` |
| **Live PASS (pool hits)** | `1697` |
| **Live FAIL** | `76153` |
| **History retained** | `1005` |
| **New PASS** | `692` |
| **History dropped** | `162` |
| **Previous public** | `1167` |
| **Published profiles (deduped)** | `1697` |
| **Share links (exportable)** | `1468` |
| **YAML proxies (exportable)** | `1468` |
| **Protocol mix** | `{"vless": 908, "shadowsocks": 275, "vmess": 93, "hysteria2": 96, "trojan": 96}` |
| **Country mix** | `{"US": 226, "CA": 409, "ZA": 5, "SG": 50, "GB": 34, "FR": 35, "NL": 172, "DE": 100, "ID": 5, "IE": 4, "CH": 9, "RO": 5, "ES": 11, "FI": 25, "JP": 62, "IN": 12, "IT": 22, "KR": 42, "PL": 20, "HU": 1, "AT": 1, "SC": 3, "TR": 6, "RU": 20, "TH": 2, "SE": 5, "EE": 8, "GR": 2, "KZ": 5, "MD": 3, "CL": 12, "SA": 1, "TW": 6, "HK": 55, "CN": 18, "BR": 2, "NO": 1, "AM": 3, "BG": 7, "AE": 4, "BE": 2, "AL": 3, "AU": 5, "CY": 2, "LV": 13, "MY": 9, "LT": 9, "MX": 1, "VN": 2, "BZ": 3, "UA": 2, "UZ": 2, "CR": 1, "CZ": 1, "RS": 2, "DK": 1, "ME": 2}` |
| **Line type mix** | `{"dc": 974, "proxy": 391, "home": 90, "mobile": 18}` |

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
