# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-06 01:30:02](https://img.shields.io/badge/updated-2026--09--06_01%3A30%3A02-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9761.2s](https://img.shields.io/badge/elapsed-9761.2s-lightgrey)
![profiles: 2020](https://img.shields.io/badge/profiles-2020-blue)
![live_hits: 2022](https://img.shields.io/badge/live__hits-2022-brightgreen)
![live_fail: 73495](https://img.shields.io/badge/live__fail-73495-orange)
![kept: 1137](https://img.shields.io/badge/kept-1137-blue)
![new: 885](https://img.shields.io/badge/new-885-success)
![dropped: 118](https://img.shields.io/badge/dropped-118-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-06 01:30:02 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9761.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `427066` |
| **Live PASS (pool hits)** | `2022` |
| **Live FAIL** | `73495` |
| **History retained** | `1137` |
| **New PASS** | `885` |
| **History dropped** | `118` |
| **Previous public** | `1255` |
| **Published profiles (deduped)** | `2020` |
| **Share links (exportable)** | `1313` |
| **YAML proxies (exportable)** | `1313` |
| **Protocol mix** | `{"vless": 775, "trojan": 51, "hysteria2": 158, "shadowsocks": 269, "vmess": 60}` |
| **Country mix** | `{"SE": 13, "NL": 229, "US": 200, "SG": 53, "JP": 54, "CA": 269, "KR": 37, "GB": 71, "DZ": 18, "IN": 7, "FI": 20, "RU": 16, "DE": 72, "AU": 5, "LV": 12, "TW": 17, "ZA": 4, "PL": 30, "FR": 29, "ID": 1, "TR": 10, "ES": 11, "LT": 6, "RO": 3, "CN": 3, "IT": 10, "KZ": 8, "NO": 22, "EE": 8, "CZ": 4, "IR": 1, "ZZ": 1, "AL": 2, "HK": 29, "GR": 2, "UZ": 3, "SK": 1, "TH": 2, "SA": 1, "MY": 3, "IE": 7, "AT": 3, "AM": 1, "HU": 1, "SC": 5, "CH": 2, "AR": 2, "JE": 1, "AE": 1, "CO": 1, "PH": 1, "EG": 1, "CR": 1, "BG": 1, "BR": 1}` |
| **Line type mix** | `{"proxy": 406, "dc": 792, "home": 107, "mobile": 10, "unknown": 1}` |

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
