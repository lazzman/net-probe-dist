# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-16 21:41:13](https://img.shields.io/badge/updated-2026--10--16_21%3A41%3A13-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10109.7s](https://img.shields.io/badge/elapsed-10109.7s-lightgrey)
![profiles: 1137](https://img.shields.io/badge/profiles-1137-blue)
![live_hits: 1138](https://img.shields.io/badge/live__hits-1138-brightgreen)
![live_fail: 77583](https://img.shields.io/badge/live__fail-77583-orange)
![kept: 825](https://img.shields.io/badge/kept-825-blue)
![new: 313](https://img.shields.io/badge/new-313-success)
![dropped: 545](https://img.shields.io/badge/dropped-545-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-16 21:41:13 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10109.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `414985` |
| **Live PASS (pool hits)** | `1138` |
| **Live FAIL** | `77583` |
| **History retained** | `825` |
| **New PASS** | `313` |
| **History dropped** | `545` |
| **Previous public** | `1370` |
| **Published profiles (deduped)** | `1137` |
| **Share links (exportable)** | `966` |
| **YAML proxies (exportable)** | `966` |
| **Protocol mix** | `{"vless": 488, "hysteria2": 100, "shadowsocks": 240, "trojan": 86, "vmess": 52}` |
| **Country mix** | `{"US": 148, "PL": 20, "NL": 179, "RU": 20, "GB": 23, "ZA": 5, "HK": 32, "DE": 52, "CH": 41, "JP": 34, "CA": 164, "IN": 8, "TH": 3, "KR": 31, "SG": 44, "ME": 5, "AT": 1, "LV": 11, "TW": 6, "FR": 23, "EE": 4, "BY": 6, "AL": 3, "SE": 5, "FI": 12, "MD": 2, "AE": 4, "IT": 14, "KZ": 5, "BR": 14, "CZ": 2, "LT": 6, "AM": 1, "ID": 3, "MX": 1, "NO": 1, "HU": 3, "SA": 1, "RO": 4, "AU": 2, "BG": 5, "EG": 1, "TR": 6, "ES": 4, "SC": 2, "KH": 1, "CY": 1, "VN": 2, "MY": 1, "DK": 1, "CN": 2, "UA": 1}` |
| **Line type mix** | `{"dc": 510, "proxy": 311, "home": 109, "mobile": 40}` |

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
