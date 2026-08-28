# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-28 08:36:16](https://img.shields.io/badge/updated-2026--08--28_08%3A36%3A16-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9551.3s](https://img.shields.io/badge/elapsed-9551.3s-lightgrey)
![profiles: 1947](https://img.shields.io/badge/profiles-1947-blue)
![live_hits: 1947](https://img.shields.io/badge/live__hits-1947-brightgreen)
![live_fail: 70650](https://img.shields.io/badge/live__fail-70650-orange)
![kept: 1052](https://img.shields.io/badge/kept-1052-blue)
![new: 895](https://img.shields.io/badge/new-895-success)
![dropped: 585](https://img.shields.io/badge/dropped-585-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-28 08:36:16 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9551.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `419882` |
| **Live PASS (pool hits)** | `1947` |
| **Live FAIL** | `70650` |
| **History retained** | `1052` |
| **New PASS** | `895` |
| **History dropped** | `585` |
| **Previous public** | `1637` |
| **Published profiles (deduped)** | `1947` |
| **Share links (exportable)** | `1433` |
| **YAML proxies (exportable)** | `1433` |
| **Protocol mix** | `{"vless": 863, "vmess": 61, "hysteria2": 204, "shadowsocks": 276, "trojan": 29}` |
| **Country mix** | `{"CA": 297, "US": 212, "KR": 25, "PL": 33, "DE": 91, "NL": 241, "JP": 40, "DZ": 8, "RU": 39, "FI": 26, "GB": 67, "SG": 53, "CH": 6, "SE": 11, "FR": 32, "LT": 8, "ES": 6, "TH": 5, "HK": 26, "MY": 4, "CN": 8, "IE": 10, "IT": 10, "AT": 6, "EE": 10, "KZ": 14, "UA": 6, "NO": 14, "TR": 2, "GE": 1, "BG": 8, "CZ": 5, "IN": 9, "TW": 10, "AE": 2, "MD": 4, "LV": 12, "ZA": 5, "AR": 2, "AU": 5, "KG": 3, "GR": 2, "AL": 5, "PH": 1, "BR": 19, "RO": 4, "SC": 4, "MX": 3, "DK": 3, "PE": 1, "CO": 2, "SK": 2, "AM": 1, "SA": 1, "AF": 1, "BZ": 2, "CR": 1, "IL": 2, "VG": 1, "HU": 1, "DO": 1, "BY": 1, "RS": 1, "CY": 1, "CW": 1}` |
| **Line type mix** | `{"dc": 862, "home": 126, "proxy": 438, "mobile": 11}` |

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
