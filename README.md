# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-31 09:06:45](https://img.shields.io/badge/updated-2026--10--31_09%3A06%3A45-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10959.5s](https://img.shields.io/badge/elapsed-10959.5s-lightgrey)
![profiles: 1527](https://img.shields.io/badge/profiles-1527-blue)
![live_hits: 1527](https://img.shields.io/badge/live__hits-1527-brightgreen)
![live_fail: 85815](https://img.shields.io/badge/live__fail-85815-orange)
![kept: 868](https://img.shields.io/badge/kept-868-blue)
![new: 659](https://img.shields.io/badge/new-659-success)
![dropped: 142](https://img.shields.io/badge/dropped-142-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-31 09:06:45 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10959.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `404485` |
| **Live PASS (pool hits)** | `1527` |
| **Live FAIL** | `85815` |
| **History retained** | `868` |
| **New PASS** | `659` |
| **History dropped** | `142` |
| **Previous public** | `1010` |
| **Published profiles (deduped)** | `1527` |
| **Share links (exportable)** | `1331` |
| **YAML proxies (exportable)** | `1331` |
| **Protocol mix** | `{"shadowsocks": 269, "vless": 694, "trojan": 168, "hysteria2": 129, "vmess": 71}` |
| **Country mix** | `{"NL": 187, "IT": 17, "US": 216, "MX": 4, "DE": 81, "CA": 330, "HK": 37, "GB": 35, "IR": 6, "PL": 27, "NO": 1, "UA": 3, "ZA": 3, "RU": 32, "CH": 53, "AL": 2, "JP": 38, "SG": 59, "BG": 11, "SE": 9, "IN": 7, "KR": 31, "BR": 2, "CL": 1, "IL": 3, "ES": 16, "TH": 2, "HU": 1, "AT": 2, "CR": 1, "LV": 9, "BY": 7, "KZ": 7, "AE": 4, "FR": 35, "FI": 15, "SA": 1, "AM": 1, "EE": 5, "TW": 3, "AU": 3, "RO": 2, "SC": 2, "LT": 7, "GR": 1, "CZ": 1, "VN": 2, "TR": 3, "MY": 3, "ID": 1, "MD": 2, "SK": 1, "CN": 1, "VG": 1, "DK": 1, "CW": 1, "BZ": 2}` |
| **Line type mix** | `{"proxy": 328, "dc": 799, "mobile": 122, "home": 89}` |

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
