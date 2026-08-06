# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-06 10:57:37](https://img.shields.io/badge/updated-2026--08--06_10%3A57%3A37-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 1584.8s](https://img.shields.io/badge/elapsed-1584.8s-lightgrey)
![profiles: 2087](https://img.shields.io/badge/profiles-2087-blue)
![live_hits: 2095](https://img.shields.io/badge/live__hits-2095-brightgreen)
![live_fail: 9328](https://img.shields.io/badge/live__fail-9328-orange)
![kept: 867](https://img.shields.io/badge/kept-867-blue)
![new: 1228](https://img.shields.io/badge/new-1228-success)
![dropped: 145](https://img.shields.io/badge/dropped-145-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-06 10:57:37 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `1584.8s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `30946` |
| **Live PASS (pool hits)** | `2095` |
| **Live FAIL** | `9328` |
| **History retained** | `867` |
| **New PASS** | `1228` |
| **History dropped** | `145` |
| **Previous public** | `1012` |
| **Published profiles (deduped)** | `2087` |
| **Share links (exportable)** | `1395` |
| **YAML proxies (exportable)** | `1395` |
| **Protocol mix** | `{"vless": 943, "shadowsocks": 188, "vmess": 77, "trojan": 92, "hysteria2": 95}` |
| **Country mix** | `{"US": 188, "FR": 51, "GB": 55, "LT": 3, "CA": 386, "NL": 185, "PT": 1, "ES": 9, "FI": 34, "RU": 84, "SE": 14, "EE": 6, "DE": 84, "HK": 36, "IT": 5, "PL": 18, "CH": 4, "CZ": 1, "AE": 1, "TW": 11, "SG": 32, "BG": 4, "BR": 4, "KZ": 5, "TR": 5, "KR": 47, "HU": 1, "DK": 2, "CO": 3, "AT": 3, "TH": 2, "SA": 2, "SC": 6, "PH": 23, "LV": 6, "CR": 1, "CY": 3, "BZ": 1, "NO": 1, "IN": 5, "AU": 3, "IE": 5, "JP": 43, "ZA": 2, "CN": 3, "BH": 1, "AZ": 1, "RO": 3, "PA": 1, "MY": 2, "IR": 1, "KH": 1, "MD": 1}` |
| **Line type mix** | `{"dc": 792, "proxy": 516, "home": 83, "mobile": 8}` |

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
