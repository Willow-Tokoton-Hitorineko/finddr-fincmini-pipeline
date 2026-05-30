# 评分脚本说明

基于 [DeepEval SummarizationMetric](https://deepeval.com/docs/metrics-summarization) 的年报分析质量评估工具。

## 重要

本仓库**未包含**脚本示例里引用的原始年报路径（如「中国移动2024年年报.md」）及对应评估 JSON/MD。  
用法见 [`使用指南.md`](使用指南.md)；要跑通需自备数据并修改路径。

配置：复制仓库根目录 [`.env.example`](../.env.example) 为 `.env`，填入 API Key。

## 文件

| 文件 | 用途 |
|------|------|
| `evaluation_score.py` | 核心评分类 |
| `quick_evaluate.py` / `batch_evaluate.py` | 快速/批量入口 |
| `ai_manual_evaluate.py` / `strict_manual_evaluator.py` | 人工辅助评估 |
| `config_example.py` | 配置模板（勿提交 `config.py`） |
| `README_评分说明.md` | 原理与 API 说明 |
| `使用指南.md` | 详细用法（路径需本地化） |

## 安装

```bash
pip install -r ../requirements.txt
```
