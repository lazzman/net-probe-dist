# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-22 23:16:47](https://img.shields.io/badge/updated-2026--08--22_23%3A16%3A47-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9056.3s](https://img.shields.io/badge/elapsed-9056.3s-lightgrey)
![profiles: 2275](https://img.shields.io/badge/profiles-2275-blue)
![live_hits: 2275](https://img.shields.io/badge/live__hits-2275-brightgreen)
![live_fail: 66976](https://img.shields.io/badge/live__fail-66976-orange)
![kept: 1473](https://img.shields.io/badge/kept-1473-blue)
![new: 802](https://img.shields.io/badge/new-802-success)
![dropped: 634](https://img.shields.io/badge/dropped-634-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-22 23:16:47 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9056.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `436164` |
| **Live PASS (pool hits)** | `2275` |
| **Live FAIL** | `66976` |
| **History retained** | `1473` |
| **New PASS** | `802` |
| **History dropped** | `634` |
| **Previous public** | `2107` |
| **Published profiles (deduped)** | `2275` |
| **Share links (exportable)** | `1652` |
| **YAML proxies (exportable)** | `1652` |
| **Protocol mix** | `{"shadowsocks": 295, "vmess": 68, "vless": 995, "hysteria2": 178, "trojan": 116}` |
| **Country mix** | `{"US": 246, "NL": 294, "DE": 167, "CA": 247, "AU": 19, "GB": 59, "FR": 41, "BG": 8, "PL": 46, "SG": 62, "RU": 38, "FI": 39, "SE": 18, "BR": 15, "TW": 16, "IN": 14, "ES": 5, "ZA": 4, "HK": 79, "JP": 36, "CN": 5, "EE": 15, "BE": 1, "TR": 10, "AE": 2, "CH": 18, "IT": 13, "KZ": 14, "VN": 2, "LV": 17, "CO": 9, "SK": 1, "SC": 8, "MD": 2, "DK": 4, "HU": 2, "LT": 10, "AM": 1, "PH": 2, "TH": 5, "KR": 24, "UZ": 1, "AL": 3, "NO": 3, "PT": 1, "PE": 1, "UA": 5, "CZ": 4, "AT": 5, "RO": 3, "ME": 2, "IE": 2, "HR": 1, "BZ": 1, "CR": 1, "BY": 1, "AF": 1, "DZ": 1, "MY": 2, "CY": 1}` |
| **Line type mix** | `{"proxy": 530, "dc": 886, "home": 228, "mobile": 13}` |

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
