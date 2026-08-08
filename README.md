# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-09 05:30:19](https://img.shields.io/badge/updated-2026--08--09_05%3A30%3A19-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10112.6s](https://img.shields.io/badge/elapsed-10112.6s-lightgrey)
![profiles: 1393](https://img.shields.io/badge/profiles-1393-blue)
![live_hits: 1393](https://img.shields.io/badge/live__hits-1393-brightgreen)
![live_fail: 92520](https://img.shields.io/badge/live__fail-92520-orange)
![kept: 868](https://img.shields.io/badge/kept-868-blue)
![new: 525](https://img.shields.io/badge/new-525-success)
![dropped: 358](https://img.shields.io/badge/dropped-358-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-09 05:30:19 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10112.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `446201` |
| **Live PASS (pool hits)** | `1393` |
| **Live FAIL** | `92520` |
| **History retained** | `868` |
| **New PASS** | `525` |
| **History dropped** | `358` |
| **Previous public** | `1226` |
| **Published profiles (deduped)** | `1393` |
| **Share links (exportable)** | `1083` |
| **YAML proxies (exportable)** | `1083` |
| **Protocol mix** | `{"vless": 617, "vmess": 85, "shadowsocks": 189, "hysteria2": 108, "trojan": 84}` |
| **Country mix** | `{"US": 143, "NL": 221, "DE": 85, "GB": 34, "ES": 7, "JP": 46, "AU": 4, "FR": 47, "IT": 5, "SE": 14, "SG": 26, "KR": 47, "TW": 9, "HK": 36, "RO": 5, "FI": 23, "AL": 1, "IN": 6, "ZA": 2, "CA": 149, "BG": 3, "IE": 3, "PL": 11, "RU": 71, "PT": 1, "KZ": 6, "EE": 9, "CH": 3, "CZ": 1, "AE": 1, "TR": 4, "CO": 7, "SC": 4, "BE": 1, "LT": 5, "TH": 2, "LV": 8, "PH": 7, "CN": 7, "SA": 3, "AZ": 1, "NO": 1, "AT": 2, "MD": 1, "MY": 1, "BR": 1, "HU": 1, "AM": 1, "VN": 1, "GR": 1, "AF": 1, "IR": 1, "UA": 1, "CY": 1, "DK": 1, "KH": 1}` |
| **Line type mix** | `{"dc": 541, "proxy": 442, "home": 96, "mobile": 5}` |

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
