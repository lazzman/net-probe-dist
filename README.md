# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-08 15:38:30](https://img.shields.io/badge/updated-2026--10--08_15%3A38%3A30-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9923.7s](https://img.shields.io/badge/elapsed-9923.7s-lightgrey)
![profiles: 2788](https://img.shields.io/badge/profiles-2788-blue)
![live_hits: 2788](https://img.shields.io/badge/live__hits-2788-brightgreen)
![live_fail: 74630](https://img.shields.io/badge/live__fail-74630-orange)
![kept: 949](https://img.shields.io/badge/kept-949-blue)
![new: 1839](https://img.shields.io/badge/new-1839-success)
![dropped: 365](https://img.shields.io/badge/dropped-365-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-08 15:38:30 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9923.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `407155` |
| **Live PASS (pool hits)** | `2788` |
| **Live FAIL** | `74630` |
| **History retained** | `949` |
| **New PASS** | `1839` |
| **History dropped** | `365` |
| **Previous public** | `1314` |
| **Published profiles (deduped)** | `2788` |
| **Share links (exportable)** | `1706` |
| **YAML proxies (exportable)** | `1706` |
| **Protocol mix** | `{"vless": 1131, "shadowsocks": 279, "hysteria2": 110, "trojan": 119, "vmess": 67}` |
| **Country mix** | `{"US": 217, "CA": 613, "FI": 19, "ZA": 4, "GB": 42, "NL": 182, "DE": 104, "TR": 7, "IE": 6, "ID": 2, "FR": 30, "IN": 17, "CH": 11, "RO": 4, "ES": 13, "JP": 58, "KR": 38, "SG": 48, "HU": 1, "AT": 3, "EE": 12, "RU": 21, "SE": 9, "LT": 9, "TH": 5, "PL": 23, "HK": 52, "UZ": 1, "IR": 3, "IT": 21, "KZ": 4, "MY": 10, "CL": 11, "LV": 26, "TW": 3, "CN": 18, "SC": 5, "NO": 2, "IL": 1, "AU": 6, "BE": 1, "PT": 2, "GR": 3, "AL": 4, "AE": 3, "NZ": 1, "BZ": 4, "BG": 10, "UA": 5, "BR": 1, "CW": 4, "CY": 3, "VN": 1, "AM": 1, "CZ": 1, "DO": 1, "SA": 1, "VG": 1, "CR": 2, "MX": 1}` |
| **Line type mix** | `{"dc": 1160, "proxy": 446, "home": 96, "mobile": 9}` |

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
