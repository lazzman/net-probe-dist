# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-21 23:27:11](https://img.shields.io/badge/updated-2026--08--21_23%3A27%3A11-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9122.3s](https://img.shields.io/badge/elapsed-9122.3s-lightgrey)
![profiles: 2904](https://img.shields.io/badge/profiles-2904-blue)
![live_hits: 2904](https://img.shields.io/badge/live__hits-2904-brightgreen)
![live_fail: 66875](https://img.shields.io/badge/live__fail-66875-orange)
![kept: 1639](https://img.shields.io/badge/kept-1639-blue)
![new: 1265](https://img.shields.io/badge/new-1265-success)
![dropped: 769](https://img.shields.io/badge/dropped-769-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-21 23:27:11 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9122.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `437977` |
| **Live PASS (pool hits)** | `2904` |
| **Live FAIL** | `66875` |
| **History retained** | `1639` |
| **New PASS** | `1265` |
| **History dropped** | `769` |
| **Previous public** | `2408` |
| **Published profiles (deduped)** | `2904` |
| **Share links (exportable)** | `1857` |
| **YAML proxies (exportable)** | `1857` |
| **Protocol mix** | `{"vless": 959, "hysteria2": 153, "shadowsocks": 309, "vmess": 64, "trojan": 372}` |
| **Country mix** | `{"US": 243, "FR": 59, "DE": 149, "AU": 20, "SG": 73, "PL": 42, "JP": 252, "FI": 36, "SE": 15, "NL": 281, "HK": 63, "IR": 3, "TW": 17, "CA": 284, "IN": 15, "TR": 4, "ZA": 3, "RO": 5, "ES": 6, "GB": 43, "KR": 32, "CN": 6, "RU": 34, "IT": 14, "IE": 18, "LV": 17, "AT": 2, "BG": 9, "CH": 11, "LT": 11, "UA": 3, "VN": 2, "EE": 12, "KZ": 13, "ZZ": 1, "SK": 1, "MD": 2, "BR": 9, "DK": 2, "SC": 9, "TH": 5, "NO": 5, "BE": 2, "MY": 3, "PH": 2, "PT": 1, "AE": 1, "AL": 3, "PE": 2, "CZ": 2, "BY": 2, "HU": 1, "SA": 1, "AM": 1, "BZ": 1, "CR": 1, "OM": 1, "AF": 1, "ID": 1, "CY": 1}` |
| **Line type mix** | `{"dc": 1062, "home": 220, "proxy": 564, "mobile": 11, "unknown": 1}` |

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
