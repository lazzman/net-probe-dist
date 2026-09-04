# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-04 21:31:42](https://img.shields.io/badge/updated-2026--09--04_21%3A31%3A42-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9792.8s](https://img.shields.io/badge/elapsed-9792.8s-lightgrey)
![profiles: 2339](https://img.shields.io/badge/profiles-2339-blue)
![live_hits: 2339](https://img.shields.io/badge/live__hits-2339-brightgreen)
![live_fail: 73338](https://img.shields.io/badge/live__fail-73338-orange)
![kept: 1319](https://img.shields.io/badge/kept-1319-blue)
![new: 1020](https://img.shields.io/badge/new-1020-success)
![dropped: 1102](https://img.shields.io/badge/dropped-1102-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-04 21:31:42 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9792.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `431325` |
| **Live PASS (pool hits)** | `2339` |
| **Live FAIL** | `73338` |
| **History retained** | `1319` |
| **New PASS** | `1020` |
| **History dropped** | `1102` |
| **Previous public** | `2421` |
| **Published profiles (deduped)** | `2339` |
| **Share links (exportable)** | `1527` |
| **YAML proxies (exportable)** | `1527` |
| **Protocol mix** | `{"vless": 1015, "hysteria2": 163, "shadowsocks": 255, "trojan": 37, "vmess": 57}` |
| **Country mix** | `{"DE": 72, "SG": 57, "PL": 29, "GB": 78, "US": 234, "DZ": 19, "AU": 4, "IN": 8, "RU": 37, "FI": 24, "SE": 13, "NL": 225, "CA": 406, "ID": 1, "FR": 29, "LT": 10, "IE": 5, "JP": 64, "ES": 11, "TH": 4, "MY": 4, "CN": 2, "IT": 8, "KZ": 9, "NO": 22, "EE": 6, "TW": 23, "TR": 11, "AE": 1, "IR": 3, "AL": 1, "GR": 2, "UA": 2, "KR": 29, "HK": 29, "SA": 1, "LV": 11, "BR": 3, "ZA": 4, "SK": 1, "HU": 1, "CH": 2, "AT": 4, "JE": 1, "CZ": 3, "AR": 2, "UZ": 1, "PT": 1, "BZ": 1, "CW": 1, "BY": 1, "SC": 2, "PH": 1, "EG": 1, "AM": 1, "RO": 2, "CR": 1, "MX": 2}` |
| **Line type mix** | `{"dc": 1002, "proxy": 403, "home": 116, "mobile": 9}` |

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
