# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-11 05:52:36](https://img.shields.io/badge/updated-2026--08--11_05%3A52%3A36-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10211.7s](https://img.shields.io/badge/elapsed-10211.7s-lightgrey)
![profiles: 1502](https://img.shields.io/badge/profiles-1502-blue)
![live_hits: 1502](https://img.shields.io/badge/live__hits-1502-brightgreen)
![live_fail: 93514](https://img.shields.io/badge/live__fail-93514-orange)
![kept: 906](https://img.shields.io/badge/kept-906-blue)
![new: 596](https://img.shields.io/badge/new-596-success)
![dropped: 355](https://img.shields.io/badge/dropped-355-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-11 05:52:36 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10211.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `448720` |
| **Live PASS (pool hits)** | `1502` |
| **Live FAIL** | `93514` |
| **History retained** | `906` |
| **New PASS** | `596` |
| **History dropped** | `355` |
| **Previous public** | `1261` |
| **Published profiles (deduped)** | `1502` |
| **Share links (exportable)** | `1167` |
| **YAML proxies (exportable)** | `1167` |
| **Protocol mix** | `{"vless": 722, "vmess": 79, "hysteria2": 89, "shadowsocks": 193, "trojan": 84}` |
| **Country mix** | `{"NL": 211, "US": 162, "FR": 60, "DE": 83, "TH": 2, "RU": 76, "HK": 42, "AU": 4, "RO": 5, "GB": 38, "FI": 31, "TW": 8, "ZA": 2, "SE": 10, "JP": 60, "IT": 4, "CA": 153, "TR": 6, "IE": 4, "KR": 49, "PL": 19, "SC": 4, "EE": 14, "SG": 30, "BE": 6, "CH": 3, "CZ": 2, "AE": 1, "KZ": 5, "MD": 1, "ZZ": 2, "ES": 5, "LT": 4, "LV": 11, "AL": 3, "PH": 6, "BG": 3, "IN": 9, "AT": 4, "PT": 1, "AZ": 1, "NO": 1, "CO": 4, "CN": 7, "SA": 2, "HU": 1, "MY": 1, "BR": 1, "AF": 1, "AM": 1, "GR": 1, "UA": 1, "KH": 1, "CR": 1, "CY": 1}` |
| **Line type mix** | `{"proxy": 449, "dc": 597, "home": 113, "mobile": 7, "unknown": 2}` |

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
