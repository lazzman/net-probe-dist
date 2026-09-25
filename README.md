# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-25 08:03:54](https://img.shields.io/badge/updated-2026--09--25_08%3A03%3A54-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10032.7s](https://img.shields.io/badge/elapsed-10032.7s-lightgrey)
![profiles: 1287](https://img.shields.io/badge/profiles-1287-blue)
![live_hits: 1288](https://img.shields.io/badge/live__hits-1288-brightgreen)
![live_fail: 77284](https://img.shields.io/badge/live__fail-77284-orange)
![kept: 986](https://img.shields.io/badge/kept-986-blue)
![new: 302](https://img.shields.io/badge/new-302-success)
![dropped: 151](https://img.shields.io/badge/dropped-151-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-25 08:03:54 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10032.7s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `435992` |
| **Live PASS (pool hits)** | `1288` |
| **Live FAIL** | `77284` |
| **History retained** | `986` |
| **New PASS** | `302` |
| **History dropped** | `151` |
| **Previous public** | `1137` |
| **Published profiles (deduped)** | `1287` |
| **Share links (exportable)** | `1140` |
| **YAML proxies (exportable)** | `1140` |
| **Protocol mix** | `{"shadowsocks": 284, "vless": 630, "vmess": 84, "hysteria2": 116, "trojan": 26}` |
| **Country mix** | `{"US": 212, "CZ": 1, "DE": 57, "KR": 28, "CA": 213, "GB": 65, "ES": 9, "RU": 32, "ZA": 3, "NL": 180, "ID": 1, "IE": 1, "FR": 31, "NO": 2, "RO": 4, "CH": 7, "SG": 27, "JP": 35, "SE": 18, "DK": 2, "IN": 15, "PL": 26, "AT": 3, "FI": 25, "TR": 3, "TW": 9, "AU": 3, "IT": 12, "AL": 1, "AM": 1, "IQ": 1, "HK": 32, "AE": 2, "IL": 3, "EE": 6, "DZ": 26, "KZ": 5, "BG": 10, "GT": 1, "LT": 8, "CL": 2, "SC": 2, "TH": 1, "LV": 9, "AZ": 1, "GR": 1, "SA": 1, "RS": 1, "CR": 1, "MY": 1}` |
| **Line type mix** | `{"proxy": 394, "home": 62, "dc": 669, "mobile": 15}` |

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
