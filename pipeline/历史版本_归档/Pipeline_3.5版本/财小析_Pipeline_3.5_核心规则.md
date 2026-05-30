# 财小析Pipeline 3.5 - 核心规则手册

> **版本**: 3.5 | **更新日期**: 2025-01-20 | **状态**: 生产环境

---

## 🎯 核心原则：语言、格式、内容三位一体

**这是Pipeline 3.5的灵魂，也是唯一最重要的原则！**

每个地区的报告必须严格遵守三大要素的**完整统一**：

### 1. 语言（Language）
- 使用该地区的**标准语言**
- Section 1-6**全部内容**必须使用该语言
- **零容忍**：不允许出现其他语言

### 2. 格式（Format）
- 使用该地区sample的**精确表格格式**
- 包括列标题、列顺序、表格结构
- Section 1-6**全部使用表格**，无段落格式

### 3. 内容（Content）
- 按该地区sample的**分析深度和表达方式**
- 财务指标计算口径与sample一致
- 论述逻辑符合该地区习惯

**记住：三者必须完全匹配，缺一不可！**

---

## 📋 八大地区完整标准

### Sample001 - 美国（NVIDIA/Exxon Mobil）
```yaml
语言: 英文
货币: USD Millions
会计准则: US GAAP
特殊要求:
  - S1.3: Field | Value
  - S3.1: Field | Answer
  - S3.3: Field | 2024 Report | 2023 Report
  - Section 4-6: 全部英文表格格式
```

### Sample002 - 英国（Chemring/Fever-Tree）
```yaml
语言: 英文
货币: GBP Millions
会计准则: IFRS
特殊要求:
  - S1.3: Field | Answer
  - S3.1: Perspective | Answer
  - S3.3: Field | 2024 Report | 2023 Report
  - Section 4-6: 全部英文表格格式
```

### Sample003 - 中国（宁德时代/五粮液）⚠️ 简体中文
```yaml
语言: 简体中文
货币: CNY Thousands
会计准则: 中国GAAP
特殊要求:
  - S1.2列标题: "公司全称2024年年度报告 | 公司全称2023年年度报告"
  - S1.3: Field | Answer
  - S3.1: Perspective | Answer (带括号说明)
  - S3.2列标题: "2024年年度报告 | 2023年年度报告"
  - S3.3列标题: "Field | 公司全称2024年年度报告 | 公司全称2023年年度报告"
  - S4.1列标题: "Perspective | 公司全称+2024+年年度报告 | 公司全称+2023+年年度报告"
  - S6列标题特殊格式
  - Section 4-6: 全部简体中文表格
```

### Sample004 - 香港（腾讯/美团）⚠️ 繁体中文
```yaml
语言: 繁体中文
货币: CNY/HKD Millions
会计准则: IFRS
特殊要求:
  - S1.3: Field | Value
  - S3.1: Perspective | Answer (带括号说明)
  - S3.3: Perspective | 2024 Report | 2023 Report
  - Section 4-6: 全部繁体中文表格
  - 简繁转换: 必须使用标准繁体字
```

### Sample005 - 新加坡（新航/IHH Healthcare）
```yaml
语言: 英文
货币: RM/SGD Millions
会计准则: MFRS/IFRS
特殊要求:
  - S1.3: Field | Answer
  - S3.1: Field | Answer
  - S3.3: Field | 2024 Report | 2023 Report
  - Section 4-6: 全部英文表格格式
```

### Sample006 - 澳大利亚（CSL/Telstra）
```yaml
语言: 英文
货币: AUD Millions
会计准则: IFRS
特殊要求:
  - S1.3: Field | Value
  - S3.1: Perspective | Answer (带括号说明)
  - S3.3: Perspective | 2024 Report | 2023 Report
  - Section 4-6: 全部英文表格格式
```

### Sample007 - 马来西亚（IJM/Maxis）
```yaml
语言: 英文
货币: RM Millions
会计准则: MFRS
特殊要求:
  - S1.3: Field | Answer
  - S3.1: Field | Answer
  - S3.2列标题: "Perspective Column | 2024 Report | 2023 Report" ⚠️注意Column
  - S3.3列标题: "Field | 2024 Report  | 2023 Report" ⚠️注意2个空格
  - Section 4-6: 全部英文表格格式
```

### Sample008 - 印尼（Garudafood/Mayora）
```yaml
语言: 英文
货币: IDR Millions/Billions
会计准则: Indonesian GAAP
特殊要求:
  - S1.3: Field | Value
  - S3.1: Perspective | Answer (带括号说明)
  - S3.3: Perspective | 2024 Report | 2023 Report
  - Section 4-6: 全部英文表格格式
```

---

## 🚨 关键执行规则

### 规则1：语言使用规则 ⭐ 重要更新

**重要发现**：语言规则**因地区类型而异**！

#### 规则1A：英文地区（简单规则）

**美国、英国、新加坡、澳大利亚、马来西亚、印尼**：

✅ **100%英文，无需分层**
- Section标题、列标题、财务科目、分析内容
- 公司信息、描述文字、所有内容
- ❌ **严禁**出现任何中文字符

```markdown
# Section 2: Financial Performance  ← 英文
## S2.1: Income Statement  ← 英文
| Field | 2024 | Multiplier | Currency |  ← 英文
| Revenue | 60,922 | Millions | USD |  ← 英文
| Revenue by Product/Service | Compute & Networking: $47,405M |  ← 英文
| Revenue & Direct-Cost Dynamics | Revenue experienced dramatic growth... |  ← 英文
```

#### 规则1B：中文地区（分层规则）⚠️

**中国、香港**：

**框架层（英文）+ 内容层（地区语言）**

**层1 - 框架（永远英文）**：
- ✅ Section标题：`# Section 1: Company Overview`
- ✅ 子Section标题：`## S2.1: Income Statement`
- ✅ 表格基础列标题：`Field`, `Multiplier`, `Currency`
- ✅ 财务科目名称：`Revenue`, `Cost of Goods Sold`, `Total Assets`

**层2 - 内容（地区语言）**：

**简体中文地区（中国）**：
- ✅ 公司名称、分析文字、S2.5描述用**简体中文**
- ✅ **特殊列标题**：S1.2/S3.2/S3.3/S4.1用中文格式（公司全称2024年年度报告）
- ❌ **严禁**将Section标题、财务科目翻译成中文

**繁体中文地区（香港）**：
- ✅ 公司名称、分析文字、S2.5描述用**繁体中文**
- ✅ 列标题用标准英文（Perspective | 2024 Report | 2023 Report）
- ❌ **严禁**使用简体中文
- ❌ **严禁**将Section标题、财务科目翻译成中文

#### 快速判断法

```
确定地区 → 选择规则

英文地区（6个）→ 规则1A：100%英文 ✅
中文地区（2个）→ 规则1B：框架英文+内容中文 ✅

关键：英文地区不需要分层！
```

### 规则2：格式使用规则（100%表格）

**Section 1-6全部使用表格格式**：
- ✅ S1.2, S1.3: 表格
- ✅ S2.1-S2.5: 表格
- ✅ S3.1, S3.2, S3.3: 表格
- ✅ S4.1: 表格（4个风险维度）
- ✅ S5.1, S5.2: 表格
- ✅ S6.1, S6.2, S6.3: 表格

**列标题必须精确匹配**：
- 严格按照对应sample的列标题
- 中文地区注意特殊格式（如"公司全称+年份+年年度报告"）
- 马来西亚S3.2注意"Perspective Column"

### 规则3：内容准则

**分析深度**：
- 参考对应sample的详细程度
- 保持同等长度的论述
- 覆盖所有sample中涉及的要点

**表达方式**：
- 语言风格与sample保持一致
- 专业术语使用符合该地区习惯
- 逻辑结构遵循sample范式

**财务口径**：
- 数据计算方法与sample一致
- Multiplier（Millions/Thousands）严格按地区
- 会计准则（US GAAP/IFRS/中国GAAP）正确应用

### 规则4：严禁行为（零容忍）

❌ **语言混用（更新：分层理解）**
- 英文地区使用中文内容
- 香港地区使用简体中文
- ⚠️ **中国/香港地区严禁**：
  - 将Section标题翻译成中文（如"第一部分：公司概述"）
  - 将财务科目名称翻译成中文（如"营业收入"应为"Revenue"）
  - 将基础列标题翻译成中文（如"字段"应为"Field"）

❌ **格式错误**
- 使用段落格式代替表格
- 列标题与sample不一致
- 表格结构不规范
- 中国地区不使用特殊列标题格式（如"公司全称2024年年度报告"）

❌ **额外内容**
- 在报告结尾添加Pipeline说明
- 添加"预期得分"、"关键优化点"等
- 添加sample中没有的section或内容

❌ **数据偷懒**
- S1.3填N/A而不查证真实信息
- 财务数据计算错误
- 使用外部信息而非年报数据

#### 常见错误示例

**❌ 错误**（中国地区）：
```markdown
# 第一部分：公司概述  ← Section标题用中文
| 字段 | 数值 |  ← 列标题用中文
| 营业收入 | 100,000 |  ← 财务科目用中文
```

**✅ 正确**（中国地区）：
```markdown
# Section 1: Company Overview  ← Section标题英文
| Field | Value |  ← 列标题英文
| Revenue | 100,000 |  ← 财务科目英文
```

---

## ✅ 执行检查清单

### 开始前（确定地区）
- [ ] 确认公司所属地区（8选1）
- [ ] 查看对应sample的精确格式
- [ ] 了解该地区的语言、货币、会计准则

### Section 1-6（逐个检查）

**语言分层检查**：
- [ ] **框架层（英文）**：Section标题、列标题（Field/Multiplier/Currency）、财务科目名称
- [ ] **内容层（地区语言）**：公司名称、分析文字、S2.5描述内容
- [ ] **特殊列标题**：中国地区S1.2/S3.2/S3.3等使用特殊格式

**格式检查**：
- [ ] 全部section使用表格格式
- [ ] 列标题与sample完全一致
- [ ] 表格结构规范

**内容检查**：
- [ ] 分析深度和表达方式匹配sample
- [ ] 财务数据计算准确
- [ ] 无数据偷懒行为

---

## 📌 评分对齐总则（v3.6，跨地区增补）

> 目的：针对非S2模块（S1/S3/S4/S5/S6）显著失分点，补充“字符串精确匹配与合规口径”。所有示例以各地区规范文档为准，不覆盖其专属差异，只作跨地区通用提醒。

### A. 标题与列头
- **Section与子节标题**：统一为 `# Section X: ...`、`## Sx.y: ...`，标题中的冒号与空格须与sample一致（`S1.2:`而非`S1.2 :`）。
- **列标题精确匹配**：严格使用地区规范文档中给出的列头字符串（含大小写、顺序与空格）。马来西亚与中国存在唯一特例，按各自地区文档执行。

### B. S1 提分点
- **S1.1 公司名称**：使用数据集/评测的“标准公司名”字符串，避免连字符、大小写差异等（示例：UK使用“Fevertree Drinks PLC”）。
- **S1.1 总部**：按地区规范给定格式书写（示例：UK使用“City, UK”）。
- **S1.3 严格N/A策略**：若年报未以正式标题披露“Mission/Vision/Core Values”，三项一律 `N/A`。严禁用口号/市场营销语替代。

### C. S3/S4/S6 行标题（逐字匹配）
- **S3.1**：各地区行标题及括号说明需逐字匹配；UK示例包含括号与分号间空格：
  - `Revenue & Direct-Cost Dynamics (Revenue Growth ; Gross Margin; Revenue by Product/Service; Revenue by Geographic Region)`
  - `Operating Efficiency (Operating Margin)`
  - `External & One-Off Impact (Effective Tax Rate, Non-Recurring Items)`
- **S3.2**：风险识别行在UK为 `Financial risk identification and early warning`。
- **S4.1**：四行固定为 `Market Risks / Operational Risks / Financial Risks / Compliance Risks`（按地区规范逐字匹配）。
- **S6.1**：行标题按地区规范执行（UK为 `Mergers and Acquisition`）。

### D. S5.1 董事薪酬（角色与金额格式）
- **角色选择**：优先列示 3 位关键角色：`Chair/Chairman`、`Chief Executive Officer (CEO)`、`Chief Financial Officer (CFO)`；其余成员非必需，避免与评测口径不一致。
- **职位命名**：必须包含标准关键字（CEO/CFO/Chair）。如“CEO & Executive Director”，输出时保留“CEO”。
- **金额口径**：严格按地区规范换算并使用本币符号与千位分隔（UK常见披露为`£k`，输出需换算为`£`，×1000）。
- **合规**：仅使用年报披露“Single total figure of remuneration / Total”列，不得估算或凑整。

### E. 执行建议
- **先按地区规范构建骨架**（列头/行头逐字匹配），再填入内容与数据。
- **提交前自检**：对比地区规范“评分对齐补充（v3.6）”清单逐项打勾；若任一项不满足，必须返工。

### 最后检查
- [ ] 删除所有结尾的Pipeline说明
- [ ] 检查Section标题是否全部英文
- [ ] 检查财务科目名称是否全部英文
- [ ] 验证所有表格格式正确

---

## 📖 Pipeline 3.5 升级说明

### 相比3.2的改进：

**1. 明确"三位一体"原则**
- 将语言、格式、内容提升为核心原则
- 强调三者必须完整统一

**2. 强化繁体中文规范**
- 明确香港地区必须使用繁体中文
- 提供简繁转换标准指导

**3. 验证集实战经验**
- 基于8个验证集修复的实战经验
- 明确常见错误和规避方法

**4. 简化文档结构**
- 整合核心规则到单一文档
- 删除重复和过时内容

### 验证集质量标准：
基于val001-val043的修复经验，所有报告必须达到：
- ✅ 语言100%正确
- ✅ 格式100%表格
- ✅ 内容符合sample标准
- ✅ 无Pipeline结尾说明

---

## 🎯 记住核心

> **语言、格式、内容三位一体**
> 
> **缺一不可，100%执行！**

---

*财小析Pipeline 3.5 - 让财务分析报告标准化、专业化、地区化* 🚀
