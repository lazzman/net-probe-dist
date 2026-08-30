# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-31 07:22:06](https://img.shields.io/badge/updated-2026--08--31_07%3A22%3A06-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9567.7s](https://img.shields.io/badge/elapsed-9567.7s-lightgrey)
![profiles: 2020](https://img.shields.io/badge/profiles-2020-blue)
![live_hits: 2020](https://img.shields.io/badge/live__hits-2020-brightgreen)
![live_fail: 71519](https://img.shields.io/badge/live__fail-71519-orange)
![kept: 1258](https://img.shields.io/badge/kept-1258-blue)
![new: 762](https://img.shields.io/badge/new-762-success)
![dropped: 150](https://img.shields.io/badge/dropped-150-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-31 07:22:06 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9567.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `418423` |
| **Live PASS (pool hits)** | `2020` |
| **Live FAIL** | `71519` |
| **History retained** | `1258` |
| **New PASS** | `762` |
| **History dropped** | `150` |
| **Previous public** | `1408` |
| **Published profiles (deduped)** | `2020` |
| **Share links (exportable)** | `1443` |
| **YAML proxies (exportable)** | `1443` |
| **Protocol mix** | `{"shadowsocks": 265, "hysteria2": 199, "vless": 886, "trojan": 26, "vmess": 67}` |
| **Country mix** | `{"NL": 219, "KR": 19, "MD": 4, "CH": 6, "FR": 32, "CA": 231, "DE": 98, "FI": 42, "DZ": 13, "RU": 46, "IT": 10, "GB": 84, "SG": 89, "US": 227, "SE": 8, "BR": 13, "TW": 25, "PL": 28, "ID": 1, "RO": 4, "ES": 9, "LT": 14, "HK": 34, "MY": 6, "TH": 3, "CN": 9, "JP": 70, "EE": 5, "IN": 7, "TR": 4, "KZ": 7, "AE": 1, "NO": 14, "IR": 1, "UA": 3, "AT": 2, "AL": 4, "GR": 1, "LV": 13, "SC": 3, "IE": 4, "ZA": 3, "AR": 2, "AU": 3, "CZ": 4, "BG": 4, "DK": 1, "PE": 1, "CO": 5, "SK": 1, "AM": 1, "PH": 1, "GE": 1, "SA": 1, "MX": 2}` |
| **Line type mix** | `{"proxy": 401, "dc": 904, "home": 126, "mobile": 12}` |

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
