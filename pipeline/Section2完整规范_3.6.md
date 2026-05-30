# Section 2: Financial Performance - 完整数据提取与计算规范

> **版本**: 3.6 | **优先级**: 🔴 最高（占总分48.75%） | **零容忍政策**

---

## 🎯 核心原则：100%真实、100%准确、100%可验证

**Section 2是得分的关键战场，失分率77%→必须降至15%以下！**

### 三个"100%" + 数据来源铁律

**1. 100%从年报原文提取**
```yaml
强制要求:
  - 所有数据必须来自提供的两年年报
  - 严禁使用任何外部数据源
  - 严禁编造、估算、凑整数据
  - 找不到数据时填N/A，不得推测
  
违规示例:
  ❌ 从网络查询公司成立日期
  ❌ 根据常识推测财务数据
  ❌ 使用上一年数据估算今年数据
  ❌ 从其他报告复制数据
```

**2. 100%计算准确** - 每个公式都有验证机制

**3. 100%格式规范** - 严格按照sample标准

---

## 📋 S2.1: Income Statement（利润表）

### 数据提取标准

#### 必填字段（12项）

| 字段 | 英文名称 | 提取位置 | 验证规则 | 常见错误 |
|------|---------|---------|---------|---------|
| 营业收入 | Revenue | Consolidated Income Statement第1行 | >0, 最大值 | 与Total Revenue混淆 |
| 营业成本 | Cost of Goods Sold | COGS或Cost of Sales | ≤Revenue | 服务业可能=N/A |
| 毛利润 | Gross Profit | Revenue - COGS | =Revenue-COGS | 计算vs直接提取 |
| 营业费用 | Operating Expense | Operating Expenses合计 | >0 | 可能包含多项 |
| 营业利润 | Operating Income | Operating Profit/EBIT | =GP-OpEx | 口径问题 |
| 净利润 | Net Profit | Net Income/Profit for the year/Profit attributable to shareholders | **地区差异** | ⚠️英国归母,澳洲/中国合并 |
| 税前利润 | Income before income taxes | Profit Before Tax | >Net Profit | - |
| 所得税费用 | Income tax expense(benefit) | Tax Expense/Benefit | 可正可负 | 负数=退税 |
| 利息费用 | Interest Expense | Finance Costs/Interest | 通常>0 | 利息收入在其他地方 |

#### 关键验证公式

```python
# 必须满足的等式
✅ Gross Profit = Revenue - COGS
✅ Operating Income = Gross Profit - Operating Expense (简化版)
✅ Net Profit = Income Before Tax - Tax Expense
✅ Income Before Tax ≥ Net Profit (税前≥税后)

# 合理性验证
✅ 0 < COGS < Revenue (制造业/零售业)
✅ COGS = N/A (纯服务业，参考Sample002)
✅ Gross Margin一般在10%-80%之间
✅ Net Profit Margin一般在-20%到50%之间
```

#### 特殊处理规则

**规则1：服务业COGS处理**
```yaml
适用行业: 咨询、软件、航空、金融服务
Sample参考: Sample002 (Chemring), Sample005 (Singapore Airlines)
处理方式:
  COGS: N/A
  Gross Profit: N/A
  Operating Expense: 填写Total Operating Costs
  Operating Income: Revenue - Operating Expense
```

**规则2：负数表示**
```yaml
Sample001-003: 使用负号 (如-187)
Sample004-008: 使用括号 (如(187))
遵循原则: 100%按该地区sample格式
```

**规则3：净利润口径（地区差异！）** ⚠️⚠️⚠️
```yaml
⚠️ 严禁跨地区通用！每个地区规则不同！

英国地区（sample002）:
  口径: 归母净利润
  英文名: Profit attributable to shareholders/owners
  示例: Chemring 39.5M
  
澳大利亚地区（sample006）:
  口径: 合并净利润
  英文名: Total profit for the year
  计算: 归母 + 少数股东损益
  示例: CSL 2,714M = 2,642M + 72M
  
中国地区（sample003）:
  口径: 合并净利润
  中文名: 合并利润表"净利润"行
  计算: 归母 + 少数股东损益
  示例: 宁德时代 54,006,794千 = 50,745,000千 + 3,261,794千

执行原则:
  → 处理英国公司 → 查英国地区规范 → 用归母
  → 处理澳洲公司 → 查澳洲地区规范 → 用合并
  → 处理中国公司 → 查中国地区规范 → 用合并
  
❌ 禁止: 尝试总结通用规律
✅ 正确: 按地区查规范，直接执行
```

### Multiplier判断（关键！）

#### 判断流程

```
Step 1: 查看年报财务报表标题或注释
  ├─ "Amounts in thousands" → Thousands
  ├─ "In millions of dollars" → Millions  
  ├─ "In billions of Rupiah" → Billions
  └─ 无明确说明 → 看数字规模

Step 2: 交叉验证Revenue规模
  ├─ 大型企业Revenue应该在数十亿到数千亿货币单位
  ├─ 如果Revenue只有几千，可能是Millions
  └─ 如果Revenue是1万+，可能是Thousands或Millions

Step 3: 参考同地区Sample
  ├─ Sample001(美国): Millions
  ├─ Sample002(英国): Millions
  ├─ Sample003(中国): Thousands (⚠️注意！)
  ├─ Sample004(香港): Millions
  ├─ Sample005(新加坡): Millions
  ├─ Sample006(澳大利亚): Millions
  ├─ Sample007(马来西亚): Thousands (⚠️注意！)
  └─ Sample008(印尼): Billions (⚠️⚠️注意！)

Step 4: 最终确认
  记录年报原文说明作为证据
```

#### 特殊案例

**印尼公司（Sample008）**：
```yaml
Garudafood 2024:
  年报标注: "Disajikan dalam jutaan Rupiah" (以百万印尼盾列示)
  Revenue原文: Rp 12,235,370 (juta)
  翻译: 12,235,370 million IDR = 12.235 billion IDR
  
  正确填法:
    Revenue: 12,235.37
    Multiplier: Billions
    Currency: IDR
  
  错误填法:
    Revenue: 12,235,370 + Multiplier: Millions (多了1000倍)
```

**中国公司（Sample003）**：
```yaml
五粮液2024:
  年报标注: "单位：千元"
  Revenue原文: 89,175,178 千元
  
  正确填法:
    Revenue: 89,175,178
    Multiplier: Thousands
    Currency: CNY
  
  错误填法:
    Revenue: 89,175 + Multiplier: Millions (会丢失精度)
```

---

## 📋 S2.2: Balance Sheet（资产负债表）

### 数据提取标准

#### 必填字段（12项）

| 字段 | 提取位置 | 验证公式 | 特别注意 |
|------|---------|---------|---------|
| Total Assets | 资产总计 | =CA+NCA | 最重要的平衡项 |
| Current Assets | 流动资产合计 | >0 | - |
| Non-Current Assets | 非流动资产合计 | >0 | - |
| Total Liabilities | 负债总计 | =CL+NCL | - |
| Current Liabilities | 流动负债合计 | >0 | - |
| Non-Current Liabilities | 非流动负债合计 | ≥0 | - |
| Shareholders' Equity | 所有者权益合计 | **含少数股东权益** | ⚠️合并口径 |
| Retained Earnings | 未分配利润/留存收益 | - | 可能为负 |
| Total Equity and Liabilities | 负债和权益总计 | =TL+SE | **必须=TA** |
| Inventories | 存货 | ≤CA | - |
| Prepaid Expenses | 预付款项 | ≤CA | 可能=N/A |

#### 核心验证公式

```python
# 绝对必须满足（会计恒等式）
✅ Total Assets = Total Equity and Liabilities
✅ Total Assets = Total Liabilities + Shareholders' Equity
✅ Current Assets + Non-Current Assets = Total Assets
✅ Current Liabilities + Non-Current Liabilities = Total Liabilities

# 如果不平衡，说明数据提取错误！
```

#### 关键注意事项

**注意1：Shareholders' Equity必须是合并口径**
```yaml
正确名称:
  - Total Equity (包括minority interest)
  - Shareholders' Equity (IFRS合并)
  - 所有者权益合计 (含少数股东权益)

错误名称（禁用）:
  - Equity attributable to owners
  - 归属于母公司所有者权益合计

验证方法:
  SE(合并) = SE(归母) + Minority Interest
```

**注意2：负债的正负号**
```yaml
Sample001-003: 正数表示 (如22,750)
Sample004-008: 部分用括号 (如(335.8))

规则: 按sample格式，但数值含义是"欠款金额"
```

---

## 📋 S2.3: Cash Flow Statement（现金流量表）

### 数据提取标准

#### 必填字段（5项）

| 字段 | 提取位置 | 验证规则 |
|------|---------|---------|
| Net Cash Flow from Operations | 经营活动现金流量净额 | 通常>0 |
| Net Cash Flow from Investing | 投资活动现金流量净额 | 通常<0 |
| Net Cash Flow from Financing | 筹资活动现金流量净额 | 可正可负 |
| Net Increase/Decrease in Cash | 现金及现金等价物净增加额 | =Operating+Investing+Financing |
| Dividends | 支付的股利 | ≤Net Profit (通常) |

#### 验证公式

```python
# 近似关系（考虑汇率影响等）
Net Increase in Cash ≈ OCF + ICF + FCF

# 如果差异>5%，需要检查：
# 1. 是否有汇率影响
# 2. 是否有其他调整项
# 3. 数据提取是否正确
```

---

## 📋 S2.4: Key Financial Metrics（关键财务指标）

### 计算公式与验证标准

#### 完整公式表（12项）

| 指标 | 公式 | 合理范围 | 验证要点 |
|------|------|---------|---------|
| **Gross Margin** | (Rev-COGS)/Rev×100% | 10%-80% | 服务业可能N/A |
| **Operating Margin** | OpIncome/Rev×100% | -10%-60% | 通常>0 |
| **Net Profit Margin** | NetProfit/Rev×100% | -20%-50% | 可为负 |
| **Current Ratio** | CA/CL×100% | 80%-500% | <100%需关注 |
| **Quick Ratio** | (CA-Inv-Prepaid)/CL×100% | 50%-300% | - |
| **Debt-to-Equity** | TL/SE×100% | 20%-200% | 高杠杆>200% |
| **Interest Coverage** | OpIncome/IntExp×100% | **100%-50,000%** | ⚠️关键 |
| **Asset Turnover** | Rev/平均TA×100% | 30%-200% | 2022=N/A |
| **ROE** | NetProfit/平均SE×100% | -10%-50% | 2022=N/A |
| **ROA** | NetProfit/平均TA×100% | -5%-30% | 2022=N/A |
| **Effective Tax Rate** | TaxExp/IncBeforeTax×100% | 0%-40% | 可为负 |
| **Dividend Payout Ratio** | Div/NetProfit×100% | 0%-100% | >100%需说明 |

#### 重点：Interest Coverage计算

**这是最容易出错的指标！**

```python
# 正确计算
Interest Coverage = (Operating Income / Interest Expense) × 100%

# 示例：五粮液2024
Operating Income = 44,200,076 千元
Interest Expense = 40,437 千元
Interest Coverage = 44,200,076 / 40,437 × 100% = 109,306.02%

# ✅ 正确输出：109,306.02%
# ❌ 错误输出：109,306,022% (多乘了1000)
# ❌ 错误输出：109,306.02 (忘记%)
# ❌ 错误输出：1093.06% (计算错误)

# 验证规则
if Interest Coverage > 50,000%:
    警告("Interest Coverage异常高，请检查：")
    检查1: Interest Expense是否太小（如<revenue的0.1%）
    检查2: 是否误用了其他利息数据
    检查3: 计算公式是否正确
    
    # 但如果公司确实利息费用极低，这是正常的！
    # 如五粮液无银行借款，利息费用仅4千万，所以覆盖倍数极高
```

#### 平均值计算（2023和2024）

```python
# 2024年指标
平均总资产_2024 = (Total_Assets_2024 + Total_Assets_2023) / 2
平均股东权益_2024 = (SE_2024 + SE_2023) / 2

Asset_Turnover_2024 = Revenue_2024 / 平均总资产_2024 × 100%
ROE_2024 = Net_Profit_2024 / 平均股东权益_2024 × 100%
ROA_2024 = Net_Profit_2024 / 平均总资产_2024 × 100%

# 2023年指标
平均总资产_2023 = (Total_Assets_2023 + Total_Assets_2022) / 2
平均股东权益_2023 = (SE_2023 + SE_2022) / 2

Asset_Turnover_2023 = Revenue_2023 / 平均总资产_2023 × 100%
ROE_2023 = Net_Profit_2023 / 平均股东权益_2023 × 100%
ROA_2023 = Net_Profit_2023 / 平均总资产_2023 × 100%

# 2022年指标
Asset_Turnover_2022 = N/A  # 缺2021年期初数据
ROE_2022 = N/A
ROA_2022 = N/A
```

#### 百分比格式规范

```yaml
标准格式: 24.70%
保留位数: 2位小数
负数: -5.23%
极大值: 109,306.02% (保留2位小数，用逗号分隔千位)

❌ 禁止格式:
  - 2470 (缺少%和小数点)
  - 24.70 (缺少%)
  - 24.7% (少一位小数)
  - 24.70 % (多余空格)
  - 109306.02% (千位无逗号，数字太大时难读)
```

---

## 📋 S2.5: Operating Performance（经营表现）

### 数据提取标准

#### 必填字段（2项）

**1. Revenue by Product/Service**

```yaml
提取位置: 年报 Management Discussion / Notes to Financial Statements
提取内容: 按产品/服务分类的收入明细
格式要求: 按sample格式，列出所有主要产品线

示例（Sample001）:
  "Compute & Networking: $47,405M Graphics: $13,517M Total: $60,922M"

示例（Sample003 - 中文）:
  "2024年分产品营业收入：动力电池系统 253,041,337 千元，储能电池系统 57,290,460 千元..."

注意:
  - 必须包含数字（不能只说"增长"）
  - 必须包含单位（M, 千元, 亿元等）
  - 中文地区用中文描述，英文地区用英文
```

**2. Revenue by Geographic Region**

```yaml
提取位置: 年报分部报告 (Segment Reporting)
提取内容: 按地理区域分类的收入明细
格式要求: 列出主要地区和金额

示例（Sample001）:
  "United States: $26,966M Taiwan: $13,405M China (incl. HK): $10,306M..."

示例（Sample003 - 中文）:
  "2024年分地区营业收入：境内 251,677,045 千元，境外 110,335,509 千元。"
```

#### 语言规则（重要！）

```yaml
英文地区（6个）:
  - 100%英文描述
  - "Revenue by Product: Product A: $1,000M, Product B: $500M"
  
中文地区（中国、香港）:
  - 中文描述 + 数字 + 单位
  - "2024年分产品营业收入：产品A 1,000,000千元，产品B 500,000千元"
  - ⚠️ 注意用"年份+分+产品/地区+营业收入"格式
```

---

## 🔍 质量检查清单（Section 2）

### 检查项（25项）

#### S2.1 Income Statement (7项)
- [ ] Revenue > 0且合理
- [ ] COGS ≤ Revenue（或=N/A for服务业）
- [ ] Gross Profit = Revenue - COGS
- [ ] Net Profit合理（合并口径）
- [ ] Income Before Tax ≥ Net Profit
- [ ] Multiplier和Currency正确
- [ ] 负数格式符合sample

#### S2.2 Balance Sheet (6项)
- [ ] Total Assets = Total Liabilities + Shareholders' Equity
- [ ] Current Assets + Non-Current Assets = Total Assets
- [ ] Shareholders' Equity是合并口径（含少数股东）
- [ ] Inventories ≤ Current Assets
- [ ] 所有数字合理（无异常大/小值）
- [ ] Multiplier和Currency与S2.1一致

#### S2.3 Cash Flow Statement (4项)
- [ ] Operating Cash Flow通常>0
- [ ] Net Increase ≈ Operating + Investing + Financing
- [ ] Dividends ≤ Net Profit（通常）
- [ ] Multiplier和Currency一致

#### S2.4 Key Financial Metrics (6项)
- [ ] 所有12个指标都已计算（除2022年部分N/A）
- [ ] Gross Margin在合理范围（10%-80%）
- [ ] Interest Coverage计算正确（无异常大值）
- [ ] 平均值计算正确（Asset Turnover, ROE, ROA）
- [ ] 百分比格式：2位小数+%符号
- [ ] 2022年Asset Turnover/ROE/ROA = N/A

#### S2.5 Operating Performance (2项)
- [ ] Revenue by Product/Service有具体数字和单位
- [ ] Revenue by Geographic Region有具体数字和单位

---

## 🚨 零容忍错误（立即失败）

1. **数据编造** - 数据未从年报提取
   - 使用外部数据源
   - 根据常识推测数据
   - 估算或凑整数据
   
2. **口径错误** - 未按地区规范选择归母/合并数据

3. **计算错误** - 公式错误或验证不通过

4. **Multiplier错误** - 单位判断错误导致数值差1000倍

5. **Balance Sheet不平衡** - 会计恒等式不成立

**发现以上任何一项，必须立即返工重做！**

---

## 📋 数据来源唯一性原则 ⭐⭐⭐

### 强制规定

**数据来源范围**：
```yaml
✅ 允许:
  - 提供的2024年年报MD文件
  - 提供的2023年年报MD文件
  - 以上两份文件中的所有内容
  
❌ 严禁:
  - 互联网搜索
  - 公司官网
  - 第三方数据库
  - 其他年份年报
  - 任何外部信息源
  - 基于常识的推测
  - 基于历史数据的估算
```

**执行标准**：
- 每个数据点都必须能追溯到年报原文
- 找不到数据时填N/A，绝不推测
- 宁可保守（N/A），不可编造

---

## 📖 实战案例

### 案例1：五粮液（Sample003标准）

**完整提取流程**：
```
Step 1: 定位利润表
  - 年报第XX页："合并利润表"
  - 确认单位："单位：千元"
  
Step 2: 逐行提取
  Revenue: 89,175,178 千元 (一、营业总收入)
  COGS: 20,461,423 千元 (二、营业总成本-其他成本)
  ...
  Net Profit: 33,193,460 千元 (五、净利润)
  
Step 3: 交叉验证
  Gross Profit = 89,175,178 - 20,461,423 = 68,713,755 ✅
  Gross Margin = 68,713,755/89,175,178 = 77.05% ✅ 合理
  
Step 4: 填写表格
  | Revenue | 89,175,178 | 83,272,067 | 73,968,641 | Thousands | CNY |
```

### 案例2：Garudafood（Sample008标准）

**Multiplier判断**：
```
Step 1: 查看年报财务报表
  标题："Laporan Posisi Keuangan Konsolidasian"
  注释："Disajikan dalam jutaan Rupiah, kecuali dinyatakan lain"
  翻译："以百万印尼盾列示，除非另有说明"
  
Step 2: 识别Revenue
  原文：Rp 12.235.370 (juta) = 12,235,370 million IDR
  
Step 3: 转换为合适单位
  12,235,370 million = 12,235.37 billion
  或保持：12,235,370 (Millions)
  
Step 4: 参考Sample008
  Sample使用：Billions
  
Step 5: 最终确定
  Revenue: 12,235.37
  Multiplier: Billions
  Currency: IDR
```

---

*Section 2完整规范 v3.6 - 数据质量优先*
