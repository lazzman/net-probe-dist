# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-11 23:58:10](https://img.shields.io/badge/updated-2026--08--11_23%3A58%3A10-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10221.9s](https://img.shields.io/badge/elapsed-10221.9s-lightgrey)
![profiles: 1562](https://img.shields.io/badge/profiles-1562-blue)
![live_hits: 1562](https://img.shields.io/badge/live__hits-1562-brightgreen)
![live_fail: 93294](https://img.shields.io/badge/live__fail-93294-orange)
![kept: 930](https://img.shields.io/badge/kept-930-blue)
![new: 632](https://img.shields.io/badge/new-632-success)
![dropped: 664](https://img.shields.io/badge/dropped-664-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-11 23:58:10 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10221.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `448167` |
| **Live PASS (pool hits)** | `1562` |
| **Live FAIL** | `93294` |
| **History retained** | `930` |
| **New PASS** | `632` |
| **History dropped** | `664` |
| **Previous public** | `1594` |
| **Published profiles (deduped)** | `1562` |
| **Share links (exportable)** | `1178` |
| **YAML proxies (exportable)** | `1178` |
| **Protocol mix** | `{"vmess": 71, "shadowsocks": 184, "vless": 769, "hysteria2": 85, "trojan": 69}` |
| **Country mix** | `{"US": 165, "CA": 225, "AU": 4, "NL": 207, "PL": 23, "DE": 78, "FR": 57, "TH": 2, "HK": 40, "RO": 5, "FI": 33, "SG": 24, "TW": 7, "NO": 2, "ES": 5, "ZA": 2, "JP": 43, "GB": 43, "TR": 7, "IT": 5, "RU": 67, "IE": 2, "KR": 38, "SA": 3, "EE": 14, "CH": 2, "AE": 1, "LV": 4, "KZ": 6, "SC": 2, "MD": 1, "IR": 2, "SE": 11, "PH": 13, "IN": 7, "LT": 2, "AZ": 2, "PT": 1, "CO": 4, "CN": 3, "AT": 3, "AL": 2, "BG": 1, "BR": 2, "ZZ": 1, "HU": 1, "AF": 1, "AM": 1, "KH": 1, "GR": 1, "CZ": 1, "CR": 1, "CY": 1}` |
| **Line type mix** | `{"dc": 620, "proxy": 453, "home": 100, "mobile": 5, "unknown": 1}` |

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
