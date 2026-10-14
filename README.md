# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-15 03:31:35](https://img.shields.io/badge/updated-2026--10--15_03%3A31%3A35-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10216.7s](https://img.shields.io/badge/elapsed-10216.7s-lightgrey)
![profiles: 1097](https://img.shields.io/badge/profiles-1097-blue)
![live_hits: 1097](https://img.shields.io/badge/live__hits-1097-brightgreen)
![live_fail: 77287](https://img.shields.io/badge/live__fail-77287-orange)
![kept: 754](https://img.shields.io/badge/kept-754-blue)
![new: 343](https://img.shields.io/badge/new-343-success)
![dropped: 189](https://img.shields.io/badge/dropped-189-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-15 03:31:35 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10216.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `404222` |
| **Live PASS (pool hits)** | `1097` |
| **Live FAIL** | `77287` |
| **History retained** | `754` |
| **New PASS** | `343` |
| **History dropped** | `189` |
| **Previous public** | `943` |
| **Published profiles (deduped)** | `1097` |
| **Share links (exportable)** | `926` |
| **YAML proxies (exportable)** | `926` |
| **Protocol mix** | `{"vless": 461, "hysteria2": 103, "shadowsocks": 219, "trojan": 87, "vmess": 56}` |
| **Country mix** | `{"US": 143, "CA": 152, "GB": 25, "RU": 31, "NL": 152, "HK": 25, "ZA": 4, "CH": 43, "RO": 3, "JP": 29, "KR": 33, "DE": 64, "IN": 4, "PL": 17, "TH": 3, "SG": 40, "MX": 1, "CR": 1, "ES": 10, "TW": 5, "SE": 11, "FR": 24, "FI": 19, "IT": 13, "TR": 3, "ME": 4, "LV": 7, "LT": 11, "AM": 1, "ID": 2, "CN": 1, "KZ": 4, "NO": 1, "UA": 1, "BG": 11, "SC": 4, "EE": 4, "AE": 4, "BR": 1, "MD": 1, "CZ": 2, "AL": 2, "MY": 4, "AT": 1, "IR": 2, "AU": 3, "VN": 1, "SA": 1}` |
| **Line type mix** | `{"dc": 495, "proxy": 315, "home": 77, "mobile": 41}` |

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
