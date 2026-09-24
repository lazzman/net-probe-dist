# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-25 03:29:07](https://img.shields.io/badge/updated-2026--09--25_03%3A29%3A07-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10088.9s](https://img.shields.io/badge/elapsed-10088.9s-lightgrey)
![profiles: 1487](https://img.shields.io/badge/profiles-1487-blue)
![live_hits: 1487](https://img.shields.io/badge/live__hits-1487-brightgreen)
![live_fail: 76992](https://img.shields.io/badge/live__fail-76992-orange)
![kept: 965](https://img.shields.io/badge/kept-965-blue)
![new: 522](https://img.shields.io/badge/new-522-success)
![dropped: 269](https://img.shields.io/badge/dropped-269-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-25 03:29:07 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10088.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `434884` |
| **Live PASS (pool hits)** | `1487` |
| **Live FAIL** | `76992` |
| **History retained** | `965` |
| **New PASS** | `522` |
| **History dropped** | `269` |
| **Previous public** | `1234` |
| **Published profiles (deduped)** | `1487` |
| **Share links (exportable)** | `1137` |
| **YAML proxies (exportable)** | `1137` |
| **Protocol mix** | `{"vless": 641, "vmess": 88, "shadowsocks": 272, "hysteria2": 110, "trojan": 26}` |
| **Country mix** | `{"CA": 218, "ES": 11, "US": 215, "ZA": 3, "KR": 23, "SG": 32, "GB": 71, "DE": 47, "NL": 160, "RU": 26, "FR": 35, "IE": 1, "RO": 4, "NO": 2, "CH": 6, "JP": 42, "SE": 15, "IN": 15, "DK": 2, "CZ": 2, "CL": 2, "PL": 24, "FI": 21, "HK": 36, "TR": 3, "TW": 8, "TH": 2, "AT": 3, "IT": 16, "AL": 1, "MD": 2, "AM": 1, "MY": 2, "CN": 1, "DZ": 25, "IR": 3, "SC": 2, "EE": 6, "KZ": 6, "AE": 2, "AU": 3, "BG": 11, "CY": 1, "GT": 1, "CO": 1, "LT": 8, "IL": 3, "IQ": 1, "LV": 10, "GR": 1, "SA": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 686, "mobile": 16, "proxy": 378, "home": 58}` |

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
