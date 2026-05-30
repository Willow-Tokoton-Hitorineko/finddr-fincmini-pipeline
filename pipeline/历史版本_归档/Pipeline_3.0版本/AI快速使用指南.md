# 🤖 AI快速使用财小析指南

**目标用户**: 其他AI系统  
**版本**: Pipeline 3.0  
**更新时间**: 2025-10-20

---

## 🚀 30秒快速上手

### Step 1: 读取核心规则（必须）
```
请立即读取：财小析_Pipeline_3.0_完整规则手册.md
这是唯一必需的核心文档，包含所有规则。
```

### Step 2: 识别公司地区
```python
def identify_region(company_info):
    if "CNY" in company_info and "中文" in company_info:
        return "中国A股", "Thousands", "CNY"
    elif "USD" in company_info and "英文" in company_info:
        return "美国", "Millions", "USD"
    elif "RM" in company_info and "英文" in company_info:
        return "新加坡/马来西亚", "Millions", "RM"
    elif "GBP" in company_info and "英文" in company_info:
        return "英国", "Millions", "GBP"
```

### Step 3: 应用核心规则
```
✅ 数据口径：合并净利润 + 合并权益（含少数股东）
✅ 表格格式：| Field | 2024 | 2023 | 2022 | Multiplier | Currency |
✅ 财务指标：严格按12个公式计算，百分比格式
✅ 内容结构：S1.2/S3.2双年份对比，S3.1单列表格
```

---

## 🎯 关键规则速查

### 绝对不能违反的规则

1. **数据口径**
```
✅ Net Profit = 合并净利润（含少数股东损益）
✅ Shareholders' Equity = 所有者权益合计（含少数股东权益）
❌ 绝不使用"归属于母公司"数据
```

2. **表格格式**
```
✅ S2.1-S2.3: 必须包含Multiplier和Currency列
✅ S2.4: 纯百分比格式，无Multiplier/Currency列
✅ S2.5: 标准三年对比表格
```

3. **财务指标计算**
```python
# 必须使用这些公式
Gross_Margin = (Revenue - COGS) / Revenue * 100  # 如COGS=N/A则结果=N/A
Operating_Margin = Operating_Income / Revenue * 100
Net_Profit_Margin = Net_Income / Revenue * 100
Current_Ratio = Current_Assets / Current_Liabilities * 100
Quick_Ratio = (Current_Assets - Inventories - Prepaid) / Current_Liabilities * 100
Debt_to_Equity = Total_Liabilities / Shareholders_Equity * 100
Interest_Coverage = Operating_Income / Interest_Expense * 100
Asset_Turnover = Revenue / 平均总资产 * 100  # 2022年=N/A
ROE = Net_Income / 平均股东权益 * 100  # 2022年=N/A
ROA = Net_Income / 平均总资产 * 100  # 2022年=N/A
Effective_Tax_Rate = Tax_Expense / Income_Before_Tax * 100
Dividend_Payout_Ratio = Dividends / Net_Income * 100
```

---

## 🌍 地区差异化处理

### 中国A股
```yaml
识别特征: CNY + 中文
Multiplier: Thousands
净利润来源: "五、净利润" 或 "净利润"
权益来源: "所有者权益合计"
表头格式: "宜宾五粮液股份有限公司2024年年度报告"
```

### 美国公司
```yaml
识别特征: USD + 英文
Multiplier: Millions
净利润来源: "Net income attributable to [Company]"
权益来源: "[Company] shareholders' equity"
表头格式: "2024 Report"
```

### 新加坡/马来西亚
```yaml
识别特征: RM + 英文
Multiplier: Millions
净利润来源: "PATMI" 或 "Profit after tax and minority interest"
权益来源: "Total equity"
表头格式: "2024 Report"
```

### 英国公司
```yaml
识别特征: GBP + 英文
Multiplier: Millions
特殊处理: 服务业COGS可能为N/A
表头格式: "2024 Report"
```

---

## 📋 内容结构模板

### S1.2 Core Competencies
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Innovation Advantages | 详细描述... | 详细描述... |
| Product Advantages | 详细描述... | 详细描述... |
| Brand Recognition | 详细描述... | 详细描述... |
| Reputation Ratings | 详细描述... | 详细描述... |
```

### S2.1 Income Statement
```markdown
| Field | 2024 | 2023 | 2022 | Multiplier | Currency |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Revenue | 89,175,178 | 83,272,067 | 73,968,641 | Thousands | CNY |
| Cost of Goods Sold | 20,461,423 | 20,157,144 | 18,178,426 | Thousands | CNY |
| Gross Profit | 68,713,755 | 63,114,923 | 55,790,215 | Thousands | CNY |
| Operating Expense | 27,693,582 | 22,171,413 | 18,927,229 | Thousands | CNY |
| Operating Income | 44,200,076 | 42,003,664 | 37,174,423 | Thousands | CNY |
| Net Profit | 33,193,460 | 31,520,778 | 27,969,786 | Thousands | CNY |
| Income before income taxes | 44,163,325 | 41,912,682 | 37,103,521 | Thousands | CNY |
| Income tax expense(benefit) | 10,969,865 | 10,391,904 | 9,133,735 | Thousands | CNY |
| Interest Expense | 40,437 | 11,618 | 48,004 | Thousands | CNY |
```

### S2.4 Key Financial Metrics
```markdown
|  | 2024 | 2023 | 2022 |
| :---- | :---- | :---- | :---- |
| Gross Margin | 77.05% | 75.79% | 75.42% |
| Operating Margin | 49.57% | 50.44% | 50.26% |
| Net Profit Margin | 37.22% | 37.85% | 37.80% |
| Current Ratio | 324.90% | 450.33% | 384.70% |
| Quick Ratio | 288.88% | 396.61% | 339.63% |
| Debt-to-Equity | 38.02% | 25.00% | 30.96% |
| Interest Coverage | 109306.02% | 361539.54% | 77440.26% |
| Asset Turnover | 50.43% | 52.33% | N/A |
| Return on Equity | 24.70% | 25.31% | N/A |
| Return on Assets | 18.77% | 19.83% | N/A |
| Effective Tax Rate | 24.84% | 24.79% | 24.62% |
| Dividend Payout Ratio | 84.74% | 46.57% | 41.96% |
```

### S3.1 Profitability Analysis
```markdown
| Perspective | Answer |
| :---- | :---- |
| Revenue & Direct-Cost Dynamics | 详细分析... |
| Operating Efficiency | 详细分析... |
| External & One-Off Impact | 详细分析... |
```

### S5.2 Internal Controls (必须6项)
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Risk assessment procedures | ... | ... |
| Control activities | ... | ... |
| Monitoring mechanisms | ... | ... |
| Identified material weaknesses | ... | ... |
| Improvements | ... | ... |
| Effectiveness | ... | ... |
```

---

## ⚠️ 常见错误避免

### 数据口径错误
```
❌ 错误：使用"归属于上市公司股东的净利润"
✅ 正确：使用"五、净利润"（合并口径）

❌ 错误：使用"归属于母公司所有者权益"
✅ 正确：使用"所有者权益合计"（含少数股东）
```

### 格式错误
```
❌ 错误：S2.4包含Multiplier列
✅ 正确：S2.4只有百分比，无Multiplier/Currency

❌ 错误：财务指标用倍数格式（如2.47x）
✅ 正确：财务指标用百分比格式（如247.00%）
```

### 计算错误
```
❌ 错误：Current Ratio = 1.31（倍数）
✅ 正确：Current Ratio = 131.00%（百分比）

❌ 错误：Interest Coverage = 1094.28%
✅ 正确：Interest Coverage = 109428.00%（注意倍数转换）
```

---

## 🔍 质量检查清单

处理完成后，请检查：

**Section 2 财务数据**：
- [ ] S2.1-S2.3包含Multiplier和Currency列
- [ ] S2.4使用百分比格式，保留2位小数
- [ ] 12项财务指标计算正确
- [ ] 数据口径统一（合并净利润+合并权益）

**格式规范**：
- [ ] 表格使用标准markdown格式
- [ ] 表头符合地区标准
- [ ] N/A使用规范，无自行推测
- [ ] 数值格式正确

**内容完整**：
- [ ] S1.2四个维度双年份对比
- [ ] S3.2五个维度双年份对比
- [ ] S5.2六项内控要素完整

---

## 🎯 成功标准

**目标得分**: 230+/240分（96%+）

**关键成功因素**:
1. 严格遵循数据口径规则
2. 准确计算12项财务指标
3. 使用标准表格格式
4. 地区差异化处理
5. 内容结构完整

---

**财小析 Pipeline 3.0 - AI智能使用，精准高效！** 🤖🚀
