# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-05 03:29:17](https://img.shields.io/badge/updated-2026--10--05_03%3A29%3A17-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10424.3s](https://img.shields.io/badge/elapsed-10424.3s-lightgrey)
![profiles: 1283](https://img.shields.io/badge/profiles-1283-blue)
![live_hits: 1283](https://img.shields.io/badge/live__hits-1283-brightgreen)
![live_fail: 78974](https://img.shields.io/badge/live__fail-78974-orange)
![kept: 972](https://img.shields.io/badge/kept-972-blue)
![new: 311](https://img.shields.io/badge/new-311-success)
![dropped: 198](https://img.shields.io/badge/dropped-198-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-05 03:29:17 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10424.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `436368` |
| **Live PASS (pool hits)** | `1283` |
| **Live FAIL** | `78974` |
| **History retained** | `972` |
| **New PASS** | `311` |
| **History dropped** | `198` |
| **Previous public** | `1170` |
| **Published profiles (deduped)** | `1283` |
| **Share links (exportable)** | `1114` |
| **YAML proxies (exportable)** | `1114` |
| **Protocol mix** | `{"shadowsocks": 256, "vless": 577, "hysteria2": 107, "vmess": 91, "trojan": 83}` |
| **Country mix** | `{"ZA": 4, "US": 214, "RU": 18, "CA": 235, "GB": 30, "NL": 146, "SG": 34, "DE": 57, "IE": 6, "FR": 26, "RO": 6, "ES": 10, "CH": 10, "JP": 54, "FI": 10, "IN": 6, "KR": 38, "CN": 16, "SE": 5, "LT": 11, "AE": 2, "HK": 47, "AZ": 1, "PL": 19, "IT": 16, "GR": 2, "LU": 2, "CL": 12, "ID": 2, "TW": 4, "BR": 1, "NO": 1, "KZ": 5, "MX": 1, "EE": 7, "SA": 1, "AM": 2, "LV": 5, "TR": 2, "AU": 6, "AL": 2, "MY": 9, "TH": 2, "AT": 1, "BG": 10, "UA": 1, "CZ": 13, "CR": 1, "SC": 1, "IL": 1}` |
| **Line type mix** | `{"proxy": 357, "dc": 673, "home": 67, "mobile": 18}` |

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
