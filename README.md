# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-08-31 23:37:16](https://img.shields.io/badge/updated-2026--08--31_23%3A37%3A16-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 9576.4s](https://img.shields.io/badge/elapsed-9576.4s-lightgrey)
![profiles: 2143](https://img.shields.io/badge/profiles-2143-blue)
![live_hits: 2143](https://img.shields.io/badge/live__hits-2143-brightgreen)
![live_fail: 72013](https://img.shields.io/badge/live__fail-72013-orange)
![kept: 1271](https://img.shields.io/badge/kept-1271-blue)
![new: 872](https://img.shields.io/badge/new-872-success)
![dropped: 1046](https://img.shields.io/badge/dropped-1046-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-08-31 23:37:16 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `9576.4s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `422369` |
| **Live PASS (pool hits)** | `2143` |
| **Live FAIL** | `72013` |
| **History retained** | `1271` |
| **New PASS** | `872` |
| **History dropped** | `1046` |
| **Previous public** | `2317` |
| **Published profiles (deduped)** | `2143` |
| **Share links (exportable)** | `1477` |
| **YAML proxies (exportable)** | `1477` |
| **Protocol mix** | `{"shadowsocks": 268, "vless": 922, "hysteria2": 182, "vmess": 70, "trojan": 35}` |
| **Country mix** | `{"NL": 219, "MD": 4, "FR": 30, "SG": 82, "KR": 21, "DE": 108, "FI": 21, "CA": 304, "IT": 9, "DZ": 13, "RU": 41, "GB": 78, "US": 220, "SE": 9, "TW": 23, "ID": 2, "PL": 28, "LT": 12, "ES": 11, "ZA": 4, "HK": 32, "TH": 4, "MY": 3, "CN": 5, "JP": 62, "EE": 6, "BR": 15, "IN": 5, "NO": 16, "TR": 8, "KZ": 9, "AE": 1, "IR": 1, "CH": 6, "LV": 10, "SK": 1, "AT": 5, "CZ": 5, "GR": 2, "BG": 4, "AL": 3, "RO": 4, "PH": 1, "SC": 7, "IE": 6, "DK": 1, "SA": 1, "AR": 2, "AU": 3, "UA": 3, "BY": 1, "CO": 3, "AM": 1, "VN": 2, "JE": 1, "CR": 1, "MX": 2}` |
| **Line type mix** | `{"proxy": 400, "dc": 962, "home": 109, "mobile": 10}` |

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
