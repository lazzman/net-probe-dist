# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-08 23:42:51](https://img.shields.io/badge/updated-2026--10--08_23%3A42%3A51-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9992.9s](https://img.shields.io/badge/elapsed-9992.9s-lightgrey)
![profiles: 1320](https://img.shields.io/badge/profiles-1320-blue)
![live_hits: 1320](https://img.shields.io/badge/live__hits-1320-brightgreen)
![live_fail: 76143](https://img.shields.io/badge/live__fail-76143-orange)
![kept: 880](https://img.shields.io/badge/kept-880-blue)
![new: 440](https://img.shields.io/badge/new-440-success)
![dropped: 826](https://img.shields.io/badge/dropped-826-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-08 23:42:51 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9992.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `409610` |
| **Live PASS (pool hits)** | `1320` |
| **Live FAIL** | `76143` |
| **History retained** | `880` |
| **New PASS** | `440` |
| **History dropped** | `826` |
| **Previous public** | `1706` |
| **Published profiles (deduped)** | `1320` |
| **Share links (exportable)** | `1079` |
| **YAML proxies (exportable)** | `1079` |
| **Protocol mix** | `{"vless": 565, "shadowsocks": 263, "hysteria2": 103, "trojan": 95, "vmess": 53}` |
| **Country mix** | `{"US": 169, "ZA": 4, "CA": 162, "NL": 171, "GB": 34, "DE": 86, "ID": 3, "IE": 6, "FR": 32, "IN": 12, "RO": 4, "CH": 11, "JP": 55, "FI": 16, "KR": 32, "SG": 41, "AT": 1, "HK": 37, "TW": 4, "RU": 19, "SE": 7, "LT": 8, "PL": 28, "EE": 11, "UZ": 1, "ES": 8, "IT": 16, "KZ": 5, "TR": 5, "MY": 10, "NO": 2, "AU": 4, "MX": 2, "SC": 3, "LV": 27, "BE": 1, "PT": 1, "GR": 2, "AL": 4, "AE": 2, "VN": 2, "BG": 8, "AM": 1, "TH": 3, "CZ": 1, "SA": 1, "CN": 16, "BR": 1}` |
| **Line type mix** | `{"dc": 621, "proxy": 365, "home": 85, "mobile": 8}` |

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
