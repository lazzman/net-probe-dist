# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-03 21:33:34](https://img.shields.io/badge/updated-2026--09--03_21%3A33%3A34-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9765.3s](https://img.shields.io/badge/elapsed-9765.3s-lightgrey)
![profiles: 1986](https://img.shields.io/badge/profiles-1986-blue)
![live_hits: 1986](https://img.shields.io/badge/live__hits-1986-brightgreen)
![live_fail: 73026](https://img.shields.io/badge/live__fail-73026-orange)
![kept: 1208](https://img.shields.io/badge/kept-1208-blue)
![new: 778](https://img.shields.io/badge/new-778-success)
![dropped: 1032](https://img.shields.io/badge/dropped-1032-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-03 21:33:34 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9765.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `424226` |
| **Live PASS (pool hits)** | `1986` |
| **Live FAIL** | `73026` |
| **History retained** | `1208` |
| **New PASS** | `778` |
| **History dropped** | `1032` |
| **Previous public** | `2240` |
| **Published profiles (deduped)** | `1986` |
| **Share links (exportable)** | `1378` |
| **YAML proxies (exportable)** | `1378` |
| **Protocol mix** | `{"shadowsocks": 252, "vless": 838, "hysteria2": 188, "trojan": 44, "vmess": 56}` |
| **Country mix** | `{"NL": 226, "PL": 31, "FR": 28, "KR": 36, "JP": 57, "CA": 262, "FI": 26, "DZ": 19, "GB": 69, "US": 233, "RU": 33, "IT": 9, "DE": 78, "LV": 9, "SE": 9, "TW": 23, "ID": 1, "ES": 7, "NO": 22, "ZA": 4, "TH": 3, "MY": 3, "CN": 5, "CO": 2, "AT": 3, "KZ": 9, "SG": 59, "IN": 7, "BR": 5, "EE": 7, "TR": 8, "IR": 2, "AL": 2, "UA": 3, "GR": 2, "HK": 30, "SC": 5, "AU": 4, "LT": 9, "ZZ": 2, "SA": 1, "AM": 1, "PH": 3, "CZ": 3, "AE": 1, "SK": 1, "HU": 1, "AR": 2, "JE": 1, "UZ": 1, "MD": 1, "BY": 1, "EG": 1, "CH": 2, "RO": 2, "CR": 1, "IE": 2, "MX": 2}` |
| **Line type mix** | `{"proxy": 393, "home": 116, "dc": 856, "mobile": 12, "unknown": 2}` |

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
