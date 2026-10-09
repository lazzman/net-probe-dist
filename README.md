# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-09 23:30:17](https://img.shields.io/badge/updated-2026--10--09_23%3A30%3A17-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9976.6s](https://img.shields.io/badge/elapsed-9976.6s-lightgrey)
![profiles: 1197](https://img.shields.io/badge/profiles-1197-blue)
![live_hits: 1197](https://img.shields.io/badge/live__hits-1197-brightgreen)
![live_fail: 76528](https://img.shields.io/badge/live__fail-76528-orange)
![kept: 839](https://img.shields.io/badge/kept-839-blue)
![new: 358](https://img.shields.io/badge/new-358-success)
![dropped: 868](https://img.shields.io/badge/dropped-868-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-09 23:30:17 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9976.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `412266` |
| **Live PASS (pool hits)** | `1197` |
| **Live FAIL** | `76528` |
| **History retained** | `839` |
| **New PASS** | `358` |
| **History dropped** | `868` |
| **Previous public** | `1707` |
| **Published profiles (deduped)** | `1197` |
| **Share links (exportable)** | `1020` |
| **YAML proxies (exportable)** | `1020` |
| **Protocol mix** | `{"vless": 463, "hysteria2": 116, "shadowsocks": 266, "trojan": 118, "vmess": 57}` |
| **Country mix** | `{"US": 157, "FI": 16, "CA": 124, "GB": 29, "NL": 165, "ZA": 4, "DE": 84, "FR": 29, "IN": 9, "RO": 5, "CH": 10, "JP": 59, "BG": 7, "SG": 42, "KR": 47, "LV": 22, "PL": 26, "ES": 11, "EE": 9, "AT": 2, "RU": 26, "TR": 7, "SE": 5, "AE": 2, "TH": 3, "IT": 16, "KZ": 4, "MY": 10, "AM": 1, "ID": 3, "HK": 40, "TW": 4, "IE": 4, "NO": 1, "SC": 3, "AU": 4, "UA": 1, "IS": 1, "GR": 1, "AL": 2, "IL": 1, "CZ": 1, "LT": 8, "SA": 1, "CN": 16}` |
| **Line type mix** | `{"dc": 592, "proxy": 344, "home": 77, "mobile": 9}` |

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
