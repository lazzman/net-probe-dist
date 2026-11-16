# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-11-16 16:13:05](https://img.shields.io/badge/updated-2026--11--16_16%3A13%3A05-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 11453.4s](https://img.shields.io/badge/elapsed-11453.4s-lightgrey)
![profiles: 1377](https://img.shields.io/badge/profiles-1377-blue)
![live_hits: 1377](https://img.shields.io/badge/live__hits-1377-brightgreen)
![live_fail: 88395](https://img.shields.io/badge/live__fail-88395-orange)
![kept: 1015](https://img.shields.io/badge/kept-1015-blue)
![new: 362](https://img.shields.io/badge/new-362-success)
![dropped: 268](https://img.shields.io/badge/dropped-268-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-11-16 16:13:05 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `11453.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `402486` |
| **Live PASS (pool hits)** | `1377` |
| **Live FAIL** | `88395` |
| **History retained** | `1015` |
| **New PASS** | `362` |
| **History dropped** | `268` |
| **Previous public** | `1283` |
| **Published profiles (deduped)** | `1377` |
| **Share links (exportable)** | `1220` |
| **YAML proxies (exportable)** | `1220` |
| **Protocol mix** | `{"hysteria2": 131, "shadowsocks": 376, "trojan": 98, "vless": 502, "vmess": 113}` |
| **Country mix** | `{"TR": 45, "US": 301, "EE": 11, "RS": 2, "CA": 116, "IR": 7, "SG": 48, "GB": 47, "DE": 89, "HK": 21, "NL": 146, "FR": 45, "SE": 14, "ZA": 4, "AL": 3, "AT": 2, "NO": 1, "IT": 22, "RO": 3, "JP": 49, "ES": 24, "BG": 6, "KR": 11, "FI": 14, "RU": 27, "CH": 52, "BY": 7, "IN": 5, "AE": 2, "LV": 10, "NE": 5, "VN": 1, "SK": 4, "PL": 52, "BR": 2, "TW": 2, "AU": 3, "NG": 3, "CZ": 1, "EG": 1, "KZ": 2, "MY": 1, "TH": 1, "BE": 2, "LT": 6, "CR": 2, "SA": 1}` |
| **Line type mix** | `{"home": 126, "proxy": 447, "dc": 526, "mobile": 124}` |

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
