# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-09 08:57:00](https://img.shields.io/badge/updated-2026--11--09_08%3A57%3A00-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11281.3s](https://img.shields.io/badge/elapsed-11281.3s-lightgrey)
![profiles: 1408](https://img.shields.io/badge/profiles-1408-blue)
![live_hits: 1408](https://img.shields.io/badge/live__hits-1408-brightgreen)
![live_fail: 86895](https://img.shields.io/badge/live__fail-86895-orange)
![kept: 874](https://img.shields.io/badge/kept-874-blue)
![new: 534](https://img.shields.io/badge/new-534-success)
![dropped: 102](https://img.shields.io/badge/dropped-102-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-09 08:57:00 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11281.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `400795` |
| **Live PASS (pool hits)** | `1408` |
| **Live FAIL** | `86895` |
| **History retained** | `874` |
| **New PASS** | `534` |
| **History dropped** | `102` |
| **Previous public** | `976` |
| **Published profiles (deduped)** | `1408` |
| **Share links (exportable)** | `1201` |
| **YAML proxies (exportable)** | `1201` |
| **Protocol mix** | `{"shadowsocks": 333, "hysteria2": 144, "trojan": 93, "vless": 516, "vmess": 115}` |
| **Country mix** | `{"DE": 62, "BY": 11, "US": 277, "ES": 27, "GB": 37, "CA": 206, "PL": 23, "HK": 31, "NL": 157, "IR": 2, "JP": 23, "RU": 14, "AL": 1, "AT": 2, "NO": 2, "ZA": 4, "RO": 5, "BG": 10, "KR": 27, "IT": 25, "CH": 55, "SE": 16, "SG": 61, "FR": 46, "IN": 5, "MX": 2, "BR": 2, "AU": 4, "IL": 1, "UA": 2, "EE": 6, "KZ": 1, "AE": 2, "FI": 12, "GR": 2, "TR": 6, "IS": 1, "VN": 2, "TW": 4, "TH": 2, "CL": 1, "LV": 4, "NG": 1, "SK": 2, "MY": 2, "SA": 1, "IM": 1, "DK": 1, "LT": 9, "CN": 1, "VG": 1, "HU": 1, "CW": 1}` |
| **Line type mix** | `{"mobile": 115, "dc": 591, "proxy": 426, "home": 72}` |

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
