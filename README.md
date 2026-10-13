# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-14 00:31:23](https://img.shields.io/badge/updated-2026--10--14_00%3A31%3A23-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10100.1s](https://img.shields.io/badge/elapsed-10100.1s-lightgrey)
![profiles: 1251](https://img.shields.io/badge/profiles-1251-blue)
![live_hits: 1251](https://img.shields.io/badge/live__hits-1251-brightgreen)
![live_fail: 77048](https://img.shields.io/badge/live__fail-77048-orange)
![kept: 822](https://img.shields.io/badge/kept-822-blue)
![new: 429](https://img.shields.io/badge/new-429-success)
![dropped: 1234](https://img.shields.io/badge/dropped-1234-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-14 00:31:23 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10100.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `411817` |
| **Live PASS (pool hits)** | `1251` |
| **Live FAIL** | `77048` |
| **History retained** | `822` |
| **New PASS** | `429` |
| **History dropped** | `1234` |
| **Previous public** | `2056` |
| **Published profiles (deduped)** | `1251` |
| **Share links (exportable)** | `1024` |
| **YAML proxies (exportable)** | `1024` |
| **Protocol mix** | `{"vless": 505, "shadowsocks": 270, "hysteria2": 100, "trojan": 94, "vmess": 55}` |
| **Country mix** | `{"US": 146, "CA": 186, "ZA": 4, "GB": 33, "RU": 38, "NL": 160, "IE": 5, "DE": 59, "FR": 24, "FI": 18, "CH": 41, "RO": 5, "JP": 53, "IN": 8, "PL": 19, "KR": 36, "SG": 36, "AT": 1, "EE": 4, "HK": 36, "TH": 2, "SE": 9, "TR": 5, "IT": 16, "BG": 9, "MY": 8, "CZ": 4, "ME": 4, "LT": 13, "LV": 4, "AM": 1, "ID": 2, "CN": 3, "TW": 4, "NO": 1, "AE": 2, "IL": 1, "SC": 4, "ES": 5, "KZ": 4, "BR": 3, "AU": 4, "GR": 1, "AL": 2, "IR": 1, "DK": 1, "SA": 1}` |
| **Line type mix** | `{"dc": 551, "proxy": 340, "home": 93, "mobile": 42}` |

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
