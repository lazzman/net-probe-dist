# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-11 08:03:51](https://img.shields.io/badge/updated-2026--10--11_08%3A03%3A51-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10017.8s](https://img.shields.io/badge/elapsed-10017.8s-lightgrey)
![profiles: 1307](https://img.shields.io/badge/profiles-1307-blue)
![live_hits: 1307](https://img.shields.io/badge/live__hits-1307-brightgreen)
![live_fail: 76590](https://img.shields.io/badge/live__fail-76590-orange)
![kept: 910](https://img.shields.io/badge/kept-910-blue)
![new: 397](https://img.shields.io/badge/new-397-success)
![dropped: 86](https://img.shields.io/badge/dropped-86-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-11 08:03:51 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10017.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `409850` |
| **Live PASS (pool hits)** | `1307` |
| **Live FAIL** | `76590` |
| **History retained** | `910` |
| **New PASS** | `397` |
| **History dropped** | `86` |
| **Previous public** | `996` |
| **Published profiles (deduped)** | `1307` |
| **Share links (exportable)** | `1088` |
| **YAML proxies (exportable)** | `1088` |
| **Protocol mix** | `{"vless": 479, "shadowsocks": 269, "hysteria2": 141, "trojan": 133, "vmess": 66}` |
| **Country mix** | `{"US": 158, "GB": 29, "SG": 52, "NL": 177, "TR": 4, "CA": 135, "ID": 3, "DE": 74, "FR": 25, "IE": 7, "ZA": 4, "CH": 38, "RO": 2, "JP": 67, "KR": 53, "IN": 8, "HK": 41, "AT": 3, "ES": 15, "RU": 34, "EE": 7, "FI": 16, "TH": 3, "UA": 1, "PL": 19, "TW": 4, "SE": 8, "IT": 16, "KZ": 5, "MY": 11, "SA": 1, "LV": 13, "AM": 1, "IR": 1, "NO": 1, "AE": 3, "ME": 3, "CZ": 2, "SC": 3, "AU": 5, "BR": 1, "GR": 1, "BG": 8, "AL": 3, "VN": 1, "DK": 1, "LT": 10, "CN": 16}` |
| **Line type mix** | `{"dc": 586, "proxy": 370, "home": 103, "mobile": 34}` |

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
