# 财小析Pipeline 3.2完整规则手册

## 版本信息
- **版本**: Pipeline 3.2
- **更新日期**: 2025-10-20
- **重大修正**: 杜绝偷懒行为，严格数据提取

## 🚨 Pipeline 3.2重大修正

### 核心问题修正
**严重问题**: S5.1 Board Composition部分存在严重偷懒行为，所有报告都填写N/A而不是提取真实数据。

**修正原则**:
1. **绝不偷懒**: 必须仔细搜索年报中的董事薪酬信息
2. **严格提取**: 只有年报中确实没有信息时才能填N/A
3. **标准执行**: 严格按照sample002标准执行
4. **地区适配**: 不同地区的薪酬披露格式需要适配

## 核心规则

### 1. 数据口径规则（绝不可违反）
- 必须使用合并净利润（含少数股东损益）
- 必须使用所有者权益合计（含少数股东权益）
- 禁止使用归母数据
- 口径必须一致性（Net Profit和Shareholders' Equity同口径）

### 2. 地区格式对应关系
- sample001 (英伟达-美国) → 美国公司案例
- sample002 (Chemring-英国) → 英国公司案例
- sample003 (宁德时代-中国) → 中国A股案例
- sample004 (待确认) → 澳大利亚案例
- sample005 (新加坡/马来西亚) → 东南亚案例
- sample006 (待确认) → 香港案例
- sample007 (待确认) → 马来西亚单独案例
- sample008 (印尼) → 印尼案例

### 3. 地区特征差异化处理

#### 🇺🇸 美国地区特征
- **货币**: 美元(USD)
- **会计准则**: US GAAP
- **报告语言**: 英文
- **Multiplier**: Millions
- **特殊处理**: Form 10-K格式，SEC规范

#### 🇨🇳 中国地区特征
- **货币**: 人民币(CNY)
- **会计准则**: 中国企业会计准则
- **报告语言**: 中文
- **Multiplier**: Thousands (大型企业用Ones)
- **特殊处理**: 归母净利润需转换为合并净利润

#### 🇬🇧 英国地区特征
- **货币**: 英镑(GBP)
- **会计准则**: IFRS
- **报告语言**: 英文
- **Multiplier**: Millions
- **特殊处理**: UK Corporate Governance Code

#### 🇸🇬 新加坡/马来西亚地区特征
- **货币**: 马来西亚林吉特(RM)
- **会计准则**: MFRS (基于IFRS)
- **报告语言**: 英文
- **Multiplier**: Millions
- **特殊处理**: PATMI概念处理

#### 🇮🇩 印尼地区特征
- **货币**: 印尼盾(IDR)
- **会计准则**: Indonesian GAAP
- **报告语言**: 英文
- **Multiplier**: Millions
- **特殊处理**: BOC和BOD薪酬合并披露

## Section格式标准

### Section 1: Company Overview

#### S1.1: Basic Information
```markdown
| Field | Value |
| :---- | :---- |
| Company Name | [公司全称] |
| Establishment Date | [成立日期或N/A] |
| Headquarters Location | [总部地址] |
```

#### S1.2: Core Competencies
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Innovation Advantages | [详细描述] | [详细描述] |
| Product Advantages | [详细描述] | [详细描述] |
| Brand Recognition | [详细描述] | [详细描述] |
| Reputation Ratings | [详细描述] | [详细描述] |
```

#### S1.3: Mission & Vision
```markdown
| Field | Value |
| :---- | :---- |
| Mission Statement | [使命声明或N/A] |
| Vision Statement | [愿景声明或N/A] |
| Core Values | [核心价值观或N/A] |
```

### Section 2: Financial Performance

#### S2.1-S2.3: 财务报表格式
```markdown
| Field | 2024 | 2023 | 2022 | Multiplier | Currency |
| :---- | :---- | :---- | :---- | :---- | :---- |
| [项目名称] | [数值] | [数值] | [数值] | [Thousands/Millions] | [货币代码] |
```

#### S2.4: Key Financial Metrics
```markdown
|  | 2024 | 2023 | 2022 |
| :---- | :---- | :---- | :---- |
| Gross Margin | XX.XX% | XX.XX% | XX.XX% |
| Operating Margin | XX.XX% | XX.XX% | XX.XX% |
| Net Profit Margin | XX.XX% | XX.XX% | XX.XX% |
| Current Ratio | XXX.XX% | XXX.XX% | XXX.XX% |
| Quick Ratio | XXX.XX% | XXX.XX% | XXX.XX% |
| Debt-to-Equity | XX.XX% | XX.XX% | XX.XX% |
| Interest Coverage | XXXX.XX% | XXXX.XX% | XXXX.XX% |
| Asset Turnover | XX.XX% | XX.XX% | N/A |
| Return on Equity | XX.XX% | XX.XX% | N/A |
| Return on Assets | XX.XX% | XX.XX% | N/A |
| Effective Tax Rate | XX.XX% | XX.XX% | XX.XX% |
| Dividend Payout Ratio | XX.XX% | XX.XX% | XX.XX% |
```

### Section 5: Corporate Governance

#### S5.1: Board Composition (🚨 重点修正)
```markdown
| Name | Position | Total Income |
| :---- | :---- | :---- |
| [董事姓名] | [职位] | [具体薪酬金额] |
| [董事姓名] | [职位] | [具体薪酬金额] |
| [董事姓名] | [职位] | [具体薪酬金额] |
```

**严格要求**:
1. 必须从年报中提取真实董事信息
2. 必须搜索remuneration/compensation/salary等关键词
3. 薪酬金额必须包含货币单位
4. 只有年报中确实没有披露时才填N/A
5. 必须注明数据来源和说明

#### S5.2: Internal Controls
必须包含6项内控要素：
1. Risk assessment procedures
2. Control activities
3. Monitoring mechanisms
4. Identified material weaknesses
5. Improvements
6. Effectiveness

## 财务指标计算公式

### 12项核心指标
1. **Gross Margin** = (Revenue-COGS)/Revenue × 100%
2. **Operating Margin** = Operating Income/Revenue × 100%
3. **Net Profit Margin** = Net Income/Revenue × 100%
4. **Current Ratio** = Current Assets/Current Liabilities × 100%
5. **Quick Ratio** = (Current Assets-Inventory-Prepaid)/Current Liabilities × 100%
6. **Debt-to-Equity** = Total Liabilities/Shareholders' Equity × 100%
7. **Interest Coverage** = Operating Income/Interest Expense × 100%
8. **Asset Turnover** = Revenue/平均总资产 × 100% (2022年N/A)
9. **ROE** = Net Income/平均股东权益 × 100% (2022年N/A)
10. **ROA** = Net Income/平均总资产 × 100% (2022年N/A)
11. **Effective Tax Rate** = Tax Expense/Income Before Tax × 100%
12. **Dividend Payout Ratio** = Dividends/Net Income × 100%

### 计算规则
- 所有指标必须计算，不能填N/A（除非数据确实缺失）
- 平均值计算：(期末+期初)/2
- 2022年缺期初数据的指标才填N/A
- 格式：百分比格式，保留2位小数

## 质量检查清单

### 🚨 Pipeline 3.2新增检查项
- [ ] S5.1是否提取了真实董事信息？
- [ ] S5.1是否搜索了薪酬相关关键词？
- [ ] S5.1薪酬金额是否包含货币单位？
- [ ] 是否避免了偷懒填写N/A？
- [ ] S1.3是否严格按照年报披露填写？
- [ ] 是否杜绝了外部信息和推理？
- [ ] 成立日期是否来自年报明确表述？
- [ ] 使命愿景是否来自年报直接披露？

### 基础检查项
- [ ] 格式是否严格按照对应sample？
- [ ] 是否移除了多余标题信息？
- [ ] Section 2是否包含Multiplier和Currency列？
- [ ] S2.4是否为纯百分比格式？
- [ ] 财务指标是否全部计算？
- [ ] 数据口径是否使用合并净利润？
- [ ] S1.2/S3.2是否为双年份对比表格？
- [ ] S5.2是否包含6项内控要素？

## 常见错误避免

### 🚨 严禁行为
1. **偷懒填写N/A** - 必须认真搜索年报数据
2. **使用外部信息** - 严禁使用年报外的任何信息源
3. **推理补充信息** - 严禁基于常识或推理填写信息
4. **格式不标准** - 必须严格按照sample格式
5. **数据口径错误** - 必须使用合并净利润
6. **财务指标缺失** - 必须计算全部12项指标

### 地区差异注意事项
- 美国：注意US GAAP特殊处理
- 中国：注意归母净利润转换
- 英国：注意IFRS标准
- 新加坡/马来西亚：注意PATMI概念
- 印尼：注意BOC/BOD薪酬合并披露

## 格式标准说明

### 🚨 核心：先确定地区，再按地区标准执行
**详细格式标准请参考《八大地区完整格式标准_3.2.md》**

#### 执行流程：
1. **确定地区** - 根据公司所在地确定使用哪个Sample
2. **查找标准** - 在《八大地区完整格式标准_3.2.md》中找到对应地区
3. **严格执行** - 按照该地区的Section 1-6所有格式要求
4. **逐项检查** - 使用快速对照表检查每个Section

#### 关键差异：
- **S1.3列标题**: 美国/香港/澳大利亚/印尼用`Value`，其他用`Answer`
- **S3.1列标题**: 美国/新加坡/马来西亚用`Field`，其他用`Perspective`
- **S3.2列标题**: 马来西亚特殊用`Perspective Column`
- **S3.3列标题**: 中国用完整公司名称+年度报告
- **中文sample**: S1.2和S3.3使用中文年度报告标题

#### 格式检查：
- [ ] 是否确定了正确的地区？
- [ ] Section 1-6是否全部使用表格格式？
- [ ] 表格列标题是否与该地区标准100%一致？
- [ ] 中文sample是否使用了正确的中文标题？

## 目标得分
- **目标**: 230+/240分（96%+）
- **质量等级**: 卓越级
- **核心**: 杜绝偷懒，严格执行标准

---

**财小析Pipeline 3.2 - 杜绝偷懒，严格执行，精准高效！** 🚀
