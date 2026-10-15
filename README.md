# net-probe-dist

[![publish-dist](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml/badge.svg)](https://github.com/lazzman/net-probe-dist/actions/workflows/publish-dist.yml)
[![release](https://img.shields.io/github/v/release/lazzman/net-probe-dist?style=flat-square&label=release)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![release-date](https://img.shields.io/github/release-date/lazzman/net-probe-dist?style=flat-square&label=released)](https://github.com/lazzman/net-probe-dist/releases/latest)
[![downloads](https://img.shields.io/github/downloads/lazzman/net-probe-dist/total?style=flat-square&label=downloads)](https://github.com/lazzman/net-probe-dist/releases/latest)
![updated: 2026-10-15 21:46:40](https://img.shields.io/badge/updated-2026--10--15_21%3A46%3A40-informational?logo=github&logoColor=white)
![result: success](https://img.shields.io/badge/result-success-brightgreen?logo=githubactions&logoColor=white)
![workers: 24](https://img.shields.io/badge/workers-24-blueviolet)
![elapsed: 10035.5s](https://img.shields.io/badge/elapsed-10035.5s-lightgrey)
![profiles: 1173](https://img.shields.io/badge/profiles-1173-blue)
![live_hits: 1174](https://img.shields.io/badge/live__hits-1174-brightgreen)
![live_fail: 77626](https://img.shields.io/badge/live__fail-77626-orange)
![kept: 755](https://img.shields.io/badge/kept-755-blue)
![new: 419](https://img.shields.io/badge/new-419-success)
![dropped: 452](https://img.shields.io/badge/dropped-452-important)


Lab CI utility: periodic **HTTP reachability probes** over public endpoint lists, then publish **encoded profile packages**.

Packages are attached to **GitHub Releases** (not stored in git history).

## Status

| Field | Value |
| --- | --- |
| **Last update** | `2026-10-15 21:46:40 CST` |
| **Timezone** | `Asia/Shanghai (UTC+8)` |
| **Workflow result** | `success` |
| **Workers** | `24` |
| **Elapsed** | `10035.5s` |
| **Probe mode** | `accumulate_full_no_sample` |
| **Candidates (unique)** | `413742` |
| **Live PASS (pool hits)** | `1174` |
| **Live FAIL** | `77626` |
| **History retained** | `755` |
| **New PASS** | `419` |
| **History dropped** | `452` |
| **Previous public** | `1207` |
| **Published profiles (deduped)** | `1173` |
| **Share links (exportable)** | `982` |
| **YAML proxies (exportable)** | `982` |
| **Protocol mix** | `{"vless": 493, "shadowsocks": 226, "hysteria2": 104, "trojan": 98, "vmess": 61}` |
| **Country mix** | `{"US": 146, "ZA": 5, "GB": 28, "NL": 177, "AU": 4, "NO": 1, "DE": 76, "CH": 41, "JP": 32, "CA": 151, "RU": 22, "PL": 14, "IN": 7, "KR": 26, "SG": 58, "CR": 1, "AT": 1, "TW": 5, "FR": 22, "TH": 3, "SE": 9, "HK": 48, "FI": 12, "AE": 4, "IL": 1, "SA": 1, "ME": 5, "CZ": 2, "IT": 11, "LV": 8, "ID": 3, "CN": 1, "RO": 6, "MY": 5, "ES": 11, "UA": 1, "TR": 4, "SC": 1, "KZ": 5, "EE": 3, "BR": 1, "BG": 3, "AL": 2, "VN": 2, "DK": 1, "LT": 9, "BY": 5}` |
| **Line type mix** | `{"dc": 539, "proxy": 319, "home": 86, "mobile": 40}` |

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
