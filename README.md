# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-22 01:32:02](https://img.shields.io/badge/updated-2026--11--22_01%3A32%3A02-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11427.2s](https://img.shields.io/badge/elapsed-11427.2s-lightgrey)
![profiles: 1251](https://img.shields.io/badge/profiles-1251-blue)
![live_hits: 1251](https://img.shields.io/badge/live__hits-1251-brightgreen)
![live_fail: 88724](https://img.shields.io/badge/live__fail-88724-orange)
![kept: 994](https://img.shields.io/badge/kept-994-blue)
![new: 257](https://img.shields.io/badge/new-257-success)
![dropped: 210](https://img.shields.io/badge/dropped-210-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-22 01:32:02 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11427.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `404955` |
| **Live PASS (pool hits)** | `1251` |
| **Live FAIL** | `88724` |
| **History retained** | `994` |
| **New PASS** | `257` |
| **History dropped** | `210` |
| **Previous public** | `1204` |
| **Published profiles (deduped)** | `1251` |
| **Share links (exportable)** | `1119` |
| **YAML proxies (exportable)** | `1119` |
| **Protocol mix** | `{"hysteria2": 71, "vless": 446, "shadowsocks": 400, "vmess": 119, "trojan": 83}` |
| **Country mix** | `{"US": 284, "RU": 29, "IT": 21, "AT": 2, "BY": 7, "DE": 95, "NL": 131, "HK": 17, "SG": 53, "CN": 2, "TR": 36, "IE": 1, "NO": 1, "FI": 14, "CA": 102, "ZA": 3, "CH": 16, "FR": 33, "JP": 43, "GB": 39, "PL": 46, "LT": 7, "KR": 15, "ES": 19, "IN": 4, "CL": 1, "BR": 15, "AU": 5, "TW": 7, "SE": 14, "AE": 3, "LV": 12, "EE": 12, "GR": 1, "DK": 1, "VN": 2, "KZ": 2, "NE": 4, "NG": 2, "AL": 1, "UA": 1, "SK": 3, "MY": 1, "TH": 1, "IR": 3, "RO": 1, "BG": 8, "IL": 2, "SA": 1}` |
| **Line type mix** | `{"dc": 467, "proxy": 450, "home": 125, "mobile": 81}` |

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
