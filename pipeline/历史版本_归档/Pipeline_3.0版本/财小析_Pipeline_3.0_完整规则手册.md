# 财小析 Pipeline 3.0 完整规则手册

**版本**: Pipeline 3.0  
**更新时间**: 2025-10-20  
**状态**: 生产就绪版本

---

## 🎯 财小析系统概述

**财小析**是专门为FinDDR 2025比赛设计的年报智能分析系统，具备：
- ✅ 多地区差异化处理能力（中国、美国、新加坡、英国等）
- ✅ 多会计准则适配（中国GAAP、US GAAP、IFRS、MFRS）
- ✅ 严格按官方CSV标准生成6-Section报告
- ✅ 目标得分：**230+/240分**（96%+）

---

## 📋 核心数据口径规则（绝不可违反）

### 1. 净利润口径
```
✅ 正确：合并净利润（含少数股东损益）
❌ 错误：归属于母公司净利润

中国GAAP: "五、净利润" 或 "净利润"
US GAAP: "Net income attributable to [Company]"
IFRS/MFRS: "Profit after tax and minority interest (PATMI)"
```

### 2. 股东权益口径
```
✅ 正确：所有者权益合计（含少数股东权益）
❌ 错误：归属于母公司所有者权益

中国GAAP: "所有者权益合计"
US GAAP: "[Company] shareholders' equity" 或 "Total equity"
IFRS/MFRS: "Total equity"
```

### 3. 口径一致性检查
```python
# 必须确保Net Profit和Shareholders' Equity使用同一口径
if net_profit_source == "合并":
    shareholders_equity_source = "合并"
elif net_profit_source == "归母":
    shareholders_equity_source = "归母"  # 但这是错误的，应避免
```

---

## 📊 Section 2: Financial Performance 完整标准

### S2.1-S2.3 表格格式标准
```markdown
| Field | 2024 | 2023 | 2022 | Multiplier | Currency |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Revenue | 89,175,178 | 83,272,067 | 73,968,641 | Thousands | CNY |
```

### S2.4 财务指标计算公式
```python
# 1. 毛利率
Gross_Margin = (Revenue - COGS) / Revenue * 100
# 如果COGS=N/A，则Gross_Margin=N/A

# 2. 营业利润率
Operating_Margin = Operating_Income / Revenue * 100

# 3. 净利润率
Net_Profit_Margin = Net_Income / Revenue * 100

# 4. 流动比率
Current_Ratio = Current_Assets / Current_Liabilities * 100

# 5. 速动比率
Quick_Ratio = (Current_Assets - Inventories - Prepaid_Expenses) / Current_Liabilities * 100

# 6. 资产负债率
Debt_to_Equity = Total_Liabilities / Shareholders_Equity * 100

# 7. 利息保障倍数
Interest_Coverage = Operating_Income / Interest_Expense * 100

# 8. 资产周转率（需要平均值）
Asset_Turnover = Revenue / ((Total_Assets_2024 + Total_Assets_2023) / 2) * 100
# 2022年填N/A（缺少2021年数据）

# 9. 净资产收益率（需要平均值）
ROE = Net_Income / ((Shareholders_Equity_2024 + Shareholders_Equity_2023) / 2) * 100
# 2022年填N/A（缺少2021年数据）

# 10. 总资产收益率（需要平均值）
ROA = Net_Income / ((Total_Assets_2024 + Total_Assets_2023) / 2) * 100
# 2022年填N/A（缺少2021年数据）

# 11. 有效税率
Effective_Tax_Rate = Tax_Expense / Income_Before_Tax * 100

# 12. 股利支付率
Dividend_Payout_Ratio = Dividends / Net_Income * 100
```

### S2.4 格式要求
```markdown
|  | 2024 | 2023 | 2022 |
| :---- | :---- | :---- | :---- |
| Gross Margin | 77.05% | 75.79% | 75.42% |
```
**注意**：S2.4不包含Multiplier和Currency列

---

## 🌍 地区差异化处理规则

### 中国A股公司
```yaml
货币: CNY (人民币)
会计准则: 中国企业会计准则
Multiplier判断: 
  - 大型企业: Thousands (千元)
  - 中型企业: Ones (元)
特殊处理:
  - 净利润: 使用"五、净利润"，避免"归属于上市公司股东"
  - 表头: "宜宾五粮液股份有限公司2024年年度报告"
```

### 美国公司
```yaml
货币: USD (美元)
会计准则: US GAAP
Multiplier判断: Millions (百万美元)
特殊处理:
  - 净利润: "Net income attributable to [Company]"
  - 股东权益: "[Company] shareholders' equity"
  - 表头: "2024 Report"
```

### 新加坡/马来西亚公司
```yaml
货币: RM (马来西亚林吉特)
会计准则: MFRS (基于IFRS)
Multiplier判断: Millions (百万林吉特)
特殊处理:
  - 净利润: PATMI (Profit After Tax and Minority Interest)
  - 表头: "2024 Report"
```

### 英国公司
```yaml
货币: GBP (英镑)
会计准则: IFRS
Multiplier判断: Millions (百万英镑)
特殊处理:
  - 服务业COGS可能为N/A
  - 表头: "2024 Report"
```

---

## 📝 Section内容结构标准

### S1.2 Core Competencies (双年份对比表格)
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Innovation Advantages | 详细描述2024年创新优势... | 详细描述2023年创新优势... |
| Product Advantages | 详细描述2024年产品优势... | 详细描述2023年产品优势... |
| Brand Recognition | 详细描述2024年品牌认知... | 详细描述2023年品牌认知... |
| Reputation Ratings | 详细描述2024年声誉评级... | 详细描述2023年声誉评级... |
```

### S1.3 Mission & Vision (严格N/A策略)
```markdown
| Field | Value |
| :---- | :---- |
| Mission Statement | N/A |  # 年报无明确披露时必须填N/A
| Vision Statement | N/A |   # 严禁自行提炼或推测
| Core Values | N/A |        # 只有明确披露时才填写原文
```

### S3.1 Profitability Analysis (单列表格)
```markdown
| Perspective | Answer |
| :---- | :---- |
| Revenue & Direct-Cost Dynamics | 详细分析收入和成本动态... |
| Operating Efficiency | 详细分析运营效率... |
| External & One-Off Impact | 详细分析外部影响... |
```

### S3.2 Financial Performance Summary (双年份对比表格)
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Comprehensive financial health | 2024年财务健康状况... | 2023年财务健康状况... |
| Profitability and earnings quality | 2024年盈利能力... | 2023年盈利能力... |
| Operational efficiency | 2024年运营效率... | 2023年运营效率... |
| Financial risk identification | 2024年风险识别... | 2023年风险识别... |
| Future financial performance | 2024年未来展望... | 2023年未来展望... |
```

### S5.2 Internal Controls (必须6项)
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Risk assessment procedures | 风险评估程序... | 风险评估程序... |
| Control activities | 控制活动... | 控制活动... |
| Monitoring mechanisms | 监督机制... | 监督机制... |
| Identified material weaknesses | 重大缺陷... | 重大缺陷... |
| Improvements | 改进措施... | 改进措施... |
| Effectiveness | 有效性... | 有效性... |
```

---

## 🔍 质量检查清单

### Section 2 财务数据检查
- [ ] 所有财务表格包含Multiplier和Currency列
- [ ] S2.4使用百分比格式，保留2位小数
- [ ] 财务指标计算公式正确
- [ ] 数据口径一致（合并净利润+合并权益）
- [ ] Multiplier判断合理（Thousands/Millions）

### 格式规范检查
- [ ] 表格使用标准markdown格式
- [ ] 中文公司使用中文表头，英文公司使用"2024 Report"
- [ ] N/A使用规范，无自行推测内容
- [ ] 数值格式正确（千分位逗号、负数处理）

### 内容完整性检查
- [ ] S1.2四个维度双年份对比
- [ ] S3.2五个维度双年份对比
- [ ] S5.2六项内控要素完整
- [ ] 所有必填字段无遗漏

---

## 🚀 使用流程

### Step 1: 地区识别
```python
def identify_region(company_name, currency, language):
    if currency == "CNY" and language == "中文":
        return "中国A股"
    elif currency == "USD" and language == "英文":
        return "美国"
    elif currency == "RM" and language == "英文":
        return "新加坡/马来西亚"
    elif currency == "GBP" and language == "英文":
        return "英国"
```

### Step 2: 数据提取
```python
def extract_financial_data(annual_report, region):
    # 根据地区差异化提取数据
    if region == "中国A股":
        net_profit = extract_cn_net_profit(annual_report)
        equity = extract_cn_equity(annual_report)
    elif region == "美国":
        net_profit = extract_us_net_profit(annual_report)
        equity = extract_us_equity(annual_report)
    # ... 其他地区
```

### Step 3: 指标计算
```python
def calculate_metrics(financial_data):
    # 严格按照公式计算12项指标
    metrics = {}
    metrics['Gross_Margin'] = calculate_gross_margin(financial_data)
    metrics['Operating_Margin'] = calculate_operating_margin(financial_data)
    # ... 其他指标
    return metrics
```

### Step 4: 报告生成
```python
def generate_report(financial_data, metrics, region):
    # 按照标准格式生成6个Section
    report = {}
    report['Section1'] = generate_section1(financial_data, region)
    report['Section2'] = generate_section2(financial_data, metrics, region)
    # ... 其他Section
    return report
```

---

## 📈 预期表现

| 指标 | Pipeline 3.0 表现 |
|------|------------------|
| **目标得分** | **230+/240分**（96%+）|
| **处理速度** | 10-15分钟/案例 |
| **支持地区** | 中国、美国、新加坡、英国等 |
| **支持会计准则** | 中国GAAP、US GAAP、IFRS、MFRS |
| **质量等级** | 卓越级（DeepEval 0.9+）|

---

## 🎯 成功案例

### 验证集实战结果
1. **val001 IHH Healthcare (新加坡)**: MFRS处理，RM Million
2. **val029 五粮液 (中国)**: 中国GAAP处理，CNY Thousands  
3. **val043 Exxon Mobil (美国)**: US GAAP处理，USD Millions

**关键成功因素**:
- ✅ 地区差异化处理
- ✅ 多会计准则适配
- ✅ 严格口径统一
- ✅ 完整财务指标计算

---

**财小析 Pipeline 3.0 - 智慧整合，精准高效！** 🚀
