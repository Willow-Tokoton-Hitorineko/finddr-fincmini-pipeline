# AI快速使用指南 - Pipeline 3.5

> **5分钟快速上手财小析Pipeline** | 版本: 3.5

---

## 🚀 5分钟快速流程

### Step 1: 确定地区（1分钟）

根据公司注册地确定所属地区：

| 地区 | 语言 | 货币单位 | 会计准则 |
|------|------|----------|----------|
| 🇺🇸 美国 | 英文 | USD Millions | US GAAP |
| 🇬🇧 英国 | 英文 | GBP Millions | IFRS |
| 🇨🇳 中国 | **简体中文** | CNY Thousands | 中国GAAP |
| 🇭🇰 香港 | **繁体中文** | CNY/HKD Millions | IFRS |
| 🇸🇬 新加坡 | 英文 | SGD Millions | MFRS/IFRS |
| 🇦🇺 澳大利亚 | 英文 | AUD Millions | IFRS |
| 🇲🇾 马来西亚 | 英文 | RM Millions | MFRS |
| 🇮🇩 印尼 | 英文 | IDR Millions | Indonesian GAAP |

### Step 2: 记住三位一体（1分钟）

**语言、格式、内容必须三位一体！**

1. **语言** → 100%使用该地区语言
2. **格式** → Section 1-6全部表格
3. **内容** → 参考该地区sample深度

### Step 3: 生成报告（2分钟）

**Section 1: Company Overview**
- S1.1: 基本信息表格
- S1.2: 核心竞争力表格（Perspective | 2024 Report | 2023 Report）
- S1.3: 使命愿景表格（Field | Value/Answer）

**Section 2: Financial Performance**
- S2.1-S2.3: 财务报表（含Multiplier和Currency列）
- S2.4: 财务比率（百分比，无Multiplier列）
- S2.5: 经营业绩（产品/地区分布）

**Section 3: Business Analysis**
- S3.1: 盈利能力分析表格（Field/Perspective | Answer）
- S3.2: 财务表现总结表格（Perspective | 2024 Report | 2023 Report）
- S3.3: 业务竞争力表格（Field/Perspective | 2024 Report | 2023 Report）

**Section 4-6: 全部表格**
- S4.1: 风险因素（4个维度表格）
- S5.1-S5.2: 公司治理表格
- S6.1-S6.3: 未来展望表格

### Step 4: 质量检查（1分钟）

使用检查清单：
- [ ] ✅ 语言100%正确（英文/简体/繁体）
- [ ] ✅ Section 1-6全部表格格式
- [ ] ✅ 列标题与sample一致
- [ ] ✅ 删除Pipeline结尾说明

---

## ⚠️ 常见错误规避

### 错误1：语言混用 ❌

**错误示例**：
```markdown
## Section 4: Risk Factors  ← 英文标题
市场竞争加剧...  ← 中文内容（❌新加坡地区应该用英文）
```

**正确做法** ✅：
- 英文地区：标题和内容全部英文
- 简体中文地区：标题和内容全部简体中文
- 繁体中文地区：标题和内容全部繁体中文

### 错误2：段落格式 ❌

**错误示例**：
```markdown
### S4.1: Risk Factors

**Market Risks**: The company faces...  ← 段落格式（❌）
**Operational Risks**: Supply chain...
```

**正确做法** ✅：
```markdown
### S4.1: Risk Factors

| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Market Risks | The company faces... | ... |
| Operational Risks | Supply chain... | ... |
```

### 错误3：添加额外内容 ❌

**错误示例**：
```markdown
---

**财小析Pipeline 2.5分析完成**  ← 删除！（❌）
**预期得分**: 230+/240分  ← 删除！（❌）
```

**正确做法** ✅：
```markdown
---

（报告在Section 6结束后直接结束，不添加任何说明）
```

### 错误4：列标题错误 ❌

**错误示例（中国地区）**：
```markdown
| Perspective | 2024 Report | 2023 Report |  ← 英文列标题（❌）
```

**正确做法** ✅：
```markdown
| Perspective | 公司全称2024年年度报告 | 公司全称2023年年度报告 |  ← 中文特殊格式（✅）
```

---

## 💡 实战技巧

### 技巧1：快速识别地区

**看公司名称和年报语言**：
- 含"有限公司"、年报中文 → 中国（简体）
- 含"股份有限公司"、香港上市 → 香港（繁体）
- Ltd/PLC/Corp、年报英文 → 英文地区

### 技巧2：简繁体转换

**香港地区必须使用繁体中文**：

常见简繁对照：
- 公司 → 公司
- 业务 → 業務
- 发展 → 發展
- 管理 → 管理
- 财务 → 財務
- 报告 → 報告
- 经营 → 經營
- 竞争 → 競爭
- 风险 → 風險

### 技巧3：表格格式记忆

**记住4个风险维度**（S4.1）：
1. Market Risks
2. Operational Risks
3. Financial Risks
4. Compliance Risks

**记住6个内控要素**（S5.2）：
1. Risk assessment procedures
2. Control activities
3. Monitoring mechanisms
4. Identified material weaknesses
5. Improvements
6. Effectiveness

**记住Section 6三个子section**：
1. S6.1: Strategic Direction（3行：M&A/Tech/Restructuring）
2. S6.2: Challenges and Uncertainties（2行：Economic/Competitive）
3. S6.3: Innovation and Development Plans（2行：R&D/Products）

### 技巧4：快速检查

**3秒检查法**：
1. Ctrl+F搜索"Pipeline" → 应该找不到任何结果
2. Ctrl+F搜索"预期得分" → 应该找不到任何结果
3. 滚动查看Section 4-6 → 应该全是表格

---

## 📋 执行模板

```markdown
# Section 1: Company Overview

## S1.1: Basic Information
[表格]

## S1.2: Core Competencies
[表格 - Perspective | 2024 Report | 2023 Report]

## S1.3: Mission & Vision
[表格 - Field | Value/Answer]

---

# Section 2: Financial Performance
[5个表格：S2.1-S2.5]

---

# Section 3: Business Analysis

## S3.1: Profitability Analysis
[表格 - Field/Perspective | Answer]

## S3.2: Financial Performance Summary
[表格 - Perspective | 2024 Report | 2023 Report]

## S3.3: Business Competitiveness
[表格 - Field/Perspective | 2024 Report | 2023 Report]

---

# Section 4: Risk Factors

## S4.1: Risk Factors
[表格 - 4个风险维度]

---

# Section 5: Corporate Governance

## S5.1: Board Composition
[表格]

## S5.2: Internal Controls
[表格 - 6个内控要素]

---

# Section 6: Future Outlook

## S6.1: Strategic Direction
[表格 - 3行]

## S6.2: Challenges and Uncertainties
[表格 - 2行]

## S6.3: Innovation and Development Plans
[表格 - 2行]

---

（结束，不添加任何说明）
```

---

## 🎯 最后提醒

### 记住核心：

> **语言、格式、内容三位一体**

### 零容忍规则：

- ❌ 语言混用
- ❌ 段落格式
- ❌ Pipeline结尾说明

### 质量目标：

- ✅ 语言100%正确
- ✅ 格式100%表格
- ✅ 内容符合sample

---

*简单、直接、有效 - 5分钟掌握Pipeline 3.5* 🚀
