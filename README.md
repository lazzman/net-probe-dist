# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-15 12:13:11](https://img.shields.io/badge/updated-2026--08--15_12%3A13%3A11-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10119.6s](https://img.shields.io/badge/elapsed-10119.6s-lightgrey)
![profiles: 4045](https://img.shields.io/badge/profiles-4045-blue)
![live_hits: 4045](https://img.shields.io/badge/live__hits-4045-brightgreen)
![live_fail: 90559](https://img.shields.io/badge/live__fail-90559-orange)
![kept: 1134](https://img.shields.io/badge/kept-1134-blue)
![new: 2911](https://img.shields.io/badge/new-2911-success)
![dropped: 163](https://img.shields.io/badge/dropped-163-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-15 12:13:11 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10119.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `439684` |
| **Live PASS (pool hits)** | `4045` |
| **Live FAIL** | `90559` |
| **History retained** | `1134` |
| **New PASS** | `2911` |
| **History dropped** | `163` |
| **Previous public** | `1297` |
| **Published profiles (deduped)** | `4045` |
| **Share links (exportable)** | `2408` |
| **YAML proxies (exportable)** | `2408` |
| **Protocol mix** | `{"vless": 1596, "hysteria2": 116, "vmess": 88, "shadowsocks": 214, "trojan": 394}` |
| **Country mix** | `{"US": 289, "NL": 242, "GB": 134, "AU": 13, "CA": 714, "FR": 46, "TH": 5, "FI": 50, "DZ": 1, "RU": 146, "DE": 129, "JP": 171, "TW": 7, "PL": 28, "NO": 3, "IN": 11, "ZA": 4, "RO": 7, "SG": 94, "KZ": 14, "KR": 103, "IR": 3, "IT": 12, "IE": 13, "ES": 11, "SC": 15, "PT": 1, "EE": 10, "LV": 8, "CH": 3, "BG": 7, "CZ": 3, "AE": 2, "HK": 51, "TR": 5, "MD": 1, "LT": 5, "SE": 10, "ID": 1, "CY": 4, "BZ": 7, "AZ": 1, "GR": 1, "AL": 1, "CN": 4, "AT": 4, "SA": 1, "HU": 3, "CW": 4, "ME": 1, "AM": 1, "UA": 3, "CR": 2, "NZ": 1, "BR": 1, "DK": 2, "KH": 1}` |
| **Line type mix** | `{"dc": 1573, "proxy": 655, "home": 173, "mobile": 13}` |

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
