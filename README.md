# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-17 03:02:47](https://img.shields.io/badge/updated-2026--10--17_03%3A02%3A47-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10165.6s](https://img.shields.io/badge/elapsed-10165.6s-lightgrey)
![profiles: 1151](https://img.shields.io/badge/profiles-1151-blue)
![live_hits: 1151](https://img.shields.io/badge/live__hits-1151-brightgreen)
![live_fail: 77682](https://img.shields.io/badge/live__fail-77682-orange)
![kept: 798](https://img.shields.io/badge/kept-798-blue)
![new: 353](https://img.shields.io/badge/new-353-success)
![dropped: 168](https://img.shields.io/badge/dropped-168-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-17 03:02:47 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10165.6s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `414503` |
| **Live PASS (pool hits)** | `1151` |
| **Live FAIL** | `77682` |
| **History retained** | `798` |
| **New PASS** | `353` |
| **History dropped** | `168` |
| **Previous public** | `966` |
| **Published profiles (deduped)** | `1151` |
| **Share links (exportable)** | `969` |
| **YAML proxies (exportable)** | `969` |
| **Protocol mix** | `{"vless": 492, "hysteria2": 97, "shadowsocks": 230, "trojan": 90, "vmess": 60}` |
| **Country mix** | `{"US": 151, "NL": 174, "GB": 24, "RU": 26, "ZA": 3, "HK": 25, "IR": 1, "DE": 56, "TR": 6, "RO": 3, "CH": 41, "CA": 183, "JP": 39, "IT": 12, "PL": 16, "IN": 8, "TH": 3, "SG": 42, "KR": 25, "ME": 3, "TW": 6, "FR": 23, "BY": 6, "SE": 8, "HU": 2, "LV": 10, "MD": 2, "FI": 12, "AE": 3, "KZ": 4, "BR": 11, "LT": 7, "AM": 1, "ID": 3, "MX": 1, "CL": 1, "AL": 3, "SC": 3, "EE": 3, "BG": 2, "EG": 1, "UA": 1, "ES": 6, "KH": 1, "AT": 1, "CZ": 3, "CY": 1, "GR": 1, "VN": 2, "MY": 1, "DK": 1, "CN": 2, "AU": 1, "SA": 1}` |
| **Line type mix** | `{"dc": 523, "proxy": 310, "home": 101, "mobile": 41}` |

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
