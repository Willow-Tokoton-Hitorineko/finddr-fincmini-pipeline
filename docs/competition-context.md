# 赛制与项目背景

FinDDR 参赛背景、名次依据与 FinCMini Agent 技术说明。个人分工见 [`contribution.md`](contribution.md)。

## 比赛是什么

**ACM ICAIF 2025 · Financial Document Deep Research Grand Challenge（FinDDR）**  
任务是从多地区上市公司年报生成结构化深度研究报告（Section 1–6），覆盖美、英、中、港、新、澳、印尼、马等市场。

## 团队与成绩

| 项 | 内容 |
|:---|:-----|
| 队名 | **DeepSeek Your Report** |
| 提交系统 | **FinCMini Agent**（财小析） |
| 单位 | 上海对外经贸大学 |
| **Test Set 最终排名** | **第 12 名**（Overall **121.92**） |

### 名次依据

前三名颁发获奖证书；第 4 名及以后为 Certificate of Participation（参赛证明）。  
本仓库所述「第 12 名」指 **Leaderboard on Test Set (Final)** 上的官方排名。

- 公开出处：[复旦大学计算机学院新闻稿](https://cs.fudan.edu.cn/93/0f/c24256a758543/page.htm) 附图「ICAIF FinDDR 2025 国际竞赛最终排名」
- 本仓备份：[`leaderboard-test-set-final.png`](leaderboard-test-set-final.png)

参赛证明扫描件未收录本仓。

## FinCMini Agent

团队为 FinDDR 构建的多地区年报分析系统，以 Agent 名义提交与评测：

| 层级 | 内容 |
|------|------|
| 规则库 | 8 地区格式、口径与取数规范（基于官方 sample 逆向整理） |
| LLM | 在规则约束下完成提取、填表与叙述生成 |
| 人工 QA | 质量清单、会计恒等式与关键财务指标复核 |

本仓库收录规则库、Pipeline 文档及部分输出样例；非比赛官方交付包。

## 方案演进

团队对赛制的理解逐步澄清：起初曾低估任务规模；赛程中与赛事方沟通后，明确任务指向模型化、系统化的分析能力交付。  
团队在剩余周期内将 FinCMini Agent 落地为规则库 + Pipeline + LLM + 人工 QA 工作流并完成 Test Set 提交。方案提出与 Pipeline 3.6 详见 [`contribution.md`](contribution.md)。

## 仓库范围

| 包含 | 不包含 |
|------|--------|
| Pipeline 规则库、8 份 sample | 完整验证/测试集原始年报 |
| 榜单截图、部分输出样例 | API Key、私有数据路径 |
| 评分脚本与说明 | 队内分工细表、参赛证明 |

## 免责声明

规则库源于比赛 sample 的逆向整理，不保证与最新赛制完全一致。年报内容版权归各上市公司及数据来源所有；请勿用于商业用途或冒充官方比赛交付物。
