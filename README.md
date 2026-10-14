# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-14 09:13:17](https://img.shields.io/badge/updated-2026--10--14_09%3A13%3A17-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10002.2s](https://img.shields.io/badge/elapsed-10002.2s-lightgrey)
![profiles: 1562](https://img.shields.io/badge/profiles-1562-blue)
![live_hits: 1562](https://img.shields.io/badge/live__hits-1562-brightgreen)
![live_fail: 76766](https://img.shields.io/badge/live__fail-76766-orange)
![kept: 863](https://img.shields.io/badge/kept-863-blue)
![new: 699](https://img.shields.io/badge/new-699-success)
![dropped: 161](https://img.shields.io/badge/dropped-161-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-14 09:13:17 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10002.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `412816` |
| **Live PASS (pool hits)** | `1562` |
| **Live FAIL** | `76766` |
| **History retained** | `863` |
| **New PASS** | `699` |
| **History dropped** | `161` |
| **Previous public** | `1024` |
| **Published profiles (deduped)** | `1562` |
| **Share links (exportable)** | `1279` |
| **YAML proxies (exportable)** | `1279` |
| **Protocol mix** | `{"vless": 739, "shadowsocks": 273, "hysteria2": 108, "trojan": 102, "vmess": 57}` |
| **Country mix** | `{"US": 166, "ZA": 4, "CA": 300, "RU": 31, "GB": 35, "HK": 45, "NL": 170, "TR": 9, "IE": 5, "SG": 55, "DE": 84, "FR": 29, "IR": 1, "RO": 3, "CH": 42, "JP": 61, "IN": 7, "KR": 41, "CR": 2, "SC": 4, "AT": 1, "TW": 5, "PL": 17, "TH": 3, "SE": 11, "FI": 17, "IT": 21, "IL": 1, "MY": 8, "ME": 6, "LT": 13, "LV": 21, "ID": 2, "EE": 8, "AE": 3, "CZ": 4, "ES": 6, "KZ": 4, "BR": 3, "AU": 4, "GR": 2, "AL": 3, "BG": 11, "VN": 3, "DK": 2, "SA": 1, "BZ": 3, "UA": 1, "MX": 1, "CN": 1}` |
| **Line type mix** | `{"dc": 752, "proxy": 378, "home": 107, "mobile": 43}` |

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
