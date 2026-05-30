# Section 3-6: 内容质量标准与数据来源规范

> **版本**: 3.6 | **适用**: Section 3-6所有内容生成 | **优先级**: 🔴 核心规范

---

## 🎯 核心原则：高质量提炼 + 年报唯一来源

### 两大铁律

#### 铁律1：数据来源唯一性 ⭐⭐⭐

```yaml
✅ 允许的唯一数据源:
  - 提供的2024年年报MD文件
  - 提供的2023年年报MD文件
  - 以上两份年报中的所有内容
  
❌ 严禁使用:
  - 互联网搜索
  - 公司官网
  - 维基百科
  - 行业报告
  - 第三方数据库
  - 新闻报道
  - 分析师报告
  - 其他任何外部信息源
  
❌ 严禁行为:
  - 根据常识推测
  - 基于历史数据估算
  - 从其他公司类比
  - 编造数据或分析
```

#### 铁律2：高质量提炼而非复制粘贴 ⭐⭐⭐

```yaml
❌ 禁止的低质量做法:
  - 简单复制粘贴年报原文
  - 大段引用不加提炼
  - 罗列数据无逻辑
  - 重复信息无增值
  
✅ 要求的高质量做法:
  - 整合多处信息
  - 按维度逻辑组织
  - 数据+分析结合
  - 符合长度和密度要求
```

---

## 📋 Section 3: Business Analysis 质量标准

### S3.1: Profitability Analysis

**内容要求**：

| 地区 | 每行长度 | 数据点数量 | 质量要求 |
|------|---------|-----------|---------|
| 英国 | 50-80词 | 3-5个数值 | 整合+简要分析 |
| 澳洲 | 80-120词 | 6-8个数值 | 整合+深入分析 |
| 中国 | 100-150词 | 10+个数值 | 整合+详细分析 |

**高质量示例** (英国 - Revenue & Direct-Cost Dynamics)：

❌ **低质量（简单复制）**：
```
Revenue £1,912.1m in 2024. Services £1,811.2m. UK £1,265.8m.
```
- 问题：仅罗列数据，无整合，无分析

✅ **高质量（提炼整合）**：
```
Revenue grew from £1,580.7m in 2023 to £1,912.1m in 2024, up 21%. 
EMEA Services delivered 19% organic revenue growth, while Global 
Solutions revenue was up 23% (declining 3% on an organic basis). 
Revenue by customer shows UK government £1,184.9m and US government 
£389.3m in 2024. Home countries represent 94% of total revenue.
```
- 优点：
  - 整合了4处年报信息
  - 有增长率计算
  - 有逻辑（总体→分部→客户→地区）
  - 符合70词标准

**数据来源要求**：
- Revenue数据：年报Consolidated Income Statement
- 分部数据：年报Segment Performance部分
- 客户数据：年报Revenue by Customer表格
- 地区数据：年报Geographic Revenue表格

**严禁**：
- ❌ 从公司官网查询业务信息
- ❌ 从行业报告推测增长率
- ❌ 根据常识补充分析

---

### S3.2: Financial Performance Summary

**内容要求**：

| 地区 | 每行长度 | 数据密度 | 质量要求 |
|------|---------|---------|---------|
| 英国 | 150-200词 | 4-6个指标 | 综合判断+数据支撑 |
| 澳洲 | 200-250词 | 8-12个指标 | 深入分析+前瞻判断 |
| 中国 | 250-300词 | 12-15个指标 | 详细分析+多维度 |

**高质量示例** (英国 - Comprehensive financial health)：

❌ **低质量（数据堆砌）**：
```
Total assets £2,106.2m. Equity £926.1m. Current ratio 115.06%. 
D/E 127.49%.
```
- 问题：仅罗列指标，无分析，无逻辑

✅ **高质量（分析整合）**：
```
Total assets increased to £2,106.2m from £2,072.1m, though 
shareholders' equity declined to £926.1m from £968.3m due to 
dividend payments and share buyback activity. The current ratio 
improved slightly to 115.06% from 112.29%, indicating adequate 
short-term liquidity. Debt-to-equity ratio increased to 127.49% 
from 114.02%, reflecting the impact of the term loan drawn down 
to fund the Avantus acquisition. The Group maintains a strong 
balance sheet with financial flexibility for further investment, 
supported by a healthy order book with 64% of FY25 revenue under 
contract.
```
- 优点：
  - 8个财务指标
  - 解释变化原因（"due to dividend payments"）
  - 有逻辑（资产→权益→流动性→杠杆→前景）
  - 180词符合标准

**数据来源要求**：
- 资产负债表数据：年报Balance Sheet
- 变化原因：年报Management Discussion
- 未来展望：年报CEO Review或Outlook部分

**严禁**：
- ❌ 从财经网站查询财务分析
- ❌ 使用外部行业对比
- ❌ 基于宏观经济推测

---

### S3.3: Business Competitiveness

**内容要求**：
- Business Model: 40-80词，描述商业模式
- Market Position: 40-80词，市场地位+数据支撑

**高质量要求**：
```yaml
✅ 必须包含:
  - 年报Strategic Report原文提炼
  - 具体的业务描述
  - 数据支撑（市场份额、收入占比等）
  
❌ 严禁:
  - 从公司官网复制使命愿景
  - 从行业报告补充市场分析
  - 根据常识描述业务模式
```

---

## 📋 Section 4-6: 内容质量标准

### S4.1: Risk Factors

**标准结构**：4个风险类别
- Market Risks
- Operational Risks
- Financial Risks
- Compliance Risks

**每个风险40-80词**

**质量要求**：
```yaml
✅ 必须:
  - 来自年报Risk Management章节
  - 包含具体风险描述
  - 包含应对措施（如有）
  
❌ 严禁:
  - 从其他公司年报复制风险
  - 根据行业常识编造风险
  - 使用通用模板套用
```

---

### S5.1: Board Composition

**数据来源要求**：
```yaml
✅ 唯一来源:
  - 年报Directors' Remuneration Report
  - 年报Executive Compensation表格
  
❌ 严禁:
  - 从公司官网查询董事信息
  - 从LinkedIn查询职位
  - 从外部数据库查询薪酬
```

---

### S5.2: Internal Controls

**5个标准维度** (每个60-120词)

**质量要求**：
```yaml
✅ 必须:
  - 来自年报Corporate Governance Report
  - 具体描述框架和机制
  - 提及具体的委员会名称
  
❌ 严禁:
  - 使用通用内控框架描述
  - 从COSO框架套用
  - 编造内控措施
```

---

### S6.1-6.3: Future Outlook

**数据来源要求**：
```yaml
✅ 必须来自:
  - Strategic Report
  - CEO Review
  - Outlook Statement
  - Future Strategy章节
  
❌ 严禁:
  - 从公司官网查询战略
  - 从行业报告推测未来
  - 根据常识编造发展计划
```

---

## 🚨 质量检查清单

### 内容质量检查

- [ ] 每行内容符合长度要求（词数）
- [ ] 每行包含足够数据点（数量）
- [ ] 内容有逻辑组织（不是简单罗列）
- [ ] 数据+分析结合（不是单纯数据堆砌）
- [ ] 有具体判断词（strong/decline/robust等）

### 数据来源检查

- [ ] 所有数据都来自两年年报
- [ ] 没有使用任何外部信息源
- [ ] 没有根据常识推测
- [ ] 没有编造或估算数据
- [ ] 找不到的信息填N/A

### 提炼质量检查

- [ ] 不是简单复制粘贴年报原文
- [ ] 整合了多处信息
- [ ] 有提炼和归纳
- [ ] 符合地区内容深度标准

---

## 📊 质量等级评估

### 优秀 (90分+)
```
✅ 数据100%来自年报
✅ 高质量提炼整合
✅ 符合长度和密度要求
✅ 有逻辑、有分析、有判断
```

### 合格 (70-89分)
```
✅ 数据来自年报
⚠️ 提炼不够深入
⚠️ 部分内容偏简单
✅ 基本符合长度要求
```

### 不合格 (<70分)
```
❌ 使用外部数据
❌ 简单复制粘贴
❌ 长度严重不足
❌ 数据密度太低
```

---

## 🎯 核心要求总结

### 数据来源（零容忍）

**只能使用**：
- 提供的2024年年报MD文件
- 提供的2023年年报MD文件

**绝对禁止**：
- 任何外部信息源
- 任何推测或估算
- 任何编造内容

### 内容质量（高标准）

**必须做到**：
- 整合多处信息
- 按逻辑组织内容
- 数据+分析结合
- 符合长度和密度要求

**严禁做法**：
- 简单复制粘贴
- 罗列数据无逻辑
- 低质量拼凑

---

**最后强调**：

⚠️ **数据来源是红线，绝不能碰！**
⚠️ **内容质量是标准，必须达到！**
⚠️ **违反任何一条，立即返工！**

---

*版本: 3.6 | 更新日期: 2025-10-22*
