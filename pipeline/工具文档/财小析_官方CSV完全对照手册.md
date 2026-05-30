# 财小析官方CSV完全对照手册

**版本**: 2.2  
**更新时间**: 2025-10-20  
**基于**: 官方CSV文件 + 样本集验证

---

## 📋 Section 1: Company Overview

### S1.1 Basic Information

| CSV字段 | 字段说明 | 数据类型 | 必填 | 样本集格式 | 财小析规则 |
|---------|----------|----------|------|------------|------------|
| Company Name | 公司名称 | Text | ✅ | 完整法定名称 | 使用年报封面完整名称 |
| Establishment Date | 成立日期 | Date/Text | ✅ | YYYY或YYYY-MM-DD或N/A | 优先完整日期，可简化为年份 |
| Headquarters Location | 总部地址 | Text | ✅ | City, Country | "城市, 国家"格式 |

### S1.2 Core Competencies

| CSV字段 | 字段说明 | 数据类型 | 必填 | 样本集格式 | 财小析规则 |
|---------|----------|----------|------|------------|------------|
| Innovation Advantages | 创新优势 | Text | ✅ | 双年份对比表 | 100-300字/年，含具体技术数据 |
| Product Advantages | 产品优势 | Text | ✅ | 双年份对比表 | 100-300字/年，含产品收入占比 |
| Brand Recognition | 品牌认知 | Text | ✅ | 双年份对比表 | 100-300字/年，含品牌价值排名 |
| Reputation Ratings | 声誉评级 | Text | ✅ | 双年份对比表 | 100-300字/年，含具体奖项评级 |

### S1.3 Mission & Vision

| CSV字段 | 字段说明 | 数据类型 | 必填 | 样本集格式 | 财小析规则 |
|---------|----------|----------|------|------------|------------|
| Mission Statement | 使命宣言 | Text | ✅ | 原文或N/A | 严格N/A策略，禁止自行提炼 |
| Vision Statement | 愿景宣言 | Text | ✅ | 原文或N/A | 严格N/A策略，禁止自行提炼 |
| Core Values | 核心价值观 | Text | ✅ | 原文或N/A | 严格N/A策略，注意复数形式 |

---

## 📊 Section 2: Financial Performance

### S2.1 Income Statement

| CSV字段 | 字段说明 | 数据类型 | 必填 | 财小析提取规则 |
|---------|----------|----------|------|----------------|
| Revenue | 营业收入 | Number | ✅ | grep("营业收入")，不含利息收入 |
| COGS | 营业成本 | Number | ✅ | grep("营业成本")，无则填N/A |
| Gross Profit | 毛利润 | Number | ✅ | Revenue - COGS，COGS为N/A则N/A |
| Operating Expenses | 营业费用 | Number | ✅ | 销售费用+管理费用+研发费用+税金及附加 |
| Operating Income | 营业利润 | Number | ✅ | grep("营业利润") |
| Net Income | 净利润 | Number | ✅ | ⭐grep("合并净利润")，含少数股东损益 |
| Income before taxes | 税前利润 | Number | ✅ | grep("利润总额") |
| Income tax expense | 所得税费用 | Number | ✅ | grep("所得税费用") |
| Interest Expense | 利息费用 | Number | ✅ | grep("利息费用")，非财务费用 |

### S2.2 Balance Sheet

| CSV字段 | 字段说明 | 数据类型 | 必填 | 财小析提取规则 |
|---------|----------|----------|------|----------------|
| Total Assets | 资产总计 | Number | ✅ | grep("资产总计") |
| Current Assets | 流动资产 | Number | ✅ | grep("流动资产合计") |
| Non-current Assets | 非流动资产 | Number | ✅ | grep("非流动资产合计") |
| Total Liabilities | 负债合计 | Number | ✅ | grep("负债合计") |
| Current Liabilities | 流动负债 | Number | ✅ | grep("流动负债合计") |
| Non-current Liabilities | 非流动负债 | Number | ✅ | grep("非流动负债合计") |
| Shareholders' Equity | 股东权益 | Number | ✅ | ⭐grep("所有者权益合计")，含少数股东 |
| Retained Earnings | 未分配利润 | Number | ✅ | grep("未分配利润") |
| Total Equity and Liabilities | 权益负债总计 | Number | ✅ | 负债合计+所有者权益合计 |
| Inventories | 存货 | Number | ✅ | grep("存货") |
| Prepaid Expenses | 预付费用 | Number | ✅ | grep("预付款项") |

### S2.3 Cash Flow Statement

| CSV字段 | 字段说明 | 数据类型 | 必填 | 财小析提取规则 |
|---------|----------|----------|------|----------------|
| Operating Cash Flow | 经营现金流 | Number | ✅ | grep("经营活动产生的现金流量净额") |
| Investing Cash Flow | 投资现金流 | Number | ✅ | grep("投资活动产生的现金流量净额") |
| Financing Cash Flow | 筹资现金流 | Number | ✅ | grep("筹资活动产生的现金流量净额") |
| Net Increase in Cash | 现金净增加 | Number | ✅ | grep("现金及现金等价物净增加额") |
| Dividends | 股利支付 | Number | ✅ | grep("对股东的分配")，实际支付额 |

### S2.4 Key Metrics

| CSV字段 | 计算公式 | 数据类型 | 必填 | 财小析格式要求 |
|---------|----------|----------|------|----------------|
| Gross Margin | (Revenue-COGS)/Revenue | Percentage | ✅ | 百分比格式：72.71% |
| Operating Margin | Operating Income/Revenue | Percentage | ✅ | 百分比格式：29.00% |
| Net Profit Margin | Net Income/Revenue | Percentage | ✅ | 百分比格式：24.70% |
| Current Ratio | Current Assets/Current Liabilities | Percentage | ✅ | 百分比格式：417.13% |
| Quick Ratio | (CA-Inventory-Prepaid)/CL | Percentage | ✅ | 百分比格式：338.47% |
| Interest Coverage | Operating Income/Interest Expense | Percentage | ✅ | 百分比格式：12829.57% |
| Asset Turnover | Revenue/平均总资产 | Percentage | ✅ | 百分比格式：113.97%或N/A |
| Debt-to-Equity | Total Liabilities/Shareholders' Equity | Percentage | ✅ | 百分比格式：52.93% |
| ROE | Net Income/平均股东权益 | Percentage | ✅ | 百分比格式：91.46%或N/A |
| ROA | Net Income/平均总资产 | Percentage | ✅ | 百分比格式：55.67%或N/A |
| Effective Tax Rate | Tax Expense/Income Before Tax | Percentage | ✅ | 百分比格式：12.00% |
| Dividend Payout Ratio | Dividends/Net Income | Percentage | ✅ | 百分比格式：1.33% |

### S2.5 Operating Performance

| CSV字段 | 字段说明 | 数据类型 | 必填 | 财小析提取规则 |
|---------|----------|----------|------|----------------|
| Revenue by Product/Service | 分产品收入 | Text | ✅ | 3年数据，优先从对比表获取 |
| Revenue by Geography | 分地区收入 | Text | ✅ | 3年数据，优先从对比表获取 |

---

## 📝 Section 3: Business Analysis

### S3.1 Financial Analysis

| CSV字段 | 字段说明 | 格式要求 | 财小析规则 |
|---------|----------|----------|------------|
| Revenue Dynamics | 收入动态分析 | 单列表格 | 200-400字，含增长率/占比 |
| Operating Efficiency | 运营效率分析 | 单列表格 | 150-300字，含利润率/费用率 |
| External Impact | 外部影响分析 | 单列表格 | 150-300字，含税率/非经常性项目 |

### S3.2 Profitability Analysis

| CSV字段 | 字段说明 | 格式要求 | 财小析规则 |
|---------|----------|----------|------------|
| Profitability Metrics | 盈利能力指标 | 双年份表格 | 150-250字/年，含具体数据 |
| Cost Management | 成本管理 | 双年份表格 | 150-250字/年，含成本率变化 |
| Revenue Quality | 收入质量 | 双年份表格 | 150-250字/年，含收入结构 |
| Margin Analysis | 利润率分析 | 双年份表格 | 150-250字/年，含同比变化 |
| Efficiency Ratios | 效率比率 | 双年份表格 | 150-250字/年，含周转率 |

### S3.3 Business Model Analysis

| CSV字段 | 字段说明 | 格式要求 | 财小析规则 |
|---------|----------|----------|------------|
| Business Model | 商业模式 | 双年份表格 | 150-250字/年，含盈利来源 |
| Market Position | 市场地位 | 双年份表格 | 150-250字/年，含市场份额 |

---

## 🚨 Section 4: Risk Assessment

### S4.1 Risk Assessment

| CSV字段 | 字段说明 | 格式要求 | 财小析规则 |
|---------|----------|----------|------------|
| Market Risk | 市场风险 | 双年份表格 | 80-200字/年，含具体风险点 |
| Operational Risk | 运营风险 | 双年份表格 | 80-200字/年，含应对措施 |
| Financial Risk | 财务风险 | 双年份表格 | 80-200字/年，含风险指标 |
| Compliance Risk | 合规风险 | 双年份表格 | 80-200字/年，含监管要求 |

---

## 🏛️ Section 5: Corporate Governance

### S5.1 Board Composition

| CSV字段 | 字段说明 | 格式要求 | 财小析规则 |
|---------|----------|----------|------------|
| Name | 姓名 | Text | 3-8人，含主要董事 |
| Position | 职位 | Text | 合并多重职务 |
| Total Income | 总收入 | Number/Text | 尽量完整，未披露填N/A |

### S5.2 Internal Controls

| CSV字段 | 字段说明 | 格式要求 | 财小析规则 |
|---------|----------|----------|------------|
| Risk Assessment | 风险评估 | 双年份表格 | 80-150字/年 |
| Control Activities | 控制活动 | 双年份表格 | 80-150字/年 |
| Monitoring | 监督机制 | 双年份表格 | 80-150字/年 |
| Weaknesses | 重大缺陷 | 双年份表格 | 80-150字/年 |
| Improvements | 改进措施 | 双年份表格 | ⭐80-150字/年，必须第5项 |
| Effectiveness | 有效性 | 双年份表格 | 80-150字/年 |

---

## 🔮 Section 6: Future Outlook

### S6.1 Strategic Direction

| CSV字段 | 字段说明 | 格式要求 | 财小析规则 |
|---------|----------|----------|------------|
| M&A Activities | 并购活动 | 双年份表格 | 80-200字/年，含具体案例 |
| Technology Advancement | 技术进步 | 双年份表格 | 80-200字/年，含投入金额 |
| Organizational Restructuring | 组织重构 | 双年份表格 | 80-200字/年，含具体措施 |

### S6.2 Challenges

| CSV字段 | 字段说明 | 格式要求 | 财小析规则 |
|---------|----------|----------|------------|
| Economic Environment | 经济环境 | 双年份表格 | 80-200字/年，含影响分析 |
| Competitive Landscape | 竞争格局 | 双年份表格 | 80-200字/年，含竞争对手 |

### S6.3 Innovation Plans

| CSV字段 | 字段说明 | 格式要求 | 财小析规则 |
|---------|----------|----------|------------|
| R&D Investments | 研发投资 | 双年份表格 | 80-200字/年，含具体金额 |
| New Product Development | 新产品开发 | 双年份表格 | 80-200字/年，含产品名称 |

---

## 🎯 格式规范总结

### 表格格式
```
双年份表格标准格式:
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |

单列表格标准格式:
| Perspective | Analysis |
| :---- | :---- |

三列表格标准格式(S5.1):
| Name | Position | Total Income |
| :---- | :---- | :---- |
```

### 数值格式
```
财务数据格式:
- 千分位逗号: 89,175,178
- 负数格式: -185,194
- 小数位数: 保留2位
- 单位标注: Multiplier + Currency

百分比格式:
- 统一格式: 24.70%
- 禁止倍数: 2.47x
- 保留2位小数
```

### 文本格式
```
N/A使用:
- 年报无披露: N/A
- 无法计算: N/A
- 禁止估算

字数要求:
- S1.2: 100-300字/年
- S3.1: 150-400字
- S3.2: 150-250字/年
- S4-S6: 80-200字/年
- S5.2: 80-150字/年
```

---

**财小析官方CSV完全对照手册 - 确保100%合规！** 📋
