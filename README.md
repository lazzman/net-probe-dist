# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-14 00:08:07](https://img.shields.io/badge/updated-2026--08--14_00%3A08%3A07-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10334.2s](https://img.shields.io/badge/elapsed-10334.2s-lightgrey)
![profiles: 1847](https://img.shields.io/badge/profiles-1847-blue)
![live_hits: 1847](https://img.shields.io/badge/live__hits-1847-brightgreen)
![live_fail: 92944](https://img.shields.io/badge/live__fail-92944-orange)
![kept: 1123](https://img.shields.io/badge/kept-1123-blue)
![new: 724](https://img.shields.io/badge/new-724-success)
![dropped: 605](https://img.shields.io/badge/dropped-605-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-14 00:08:07 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10334.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `445841` |
| **Live PASS (pool hits)** | `1847` |
| **Live FAIL** | `92944` |
| **History retained** | `1123` |
| **New PASS** | `724` |
| **History dropped** | `605` |
| **Previous public** | `1728` |
| **Published profiles (deduped)** | `1847` |
| **Share links (exportable)** | `1338` |
| **YAML proxies (exportable)** | `1338` |
| **Protocol mix** | `{"vmess": 77, "shadowsocks": 216, "vless": 720, "hysteria2": 88, "trojan": 237}` |
| **Country mix** | `{"US": 185, "CA": 195, "NL": 185, "AU": 9, "GB": 58, "TH": 5, "JP": 114, "IN": 12, "FR": 43, "KR": 76, "DE": 86, "HK": 51, "SG": 42, "TW": 8, "FI": 33, "RO": 10, "PL": 28, "ES": 9, "ZA": 3, "IT": 8, "BG": 2, "KZ": 10, "TR": 9, "RU": 91, "EE": 8, "SE": 11, "IR": 2, "CH": 1, "CZ": 2, "MD": 1, "ZZ": 1, "CN": 4, "LT": 4, "IE": 8, "SC": 5, "NO": 1, "AZ": 1, "PT": 1, "AT": 2, "MY": 1, "AL": 3, "AE": 1, "UA": 1, "LV": 3, "HU": 1, "SA": 1, "AM": 1, "CR": 1, "CY": 1, "KH": 1}` |
| **Line type mix** | `{"dc": 749, "proxy": 479, "home": 105, "mobile": 5, "unknown": 1}` |

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
