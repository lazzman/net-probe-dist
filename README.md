# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-21 08:24:49](https://img.shields.io/badge/updated-2026--10--21_08%3A24%3A49-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10868.1s](https://img.shields.io/badge/elapsed-10868.1s-lightgrey)
![profiles: 1359](https://img.shields.io/badge/profiles-1359-blue)
![live_hits: 1359](https://img.shields.io/badge/live__hits-1359-brightgreen)
![live_fail: 84869](https://img.shields.io/badge/live__fail-84869-orange)
![kept: 853](https://img.shields.io/badge/kept-853-blue)
![new: 506](https://img.shields.io/badge/new-506-success)
![dropped: 119](https://img.shields.io/badge/dropped-119-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-21 08:24:49 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10868.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `412276` |
| **Live PASS (pool hits)** | `1359` |
| **Live FAIL** | `84869` |
| **History retained** | `853` |
| **New PASS** | `506` |
| **History dropped** | `119` |
| **Previous public** | `972` |
| **Published profiles (deduped)** | `1359` |
| **Share links (exportable)** | `1178` |
| **YAML proxies (exportable)** | `1178` |
| **Protocol mix** | `{"shadowsocks": 238, "hysteria2": 91, "vless": 638, "trojan": 142, "vmess": 69}` |
| **Country mix** | `{"US": 161, "CH": 40, "NL": 170, "GB": 39, "HK": 52, "ZA": 3, "NO": 1, "RO": 4, "IE": 2, "DE": 88, "JP": 62, "KR": 23, "IR": 3, "IT": 19, "CA": 262, "IN": 9, "TH": 2, "SG": 58, "PL": 22, "AT": 1, "ME": 10, "RU": 16, "CR": 1, "TW": 4, "EE": 3, "FI": 13, "FR": 22, "AE": 4, "TR": 7, "CZ": 5, "LT": 5, "DK": 3, "AM": 1, "SC": 3, "CN": 1, "SE": 9, "CL": 1, "BY": 4, "HR": 1, "KZ": 4, "ES": 6, "BR": 1, "LV": 13, "AU": 3, "BG": 4, "GR": 2, "MD": 2, "VN": 2, "MY": 2, "ID": 1, "SA": 1, "UA": 2, "IL": 1, "VG": 1, "BE": 1, "CW": 1, "BZ": 1}` |
| **Line type mix** | `{"proxy": 301, "dc": 720, "home": 108, "mobile": 53}` |

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
