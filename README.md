# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-06 00:42:48](https://img.shields.io/badge/updated-2026--10--06_00%3A42%3A48-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10382.2s](https://img.shields.io/badge/elapsed-10382.2s-lightgrey)
![profiles: 1351](https://img.shields.io/badge/profiles-1351-blue)
![live_hits: 1352](https://img.shields.io/badge/live__hits-1352-brightgreen)
![live_fail: 78757](https://img.shields.io/badge/live__fail-78757-orange)
![kept: 1005](https://img.shields.io/badge/kept-1005-blue)
![new: 347](https://img.shields.io/badge/new-347-success)
![dropped: 862](https://img.shields.io/badge/dropped-862-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-06 00:42:48 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10382.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `433722` |
| **Live PASS (pool hits)** | `1352` |
| **Live FAIL** | `78757` |
| **History retained** | `1005` |
| **New PASS** | `347` |
| **History dropped** | `862` |
| **Previous public** | `1867` |
| **Published profiles (deduped)** | `1351` |
| **Share links (exportable)** | `1168` |
| **YAML proxies (exportable)** | `1168` |
| **Protocol mix** | `{"vless": 633, "vmess": 93, "shadowsocks": 259, "hysteria2": 89, "trojan": 94}` |
| **Country mix** | `{"US": 201, "CA": 280, "ZA": 4, "GB": 31, "NL": 150, "DE": 73, "FR": 33, "IE": 6, "ES": 9, "CH": 8, "FI": 12, "JP": 49, "IN": 12, "SG": 30, "KR": 33, "HK": 81, "HU": 1, "AT": 2, "RU": 16, "PL": 18, "TH": 2, "IT": 17, "EE": 5, "GT": 1, "SE": 4, "KZ": 5, "CL": 12, "TR": 4, "MY": 10, "TW": 3, "ZZ": 1, "NO": 2, "BR": 2, "SA": 1, "AU": 5, "MX": 1, "AL": 2, "AE": 3, "GR": 1, "VN": 1, "ID": 1, "AM": 2, "RO": 1, "LV": 11, "LT": 7, "BG": 3, "CN": 17, "CR": 1}` |
| **Line type mix** | `{"dc": 727, "proxy": 354, "home": 77, "mobile": 15, "unknown": 1}` |

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
