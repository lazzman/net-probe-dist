# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-18 21:33:29](https://img.shields.io/badge/updated-2026--10--18_21%3A33%3A29-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10861.7s](https://img.shields.io/badge/elapsed-10861.7s-lightgrey)
![profiles: 1190](https://img.shields.io/badge/profiles-1190-blue)
![live_hits: 1190](https://img.shields.io/badge/live__hits-1190-brightgreen)
![live_fail: 86029](https://img.shields.io/badge/live__fail-86029-orange)
![kept: 838](https://img.shields.io/badge/kept-838-blue)
![new: 352](https://img.shields.io/badge/new-352-success)
![dropped: 542](https://img.shields.io/badge/dropped-542-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-18 21:33:29 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10861.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `454806` |
| **Live PASS (pool hits)** | `1190` |
| **Live FAIL** | `86029` |
| **History retained** | `838` |
| **New PASS** | `352` |
| **History dropped** | `542` |
| **Previous public** | `1380` |
| **Published profiles (deduped)** | `1190` |
| **Share links (exportable)** | `1007` |
| **YAML proxies (exportable)** | `1007` |
| **Protocol mix** | `{"vless": 518, "hysteria2": 109, "shadowsocks": 229, "trojan": 88, "vmess": 63}` |
| **Country mix** | `{"CA": 168, "RU": 41, "CH": 40, "GB": 30, "AU": 4, "US": 142, "NL": 168, "HK": 35, "ZA": 3, "DE": 74, "RO": 5, "JP": 37, "IN": 10, "PL": 24, "TH": 3, "SG": 44, "KR": 27, "CR": 1, "ME": 2, "FI": 18, "TW": 4, "KH": 1, "FR": 28, "BY": 4, "IT": 9, "SE": 6, "HU": 3, "MD": 3, "ES": 9, "AE": 4, "TR": 9, "IL": 2, "CZ": 3, "LT": 8, "LV": 11, "KZ": 5, "CN": 2, "MX": 1, "CL": 1, "NO": 1, "EE": 3, "IR": 2, "ID": 2, "NZ": 1, "BZ": 1, "CW": 1, "CY": 1, "GR": 1, "VN": 2, "MY": 1, "BG": 3, "SA": 1, "AL": 2}` |
| **Line type mix** | `{"dc": 533, "home": 110, "proxy": 328, "mobile": 40}` |

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
