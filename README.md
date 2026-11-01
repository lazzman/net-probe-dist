# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-01 08:09:46](https://img.shields.io/badge/updated-2026--11--01_08%3A09%3A46-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11033.8s](https://img.shields.io/badge/elapsed-11033.8s-lightgrey)
![profiles: 1255](https://img.shields.io/badge/profiles-1255-blue)
![live_hits: 1255](https://img.shields.io/badge/live__hits-1255-brightgreen)
![live_fail: 86190](https://img.shields.io/badge/live__fail-86190-orange)
![kept: 906](https://img.shields.io/badge/kept-906-blue)
![new: 349](https://img.shields.io/badge/new-349-success)
![dropped: 116](https://img.shields.io/badge/dropped-116-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-01 08:09:46 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11033.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `403033` |
| **Live PASS (pool hits)** | `1255` |
| **Live FAIL** | `86190` |
| **History retained** | `906` |
| **New PASS** | `349` |
| **History dropped** | `116` |
| **Previous public** | `1022` |
| **Published profiles (deduped)** | `1255` |
| **Share links (exportable)** | `1100` |
| **YAML proxies (exportable)** | `1100` |
| **Protocol mix** | `{"shadowsocks": 254, "hysteria2": 135, "trojan": 163, "vless": 475, "vmess": 73}` |
| **Country mix** | `{"NL": 163, "IT": 13, "DE": 70, "US": 196, "GB": 27, "ZA": 4, "RO": 4, "JP": 25, "SG": 38, "CA": 241, "BG": 13, "KR": 27, "IN": 9, "PL": 17, "CH": 51, "ES": 12, "SE": 7, "AT": 2, "LV": 5, "LT": 11, "RU": 27, "FR": 29, "FI": 13, "BY": 8, "KZ": 7, "HK": 31, "CZ": 1, "MY": 2, "IL": 4, "IR": 4, "AE": 4, "AM": 2, "TH": 3, "CN": 1, "TW": 3, "AU": 2, "NO": 1, "EE": 2, "CO": 1, "AL": 1, "MX": 1, "BR": 1, "PH": 2, "SC": 2, "UA": 1, "ID": 7, "GR": 1, "DK": 1, "VN": 1, "SI": 1, "TR": 2, "SA": 1, "EG": 1}` |
| **Line type mix** | `{"proxy": 297, "dc": 607, "home": 81, "mobile": 118}` |

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
