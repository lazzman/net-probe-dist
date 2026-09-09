# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-10 02:47:59](https://img.shields.io/badge/updated-2026--09--10_02%3A47%3A59-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9772.8s](https://img.shields.io/badge/elapsed-9772.8s-lightgrey)
![profiles: 1643](https://img.shields.io/badge/profiles-1643-blue)
![live_hits: 1646](https://img.shields.io/badge/live__hits-1646-brightgreen)
![live_fail: 74037](https://img.shields.io/badge/live__fail-74037-orange)
![kept: 995](https://img.shields.io/badge/kept-995-blue)
![new: 651](https://img.shields.io/badge/new-651-success)
![dropped: 151](https://img.shields.io/badge/dropped-151-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-10 02:47:59 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9772.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `424843` |
| **Live PASS (pool hits)** | `1646` |
| **Live FAIL** | `74037` |
| **History retained** | `995` |
| **New PASS** | `651` |
| **History dropped** | `151` |
| **Previous public** | `1146` |
| **Published profiles (deduped)** | `1643` |
| **Share links (exportable)** | `1153` |
| **YAML proxies (exportable)** | `1153` |
| **Protocol mix** | `{"vless": 628, "hysteria2": 176, "vmess": 69, "shadowsocks": 264, "trojan": 16}` |
| **Country mix** | `{"CA": 202, "JP": 40, "KR": 29, "SG": 42, "GB": 57, "FR": 25, "AU": 3, "IN": 7, "DZ": 20, "RU": 29, "FI": 31, "US": 166, "DE": 63, "NL": 209, "ID": 1, "NO": 12, "ZA": 5, "LT": 10, "PL": 31, "RO": 5, "ES": 8, "CN": 3, "IT": 6, "MY": 3, "KZ": 8, "EE": 4, "CZ": 2, "SE": 5, "TW": 17, "TR": 12, "CH": 3, "JE": 1, "HK": 46, "LV": 14, "GR": 2, "UZ": 2, "SK": 1, "EG": 1, "SA": 1, "TH": 3, "AM": 1, "AE": 4, "BR": 1, "DK": 2, "HU": 1, "AT": 1, "AR": 2, "IR": 3, "UA": 2, "PH": 1, "SC": 1, "IE": 4, "AZ": 1}` |
| **Line type mix** | `{"dc": 674, "proxy": 371, "home": 101, "mobile": 7}` |

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
