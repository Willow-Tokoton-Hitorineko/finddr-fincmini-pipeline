# 马来西亚地区完整规范 - Sample007 (IJM)

> **适用地区**: 马来西亚 (Malaysia)
> **Sample编号**: Sample007
> **Sample公司**: IJM Corporation Berhad
> **验证集案例**: val010 (Maxis Berhad)

---

## 📋 地区基本信息

```yaml
地区: 马来西亚
语言: 100%英文
货币: MYR (马来西亚林吉特/RM)
Multiplier: Thousands
会计准则: MFRS (Malaysian Financial Reporting Standards)
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
| Company Name | IJM Corporation Berhad |
| Establishment Date | 1983 |
| Headquarters Location | Petaling Jaya, Selangor Darul Ehsan, Malaysia |
```

---

### S1.2: Core Competencies

**⚠️ 标题格式要求**：`## S1.2 : Core Competencies`（冒号前有空格）

**表格格式**：标准双年份对比

---

### S1.3: Mission & Vision

**⚠️ 标题格式要求**：`## S1.3 : Mission & Vision`（冒号前有空格）

**表格格式**：
```markdown
| Field | Answer |
| :---- | :---- |
| Mission Statement | [原文或N/A] |
| Vision Statement | [原文或N/A] |
| Core Values | [原文或N/A] |
```

**⚠️ 马来西亚地区特殊要求**：列标题为 **Field | Answer**

**Sample007示例**：
```
| Mission Statement | Our mission is to deliver sustainable value to our stakeholders... |
| Vision Statement | Our vision is to become a leading Malaysian conglomerate... |
| Core Values | INTEGRITY, TEAMWORK, INNOVATION, CUSTOMER FOCUS |
```

---

## 📊 Section 2: Financial Performance

### S2.1: Income Statement

**表格格式**：
```markdown
| Field | 2024 | 2023 | 2022 | Multiplier | Currency |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Revenue | 5,918,814 | 4,572,485 | 4,408,980 | Thousands | MYR |
| Cost of Goods Sold | 4,368,576 | 3,392,540 | 3,646,889 | Thousands | MYR |
| Gross Profit | 1,550,238 | 1,179,945 | 762,091 | Thousands | MYR |
| Operating Expense | 597,087 | 673,994 | 474,489 | Thousands | MYR |
| Operating income | 1,272,780 | 740,865 | 537,480 | Thousands | MYR |
| Net Profit | 660,278 | 158,275 | 794,890 | Thousands | MYR |
| Income before income taxes | 964,169 | 483,028 | 317,871 | Thousands | MYR |
| Income tax expense (benefit) | (298,977) | (271,432) | (182,935) | Thousands | MYR |
| Interest Expense | 307,137 | 255,572 | 188,295 | Thousands | MYR |
```

**⚠️ 马来西亚地区关键特征**：

**1. Multiplier判断**：
```yaml
马来西亚中大型企业:
  年报标注：RM'000 或 Thousands
  Multiplier: Thousands ✅
  
特大型企业可能:
  年报标注：RM million
  Multiplier: Millions
```

**Sample007使用**：Thousands

**2. 货币标识**：
```
Currency: MYR ✅
或简写为：RM
年报中常见：RM'000
```

**3. 负数格式**：
```markdown
马来西亚/MFRS使用括号：
Income tax expense (benefit): (298,977) ✅
注意：科目名称中也有括号
```

**4. MFRS科目名称**：
```
Revenue = Revenue
Net Profit = Profit for the year (合并口径)
Operating income = Operating profit
```

---

### S2.2: Balance Sheet

**表格格式**：
```markdown
| Field | 2024 | 2023 | 2022 | Multiplier | Currency |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Total Assets | 21,315,323 | 20,510,595 | 21,012,048 | Thousands | MYR |
| Current Assets | 12,103,108 | 11,834,454 | 12,358,903 | Thousands | MYR |
| Non-Current Assets | 9,212,215 | 8,676,141 | 8,653,145 | Thousands | MYR |
| Total Liabilities | 9,996,467 | 9,549,525 | 9,551,314 | Thousands | MYR |
| Current Liabilities | 5,014,777 | 4,800,790 | 4,562,491 | Thousands | MYR |
| Non-Current Liabilities | 4,981,685 | 4,748,735 | 4,988,823 | Thousands | MYR |
| Shareholders' Equity | 10,216,514 | 9,843,764 | 9,937,547 | Thousands | MYR |
| Retained Earnings | 4,342,205 | 4,024,571 | 4,000,050 | Thousands | MYR |
| Total Equity and Liabilities | 21,315,323 | 20,510,595 | 21,012,048 | Thousands | MYR |
| Inventories | 6,848,097 | 7,209,996 | 7,553,071 | Thousands | MYR |
| Prepaid Expenses | N/A | N/A | N/A | N/A | N/A |
```

**注意**：Prepaid Expenses可能N/A（年报未单独披露）

---

### S2.3: Cash Flow Statement

**表格格式**：标准格式

---

### S2.4: Key Financial Metrics

**表格格式**：标准格式

---

### S2.5: Operating Performance

**表格格式**：
```markdown
| Field | 2024 | 2023 | 2022 |
| :---- | :---- | :---- | :---- |
| Revenue by Product/Service: What is the revenue breakdown by product/service (NOT by market)? | Construction contracts: RM1,656,164,000 Property development: RM1,972,430,000... | ... | ... |
| Revenue by Geographic Region: What is the revenue breakdown by geographic region? | Malaysia: RM5,445,752,000 India: RM444,597,000... | ... | ... |
```

**⚠️ 马来西亚地区特殊要求**：
- 行标题包含问题说明（带冒号）
- 格式详细列出各项收入

---

## 📊 Section 3: Business Analysis

### S3.1: Profitability Analysis

**表格格式**：
```markdown
| Field | Answer |
| :---- | :---- |
| Revenue & Direct-Cost Dynamics | [英文分析] |
| Operating Efficiency | [英文分析] |
| External & One-Off Impact | [英文分析] |
```

**⚠️ 马来西亚地区特殊要求**：列标题为 **Field | Answer**

---

### S3.2: Financial Performance Summary

**表格格式**：
```markdown
| Perspective Column | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Comprehensive financial health | [分析] | [分析] |
| Profitability and earnings quality | [分析] | [分析] |
| Operational efficiency | [分析] | [分析] |
| Financial risk identification and early warning | [分析] | [分析] |
| Future financial performance projection | [分析] | [分析] |
```

**⚠️⚠️ 马来西亚地区超级特殊要求**：
- 第一列标题为 **Perspective Column**（不是Perspective）✅
- 这是唯一使用这个标题的地区！

---

### S3.3: Business Competitiveness

**表格格式**：
```markdown
| Field | 2024 Report  | 2023 Report |
| :---- | :---- | :---- |
| Business Model | [分析] | [分析] |
| Market Position | [分析] | [分析] |
```

**⚠️ 马来西亚地区特殊要求**：
- 列标题为 **Field | 2024 Report  | 2023 Report**
- 注意：2024 Report后面有**2个空格** ✅

---

## 📊 Section 4-6

标准表格对比格式，全部英文。

---

## ✅ 马来西亚地区质量检查清单

### 格式检查（关键！）
- [ ] S1.3列标题：Field | Answer ✅
- [ ] S3.1列标题：Field | Answer ✅
- [ ] S3.2列标题：**Perspective Column** | 2024 Report | 2023 Report ✅✅
- [ ] S3.3列标题：Field | 2024 Report  | 2023 Report（2个空格）✅

### 数据检查
- [ ] Multiplier为Thousands（大多数情况）
- [ ] Currency为MYR
- [ ] 负数使用括号格式
- [ ] 科目名称中的括号保留：Income tax expense (benefit)

### 内容检查
- [ ] S2.5行标题包含问题说明

---

## 🎯 马来西亚地区常见错误

### ❌ 错误1：S3.2列标题错误（最容易出错！）
```markdown
错误：| Perspective | 2024 Report | 2023 Report |
正确：| Perspective Column | 2024 Report | 2023 Report |
```

### ❌ 错误2：S3.3空格数量错误
```markdown
错误：| Field | 2024 Report | 2023 Report |
正确：| Field | 2024 Report  | 2023 Report | (2个空格)
```

### ❌ 错误3：Multiplier错误
```markdown
错误：使用Millions（数值会小1000倍）
正确：使用Thousands（马来西亚标准）
```

---

## 📖 Sample007完整参考

**公司**：IJM Corporation Berhad
**年报**：Annual Report 2024
**位置**：samples/sample007.md

**关键特征**：
- 建筑和房地产综合集团
- Multiplier: Thousands（RM'000）
- 使用MFRS准则
- S3.2特殊列标题：Perspective Column
- S3.3特殊空格：2个空格

---

*马来西亚地区完整规范 v1.0 - 基于Sample007 (IJM)*
