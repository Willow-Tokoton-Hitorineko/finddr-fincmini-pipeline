# 印尼地区完整规范 - Sample008 (Garudafood)

> **适用地区**: 印尼 (Indonesia)
> **Sample编号**: Sample008
> **Sample公司**: PT Garudafood Putra Putri Jaya Tbk
> **验证集案例**: val018 (PT Indofood CBP Sukses Makmur Tbk)

---

## 📋 地区基本信息

```yaml
地区: 印尼
语言: 100%英文
货币: IDR (印尼盾/Rupiah)
Multiplier: Billions (⚠️ 特别注意！)
会计准则: Indonesian GAAP (基于IFRS)
年报格式: Laporan Tahunan / Annual Report
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
| Company Name | PT Garudafood Putra Putri Jaya Tbk |
| Establishment Date | N/A |
| Headquarters Location | Jakarta, Indonesia |
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
| Field | Value |
| :---- | :---- |
| Mission Statement | [原文或N/A] |
| Vision Statement | [原文或N/A] |
| Core Values | [原文或N/A] |
```

**⚠️ 印尼地区特殊要求**：列标题为 **Field | Value**

**Sample008示例**：
```
| Mission Statement | Providing quality food products with love for the people of Indonesia |
| Vision Statement | To be the leading food company in Indonesia and regional markets |
| Core Values | N/A |
```

---

## 📊 Section 2: Financial Performance

### S2.1: Income Statement

**表格格式**：
```markdown
| Field | 2024 | 2023 | 2022 | Multiplier | Currency |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Revenue | 12,235.37 | 11,345.89 | 10,567.23 | Billions | IDR |
| Cost of Goods Sold | (8,456.78) | (7,890.12) | (7,345.67) | Billions | IDR |
| Gross Profit | 3,778.59 | 3,455.77 | 3,221.56 | Billions | IDR |
| Operating Expense | (2,123.45) | (1,987.65) | (1,876.54) | Billions | IDR |
| Operating income | 1,655.14 | 1,468.12 | 1,345.02 | Billions | IDR |
| Net Profit | 1,123.45 | 987.65 | 876.54 | Billions | IDR |
| Income before income taxes | 1,456.78 | 1,234.56 | 1,098.76 | Billions | IDR |
| Income tax expense(benefit) | (333.33) | (246.91) | (222.22) | Billions | IDR |
| Interest Expense | (123.45) | (98.76) | (87.65) | Billions | IDR |
```

**⚠️⚠️ 印尼地区超级关键特征**：

**1. Multiplier判断（最容易出错！）**：
```yaml
印尼盾价值小，企业常用Billions:
  年报标注：Rp jutaan (百万盾)
  实际含义：Millions IDR
  但换算为：Billions IDR显示更清晰
  
Sample008标准：
  Revenue: 12,235.37
  Multiplier: Billions ✅
  Currency: IDR
  
完整数值：12,235,370,000,000 IDR (12.2 trillion)

⚠️⚠️ 如果误用Millions：
  数值会是：12,235,370 (错误！差1000倍)
  
正确理解：
  年报：Rp 12.235.370 juta (百万)
  = 12,235,370 million IDR
  = 12,235.37 billion IDR ✅
```

**判断流程**：
```
Step 1: 查看年报标注
  "Disajikan dalam jutaan Rupiah" = 以百万印尼盾列示
  "juta" = million
  
Step 2: 读取原始数值
  Rp 12.235.370 (juta) = 12,235,370 million IDR
  
Step 3: 转换为合适单位
  12,235,370 million = 12,235.37 billion
  
Step 4: 填写表格
  Revenue: 12,235.37
  Multiplier: Billions ✅
  Currency: IDR
```

**2. 负数格式**：
```markdown
印尼/IFRS使用括号：
Cost of Goods Sold: (8,456.78) ✅
Interest Expense: (123.45) ✅
```

**3. Indonesian GAAP科目名称**：
```
Revenue = Pendapatan / Revenue
Net Profit = Laba / Profit for the year (合并口径)
Operating income = Laba usaha / Operating profit
```

---

### S2.2: Balance Sheet

**表格格式**：
```markdown
| Field | 2024 | 2023 | 2022 | Multiplier | Currency |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Total Assets | 15,678.90 | 14,567.89 | 13,456.78 | Billions | IDR |
| Current Assets | 8,234.56 | 7,654.32 | 7,123.45 | Billions | IDR |
| Non-Current Assets | 7,444.34 | 6,913.57 | 6,333.33 | Billions | IDR |
| Total Liabilities | 9,876.54 | 9,234.56 | 8,765.43 | Billions | IDR |
| Current Liabilities | 4,567.89 | 4,123.45 | 3,876.54 | Billions | IDR |
| Non-Current Liabilities | 5,308.65 | 5,111.11 | 4,888.89 | Billions | IDR |
| Shareholders' Equity | 5,802.36 | 5,333.33 | 4,691.35 | Billions | IDR |
| Retained Earnings | 2,345.67 | 2,111.11 | 1,876.54 | Billions | IDR |
| Total Equity and Liabilities | 15,678.90 | 14,567.89 | 13,456.78 | Billions | IDR |
| Inventories | 1,234.56 | 1,098.76 | 987.65 | Billions | IDR |
| Prepaid Expenses | 234.56 | 198.76 | 176.54 | Billions | IDR |
```

**注意**：所有数值都用Billions IDR

---

### S2.3: Cash Flow Statement

**表格格式**：标准格式，Multiplier: Billions, Currency: IDR

---

### S2.4: Key Financial Metrics

**表格格式**：标准格式

**验证范围**：
- Gross Margin通常30%-40%（食品业）
- Interest Coverage正常范围
- 注意印尼盾汇率影响

---

### S2.5: Operating Performance

**表格格式**：
```markdown
| Field | 2024 | 2023 | 2022 |
| :---- | :---- | :---- | :---- |
| Revenue by Product/Service | Snacks: Rp 5,678 billion Beverages: Rp 3,456 billion... | ... | ... |
| Revenue by Geographic Region | Java: Rp 7,890 billion Sumatra: Rp 2,345 billion... | ... | ... |
```

**注意**：描述中可以标注"Rp X billion"帮助理解

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

**⚠️ 印尼地区特殊要求**：
- 列标题：**Perspective | Answer** ✅
- 行标题带括号说明 ✅

---

### S3.2: Financial Performance Summary

**表格格式**：标准双年份对比

---

### S3.3: Business Competitiveness

**表格格式**：
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Business Model | [分析] | [分析] |
| Market Position | [分析] | [分析] |
```

**⚠️ 印尼地区特殊要求**：列标题为 **Perspective | 2024 Report | 2023 Report**

---

## 📊 Section 4-6

标准表格对比格式，全部英文。

---

## ✅ 印尼地区质量检查清单

### 格式检查
- [ ] S1.3列标题：Field | Value ✅
- [ ] S3.1列标题：Perspective | Answer（带括号）✅
- [ ] S3.3列标题：Perspective | 2024 Report | 2023 Report ✅

### 数据检查（⚠️ 最关键！）
- [ ] Multiplier为**Billions**（不是Millions）✅✅✅
- [ ] Currency为IDR
- [ ] 负数使用括号格式
- [ ] 数值换算正确（年报jutaan → Billions）

### Multiplier验证流程
```
□ 查看年报标注："jutaan Rupiah"
□ 理解含义：million IDR
□ 转换单位：million → billion (÷1000)
□ 填写：Multiplier: Billions ✅
□ 交叉验证：Revenue约10-20 trillion IDR合理
```

---

## 🎯 印尼地区常见错误（关键！）

### ❌ 错误1：Multiplier判断错误（最严重！）
```markdown
错误：Multiplier: Millions
      Revenue: 12,235,370
      实际值：12.2 trillion IDR ✅

错误结果：12.2 billion IDR ❌（差1000倍）

正确：Multiplier: Billions
      Revenue: 12,235.37
      实际值：12.2 trillion IDR ✅
```

### ❌ 错误2：年报单位理解错误
```markdown
错误理解：
  年报"jutaan" = thousands（千）

正确理解：
  "jutaan" = millions（百万）
  "ribuan" = thousands（千）
  "miliar" = billions（十亿）
```

### ❌ 错误3：数值格式错误
```markdown
错误：12,235,370.00 (Billions)
正确：12,235.37 (Billions)

或者：
错误：12235.37 (无逗号)
正确：12,235.37 (千位分隔)
```

---

## 📖 Sample008完整参考

**公司**：PT Garudafood Putra Putri Jaya Tbk
**年报**：Laporan Tahunan 2024
**位置**：samples/sample008.md

**关键特征**：
- 食品饮料制造业
- **Multiplier: Billions IDR** ⚠️⚠️
- 使用Indonesian GAAP（基于IFRS）
- 年报双语（印尼语+英文）
- 负数用括号格式

**数值示例**：
```
年报原文：Rp 12.235.370 juta
含义：12,235,370 million IDR
转换：12,235.37 billion IDR
填写：12,235.37 | Billions | IDR ✅
```

---

## 🚨 特别警告

**印尼地区是唯一使用Billions的地区！**

```
美国：Millions USD ✅
英国：Millions GBP ✅
中国：Thousands CNY ✅
香港：Millions CNY ✅
新加坡：Millions SGD ✅
澳大利亚：Millions USD/AUD ✅
马来西亚：Thousands MYR ✅
印尼：Billions IDR ✅✅✅ ← 唯一！
```

**如果Multiplier错误，Section 2得分会接近0分！**

---

*印尼地区完整规范 v1.0 - 基于Sample008 (Garudafood)*

**⚠️ 最后提醒：印尼=Billions，不是Millions！**
