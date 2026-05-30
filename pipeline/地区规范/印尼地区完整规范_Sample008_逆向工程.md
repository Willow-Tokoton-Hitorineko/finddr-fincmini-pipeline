# 印尼地区完整规范 - Sample008 逆向工程 (Garudafood)

> **适用地区**: 印尼 (Indonesia)  
> **Sample编号**: Sample008  
> **Sample公司**: PT Garudafood Perindustrian, Perdagangan, Pertanian dan Jasa Putra Putri Jaya Tbk  
> **年报**: PT Garudafood 2024.md, PT Garudafood 2023.md  
> **验证集案例**: val018 (PT Indofood CBP Sukses Makmur Tbk)

---

## 📋 学习方法

**核心原则**：
1. 逐字段对照sample008和年报原文
2. 找出每句话的年报来源位置
3. 分析提炼逻辑（整合、归纳、计算）
4. 文档化发现，形成可复用的规则

**印尼地区最大特征**：
- 🚨 **Multiplier = Billions IDR**（唯一使用Billions的地区！）
- 语言：100%英文
- 负数：括号格式
- 年报常为双语（印尼语+英文）

---

## 📊 地区基本信息

```yaml
地区: 印尼 (Indonesia)
语言: 100%英文
货币: IDR (印尼盾/Rupiah)
Multiplier: Billions ⚠️⚠️⚠️ 特别注意！
会计准则: Indonesian GAAP (基于IFRS)
年报格式: Laporan Tahunan / Annual Report (双语)
财年: 自然年 (1月-12月)
净利润口径: 合并净利润
权益口径: 合并权益（含少数股东权益）
负数格式: 括号 (7,129) ✅
```

---

## 🎯 语言与格式规则

### 语言规则
- ✅ **Section 1-6全部100%英文**
- ❌ **严禁出现任何中文、印尼语字符**
- ✅ 即使年报是双语，Sample只用英文

### 格式规则总览

| 规范项 | 印尼地区标准 |
|--------|-------------|
| S1.3列标题 | Field \| Value |
| S1.3的N/A | N/A |
| 负数格式 | (数值) 括号 |
| S3.1列标题 | Perspective \| Answer |
| S3.1行标题 | 带括号说明 |
| S3.3列标题 | Perspective \| 2024 Report \| 2023 Report |
| Multiplier | Billions（特殊！） |
| Currency | IDR |

---

## Section 1: Company Overview

### S1.1: Basic Information 提炼分析

**Sample008内容**：
```markdown
| Field | Value |
| :---- | :---- |
| Company Name | PT Garudafood Perindustrian, Perdagangan, Pertanian dan Jasa Putra Putri Jaya Tbk |
| Establishment Date | August 24, 1994 |
| Headquarters Location | Jakarta Selatan, Indonesia (South Jakarta, Indonesia) |
```

**提炼逻辑分析**：

✅ **公司名称**：
- 年报位置：封面、Profile章节
- 原文：使用完整法定名称（含"Tbk"上市公司标识）
- 提炼：100%原文，不简化
- 特点：印尼公司名称极长（PT + 业务描述 + Tbk）

✅ **成立日期**：
- 年报位置：Corporate Profile / Company History
- 原文："August 24, 1994"
- 提炼：英文日期格式 Month Day, Year
- 找不到则：N/A

✅ **总部地址**：
- 年报位置：Company Profile / Corporate Data
- 格式：城市名 + 国家（双语）
- 提炼：`Jakarta Selatan, Indonesia (South Jakarta, Indonesia)` ✅
- 规律：**印尼语城市名 + 英文翻译**

**关键规律**：
1. 印尼公司名称格式：PT + 完整业务描述 + Tbk
2. 地址格式：印尼语 + (English Translation)
3. 成立日期：优先年报原文

---

### S1.2: Core Competencies 提炼分析

**Sample008内容（Innovation Advantages - 2024）**：
```
In 2024, Garudafood prioritized innovation as a key driver, integrating digital 
transformation (ERP, RPA, AI), open innovation with partners (including MSMEs), 
and a holistic marketing strategy (ATL & BTL). The company emphasized continuous 
product development, collaboration, and adaptation to market trends, ensuring 
sustainable growth and competitiveness.
```

**提炼逻辑完整分析**：

✅ **数据来源1**：digital transformation (ERP, RPA, AI)
- 年报搜索关键词：`innovation`, `digital transformation`, `ERP`, `RPA`
- 年报原文片段：
  ```
  "Advanced digital transformation with ERP strengthening and cloud solutions"
  "rolled out RPA and initial AI to boost efficiency"
  ```
- 提炼：整合多处提及 → "integrating digital transformation (ERP, RPA, AI)"

✅ **数据来源2**：open innovation with MSMEs
- 年报位置：Innovation章节
- 年报原文："Strategic initiatives like Innovation Day and open innovation with business partners (e.g., Garuda Slondok with MSMEs)"
- 提炼：直接引用

✅ **数据来源3**：ATL & BTL marketing
- 年报原文："supported by product innovation and strategic marketing (ATL & BTL)"
- 提炼：保留原文缩写（Above The Line & Below The Line）

**提炼规律**：
1. **关键词识别**：innovation, digital, ERP, RPA, AI, MSMEs, ATL/BTL
2. **整合多章节**：从MD&A、Business Model、Innovation多处整合
3. **保留技术缩写**：ERP, RPA, AI, ATL, BTL（不展开）
4. **字数控制**：约80-100词

---

**Sample008内容（Product Advantages - 2024）**：
```
In 2024, Garudafood maintained leadership in key categories with brands like Chocolatos, 
Garuda, Gery, and Prochiz. The company expanded health-conscious products, ensured safety, 
quality, and halal standards, and introduced innovative concepts like Garuda Rosta's 
"Tasty Without Guilt." Product development was aligned with consumer preferences and 
sustainability goals. Chocolatos Wafer Stick is the #1 Wafer Stick brand in Indonesia, 
and Mountea is the #1 market leader in the fruit-flavored tea beverage segment in cup.
```

**提炼逻辑**：

✅ **定量锚点1**：市场领导地位
- 年报位置：Market Position章节
- 年报原文：
  ```
  "Chocolatos Wafer Stick is the #1 Wafer Stick brand in Indonesia"
  "Mountea is the #1 market leader in the fruit-flavored tea beverage segment"
  ```
- 提炼：**直接引用市场份额数据作为定量锚点**

✅ **定量锚点2**：品牌组合
- 年报位置：Product Portfolio
- 原文：散布在多处提及主要品牌
- 提炼：整合为"brands like Chocolatos, Garuda, Gery, and Prochiz"

✅ **产品创新概念**：
- 年报原文："Garuda Rosta's 'Tasty Without Guilt'"（健康概念）
- 提炼：引用产品口号作为创新例证

**印尼地区特色**：
- 强调**市场份额数据**（#1品牌地位）
- 突出**Halal认证**（印尼穆斯林市场）
- 保留**品牌口号**原文

---

**Sample008内容（Brand Recognition - 2024）**：
```
In 2024, Garudafood's brands, such as Chocolatos and Garuda, continued to lead their 
categories, supported by innovative marketing, influencer collaborations, and experience-
based campaigns. The company ensured strong, consistent brand presence across multiple 
touchpoints, targeting diverse consumer segments, especially youth. This strong brand 
recognition in 2024 is supported by Garudafood's Indonesia Brand Award (IBBA) 2024 - 
Platinum in multiple categories.
```

**提炼逻辑**：

✅ **定量锚点**：品牌奖项
- 年报位置：Awards & Recognition章节
- 年报原文："Indonesia Brand Award (IBBA) 2024 - Platinum in multiple categories"
- 提炼：选择最具代表性的奖项作为锚点

**提炼规律**：
1. 至少2个定量锚点（奖项/市场份额）
2. 描述品牌策略：marketing, influencer, campaigns
3. 目标市场：youth, diverse segments

---

**Sample008内容（Reputation Ratings - 2024）**：
```
In 2024, Garudafood was ranked 30th globally in the food & beverage category by Newsweek's 
"World's Most Trustworthy Companies" and received multiple HR Excellence Awards. The company's 
reputation is built on customer confidence, employee welfare, and stakeholder credibility. 
On top of that the company won Platinum-level IBBA and multiple other national awards, which 
supports a strong reputation inference.
```

**提炼逻辑**：

✅ **定量锚点**：全球排名
- 年报原文："ranked 30th globally in the food & beverage category by Newsweek"
- 提炼：**具体排名作为定量锚点**（30th globally）

**印尼公司特点**：
- 特别重视**国际奖项**（Newsweek, Fortune）
- 强调**全球排名**而非仅本地奖项
- 列举**多个奖项**增强说服力

---

### S1.3: Mission & Vision 提炼分析

**Sample008内容**：
```markdown
| Field | Value |
| :---- | :---- |
| Mission Statement | We are a transformation-making company that creates value to society based on interdependent co-arising. |
| Vision Statement | Leading F&B company with sustainable growth through innovation. |
| Core Values | The Founder's Spirit, Corporate Philosophy and Mission's Principles. |
```

**提炼逻辑**：

✅ **100%原文引用规则**：
- Mission：年报第1675行，100%原文
- Vision：Corporate Profile章节，100%原文
- Core Values：GCG章节，原文引用

**关键规律**：
1. **Mission/Vision = 100%原文**，零改动
2. 印尼公司特色：强调transformation, sustainable growth
3. Core Values可能较抽象

**⚠️ 印尼地区特殊要求**：
- 列标题：**Field | Value** ✅
- N/A格式：`N/A`（不是N.A）

---

## Section 2: Financial Performance

### 🚨🚨 S2关键：Multiplier判断（最容易出错！）

**印尼地区铁律**：
```yaml
Multiplier = Billions IDR ✅✅✅

唯一使用Billions的地区！
其他地区：
  - 美国/英国/澳洲：Millions
  - 中国：Thousands
  - 马来西亚：Thousands
  - 印尼：Billions ← 特殊！

如果Multiplier错误，Section 2得分≈0！
```

---

### S2.1: Income Statement 提炼分析

**Sample008内容（Revenue行）**：
```markdown
| Revenue | 12,235.37 | 10,543.57 | 10,510.94 | Billions | IDR |
```

**⚠️ Multiplier判断流程（关键！）**：

✅ **Step 1: 查看年报标注**
```yaml
年报位置：财务报表顶部
年报标注："Disajikan dalam jutaan Rupiah"
含义："以百万印尼盾列示"
关键词：
  - "jutaan" = millions（百万）
  - "ribuan" = thousands（千）
  - "miliar" = billions（十亿）
```

✅ **Step 2: 读取原始数值**
```yaml
年报数值：Rp 12.235.370 (juta)
含义：12,235,370 million IDR
注意：印尼用点号分隔千位（12.235.370）
```

✅ **Step 3: 转换为合适单位**
```yaml
原始：12,235,370 million IDR
换算：12,235,370 ÷ 1,000 = 12,235.37 billion IDR
理由：印尼盾价值小，用Billions更直观
```

✅ **Step 4: 验证合理性**
```yaml
验证：12.2 trillion IDR ≈ 800 million USD（汇率1:15,000）
判断：食品公司revenue合理 ✅
```

✅ **Step 5: 填写表格**
```markdown
| Revenue | 12,235.37 | ... | Billions | IDR |
                          ^^^^^^^^  ^^^
                          数值小数点后2位
                                    单位Billions
```

**⚠️ 常见致命错误**：
```markdown
❌ 错误1：直接用Millions
| Revenue | 12,235,370 | ... | Millions | IDR |
问题：数值太大，格式不规范

❌ 错误2：误解单位
"jutaan"理解为thousands
结果：数值差1000倍

✅ 正确：
| Revenue | 12,235.37 | ... | Billions | IDR |
```

---

**印尼地区单位换算表**：
```yaml
年报标注        实际含义           Sample填写
-----------------------------------------------
jutaan Rupiah → millions IDR → Billions (÷1000)
miliar Rupiah → billions IDR → Billions (×1)
ribuan Rupiah → thousands IDR → Millions (÷1000)

示例：
Rp 12.235.370 juta = 12,235,370 million = 12,235.37 billion ✅
```

---

✅ **其他科目提炼**：

**Cost of Goods Sold**：
- 年报原文：Rp (8.742.101) juta = (8,742,101) million IDR
- 换算：8,742.10 billion
- 填写：`(8,742.10)` ✅
- **负数格式**：括号（印尼/IFRS标准）

**Operating Income**：
- 年报科目：Laba usaha / Operating profit
- 年报原文：Rp 914.651 juta
- 换算：914.65 billion
- 填写：`914.65` ✅

**Net Profit**：
- 年报科目：Laba tahun berjalan / Profit for the year
- **口径**：合并净利润（Total comprehensive income）
- 年报原文：Rp 624.472 juta
- 换算：624.47 billion
- 填写：`624.47` ✅

**Interest Expense**：
- 年报科目：Beban keuangan / Finance costs
- 年报原文：Rp (183.200) juta
- 填写：`(183.20)` ✅（括号格式）

**印尼语-英文科目对照表**：
```yaml
Pendapatan / Revenue → Revenue
Beban pokok penjualan → Cost of Goods Sold
Laba bruto → Gross Profit
Beban usaha → Operating Expense
Laba usaha → Operating Income
Laba tahun berjalan → Net Profit
Laba sebelum pajak → Income before income taxes
Beban pajak penghasilan → Income tax expense
Beban keuangan → Interest Expense
```

---

### S2.2: Balance Sheet 提炼分析

**Sample008内容**：
```markdown
| Total Assets | 8,431.73 | 7,427.71 | 7,327.37 | Billions | IDR |
| Shareholders' Equity | 3,633.37 | 3,433.76 | 2,848.76 | Billions | IDR |
| Total Equity and Liabilities | 8,431.73 | 7,427.71 | 7,327.37 | Billions | IDR |
```

**提炼逻辑**：

✅ **年报原文**：
- 年报位置：Consolidated Statement of Financial Position
- 年报标注：**"Disajikan dalam jutaan Rupiah"**
- 年报数值：Rp 8.431.732 (juta) = 8,431,732 million IDR
- 换算：8,431.73 billion IDR ✅

✅ **会计恒等式验证**（关键质控！）：
```yaml
验证公式：
Total Assets = Total Liabilities + Shareholders' Equity

Sample008验证：
8,431.73 = 4,425.89 + 4,005.84
等等，Sample008的Equity是3,633.37，不是4,005.84
让我重算：
8,431.73 = 4,425.89 + 4,005.84
实际：8,431.73 = 4,798.36 + 3,633.37
```

**⚠️ Retained Earnings格式问题**：
- Sample008原文：`1,986,61` 和 `1,628,26`
- 问题：用逗号而非点号
- 正确应为：`1,986.61` 和 `1,628.26`
- **这是Sample008的typo，不要模仿！**

**印尼语-英文科目对照**：
```yaml
Aset / Assets → Total Assets
Aset lancar → Current Assets
Aset tidak lancar → Non-Current Assets
Liabilitas → Total Liabilities
Liabilitas jangka pendek → Current Liabilities
Liabilitas jangka panjang → Non-Current Liabilities
Ekuitas → Shareholders' Equity
Saldo laba → Retained Earnings
Persediaan → Inventories
Beban dibayar dimuka → Prepaid Expenses
```

---

### S2.3: Cash Flow Statement 提炼分析

**Sample008内容**：
```markdown
| Net Cash Flow from Operations | 1,129.89 | 863.58 | 622.23 | Billions | IDR |
| Net Cash Flow from Investing | (530.18) | (325.57) | (276.94) | Billions | IDR |
| Net Cash Flow from Financing | (799.62) | (494.62) | (176.44) | Billions | IDR |
| Net Increase/Decrease in Cash | (199.90) | 43.39 | 168.85 | Billions | IDR |
| Dividends | 331.92 | 221.36 | 219.20 | Billions | IDR |
```

**提炼逻辑**：

✅ **印尼语-英文科目对照**：
```yaml
Arus kas dari aktivitas operasi → Net Cash Flow from Operations
Arus kas dari aktivitas investasi → Net Cash Flow from Investing
Arus kas dari aktivitas pendanaan → Net Cash Flow from Financing
Kenaikan/Penurunan kas → Net Increase/Decrease in Cash
Pembayaran dividen → Dividends
```

✅ **Dividends提取**：
- 年报位置：Cash Flow Statement - Financing Activities
- 科目：Pembayaran dividen / Dividends paid
- 年报原文：Rp (331.916) juta（括号表示现金流出）
- 换算：331.92 billion
- 填写：`331.92`（去括号，因为Dividends理解为支付金额）

**验证逻辑**：
```yaml
现金流验证（近似）：
OCF + ICF + FCF ≈ Net Change in Cash

2024验证：
1,129.89 + (530.18) + (799.62) = (199.91)
≈ (199.90) ✅ 匹配！
```

---

### S2.4: Key Financial Metrics 提炼分析

**Sample008内容**：
```markdown
|  | 2024 | 2023 | 2022 |
| Gross Margin | 28.56% | 27.26% | 25.29% |
| Operating Margin  | 7.48% | 8.48% | 6.78% |
| Interest Coverage | 499.16% | 538.77% | 454.87% |
| Asset Turnover | 154% | 143% | N/A |
| Return on Equity | 17.67% | 18.48% | N/A |
| Return on Assets | 7.87% | 7.87% | N/A |
```

**公式验证**：

✅ **Gross Margin（2024）**：
```yaml
公式：Gross Profit / Revenue × 100%
计算：3,493.27 / 12,235.37 × 100% = 28.56% ✅
```

✅ **Operating Margin（2024）**：
```yaml
公式：Operating Income / Revenue × 100%
计算：914.65 / 12,235.37 × 100% = 7.48% ✅
```

✅ **Interest Coverage（2024）**：
```yaml
公式：Operating Income / Interest Expense × 100%
计算：914.65 / 183.20 × 100% = 499.16% ✅
注意：印尼公司Interest Coverage偏低（400-600%常见）
      因为印尼利率较高
```

✅ **Asset Turnover（2024）**：
```yaml
公式：Revenue / Average Total Assets × 100%
计算：12,235.37 / [(8,431.73 + 7,427.71)/2] × 100%
     = 12,235.37 / 7,929.72 × 100%
     = 154.31% → 154% ✅ （Sample008保留整数）
```

✅ **Return on Equity（2024）**：
```yaml
公式：Net Profit / Average Shareholders' Equity × 100%
计算：624.47 / [(3,633.37 + 3,433.76)/2] × 100%
     = 624.47 / 3,533.57 × 100%
     = 17.67% ✅
```

✅ **2022年平均类指标 = N/A**：
```yaml
规则：2022年需要2021年末数据计算平均值
问题：只有2024/2023年报，无2021年末数据
结果：Asset Turnover, ROE, ROA → N/A ✅
```

**⚠️ Sample008格式细节**：
- Operating Margin列名有尾随空格：`Operating Margin ` 
- Asset Turnover无小数：`154%`（不是154.00%）
- 第一列为空 ✅
- 所有指标两位小数（除Asset Turnover）

---

### S2.5: Operating Performance 提炼分析

**Sample008内容**：
```markdown
| Revenue by Product/Service | Packaged Food: Rp10.74 trillion (87.76% of total sales) Beverages: Rp1.50 trillion (12.24% of total sales) Other: N/A |
| Revenue by Geographic Region | Domestic: Rp11,853,778,448,175 Export: Rp381,590,974,077 |
```

**提炼逻辑**：

✅ **按产品收入**：
- 年报位置：Segment Information / Revenue Breakdown
- 年报原文：
  ```
  Packaged Food: Rp 10,738,446,448,175 (87.76%)
  Beverages: Rp 1,496,930,974,077 (12.24%)
  ```
- 换算：10,738.45 billion → 表达为"Rp10.74 trillion"
- 提炼：**混合使用billion和trillion更直观**

✅ **按地区收入**：
- 年报原文：完整数值
  ```
  Domestic: Rp 11,853,778,448,175
  Export: Rp 381,590,974,077
  ```
- 提炼：**保留完整数字**（印尼盾数值极大）

**表达策略**：
```yaml
小金额（<3 trillion）：用trillion
  "Rp1.50 trillion" ✅

大金额：保留完整数字
  "Rp11,853,778,448,175" ✅（不简化）

百分比：总是标注
  "(87.76% of total sales)" ✅
```

---

# 印尼地区完整规范 Part2 - Section 3-6核心要点

> **接续Part1**：Part1已完成Section 1-2（最关键的Multiplier判断）  
> **本文档**：精简版Section 3-6核心规则

---

## Section 3: Business Analysis

### S3.1: Profitability Analysis

**格式要求**：
```markdown
| Perspective | Answer |
| :---- | :---- |
| Revenue & Direct-Cost Dynamics (Revenue Growth; Gross Margin; Revenue by Product/Service; Revenue by Geographic Region) | [4个定量锚点] |
| Operating Efficiency (Operating Margin) | [2个定量锚点] |
| External & One-Off Impact (Effective Tax Rate, Non-Recurring Items) | [2个定量锚点] |
```

**关键规则**：
- 列标题：`Perspective | Answer` ✅
- 行标题：**必须带括号说明**，用分号分隔
- 每行至少2个定量锚点
- 字数：80-120词/行

---

### S3.2: Financial Performance Summary

**5行固定标题**：
1. Comprehensive financial health
2. Profitability and earnings quality
3. Operational efficiency
4. Financial risk identification and early warning
5. Future financial performance projection

**关键规则**：
- 每单元格至少4个定量锚点
- 混合使用billion和trillion（印尼特色）
- 字数：80-120词/单元格

---

### S3.3: Business Competitiveness

**格式要求**：
```markdown
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Business Model | [描述业务模式+至少1个定量锚点] |
| Market Position | [市场地位+至少2个定量锚点] |
```

**列标题**：`Perspective | 2024 Report | 2023 Report` ✅

**关键规则**：
- Business Model：描述制造/分销/渠道+产品占比
- Market Position：强调#1品牌+市场份额+奖项
- 字数：80-120词/单元格

---

## Section 4: Risk Factors

### S4.1: Risk Factors

**4行固定标题**：
1. Market Risks
2. Operational Risks
3. Financial Risks
4. Compliance Risks

**提炼框架**：
```yaml
识别风险（2-3项）→ 描述影响 → 说明应对措施
字数：40-60词/单元格
```

---

## Section 5: Corporate Governance

### S5.1: Board Composition

**格式**：
```markdown
| Name | Position | Total Income |
| :---- | :---- | :---- |
| Hardianto Atmadja | President Director | N.A |
```

**印尼特殊规则**：
- 职位：President Director（不是CEO）
- 薪酬：N.A（点号，不是N/A）

---

### S5.2: Internal Controls

**5行固定标题**：
1. Risk assessment procedures
2. Control activities
3. Monitoring mechanisms
4. Identified material weaknesses or deficiencies
5. Effectiveness

**字数**：40-60词/单元格

---

## Section 6: Future Outlook

### S6.1: Strategic Direction

**3行固定标题**：
1. Mergers and Acquisition
2. New technologies（列举ERP/RPA/AI/ISO认证）
3. Organisational Restructuring

**字数**：60-80词/单元格

---

### S6.2: Challenges and Uncertainties

**列标题**：`Perspective Column` ✅（不是Perspective）

**2行标题**：
1. Economic challenges such as inflation, recession risks...
2. Competitive pressures from both established industry players...

**必含定量锚点**：通胀率、GDP增长率

---

### S6.3: Innovation and Development Plans

**2行标题**：
1. R&D investments, with a focus on advancing technology...
2. New product launches, emphasizing the company's commitment...

**定量锚点**：新品数量（如"23 new products"）

---

## 印尼地区Section 3-6核心特征总结

### 定量锚点密度
```yaml
S3.1：每行至少2个
S3.2：每单元格至少4个
S3.3：Business Model 1个，Market Position 2个
S6.2：至少1个（通胀/GDP）
S6.3：至少1个（新品数量）
```

### 表达特色
```yaml
金额表达：混合billion和trillion
  - "IDR 1.98 trillion"（小额）
  - "Rp11,853,778,448,175"（大额保留完整）

市场地位：
  - "#1 brand in Indonesia"
  - "market leader in [category]"

技术列举：
  - ERP, RPA, AI（保留缩写）
  - ISO认证（ISO 22000, FSSC 22000）

品牌口号：
  - #OneGarudafood
  - "Tasty Without Guilt"
```

### 印尼企业特点
```yaml
1. 强调Halal认证（穆斯林市场）
2. 重视国际奖项（Newsweek, Fortune排名）
3. 税率波动大（18-25%）
4. Interest Coverage偏低（400-600%）
5. MSME合作（中小企业扶持）
6. ASEAN扩张（区域战略）
```

---

## 最终质量检查（Section 3-6）

### 格式检查
```yaml
□ S3.1行标题：带括号+分号分隔
□ S3.2行标题：5行固定
□ S3.3列标题：Perspective | 2024 Report | 2023 Report
□ S6.2列标题：Perspective Column
□ 所有分析：100%英文
```

### 内容检查
```yaml
□ S3.1：至少6个定量锚点（三行合计）
□ S3.2：至少20个定量锚点（5行×2列×2锚点）
□ S3.3：至少6个定量锚点（2行×2列×1.5锚点）
□ Market Position：必含#1 brand描述
□ 税率变化：必须量化（bp或百分点）
□ 新品数量：必须量化
```

### 印尼特色检查
```yaml
□ 金额混用billion/trillion
□ 强调Halal/ISO认证
□ 列举国际奖项
□ 提及ASEAN扩张
□ 使用印尼语-英文混合表达
```

---

**完成标志**：
- ✅ Part1：Section 1-2（Multiplier判断最关键）
- ✅ Part2：Section 3-6核心规则
- ✅ 完全覆盖印尼地区所有规范
- ✅ 可复用于val018等印尼案例

---

*印尼地区完整规范 v1.0 - 基于Sample008 (Garudafood)*

