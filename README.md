# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-15 08:22:23](https://img.shields.io/badge/updated-2026--09--15_08%3A22%3A23-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9768.5s](https://img.shields.io/badge/elapsed-9768.5s-lightgrey)
![profiles: 1723](https://img.shields.io/badge/profiles-1723-blue)
![live_hits: 1723](https://img.shields.io/badge/live__hits-1723-brightgreen)
![live_fail: 74938](https://img.shields.io/badge/live__fail-74938-orange)
![kept: 1091](https://img.shields.io/badge/kept-1091-blue)
![new: 632](https://img.shields.io/badge/new-632-success)
![dropped: 89](https://img.shields.io/badge/dropped-89-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-15 08:22:23 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9768.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `430490` |
| **Live PASS (pool hits)** | `1723` |
| **Live FAIL** | `74938` |
| **History retained** | `1091` |
| **New PASS** | `632` |
| **History dropped** | `89` |
| **Previous public** | `1180` |
| **Published profiles (deduped)** | `1723` |
| **Share links (exportable)** | `1402` |
| **YAML proxies (exportable)** | `1402` |
| **Protocol mix** | `{"vless": 849, "vmess": 122, "hysteria2": 161, "trojan": 27, "shadowsocks": 243}` |
| **Country mix** | `{"DE": 69, "NL": 210, "CA": 369, "SG": 36, "US": 202, "JP": 33, "IN": 11, "GB": 62, "RU": 27, "SE": 11, "ID": 1, "NO": 6, "ZA": 4, "RO": 3, "PL": 31, "ES": 10, "FI": 22, "DK": 5, "KR": 32, "IT": 8, "HR": 1, "TW": 18, "EE": 11, "UZ": 2, "FR": 33, "HK": 63, "AE": 4, "TH": 4, "UA": 3, "GR": 4, "GT": 1, "TR": 6, "LT": 12, "CZ": 5, "SA": 1, "AM": 2, "MY": 4, "KZ": 7, "DZ": 24, "CL": 1, "LV": 13, "CH": 2, "AU": 3, "SC": 1, "BA": 1, "BE": 2, "IR": 1, "RS": 1, "CY": 1, "BG": 5, "CR": 1, "CN": 1, "IL": 2, "HU": 2, "KG": 1, "DO": 1, "MD": 4, "BY": 1, "MO": 1, "BR": 1, "IE": 1, "BZ": 1, "AL": 1}` |
| **Line type mix** | `{"dc": 921, "proxy": 385, "home": 94, "mobile": 6}` |

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
