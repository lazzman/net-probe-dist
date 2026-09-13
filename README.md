# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-14 02:31:03](https://img.shields.io/badge/updated-2026--09--14_02%3A31%3A03-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9831.2s](https://img.shields.io/badge/elapsed-9831.2s-lightgrey)
![profiles: 1571](https://img.shields.io/badge/profiles-1571-blue)
![live_hits: 1571](https://img.shields.io/badge/live__hits-1571-brightgreen)
![live_fail: 74547](https://img.shields.io/badge/live__fail-74547-orange)
![kept: 1119](https://img.shields.io/badge/kept-1119-blue)
![new: 452](https://img.shields.io/badge/new-452-success)
![dropped: 205](https://img.shields.io/badge/dropped-205-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-14 02:31:03 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9831.2s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `432044` |
| **Live PASS (pool hits)** | `1571` |
| **Live FAIL** | `74547` |
| **History retained** | `1119` |
| **New PASS** | `452` |
| **History dropped** | `205` |
| **Previous public** | `1324` |
| **Published profiles (deduped)** | `1571` |
| **Share links (exportable)** | `1230` |
| **YAML proxies (exportable)** | `1230` |
| **Protocol mix** | `{"trojan": 25, "hysteria2": 152, "vmess": 53, "vless": 756, "shadowsocks": 244}` |
| **Country mix** | `{"US": 187, "AU": 4, "GB": 46, "JP": 35, "DE": 47, "DZ": 24, "RU": 21, "FI": 14, "SE": 10, "NL": 194, "CA": 350, "SG": 29, "ID": 1, "NO": 5, "FR": 31, "IE": 1, "PL": 26, "ES": 5, "RO": 6, "AL": 2, "TR": 8, "MX": 1, "IN": 9, "DK": 1, "IT": 10, "KR": 28, "HR": 1, "TW": 14, "EE": 5, "UZ": 2, "CZ": 4, "HK": 52, "AE": 2, "TH": 3, "UA": 3, "GR": 1, "GT": 1, "AZ": 1, "SA": 1, "MY": 3, "LT": 12, "AM": 2, "ZA": 4, "BR": 1, "CL": 1, "LV": 11, "KZ": 4, "CH": 2, "AT": 1, "SC": 1, "ZZ": 1, "BG": 1, "CR": 1}` |
| **Line type mix** | `{"dc": 813, "proxy": 348, "home": 63, "mobile": 5, "unknown": 1}` |

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
