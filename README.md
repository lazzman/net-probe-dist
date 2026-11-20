# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-21 02:13:07](https://img.shields.io/badge/updated-2026--11--21_02%3A13%3A07-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11526.9s](https://img.shields.io/badge/elapsed-11526.9s-lightgrey)
![profiles: 1153](https://img.shields.io/badge/profiles-1153-blue)
![live_hits: 1153](https://img.shields.io/badge/live__hits-1153-brightgreen)
![live_fail: 88623](https://img.shields.io/badge/live__fail-88623-orange)
![kept: 884](https://img.shields.io/badge/kept-884-blue)
![new: 269](https://img.shields.io/badge/new-269-success)
![dropped: 244](https://img.shields.io/badge/dropped-244-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-21 02:13:07 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11526.9s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `404339` |
| **Live PASS (pool hits)** | `1153` |
| **Live FAIL** | `88623` |
| **History retained** | `884` |
| **New PASS** | `269` |
| **History dropped** | `244` |
| **Previous public** | `1128` |
| **Published profiles (deduped)** | `1153` |
| **Share links (exportable)** | `1050` |
| **YAML proxies (exportable)** | `1050` |
| **Protocol mix** | `{"shadowsocks": 383, "vless": 389, "vmess": 126, "hysteria2": 78, "trojan": 74}` |
| **Country mix** | `{"US": 268, "RU": 25, "AT": 2, "DE": 81, "HK": 26, "SG": 53, "NL": 123, "CN": 1, "CA": 87, "GB": 39, "FR": 29, "AL": 1, "NO": 1, "IE": 1, "ZA": 3, "IT": 24, "JP": 53, "ES": 14, "LT": 5, "KR": 15, "FI": 10, "CH": 17, "CL": 2, "AU": 4, "SE": 12, "IN": 4, "TR": 31, "EE": 15, "BY": 7, "KZ": 1, "LU": 1, "GR": 1, "NE": 4, "BR": 14, "TW": 7, "MY": 1, "PL": 37, "IR": 7, "LY": 1, "NG": 2, "BG": 7, "VN": 2, "SK": 2, "TH": 1, "RO": 1, "LV": 8, "AE": 1, "ZZ": 1, "SA": 1}` |
| **Line type mix** | `{"proxy": 416, "home": 111, "dc": 450, "mobile": 75, "unknown": 1}` |

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
