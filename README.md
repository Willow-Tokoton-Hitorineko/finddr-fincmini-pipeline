<div align="center">

<h1>finddr-fincmini-pipeline</h1>

<b>ACM ICAIF 2025 · FinDDR</b> · 财小析（FinCMini Agent）规则库<br/>
队名 DeepSeek Your Report · Test Set 最终榜 <b>第 12</b>（121.92）

<br/>

<img src="https://img.shields.io/badge/FinDDR-TestSet_Rank_12-F97316?style=flat-square&labelColor=DC2626" alt="Rank 12" />
<img src="https://img.shields.io/badge/FinCMini-财小析-3776AB?style=flat-square" alt="FinCMini" />
<img src="https://img.shields.io/badge/8_Regions-Multi--GAAP-60A5FA?style=flat-square" alt="8 regions" />
<img src="https://img.shields.io/badge/License-MIT-181717?style=flat-square" alt="MIT" />

<br/><br/>

<a href="https://github.com/Willow-Tokoton-Hitorineko/Willow-Tokoton-Hitorineko">← 戆北在coding の猫窝</a>

</div>

<p align="center">🐾 ─────────── 🏆 ─────────── 🐾</p>

## 这是什么

FINDDR 赛事里做的 **FinCMini Agent（财小析）** 知识工程归档：  
8 个地区的年报分析**规则库**、Pipeline 文档、部分测试/验证输出样例，以及自研评分脚本说明。

**Test Set 最终榜第 12 名**（队名 DeepSeek Your Report / 模型 FinCMini Agent）。  
名次见 [复旦新闻稿排名附图](https://cs.fudan.edu.cn/93/0f/c24256a758543/page.htm) 或本仓 [`docs/leaderboard-test-set-final.png`](docs/leaderboard-test-set-final.png)；参赛为 Participation 证书（前三名为获奖证书）。

本仓库为 FinDDR 参赛归档，非比赛官方交付包。

→ [个人贡献说明](docs/contribution.md) · [赛制与项目背景](docs/competition-context.md)

<p align="center">🐾 ─────────── 🏆 ─────────── 🐾</p>

## 主要工作

| | |
|:--|:--|
| **方案设计及主导推进** | FinCMini Agent：规则库 + Pipeline + LLM（[`contribution.md`](docs/contribution.md#方案背景)） |
| **规则库** | 8 地区规范逆向工程；Pipeline 3.6（80+ 文档） |
| **案例** | 测试集 **7 案**（test025–032 范围内，无 test030 输出） |
| **支援** | 印尼 Multiplier 换算规范（Sample008） |

<p align="center">🐾 ─────────── 🏆 ─────────── 🐾</p>

## 目录

```
pipeline/              财小析 Pipeline 3.6 规则库（核心）
  地区规范/            8 地区完整规范
  历史版本_归档/       3.2 / 3.5 归档
samples/               官方 sample001–008 格式参考
outputs/
  test/                测试集输出 test025–032
  validation/          部分验证集输出样例
scoring/               质量评分脚本 + 使用说明
docs/                  贡献说明、项目摘要、赛制说明
```

**入口文档：** [`pipeline/README_3.6.md`](pipeline/README_3.6.md) · [`pipeline/地区规范/README_地区规范总索引.md`](pipeline/地区规范/README_地区规范总索引.md)

<p align="center">🐾 ─────────── 🏆 ─────────── 🐾</p>

## 如何使用

本仓库以阅读规则库与样例为主，不是一键跑分应用：

1. 从 `pipeline/README_3.6.md` 了解 Pipeline 3.6
2. 按地区打开 `pipeline/地区规范/` 对应规范
3. 对照 `samples/sample00X.md` 与 `outputs/` 里的报告样例
4. （可选）`scoring/` 评估脚本 — 见 [`scoring/README.md`](scoring/README.md)（示例路径需自备数据）

```bash
git clone https://github.com/Willow-Tokoton-Hitorineko/finddr-fincmini-pipeline.git
cd finddr-fincmini-pipeline
copy .env.example .env   # 仅 scoring 脚本需要时再填
pip install -r requirements.txt   # 可选，仅 scoring 需要
```

<p align="center">🐾 ─────────── 🏆 ─────────── 🐾</p>

## 仓库范围

| 在本仓 | 不在本仓 |
|:--|:--|
| 规则库、sample、榜单截图、部分输出样例 | 完整验证/测试原始年报（版权 + 体积） |
| 名次依据（复旦新闻稿 + 本地榜单图） | API Key、队内私信 |
| 个人贡献说明 | 参赛证明（未收录） |

<p align="center">🐾 ─────────── 🏆 ─────────── 🐾</p>

## 说明

- 年报内容版权归原公司；sample 来自比赛公开参考格式
- 规则库为赛程中逆向整理，**不保证与最新赛制完全一致**
- MIT → [LICENSE](LICENSE)

<p align="center"><sub>🐱 <a href="https://github.com/Willow-Tokoton-Hitorineko/Willow-Tokoton-Hitorineko">戆北在coding の猫窝</a> · 欢迎 Issue</sub></p>
