# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-21 14:34:38](https://img.shields.io/badge/updated-2026--09--21_14%3A34%3A38-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10018.1s](https://img.shields.io/badge/elapsed-10018.1s-lightgrey)
![profiles: 4407](https://img.shields.io/badge/profiles-4407-blue)
![live_hits: 4410](https://img.shields.io/badge/live__hits-4410-brightgreen)
![live_fail: 73376](https://img.shields.io/badge/live__fail-73376-orange)
![kept: 1271](https://img.shields.io/badge/kept-1271-blue)
![new: 3139](https://img.shields.io/badge/new-3139-success)
![dropped: 160](https://img.shields.io/badge/dropped-160-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-21 14:34:38 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10018.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `420316` |
| **Live PASS (pool hits)** | `4410` |
| **Live FAIL** | `73376` |
| **History retained** | `1271` |
| **New PASS** | `3139` |
| **History dropped** | `160` |
| **Previous public** | `1431` |
| **Published profiles (deduped)** | `4407` |
| **Share links (exportable)** | `2479` |
| **YAML proxies (exportable)** | `2479` |
| **Protocol mix** | `{"vless": 1982, "hysteria2": 112, "vmess": 55, "trojan": 83, "shadowsocks": 247}` |
| **Country mix** | `{"US": 316, "DE": 94, "GB": 101, "DK": 7, "CA": 1089, "ES": 19, "NL": 198, "RU": 31, "KR": 36, "SE": 18, "TW": 18, "ID": 1, "FR": 37, "RO": 5, "SG": 44, "CH": 7, "JP": 57, "MX": 2, "IN": 17, "FI": 31, "CL": 3, "AT": 4, "PL": 27, "TR": 9, "TH": 5, "KZ": 15, "EE": 12, "BG": 12, "HK": 82, "IT": 19, "GR": 3, "AL": 2, "CZ": 14, "SA": 11, "CY": 13, "ME": 3, "NO": 5, "PT": 3, "AM": 3, "IM": 1, "SC": 9, "ZA": 3, "BZ": 11, "DZ": 24, "IR": 4, "AE": 2, "AU": 8, "LT": 5, "CN": 1, "BR": 2, "UA": 2, "CR": 2, "GT": 1, "MD": 2, "LV": 10, "HU": 3, "NZ": 1, "CW": 3, "VN": 2, "VG": 1, "MY": 5, "UZ": 2, "LU": 1, "SK": 3, "BE": 3, "BY": 1, "IE": 3, "RS": 1, "IS": 2}` |
| **Line type mix** | `{"home": 107, "dc": 1841, "proxy": 535, "mobile": 8}` |

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
