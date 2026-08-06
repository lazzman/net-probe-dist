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


实验室 CI 工具：定期对公开端点列表做 **HTTP 可达性探测**，并发布 **编码后的配置包**。

配置包挂在 **GitHub Releases** 上（不写入 git 历史）。

## 状态

| 字段 | 值 |
| --- | --- |
| **最近更新** | `2026-08-06 10:57:37 CST` |
| **时区** | `Asia/Shanghai (UTC+8)` |
| **工作流结果** | `success` |
| **并发 Worker** | `24` |
| **耗时** | `1584.8s` |
| **探测模式** | `accumulate_full_no_sample` |
| **候选数（去重）** | `30946` |
| **测活通过（池命中）** | `2095` |
| **测活失败** | `9328` |
| **历史保留** | `867` |
| **新增通过** | `1228` |
| **历史淘汰** | `145` |
| **上一轮公开数** | `1012` |
| **发布配置数（去重后）** | `2087` |
| **分享链接（可导出）** | `1395` |
| **YAML 代理（可导出）** | `1395` |
| **协议分布** | `{"vless": 943, "shadowsocks": 188, "vmess": 77, "trojan": 92, "hysteria2": 95}` |
| **国家/地区分布** | `{"US": 188, "FR": 51, "GB": 55, "LT": 3, "CA": 386, "NL": 185, "PT": 1, "ES": 9, "FI": 34, "RU": 84, "SE": 14, "EE": 6, "DE": 84, "HK": 36, "IT": 5, "PL": 18, "CH": 4, "CZ": 1, "AE": 1, "TW": 11, "SG": 32, "BG": 4, "BR": 4, "KZ": 5, "TR": 5, "KR": 47, "HU": 1, "DK": 2, "CO": 3, "AT": 3, "TH": 2, "SA": 2, "SC": 6, "PH": 23, "LV": 6, "CR": 1, "CY": 3, "BZ": 1, "NO": 1, "IN": 5, "AU": 3, "IE": 5, "JP": 43, "ZA": 2, "CN": 3, "BH": 1, "AZ": 1, "RO": 3, "PA": 1, "MY": 2, "IR": 1, "KH": 1, "MD": 1}` |
| **线路类型分布** | `{"dc": 792, "proxy": 516, "home": 83, "mobile": 8}` |

### 数量漏斗

以下字段**不是**同一口径的数量：

1. **候选数（去重）** — 本轮公开订阅去重候选  
2. **池（Pool）** — 候选 ∪ 历史 public（累积）；历史节点**每轮复测**  
3. **测活通过 / 失败** — 对本轮 pool 的测活结果  
4. **历史保留 / 新增通过 / 历史淘汰** — 累积账本：留下的老节点 / 新通过 / 被淘汰的老节点  
5. **发布配置数** — 指纹去重后的最终 outbound（`fslsb` / `outbounds.json`）  
6. **分享链接 / YAML** — 可导出分享链的节点（vless/ss/trojan/vmess/hysteria2）

模式：**accumulate**（默认）= 累积 + 历史复测；`--fresh` = 仅本轮、不累积。

## 最新包

| 代码 | 包说明 | 最新链接 |
| --- | --- | --- |
| `fsl64` | 编码 blob | https://github.com/lazzman/net-probe-dist/releases/latest/download/fsl64 |
| `fslyaml` | YAML 包 | https://github.com/lazzman/net-probe-dist/releases/latest/download/fslyaml |
| `fslsb` | JSON 运行时包 | https://github.com/lazzman/net-probe-dist/releases/latest/download/fslsb |
| `fslyamlcomp` | 旧版 YAML 包 | https://github.com/lazzman/net-probe-dist/releases/latest/download/fslyamlcomp |
| manifest | 构建元数据 | https://github.com/lazzman/net-probe-dist/releases/latest/download/manifest.json |

Release 页面：https://github.com/lazzman/net-probe-dist/releases/latest

替换文件名（`fsl64` → 其他代码）即可切换格式。

### 拆分包（地区 / 线路类型）

IP enrichment 会对每个存活节点做分类，并额外输出分包：

| 类型 | 示例资源 | 含义 |
| --- | --- | --- |
| 全部 | `fsl64` | 全部节点 |
| 按国家/地区 | `geo-US-fsl64` | countryCode=US |
| 按类型 | `type-dc-fsl64` | 机房 / datacenter |
| 按类型 | `type-home-fsl64` | 家宽 / residential |
| 按类型 | `type-mobile-fsl64` | 移动网络 |
| 按类型 | `type-proxy-fsl64` | 代理 |
| 索引 | `splits.json` / `SPLITS.md` | 完整列表与计数 |

替换规则相同：`geo-US-fsl64` → `geo-US-fslyaml` / `geo-US-fslsb`。


## 自动化

- 工作流：`publish-dist`（每 6 小时 + 手动触发）
- 在 release 标签 `dist` 上上传/覆盖资源
- 每次运行会刷新本 README 中的 **最近更新** 与 **Workers** 徽章/表格
- git 树仅保留代码与状态指针（不含大体积 blob）

## 本地运行

```bash
python3 scripts/ci_public_sub_pipeline.py --workspace . --workers 24
python3 scripts/render_readme.py --workspace .
# 输出位于 ./dist ；发布命令示例：
#   gh release upload dist dist/fsl64 dist/fslyaml dist/fslsb dist/fslyamlcomp dist/manifest.json --clobber
```

## 安全说明

- Release 中不含 WireGuard 私钥文件
- 仅为实验室 / CI 产物，可能过期
