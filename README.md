# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-17 21:06:36](https://img.shields.io/badge/updated-2026--10--17_21%3A06%3A36-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10202.6s](https://img.shields.io/badge/elapsed-10202.6s-lightgrey)
![profiles: 1172](https://img.shields.io/badge/profiles-1172-blue)
![live_hits: 1172](https://img.shields.io/badge/live__hits-1172-brightgreen)
![live_fail: 77949](https://img.shields.io/badge/live__fail-77949-orange)
![kept: 857](https://img.shields.io/badge/kept-857-blue)
![new: 315](https://img.shields.io/badge/new-315-success)
![dropped: 580](https://img.shields.io/badge/dropped-580-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-17 21:06:36 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10202.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `414116` |
| **Live PASS (pool hits)** | `1172` |
| **Live FAIL** | `77949` |
| **History retained** | `857` |
| **New PASS** | `315` |
| **History dropped** | `580` |
| **Previous public** | `1437` |
| **Published profiles (deduped)** | `1172` |
| **Share links (exportable)** | `996` |
| **YAML proxies (exportable)** | `996` |
| **Protocol mix** | `{"vless": 511, "shadowsocks": 222, "hysteria2": 100, "trojan": 104, "vmess": 59}` |
| **Country mix** | `{"NL": 178, "US": 145, "PL": 21, "ZA": 2, "GB": 27, "RU": 26, "AU": 3, "HK": 25, "RO": 4, "DE": 68, "CH": 42, "CA": 194, "JP": 32, "KR": 30, "CZ": 4, "IN": 9, "TH": 2, "CL": 1, "SG": 50, "ES": 8, "AT": 1, "ME": 5, "CR": 1, "TW": 5, "KH": 1, "FI": 13, "FR": 23, "EE": 4, "BY": 6, "ID": 3, "HU": 2, "MD": 3, "LV": 8, "SE": 6, "AE": 4, "IT": 9, "LT": 5, "AM": 1, "KZ": 5, "AL": 2, "TR": 6, "UA": 1, "SC": 2, "NZ": 1, "BZ": 1, "CW": 1, "GR": 1, "VN": 2, "MY": 1, "CN": 2, "SA": 1, "BG": 1, "BR": 1}` |
| **Line type mix** | `{"proxy": 316, "dc": 556, "home": 86, "mobile": 41}` |

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
