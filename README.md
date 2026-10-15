# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-15 08:11:31](https://img.shields.io/badge/updated-2026--10--15_08%3A11%3A31-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10043.2s](https://img.shields.io/badge/elapsed-10043.2s-lightgrey)
![profiles: 1208](https://img.shields.io/badge/profiles-1208-blue)
![live_hits: 1208](https://img.shields.io/badge/live__hits-1208-brightgreen)
![live_fail: 77213](https://img.shields.io/badge/live__fail-77213-orange)
![kept: 809](https://img.shields.io/badge/kept-809-blue)
![new: 399](https://img.shields.io/badge/new-399-success)
![dropped: 117](https://img.shields.io/badge/dropped-117-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-15 08:11:31 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10043.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `412579` |
| **Live PASS (pool hits)** | `1208` |
| **Live FAIL** | `77213` |
| **History retained** | `809` |
| **New PASS** | `399` |
| **History dropped** | `117` |
| **Previous public** | `926` |
| **Published profiles (deduped)** | `1208` |
| **Share links (exportable)** | `1021` |
| **YAML proxies (exportable)** | `1021` |
| **Protocol mix** | `{"vless": 517, "hysteria2": 104, "shadowsocks": 248, "trojan": 90, "vmess": 62}` |
| **Country mix** | `{"US": 169, "GB": 24, "RU": 25, "NL": 166, "HK": 42, "ZA": 4, "IR": 3, "NO": 1, "DE": 67, "CH": 43, "RO": 5, "CA": 164, "JP": 32, "SE": 12, "IN": 5, "KR": 36, "SG": 40, "CR": 1, "TW": 6, "FR": 26, "FI": 17, "ZZ": 1, "PL": 18, "AE": 6, "IT": 16, "IE": 1, "ME": 7, "ES": 11, "LV": 13, "LT": 11, "TR": 4, "AM": 1, "TH": 2, "KZ": 5, "CN": 2, "UA": 1, "SC": 3, "EE": 3, "BR": 1, "MD": 1, "CZ": 2, "GR": 1, "AL": 1, "ID": 1, "MY": 5, "DK": 1, "KH": 1, "SA": 1, "AU": 3, "BG": 8, "IL": 1, "BZ": 1, "VN": 1}` |
| **Line type mix** | `{"dc": 543, "proxy": 347, "home": 87, "unknown": 1, "mobile": 44}` |

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
