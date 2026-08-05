# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-06 03:54:48](https://img.shields.io/badge/updated-2026--08--06_03%3A54%3A48-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 1554.6s](https://img.shields.io/badge/elapsed-1554.6s-lightgrey)
![profiles: 1237](https://img.shields.io/badge/profiles-1237-blue)
![live_hits: 1239](https://img.shields.io/badge/live__hits-1239-brightgreen)
![live_fail: 9349](https://img.shields.io/badge/live__fail-9349-orange)
![kept: 834](https://img.shields.io/badge/kept-834-blue)
![new: 405](https://img.shields.io/badge/new-405-success)
![dropped: 238](https://img.shields.io/badge/dropped-238-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-06 03:54:48 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `1554.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `30339` |
| **Live PASS (pool hits)** | `1239` |
| **Live FAIL** | `9349` |
| **History retained** | `834` |
| **New PASS** | `405` |
| **History dropped** | `238` |
| **Previous public** | `1072` |
| **Published profiles (deduped)** | `1237` |
| **Share links (exportable)** | `1012` |
| **YAML proxies (exportable)** | `1012` |
| **Protocol mix** | `{"vless": 574, "shadowsocks": 178, "vmess": 70, "trojan": 100, "hysteria2": 90}` |
| **Country mix** | `{"US": 155, "FR": 38, "GB": 47, "IT": 21, "PT": 1, "CA": 195, "FI": 25, "RU": 47, "NL": 153, "DE": 58, "PL": 8, "LT": 3, "CH": 3, "AT": 5, "CZ": 1, "EE": 3, "AE": 1, "TW": 8, "HU": 1, "SG": 27, "LV": 6, "ES": 11, "DK": 2, "SE": 12, "KZ": 3, "TR": 5, "KR": 43, "CO": 4, "MD": 1, "TH": 3, "HK": 33, "SA": 3, "PH": 4, "CR": 1, "SC": 5, "AU": 3, "ZA": 2, "BR": 3, "JP": 41, "BG": 2, "IN": 4, "NO": 1, "IE": 6, "CN": 6, "BH": 1, "AZ": 1, "RO": 3, "PA": 1, "IR": 1, "MY": 1, "KH": 1}` |
| **Line type mix** | `{"dc": 511, "proxy": 437, "home": 57, "mobile": 8}` |

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
