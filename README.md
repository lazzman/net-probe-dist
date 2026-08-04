# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-04 22:36:19](https://img.shields.io/badge/updated-2026--08--04_22%3A36%3A19-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 1554.2s](https://img.shields.io/badge/elapsed-1554.2s-lightgrey)
![profiles: 1176](https://img.shields.io/badge/profiles-1176-blue)
![live_hits: 1183](https://img.shields.io/badge/live__hits-1183-brightgreen)
![live_fail: 9393](https://img.shields.io/badge/live__fail-9393-orange)
![kept: 820](https://img.shields.io/badge/kept-820-blue)
![new: 363](https://img.shields.io/badge/new-363-success)
![dropped: 485](https://img.shields.io/badge/dropped-485-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-04 22:36:19 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `1554.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `28291` |
| **Live PASS (pool hits)** | `1183` |
| **Live FAIL** | `9393` |
| **History retained** | `820` |
| **New PASS** | `363` |
| **History dropped** | `485` |
| **Previous public** | `1305` |
| **Published profiles (deduped)** | `1176` |
| **Share links (exportable)** | `951` |
| **YAML proxies (exportable)** | `951` |
| **Protocol mix** | `{"vless": 594, "shadowsocks": 160, "vmess": 57, "trojan": 80, "hysteria2": 60}` |
| **Country mix** | `{"US": 143, "CA": 184, "RU": 59, "NL": 145, "FI": 23, "EE": 2, "HK": 29, "DE": 70, "GB": 20, "IT": 17, "FR": 34, "ZZ": 2, "AT": 4, "PL": 15, "CH": 1, "TW": 10, "HU": 1, "SG": 21, "PA": 1, "SE": 19, "KZ": 6, "JP": 48, "ID": 1, "MD": 1, "IR": 2, "SC": 2, "SA": 3, "PH": 16, "LT": 2, "CR": 1, "IE": 2, "IN": 4, "RO": 3, "AU": 3, "ZA": 2, "TH": 2, "ES": 5, "CO": 1, "TR": 6, "BG": 2, "KR": 26, "BH": 1, "CN": 2, "LV": 4, "BR": 2, "KH": 1, "DK": 3, "IL": 1, "AE": 1}` |
| **Line type mix** | `{"dc": 473, "proxy": 432, "unknown": 2, "home": 40, "mobile": 6}` |

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
