# 三地区格式重点对照 - China, Australia, UK

> **负责地区**：中国、澳大利亚、英国  
> **目的**：重点匹配这三个地区的格式标准，避免混淆  
> **创建日期**：2025-10-22

---

## 🎯 核心原则

**每个地区独立标准，严禁混用！**

- ✅ 中国用中国的标准（Sample003）
- ✅ 澳大利亚用澳大利亚的标准（Sample006）
- ✅ 英国用英国的标准（Sample002）
- ❌ 绝对不能把A地区的格式用到B地区

---

## 📊 Section 1-2 格式对照

### S1.1: Basic Information

| 项目 | 中国 | 澳大利亚 | 英国 |
|------|------|---------|------|
| **列标题** | Field \| Value | Field \| Value | Field \| Value |
| **公司名称格式** | 中文全称 | 英文全称 | 英文全称 |
| **地址格式** | 中国+省+市 | City, Australia | City, UK |
| **示例** | 中国福建省宁德市 | Melbourne, Australia | Romsey, Hampshire, UK |

✅ **三地区统一**：列标题都是 `Field | Value`

---

### S1.2: Core Competencies

| 项目 | 中国 | 澳大利亚 | 英国 |
|------|------|---------|------|
| **标题格式** | `## S1.2 : Core Competencies` ⚠️ 冒号前有空格 | `## S1.2 : Core Competencies` ⚠️ 冒号前有空格 | `## S1.2 : Core Competencies` ⚠️ 冒号前有空格 |
| **列标题** | Perspective \| 公司全称2024年年度报告 \| 公司全称2023年年度报告 | Perspective \| 2024 Report \| 2023 Report | Perspective \| 2024 Report \| 2023 Report |
| **内容语言** | **简体中文** | 英文 | 英文 |

**中国特殊**：
- ✅ 列标题包含完整公司名称
- ✅ 内容必须简体中文
- 示例：`| Perspective | 宁德时代新能源科技股份有限公司2024年年度报告 | ...`

**澳大利亚/英国**：
- ✅ 列标题简短：`2024 Report | 2023 Report`
- ✅ 内容必须英文

---

### S1.3: Mission & Vision

| 项目 | 中国 | 澳大利亚 | 英国 |
|------|------|---------|------|
| **标题格式** | `## S1.3 : Mission & Vision` ⚠️ 冒号前有空格 | `## S1.3 : Mission & Vision` ⚠️ 冒号前有空格 | `## S1.3 : Mission & Vision` ⚠️ 冒号前有空格 |
| **列标题** | Field \| **Answer** | Field \| **Value** | Field \| **Answer** |
| **N/A格式** | **N.A** | N/A | N/A |
| **内容语言** | 简体中文 | 英文 | 英文 |

**⚠️ 关键差异**：
- 中国：`Field | Answer` + 使用`N.A`
- 澳大利亚：`Field | Value` + 使用`N/A`
- 英国：`Field | Answer` + 使用`N/A`

---

### S2.1-S2.3: Financial Statements

| 项目 | 中国 | 澳大利亚 | 英国 |
|------|------|---------|------|
| **货币** | CNY | USD (或AUD) | GBP |
| **Multiplier** | Thousands (或Ones) | Millions | Millions |
| **负数格式** | `\-48,875,311` (反斜杠转义) | `(数值)` 括号 | `(数值)` 括号 |
| **会计准则** | 中国GAAP | IFRS | IFRS |

**中国特殊**：
- ✅ 负数用反斜杠转义：`\-48,875,311`
- ✅ Multiplier判断：大型企业Thousands，超大型Ones

**澳大利亚/英国**：
- ✅ 负数用括号：`(335.8)`
- ✅ Multiplier统一Millions

---

### S2.4: Key Financial Metrics

| 项目 | 中国 | 澳大利亚 | 英国 |
|------|------|---------|------|
| **第一列** | `\|   \|` (空) | `\|   \|` (空) | `\|   \|` (空) |
| **格式** | 纯百分比 | 纯百分比 | 纯百分比 |
| **示例** | 24.44% | 51.8% | 11.38% |

✅ **三地区完全统一**：
- 第一列为空
- 无Multiplier/Currency列
- 所有数值必须有%符号
- 保留2位小数

---

### S2.5: Operating Performance

| 项目 | 中国 | 澳大利亚 | 英国 |
|------|------|---------|------|
| **行标题格式** | Revenue by Product/Service | Revenue by Product/Service | Revenue by Product/Service |
| **内容格式** | 2024年分产品营业收入（千元）：动力电池系统... | Immunoglobulins: 5,666, Albumin: 1,209... | Sensors & Information: £212.0m... |
| **语言** | **简体中文** | 英文 | 英文 |

**中国特殊**：
- ✅ 描述性中文：`2024年分产品营业收入（千元）：...`
- ✅ 单位明确标注

---

## 📊 Section 3 格式对照（⚠️ 关键差异）

### S3.1: Profitability Analysis

| 项目 | 中国 | 澳大利亚 | 英国 |
|------|------|---------|------|
| **列标题** | Perspective \| Answer | Perspective \| Answer | Perspective \| Answer |
| **行标题格式** | **带括号说明** | **带括号说明** | **不带括号** |
| **内容语言** | **简体中文** | 英文 | 英文 |

**行标题示例**：

**中国**：
```markdown
| Revenue & Direct-Cost Dynamics (Revenue Growth ; Gross Margin; Revenue by Product/Service; Revenue by Geographic Region) | 公司收入在2022-2023年间实现强劲增长... |
```

**澳大利亚**：
```markdown
| Revenue & Direct-Cost Dynamics (Revenue Growth ; Gross Margin; Revenue by Product/Service; Revenue by Geographic Region) | CSL demonstrated strong revenue growth... |
```

**英国**：
```markdown
| Revenue & Direct-Cost Dynamics | Revenue grew from £442.8m... |
```

⚠️ **英国特殊**：行标题**不带括号说明**，其他两个地区带括号

---

### S3.2: Financial Performance Summary

| 项目 | 中国 | 澳大利亚 | 英国 |
|------|------|---------|------|
| **列标题** | Perspective \| **2024年年度报告** \| **2023年年度报告** | Perspective \| 2024 Report \| 2023 Report | Perspective \| 2024 Report \| 2023 Report |
| **内容语言** | **简体中文** | 英文 | 英文 |

**中国特殊**：
- ✅ 列标题：`2024年年度报告`（短格式，无公司全称）
- ✅ 内容简体中文

**澳大利亚/英国**：
- ✅ 列标题：`2024 Report`（英文）
- ✅ 内容英文

---

### S3.3: Business Competitiveness

| 项目 | 中国 | 澳大利亚 | 英国 |
|------|------|---------|------|
| **列标题第一列** | **Field** | **Perspective** | **Field** |
| **列标题2/3** | **公司全称2024年年度报告** \| **公司全称2023年年度报告** | 2024 Report \| 2023 Report | 2024 Report \| 2023 Report |
| **内容语言** | **简体中文** | 英文 | 英文 |

**⚠️ 超级关键差异**：

**中国**：
```markdown
| Field | 宁德时代新能源科技股份有限公司2024年年度报告 | 宁德时代新能源科技股份有限公司2023年年度报告 |
| :---- | :---- | :---- |
| Business Model | 公司主要通过销售动力电池... | 公司主要通过销售动力电池... |
```
- 第一列：`Field`
- 包含完整公司全称

**澳大利亚**：
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Business Model | CSL operates a global... | CSL's business model... |
```
- 第一列：`Perspective`

**英国**：
```markdown
| Field | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Business Model | Chemring operates a technology-driven... | Chemring's business model... |
```
- 第一列：`Field`

✅ **总结**：中国和英国用`Field`，澳大利亚用`Perspective`

---

## 📊 Section 4 格式对照

### S4.1: Risk Factors

| 项目 | 中国 | 澳大利亚 | 英国 |
|------|------|---------|------|
| **列标题** | Perspective \| 公司全称**+2024+**年年度报告 \| ... | Perspective \| 2024 Report \| 2023 Report | Perspective \| 2024 Report \| 2023 Report |
| **内容语言** | **简体中文** | 英文 | 英文 |

**中国特殊**：
- ✅ 列标题有**加号连接**：`宁德时代新能源科技股份有限公司+2024+年年度报告`
- ✅ 这是中国地区的独特标记！

**示例对比**：

**中国**：
```markdown
| Perspective | 宁德时代新能源科技股份有限公司+2024+年年度报告 | 宁德时代新能源科技股份有限公司+2023+年年度报告 |
```

**澳大利亚/英国**：
```markdown
| Perspective | 2024 Report | 2023 Report |
```

---

## 📊 Section 4-6 格式对照

### S5.1: Board Composition

| 项目 | 中国 | 澳大利亚 | 英国 |
|------|------|---------|------|
| **列标题** | Name \| Position \| Total Income | Name \| Position \| Total Income | Name \| Position \| Total Income |
| **币种格式** | 万元或千元 | USD/AUD (需标注$或A$) | £或GBP |

✅ **三地区统一**：列标题完全一致

### S5.2: Internal Controls

✅ **三地区统一**：`Perspective | 2024 Report | 2023 Report`

---

## ⚠️ Section 6 格式对照（新发现）

### S6.1: Strategic Direction

| 项目 | 中国 | 澳大利亚 | 英国 |
|------|------|---------|------|
| **列标题格式** | 公司全称 **2024 年**年度报告**.pdf** | Perspective \| 2024 Report | Perspective \| 2024 Report |

**中国S6.1特殊**：
```markdown
| Perspective | 宁德时代新能源科技股份有限公司 2024 年年度报告.pdf | ...
                                                    ↑ 有PDF后缀 ↑
```

### S6.2: Challenges and Uncertainties

| 项目 | 中国 | 澳大利亚 | 英国 |
|------|------|---------|------|
| **第一列** | Perspective | **Perspective Column** | **Perspective Column** |
| **列标题格式** | 公司全称**+2024+**年年度报告 | Perspective Column \| 2024 Report | Perspective Column \| 2024 Report |

**中国S6.2特殊**：
```markdown
| Perspective | 宁德时代新能源科技股份有限公司+2024+年年度报告 | ...
                                              ↑ 加号连接 ↑
```

**澳大利亚/英国S6.2特殊**：
```markdown
| Perspective Column | 2024 Report | 2023 Report |
  ↑ Perspective Column，不是Perspective！
```

### S6.3: Innovation and Development Plans

| 项目 | 中国 | 澳大利亚 | 英国 |
|------|------|---------|------|
| **列标题格式** | 公司全称 **2024 年**年度报告（无PDF无加号） | Perspective \| 2024 Report | Perspective \| 2024 Report |

**中国S6.3格式**：
```markdown
| Perspective | 宁德时代新能源科技股份有限公司 2024 年年度报告 | ...
  有空格，无PDF，无加号
```

---

## 🔍 三地区核心差异总结表（完整版）

| 格式项 | 中国 (Sample003) | 澳大利亚 (Sample006) | 英国 (Sample002) |
|--------|-----------------|---------------------|-----------------|
| **S1.2列标题** | 含公司全称 | 简短2024 Report | 简短2024 Report |
| **S1.3列标题** | Field \| **Answer** | Field \| **Value** | Field \| **Answer** |
| **S1.3的N/A** | **N.A** | N/A | N/A |
| **负数格式** | **\-数值** (反斜杠) | (数值) 括号 | (数值) 括号 |
| **S3.1行标题** | 带括号 | 带括号 | **不带括号** |
| **S3.2列标题** | 2024年年度报告 | 2024 Report | 2024 Report |
| **S3.3第一列** | **Field** | **Perspective** | **Field** |
| **S3.3列标题** | 含公司全称 | 简短Report | 简短Report |
| **S4.1列标题** | 含**+号连接** | 简短Report | 简短Report |
| **S6.1列标题** | 含**.pdf后缀** | 简短Report | 简短Report |
| **S6.2第一列** | Perspective | **Perspective Column** | **Perspective Column** |
| **S6.2列标题** | 含**+号连接** | 简短Report | 简短Report |
| **S6.3列标题** | 正常格式（无PDF无+） | 简短Report | 简短Report |
| **内容语言** | **简体中文** | 英文 | 英文 |
| **Multiplier** | Thousands/Ones | Millions | Millions |

---

## ⚠️ 最容易混淆的8个点（更新版）

### 1. S1.3列标题（三地区不同）
```markdown
中国：Field | Answer ✅
澳大利亚：Field | Value ✅  ← 特殊！
英国：Field | Answer ✅
```

### 2. S3.1行标题括号（英国特殊）
```markdown
中国：带括号 ✅
澳大利亚：带括号 ✅
英国：不带括号 ✅  ← 特殊！
```

### 3. S3.3第一列（三地区不同）
```markdown
中国：Field ✅
澳大利亚：Perspective ✅  ← 特殊！
英国：Field ✅
```

### 4. 负数格式（中国特殊）
```markdown
中国：\-48,875,311 ✅  ← 反斜杠转义
澳大利亚：(5,282) ✅  ← 括号
英国：(335.8) ✅  ← 括号
```

### 5. S4.1列标题（中国特殊）
```markdown
中国：公司全称+2024+年年度报告 ✅  ← 有加号
澳大利亚：2024 Report ✅
英国：2024 Report ✅
```

### 6. S6.1列标题（中国特殊） ⭐ 新增
```markdown
中国：公司全称 2024 年年度报告.pdf ✅  ← 有PDF后缀
澳大利亚：2024 Report ✅
英国：2024 Report ✅
```

### 7. S6.2第一列（澳英特殊） ⭐ 新增
```markdown
中国：Perspective ✅
澳大利亚：Perspective Column ✅  ← 特殊！
英国：Perspective Column ✅  ← 特殊！
```

### 8. S6.2列标题（中国特殊） ⭐ 新增
```markdown
中国：公司全称+2024+年年度报告 ✅  ← 有加号
澳大利亚：Perspective Column | 2024 Report ✅
英国：Perspective Column | 2024 Report ✅
```

---

## ✅ 三地区格式检查清单

### 中国地区检查清单
- [ ] S1.2列标题包含完整公司全称
- [ ] S1.3使用`N.A`（不是N/A）
- [ ] S1.3列标题：Field | **Answer**
- [ ] 负数用反斜杠转义：`\-数值`
- [ ] S3.1行标题带括号说明
- [ ] S3.2列标题：`2024年年度报告`（短格式）
- [ ] S3.3第一列：`Field`
- [ ] S3.3列标题包含完整公司全称
- [ ] S4.1列标题有加号：`+2024+`
- [ ] **S6.1列标题有PDF后缀**：`.pdf` ⭐
- [ ] **S6.2第一列**：`Perspective`（正常）
- [ ] **S6.2列标题有加号**：`+2024+` ⭐
- [ ] **S6.3列标题无PDF无加号** ⭐
- [ ] 所有内容简体中文（除了框架）
- [ ] Multiplier: Thousands或Ones

### 澳大利亚地区检查清单
- [ ] S1.2列标题：`2024 Report`（简短）
- [ ] S1.3使用`N/A`
- [ ] S1.3列标题：Field | **Value**
- [ ] 负数用括号：`(数值)`
- [ ] S3.1行标题带括号说明
- [ ] S3.2列标题：`2024 Report`
- [ ] S3.3第一列：`Perspective`（特殊！）
- [ ] S3.3列标题：`2024 Report`
- [ ] S4.1列标题：`2024 Report`
- [ ] **S6.1列标题**：`2024 Report`
- [ ] **S6.2第一列**：`Perspective Column`（特殊！）⭐
- [ ] **S6.3列标题**：`2024 Report`
- [ ] 所有内容英文
- [ ] Multiplier: Millions

### 英国地区检查清单
- [ ] S1.2列标题：`2024 Report`（简短）
- [ ] S1.3使用`N/A`
- [ ] S1.3列标题：Field | **Answer**
- [ ] 负数用括号：`(数值)`
- [ ] S3.1行标题**不带**括号（特殊！）
- [ ] S3.2列标题：`2024 Report`
- [ ] S3.3第一列：`Field`
- [ ] S3.3列标题：`2024 Report`
- [ ] S4.1列标题：`2024 Report`
- [ ] **S6.1列标题**：`2024 Report`
- [ ] **S6.2第一列**：`Perspective Column`（特殊！）⭐
- [ ] **S6.3列标题**：`2024 Report`
- [ ] 所有内容英文
- [ ] Multiplier: Millions
- [ ] 服务业COGS=N/A

---

## 📖 快速参考

### 执行步骤

1. **确定地区**：中国/澳大利亚/英国
2. **打开对应规范**：
   - 中国：`中国地区完整规范_Sample003.md`
   - 澳大利亚：`澳大利亚地区完整规范_Sample006.md`
   - 英国：`英国地区完整规范_Sample002.md`
3. **使用本文档检查清单**：逐项核对
4. **严禁混用**：只用对应地区的格式

---

## 🚨 严禁行为

1. ❌ **把中国的格式用到澳大利亚/英国**
2. ❌ **把澳大利亚的Perspective用到中国S3.3**
3. ❌ **把英国的无括号格式用到中国/澳大利亚S3.1**
4. ❌ **混淆N.A和N/A**
5. ❌ **负数格式混用**

---

*三地区格式重点对照 v1.0 - 2025-10-22*

**核心原则**：各地区独立标准，严禁混用！
