# 香港地区完整规范 - Sample004 (腾讯)

> **适用地区**: 香港 (Hong Kong)
> **Sample编号**: Sample004
> **Sample公司**: 騰訊控股有限公司
> **验证集案例**: val042 (美团)

---

## 📋 地区基本信息

```yaml
地区: 香港
语言: 繁体中文（内容层） + 英文（框架层）
货币: CNY/HKD (人民币/港币)
Multiplier: Millions
会计准则: IFRS (International Financial Reporting Standards)
年报格式: Annual Report
```

---

## 🎯 语言规则（⚠️ 重要！香港地区特殊）

### 双层语言规则

**框架层（永远英文）**：
```markdown
✅ Section标题：# Section 1: Company Overview
✅ 子Section标题：## S1.1: Basic Information
✅ 表格基础列标题：Field, Multiplier, Currency
✅ 财务科目名称：Revenue, Net Profit, Total Assets
```

**内容层（繁体中文）**：
```markdown
✅ 公司名称：騰訊控股有限公司
✅ 分析文字：公司收入在2022-2024年間保持穩健增長...
✅ S2.5描述：2024年分產品營業收入...
✅ 繁体用字：騰訊、營業、穩健、實現
```

### ⚠️ 严禁行为
```markdown
❌ 使用简体中文：腾讯（应为騰訊）
❌ Section标题翻译：第一部分：公司概述
❌ 财务科目翻译：營業收入（应为Revenue）
```

### 简繁对照表（常用）
```
简体 → 繁体
腾讯 → 騰訊
营业 → 營業
实现 → 實現
财务 → 財務
资产 → 資產
负债 → 負債
经营 → 經營
战略 → 戰略
```

---

## 📊 Section 1: Company Overview

### S1.1: Basic Information

**表格格式**：
```markdown
| Field | Value |
| :---- | :---- |
| Company Name | 騰訊控股有限公司 |
| Establishment Date | 1998年 |
| Headquarters Location | 中國廣東省深圳市 |
```

**⚠️ 香港地区特殊要求**：列标题为 **Field | Value**（不是Answer）

**Sample004示例**：
```
| Company Name | 騰訊控股有限公司 |
| Establishment Date | 1998年 |
| Headquarters Location | 中國廣東省深圳市 |
```

---

### S1.2: Core Competencies

**⚠️ 标题格式要求**：`## S1.2 : Core Competencies`（冒号前有空格）

**表格格式**：
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Innovation Advantages | [繁体中文分析，200-300字] | [繁体中文分析] |
| Product Advantages | [繁体中文分析] | [繁体中文分析] |
| Brand Recognition | [繁体中文分析] | [繁体中文分析] |
| Reputation Ratings | [繁体中文分析] | [繁体中文分析] |
```

**注意**：
- 列标题用标准英文：2024 Report | 2023 Report ✅
- 不需要公司全称（与中国地区不同）
- 内容用繁体中文

**Sample004示例**：
```
騰訊持續加大技術投入，**利用混元基礎模型等AI核心技術提升產品智能化水平，並深化產學研合作以促進AI、量子計算等前沿技術轉化。**
```

---

### S1.3: Mission & Vision

**⚠️ 标题格式要求**：`## S1.3 : Mission & Vision`（冒号前有空格）

**表格格式**：
```markdown
| Field | Value |
| :---- | :---- |
| Mission Statement | 用戶為本,科技向善 |
| Vision Statement | 智慧溝通 靈感無限 |
| Core Values | 正直、進取、協作、創造 |
```

**⚠️ 香港地区特殊要求**：列标题为 **Field | Value**

---

## 📊 Section 2: Financial Performance

### S2.1: Income Statement

**表格格式**：
```markdown
| Field | 2024 | 2023 | 2022 | Multiplier | Currency |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Revenue | 660,257 | 609,015 | 554,552 | Millions | CNY |
| Cost of Goods Sold | (311,011) | (315,906) | (315,806) | Millions | CNY |
| Gross Profit | 349,246 | 293,109 | 238,746 | Millions | CNY |
| Operating Expense | (149,149) | (137,736) | (135,925) | Millions | CNY |
| Operating income | 208,099 | 160,074 | 110,827 | Millions | CNY |
| Net Profit | 196,467 | 118,048 | 188,709 | Millions | CNY |
| Income before income taxes | 241,485 | 161,324 | 210,225 | Millions | CNY |
| Income tax expense(benefit) | (45,018) | (43,276) | (21,516) | Millions | CNY |
| Interest Expense | (12,447) | (11,885) | (9,352) | Millions | CNY |
```

**⚠️ 香港地区关键特征**：

**1. Multiplier判断**：
```yaml
腾讯级别大公司:
  年报标注：人民币百万元
  Multiplier: Millions ✅
  Currency: CNY
  
港股公司也可能用HKD:
  年报标注：港币百万元
  Multiplier: Millions
  Currency: HKD
```

**2. 负数格式**：
```markdown
香港/IFRS通常使用括号：
Cost of Goods Sold: (311,011) ✅
Interest Expense: (12,447) ✅
```

**3. IFRS科目名称**（框架英文）：
```markdown
✅ Revenue (不翻译成"收入")
✅ Net Profit (不翻译成"淨利潤")
✅ Operating income (不翻译成"經營溢利")
```

**4. 数据口径**：
```yaml
Net Profit: "本公司權益持有人應佔盈利" + "非控股權益"
= 合并净利润（含少数股东）✅
```

---

### S2.2: Balance Sheet

**表格格式**：标准格式

**IFRS科目名称**：
- Shareholders' Equity = **Total Equity** (包含非控股权益)
- 负债用括号：(727,099)

**Sample004示例**：
```
| Total Liabilities | 727,099 | 703,565 | 795,271 | Millions | CNY |
| Shareholders' Equity | 1,053,896 | 873,681 | 782,860 | Millions | CNY |
```

---

### S2.3: Cash Flow Statement

**表格格式**：标准格式，注意负数用括号

---

### S2.4: Key Financial Metrics

**表格格式**：标准格式，第一列为空

---

### S2.5: Operating Performance

**表格格式**：
```markdown
| Field | 2024 | 2023 | 2022 |
| :---- | :---- | :---- | :---- |
| Revenue by Product/Service | 2024年：• 增值服務：人民幣319,168百萬元（佔49%）• 營銷服務：人民幣121,374百萬元（佔18%）... | 2023年：... | 2022年：... |
| Revenue by Geographic Region | 2024年：• 中國內地：人民幣595,458百萬元• 其他地區：人民幣64,799百萬元 | ... | ... |
```

**⚠️ 香港地区特殊要求**：
- 使用繁体中文描述 ✅
- 格式类似中国地区，但用繁体字
- 可以使用项目符号"•"
- 必须包含数字和单位

**Sample004示例**：
```
2024年：• 增值服務：人民幣319,168百萬元（佔49%）• 營銷服務：人民幣121,374百萬元（佔18%）...
```

---

## 📊 Section 3: Business Analysis

### S3.1: Profitability Analysis

**表格格式**：
```markdown
| Perspective | Answer |
| :---- | :---- |
| Revenue & Direct-Cost Dynamics (Revenue Growth ; Gross Margin; Revenue by Product/Service; Revenue by Geographic Region) | [繁体中文分析] |
| Operating Efficiency (Operating Margin) | [繁体中文分析] |
| External & One-Off Impact (Effective Tax Rate, Non-Recurring Items) | [繁体中文分析] |
```

**⚠️ 香港地区特殊要求**：
- 列标题：**Perspective | Answer** ✅
- 行标题带英文括号说明 ✅
- 分析内容用繁体中文 ✅

---

### S3.2: Financial Performance Summary

**表格格式**：
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Comprehensive financial health | [繁体中文分析] | [繁体中文分析] |
| Profitability and earnings quality | [繁体中文分析] | [繁体中文分析] |
| Operational efficiency | [繁体中文分析] | [繁体中文分析] |
| Financial risk identification and early warning | [繁体中文分析] | [繁体中文分析] |
| Future financial performance projection | [繁体中文分析] | [繁体中文分析] |
```

**注意**：列标题用标准英文格式，不需要公司全称

---

### S3.3: Business Competitiveness

**表格格式**：
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Business Model | [繁体中文分析] | [繁体中文分析] |
| Market Position | [繁体中文分析] | [繁体中文分析] |
```

**⚠️ 香港地区特殊要求**：列标题为 **Perspective | 2024 Report | 2023 Report**

---

## 📊 Section 4-6

所有Section使用标准表格对比格式，内容用繁体中文。

---

## ✅ 香港地区质量检查清单

### 语言检查（关键！）
- [ ] 使用标准繁体中文（不是简体）✅
- [ ] Section标题全部英文 ✅
- [ ] 财务科目名称全部英文 ✅
- [ ] 基础列标题英文 ✅
- [ ] 无简繁混用

### 繁体字检查
- [ ] 騰訊（不是腾讯）
- [ ] 營業（不是营业）
- [ ] 實現（不是实现）
- [ ] 經營（不是经营）
- [ ] 戰略（不是战略）

### 格式检查
- [ ] S1.3列标题：Field | Value ✅
- [ ] S3.1列标题：Perspective | Answer（带括号）✅
- [ ] S3.3列标题：Perspective | 2024 Report | 2023 Report ✅
- [ ] 负数使用括号格式：(311,011) ✅

### 数据检查
- [ ] Multiplier通常为Millions
- [ ] Currency为CNY或HKD
- [ ] Net Profit使用合并口径
- [ ] Shareholders' Equity包含非控股权益

---

## 🎯 香港地区常见错误

### ❌ 错误1：使用简体中文
```markdown
错误：腾讯控股有限公司
正确：騰訊控股有限公司
```

### ❌ 错误2：列标题格式错误
```markdown
错误：S1.3用 Field | Answer
正确：S1.3用 Field | Value
```

### ❌ 错误3：负数格式错误
```markdown
错误：Cost of Goods Sold: -311,011
正确：Cost of Goods Sold: (311,011)
```

### ❌ 错误4：简繁混用
```markdown
错误：公司經營状况良好（"状况"是简体）
正确：公司經營狀況良好（全部繁体）
```

---

## 📖 Sample004完整参考

**公司**：騰訊控股有限公司
**年报**：Annual Report 2024
**位置**：samples/sample004.md

**关键特征**：
- 互联网科技公司
- 使用IFRS准则
- Multiplier: Millions（百万元）
- Currency: CNY（人民币）
- 双层语言结构（框架英文+内容繁体中文）
- 负数使用括号格式

---

*香港地区完整规范 v1.0 - 基于Sample004 (騰訊)*
