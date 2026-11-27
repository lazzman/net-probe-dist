# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-28 03:24:30](https://img.shields.io/badge/updated-2026--11--28_03%3A24%3A30-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11289.7s](https://img.shields.io/badge/elapsed-11289.7s-lightgrey)
![profiles: 1027](https://img.shields.io/badge/profiles-1027-blue)
![live_hits: 1027](https://img.shields.io/badge/live__hits-1027-brightgreen)
![live_fail: 88626](https://img.shields.io/badge/live__fail-88626-orange)
![kept: 769](https://img.shields.io/badge/kept-769-blue)
![new: 258](https://img.shields.io/badge/new-258-success)
![dropped: 577](https://img.shields.io/badge/dropped-577-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-28 03:24:30 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11289.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `397464` |
| **Live PASS (pool hits)** | `1027` |
| **Live FAIL** | `88626` |
| **History retained** | `769` |
| **New PASS** | `258` |
| **History dropped** | `577` |
| **Previous public** | `1346` |
| **Published profiles (deduped)** | `1027` |
| **Share links (exportable)** | `914` |
| **YAML proxies (exportable)** | `914` |
| **Protocol mix** | `{"hysteria2": 66, "vless": 362, "shadowsocks": 364, "vmess": 120, "trojan": 2}` |
| **Country mix** | `{"AE": 7, "US": 230, "DE": 58, "HK": 22, "NL": 114, "FR": 38, "AT": 2, "NO": 1, "CA": 57, "ZA": 2, "ES": 21, "JP": 78, "GB": 41, "PL": 12, "LT": 8, "BG": 10, "KR": 15, "RU": 28, "FI": 5, "SE": 9, "SG": 41, "CH": 7, "IT": 19, "IN": 3, "BY": 6, "NG": 2, "TR": 23, "CZ": 1, "NE": 3, "AL": 2, "RO": 5, "IR": 5, "BR": 9, "KZ": 4, "TW": 3, "LV": 8, "GR": 1, "SK": 3, "TH": 1, "MY": 2, "AU": 3, "CY": 1, "IL": 1, "MX": 1, "EE": 4}` |
| **Line type mix** | `{"dc": 409, "proxy": 388, "mobile": 29, "home": 90}` |

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
