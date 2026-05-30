# 美国地区完整规范 - Sample001 (NVIDIA)

> **适用地区**: 美国 (United States)
> **Sample编号**: Sample001
> **Sample公司**: NVIDIA Corporation
> **验证集案例**: val043 (Exxon Mobil Corporation)

---

## 📋 地区基本信息

```yaml
地区: 美国
语言: 100%英文
货币: USD (美元)
Multiplier: Millions
会计准则: US GAAP (Generally Accepted Accounting Principles)
年报格式: Form 10-K (SEC规范)
```

---

## 🎯 语言规则

### 绝对规则
- ✅ **Section 1-6全部100%英文**
- ✅ 公司信息、分析内容、描述全部英文
- ❌ **严禁出现任何中文字符**

### 框架标准
```markdown
# Section 1: Company Overview
## S1.1: Basic Information
## S1.2: Core Competencies
## S1.3: Mission & Vision
```

**注意**：美国地区不需要语言分层，全部英文即可。

---

## 📊 Section 1: Company Overview

### S1.1: Basic Information

**表格格式**：
```markdown
| Field | Value |
| :---- | :---- |
| Company Name | [公司全名] |
| Establishment Date | [成立日期] |
| Headquarters Location | [城市, 州, USA] |
```

**提取标准**：
- Company Name: 年报封面完整名称
- Establishment Date: 如未披露填N/A
- Headquarters Location: 城市 + 州 + USA格式

**Sample001示例**：
```
| Company Name | NVIDIA Corporation |
| Establishment Date | April 1993 |
| Headquarters Location | Santa Clara, California, USA |
```

---

### S1.2: Core Competencies

**⚠️ 标题格式要求**：`## S1.2 : Core Competencies`（冒号前有空格）

**表格格式**：
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Innovation Advantages | [200-300字英文分析] | [200-300字英文分析] |
| Product Advantages | [200-300字英文分析] | [200-300字英文分析] |
| Brand Recognition | [150-250字英文分析] | [150-250字英文分析] |
| Reputation Ratings | [150-250字英文分析] | [150-250字英文分析] |
```

**内容要求**：
1. Innovation Advantages
   - R&D投入金额
   - 技术突破和专利
   - 创新平台和能力
   - 具体事实+数据支撑

2. Product Advantages
   - 核心产品线
   - 市场地位
   - 完整解决方案
   - 产品差异化优势

3. Brand Recognition
   - 品牌影响力
   - 市场认知度
   - 传播策略
   - 行业地位

4. Reputation Ratings
   - ESG表现
   - 行业认证
   - 利益相关者信任
   - 可持续发展承诺

**Sample001参考长度**：每项150-300字

---

### S1.3: Mission & Vision

**⚠️ 标题格式要求**：`## S1.3 : Mission & Vision`（冒号前有空格）

**表格格式**：
```markdown
| Field | Value |
| :---- | :---- |
| Mission Statement | [原文或N/A] |
| Vision Statement | [原文或N/A] |
| Core Values | [原文或N/A] |
```

**⚠️ 美国地区特殊要求**：列标题为 **Field | Value**（不是Answer）

**提取规则**：
- ✅ 必须年报原文引用
- ❌ 严禁推测、编造、改写
- ❌ 禁止使用公司网站信息
- ✅ 无明确披露时勇敢填N/A

**Sample001示例**：
```
| Mission Statement | N/A |
| Vision Statement | N/A |
| Core Values | Innovation is at our core. |
```

---

## 📊 Section 2: Financial Performance

### S2.1: Income Statement

**表格格式**：
```markdown
| Field | 2024 | 2023 | 2022 | Multiplier | Currency |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Revenue | [数值] | [数值] | [数值] | Millions | USD |
| Cost of Goods Sold | [数值] | [数值] | [数值] | Millions | USD |
| Gross Profit | [数值] | [数值] | [数值] | Millions | USD |
| Operating Expense | [数值] | [数值] | [数值] | Millions | USD |
| Operating Income | [数值] | [数值] | [数值] | Millions | USD |
| Net Profit | [数值] | [数值] | [数值] | Millions | USD |
| Income before income taxes | [数值] | [数值] | [数值] | Millions | USD |
| Income tax expense(benefit) | [数值] | [数值] | [数值] | Millions | USD |
| Interest Expense | [数值] | [数值] | [数值] | Millions | USD |
```

**美国特殊科目名称（US GAAP）**：
- Revenue = Total Revenue
- Net Profit = **Net Income** (合并口径)
- Operating Income = Operating Income / EBIT
- Income tax expense(benefit) = Provision for income taxes

**数据提取位置**：
- Consolidated Statements of Income
- 通常在Form 10-K的第50-60页附近

**Multiplier判断**：
```
查看年报标注：
"In millions" → Millions ✅
"In thousands" → Thousands
```

**数值格式**：
- 正数：60,922
- 负数：-257 或 (257)
- 保留原始精度，不凑整

**验证公式**：
```
✓ Gross Profit = Revenue - COGS
✓ Operating Income ≈ Gross Profit - Operating Expense
✓ Net Profit = Income Before Tax - Tax Expense
```

**Sample001示例**：
```
| Revenue | 60,922 | 26,974 | 26,914 | Millions | USD |
| Net Profit | 29,760 | 4,368 | 9,752 | Millions | USD |
```

---

### S2.2: Balance Sheet

**表格格式**：
```markdown
| Field | 2024 | 2023 | 2022 | Multiplier | Currency |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Total Assets | [数值] | [数值] | [数值] | Millions | USD |
| Current Assets | [数值] | [数值] | [数值] | Millions | USD |
| Non-Current Assets | [数值] | [数值] | [数值] | Millions | USD |
| Total Liabilities | [数值] | [数值] | [数值] | Millions | USD |
| Current Liabilities | [数值] | [数值] | [数值] | Millions | USD |
| Non-Current Liabilities | [数值] | [数值] | [数值] | Millions | USD |
| Shareholders' Equity | [数值] | [数值] | [数值] | Millions | USD |
| Retained Earnings | [数值] | [数值] | [数值] | Millions | USD |
| Total Equity and Liabilities | [数值] | [数值] | [数值] | Millions | USD |
| Inventories | [数值] | [数值] | [数值] | Millions | USD |
| Prepaid Expenses | [数值] | [数值] | [数值] | Millions | USD |
```

**美国特殊科目名称**：
- Shareholders' Equity = **Total Stockholders' Equity**
- Non-Current Assets = Long-term assets
- Prepaid Expenses = Prepaid expenses and other current assets

**⚠️ 关键注意**：
- Shareholders' Equity必须是**合并口径**（包含所有股东权益）
- 负债通常用正数表示（不加负号）

**必须验证（会计恒等式）**：
```
✓ Total Assets = Total Liabilities + Shareholders' Equity
✓ Total Assets = Total Equity and Liabilities
✓ Current + Non-Current Assets = Total Assets
✓ Current + Non-Current Liabilities = Total Liabilities
```

**Sample001示例**：
```
| Total Assets | 65,728 | 41,182 | 44,187 | Millions | USD |
| Shareholders' Equity | 42,978 | 22,101 | 26,612 | Millions | USD |
验证：65,728 = 22,750 + 42,978 ✅
```

---

### S2.3: Cash Flow Statement

**表格格式**：
```markdown
| Field | 2024 | 2023 | 2022 | Multiplier | Currency |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Net Cash Flow from Operations | [数值] | [数值] | [数值] | Millions | USD |
| Net Cash Flow from Investing | [数值] | [数值] | [数值] | Millions | USD |
| Net Cash Flow from Financing | [数值] | [数值] | [数值] | Millions | USD |
| Net Increase/Decrease in Cash | [数值] | [数值] | [数值] | Millions | USD |
| Dividends | [数值] | [数值] | [数值] | Millions | USD |
```

**美国特殊科目名称**：
- Net Cash Flow from Operations = Net cash provided by operating activities
- Dividends = Cash dividends paid (通常为负数)

**负数表示**：
- Sample001使用：-395 (负号)
- 部分公司使用：(395) (括号)
- 按实际年报格式

---

### S2.4: Key Financial Metrics

**表格格式**：
```markdown
|   | 2024 | 2023 | 2022 |
| :---- | :---- | :---- | :---- |
| Gross Margin | 72.71% | 56.92% | 64.9% |
| Operating Margin | 54.12% | 15.66% | 37.31% |
| Net Profit Margin | 48.85% | 16.20% | 36.23% |
| Current Ratio | 417.13% | 351.56% | 665.03% |
| Quick Ratio | 338.47% | 260.90% | 596.49% |
| Debt-to-Equity | 52.93% | 86.34% | 66.04% |
| Interest Coverage | 12,829.57% | 1,612.21% | 4,254.66% |
| Asset Turnover | 113.97% | 63.19% | N/A |
| Return on Equity | 91.46% | 17.93% | N/A |
| Return on Assets | 55.67% | 10.23% | N/A |
| Effective Tax Rate | 12.00% | -4.47% | 1.90% |
| Dividend Payout Ratio | 1.33% | 9.11% | 4.09% |
```

**⚠️ 美国地区特殊要求**：
- **第一列为空**（`|   |`，只有空格，无列标题）
- 无Multiplier和Currency列
- 纯百分比格式，所有数值必须包含%符号
- 保留2位小数

**计算公式**（全部×100%）：
```
1. Gross Margin = (Revenue - COGS) / Revenue × 100%
2. Operating Margin = Operating Income / Revenue × 100%
3. Net Profit Margin = Net Profit / Revenue × 100%
4. Current Ratio = Current Assets / Current Liabilities × 100%
5. Quick Ratio = (CA - Inventory - Prepaid) / CL × 100%
6. Debt-to-Equity = Total Liabilities / Shareholders' Equity × 100%
7. Interest Coverage = Operating Income / Interest Expense × 100%
8. Asset Turnover = Revenue / 平均总资产 × 100%
9. ROE = Net Profit / 平均股东权益 × 100%
10. ROA = Net Profit / 平均总资产 × 100%
11. Effective Tax Rate = Tax Expense / Income Before Tax × 100%
12. Dividend Payout Ratio = Dividends / Net Profit × 100%
```

**平均值计算**：
```
平均总资产_2024 = (Total Assets_2024 + Total Assets_2023) / 2
平均股东权益_2024 = (SE_2024 + SE_2023) / 2

2022年因缺期初数据：
Asset Turnover_2022 = N/A
ROE_2022 = N/A
ROA_2022 = N/A
```

**格式要求**：
- 保留2位小数
- 必须有%符号
- 负数：-4.47%
- 极大值用千位分隔：12,829.57%

---

### S2.5: Operating Performance

**表格格式**：
```markdown
| Field | 2024 | 2023 | 2022 |
| :---- | :---- | :---- | :---- |
| Revenue by Product/Service | [详细英文描述+数据] | [详细英文描述+数据] | [详细英文描述+数据] |
| Revenue by Geographic Region | [详细英文描述+数据] | [详细英文描述+数据] | [详细英文描述+数据] |
```

**内容要求**：
1. Revenue by Product/Service
   - 列出所有主要产品/服务线
   - 包含具体金额（带单位M）
   - 计算合计验证

2. Revenue by Geographic Region
   - 列出主要地理区域
   - 包含具体金额
   - 确保总和=Revenue

**Sample001示例**：
```
| Revenue by Product/Service | Compute & Networking: $47,405M Graphics: $13,517M Total: $60,922M | ... |
| Revenue by Geographic Region | United States: $26,966M Taiwan: $13,405M China (incl. HK): $10,306M Other: $10,245M Total: $60,922M | ... |
```

---

## 📊 Section 3: Business Analysis

### S3.1: Profitability Analysis

**表格格式**：
```markdown
| Field | Answer |
| :---- | :---- |
| Revenue & Direct-Cost Dynamics | [300-500字英文分析] |
| Operating Efficiency | [300-500字英文分析] |
| External & One-Off Impact | [200-400字英文分析] |
```

**⚠️ 美国地区特殊要求**：列标题为 **Field | Answer**

**分析要求**：
1. Revenue & Direct-Cost Dynamics
   - 收入增长趋势和驱动因素
   - 毛利率变化分析
   - 产品结构和地理分布
   - 具体数据支撑

2. Operating Efficiency
   - 营业利润率分析
   - 费用控制情况
   - 运营杠杆效应
   - 现金流表现

3. External & One-Off Impact
   - 有效税率波动
   - 非经常性损益
   - 外部因素影响
   - 一次性调整项

**Sample001参考长度**：每项200-500字

---

### S3.2: Financial Performance Summary

**表格格式**：
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Comprehensive financial health | [200-300字] | [200-300字] |
| Profitability and earnings quality | [200-300字] | [200-300字] |
| Operational efficiency | [200-300字] | [200-300字] |
| Financial risk identification and early warning | [200-300字] | [200-300字] |
| Future financial performance projection | [200-300字] | [200-300字] |
```

**5个维度详细要求**：每个维度都需要双年份对比

---

### S3.3: Business Competitiveness

**表格格式**：
```markdown
| Field | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Business Model | [150-250字] | [150-250字] |
| Market Position | [150-250字] | [150-250字] |
```

**⚠️ 美国地区特殊要求**：列标题为 **Field | 2024 Report | 2023 Report**

---

## 📊 Section 4: Risk Factors

**表格格式**：
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Market Risks | [150-250字] | [150-250字] |
| Operational Risks | [150-250字] | [150-250字] |
| Financial Risks | [150-250字] | [150-250字] |
| Compliance Risks | [150-250字] | [150-250字] |
```

---

## 📊 Section 5: Corporate Governance

### S5.1: Board Composition

**表格格式**：
```markdown
| Name | Position | Total Income |
| :---- | :---- | :---- |
| [董事姓名] | [职位] | [薪酬或N/A] |
```

**提取规则**：
- 列出所有执行董事/高管
- Total Income: 如披露填写，未披露填N/A
- 严禁编造数据

---

### S5.2: Internal Controls

**表格格式**：
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Risk assessment procedures | [100-150字] | [100-150字] |
| Control activities | [100-150字] | [100-150字] |
| Monitoring mechanisms | [100-150字] | [100-150字] |
| Identified material weaknesses or deficiencies | N/A | N/A |
| Effectiveness | N/A | N/A |
```

**注意**：最后两项通常为N/A

---

## 📊 Section 6: Future Outlook

### S6.1: Strategic Direction

**表格格式**：
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Mergers and Acquisition | [150-200字] | [150-200字] |
| New technologies | [150-200字] | [150-200字] |
| Organisational Restructuring | [100-150字或N/A] | [100-150字或N/A] |
```

---

### S6.2: Challenges and Uncertainties

**表格格式**：
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Economic challenges such as inflation, recession risks... | [150-200字] | [150-200字] |
| Competitive pressures from both established industry players... | [150-200字] | [150-200字] |
```

---

### S6.3: Innovation and Development Plans

**表格格式**：
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| R&D investments, with a focus on advancing technology... | [150-200字] | [150-200字] |
| New product launches, emphasizing the company's commitment... | [150-200字] | [150-200字] |
```

---

## ✅ 美国地区质量检查清单

### 语言检查
- [ ] Section 1-6全部100%英文
- [ ] 无任何中文字符
- [ ] 专业术语使用正确

### 格式检查
- [ ] S1.3列标题：Field | Value ✅
- [ ] S3.1列标题：Field | Answer ✅
- [ ] S3.3列标题：Field | 2024 Report | 2023 Report ✅
- [ ] S2.4第一列为空，无Multiplier/Currency ✅
- [ ] 所有section使用表格格式

### 数据检查
- [ ] Multiplier统一为Millions
- [ ] Currency统一为USD
- [ ] Balance Sheet平衡验证
- [ ] 12个财务指标全部计算
- [ ] 百分比格式正确（2位小数+%）

### 内容检查
- [ ] 所有数据从Form 10-K提取
- [ ] Net Profit使用合并口径
- [ ] Shareholders' Equity使用合并口径
- [ ] S1.3严格遵守N/A规则
- [ ] 分析深度符合Sample001标准

---

## 🎯 美国地区常见错误

### ❌ 错误1：语言混用
```markdown
错误：Revenue（营业收入）
正确：Revenue
```

### ❌ 错误2：列标题错误
```markdown
错误：S1.3用 Field | Answer
正确：S1.3用 Field | Value
```

### ❌ 错误3：数据口径错误
```markdown
错误：Net income attributable to shareholders
正确：Net income (合并口径，含少数股东)
```

### ❌ 错误4：Multiplier错误
```markdown
错误：使用Thousands（石油公司数据太大）
正确：使用Millions（查看年报标注）
```

---

## 📖 Sample001完整参考

**公司**：NVIDIA Corporation
**年报**：Form 10-K 2024
**位置**：samples/sample001.md

**关键特征**：
- 科技公司，GPU和AI领域
- 收入高速增长（126% 2022-2024）
- 毛利率极高（72%+）
- 现金流强劲
- 无银行借款

**可参考点**：
- Section 1-2格式完全标准
- Section 3分析深度适中
- 财务指标计算准确
- 语言专业地道

---

*美国地区完整规范 v1.0 - 基于Sample001 (NVIDIA)*
