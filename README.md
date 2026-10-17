# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-17 14:04:53](https://img.shields.io/badge/updated-2026--10--17_14%3A04%3A53-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10128.4s](https://img.shields.io/badge/elapsed-10128.4s-lightgrey)
![profiles: 1830](https://img.shields.io/badge/profiles-1830-blue)
![live_hits: 1830](https://img.shields.io/badge/live__hits-1830-brightgreen)
![live_fail: 77036](https://img.shields.io/badge/live__fail-77036-orange)
![kept: 877](https://img.shields.io/badge/kept-877-blue)
![new: 953](https://img.shields.io/badge/new-953-success)
![dropped: 130](https://img.shields.io/badge/dropped-130-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-17 14:04:53 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10128.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `416169` |
| **Live PASS (pool hits)** | `1830` |
| **Live FAIL** | `77036` |
| **History retained** | `877` |
| **New PASS** | `953` |
| **History dropped** | `130` |
| **Previous public** | `1007` |
| **Published profiles (deduped)** | `1830` |
| **Share links (exportable)** | `1437` |
| **YAML proxies (exportable)** | `1437` |
| **Protocol mix** | `{"shadowsocks": 250, "vless": 893, "trojan": 130, "hysteria2": 101, "vmess": 63}` |
| **Country mix** | `{"US": 216, "CA": 370, "PL": 20, "NL": 195, "GB": 46, "ZA": 3, "RU": 30, "AU": 5, "HK": 44, "DE": 90, "NO": 1, "RO": 4, "CH": 42, "SG": 58, "JP": 47, "KR": 39, "IN": 10, "TH": 5, "EG": 1, "ES": 11, "AT": 3, "ME": 6, "LV": 16, "TW": 6, "KH": 1, "FR": 24, "BY": 3, "AL": 3, "FI": 16, "ZZ": 4, "SE": 9, "HU": 3, "MD": 3, "AE": 6, "IT": 17, "KZ": 8, "LT": 8, "AM": 2, "MX": 1, "CL": 1, "ID": 3, "TR": 8, "SA": 1, "MY": 1, "EE": 6, "BG": 6, "CZ": 3, "UA": 5, "SC": 6, "NZ": 1, "PT": 1, "CY": 3, "BZ": 4, "IR": 1, "CW": 4, "GR": 1, "VN": 2, "DK": 1, "CN": 3, "UZ": 1, "VG": 1, "BR": 2, "IL": 1}` |
| **Line type mix** | `{"proxy": 422, "dc": 847, "home": 126, "unknown": 4, "mobile": 43}` |

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
