# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-27 15:02:30](https://img.shields.io/badge/updated-2026--10--27_15%3A02%3A30-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11053.6s](https://img.shields.io/badge/elapsed-11053.6s-lightgrey)
![profiles: 1780](https://img.shields.io/badge/profiles-1780-blue)
![live_hits: 1780](https://img.shields.io/badge/live__hits-1780-brightgreen)
![live_fail: 85201](https://img.shields.io/badge/live__fail-85201-orange)
![kept: 989](https://img.shields.io/badge/kept-989-blue)
![new: 791](https://img.shields.io/badge/new-791-success)
![dropped: 305](https://img.shields.io/badge/dropped-305-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-27 15:02:30 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11053.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `412998` |
| **Live PASS (pool hits)** | `1780` |
| **Live FAIL** | `85201` |
| **History retained** | `989` |
| **New PASS** | `791` |
| **History dropped** | `305` |
| **Previous public** | `1294` |
| **Published profiles (deduped)** | `1780` |
| **Share links (exportable)** | `1418` |
| **YAML proxies (exportable)** | `1418` |
| **Protocol mix** | `{"shadowsocks": 270, "hysteria2": 145, "trojan": 98, "vless": 836, "vmess": 69}` |
| **Country mix** | `{"IT": 16, "DE": 90, "GB": 52, "US": 222, "NL": 207, "ZZ": 1, "TR": 18, "RO": 6, "NO": 1, "ZA": 5, "CH": 45, "JP": 31, "CA": 358, "KR": 26, "RU": 38, "IN": 11, "PL": 8, "HK": 45, "AT": 2, "LV": 3, "FR": 32, "BY": 8, "SG": 49, "TH": 3, "MX": 3, "FI": 22, "AU": 6, "AE": 4, "BZ": 3, "BG": 11, "ES": 14, "SE": 13, "GR": 1, "MD": 2, "VN": 2, "BR": 2, "SA": 1, "IL": 6, "SC": 7, "TW": 4, "UA": 3, "KZ": 6, "SI": 2, "CN": 4, "AM": 2, "EE": 3, "MK": 1, "LU": 1, "NZ": 1, "IR": 1, "CY": 2, "LT": 8, "CW": 2, "RS": 1, "CR": 2, "MY": 3, "ID": 1, "PH": 1, "PT": 1, "AL": 1}` |
| **Line type mix** | `{"dc": 867, "mobile": 88, "proxy": 363, "unknown": 1, "home": 105}` |

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
