# 中国地区完整规范 - Sample003 (宁德时代)

> **适用地区**: 中国 (China)
> **Sample编号**: Sample003
> **Sample公司**: 宁德时代新能源科技股份有限公司
> **验证集案例**: val029 (五粮液)

---

## 📋 地区基本信息

```yaml
地区: 中国
语言: 简体中文（内容层） + 英文（框架层）
货币: CNY (人民币)
Multiplier: Thousands (千元) 或 Ones (元)
会计准则: 中国企业会计准则 (CAS)
年报格式: 年度报告
```

---

## 🎯 语言规则（⚠️ 重要！中国地区特殊）

### 双层语言规则

**框架层（永远英文）**：
```markdown
✅ Section标题：# Section 1: Company Overview
✅ 子Section标题：## S1.1: Basic Information
✅ 表格基础列标题：Field, Multiplier, Currency
✅ 财务科目名称：Revenue, Net Profit, Total Assets
```

**内容层（简体中文）**：
```markdown
✅ 公司名称：宁德时代新能源科技股份有限公司
✅ 分析文字：公司收入在2022-2024年间保持稳健增长...
✅ S2.5描述：2024年分产品营业收入：动力电池系统...
✅ 特殊列标题：宁德时代新能源科技股份有限公司2024年年度报告
```

### ❌ 严禁行为
```markdown
❌ Section标题翻译成中文：第一部分：公司概述
❌ 财务科目翻译成中文：营业收入（应为Revenue）
❌ 基础列标题翻译：字段（应为Field）
```

---

## 📊 Section 1: Company Overview

### S1.1: Basic Information

**表格格式**：
```markdown
| Field | Value |
| :---- | :---- |
| Company Name | 宁德时代新能源科技股份有限公司 |
| Establishment Date | 2011年 |
| Headquarters Location | 中国福建省宁德市 |
```

**注意**：
- Field和Value是英文 ✅
- 公司名称等内容用简体中文 ✅

---
**⚠️ 评分对齐补充（v3.6）**
- 公司全称须与年报封面一致（含“股份有限公司/控股有限公司”等），与数据集期望字符串一致优先。
- 总部地址建议规范为“国家+省/直辖市+城市”（示例：`中国福建省宁德市`）。
- 成立日期无明确披露时，统一填 `N/A`，禁止推测。

---

### S1.2: Core Competencies

**⚠️ 标题格式要求**：`## S1.2 : Core Competencies`（冒号前有空格）

**表格格式**：
```markdown
| Perspective | 宁德时代新能源科技股份有限公司2024年年度报告 | 宁德时代新能源科技股份有限公司2023年年度报告 |
| :---- | :---- | :---- |
| Innovation Advantages | [简体中文分析内容，200-300字] | [简体中文分析内容] |
| Product Advantages | [简体中文分析内容] | [简体中文分析内容] |
| Brand Recognition | [简体中文分析内容] | [简体中文分析内容] |
| Reputation Ratings | [简体中文分析内容] | [简体中文分析内容] |
```

**⚠️ 中国地区特殊要求**：
- 列标题格式：**公司全称 + 2024年年度报告**
- Perspective是英文 ✅
- 分析内容用简体中文 ✅

**Sample003示例**：
```markdown
| Perspective | 宁德时代新能源科技股份有限公司2024年年度报告 | 宁德时代新能源科技股份有限公司2023年年度报告 |
```

---

### S1.3: Mission & Vision

**⚠️ 标题格式要求**：`## S1.3 : Mission & Vision`（冒号前有空格）

**表格格式**：
```markdown
| Field | Answer |
| :---- | :---- |
| Mission Statement | 为人类新能源事业做出卓越贡献 |
| Vision Statement | 致力于成为全球领先的绿色能源解决方案服务商 |
| Core Values | 诚信、敬业、创新、共赢 |
```

**⚠️ 中国地区特殊要求**：列标题为 **Field | Answer**

---
**⚠️ 评分对齐补充（v3.6）**
- 年报未以正式标题披露“使命/愿景/核心价值观”等条目时，`Mission Statement / Vision Statement / Core Values` 三项一律填 `N/A`。
- 禁止将品牌口号或广告语替代为使命/愿景。

---

## 📊 Section 2: Financial Performance

### S2.1: Income Statement

**表格格式**：
```markdown
| Field | 2024 | 2023 | 2022 | Multiplier | Currency |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Revenue | 362,012,554 | 400,909,067 | 329,084,730 | Thousands | CNY |
| Cost of Goods Sold | 276,934,717 | 327,064,920 | 254,395,089 | Thousands | CNY |
| Gross Profit | 85,077,837 | 73,844,147 | 74,689,641 | Thousands | CNY |
| Operating Expense | 32,085,906 | 30,049,169 | 24,777,636 | Thousands | CNY |
| Operating income | 52,991,931 | 43,794,978 | 49,912,005 | Thousands | CNY |
| Net Profit | 54,006,794 | 44,129,486 | 33,126,813 | Thousands | CNY |
| Income before income taxes | 57,172,654 | 46,653,077 | 37,072,048 | Thousands | CNY |
| Income tax expense(benefit) | 3,165,860 | 2,523,591 | 3,945,235 | Thousands | CNY |
| Interest Expense | 3,321,193 | 2,011,549 | 1,344,925 | Thousands | CNY |
```

**⚠️ 中国地区关键特征**：

**1. Multiplier判断**：
```yaml
大型企业（收入>100亿）:
  年报标注：单位：千元
  Multiplier: Thousands ✅
  
特大型企业（收入>1000亿）:
  年报标注：单位：元
  Multiplier: Ones
  
中小企业:
  可能用：万元 (需转换为Thousands)
```

**Sample003使用**：Thousands (千元)

**2. 中国会计准则科目名称（框架英文）**：
```markdown
✅ Revenue (不要翻译成"营业收入")
✅ Cost of Goods Sold (不要翻译成"营业成本")
✅ Net Profit (不要翻译成"净利润")
```

**3. 数据口径 ⭐ 重要**：
```yaml
净利润口径: 合并净利润（含少数股东）
  - 对应字段: 合并利润表中的"净利润"行
  - 计算: 归属于母公司所有者的净利润 + 少数股东损益
  - 验证: sample003 宁德时代: 
      54,006,794千 = 50,745,000千(归母) + 3,261,794千(少数股东)
  - 原因: 这是中国地区标准，直接执行

❌ 错误做法: 只用"归属于上市公司股东的净利润"
✅ 正确做法: 使用合并利润表"净利润"行（含少数股东）
```

**4. 数值格式**：
```markdown
正数：362,012,554
负数：-3,165,860 或 (3,165,860)
保留原始精度，千位用逗号
```

---

### S2.2: Balance Sheet

**表格格式**：
```markdown
| Field | 2024 | 2023 | 2022 | Multiplier | Currency |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Total Assets | 831,693,524 | 710,380,878 | 574,069,821 | Thousands | CNY |
| Current Assets | 520,669,968 | 432,085,653 | 338,476,945 | Thousands | CNY |
| Non-Current Assets | 311,023,556 | 278,295,225 | 235,592,876 | Thousands | CNY |
| Total Liabilities | 433,726,698 | 347,879,524 | 270,892,936 | Thousands | CNY |
| Current Liabilities | 329,617,050 | 261,023,851 | 202,584,297 | Thousands | CNY |
| Non-Current Liabilities | 104,109,648 | 86,855,673 | 68,308,639 | Thousands | CNY |
| Shareholders' Equity | 397,966,826 | 362,501,354 | 303,176,885 | Thousands | CNY |
| Retained Earnings | 141,595,669 | 118,476,050 | 89,655,383 | Thousands | CNY |
| Total Equity and Liabilities | 831,693,524 | 710,380,878 | 574,069,821 | Thousands | CNY |
| Inventories | 123,567,890 | 98,234,567 | 78,901,234 | Thousands | CNY |
| Prepaid Expenses | 5,432,109 | 4,567,890 | 3,456,789 | Thousands | CNY |
```

**中国会计准则科目（框架英文）**：
```markdown
✅ Shareholders' Equity (不翻译成"所有者权益")
✅ Total Assets (不翻译成"资产总计")
✅ Retained Earnings (不翻译成"未分配利润")
```

**数据口径**：
```yaml
Shareholders' Equity: 必须使用"所有者权益合计"
= 包含少数股东权益 ✅

错误做法：只用"归属于母公司所有者权益" ❌
```

---

### S2.3: Cash Flow Statement

**表格格式**：标准格式，注意Multiplier: Thousands, Currency: CNY

---

### S2.4: Key Financial Metrics

**表格格式**：
```markdown
|  | 2024 | 2023 | 2022 |
| :---- | :---- | :---- | :---- |
| Gross Margin | 23.50% | 18.42% | 22.70% |
| Operating Margin | 14.64% | 10.92% | 15.16% |
| Net Profit Margin | 14.92% | 11.01% | 10.06% |
| Current Ratio | 157.97% | 165.51% | 167.08% |
| Quick Ratio | 120.45% | 128.02% | 128.15% |
| Debt-to-Equity | 108.98% | 95.97% | 89.35% |
| Interest Coverage | 1,595.57% | 2,177.30% | 3,711.65% |
| Asset Turnover | 47.01% | 55.84% | N/A |
| Return on Equity | 14.14% | 13.23% | N/A |
| Return on Assets | 6.97% | 6.47% | N/A |
| Effective Tax Rate | 5.54% | 5.41% | 10.64% |
| Dividend Payout Ratio | 25.89% | 23.45% | 18.90% |
```

**公式必检（不得偏离比赛规则）**
- Quick Ratio = (Current Assets − Inventories − Prepaid)/Current Liabilities × 100%
- Interest Coverage = Operating income/Interest expense × 100%
- ROE/ROA/Asset Turnover 使用平均口径；若缺少期初（如2022）→ N/A
- Dividend Payout Ratio = Dividends/Net Profit × 100%
- 所有百分比统一两位小数输出

**注意**：第一列为空，格式与其他地区相同

---

### S2.5: Operating Performance

**表格格式**：
```markdown
| Field | 2024 | 2023 | 2022 |
| :---- | :---- | :---- | :---- |
| Revenue by Product/Service | 2024年分产品营业收入（千元）：动力电池系统 253,041,337，储能电池系统 57,290,460，电池材料及回收 41,234,567，其他 10,446,190。 | 2023年分产品营业收入（千元）：动力电池系统... | 2022年... |
| Revenue by Geographic Region | 2024年分地区营业收入（千元）：境内 251,677,045，境外 110,335,509。 | 2023年... | 2022年... |
```

**⚠️ 中国地区特殊要求**：
- 使用简体中文描述 ✅
- 格式：**年份 + 分产品/地区 + 营业收入**
- 必须包含数字和单位（千元）
- Field和列标题用英文，内容用中文

**Sample003示例**：
```
2024年分产品营业收入（千元）：动力电池系统 253,041,337，储能电池系统 57,290,460...
```

---

## 📊 Section 3: Business Analysis

### S3.1: Profitability Analysis

**表格格式**：
```markdown
| Perspective | Answer |
| :---- | :---- |
| Revenue & Direct-Cost Dynamics (Revenue Growth ; Gross Margin; Revenue by Product/Service; Revenue by Geographic Region) | [简体中文分析] |
| Operating Efficiency (Operating Margin) | [简体中文分析] |
| External & One-Off Impact (Effective Tax Rate, Non-Recurring Items) | [简体中文分析] |
```

**⚠️ 中国地区特殊要求**：
- 列标题：**Perspective | Answer** ✅
- 行标题带括号说明（与澳洲相同）✅
- **内容必须用简体中文**

---

**📏 S3.1 内容长度与密度标准（v3.6新增 - 基于Sample003逆向分析）**

| 维度 | 标准长度 | 数据密度 | 必须包含 |
|------|---------|---------|---------|
| Revenue & Direct-Cost Dynamics | 100-150词 | 10-15个数据点 | 收入增长率、毛利率、主要产品、地区分布（**三年对比**） |
| Operating Efficiency | 100-150词 | 8-10个数据点 | 营业利润率、营业利润、费用控制 |
| External & One-Off Impact | 90-120词 | 8-10个数据点 | 有效税率、所得税费用、非经常性损益 |

**与澳洲对比（关键差异）**：
- **长度**：比澳洲多30词（澳洲80-120词，中国100-150词）
- **数据密度**：比澳洲多4-7个数据点（澳洲6-8个，中国10-15个）
- **三年对比**：中国强调2022-2023-2024完整对比 ⭐

**提炼方法（中文特色）**：
1. **三年完整对比**：必须包含2022-2023-2024三年数据链
2. **多源整合**：从利润表+附注+管理层讨论整合
3. **计算增长率**：(本期-上期)/上期 × 100%
4. **归纳总结**：用总括语（"公司收入在2022-2023年间实现强劲增长..."）
5. **深度分析**：用"表明"、"显示"、"反映"连接判断

**分析用词库（简体中文）**：
- 正面：显著、持续、稳健、强劲、良好、健康、大幅、明显、卓越
- 负面：下降、承压、回落、有所调整、有待提升、压力
- 中性：相对稳定、有所改善、适度、进一步、逐渐
- 因果：表明、显示、反映、体现、说明
- 转折：尽管...但...、然而、同时、此外

**句式结构（中文特色）**：
- "从...提升至..."（变化描述）
- "表明..."、"显示..."（因果分析）
- "尽管...但..."（转折对比）
- "...方面"（维度切换）
- "整体而言"（总结判断）

---

**⚠️ 评分对齐补充（v3.6）**
```markdown
| Perspective | Answer |
| :---- | :---- |
| Revenue & Direct-Cost Dynamics (Revenue Growth ; Gross Margin; Revenue by Product/Service; Revenue by Geographic Region) | ... |
| Operating Efficiency (Operating Margin) | ... |
| External & One-Off Impact (Effective Tax Rate, Non-Recurring Items) | ... |
```
— 三行标题需逐字匹配（含括号与分号空格）。

---

### S3.2: Financial Performance Summary

**表格格式**：
```markdown
| Perspective | 2024年年度报告 | 2023年年度报告 |
| :---- | :---- | :---- |
| Comprehensive financial health | [简体中文分析] | [简体中文分析] |
| Profitability and earnings quality | [简体中文分析] | [简体中文分析] |
| Operational efficiency | [简体中文分析] | [简体中文分析] |
| Financial risk identification and early warning | [简体中文分析] | [简体中文分析] |
| Future financial performance projection | [简体中文分析] | [简体中文分析] |
```

**⚠️ 中国地区特殊要求**：
- 列标题格式：**2024年年度报告 | 2023年年度报告** ✅
- 不需要公司全称（与S1.2不同）
- Perspective是英文，内容用简体中文

---

**📏 S3.2 内容长度与密度标准（v3.6新增 - 基于Sample003逆向分析）**

| 维度 | 单列长度 | 数据密度 | 组织结构 |
|------|---------|---------|---------|
| Comprehensive financial health | 120-155词 | 10-12个指标 | 总资产→股东权益→资产负债率→流动比率 |
| Profitability and earnings quality | 120-155词 | 10-12个指标 | 净利润→净利润率→毛利率→质量判断 |
| Operational efficiency | 115-140词 | 10-11个指标 | 营业利润率→营业利润→费用控制→运营杠杆 |
| Financial risk | 145-155词 | 12个指标 | 有效税率→分红比例→资产周转率→风险判断 |
| Future projection | 150-155词 | 前瞻性判断 | 基于趋势→盈利能力→增长动力→风险平衡 |

**注意**：每个维度有2024+2023两列，总计240-310词/维度

**与澳洲对比（关键差异）**：
- **单列长度**：比澳洲长（澳洲120-180词，中国120-155词接近上限）
- **数据密度**：略高于澳洲（澳洲8-12个，中国10-12个）
- **双列呼应**：中国更强调两列间的趋势延续或变化说明

**整合逻辑（中文特色）**：
1. 开篇总括（"公司财务状况整体稳健..."）
2. 分项数据呈现（总资产、权益、比率等）
3. 三年趋势分析（2022→2023→2024）
4. 因果判断（"表明"、"反映"、"显示"）
5. 平衡评价（"尽管...但..."、"整体而言"）

---

**⚠️ 评分对齐补充（v3.6）**
- 行标题`Financial risk identification and early warning`须逐字匹配。
- 列标题必须完全为“2024年年度报告 | 2023年年度报告”。

**内容模板与评分对齐（v3.6）—安全锚点策略（来源与留痕）**
- 优先使用本文件 `S2.1–S2.5` 的数字；若 S2 未覆盖，允许使用“同一案例两年年报的原始披露数据”（同公司、同年度范围、同口径）。
- 使用年报原始披露数据时：
  - 必须在《样本取数路径_3.6.md》中记录证据留痕（文件名/页码或章节/表名）。
  - 单位/倍率/币种按年报原文，且与本文件整体口径一致（如 Thousands/CNY 或 Ones/CNY）。
- 表达方式：优先“并列对照”（如“总资产188,252,219千元 vs 165,432,982千元”）；YoY/pp 仅在两种情形下使用：① 年报明确披露该YoY/pp；② 由本文件S2数字可直接计算。否则避免自行推导。
- 每个单元格建议≤3个锚点（金额/比率/pp变化），确保简洁且可追溯。
- 比率口径与 `S2.4` 保持一致（百分比，两位小数）。
- 风险行（`Financial risk identification and early warning`）推荐锚点：`Debt-to-Equity`、`Interest Coverage`、`Current Ratio`、`Dividend Payout Ratio`、`Net Cash Flow from Operations/Inventories`（来源 S2 或年报披露）。

---

### S3.3: Business Competitiveness

**表格格式**：
```markdown
| Field | 宁德时代新能源科技股份有限公司2024年年度报告 | 宁德时代新能源科技股份有限公司2023年年度报告 |
| :---- | :---- | :---- |
| Business Model | [简体中文分析] | [简体中文分析] |
| Market Position | [简体中文分析] | [简体中文分析] |
```

**⚠️ 中国地区特殊要求**：
- 列标题格式：**Field | 公司全称+年份+年年度报告** ✅
- 需要公司全称（与S3.2不同）

---

## 📊 Section 4: Risk Factors

### S4.1: Risk Factors

**表格格式**：
```markdown
| Perspective | 宁德时代新能源科技股份有限公司+2024+年年度报告 | 宁德时代新能源科技股份有限公司+2023+年年度报告 |
| :---- | :---- | :---- |
| Market Risks | [简体中文分析] | [简体中文分析] |
| Operational Risks | [简体中文分析] | [简体中文分析] |
| Financial Risks | [简体中文分析] | [简体中文分析] |
| Compliance Risks | [简体中文分析] | [简体中文分析] |
```

**⚠️ 中国地区超级特殊要求**：
- 列标题需要公司全称
- **年份用加号连接**：`公司全称+2024+年年度报告` ✅
- 这是中国地区S4.1的独特标记！

**Sample003实际格式**：
```markdown
| Perspective | 宁德时代新能源科技股份有限公司+2024+年年度报告 | ...
                                              ↑ 加号 ↑
```

---
**⚠️ 评分对齐补充（v3.6）**
- 行标题固定为：`Market Risks`、`Operational Risks`、`Financial Risks`、`Compliance Risks`（逐字匹配）。

---

**📏 S4.1 内容长度与密度标准（v3.6）**

| 维度 | 单列长度 | 内容要求 | 数据来源 |
|------|---------|---------|----------|
| Market Risks | 100-120词 | 宏观经济、市场波动、竞争加剧 | 年报"风险因素"章节 |
| Operational Risks | 100-120词 | 技术开发、供应链、生产运营 | 年报"风险因素"章节 |
| Financial Risks | 120-140词 | 信用、流动性、市场风险（汇率/利率） | 年报"风险因素"章节 |
| Compliance Risks | 100-120词 | 合规、政策法规变化 | 年报"风险因素"章节 |

**Sample003示例 - Market Risks (2024)**：
```markdown
面临宏观经济与市场波动风险，全球宏观经济存在不确定性，若未来出现经济增长放缓
和市场需求下滑，将影响整个新能源以及动力和储能电池行业的发展。同时面临市场竞
争加剧风险，随着全球新能源市场快速发展，国内外企业电池产能快速扩张。
```

**提炼方法**：
- 从年报"第三节 风险因素"或"第四节 管理层讨论与分析"提取
- 保持原文用词的专业性
- 使用"面临...风险"句式
- 说明风险对业务的影响
- 每个风险维度2-3个具体风险点

---

## 📊 Section 5: Corporate Governance

### S5.1: Board Composition

**表格格式**：
```markdown
| Name | Position | Total Income |
| :---- | :---- | :---- |
| 曾毓群 | 董事长 | 3,456,789 |
| 周佳 | 总经理 | 2,345,678 |
```

**注意**：
- Name和Position列用简体中文 ✅
- Total Income用数字
- 表头用英文

---
**⚠️ 评分对齐补充（v3.6）**
- 优先列示三位关键角色：`董事长`、`总经理/首席执行官(CEO)`、`首席财务官/财务总监/财务负责人(CFO)`；其余可不列，以对齐评测口径。
- 金额单位统一以“元”输出：
  - 若年报披露单位为“万元”，输出时×10,000；若为“千元”，输出时×1,000；保留千位分隔符（示例：`3,456,789`）。
  - 若披露为“人民币万元（RMB’10k）”或“人民币千元（RMB’000）”，同上换算到“元”。
- 使用董事薪酬表中的“合计/Total/应付报酬总额”等单一总额，不得估算。

---

### S5.2: Internal Controls

**表格格式**：
```markdown
| Perspective | 2024年年度报告 | 2023年年度报告 |
| :---- | :---- | :---- |
| Risk assessment procedures | [简体中文] | [简体中文] |
| Control activities | [简体中文] | [简体中文] |
| Monitoring mechanisms | [简体中文] | [简体中文] |
| Identified material weaknesses or deficiencies | N/A | N/A |
| Effectiveness | N/A | N/A |
```

**注意**：列标题用简洁格式，不需要公司全称；行标题包含：`Risk assessment procedures`、`Control activities`、`Monitoring mechanisms`、`Identified material weaknesses or deficiencies`、`Improvements`、`Effectiveness`。

---

**📏 S5.1 内容标准（v3.6）**

**Sample003示例**：
```markdown
| Name | Position | Total Income |
| :---- | :---- | :---- |
| 曾毓群 | 董事长、总经理 | 5,743,000 |
| 潘健 | 联席董事长 | 328,000 |
| 李平 | 副董事长 | 538,000 |
| 周佳 | 副董事长 | 3,328,000 |
| 欧阳楚英 | 董事 | 3,096,000 |
| 赵丰刚 | 董事 | 3,313,000 |
```

**提取方法**：
- 数据来源：年报"第八节 董事、监事、高级管理人员和员工情况"→董事薪酬表
- 单位换算：
  - 若年报为"千元"→乘以1,000→输出"元"
  - 若年报为"万元"→乘以10,000→输出"元"
- 保留千位分隔符：`5,743,000`
- 优先列示：董事长、总经理/CEO、财务负责人/CFO
- 其他董事可选列示（sample003列了6位）

---

**📏 S5.2 内容长度与密度标准（v3.6）**

| 维度 | 单列长度 | 内容要求 |
|------|---------|----------|
| Risk assessment procedures | 80-100词 | 风险管理目标、政策、主要风险类型 |
| Control activities | 80-100词 | 内控体系、子公司管理、重点关注领域 |
| Monitoring mechanisms | 70-90词 | 审阅机制、内部审计、专项审计 |
| Identified material weaknesses | 80-100词 | 重大缺陷数量、具体说明（通常为0） |
| Effectiveness | 60-80词 | 董事会认定、审计意见 |

**Sample003示例 - Risk assessment procedures (2024)**：
```markdown
公司从事风险管理的目标是在风险和收益之间取得适当的平衡，制定风险管理政策以辨
别和分析面临的风险，设定适当的风险可接受水平并设计相应的内部控制程序。主要风
险包括信用风险、流动性风险、市场风险。
```

**提炼方法**：
- 数据来源：年报"第十节 财务报告"→内部控制相关章节
- 保持原文表述的专业性
- 简明扼要，不需要过度展开
- 注意：sample003的2024和2023内容基本相同

---

## 📊 Section 6: Future Outlook

### S6.1: Strategic Direction

**⚠️ 中国S6.1超级特殊格式**：列标题有`.pdf`后缀！

**表格格式**：
```markdown
| Perspective | 宁德时代新能源科技股份有限公司 2024 年年度报告.pdf | 宁德时代新能源科技股份有限公司 2023 年年度报告.pdf |
| :---- | :---- | :---- |
| Mergers and Acquisition | [简体中文] | [简体中文] |
| New technologies | [简体中文] | [简体中文] |
| Organisational Restructuring | [简体中文或N/A] | [简体中文或N/A] |

**Sample003实际格式**：
```markdown
| Perspective | 宁德时代新能源科技股份有限公司 2024 年年度报告.pdf | ...
                                                    ↑ 有PDF后缀 ↑
```

**关键点**：
- ✅ 有空格：`公司全称 2024 年年度报告.pdf`
- ✅ 有PDF后缀
- ✅ 这是S6.1独有的格式

---
**⚠️ 评分对齐补充（v3.6）**
- 行标题`Mergers and Acquisition`与`Organisational Restructuring`保持英式拼写与单复数，逐字匹配。

---

### S6.2: Challenges and Uncertainties

**⚠️ 中国S6.2超级特殊格式**：列标题用加号连接（与S4.1相同）！

**表格格式**：
```markdown
| Perspective | 宁德时代新能源科技股份有限公司+2024+年年度报告 | 宁德时代新能源科技股份有限公司+2023+年年度报告 |
| :---- | :---- | :---- |
| Economic challenges such as inflation, recession risks, and shifting consumer behavior that could impact revenue and profitability. | [简体中文] | [简体中文] |
| Competitive pressures from both established industry players and new, disruptive market entrants that the company faces. | [简体中文] | [简体中文] |
```

**Sample003实际格式**：
```markdown
| Perspective | 宁德时代新能源科技股份有限公司+2024+年年度报告 | ...
                                              ↑ 加号 ↑
```

**关键点**：
- ✅ 加号连接：`公司全称+2024+年年度报告`
- ✅ 与S4.1格式相同
- ✅ 无空格、无PDF后缀

**注意**：行标题保持英文，内容用简体中文

---

### S6.3: Innovation and Development Plans

**⚠️ 中国S6.3格式**：正常格式（无PDF、无加号）

**表格格式**：
```markdown
| Perspective | 宁德时代新能源科技股份有限公司 2024 年年度报告 | 宁德时代新能源科技股份有限公司 2023 年年度报告 |
| :---- | :---- | :---- |
| R\&D investments, with a focus on advancing technology, improving products, and creating new solutions to cater to market trends | [简体中文] | [简体中文] |
| New product launches, emphasizing the company's commitment to continuously introducing differentiated products | [简体中文] | [简体中文] |
```

**Sample003实际格式**：
```markdown
| Perspective | 宁德时代新能源科技股份有限公司 2024 年年度报告 | ...
  有空格，无PDF后缀，无加号
```

**关键点**：
- ✅ 有空格：`公司全称 2024 年年度报告`
- ✅ 无PDF后缀（与S6.1不同）
- ✅ 无加号（与S6.2不同）

---

**📏 S6.1 内容长度与密度标准（v3.6）**

| 维度 | 单列长度 | 内容特征 |
|------|---------|----------|
| Mergers and Acquisition | 100-120词 | 未来并购计划（通常"未披露"） |
| New technologies | 120-150词 | 四大创新体系、具体技术和产品 |
| Organisational Restructuring | 100-130词 | 组织架构调整（通常"未披露"） |

**Sample003示例 - New technologies (2024)**：
```markdown
公司将"材料及材料体系创新"、"系统结构创新"、"绿色极限制造创新"和"商业模式创
新"作为四大创新体系，持续加大研发投入，推动高能量密度、高安全性、长寿命等新
一代电池技术开发。重点推进麒麟电池、神行电池、天恒储能系统、巧克力换电、骐骥
换电、滑板底盘等创新产品和解决方案，利用数字化、智能化平台提升研发效率，保持
技术领先。
```

**提炼方法**：
- 数据来源：年报"经营情况讨论与分析"→未来发展战略
- 列举具体技术和产品名称
- 强调创新体系和研发平台
- 使用"持续"、"重点推进"等前瞻性用词

---

**📏 S6.2 内容长度与密度标准（v3.6）**

| 维度 | 单列长度 | 内容重点 |
|------|---------|----------|
| Economic challenges | 120-140词 | 宏观经济、通胀、原材料价格 |
| Competitive pressures | 100-120词 | 行业竞争、技术竞争 |

**Sample003示例 - Economic challenges (2024)**：
```markdown
公司面临全球宏观经济不确定性风险，若未来出现经济增长放缓和市场需求下滑，将影
响整个新能源以及动力和储能电池行业的发展，进而对公司的经营业绩和财务状况产生
不利影响。原材料价格波动风险持续存在，主要原材料受锂、镍、钴等大宗商品价格影
响较大。
```

**提炼方法**：
- 数据来源：年报"风险因素"章节
- 与S4.1内容呼应，但更聚焦于未来挑战
- 说明对revenue和profitability的影响
- 保持客观、专业的表述

---

**📏 S6.3 内容长度与密度标准（v3.6）**

| 维度 | 单列长度 | 内容重点 |
|------|---------|----------|
| R&D investments | 140-160词 | 研发费用、人员、体系、占比 |
| New product launches | 150-180词 | 具体产品名称、技术参数、应用场景 |

**Sample003示例 - R&D investments (2024)**：
```markdown
公司持续加大研发投入，2024年研发费用达186.07亿元，同比增长1.37%。公司拥有六
大研发中心，研发人员超2万人，研发体系涵盖高通量材料集成计算、智能化电芯设计等
平台，推动材料、系统结构、绿色极限制造和商业模式创新。研发投入占营业收入比例
提升至5.14%。公司通过高强度研发投入和智能化平台，保持新产品新技术开发的前瞻性
和领先性，增强产品竞争力，满足市场多元化需求。
```

**Sample003示例 - New product launches (2024)**：
```markdown
公司持续推出创新产品。2024年，乘用车领域发布神行Plus电池（系统能量密度超
200Wh/kg，全球首个兼备1000km续航及4C超充的磷酸铁锂电池）、新一代麒麟高功率电
池（放电功率超1300kW）、骁遥增混电池（纯电续航超400公里且4C超充），商用车领域
推出天行L-超充、天行L-长续航、天行客车版、天行重型商用车版，储能领域发布天恒储
能系统（全球首款5年零衰减、单体6.25MWh），PU100储能产品等。公司还持续拓展工程
机械、船舶、航空器等新兴应用场景，推出滑板底盘、巧克力换电、骐骥换电等创新解决
方案。
```

**提炼方法**：
- 数据来源：年报"经营情况讨论与分析"→研发投入、产品创新
- R&D investments必须包含具体金额和同比增长率
- New product launches列举具体产品名称和技术参数
- 使用括号补充技术细节（如：系统能量密度超200Wh/kg）
- 按产品线分类（乘用车、商用车、储能等）

---

## ✅ 中国地区质量检查清单

### 语言检查（关键！）
- [ ] Section标题全部英文 ✅
- [ ] 财务科目名称全部英文（Revenue, Net Profit等）✅
- [ ] 基础列标题英文（Field, Multiplier, Currency）✅
- [ ] 公司名称用简体中文 ✅
- [ ] 分析内容用简体中文 ✅
- [ ] S2.5描述用简体中文 ✅
- [ ] 无英文和中文混用在同一层级

### 格式检查
- [ ] S1.2列标题：公司全称+年份+年年度报告 ✅
- [ ] S1.3列标题：Field | Answer ✅
- [ ] S3.1列标题：Perspective | Answer（带括号）✅
- [ ] S3.2列标题：2024年年度报告 | 2023年年度报告 ✅
- [ ] S3.3列标题：Field | 公司全称+年份+年年度报告 ✅
- [ ] S4.1列标题：Perspective | 公司全称**+2024+**年年度报告 ✅（加号连接）
- [ ] S6.1列标题：Perspective | 公司全称 2024 年年度报告**.pdf** ✅（PDF后缀）
- [ ] S6.2列标题：Perspective | 公司全称**+2024+**年年度报告 ✅（加号连接）
- [ ] S6.3列标题：Perspective | 公司全称 2024 年年度报告 ✅（正常格式）

### 数据检查
- [ ] Multiplier通常为Thousands
- [ ] Currency为CNY
- [ ] Net Profit使用合并口径（含少数股东）
- [ ] Shareholders' Equity使用合并口径
- [ ] Balance Sheet平衡验证

### 内容检查
- [ ] S2.5用中文格式："2024年分产品营业收入（千元）：..."
- [ ] 所有数据从年度报告提取
- [ ] 分析内容用地道的简体中文表达

---

## 🎯 中国地区常见错误

### ❌ 错误1：Section标题翻译
```markdown
错误：# 第一部分：公司概述
正确：# Section 1: Company Overview
```

### ❌ 错误2：财务科目翻译
```markdown
错误：| 营业收入 | 362,012,554 |
正确：| Revenue | 362,012,554 |
```

### ❌ 错误3：列标题格式错误
```markdown
错误：| Perspective | 2024 Report | 2023 Report |
正确：| Perspective | 2024年年度报告 | 2023年年度报告 | (S3.2)
正确：| Perspective | 公司全称2024年年度报告 | ... | (S1.2)
```

### ❌ 错误4：数据口径错误
```markdown
错误：只用"归属于母公司所有者的净利润"
正确：合并净利润 = 归母净利润 + 少数股东损益
```

### ❌ 错误5：S2.5格式错误
```markdown
错误：Revenue by Product: Battery System $253M
正确：2024年分产品营业收入（千元）：动力电池系统 253,041,337...
```

---

## 📖 Sample003完整参考

**公司**：宁德时代新能源科技股份有限公司
**年报**：2024年年度报告
**位置**：samples/sample003.md

**关键特征**：
- 新能源动力电池行业
- 使用中国企业会计准则
- Multiplier: Thousands（千元）
- 双层语言结构（框架英文+内容中文）
- 特殊列标题格式

---

*中国地区完整规范 v1.0 - 基于Sample003 (宁德时代)*
