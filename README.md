# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-20 23:27:37](https://img.shields.io/badge/updated-2026--08--20_23%3A27%3A37-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9043.2s](https://img.shields.io/badge/elapsed-9043.2s-lightgrey)
![profiles: 2851](https://img.shields.io/badge/profiles-2851-blue)
![live_hits: 2851](https://img.shields.io/badge/live__hits-2851-brightgreen)
![live_fail: 66364](https://img.shields.io/badge/live__fail-66364-orange)
![kept: 1602](https://img.shields.io/badge/kept-1602-blue)
![new: 1249](https://img.shields.io/badge/new-1249-success)
![dropped: 876](https://img.shields.io/badge/dropped-876-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-20 23:27:37 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9043.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `432278` |
| **Live PASS (pool hits)** | `2851` |
| **Live FAIL** | `66364` |
| **History retained** | `1602` |
| **New PASS** | `1249` |
| **History dropped** | `876` |
| **Previous public** | `2478` |
| **Published profiles (deduped)** | `2851` |
| **Share links (exportable)** | `1782` |
| **YAML proxies (exportable)** | `1782` |
| **Protocol mix** | `{"vless": 979, "hysteria2": 146, "vmess": 52, "shadowsocks": 238, "trojan": 367}` |
| **Country mix** | `{"US": 269, "DE": 127, "SG": 62, "AU": 19, "NL": 288, "FR": 60, "SE": 30, "JP": 240, "FI": 39, "GB": 41, "BR": 7, "ZA": 4, "CA": 243, "PL": 41, "IN": 11, "AL": 4, "ES": 5, "RO": 4, "RU": 41, "TR": 12, "IE": 18, "HK": 63, "EE": 20, "TW": 10, "IT": 7, "PT": 1, "LV": 11, "CH": 9, "LT": 5, "VN": 2, "KG": 1, "KZ": 10, "CO": 4, "SK": 1, "AT": 1, "MD": 2, "DK": 3, "CN": 3, "MY": 2, "SC": 14, "TH": 5, "KR": 14, "NO": 6, "BE": 2, "AE": 1, "CZ": 3, "PE": 2, "BG": 2, "UA": 3, "IL": 2, "GR": 2, "BY": 1, "HU": 1, "PH": 1, "SA": 1, "DZ": 2, "BZ": 1, "CR": 1, "CY": 1}` |
| **Line type mix** | `{"dc": 1080, "home": 185, "proxy": 512, "mobile": 8}` |

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
