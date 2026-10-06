# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-06 23:48:08](https://img.shields.io/badge/updated-2026--10--06_23%3A48%3A08-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10357.6s](https://img.shields.io/badge/elapsed-10357.6s-lightgrey)
![profiles: 1353](https://img.shields.io/badge/profiles-1353-blue)
![live_hits: 1353](https://img.shields.io/badge/live__hits-1353-brightgreen)
![live_fail: 78725](https://img.shields.io/badge/live__fail-78725-orange)
![kept: 1004](https://img.shields.io/badge/kept-1004-blue)
![new: 349](https://img.shields.io/badge/new-349-success)
![dropped: 711](https://img.shields.io/badge/dropped-711-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-06 23:48:08 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10357.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `432779` |
| **Live PASS (pool hits)** | `1353` |
| **Live FAIL** | `78725` |
| **History retained** | `1004` |
| **New PASS** | `349` |
| **History dropped** | `711` |
| **Previous public** | `1715` |
| **Published profiles (deduped)** | `1353` |
| **Share links (exportable)** | `1167` |
| **YAML proxies (exportable)** | `1167` |
| **Protocol mix** | `{"vless": 623, "vmess": 93, "shadowsocks": 260, "hysteria2": 98, "trojan": 93}` |
| **Country mix** | `{"US": 200, "CA": 269, "GB": 29, "NL": 164, "FR": 38, "DE": 83, "ZA": 3, "IE": 5, "RO": 5, "ES": 8, "CH": 11, "HK": 39, "FI": 15, "JP": 50, "SG": 38, "KR": 29, "IN": 10, "AT": 1, "RU": 20, "TR": 3, "ID": 2, "TH": 2, "EE": 8, "IT": 18, "PL": 19, "CL": 12, "TW": 3, "MY": 9, "AU": 4, "NO": 1, "SA": 1, "AM": 2, "BR": 1, "LV": 12, "BE": 1, "AL": 2, "SE": 4, "AE": 3, "KZ": 4, "CY": 2, "ZZ": 1, "GR": 1, "CN": 19, "SC": 2, "MD": 1, "IR": 1, "BG": 6, "LT": 8, "VN": 1}` |
| **Line type mix** | `{"dc": 729, "proxy": 355, "home": 69, "mobile": 16, "unknown": 1}` |

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
