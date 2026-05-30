# 年报分析质量评分系统使用说明

基于 [DeepEval SummarizationMetric](https://deepeval.com/docs/metrics-summarization#how-is-it-calculated) 实现的年报分析质量评分系统。

## 评分原理

根据 DeepEval 文档，Summarization 指标通过以下公式计算：

```
Summarization Score = min(Alignment Score, Coverage Score)
```

其中：
- **Alignment Score（对齐分数）**: 评估生成的总结是否包含与原文矛盾或虚构的信息
- **Coverage Score（覆盖率分数）**: 评估生成的总结是否包含原文的必要信息

## 安装依赖

```bash
pip install deepeval
```

## 快速开始

### 1. 基础使用示例

```python
from deepeval.test_case import LLMTestCase
from deepeval.metrics import SummarizationMetric

# 原始年报文本
input_text = """
公司收入在2022-2023年间实现强劲增长7.7%，2023-2024年间继续保持稳健增长3.1%。
毛利率持续改善，从2022年的27.78%提升至2024年的29.01%...
"""

# 生成的分析内容
actual_output = """
公司收入保持稳健增长，毛利率持续改善，显示出良好的成本控制能力...
"""

# 创建测试用例
test_case = LLMTestCase(
    input=input_text,
    actual_output=actual_output
)

# 创建评估指标
metric = SummarizationMetric(
    threshold=0.5,
    model="gpt-4",
    assessment_questions=[
        "分析是否包含收入增长率的讨论?",
        "是否准确反映了毛利率的变化趋势?",
        "是否提及了营业利润率的表现?"
    ]
)

# 执行评估
metric.measure(test_case)

# 查看结果
print(f"总分: {metric.score}")
print(f"对齐分数: {metric.score_breakdown['Alignment Score']}")
print(f"覆盖率分数: {metric.score_breakdown['Coverage Score']}")
print(f"评估原因: {metric.reason}")
```

### 2. 使用评分系统类

```python
from evaluation_score import AnnualReportEvaluator, SECTION_ASSESSMENT_QUESTIONS

# 初始化评估器
evaluator = AnnualReportEvaluator(
    model="gpt-4",      # 可选: gpt-4, gpt-4o, gpt-3.5-turbo
    threshold=0.5       # 通过阈值
)

# 评估单个章节
result = evaluator.evaluate_section(
    original_text="原始年报文本...",
    generated_summary="生成的分析内容...",
    section_name="Section 3.1 Profitability Analysis",
    assessment_questions=SECTION_ASSESSMENT_QUESTIONS["Section 3.1 Profitability Analysis"]
)

print(f"章节分数: {result['score']:.3f}")
```

### 3. 评估完整报告

```python
# 准备所有章节数据
sections_data = [
    {
        "section_name": "Section 3.1 Profitability Analysis",
        "original_text": "原始年报相关文本...",
        "generated_summary": "生成的盈利能力分析...",
        "assessment_questions": SECTION_ASSESSMENT_QUESTIONS["Section 3.1 Profitability Analysis"]
    },
    {
        "section_name": "Section 3.2 Financial Performance Summary",
        "original_text": "原始年报相关文本...",
        "generated_summary": "生成的财务表现总结...",
        "assessment_questions": SECTION_ASSESSMENT_QUESTIONS["Section 3.2 Financial Performance Summary"]
    },
    # ... 更多章节
]

# 评估完整报告
final_results = evaluator.evaluate_full_report(
    sections_data=sections_data,
    output_file="evaluation_results.json"
)

print(f"整体分数: {final_results['overall_score']:.3f}")
print(f"通过章节: {final_results['passed_sections']}/{final_results['total_sections']}")
```

## 参数说明

### SummarizationMetric 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `threshold` | float | 0.5 | 通过阈值，分数需要 >= 该值才算通过 |
| `model` | str | "gpt-4.1" | 评估使用的模型 |
| `assessment_questions` | List[str] | None | 评估问题列表（是/否问题） |
| `n` | int | 5 | 未提供问题时自动生成的问题数量 |
| `include_reason` | bool | True | 是否包含评估原因 |
| `strict_mode` | bool | False | 严格模式（完美=1，其他=0） |
| `async_mode` | bool | True | 是否启用异步执行 |
| `verbose_mode` | bool | False | 是否打印详细过程 |
| `truths_extraction_limit` | int | None | 提取真实信息的最大数量 |

### 评估问题设计原则

根据 DeepEval 文档，评估问题应该：
1. **是封闭式问题**：只能用"是"或"否"回答
2. **关注关键信息**：聚焦于总结应该包含的重要内容
3. **清晰明确**：避免模糊或多义的表述

示例：
- ✅ 好的问题："分析是否包含收入增长率的讨论？"
- ❌ 不好的问题："分析质量如何？"（开放式）
- ❌ 不好的问题："分析是否全面？"（过于模糊）

## 预定义评估问题

系统为各章节预定义了评估问题：

### Section 3: Business Analysis
- **3.1 Profitability Analysis**: 5个问题（收入、毛利率、营业利润率、税率、非经常性项目）
- **3.2 Financial Performance Summary**: 5个问题（财务健康、盈利质量、运营效率、风险、预测）
- **3.3 Business Competitiveness**: 3个问题（商业模式、市场地位、市场份额）

### Section 4: Risk Factors
- **4.1 Risk Factors**: 4个问题（市场风险、运营风险、财务风险、合规风险）

### Section 5: Corporate Governance
- **5.1 Board Composition**: 3个问题（姓名、职位、薪酬）
- **5.2 Internal Controls**: 5个问题（风险评估、控制活动、监督机制、有效性、缺陷）

### Section 6: Future Outlook
- **6.1 Strategic Direction**: 3个问题（并购、新技术、组织重组）
- **6.2 Challenges and Uncertainties**: 2个问题（经济挑战、竞争压力）
- **6.3 Innovation and Development Plans**: 2个问题（研发投入、新产品）

## 输出结果格式

评估结果保存为 JSON 格式：

```json
{
  "overall_score": 0.75,
  "overall_alignment_score": 0.80,
  "overall_coverage_score": 0.70,
  "total_sections": 9,
  "passed_sections": 8,
  "section_results": [
    {
      "section_name": "Section 3.1 Profitability Analysis",
      "score": 0.75,
      "alignment_score": 0.80,
      "coverage_score": 0.75,
      "reason": "总结准确反映了原文的关键财务指标，但在非经常性项目的讨论上略有不足..."
    }
  ]
}
```

## 评分标准解读

- **0.0 - 0.3**: 质量较差，需要大幅改进
- **0.3 - 0.5**: 质量一般，部分内容缺失或不准确
- **0.5 - 0.7**: 质量良好，基本满足要求
- **0.7 - 0.9**: 质量优秀，准确且全面
- **0.9 - 1.0**: 质量卓越，近乎完美

## 常见问题

### 1. 如何提高覆盖率分数？
确保生成的分析包含原文的所有关键信息点。

### 2. 如何提高对齐分数？
避免添加原文中没有的信息，确保所有陈述都有原文依据。

### 3. 是否需要提供评估问题？
不是必需的。如果不提供，系统会自动生成 n 个问题（默认5个）。但提供特定问题可以让评估更贴合您的需求。

### 4. 评估速度如何优化？
- 启用 `async_mode=True`（默认）
- 减少评估问题数量
- 使用更快的模型（如 gpt-3.5-turbo）

### 5. 如何设置 truths_extraction_limit？
当原文很长时，可以限制提取的关键真实信息数量，例如只考虑最重要的20条信息：
```python
metric = SummarizationMetric(truths_extraction_limit=20)
```

## 参考资源

- [DeepEval Summarization Metric 官方文档](https://deepeval.com/docs/metrics-summarization#how-is-it-calculated)
- [DeepEval GitHub](https://github.com/confident-ai/deepeval)
- [LLM评估指南](https://deepeval.com/blog/llm-evaluation-metrics)

## 联系方式

如有问题，请参考 DeepEval 官方文档或在 GitHub 提 Issue。

