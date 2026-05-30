# 新加坡地区完整规范 - Sample005 (Singapore Airlines)

> **适用地区**: 新加坡 (Singapore)
> **Sample编号**: Sample005
> **Sample公司**: Singapore Airlines Limited
> **验证集案例**: val001 (IHH Healthcare)

---

## 📋 地区基本信息

```yaml
地区: 新加坡
语言: 100%英文
货币: SGD (新加坡元) 或 RM (马来西亚林吉特)
Multiplier: Millions
会计准则: SFRS/MFRS (基于IFRS)
年报格式: Annual Report
特殊概念: PATMI (Profit After Tax and Minority Interest)
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
| Company Name | Singapore Airlines Limited |
| Establishment Date | N/A |
| Headquarters Location | Singapore, Singapore |
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

**⚠️ 新加坡地区特殊要求**：列标题为 **Field | Answer**

**Sample005示例**：
```
| Mission Statement | Singapore Airlines is a global company dedicated to providing air transportation services of the highest quality... |
| Vision Statement | The Singapore Airlines Group remains committed to maintaining its position as a leading airline... |
| Core Values | N/A |
```

---

## 📊 Section 2: Financial Performance

### S2.1: Income Statement

**表格格式**：
```markdown
| Field | 2025 | 2024 | 2023 | Multiplier | Currency |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Revenue | 19,539.8 | 19,012.7 | 17,774.8 | Millions | SGD |
| Cost of Goods Sold | N/A | N/A | N/A | Millions | SGD |
| Gross Profit | N/A | N/A | N/A | Millions | SGD |
| Operating Expense | N/A | N/A | N/A | N/A | N/A |
| Operating Income | 1,709.1 | 2,727.5 | 2,692.1 | Millions | SGD |
| Net Profit | 2,778.0 | 2,674.8 | 2,156.8 | Millions | SGD |
| Income before income taxes | 2,964.8 | 3,037.1 | 2,636.8 | Millions | SGD |
| Income tax expense(benefit) | 152.6 | 342.0 | 473.5 | Millions | SGD |
| Interest Expense | 366.1 | 394.8 | 388.7 | Millions | SGD |
```

**⚠️ 新加坡地区关键特征**：

**1. 航空业特殊处理**：
```yaml
航空服务业:
  COGS: N/A ✅
  Gross Profit: N/A ✅
  Operating Expense: N/A ✅
  只填Revenue和Operating Income
```

**2. 财年制度**：
```markdown
注意：新加坡公司可能使用非自然年财年
Sample005使用：2025财年 = 2024年4月-2025年3月
列标题使用财年年份：2025, 2024, 2023 ✅
```

**3. Multiplier判断**：
```
年报标注："S$ million" 或 "SGD million" → Millions ✅
```

**4. 特殊科目**：
```
Net Profit = Profit attributable to owners of the parent
或使用PATMI概念（合并口径）
```

---

### S2.2: Balance Sheet

**表格格式**：
```markdown
| Field | 2025 | 2024 | 2023 | Multiplier | Currency |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Total Assets | 43,086.8 | 44,264.7 | 49,101.2 | Millions | SGD |
| Current Assets | 11,396.0 | 15,641.7 | 19,299.3 | Millions | SGD |
| Non-Current Assets | N/A | N/A | N/A | N/A | N/A |
| Total Liabilities | 27,016.8 | 27,520.1 | 28,851.4 | Millions | SGD |
| Current Liabilities | 13,955.1 | 12,671.7 | 13,670.9 | Millions | SGD |
| Non-Current Liabilities | N/A | N/A | N/A | N/A | N/A |
| Shareholders' Equity | 16,070.0 | 16,744.6 | 20,249.8 | Millions | SGD |
| Retained Earnings | N/A | N/A | N/A | N/A | N/A |
| Total Equity and Liabilities | 43,086.8 | 44,264.7 | 49,101.2 | Millions | SGD |
| Inventories | 344.9 | 268.0 | 227.0 | Millions | SGD |
| Prepaid Expenses | 109.9 | 153.9 | 105.0 | Millions | SGD |
```

**注意**：
- 部分科目可能N/A（如年报未单独披露）
- Non-Current Assets和Non-Current Liabilities可能N/A
- Retained Earnings可能N/A

---

### S2.3: Cash Flow Statement

**表格格式**：标准格式

---

### S2.4: Key Financial Metrics

**表格格式**：
```markdown
|  | 2025 | 2024 | 2023 |
| :---- | :---- | :---- | :---- |
| Gross Margin | N/A | N/A | N/A |
| Operating Margin | 8.75% | 14.35% | 15.15% |
| Net Profit Margin | 14.17% | 14.07% | 12.13% |
| Current Ratio | 81.66% | 123.44% | 141.17% |
| Quick Ratio | 78.40% | 120.11% | 138.74% |
| Debt-to-Equity | 168.12% | 164.35% | 142.48% |
| Interest Coverage | 466.84% | 690.86% | 692.59% |
| Asset Turnover | 44.74% | 40.73% | N/A |
| Return on Equity | 16.93% | 14.46% | N/A |
| Return on Assets | 6.3% | 5.73% | N/A |
| Effective Tax Rate | 5.15% | 11.26% | 17.96% |
| Dividend Payout Ratio | 51.43% | 42.25% | 13.78% |
```

**注意**：航空服务业Gross Margin = N/A

---

### S2.5: Operating Performance

**表格格式**：
```markdown
| Field | 2025 | 2024 | 2023 |
| :---- | :---- | :---- | :---- |
| Revenue by Product/Service | Full-Service Carrier (FSC): $16,738.0M Low-Cost Carrier (LCC): $2,349.2M Engineering Services: $1,245.1M Others: $154.2M | ... | ... |
| Revenue by Geographic Region | East Asia: $9,917.8M Europe: $2,512.6M South West Pacific: $2,957.7M Americas: $1,333.7M West Asia and Africa: $1,328.2M... | ... | ... |
```

**Sample005示例**：详细列出各服务线和地理区域收入

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

**⚠️ 新加坡地区特殊要求**：列标题为 **Field | Answer**

---

### S3.2: Financial Performance Summary

**表格格式**：标准双年份对比

---

### S3.3: Business Competitiveness

**表格格式**：
```markdown
| Field | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Business Model | [分析] | [分析] |
| Market Position | [分析] | [分析] |
```

**⚠️ 新加坡地区特殊要求**：列标题为 **Field | 2024 Report | 2023 Report**

---

## 📊 Section 4-6

标准表格对比格式，全部英文。

---

## ✅ 新加坡地区质量检查清单

### 格式检查
- [ ] S1.3列标题：Field | Answer ✅
- [ ] S3.1列标题：Field | Answer ✅
- [ ] S3.3列标题：Field | 2024 Report | 2023 Report ✅

### 数据检查
- [ ] 航空/服务业COGS和Gross Profit可能为N/A
- [ ] 财年年份使用正确（可能非自然年）
- [ ] Multiplier为Millions
- [ ] Currency为SGD或RM

### 特殊概念
- [ ] PATMI = Profit After Tax and Minority Interest
- [ ] 理解为合并净利润（含少数股东）

---

## 🎯 新加坡地区常见错误

### ❌ 错误1：财年理解错误
```markdown
错误：2024年报 = 2024年1-12月
正确：2024年报可能 = 2023年4月-2024年3月（视公司而定）
```

### ❌ 错误2：列标题错误
```markdown
错误：S3.1用 Perspective | Answer
正确：S3.1用 Field | Answer
```

---

## 📖 Sample005完整参考

**公司**：Singapore Airlines Limited
**年报**：Annual Report 2024/25
**位置**：samples/sample005.md

**关键特征**：
- 航空服务业
- COGS和Gross Profit为N/A
- 使用财年制（非自然年）
- 使用SFRS准则（基于IFRS）
- Currency: SGD

---

*新加坡地区完整规范 v1.0 - 基于Sample005 (Singapore Airlines)*
