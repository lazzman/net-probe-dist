# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-04 07:46:17](https://img.shields.io/badge/updated-2026--10--04_07%3A46%3A17-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11075.7s](https://img.shields.io/badge/elapsed-11075.7s-lightgrey)
![profiles: 1423](https://img.shields.io/badge/profiles-1423-blue)
![live_hits: 1423](https://img.shields.io/badge/live__hits-1423-brightgreen)
![live_fail: 82338](https://img.shields.io/badge/live__fail-82338-orange)
![kept: 996](https://img.shields.io/badge/kept-996-blue)
![new: 427](https://img.shields.io/badge/new-427-success)
![dropped: 160](https://img.shields.io/badge/dropped-160-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-04 07:46:17 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11075.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `446342` |
| **Live PASS (pool hits)** | `1423` |
| **Live FAIL** | `82338` |
| **History retained** | `996` |
| **New PASS** | `427` |
| **History dropped** | `160` |
| **Previous public** | `1156` |
| **Published profiles (deduped)** | `1423` |
| **Share links (exportable)** | `1152` |
| **YAML proxies (exportable)** | `1152` |
| **Protocol mix** | `{"vless": 591, "hysteria2": 112, "vmess": 99, "shadowsocks": 262, "trojan": 88}` |
| **Country mix** | `{"US": 218, "GB": 33, "RU": 22, "CA": 244, "ZA": 6, "NL": 152, "IE": 5, "DE": 66, "FR": 29, "CH": 10, "ES": 12, "JP": 53, "CO": 1, "IN": 11, "KR": 31, "SG": 36, "AT": 1, "EE": 8, "TW": 5, "SE": 14, "FI": 13, "PL": 21, "TH": 2, "RO": 5, "IT": 14, "GR": 3, "HK": 31, "UA": 1, "MD": 1, "CL": 11, "SA": 1, "ID": 3, "NO": 1, "MX": 1, "TR": 6, "CZ": 14, "AM": 2, "KZ": 4, "SC": 4, "LV": 4, "AE": 2, "AU": 5, "AL": 2, "MY": 9, "BR": 2, "LT": 9, "CN": 17, "GT": 1, "BG": 9, "LU": 1}` |
| **Line type mix** | `{"dc": 707, "home": 71, "proxy": 358, "mobile": 20}` |

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
