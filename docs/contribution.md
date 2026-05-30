# 个人贡献

**DeepSeek Your Report** · FinCMini Agent · ACM ICAIF 2025 FinDDR  
Test Set 第 **12** 名（121.92）· [榜单来源](competition-context.md#名次依据)

## 概述

赛程前期团队一度以为只要处理一篇年报；我判断任务应指向模型化交付，并建议组长向赛事方确认。对齐理解后，我提出将 FinCMini Agent 落地为规则库 + Pipeline + LLM 辅助工作流，并主要负责 8 地区规范与 Pipeline 3.6；测试集 7 案（test025–029、031–032）由我完成处理与验证。

## 方案背景

### 前期误判

刚接触赛制时，团队把任务理解成把 sample 或某一两篇年报分析做完即可。若真是这样，很快就会收尾，但比赛名称、多地区 sample 和后续材料显然不是这个量级。（非计算机科班，存在跨专业的理解错误）

### 模型化方向

我判断赛制要求的是训练 / 交付可复用的分析能力，而不是手工做完一篇就结束。

### 与赛事方确认

我建议组长联系赛事方核对；团队据此与官方对齐了任务指向模型化、系统化交付，并开始按该方向推进。

### FinCMini Agent 落地

在剩余不长的周期内，我提出并推动将 FinCMini Agent 实现为规则库 + Pipeline + LLM 辅助 + 人工 QA 的工作流，并完成 Test Set 提交。后续 8 地区逆向规范与 Pipeline 3.6 均沿此路线展开。

## 时间线

| 阶段 | 内容 |
|------|------|
| 前期 | 团队一度以为「处理一篇年报即可」 |
| 研判 | 我提出任务应指向模型化 / ML 训模方向 |
| 确认 | 组长向赛事方确认；团队对齐官方对任务的理解 |
| 落地 | 提出 FinCMini Agent 方案（规则库 + Pipeline + LLM + QA） |
| 中期 | 8 个 sample 逆向 → 8 份地区规范；Pipeline 文档 v3.2 → 3.6 |
| 后期 | 测试集 7 案（test025–032，无 test030）；恒等式与 12 项指标验证 |
| 支援 | 印尼 Multiplier 换算文档（Sample008） |

## 本仓内容

| 路径 | 说明 |
|------|------|
| `pipeline/` | 规则库：地区规范、Section 标准、QA 流程、版本日志 |
| `pipeline/地区规范/` | 8 地区完整规范（逆向 sample001–008） |
| `outputs/test/` | 我负责的测试集输出（7 案） |
| `outputs/validation/` | 部分验证集样例 |
| `samples/` | 官方 sample 格式参考 |
| `scoring/` | 质量评分脚本与说明 |

## 技术栈

- 多地区财务报告结构化（US GAAP / IFRS / 中国准则等）
- Sample 逆向工程、知识库 / Pipeline 设计
- Section 2 口径与格式控制（占分约 48.75%）
- 会计恒等式与 12 项财务指标校验
- LLM 辅助提取 + 人工 QA

## 说明

PDF 转 Markdown、部分案例执行与模型实验由队友完成；本仓库主要收录我负责的部分。  
更长摘要见 [`project-summary.md`](project-summary.md)，赛制背景见 [`competition-context.md`](competition-context.md)。
