# 🤖 AI快速使用财小析指南

**目标用户**: 其他AI系统  
**版本**: Pipeline 3.6  
**更新时间**: 2025-10-21

---

## 🔴 最新更新（3.6版本）

### 格式迭代：Sample格式细节补充（2025-10-22）
**必读文档**: `Sample格式细节补充_3.6.md`

**关键发现**：
1. **S1.2和S1.3标题格式** - 冒号前有空格
   - 正确：`## S1.2 : Core Competencies`
   - 正确：`## S1.3 : Mission & Vision`
   - 错误：`## S1.2: Core Competencies`（无空格）

2. **S2.4第一列为空** - 所有8个地区统一
   - 表格第一列：`|   |`（只有空格）
   - 无列标题
   - 所有数值必须包含%符号

3. **负数格式** - 按地区差异
   - 中国：`\-48,875,311`（反斜杠转义）
   - IFRS地区：`(335.8)`（括号）
   - 美国：`-257`（负号）

### 紧急修正：N/A滥用问题（2025-10-21）
**必读文档**: `紧急修正_N/A滥用问题_3.6.md`

**关键规则**：
1. **禁止偷懒填N/A** - Section 2.1-2.3的所有字段都必须从年报提取
2. **格式精确匹配** - 标题冒号前有空格、中国地区使用`N.A`而非`N/A`
3. **数据100%真实** - 不允许"年报未披露"的借口

---

## 🚀 30秒快速上手

### Step 1: 读取核心规则（必须）
```
必读文档（按优先级）：
1. 紧急修正_N/A滥用问题_3.6.md ⭐⭐⭐ 最新修正
2. Section2完整规范_3.6.md ⭐ Section 2详细规范
3. 数据口径与内容取数总则_3.6.md ⭐ 数据口径规范
4. 地区规范核对清单_3.6.md - 地区格式标准
```

### Step 2: 识别公司地区
```python
def identify_region(company_info):
    if "CNY" in company_info and "中文" in company_info:
        return "中国A股", "Thousands", "CNY", "N.A"
    elif "USD" in company_info and "英文" in company_info:
        return "美国", "Millions", "USD", "N/A"
    elif "SGD" in company_info and "英文" in company_info:
        return "新加坡", "Thousands", "SGD", "N/A"
    elif "RM" in company_info and "英文" in company_info:
        return "马来西亚", "Thousands", "RM", "N/A"
    elif "GBP" in company_info and "英文" in company_info:
        return "英国", "Millions", "GBP", "N/A"
```

### Step 3: 应用核心规则
```
✅ 数据口径：合并净利润 + 合并权益（含少数股东）
✅ 表格格式：| Field | 2024 | 2023 | 2022 | Multiplier | Currency |
✅ 财务指标：严格按12个公式计算，百分比格式
✅ 内容结构：S1.2/S3.2双年份对比，S3.1单列表格
✅ N/A使用：Section 2禁止滥用N/A，必须提取真实数据
```

---

## 🎯 关键规则速查

### 绝对不能违反的规则

#### 1. **数据口径**（零容忍）
```
✅ Net Profit = 合并净利润（含少数股东损益）
✅ Shareholders' Equity = 所有者权益合计（含少数股东权益）
❌ 绝不使用"归属于母公司"数据
```

#### 2. **N/A使用规则**（3.6新增）
```
Section 2.1 Income Statement:
✅ Revenue - 必填
✅ Cost of Goods Sold - 必填（制造业）
✅ Gross Profit - 必填
✅ Operating Expense - 必填
✅ Operating Income - 必填
✅ Net Profit - 必填
✅ Income Before Tax - 必填
✅ Tax Expense - 必填
✅ Interest Expense - 必填

❌ 禁止填N/A的情况：中国A股年报披露完整，所有数据都能找到
✅ 允许N/A的情况：纯服务业的COGS、年报确实未披露的细分项目
```

#### 3. **表格格式**
```
✅ S2.1-S2.3: 必须包含Multiplier和Currency列
✅ S2.4: 纯百分比格式，无Multiplier/Currency列
✅ S2.5: 标准三年对比表格
✅ 中国地区标题：## S1.2 : Core Competencies（冒号前有空格）
✅ 中国地区N/A：使用N.A（点号）而非N/A（斜杠）
```

#### 4. **财务指标计算**
```python
# 必须使用这些公式，百分比格式，保留2位小数
Gross_Margin = (Revenue - COGS) / Revenue * 100  # 如COGS=N/A则结果=N/A
Operating_Margin = Operating_Income / Revenue * 100
Net_Profit_Margin = Net_Income / Revenue * 100
Current_Ratio = Current_Assets / Current_Liabilities * 100
Quick_Ratio = (Current_Assets - Inventories - Prepaid) / Current_Liabilities * 100
Debt_to_Equity = Total_Liabilities / Shareholders_Equity * 100
Interest_Coverage = Operating_Income / Interest_Expense * 100  # 注意：结果可能>10000%
Asset_Turnover = Revenue / 平均总资产 * 100  # 2022年=N/A
ROE = Net_Income / 平均股东权益 * 100  # 2022年=N/A
ROA = Net_Income / 平均总资产 * 100  # 2022年=N/A
Effective_Tax_Rate = Tax_Expense / Income_Before_Tax * 100
Dividend_Payout_Ratio = Dividends / Net_Income * 100
```

---

## 🌍 地区差异化处理

### 中国A股（Sample003）
```yaml
识别特征: CNY + 中文
Multiplier: Thousands
净利润来源: "五、净利润" 或 "净利润"（合并口径）
权益来源: "所有者权益合计"（含少数股东权益）
表头格式: "宁德时代新能源科技股份有限公司2024年年度报告"
标题格式: "## S1.2 : Core Competencies"（冒号前有空格）
N/A格式: "N.A"（用点号）
数据提取: 必须从"合并财务报表"提取，禁止填N/A
```

### 美国公司（Sample001）
```yaml
识别特征: USD + 英文
Multiplier: Millions
净利润来源: "Net income" (合并口径)
权益来源: "Total stockholders' equity"
表头格式: "2024 Report"
标题格式: "## S1.2: Core Competencies"（冒号前无空格）
N/A格式: "N/A"（用斜杠）
```

### 新加坡（Sample005）
```yaml
识别特征: SGD + 英文
Multiplier: Thousands
净利润来源: "Profit after tax and minority interest (PATMI)"
权益来源: "Total equity"
表头格式: "2024 Report"
负数格式: 使用括号 (123)
```

### 马来西亚（Sample007）
```yaml
识别特征: RM + 英文
Multiplier: Thousands
净利润来源: "Profit for the year"
权益来源: "Total equity"
表头格式: "2024 Report"
```

### 英国公司（Sample002）
```yaml
识别特征: GBP + 英文
Multiplier: Millions
特殊处理: 服务业COGS可能为N/A
表头格式: "2024 Report"
```

### 印尼（Sample008）
```yaml
识别特征: IDR + 英文
Multiplier: Billions（特别注意！）
净利润来源: "Profit for the year"
权益来源: "Total equity"
表头格式: "2024 Report"
```

---

## 📋 Section 2数据提取流程（3.6强化）

### Step 1: 定位财务报表
```
中国A股：第十节 财务报告 → 合并财务报表
美国：Financial Statements → Consolidated Statements
新加坡/马来西亚：Financial Statements → Consolidated
```

### Step 2: 精确提取数据
```
利润表（Income Statement）：
- Revenue = 营业收入（第一行）
- COGS = 营业成本
- Gross Profit = Revenue - COGS
- Operating Expense = 销售费用 + 管理费用 + 研发费用 + 财务费用
- Operating Income = 营业利润
- Net Profit = 净利润（合并口径，含少数股东损益）
- Income Before Tax = 利润总额
- Tax Expense = 所得税费用

资产负债表（Balance Sheet）：
- Total Assets = 资产总计
- Current Assets = 流动资产合计
- Non-Current Assets = 非流动资产合计
- Total Liabilities = 负债合计
- Shareholders' Equity = 所有者权益合计（含少数股东权益）
- Inventories = 存货
- Prepaid Expenses = 预付款项

现金流量表（Cash Flow Statement）：
- Operating Cash Flow = 经营活动产生的现金流量净额
- Investing Cash Flow = 投资活动产生的现金流量净额
- Financing Cash Flow = 筹资活动产生的现金流量净额
- Net Change in Cash = 现金及现金等价物净增加额
- Dividends = 分配股利、利润或偿付利息支付的现金
```

### Step 3: 验证数据合理性
```python
# 必须通过的验证
assert Gross_Profit == Revenue - COGS
assert Net_Profit == Income_Before_Tax - Tax_Expense
assert Total_Assets == Total_Liabilities + Shareholders_Equity
assert Current_Assets + Non_Current_Assets == Total_Assets
```

---

## ⚠️ 常见错误避免（3.6更新）

### 1. N/A滥用错误（最严重）
```
❌ 错误：Section 2.1有5个N/A（Cost of Goods Sold, Gross Profit等）
✅ 正确：中国A股年报披露完整，所有数据都能找到，N/A应该是0个

❌ 错误：看到"年报未披露"就填N/A
✅ 正确：仔细搜索年报，从合并财务报表中提取真实数据
```

### 2. 格式细节错误
```
❌ 错误：## S1.2: Core Competencies（中国地区）
✅ 正确：## S1.2 : Core Competencies（冒号前有空格）

❌ 错误：| Mission Statement | N/A |（中国地区）
✅ 正确：| Mission Statement | N.A |（用点号）

❌ 错误：表头使用"2024 Report"（中国地区）
✅ 正确：表头使用"宁德时代新能源科技股份有限公司2024年年度报告"
```

### 3. 数据口径错误
```
❌ 错误：使用"归属于上市公司股东的净利润"
✅ 正确：使用"五、净利润"（合并口径）

❌ 错误：使用"归属于母公司所有者权益"
✅ 正确：使用"所有者权益合计"（含少数股东）
```

### 4. 计算错误
```
❌ 错误：Current Ratio = 1.31（倍数）
✅ 正确：Current Ratio = 131.00%（百分比）

❌ 错误：Interest Coverage = 1094.28%
✅ 正确：Interest Coverage = 109428.00%（注意倍数转换）
```

---

## 🔍 质量检查清单（3.6强化）

### 生成前检查（Pre-Check）
- [ ] 已定位到年报的"合并财务报表"部分
- [ ] 已确认Multiplier（中国A股通常是Thousands）
- [ ] 已确认该公司是制造业还是服务业
- [ ] 已确认地区格式标准（标题空格、N/A格式）

### Section 2数据检查
- [ ] S2.1: 9个字段都从年报提取，N/A不超过1个
- [ ] S2.2: 11个字段都从年报提取，N/A = 0个
- [ ] S2.3: 5个字段都从年报提取，N/A = 0个
- [ ] S2.4: 12个指标都计算，百分比格式，保留2位小数
- [ ] 验证：Gross Profit = Revenue - COGS
- [ ] 验证：Net Profit = Income Before Tax - Tax Expense
- [ ] 验证：Total Assets = Total Liabilities + Shareholders' Equity

### 格式检查
- [ ] 表格使用标准markdown格式
- [ ] 表头符合地区标准（中国用公司全称+年度报告）
- [ ] 标题格式正确（中国地区冒号前有空格）
- [ ] N/A格式正确（中国用N.A，其他地区用N/A）
- [ ] 数值格式正确（百分比保留2位小数）

### 内容完整性检查
- [ ] S1.2四个维度双年份对比
- [ ] S3.2五个维度双年份对比
- [ ] S5.2六项内控要素完整
- [ ] 整个报告N/A总数不超过5个

---

## 🎯 成功标准（3.6版本）

**目标得分**: 216+/240分（90%+）

**关键成功因素**:
1. ✅ Section 2数据100%真实提取，N/A不超过3个
2. ✅ 格式精确匹配sample标准（标题空格、N/A格式）
3. ✅ 严格遵循数据口径规则（合并净利润+合并权益）
4. ✅ 准确计算12项财务指标（百分比格式）
5. ✅ 地区差异化处理（表头、语言、格式）

**质量保证**:
- Section 2得分目标：>100/117 (85%+)
- 总体得分目标：>216/240 (90%+)
- 返工率：<10%

---

## 💡 3.6版本核心改进

### 从3.5到3.6的主要变化

1. **新增N/A滥用问题专项修正**
   - 明确禁止Section 2偷懒填N/A
   - 提供详细的数据提取流程
   - 强化验证机制

2. **格式细节精确化**
   - 中国地区标题格式：冒号前有空格
   - 中国地区N/A格式：使用N.A而非N/A
   - 表头格式：中国用公司全称+年度报告

3. **质量标准提升**
   - Section 2的N/A不超过3个
   - 数据100%可验证
   - 格式100%匹配sample

---

## 📚 参考文档

**必读文档**：
1. `紧急修正_N/A滥用问题_3.6.md` - N/A问题专项修正
2. `Section2完整规范_3.6.md` - Section 2详细规范
3. `数据口径与内容取数总则_3.6.md` - 数据口径规范
4. `单Case质量保证流程_3.6.md` - 质量保证流程

**地区规范**：
- `地区规范/中国_Sample003_格式标准.md`
- `地区规范/美国_Sample001_格式标准.md`
- `地区规范/新加坡_Sample005_格式标准.md`
- 等8个地区的详细规范

---

**财小析 Pipeline 3.6 - 质量优先，零容忍N/A滥用！** 🤖🚀
