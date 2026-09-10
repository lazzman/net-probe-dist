# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-11 07:14:47](https://img.shields.io/badge/updated-2026--09--11_07%3A14%3A47-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9793.5s](https://img.shields.io/badge/elapsed-9793.5s-lightgrey)
![profiles: 1419](https://img.shields.io/badge/profiles-1419-blue)
![live_hits: 1419](https://img.shields.io/badge/live__hits-1419-brightgreen)
![live_fail: 74881](https://img.shields.io/badge/live__fail-74881-orange)
![kept: 991](https://img.shields.io/badge/kept-991-blue)
![new: 428](https://img.shields.io/badge/new-428-success)
![dropped: 181](https://img.shields.io/badge/dropped-181-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-11 07:14:47 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9793.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `426240` |
| **Live PASS (pool hits)** | `1419` |
| **Live FAIL** | `74881` |
| **History retained** | `991` |
| **New PASS** | `428` |
| **History dropped** | `181` |
| **Previous public** | `1172` |
| **Published profiles (deduped)** | `1419` |
| **Share links (exportable)** | `1102` |
| **YAML proxies (exportable)** | `1102` |
| **Protocol mix** | `{"trojan": 16, "hysteria2": 159, "vless": 593, "shadowsocks": 256, "vmess": 78}` |
| **Country mix** | `{"US": 154, "SG": 37, "CA": 204, "JP": 34, "GB": 44, "AU": 3, "IN": 8, "DZ": 22, "RU": 28, "FI": 15, "DE": 61, "NL": 193, "TW": 16, "FR": 31, "RO": 4, "PL": 36, "ES": 8, "NO": 3, "IE": 11, "MY": 4, "CN": 2, "KR": 25, "IT": 8, "LV": 15, "EE": 7, "TR": 10, "AE": 3, "CH": 3, "GR": 2, "HK": 61, "SK": 1, "SE": 6, "LT": 11, "AT": 2, "EG": 1, "SA": 1, "TH": 2, "UZ": 2, "ZA": 3, "MX": 1, "ZZ": 1, "DK": 1, "KZ": 7, "CZ": 2, "UA": 2, "GT": 1, "PH": 1, "AM": 1, "SC": 1, "IR": 1, "BG": 2}` |
| **Line type mix** | `{"dc": 669, "home": 84, "proxy": 341, "mobile": 7, "unknown": 1}` |

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
