# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-20 09:05:53](https://img.shields.io/badge/updated-2026--10--20_09%3A05%3A53-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10785.1s](https://img.shields.io/badge/elapsed-10785.1s-lightgrey)
![profiles: 1357](https://img.shields.io/badge/profiles-1357-blue)
![live_hits: 1358](https://img.shields.io/badge/live__hits-1358-brightgreen)
![live_fail: 84102](https://img.shields.io/badge/live__fail-84102-orange)
![kept: 799](https://img.shields.io/badge/kept-799-blue)
![new: 559](https://img.shields.io/badge/new-559-success)
![dropped: 175](https://img.shields.io/badge/dropped-175-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-20 09:05:53 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10785.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `412905` |
| **Live PASS (pool hits)** | `1358` |
| **Live FAIL** | `84102` |
| **History retained** | `799` |
| **New PASS** | `559` |
| **History dropped** | `175` |
| **Previous public** | `974` |
| **Published profiles (deduped)** | `1357` |
| **Share links (exportable)** | `1186` |
| **YAML proxies (exportable)** | `1186` |
| **Protocol mix** | `{"shadowsocks": 223, "vless": 659, "hysteria2": 91, "trojan": 139, "vmess": 74}` |
| **Country mix** | `{"NL": 174, "DE": 90, "CH": 40, "US": 159, "CA": 266, "GB": 41, "HK": 44, "ZA": 4, "NO": 1, "IE": 2, "JP": 50, "IN": 10, "KR": 27, "PL": 20, "TH": 2, "CR": 1, "AT": 1, "ME": 10, "RU": 20, "TW": 4, "FR": 23, "BY": 5, "SG": 66, "FI": 19, "HU": 3, "LV": 8, "MD": 7, "SE": 8, "HR": 1, "AE": 4, "IT": 7, "IL": 1, "CZ": 4, "SA": 1, "ES": 6, "LT": 9, "AM": 1, "SC": 4, "MY": 3, "RO": 4, "KZ": 6, "TR": 5, "BR": 2, "UA": 2, "IR": 1, "EE": 2, "AU": 6, "GR": 2, "VN": 2, "ID": 1, "CN": 1, "BG": 2, "AL": 1, "DK": 2, "BZ": 2, "VG": 1, "BE": 1}` |
| **Line type mix** | `{"proxy": 321, "dc": 703, "home": 122, "mobile": 43}` |

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
