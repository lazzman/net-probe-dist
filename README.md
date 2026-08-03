# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-04 00:48:52](https://img.shields.io/badge/updated-2026--08--04_00%3A48%3A52-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 32](https://img.shields.io/badge/workers-32-blueviolet)
![elapsed: n/a](https://img.shields.io/badge/elapsed-n%2Fa-lightgrey)
![profiles: 1401](https://img.shields.io/badge/profiles-1401-blue)
![live_hits: n/a](https://img.shields.io/badge/live__hits-n%2Fa-brightgreen)
![live_fail: n/a](https://img.shields.io/badge/live__fail-n%2Fa-orange)
![kept: n/a](https://img.shields.io/badge/kept-n%2Fa-blue)
![new: n/a](https://img.shields.io/badge/new-n%2Fa-success)
![dropped: n/a](https://img.shields.io/badge/dropped-n%2Fa-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-04T00:48:52.125311+08:00` |
| **Workflow result** | `success` |
| **Workers** | `32` |
| **Elapsed** | `n/a` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `—` |
| **Live PASS (pool hits)** | `—` |
| **Live FAIL** | `—` |
| **History retained** | `—` |
| **New PASS** | `—` |
| **History dropped** | `—` |
| **Previous public** | `—` |
| **Published profiles (deduped)** | `1401` |
| **Share links (exportable)** | `1401` |
| **YAML proxies (exportable)** | `1401` |
| **Protocol mix** | `{"vless": 990, "shadowsocks": 195, "trojan": 41, "vmess": 86, "hysteria2": 89}` |
| **Country mix** | `{"US": 209, "CA": 346, "DE": 90, "NL": 188, "ES": 12, "RU": 61, "FI": 38, "PL": 22, "FR": 36, "GB": 33, "IT": 24, "AT": 5, "LT": 3, "HK": 54, "CH": 26, "TW": 14, "TR": 13, "HU": 1, "SG": 18, "SE": 20, "KZ": 4, "JP": 15, "ID": 1, "EE": 3, "LV": 11, "SC": 7, "MD": 2, "IL": 2, "PH": 70, "CR": 2, "IE": 1, "AL": 1, "TH": 2, "KR": 26, "BG": 2, "ZA": 2, "NO": 2, "IN": 4, "MY": 4, "BH": 1, "RO": 5, "IS": 4, "SA": 2, "AE": 1, "PA": 1, "CN": 3, "ZZ": 2, "DK": 1, "BR": 2, "AU": 3, "KH": 1, "BE": 1}` |
| **Line type mix** | `{"dc": 721, "home": 99, "proxy": 573, "mobile": 6, "unknown": 2}` |

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
