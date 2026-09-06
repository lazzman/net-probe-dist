# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-06 21:13:16](https://img.shields.io/badge/updated-2026--09--06_21%3A13%3A16-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9881.8s](https://img.shields.io/badge/elapsed-9881.8s-lightgrey)
![profiles: 2000](https://img.shields.io/badge/profiles-2000-blue)
![live_hits: 2000](https://img.shields.io/badge/live__hits-2000-brightgreen)
![live_fail: 74146](https://img.shields.io/badge/live__fail-74146-orange)
![kept: 1192](https://img.shields.io/badge/kept-1192-blue)
![new: 808](https://img.shields.io/badge/new-808-success)
![dropped: 917](https://img.shields.io/badge/dropped-917-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-06 21:13:16 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9881.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `437606` |
| **Live PASS (pool hits)** | `2000` |
| **Live FAIL** | `74146` |
| **History retained** | `1192` |
| **New PASS** | `808` |
| **History dropped** | `917` |
| **Previous public** | `2109` |
| **Published profiles (deduped)** | `2000` |
| **Share links (exportable)** | `1364` |
| **YAML proxies (exportable)** | `1364` |
| **Protocol mix** | `{"vless": 818, "trojan": 27, "hysteria2": 175, "shadowsocks": 281, "vmess": 63}` |
| **Country mix** | `{"SK": 1, "CA": 288, "US": 204, "GB": 78, "FR": 30, "AU": 6, "DZ": 22, "RU": 23, "FI": 21, "JP": 54, "DE": 66, "NL": 232, "SG": 54, "TW": 16, "ZA": 4, "NO": 23, "PL": 37, "ES": 8, "CZ": 4, "TH": 3, "MY": 3, "CN": 3, "IE": 6, "IN": 7, "IT": 14, "HR": 1, "EE": 8, "KZ": 8, "KR": 28, "SE": 13, "AE": 1, "IR": 2, "LV": 14, "GR": 2, "HK": 36, "TR": 4, "SA": 1, "LT": 8, "HU": 1, "AT": 6, "CH": 2, "JE": 1, "AR": 2, "UA": 2, "PH": 1, "EG": 1, "AM": 1, "SC": 1, "RO": 3, "UZ": 1, "CO": 1, "BG": 6, "BR": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 847, "home": 100, "proxy": 408, "mobile": 9}` |

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
