# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-14 22:09:01](https://img.shields.io/badge/updated-2026--10--14_22%3A09%3A01-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10062.4s](https://img.shields.io/badge/elapsed-10062.4s-lightgrey)
![profiles: 1130](https://img.shields.io/badge/profiles-1130-blue)
![live_hits: 1130](https://img.shields.io/badge/live__hits-1130-brightgreen)
![live_fail: 77134](https://img.shields.io/badge/live__fail-77134-orange)
![kept: 783](https://img.shields.io/badge/kept-783-blue)
![new: 347](https://img.shields.io/badge/new-347-success)
![dropped: 595](https://img.shields.io/badge/dropped-595-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-14 22:09:01 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10062.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `408937` |
| **Live PASS (pool hits)** | `1130` |
| **Live FAIL** | `77134` |
| **History retained** | `783` |
| **New PASS** | `347` |
| **History dropped** | `595` |
| **Previous public** | `1378` |
| **Published profiles (deduped)** | `1130` |
| **Share links (exportable)** | `943` |
| **YAML proxies (exportable)** | `943` |
| **Protocol mix** | `{"vless": 498, "shadowsocks": 240, "hysteria2": 96, "trojan": 52, "vmess": 57}` |
| **Country mix** | `{"US": 146, "GB": 23, "RU": 28, "NL": 167, "HK": 31, "DE": 63, "KR": 35, "FR": 21, "RO": 5, "ZA": 3, "CH": 44, "SG": 39, "JP": 28, "IN": 9, "CA": 145, "PL": 21, "TW": 5, "TR": 6, "EE": 6, "TH": 3, "SE": 12, "FI": 14, "IT": 15, "MY": 8, "ME": 3, "LV": 6, "LT": 10, "AM": 1, "ID": 2, "SC": 1, "CL": 1, "NO": 1, "KZ": 4, "AU": 4, "BR": 3, "ES": 11, "AE": 2, "MD": 1, "CZ": 2, "GR": 1, "AL": 2, "DK": 1, "MX": 1, "VN": 1, "IR": 1, "SA": 1, "BG": 7, "UA": 1}` |
| **Line type mix** | `{"dc": 479, "proxy": 334, "home": 87, "mobile": 45}` |

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
