# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-12 11:21:07](https://img.shields.io/badge/updated-2026--11--12_11%3A21%3A07-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11292.5s](https://img.shields.io/badge/elapsed-11292.5s-lightgrey)
![profiles: 1669](https://img.shields.io/badge/profiles-1669-blue)
![live_hits: 1669](https://img.shields.io/badge/live__hits-1669-brightgreen)
![live_fail: 87020](https://img.shields.io/badge/live__fail-87020-orange)
![kept: 985](https://img.shields.io/badge/kept-985-blue)
![new: 684](https://img.shields.io/badge/new-684-success)
![dropped: 116](https://img.shields.io/badge/dropped-116-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-12 11:21:07 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11292.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `400289` |
| **Live PASS (pool hits)** | `1669` |
| **Live FAIL** | `87020` |
| **History retained** | `985` |
| **New PASS** | `684` |
| **History dropped** | `116` |
| **Previous public** | `1101` |
| **Published profiles (deduped)** | `1669` |
| **Share links (exportable)** | `1462` |
| **YAML proxies (exportable)** | `1462` |
| **Protocol mix** | `{"hysteria2": 145, "shadowsocks": 369, "trojan": 121, "vless": 718, "vmess": 109}` |
| **Country mix** | `{"PL": 63, "DE": 76, "CA": 324, "US": 342, "NL": 153, "HK": 27, "AL": 3, "ZA": 4, "AT": 5, "IE": 1, "RO": 4, "GB": 41, "ES": 27, "BG": 8, "JP": 37, "FI": 11, "RU": 35, "IN": 7, "SE": 13, "IT": 25, "SG": 53, "FR": 45, "CH": 54, "BR": 4, "CL": 2, "EE": 2, "BY": 6, "KR": 14, "IR": 4, "CR": 5, "LV": 14, "AE": 3, "IL": 2, "GR": 1, "AU": 6, "SA": 1, "SC": 2, "TW": 5, "MY": 3, "MX": 3, "TH": 4, "LY": 1, "CZ": 2, "KZ": 1, "DK": 1, "VN": 1, "SK": 3, "ID": 1, "CN": 1, "TR": 3, "LT": 8, "NG": 1, "UA": 1, "MD": 1, "CW": 1}` |
| **Line type mix** | `{"dc": 794, "mobile": 130, "proxy": 464, "home": 77}` |

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
