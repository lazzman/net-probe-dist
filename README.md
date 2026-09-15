# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-15 14:31:07](https://img.shields.io/badge/updated-2026--09--15_14%3A31%3A07-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9802.3s](https://img.shields.io/badge/elapsed-9802.3s-lightgrey)
![profiles: 4172](https://img.shields.io/badge/profiles-4172-blue)
![live_hits: 4173](https://img.shields.io/badge/live__hits-4173-brightgreen)
![live_fail: 72542](https://img.shields.io/badge/live__fail-72542-orange)
![kept: 1150](https://img.shields.io/badge/kept-1150-blue)
![new: 3023](https://img.shields.io/badge/new-3023-success)
![dropped: 252](https://img.shields.io/badge/dropped-252-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-15 14:31:07 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9802.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `428057` |
| **Live PASS (pool hits)** | `4173` |
| **Live FAIL** | `72542` |
| **History retained** | `1150` |
| **New PASS** | `3023` |
| **History dropped** | `252` |
| **Previous public** | `1402` |
| **Published profiles (deduped)** | `4172` |
| **Share links (exportable)** | `2293` |
| **YAML proxies (exportable)** | `2293` |
| **Protocol mix** | `{"vless": 1692, "hysteria2": 150, "vmess": 130, "shadowsocks": 239, "trojan": 82}` |
| **Country mix** | `{"DE": 94, "SG": 45, "GB": 115, "NL": 219, "CA": 1064, "JP": 35, "US": 282, "PL": 25, "RU": 35, "IN": 15, "SE": 15, "IE": 1, "NO": 4, "ID": 2, "RO": 3, "ES": 9, "FI": 24, "MX": 1, "IT": 14, "DK": 3, "KR": 34, "HR": 2, "AT": 3, "TW": 18, "EE": 14, "UZ": 2, "CZ": 4, "IR": 3, "AE": 4, "TH": 6, "RS": 1, "FR": 28, "UA": 5, "HK": 45, "GR": 2, "GT": 1, "TR": 3, "SC": 8, "SA": 2, "MY": 6, "AM": 1, "KZ": 7, "LT": 15, "ZA": 3, "DZ": 24, "BR": 2, "CH": 3, "BG": 10, "MD": 1, "AU": 6, "NZ": 1, "PT": 1, "CN": 1, "BZ": 3, "CW": 4, "ME": 1, "LV": 11, "BA": 1, "BE": 1, "CY": 4, "VN": 2, "VG": 1, "CR": 1, "MO": 1, "AL": 1}` |
| **Line type mix** | `{"dc": 1682, "proxy": 512, "home": 102, "mobile": 6}` |

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
