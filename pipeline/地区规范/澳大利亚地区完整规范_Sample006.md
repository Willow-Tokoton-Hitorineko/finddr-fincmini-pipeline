# 澳大利亚地区完整规范 - Sample006 (CSL)

> **适用地区**: 澳大利亚 (Australia)
> **Sample编号**: Sample006
> **Sample公司**: CSL Limited
> **验证集案例**: val036 (Telstra)

---

## 📋 地区基本信息

```yaml
地区: 澳大利亚
语言: 100%英文
货币: USD (美元) 或 AUD (澳元)
Multiplier: Millions
会计准则: IFRS (Australian Accounting Standards)
年报格式: Annual Report
```

---

## 🎯 语言规则

### 绝对规则
- ✅ **Section 1-6全部100%英文**
- ✅ 公司信息、分析内容、描述全部英文
- ❌ **严禁出现任何中文字符**

---

## 📊 Section 1: Company Overview

### S1.1: Basic Information

**表格格式**：
```markdown
| Field | Value |
| :---- | :---- |
| Company Name | CSL Limited |
| Establishment Date | 1916 |
| Headquarters Location | Melbourne, Australia |
```

---
**⚠️ 评分对齐补充（v3.6）**
- 公司名称使用数据集标准字符串（避免大小写/连字符差异）。
- 总部地址统一格式为“City, Australia”（例如：`Melbourne, Australia`）。
- 成立日期未明确披露时，一律 `N/A`，禁止推测。

---

### S1.2: Core Competencies

**⚠️ 标题格式要求**：`## S1.2 : Core Competencies`（冒号前有空格）

**表格格式**：标准双年份对比
**内容模板与评分对齐（v3.6）**
- 每行至少包含**2个定量锚点**（金额/比率/pp变化等），并给出**2024 vs 2023**明确对照。
- 仅增强内容，不得改动任何列头/行头字符串。

**安全锚点策略（来源与留痕）**
- 优先使用本文件 `S2.1–S2.5` 的数字；若 S2 未覆盖，允许使用“同一案例两年年报的原始披露数据”（同公司、同年度范围、同口径）。
- 使用年报原始披露数据时：
  - 必须在《样本取数路径_3.6.md》中记录证据留痕（文件名/页码或章节/表名）。
  - 单位/倍率/币种按年报原文，且与本文件整体口径一致（如 Millions/A$）。
- 表达方式：优先“并列对照”（如“Assets 45,600 vs 44,200 (Millions, A$)”）；YoY/pp 仅在两种情形下使用：① 年报明确披露该YoY/pp；② 由本文件S2数字可直接计算。否则避免自行推导。
- 每个单元格建议≤3个锚点（金额/比率/pp变化），确保简洁且可追溯。
- 比率口径与 `S2.4` 保持一致（百分比，两位小数）。
- 风险行推荐锚点：`Debt-to-Equity`、`Interest Coverage`、`Current Ratio`、`Dividend Payout Ratio`、`Net Cash Flow from Operations`（来源 S2 或年报披露）。

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

**⚠️ 澳大利亚地区特殊要求**：列标题为 **Field | Value**

**Sample006示例**：
```
| Mission Statement | The people and science of CSL save lives... |
| Vision Statement | CSL is committed to a healthier world... |
| Core Values | Patient Focus, Integrity, Innovation, Superior Performance, Collaboration |
```

---
**⚠️ 评分对齐补充（v3.6）**
- 若年报未以正式标题披露 Mission/Vision/Core Values，则三项均填 `N/A`；禁止以品牌口号替代。

---

## 📊 Section 2: Financial Performance

### S2.1: Income Statement

**表格格式**：
```markdown
| Field | 2024 | 2023 | 2022 | Multiplier | Currency |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Revenue | 14,800 | 13,310 | 10,562 | Millions | USD |
| Cost of Goods Sold | (7,129) | (6,485) | (4,830) | Millions | USD |
| Gross Profit | 7,671 | 6,825 | 5,732 | Millions | USD |
| Operating Expense | (3,859) | (3,756) | (2,805) | Millions | USD |
| Operating Income | 3,812 | 3,069 | 2,927 | Millions | USD |
| Net Profit | 2,714 | 2,244 | 2,255 | Millions | USD |
| Income before income taxes | 3,375 | 2,663 | 2,780 | Millions | USD |
| Income tax expense(benefit) | (661) | (419) | (525) | Millions | USD |
| Interest Expense | (476) | (444) | (165) | Millions | USD |
```

**⚠️ 澳大利亚地区数据口径**：
```yaml
净利润口径: 合并净利润（Total profit for the year）
  - 包含: Profit attributable to equity holders + Non-controlling interests
  - 计算: 归母净利润 + 少数股东损益
  - 验证: sample006 CSL: 2,714M = 2,642M(归母) + 72M(少数股东)
  - 原因: 这是澳大利亚地区标准，直接执行
```

**⚠️ 澳大利亚地区关键特征**：

**1. Currency特殊情况**：
```yaml
跨国公司（如CSL）:
  报告货币: USD ✅
  
本土公司（如Telstra）:
  报告货币: AUD
```

**2. 负数格式**：
```markdown
澳大利亚/IFRS使用括号：
Cost of Goods Sold: (7,129) ✅
Interest Expense: (476) ✅
```

**3. Multiplier判断**：
```
年报标注：
"US$ million" → Millions, USD ✅
"A$ million" → Millions, AUD
```

**4. 财年制度**：
```markdown
注意：澳大利亚公司常用非自然年财年
Sample006: 2024财年 = 2023年7月-2024年6月
```

---

### S2.2: Balance Sheet

**表格格式**：标准格式，注意负数用括号

---

### S2.3: Cash Flow Statement

**表格格式**：标准格式，注意负数用括号

---

### S2.4: Key Financial Metrics

**表格格式**：
```markdown
|  | 2024 | 2023 | 2022 |
| :---- | :---- | :---- | :---- |
| Gross Margin (%) | 51.8% | 51.3% | 54.3% |
| Operating Margin (%) | 25.77% | 23.06% | 27.72% |
| Net Profit Margin | 18.34% | 16.87% | 21.37% |
| Current Ratio | 217.54% | 200.93% | 231.58% |
| Quick Ratio | 91.92% | 75.61% | 168.18% |
| Debt-to-Equity | 107.25% | 116.61% | 94.46% |
| Interest Coverage | 801.68% | 691.22% | 1,773.94% |
| Asset Turnover | 40.0% | 41.22% | N/A |
| Return on Equity | 14.58% | 13.85% | N/A |
| Return on Assets | 7.3% | 6.95% | N/A |
| Effective Tax Rate | 19.59% | 15.74% | 18.90% |
| Dividend Payout Ratio | 45.65% | 56.42% | 46.08% |
```

**公式必检（不得偏离比赛规则）**
- Quick Ratio = (Current Assets − Inventories − Prepaid)/Current Liabilities × 100%
- Interest Coverage = Operating income/Interest expense × 100%
- ROE/ROA/Asset Turnover 使用平均口径；若缺少期初（如2022）→ N/A
- Dividend Payout Ratio = Dividends/Net Profit × 100%
- 所有百分比统一两位小数输出

**注意**：Sample006指标名称略有差异（如"Gross Margin (%)"），但内容一致

---

### S2.5: Operating Performance

**表格格式**：
```markdown
| Field | 2024 | 2023 | 2022 |
| :---- | :---- | :---- | :---- |
| Revenue by Product/Service | Immunoglobulins: 5,666, Albumin: 1,209, Haemophilia: 1,313... | ... | ... |
| Revenue by Geographic Region | Australia: 900, United States: 7,294, Germany: 873, UK: 744... | ... | ... |
```

---

## 📊 Section 3: Business Analysis

### S3.1: Profitability Analysis

**表格格式**：
```markdown
| Perspective | Answer |
| :---- | :---- |
| Revenue & Direct-Cost Dynamics (Revenue Growth ; Gross Margin; Revenue by Product/Service; Revenue by Geographic Region) | [英文分析] |
| Operating Efficiency (Operating Margin) | [英文分析] |
| External & One-Off Impact (Effective Tax Rate, Non-Recurring Items) | [英文分析] |
```

**⚠️ 澳大利亚地区特殊要求**：
- 列标题：**Perspective | Answer** ✅
- 行标题带括号说明 ✅

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
**内容模板与评分对齐（v3.6）**
- 每行至少包含**2个定量锚点**（金额/比率/pp变化等），并给出**2024 vs 2023**明确对照。
- 仅增强内容，不得改动任何列头/行头字符串。

---

**📏 S3.1 内容长度与密度标准（v3.6新增 - 基于Sample006逆向分析）**

| 维度 | 标准长度 | 数据密度 | 必须包含 |
|------|---------|---------|---------|
| Revenue & Direct-Cost Dynamics | 80-120词 | 6-8个数据点 | 收入增长率、毛利率、主要产品/地区 |
| Operating Efficiency | 80-120词 | 6-8个数据点 | 营业利润率、营业利润、现金流 |
| External & One-Off Impact | 80-120词 | 6-8个数据点 | 有效税率、非经常性损益 |

**数据点定义**：
- 具体数值（如$14,800M）= 1点
- 百分比/比率（如26.0%增长）= 1点  
- 定性判断（如"strong growth"）= 1点

**提炼方法（关键原则）**：
1. **多源整合**：从利润表+附注+MD&A整合3-5个数据源
2. **计算增长率**：(本期-上期)/上期 × 100%
3. **归纳总结**：用总括语（"demonstrated strong revenue growth"）
4. **逻辑连接**：用"However"、"while"、"indicating"构建段落
5. **深度分析**：不只列数据，要有判断（"indicating cost pressures"）

**分析用词库（澳洲英文）**：
- 正面：strong, robust, healthy, significant, enhanced, expanding
- 负面：declined, compressed, pressures, challenges, modest recovery
- 中性：remained, relatively stable, mixed performance
- 因果：indicating, suggesting, demonstrating, representing

---

### S3.2: Financial Performance Summary

**表格格式**：标准双年份对比（逐字匹配五行）
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Comprehensive financial health | ... | ... |
| Profitability and earnings quality | ... | ... |
| Operational efficiency | ... | ... |
| Financial risk identification and early warning | ... | ... |
| Future financial performance projection | ... | ... |
```

---
**内容模板与评分对齐（v3.6）**
- 每行至少包含**2个定量锚点**（金额/比率/pp变化等），并给出**2024 vs 2023**明确对照。
- 仅增强内容，不得改动任何列头/行头字符串。

---

**📏 S3.2 内容长度与密度标准（v3.6新增 - 基于Sample006逆向分析）**

| 维度 | 单列长度 | 数据密度 | 组织结构 |
|------|---------|---------|---------|
| Comprehensive financial health | 120-180词 | 8-12个指标 | 资产→权益→流动性→现金流 |
| Profitability and earnings quality | 120-180词 | 8-12个指标 | 净利润→利润率→ROE/ROA→质量判断 |
| Operational efficiency | 120-180词 | 8-12个指标 | 营业利润率→费用控制→资产周转 |
| Financial risk | 120-180词 | 8-12个指标 | D/E→利息覆盖→流动比率→风险点 |
| Future projection | 120-180词 | 前瞻性判断 | 基于趋势→增长动力→风险→平衡判断 |

**注意**：每个维度有2024+2023两列，总计240-360词/维度

**整合逻辑**：
1. 开篇总括（"demonstrates robust financial health"）
2. 分项数据呈现（总资产、权益、比率等）
3. 趋势分析（增长、改善、下降）
4. 因果判断（"strengthening"、"indicating"）
5. 平衡评价（"However"转折）

---

### S3.3: Business Competitiveness

**表格格式**：
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Business Model | [分析] | [分析] |
| Market Position | [分析] | [分析] |
```

**⚠️ 澳大利亚地区特殊要求**：列标题为 **Perspective | 2024 Report | 2023 Report**

---

## 📊 Section 4-6

标准表格对比格式，全部英文。

### S4.1: Risk Factors（评分对齐补充 v3.6）
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Market Risks | ... | ... |
| Operational Risks | ... | ... |
| Financial Risks | ... | ... |
| Compliance Risks | ... | ... |
```
— 四行标题逐字匹配。

---
**内容模板与评分对齐（v3.6）**
- 每行至少包含**2个定量锚点**（金额/比率/pp变化等），并给出**2024 vs 2023**明确对照。
- 仅增强内容，不得改动任何列头/行头字符串。

---

### S5.1: Board Composition（评分对齐补充 v3.6）
- 建议仅列三位关键角色：`Chair/Chairman`、`Chief Executive Officer (CEO)`、`Chief Financial Officer (CFO)`。
- 职位命名应含关键字（CEO/CFO/Chair），如“CEO & Managing Director”可输出为“Chief Executive Officer (CEO)”。
- 金额口径：若披露为`A$'000`或`$'000`，输出需换算为`A$`或`$`整额（×1000），并带千位分隔；货币按年报（AUD→`A$`，USD→`US$`）。
- 仅使用“Single total figure of remuneration/Total”列，不得估算。

### S5.2: Internal Controls（评分对齐补充 v3.6）
- 列标题：`Perspective | 2024 Report | 2023 Report`
- 行标题包含：`Risk assessment procedures`、`Control activities`、`Monitoring mechanisms`、`Identified material weaknesses or deficiencies`、`Improvements`、`Effectiveness`。

---
### S6.1: Strategic Direction（评分对齐补充 v3.6）
- 列标题：`Perspective | 2024 Report | 2023 Report`
- 行标题使用：`Mergers and Acquisitions`、`New Technologies`、`Organisational Restructuring`（英式拼写，逐字匹配）。

### S6.2: Challenges and Uncertainties（评分对齐补充 v3.6）

**⚠️ 澳大利亚S6.2特殊格式**：第一列用`Perspective Column`（不是Perspective）！

- **列标题**：`Perspective Column | 2024 Report | 2023 Report`
- 行标题：标准英文描述
- 这是S6.2唯一的特殊格式

**Sample006实际格式**（第178行）：
```markdown
| Perspective Column | 2024 Report | 2023 Report |
  ↑ Perspective Column，不是Perspective！
```

### S6.3: Innovation and Development Plans（评分对齐补充 v3.6）
- 列标题：`Perspective | 2024 Report | 2023 Report`
- 行标题：标准英文描述

---

## ✅ 澳大利亚地区质量检查清单

### 格式检查
- [ ] S1.3列标题：Field | Value ✅
- [ ] S3.1列标题：Perspective | Answer（带括号）✅
- [ ] S3.3列标题：Perspective | 2024 Report | 2023 Report ✅

### 数据检查
- [ ] 负数使用括号格式：(7,129) ✅
- [ ] Multiplier为Millions
- [ ] Currency为USD或AUD（视公司而定）
- [ ] 注意财年制度（可能非自然年）

---

## 🎯 澳大利亚地区常见错误

### ❌ 错误1：财年理解错误
```markdown
错误：2024年报 = 2024年1-12月
正确：2024年报可能 = 2023年7月-2024年6月
```

### ❌ 错误2：Currency混淆
```markdown
错误：所有澳大利亚公司都用AUD
正确：跨国公司可能用USD（如CSL）
```

### ❌ 错误3：列标题错误
```markdown
错误：S3.3用 Field | 2024 Report | 2023 Report
正确：S3.3用 Perspective | 2024 Report | 2023 Report
```

---

## 📖 Sample006完整参考

**公司**：CSL Limited
**年报**：Annual Report 2023/24
**位置**：samples/sample006.md

**关键特征**：
- 生物制药公司
- 使用USD作为报告货币
- 财年制：7月-6月
- 使用IFRS（澳大利亚准则）
- 负数用括号格式

---

*澳大利亚地区完整规范 v1.0 - 基于Sample006 (CSL)*
