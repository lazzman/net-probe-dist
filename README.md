# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-09-25 22:07:50](https://img.shields.io/badge/updated-2026--09--25_22%3A07%3A50-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10068.3s](https://img.shields.io/badge/elapsed-10068.3s-lightgrey)
![profiles: 1371](https://img.shields.io/badge/profiles-1371-blue)
![live_hits: 1371](https://img.shields.io/badge/live__hits-1371-brightgreen)
![live_fail: 77030](https://img.shields.io/badge/live__fail-77030-orange)
![kept: 1051](https://img.shields.io/badge/kept-1051-blue)
![new: 320](https://img.shields.io/badge/new-320-success)
![dropped: 1051](https://img.shields.io/badge/dropped-1051-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-09-25 22:07:50 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10068.3s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `437230` |
| **Live PASS (pool hits)** | `1371` |
| **Live FAIL** | `77030` |
| **History retained** | `1051` |
| **New PASS** | `320` |
| **History dropped** | `1051` |
| **Previous public** | `2102` |
| **Published profiles (deduped)** | `1371` |
| **Share links (exportable)** | `1198` |
| **YAML proxies (exportable)** | `1198` |
| **Protocol mix** | `{"shadowsocks": 263, "vmess": 89, "vless": 697, "hysteria2": 110, "trojan": 39}` |
| **Country mix** | `{"CZ": 2, "US": 219, "ZA": 3, "ES": 9, "CA": 268, "KR": 26, "GB": 69, "JP": 40, "NL": 161, "DE": 54, "FR": 34, "ID": 1, "RO": 4, "CH": 7, "MX": 1, "SE": 20, "DK": 1, "IN": 14, "PL": 25, "AT": 3, "FI": 19, "TR": 3, "RU": 26, "TW": 10, "SG": 27, "AU": 3, "IT": 18, "AL": 1, "IL": 3, "EE": 7, "AM": 1, "IQ": 2, "HK": 37, "CN": 2, "NO": 2, "DZ": 26, "SC": 3, "UA": 2, "KZ": 5, "AE": 3, "TH": 2, "BZ": 1, "CW": 4, "CY": 1, "GT": 1, "IR": 1, "LT": 8, "MD": 1, "CL": 1, "LV": 5, "LU": 1, "BG": 8, "GR": 1, "SA": 1, "CR": 1, "MY": 1}` |
| **Line type mix** | `{"proxy": 387, "home": 66, "mobile": 16, "dc": 730}` |

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
