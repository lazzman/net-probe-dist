# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-06 10:31:39](https://img.shields.io/badge/updated-2026--11--06_10%3A31%3A39-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11208.6s](https://img.shields.io/badge/elapsed-11208.6s-lightgrey)
![profiles: 1664](https://img.shields.io/badge/profiles-1664-blue)
![live_hits: 1664](https://img.shields.io/badge/live__hits-1664-brightgreen)
![live_fail: 86354](https://img.shields.io/badge/live__fail-86354-orange)
![kept: 887](https://img.shields.io/badge/kept-887-blue)
![new: 777](https://img.shields.io/badge/new-777-success)
![dropped: 139](https://img.shields.io/badge/dropped-139-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-06 10:31:39 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11208.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `404325` |
| **Live PASS (pool hits)** | `1664` |
| **Live FAIL** | `86354` |
| **History retained** | `887` |
| **New PASS** | `777` |
| **History dropped** | `139` |
| **Previous public** | `1026` |
| **Published profiles (deduped)** | `1664` |
| **Share links (exportable)** | `1389` |
| **YAML proxies (exportable)** | `1389` |
| **Protocol mix** | `{"hysteria2": 151, "shadowsocks": 296, "trojan": 113, "vless": 706, "vmess": 123}` |
| **Country mix** | `{"HK": 32, "DE": 81, "ES": 17, "BY": 9, "PL": 25, "NL": 167, "US": 333, "AT": 4, "NO": 1, "RO": 4, "ZA": 3, "GB": 52, "JP": 31, "CA": 270, "BG": 10, "IN": 6, "IT": 21, "FR": 40, "CH": 54, "MX": 4, "AU": 4, "IL": 1, "UA": 6, "EE": 7, "SG": 70, "RU": 13, "AE": 3, "SE": 15, "FI": 12, "KR": 27, "TW": 4, "TR": 10, "AL": 2, "BR": 2, "PT": 1, "TH": 4, "PH": 1, "LV": 5, "GR": 2, "VN": 1, "KZ": 4, "MY": 3, "ID": 1, "CN": 2, "LT": 10, "CL": 1, "SA": 1, "SC": 3, "NZ": 1, "BZ": 4, "CW": 3, "IR": 1, "VG": 1, "HU": 1, "DK": 1}` |
| **Line type mix** | `{"dc": 715, "mobile": 137, "proxy": 456, "home": 83}` |

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
