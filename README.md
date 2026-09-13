# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-13 21:59:37](https://img.shields.io/badge/updated-2026--09--13_21%3A59%3A37-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9750.6s](https://img.shields.io/badge/elapsed-9750.6s-lightgrey)
![profiles: 1715](https://img.shields.io/badge/profiles-1715-blue)
![live_hits: 1715](https://img.shields.io/badge/live__hits-1715-brightgreen)
![live_fail: 74354](https://img.shields.io/badge/live__fail-74354-orange)
![kept: 1160](https://img.shields.io/badge/kept-1160-blue)
![new: 555](https://img.shields.io/badge/new-555-success)
![dropped: 1181](https://img.shields.io/badge/dropped-1181-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-13 21:59:37 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9750.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `431966` |
| **Live PASS (pool hits)** | `1715` |
| **Live FAIL** | `74354` |
| **History retained** | `1160` |
| **New PASS** | `555` |
| **History dropped** | `1181` |
| **Previous public** | `2341` |
| **Published profiles (deduped)** | `1715` |
| **Share links (exportable)** | `1324` |
| **YAML proxies (exportable)** | `1324` |
| **Protocol mix** | `{"trojan": 42, "vmess": 65, "vless": 824, "hysteria2": 154, "shadowsocks": 239}` |
| **Country mix** | `{"US": 198, "CA": 424, "GB": 55, "NL": 188, "DE": 54, "DZ": 24, "RU": 20, "FI": 14, "JP": 38, "SE": 13, "NO": 5, "ID": 1, "FR": 28, "IE": 1, "PL": 24, "SG": 27, "ES": 8, "MX": 1, "DK": 1, "IT": 7, "AT": 2, "HR": 1, "TW": 13, "EE": 6, "TR": 4, "UZ": 2, "CH": 3, "IN": 8, "HK": 62, "AE": 3, "UA": 3, "GR": 1, "TH": 3, "CZ": 2, "GT": 1, "AZ": 2, "RO": 5, "SA": 1, "MY": 3, "LT": 11, "AM": 1, "KR": 25, "ZA": 4, "AL": 1, "LV": 10, "ZZ": 1, "KZ": 4, "AU": 4, "SC": 2, "BG": 3, "CL": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 898, "proxy": 355, "home": 64, "mobile": 6, "unknown": 1}` |

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
