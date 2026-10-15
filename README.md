# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-16 03:19:42](https://img.shields.io/badge/updated-2026--10--16_03%3A19%3A42-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10318.6s](https://img.shields.io/badge/elapsed-10318.6s-lightgrey)
![profiles: 1063](https://img.shields.io/badge/profiles-1063-blue)
![live_hits: 1063](https://img.shields.io/badge/live__hits-1063-brightgreen)
![live_fail: 77878](https://img.shields.io/badge/live__fail-77878-orange)
![kept: 784](https://img.shields.io/badge/kept-784-blue)
![new: 279](https://img.shields.io/badge/new-279-success)
![dropped: 198](https://img.shields.io/badge/dropped-198-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-16 03:19:42 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10318.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `414698` |
| **Live PASS (pool hits)** | `1063` |
| **Live FAIL** | `77878` |
| **History retained** | `784` |
| **New PASS** | `279` |
| **History dropped** | `198` |
| **Previous public** | `982` |
| **Published profiles (deduped)** | `1063` |
| **Share links (exportable)** | `905` |
| **YAML proxies (exportable)** | `905` |
| **Protocol mix** | `{"vless": 448, "hysteria2": 104, "shadowsocks": 203, "trojan": 95, "vmess": 55}` |
| **Country mix** | `{"US": 129, "GB": 27, "NL": 181, "ZA": 5, "HK": 22, "DE": 71, "CH": 42, "CA": 139, "JP": 37, "IN": 7, "KR": 33, "IT": 7, "PL": 12, "SG": 44, "TR": 4, "FR": 25, "CR": 1, "ME": 7, "AT": 1, "RU": 13, "TW": 7, "SE": 7, "LV": 10, "FI": 11, "HU": 1, "AE": 4, "IL": 1, "BR": 3, "SA": 1, "LT": 5, "EE": 4, "CN": 2, "ES": 8, "AU": 5, "MX": 1, "TH": 3, "RO": 4, "SC": 3, "UA": 1, "KZ": 3, "MD": 2, "CZ": 1, "GR": 1, "AL": 2, "ID": 1, "MY": 3, "DK": 1, "BY": 5}` |
| **Line type mix** | `{"dc": 494, "proxy": 290, "home": 83, "mobile": 40}` |

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
