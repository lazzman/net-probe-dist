# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-04 04:04:03](https://img.shields.io/badge/updated-2026--10--04_04%3A04%3A03-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 15054.5s](https://img.shields.io/badge/elapsed-15054.5s-lightgrey)
![profiles: 1419](https://img.shields.io/badge/profiles-1419-blue)
![live_hits: 1419](https://img.shields.io/badge/live__hits-1419-brightgreen)
![live_fail: 110293](https://img.shields.io/badge/live__fail-110293-orange)
![kept: 982](https://img.shields.io/badge/kept-982-blue)
![new: 437](https://img.shields.io/badge/new-437-success)
![dropped: 246](https://img.shields.io/badge/dropped-246-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-04 04:04:03 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `15054.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `517461` |
| **Live PASS (pool hits)** | `1419` |
| **Live FAIL** | `110293` |
| **History retained** | `982` |
| **New PASS** | `437` |
| **History dropped** | `246` |
| **Previous public** | `1228` |
| **Published profiles (deduped)** | `1419` |
| **Share links (exportable)** | `1156` |
| **YAML proxies (exportable)** | `1156` |
| **Protocol mix** | `{"vless": 590, "hysteria2": 119, "shadowsocks": 272, "trojan": 80, "vmess": 95}` |
| **Country mix** | `{"US": 217, "CA": 252, "RU": 24, "GB": 31, "SG": 43, "NL": 150, "IE": 4, "ID": 3, "DE": 65, "FR": 25, "RO": 6, "ZA": 5, "CH": 10, "ES": 8, "JP": 49, "IN": 10, "KR": 36, "AT": 1, "HK": 38, "TW": 4, "IT": 17, "EE": 7, "GR": 3, "PL": 18, "SE": 13, "FI": 10, "CL": 11, "AM": 2, "NO": 2, "CO": 1, "SC": 2, "LV": 5, "TR": 2, "AE": 2, "AU": 5, "KZ": 3, "MY": 10, "LU": 2, "VN": 5, "AL": 2, "TH": 1, "BR": 2, "CZ": 14, "BG": 9, "LT": 10, "GT": 1, "MD": 1, "SA": 1, "CN": 15, "ZZ": 1}` |
| **Line type mix** | `{"dc": 701, "home": 63, "proxy": 368, "mobile": 25, "unknown": 1}` |

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
