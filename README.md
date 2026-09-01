# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-01 09:19:02](https://img.shields.io/badge/updated-2026--09--01_09%3A19%3A02-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9542.8s](https://img.shields.io/badge/elapsed-9542.8s-lightgrey)
![profiles: 2600](https://img.shields.io/badge/profiles-2600-blue)
![live_hits: 2601](https://img.shields.io/badge/live__hits-2601-brightgreen)
![live_fail: 71815](https://img.shields.io/badge/live__fail-71815-orange)
![kept: 1241](https://img.shields.io/badge/kept-1241-blue)
![new: 1360](https://img.shields.io/badge/new-1360-success)
![dropped: 236](https://img.shields.io/badge/dropped-236-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-01 09:19:02 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9542.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `422285` |
| **Live PASS (pool hits)** | `2601` |
| **Live FAIL** | `71815` |
| **History retained** | `1241` |
| **New PASS** | `1360` |
| **History dropped** | `236` |
| **Previous public** | `1477` |
| **Published profiles (deduped)** | `2600` |
| **Share links (exportable)** | `1853` |
| **YAML proxies (exportable)** | `1853` |
| **Protocol mix** | `{"hysteria2": 210, "vless": 1237, "shadowsocks": 282, "trojan": 38, "vmess": 86}` |
| **Country mix** | `{"DE": 109, "CA": 383, "FR": 32, "NL": 250, "US": 268, "FI": 51, "MD": 7, "IT": 11, "DZ": 19, "RU": 39, "SE": 14, "SG": 92, "TW": 23, "PL": 33, "LT": 16, "ES": 16, "ZA": 4, "HK": 42, "GB": 120, "TH": 4, "MY": 6, "CN": 10, "JP": 74, "KR": 33, "KZ": 15, "EE": 7, "NO": 18, "IN": 7, "TR": 7, "CZ": 8, "AE": 3, "IR": 3, "DK": 3, "CH": 5, "GR": 5, "UA": 5, "BR": 14, "UZ": 2, "SK": 2, "BG": 6, "AL": 6, "LV": 15, "VN": 1, "ID": 2, "SC": 6, "IE": 8, "SA": 1, "AT": 5, "AR": 2, "AU": 6, "CO": 4, "RO": 5, "AM": 2, "GE": 1, "JE": 1, "BZ": 2, "PH": 2, "CR": 2, "BE": 1, "IL": 2, "VG": 1, "HU": 3, "KG": 1, "RS": 2, "MX": 3, "DO": 1, "BY": 2, "CL": 1}` |
| **Line type mix** | `{"dc": 1210, "proxy": 485, "home": 149, "mobile": 10}` |

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
