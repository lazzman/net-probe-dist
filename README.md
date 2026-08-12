# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-13 00:04:23](https://img.shields.io/badge/updated-2026--08--13_00%3A04%3A23-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10203.1s](https://img.shields.io/badge/elapsed-10203.1s-lightgrey)
![profiles: 1590](https://img.shields.io/badge/profiles-1590-blue)
![live_hits: 1590](https://img.shields.io/badge/live__hits-1590-brightgreen)
![live_fail: 92661](https://img.shields.io/badge/live__fail-92661-orange)
![kept: 938](https://img.shields.io/badge/kept-938-blue)
![new: 652](https://img.shields.io/badge/new-652-success)
![dropped: 635](https://img.shields.io/badge/dropped-635-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-13 00:04:23 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10203.1s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `445296` |
| **Live PASS (pool hits)** | `1590` |
| **Live FAIL** | `92661` |
| **History retained** | `938` |
| **New PASS** | `652` |
| **History dropped** | `635` |
| **Previous public** | `1573` |
| **Published profiles (deduped)** | `1590` |
| **Share links (exportable)** | `1171` |
| **YAML proxies (exportable)** | `1171` |
| **Protocol mix** | `{"vmess": 72, "shadowsocks": 187, "vless": 736, "hysteria2": 96, "trojan": 80}` |
| **Country mix** | `{"US": 146, "CA": 235, "AU": 5, "NL": 175, "GB": 53, "DE": 81, "TH": 3, "FR": 58, "HK": 46, "PL": 24, "RO": 5, "FI": 37, "TR": 9, "TW": 7, "ES": 10, "JP": 39, "IT": 5, "SG": 26, "BG": 2, "SA": 2, "RU": 87, "PT": 1, "KZ": 8, "EE": 12, "AE": 2, "IR": 1, "CH": 4, "LV": 5, "SE": 4, "KR": 34, "CO": 2, "MD": 1, "PH": 11, "IN": 4, "IE": 2, "LT": 3, "ZA": 2, "NO": 1, "AZ": 1, "HU": 2, "CZ": 2, "AT": 2, "AL": 2, "ZZ": 2, "SC": 3, "AF": 1, "AM": 1, "CR": 2, "CY": 1, "KH": 1}` |
| **Line type mix** | `{"dc": 631, "proxy": 445, "home": 82, "mobile": 12, "unknown": 2}` |

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
