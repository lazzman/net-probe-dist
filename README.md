# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-01 14:39:13](https://img.shields.io/badge/updated-2026--09--01_14%3A39%3A13-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9522.9s](https://img.shields.io/badge/elapsed-9522.9s-lightgrey)
![profiles: 4489](https://img.shields.io/badge/profiles-4489-blue)
![live_hits: 4492](https://img.shields.io/badge/live__hits-4492-brightgreen)
![live_fail: 69404](https://img.shields.io/badge/live__fail-69404-orange)
![kept: 1521](https://img.shields.io/badge/kept-1521-blue)
![new: 2971](https://img.shields.io/badge/new-2971-success)
![dropped: 332](https://img.shields.io/badge/dropped-332-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-01 14:39:13 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9522.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `423416` |
| **Live PASS (pool hits)** | `4492` |
| **Live FAIL** | `69404` |
| **History retained** | `1521` |
| **New PASS** | `2971` |
| **History dropped** | `332` |
| **Previous public** | `1853` |
| **Published profiles (deduped)** | `4489` |
| **Share links (exportable)** | `2481` |
| **YAML proxies (exportable)** | `2481` |
| **Protocol mix** | `{"hysteria2": 181, "vless": 1865, "shadowsocks": 282, "trojan": 76, "vmess": 77}` |
| **Country mix** | `{"FI": 33, "IT": 16, "MD": 3, "PL": 36, "FR": 36, "US": 353, "NL": 256, "CA": 920, "DZ": 15, "GB": 116, "DE": 111, "RU": 55, "SE": 24, "TW": 23, "ID": 2, "LT": 16, "ES": 11, "RO": 5, "ZA": 3, "JP": 77, "SG": 90, "TH": 5, "MY": 3, "CN": 8, "KR": 39, "AT": 5, "KZ": 14, "EE": 13, "IN": 9, "NO": 16, "TR": 7, "IR": 3, "HK": 55, "DK": 1, "CH": 6, "GE": 1, "SC": 12, "LV": 13, "BR": 11, "UA": 6, "UZ": 3, "CO": 3, "SK": 1, "AU": 7, "BG": 10, "GR": 3, "AL": 4, "VN": 1, "AM": 1, "IE": 7, "CZ": 4, "AE": 2, "AR": 2, "JE": 1, "NZ": 1, "PT": 1, "CY": 1, "BZ": 4, "CW": 4, "PH": 2, "BY": 1, "EG": 1, "SA": 1, "CR": 2, "MX": 2}` |
| **Line type mix** | `{"home": 170, "dc": 1773, "proxy": 541, "mobile": 13}` |

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
