# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-22 10:05:41](https://img.shields.io/badge/updated-2026--11--22_10%3A05%3A41-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11429.2s](https://img.shields.io/badge/elapsed-11429.2s-lightgrey)
![profiles: 1650](https://img.shields.io/badge/profiles-1650-blue)
![live_hits: 1650](https://img.shields.io/badge/live__hits-1650-brightgreen)
![live_fail: 88401](https://img.shields.io/badge/live__fail-88401-orange)
![kept: 992](https://img.shields.io/badge/kept-992-blue)
![new: 658](https://img.shields.io/badge/new-658-success)
![dropped: 127](https://img.shields.io/badge/dropped-127-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-22 10:05:41 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11429.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `405411` |
| **Live PASS (pool hits)** | `1650` |
| **Live FAIL** | `88401` |
| **History retained** | `992` |
| **New PASS** | `658` |
| **History dropped** | `127` |
| **Previous public** | `1119` |
| **Published profiles (deduped)** | `1650` |
| **Share links (exportable)** | `1426` |
| **YAML proxies (exportable)** | `1426` |
| **Protocol mix** | `{"shadowsocks": 412, "vless": 709, "hysteria2": 79, "vmess": 136, "trojan": 90}` |
| **Country mix** | `{"DE": 120, "US": 318, "CH": 17, "IT": 21, "AT": 3, "BY": 7, "RU": 28, "SG": 75, "GB": 50, "CN": 2, "NL": 154, "AL": 3, "IE": 2, "FI": 15, "NO": 1, "CA": 212, "ZA": 5, "FR": 36, "JP": 51, "PL": 63, "ES": 31, "LV": 13, "LT": 6, "KR": 16, "IN": 5, "BR": 15, "CL": 1, "TW": 8, "AE": 4, "EE": 13, "HK": 37, "TR": 24, "GR": 1, "DK": 2, "UA": 3, "SE": 19, "VN": 2, "KZ": 3, "RO": 2, "MY": 2, "AU": 6, "NE": 6, "NG": 2, "LY": 1, "SK": 3, "TH": 1, "IR": 3, "BG": 8, "IL": 1, "SA": 1, "BZ": 1, "AM": 1, "VG": 1, "MD": 1, "CZ": 1}` |
| **Line type mix** | `{"dc": 696, "proxy": 515, "mobile": 89, "home": 127}` |

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
