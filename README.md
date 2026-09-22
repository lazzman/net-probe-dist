# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-22 08:38:17](https://img.shields.io/badge/updated-2026--09--22_08%3A38%3A17-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10058.9s](https://img.shields.io/badge/elapsed-10058.9s-lightgrey)
![profiles: 2176](https://img.shields.io/badge/profiles-2176-blue)
![live_hits: 2176](https://img.shields.io/badge/live__hits-2176-brightgreen)
![live_fail: 76238](https://img.shields.io/badge/live__fail-76238-orange)
![kept: 1228](https://img.shields.io/badge/kept-1228-blue)
![new: 948](https://img.shields.io/badge/new-948-success)
![dropped: 334](https://img.shields.io/badge/dropped-334-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-22 08:38:17 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10058.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `427723` |
| **Live PASS (pool hits)** | `2176` |
| **Live FAIL** | `76238` |
| **History retained** | `1228` |
| **New PASS** | `948` |
| **History dropped** | `334` |
| **Previous public** | `1562` |
| **Published profiles (deduped)** | `2176` |
| **Share links (exportable)** | `1710` |
| **YAML proxies (exportable)** | `1710` |
| **Protocol mix** | `{"trojan": 41, "hysteria2": 110, "vless": 1251, "shadowsocks": 239, "vmess": 69}` |
| **Country mix** | `{"NL": 178, "DK": 5, "RU": 20, "CA": 469, "US": 274, "GB": 51, "KR": 40, "ES": 15, "AU": 9, "DE": 82, "SE": 16, "TW": 14, "ID": 2, "ZA": 4, "FR": 40, "RO": 5, "CH": 10, "JP": 59, "FI": 31, "IN": 15, "AT": 4, "PL": 26, "TR": 4, "SG": 47, "TH": 5, "BG": 11, "IT": 20, "AL": 1, "CZ": 11, "SA": 11, "CY": 12, "KZ": 15, "BZ": 10, "BE": 2, "EE": 8, "ME": 2, "HK": 83, "AM": 3, "MY": 8, "NO": 3, "IQ": 1, "DZ": 25, "HU": 2, "SC": 4, "LV": 10, "AE": 5, "CL": 4, "BR": 5, "GT": 1, "IE": 4, "LU": 1, "IS": 2, "MD": 3, "GR": 2, "UZ": 4, "SK": 1, "LT": 5, "VN": 1, "IR": 2, "CR": 2, "CN": 1, "UA": 1, "RS": 2, "AR": 1}` |
| **Line type mix** | `{"dc": 1168, "proxy": 433, "home": 105, "mobile": 8}` |

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
