# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-29 09:59:33](https://img.shields.io/badge/updated-2026--09--29_09%3A59%3A33-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10241.4s](https://img.shields.io/badge/elapsed-10241.4s-lightgrey)
![profiles: 3184](https://img.shields.io/badge/profiles-3184-blue)
![live_hits: 3184](https://img.shields.io/badge/live__hits-3184-brightgreen)
![live_fail: 76282](https://img.shields.io/badge/live__fail-76282-orange)
![kept: 999](https://img.shields.io/badge/kept-999-blue)
![new: 2185](https://img.shields.io/badge/new-2185-success)
![dropped: 173](https://img.shields.io/badge/dropped-173-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-29 09:59:33 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10241.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `435183` |
| **Live PASS (pool hits)** | `3184` |
| **Live FAIL** | `76282` |
| **History retained** | `999` |
| **New PASS** | `2185` |
| **History dropped** | `173` |
| **Previous public** | `1172` |
| **Published profiles (deduped)** | `3184` |
| **Share links (exportable)** | `1917` |
| **YAML proxies (exportable)** | `1917` |
| **Protocol mix** | `{"vless": 1399, "shadowsocks": 284, "vmess": 85, "hysteria2": 130, "trojan": 19}` |
| **Country mix** | `{"US": 270, "CZ": 5, "NL": 162, "CA": 685, "GB": 98, "ES": 15, "ID": 1, "DE": 92, "SG": 68, "FR": 33, "RO": 6, "ZA": 4, "CH": 9, "PL": 28, "FI": 32, "JP": 54, "IN": 18, "SE": 20, "TR": 3, "RU": 39, "TW": 7, "LV": 12, "LT": 13, "EE": 10, "HK": 54, "AE": 7, "UA": 7, "IL": 2, "IT": 20, "HU": 3, "KR": 32, "AT": 4, "AU": 5, "AD": 1, "MY": 13, "SK": 2, "IE": 1, "CN": 1, "NO": 2, "AL": 2, "MX": 2, "AM": 1, "DZ": 29, "CL": 2, "KZ": 5, "GT": 1, "GR": 3, "BG": 9, "SC": 3, "TH": 3, "GE": 1, "BE": 2, "VN": 1, "SA": 1, "CY": 3, "VG": 1, "IR": 2, "CR": 2, "BZ": 3, "UZ": 1, "MD": 2, "RS": 2, "DK": 1, "BR": 1, "AR": 1, "OM": 1}` |
| **Line type mix** | `{"proxy": 478, "home": 105, "dc": 1317, "mobile": 23}` |

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
