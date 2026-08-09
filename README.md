# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-10 05:34:56](https://img.shields.io/badge/updated-2026--08--10_05%3A34%3A56-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10164.2s](https://img.shields.io/badge/elapsed-10164.2s-lightgrey)
![profiles: 1662](https://img.shields.io/badge/profiles-1662-blue)
![live_hits: 1662](https://img.shields.io/badge/live__hits-1662-brightgreen)
![live_fail: 92521](https://img.shields.io/badge/live__fail-92521-orange)
![kept: 970](https://img.shields.io/badge/kept-970-blue)
![new: 692](https://img.shields.io/badge/new-692-success)
![dropped: 281](https://img.shields.io/badge/dropped-281-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-10 05:34:56 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10164.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `450487` |
| **Live PASS (pool hits)** | `1662` |
| **Live FAIL** | `92521` |
| **History retained** | `970` |
| **New PASS** | `692` |
| **History dropped** | `281` |
| **Previous public** | `1251` |
| **Published profiles (deduped)** | `1662` |
| **Share links (exportable)** | `1231` |
| **YAML proxies (exportable)** | `1231` |
| **Protocol mix** | `{"vless": 771, "shadowsocks": 191, "vmess": 77, "hysteria2": 100, "trojan": 92}` |
| **Country mix** | `{"US": 159, "NL": 216, "ES": 6, "DE": 81, "TH": 3, "AU": 5, "SE": 14, "FR": 47, "GB": 39, "IT": 6, "HK": 37, "RO": 6, "BR": 3, "FI": 28, "JP": 54, "IN": 6, "ZA": 2, "PL": 18, "BG": 3, "CA": 166, "KR": 32, "IE": 4, "SA": 3, "SC": 4, "RU": 172, "PT": 1, "TR": 5, "SG": 25, "EE": 12, "BE": 5, "CH": 2, "ZZ": 4, "KZ": 5, "TW": 8, "LT": 3, "CN": 8, "HU": 2, "CO": 5, "NO": 1, "AZ": 1, "AE": 2, "UA": 3, "CZ": 2, "MD": 2, "AM": 1, "PH": 7, "MY": 2, "AL": 2, "AT": 1, "LV": 5, "AF": 1, "KH": 1, "GR": 1, "CR": 1, "CY": 1}` |
| **Line type mix** | `{"dc": 606, "proxy": 476, "home": 138, "mobile": 9, "unknown": 4}` |

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
