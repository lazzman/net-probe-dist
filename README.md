# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-07 15:30:49](https://img.shields.io/badge/updated-2026--10--07_15%3A30%3A49-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10115.5s](https://img.shields.io/badge/elapsed-10115.5s-lightgrey)
![profiles: 2580](https://img.shields.io/badge/profiles-2580-blue)
![live_hits: 2580](https://img.shields.io/badge/live__hits-2580-brightgreen)
![live_fail: 75044](https://img.shields.io/badge/live__fail-75044-orange)
![kept: 963](https://img.shields.io/badge/kept-963-blue)
![new: 1617](https://img.shields.io/badge/new-1617-success)
![dropped: 505](https://img.shields.io/badge/dropped-505-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-07 15:30:49 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10115.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `404191` |
| **Live PASS (pool hits)** | `2580` |
| **Live FAIL** | `75044` |
| **History retained** | `963` |
| **New PASS** | `1617` |
| **History dropped** | `505` |
| **Previous public** | `1468` |
| **Published profiles (deduped)** | `2580` |
| **Share links (exportable)** | `1673` |
| **YAML proxies (exportable)** | `1673` |
| **Protocol mix** | `{"vless": 1061, "vmess": 103, "shadowsocks": 281, "hysteria2": 107, "trojan": 121}` |
| **Country mix** | `{"US": 217, "DE": 111, "SG": 45, "CA": 602, "NL": 179, "FR": 35, "GB": 42, "ZA": 3, "ID": 2, "IE": 5, "RO": 2, "CH": 9, "ES": 12, "FI": 21, "JP": 54, "IN": 14, "KR": 40, "PL": 21, "AE": 6, "AT": 3, "TR": 4, "RU": 24, "SE": 10, "IT": 22, "EE": 7, "CL": 12, "AM": 2, "TW": 4, "MY": 9, "KZ": 6, "CN": 18, "HK": 54, "AU": 8, "NO": 1, "LT": 9, "IL": 1, "SC": 6, "LV": 13, "BE": 2, "AL": 3, "BZ": 4, "BR": 2, "CW": 3, "CY": 3, "UA": 4, "GR": 2, "TH": 4, "NZ": 1, "SA": 1, "VG": 1, "BG": 9, "IR": 2, "CR": 2, "DK": 1, "CZ": 1}` |
| **Line type mix** | `{"dc": 1126, "mobile": 21, "proxy": 440, "home": 91}` |

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
