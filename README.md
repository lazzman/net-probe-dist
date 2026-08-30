# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-30 14:44:23](https://img.shields.io/badge/updated-2026--08--30_14%3A44%3A23-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9603.0s](https://img.shields.io/badge/elapsed-9603.0s-lightgrey)
![profiles: 3644](https://img.shields.io/badge/profiles-3644-blue)
![live_hits: 3645](https://img.shields.io/badge/live__hits-3645-brightgreen)
![live_fail: 69327](https://img.shields.io/badge/live__fail-69327-orange)
![kept: 1294](https://img.shields.io/badge/kept-1294-blue)
![new: 2351](https://img.shields.io/badge/new-2351-success)
![dropped: 133](https://img.shields.io/badge/dropped-133-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-30 14:44:23 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9603.0s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `423776` |
| **Live PASS (pool hits)** | `3645` |
| **Live FAIL** | `69327` |
| **History retained** | `1294` |
| **New PASS** | `2351` |
| **History dropped** | `133` |
| **Previous public** | `1427` |
| **Published profiles (deduped)** | `3644` |
| **Share links (exportable)** | `2105` |
| **YAML proxies (exportable)** | `2105` |
| **Protocol mix** | `{"shadowsocks": 307, "vless": 1498, "hysteria2": 189, "trojan": 45, "vmess": 66}` |
| **Country mix** | `{"NL": 241, "IT": 16, "CA": 713, "MD": 4, "PL": 28, "KR": 34, "US": 280, "DE": 114, "DZ": 12, "RU": 31, "GB": 102, "FI": 36, "SG": 102, "SE": 14, "TW": 24, "FR": 36, "ID": 1, "LT": 14, "RO": 3, "HK": 36, "ES": 12, "JP": 87, "MY": 6, "TH": 6, "IE": 6, "CN": 5, "KZ": 11, "EE": 8, "BR": 18, "NO": 17, "IN": 9, "TR": 5, "CH": 5, "CZ": 5, "AE": 2, "BY": 1, "UA": 4, "LV": 10, "IR": 3, "CO": 5, "SK": 1, "BG": 10, "AL": 4, "GR": 2, "SC": 5, "ZA": 3, "BZ": 2, "AU": 5, "AT": 4, "PH": 1, "AR": 2, "DK": 1, "PE": 1, "AM": 1, "NZ": 1, "SA": 1, "CY": 1, "CR": 1, "MX": 2}` |
| **Line type mix** | `{"proxy": 495, "dc": 1482, "home": 127, "mobile": 10}` |

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
