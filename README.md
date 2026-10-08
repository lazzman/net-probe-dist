# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-08 09:36:39](https://img.shields.io/badge/updated-2026--10--08_09%3A36%3A39-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9901.8s](https://img.shields.io/badge/elapsed-9901.8s-lightgrey)
![profiles: 1580](https://img.shields.io/badge/profiles-1580-blue)
![live_hits: 1580](https://img.shields.io/badge/live__hits-1580-brightgreen)
![live_fail: 75767](https://img.shields.io/badge/live__fail-75767-orange)
![kept: 877](https://img.shields.io/badge/kept-877-blue)
![new: 703](https://img.shields.io/badge/new-703-success)
![dropped: 183](https://img.shields.io/badge/dropped-183-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-08 09:36:39 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9901.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `406557` |
| **Live PASS (pool hits)** | `1580` |
| **Live FAIL** | `75767` |
| **History retained** | `877` |
| **New PASS** | `703` |
| **History dropped** | `183` |
| **Previous public** | `1060` |
| **Published profiles (deduped)** | `1580` |
| **Share links (exportable)** | `1314` |
| **YAML proxies (exportable)** | `1314` |
| **Protocol mix** | `{"vless": 758, "hysteria2": 113, "shadowsocks": 280, "trojan": 92, "vmess": 71}` |
| **Country mix** | `{"US": 199, "FR": 33, "ZA": 5, "NL": 174, "GB": 33, "CA": 276, "ID": 3, "DE": 101, "SG": 47, "IN": 12, "CH": 9, "RO": 3, "ES": 16, "FI": 23, "JP": 62, "TH": 3, "KR": 41, "IE": 6, "HU": 1, "PL": 19, "AT": 3, "SC": 4, "HK": 59, "RU": 17, "TW": 3, "SE": 7, "EE": 9, "IT": 18, "KZ": 6, "CL": 11, "MY": 11, "CN": 17, "NO": 1, "TR": 9, "LV": 26, "BE": 2, "PT": 1, "GR": 2, "AL": 4, "LT": 9, "AE": 3, "AU": 6, "BY": 1, "BG": 9, "VN": 2, "AM": 2, "CZ": 2, "SA": 1, "BZ": 2, "UA": 2, "CR": 1, "MD": 1, "RS": 2, "BR": 1, "UZ": 1}` |
| **Line type mix** | `{"dc": 836, "proxy": 383, "home": 93, "mobile": 9}` |

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
