# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-01 04:55:01](https://img.shields.io/badge/updated-2026--10--01_04%3A55%3A01-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10326.1s](https://img.shields.io/badge/elapsed-10326.1s-lightgrey)
![profiles: 1296](https://img.shields.io/badge/profiles-1296-blue)
![live_hits: 1296](https://img.shields.io/badge/live__hits-1296-brightgreen)
![live_fail: 78344](https://img.shields.io/badge/live__fail-78344-orange)
![kept: 1015](https://img.shields.io/badge/kept-1015-blue)
![new: 281](https://img.shields.io/badge/new-281-success)
![dropped: 257](https://img.shields.io/badge/dropped-257-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-01 04:55:01 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10326.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `432565` |
| **Live PASS (pool hits)** | `1296` |
| **Live FAIL** | `78344` |
| **History retained** | `1015` |
| **New PASS** | `281` |
| **History dropped** | `257` |
| **Previous public** | `1272` |
| **Published profiles (deduped)** | `1296` |
| **Share links (exportable)** | `1205` |
| **YAML proxies (exportable)** | `1205` |
| **Protocol mix** | `{"vless": 676, "shadowsocks": 284, "trojan": 32, "vmess": 85, "hysteria2": 128}` |
| **Country mix** | `{"US": 242, "IE": 4, "GB": 52, "DE": 62, "CA": 265, "NL": 156, "FR": 30, "ID": 3, "SG": 39, "NO": 2, "RO": 2, "ES": 13, "ZA": 3, "CH": 9, "JP": 36, "IN": 12, "HU": 1, "AT": 1, "SC": 2, "TW": 6, "RU": 27, "HK": 39, "AE": 3, "FI": 16, "SE": 11, "PL": 13, "LT": 11, "IT": 17, "EE": 1, "ZZ": 1, "UA": 3, "TR": 4, "SK": 2, "KR": 30, "KZ": 4, "DZ": 28, "MX": 2, "PH": 1, "AU": 3, "GE": 1, "GR": 1, "AL": 2, "AD": 1, "IR": 7, "MY": 12, "CZ": 8, "AM": 2, "TH": 2, "PT": 1, "CL": 1, "SA": 1, "BG": 5, "LV": 1, "CO": 1, "IL": 1, "CR": 1, "CN": 2}` |
| **Line type mix** | `{"dc": 736, "mobile": 22, "proxy": 365, "home": 82, "unknown": 1}` |

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
