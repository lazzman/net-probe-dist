# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-10 07:16:40](https://img.shields.io/badge/updated-2026--09--10_07%3A16%3A40-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9622.8s](https://img.shields.io/badge/elapsed-9622.8s-lightgrey)
![profiles: 1650](https://img.shields.io/badge/profiles-1650-blue)
![live_hits: 1653](https://img.shields.io/badge/live__hits-1653-brightgreen)
![live_fail: 73951](https://img.shields.io/badge/live__fail-73951-orange)
![kept: 1010](https://img.shields.io/badge/kept-1010-blue)
![new: 643](https://img.shields.io/badge/new-643-success)
![dropped: 143](https://img.shields.io/badge/dropped-143-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-10 07:16:40 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9622.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `423833` |
| **Live PASS (pool hits)** | `1653` |
| **Live FAIL** | `73951` |
| **History retained** | `1010` |
| **New PASS** | `643` |
| **History dropped** | `143` |
| **Previous public** | `1153` |
| **Published profiles (deduped)** | `1650` |
| **Share links (exportable)** | `1178` |
| **YAML proxies (exportable)** | `1178` |
| **Protocol mix** | `{"vless": 639, "trojan": 39, "hysteria2": 142, "vmess": 97, "shadowsocks": 261}` |
| **Country mix** | `{"CA": 240, "HR": 1, "DE": 71, "RU": 31, "DZ": 16, "AU": 4, "GB": 54, "FI": 18, "US": 158, "NL": 211, "SG": 45, "ID": 1, "AE": 2, "JP": 39, "FR": 25, "ZA": 4, "PL": 32, "ES": 9, "RO": 5, "CN": 5, "MY": 4, "IE": 4, "LT": 10, "IT": 10, "AT": 2, "KZ": 8, "NO": 13, "LV": 16, "EE": 7, "CZ": 4, "IN": 6, "TW": 15, "TR": 7, "JE": 1, "HK": 42, "GR": 2, "UZ": 2, "SK": 1, "SE": 5, "EG": 1, "SA": 1, "KR": 25, "TH": 4, "AL": 1, "DK": 2, "HU": 1, "SC": 3, "AR": 2, "UA": 3, "PH": 1, "AM": 1, "BE": 1, "IR": 1, "CH": 2}` |
| **Line type mix** | `{"dc": 686, "proxy": 381, "home": 102, "mobile": 10}` |

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
