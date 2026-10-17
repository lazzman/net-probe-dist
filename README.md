# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-18 07:02:59](https://img.shields.io/badge/updated-2026--10--18_07%3A02%3A59-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10112.5s](https://img.shields.io/badge/elapsed-10112.5s-lightgrey)
![profiles: 1118](https://img.shields.io/badge/profiles-1118-blue)
![live_hits: 1118](https://img.shields.io/badge/live__hits-1118-brightgreen)
![live_fail: 77908](https://img.shields.io/badge/live__fail-77908-orange)
![kept: 813](https://img.shields.io/badge/kept-813-blue)
![new: 305](https://img.shields.io/badge/new-305-success)
![dropped: 211](https://img.shields.io/badge/dropped-211-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-18 07:02:59 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10112.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `413407` |
| **Live PASS (pool hits)** | `1118` |
| **Live FAIL** | `77908` |
| **History retained** | `813` |
| **New PASS** | `305` |
| **History dropped** | `211` |
| **Previous public** | `1024` |
| **Published profiles (deduped)** | `1118` |
| **Share links (exportable)** | `973` |
| **YAML proxies (exportable)** | `973` |
| **Protocol mix** | `{"vless": 505, "hysteria2": 102, "shadowsocks": 222, "trojan": 78, "vmess": 66}` |
| **Country mix** | `{"US": 143, "RU": 27, "CH": 40, "ZA": 3, "GB": 25, "NL": 170, "AU": 3, "HK": 34, "DE": 61, "RO": 3, "CA": 158, "JP": 39, "KR": 30, "IN": 6, "IT": 10, "PL": 22, "TH": 4, "BG": 5, "SG": 51, "ES": 7, "CR": 1, "AT": 1, "ME": 3, "TW": 4, "KH": 1, "FR": 21, "BY": 5, "FI": 14, "SE": 9, "LV": 10, "HU": 4, "TR": 7, "AE": 4, "IR": 3, "CZ": 3, "PH": 7, "SA": 1, "LT": 7, "AM": 1, "EE": 4, "CL": 1, "NO": 1, "ID": 3, "KZ": 4, "AL": 2, "SC": 2, "MD": 3, "VN": 1, "MY": 1, "BR": 2, "DK": 1, "CN": 2, "IE": 2, "IL": 1}` |
| **Line type mix** | `{"dc": 522, "home": 103, "proxy": 313, "mobile": 39}` |

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
