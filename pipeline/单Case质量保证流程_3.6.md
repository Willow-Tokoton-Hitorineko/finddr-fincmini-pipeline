# 单Case质量保证流程 - Pipeline 3.6

> **核心理念**：质量优先于速度，单篇精品优于批量劣品

---

## 🎯 流程目标

- **Section 2得分率**：85%+ (目前22.9%)
- **总体得分率**：90%+ (目前30.3%)
- **处理时间**：允许增加，但质量不妥协
- **返工率**：降至0%

---

## 📋 完整处理流程（9个阶段）

### 阶段1：准备与定位（15分钟）

**任务清单**：
- [ ] 确认公司名称和所属地区
- [ ] 找到对应的sample编号（001-008）
- [ ] 完整阅读该sample（了解格式和深度标准）
- [ ] 准备年报文件（2024、2023、2022三年）
- [ ] 创建工作笔记文档（记录数据来源页码）

**输出**：
```yaml
公司: Exxon Mobil Corporation
地区: 美国
Sample: Sample001 (NVIDIA)
语言: 英文
货币: USD Millions
会计准则: US GAAP
年报文件: 
  - Exxon_2024.pdf (已准备)
  - Exxon_2023.pdf (已准备)
  - Exxon_2022.pdf (已准备)
```

---

### 阶段2：Section 1数据提取（20分钟）

**S1.1: Basic Information**
```
提取任务：
  □ Company Name（100%按年报）
  □ Establishment Date（年报查找，未披露填N/A）
  □ Headquarters Location（城市+州/省+国家）

验证标准：
  ✓ 公司名称与年报封面完全一致
  ✓ 地址格式符合该地区习惯
  ✓ 如确实未披露，勇敢填N/A（不要猜测）
```

**S1.2: Core Competencies**
```
提取任务：
  □ Innovation Advantages（2024 vs 2023）
  □ Product Advantages（2024 vs 2023）
  □ Brand Recognition（2024 vs 2023）
  □ Reputation Ratings（2024 vs 2023）

质量标准：
  ✓ 每项150-300字（参考sample长度）
  ✓ 具体事实+数据支撑
  ✓ 双年份有明显对比差异
  ✓ 语言符合该地区标准（英文区100%英文）

记录页码：
  Innovation: 2024年报p.XX, 2023年报p.XX
```

**S1.3: Mission & Vision**
```
严格规则：
  □ Mission Statement: 年报原文引用或N/A
  □ Vision Statement: 年报原文引用或N/A
  □ Core Values: 年报原文引用或N/A

⚠️ 绝对禁止：
  ✗ 根据业务内容推测使命愿景
  ✗ 使用公司网站信息
  ✗ 编造或美化原文

记录页码：如有，标注页码；如无，标注"未披露"
```

**阶段2输出**：Section 1初稿 + 数据来源页码清单

---

### 阶段3：Section 2数据提取（⭐核心，60分钟）

**准备阶段（10分钟）**
```
□ 定位三年财务报表位置
  - Consolidated Income Statement
  - Consolidated Balance Sheet  
  - Consolidated Cash Flow Statement
  
□ 确认单位（关键！）
  年报标注：_________________
  判断结果：Millions/Thousands/Billions
  
□ 确认会计准则
  US GAAP / IFRS / 中国GAAP / 其他

□ 创建提取表格模板
```

**S2.1: Income Statement（15分钟）**
```
逐行提取（2024、2023、2022）：

□ Revenue
  2024: _______ (页码:___)
  2023: _______ (页码:___)
  2022: _______ (页码:___)
  
□ Cost of Goods Sold
  2024: _______ (页码:___)
  2023: _______ (页码:___)
  2022: _______ (页码:___)
  备注：如为服务业且无COGS，填N/A
  
□ Gross Profit
  方式1：直接提取 _______
  方式2：计算 Revenue - COGS = _______
  验证：两种方式是否一致？□是 □否
  
□ Operating Expense
  注意：可能需要合并多项费用
  包含项：_________________
  
□ Operating Income (EBIT)
  提取值：_______
  验证：Gross Profit - Op Expense = _______
  差异原因：_________________
  
□ Net Profit ⚠️关键
  科目名称：_________________ (记录原文)
  确认口径：□合并 □归母
  如为归母，少数股东损益：_______
  调整后Net Profit = _______
  
□ Income before income taxes
□ Income tax expense(benefit)
□ Interest Expense

立即验证：
  ✓ Net Profit = Inc Before Tax - Tax Expense?
  ✓ Gross Margin = (Rev-COGS)/Rev在10%-80%?
  ✓ 所有数字>0（除Tax可能为负）？
```

**S2.2: Balance Sheet（15分钟）**
```
逐行提取：

□ Total Assets (2024/2023/2022)
□ Current Assets
□ Non-Current Assets
□ Total Liabilities
□ Current Liabilities  
□ Non-Current Liabilities
□ Shareholders' Equity ⚠️关键
  科目名称：_________________
  确认口径：□合并（含少数股东）□归母
□ Retained Earnings
□ Total Equity and Liabilities
□ Inventories
□ Prepaid Expenses

立即验证（会计恒等式）：
  ✓ Total Assets = Total Liabilities + SE?
    2024: _______ = _______ + _______? □通过
    2023: _______ = _______ + _______? □通过
    2022: _______ = _______ + _______? □通过
    
  ✓ Total Assets = Total Equity and Liabilities?
    全部年份一致？□是
    
  ⚠️ 如不平衡，必须找出问题！
```

**S2.3: Cash Flow Statement（10分钟）**
```
□ Net Cash Flow from Operations
□ Net Cash Flow from Investing
□ Net Cash Flow from Financing
□ Net Increase/Decrease in Cash
□ Dividends

验证：
  ✓ Net Increase ≈ OCF + ICF + FCF?
    差异：_______ (<%5正常)
```

**S2.4: Key Financial Metrics（15分钟）**
```
计算12个指标（使用Section2完整规范_3.6.md）

对每个指标：
  1. 套用公式
  2. 计算三年数据
  3. 检查合理性
  4. 格式化为百分比（2位小数）

重点检查：
  □ Interest Coverage是否在合理范围
    2024: _______% (100%-50,000%?)
    如>50,000%，原因：_________________
    
  □ 2022年指标
    Asset Turnover: N/A ✓
    ROE: N/A ✓
    ROA: N/A ✓
```

**S2.5: Operating Performance（5分钟）**
```
□ Revenue by Product/Service
  来源：年报MD&A或Notes，页码：___
  格式：按sample语言风格
  
□ Revenue by Geographic Region
  来源：Segment Reporting，页码：___
  格式：按sample语言风格
```

**阶段3输出**：
- Section 2完整数据表格
- 数据来源页码记录
- 所有验证通过确认

---

### 阶段4：Section 3分析撰写（30分钟）

**S3.1: Profitability Analysis（10分钟）**
```
撰写三个维度分析（每个200-400字）：

□ Revenue & Direct-Cost Dynamics
  覆盖点：收入增长、毛利率、产品结构、地区分布
  数据支撑：引用S2数据
  
□ Operating Efficiency  
  覆盖点：营业利润率、费用控制、现金流
  
□ External & One-Off Impact
  覆盖点：有效税率、非经常性损益

质量标准：
  ✓ 有具体数字和百分比
  ✓ 有年度对比分析
  ✓ 逻辑清晰，结论明确
  ✓ 语言符合该地区标准
```

**S3.2: Financial Performance Summary（15分钟）**
```
撰写五个维度分析（每个150-300字，双年份对比）：

□ Comprehensive financial health
□ Profitability and earnings quality
□ Operational efficiency
□ Financial risk identification and early warning
□ Future financial performance projection

格式：
  | Perspective | 2024 Report | 2023 Report |
  
注意：
  ✓ 中国地区用"2024年年度报告"格式
  ✓ 每个维度都有2024和2023的对比
```

**S3.3: Business Competitiveness（5分钟）**
```
撰写两个维度（每个100-200字，双年份对比）：

□ Business Model
□ Market Position

格式要求：参考对应sample的列标题
```

---

### 阶段5：Section 4-6快速完成（30分钟）

**时间分配**：
- S4.1: Risk Factors - 10分钟
- S5.1: Board Composition - 5分钟
- S5.2: Internal Controls - 10分钟
- S6.1-6.3: Future Outlook - 5分钟

**注意事项**：
- 全部使用表格格式
- 按sample的列标题
- 语言100%符合地区标准
- S5.1必须提取真实董事薪酬（不能偷懒填N/A）

---

### 阶段6：完整性检查（15分钟）

**使用25项检查清单**：

#### 格式检查（5分钟）
- [ ] 所有Section标题为英文
- [ ] 所有财务科目名称为英文（Field, Revenue等）
- [ ] 所有内容使用表格格式（无段落）
- [ ] 表格列标题与sample完全一致
- [ ] 中文地区特殊列标题正确（如"公司全称2024年年度报告"）

#### 语言检查（5分钟）
- [ ] 英文地区：100%英文内容
- [ ] 中国地区：框架英文+内容简体中文
- [ ] 香港地区：框架英文+内容繁体中文
- [ ] 无语言混用现象

#### 数据检查（5分钟）
- [ ] Section 2所有验证公式通过
- [ ] Balance Sheet平衡（会计恒等式）
- [ ] Interest Coverage合理
- [ ] 所有百分比格式正确（2位小数+%）
- [ ] Multiplier和Currency一致

---

### 阶段7：交叉验证（10分钟）

**逻辑一致性验证**：
```
□ S1.2的产品优势 ↔ S2.5的产品收入数据是否一致？
□ S3.1的盈利分析 ↔ S2.4的财务指标是否吻合？
□ S3.2的风险预警 ↔ S4.1的风险因素是否关联？
□ S6.1的战略方向 ↔ S1.2的创新优势是否呼应？
```

**合理性验证**：
```
□ 收入增长率与行业情况是否匹配？
□ 毛利率水平与行业平均是否合理？
□ 财务指标年度变化是否有合理解释？
□ 没有明显的数据矛盾？
```

---

### 阶段8：最终审核（10分钟）

**自我审核清单**：
```
□ 删除所有结尾的Pipeline说明
□ 删除"预期得分"、"关键优化点"等额外内容
□ 检查是否有遗漏的section或字段
□ 检查是否有格式错误（如多余空行）
□ 确认文件命名规范：公司名_财小析报告.md
```

**对比sample最终检查**：
```
□ Section 1-6的结构与sample完全一致
□ 表格格式与sample完全一致
□ 内容深度与sample相当
□ 语言风格与sample一致
```

**数据溯源确认**：
```
□ 工作笔记中有所有数据的页码记录
□ 关键数据可以快速在年报中定位
□ 计算过程清晰可复现
```

---

### 阶段9：质量评分与归档（5分钟）

**自我评分（参考标准）**：
```
Section 1 (22分): ____/22
  S1.1: 信息完整准确？____/7
  S1.2: 分析深度充分？____/10
  S1.3: 严格遵守N/A规则？____/5

Section 2 (117分): ____/117 ⭐关键
  S2.1: 数据准确完整？____/30
  S2.2: Balance Sheet平衡？____/30
  S2.3: 现金流数据准确？____/20
  S2.4: 12个指标计算正确？____/30
  S2.5: 经营数据详细？____/7

Section 3 (34分): ____/34
  S3.1: 分析深入有据？____/12
  S3.2: 五个维度完整？____/15
  S3.3: 竞争力分析到位？____/7

Section 4 (16分): ____/16
Section 5 (23分): ____/23
Section 6 (28分): ____/28

总分预估: ____/240
```

**预期标准**：
- 目标：210+/240 (87.5%+)
- 底线：216+/240 (90%+)
- 如低于210分，必须找出问题并修正

**归档文件**：
```
保存文件：
  □ 公司名_财小析报告.md (最终成品)
  □ 公司名_数据来源记录.txt (页码清单)
  □ 公司名_质量检查表.md (自我评分)
```

---

## ⚠️ 关键原则

### 原则1：遇到问题立即停止
```
发现以下情况，必须停止并解决：
  ✗ Balance Sheet不平衡
  ✗ 找不到合并口径Net Profit
  ✗ Multiplier无法判断
  ✗ Sample格式理解不清
  
不要带病前进，不要侥幸心理！
```

### 原则2：数据质量>速度
```
宁可多花30分钟仔细提取数据
不要为了快而编造或估算数据

Section 2是得分关键（48.75%权重）
数据错误=全盘皆输
```

### 原则3：100%可验证
```
所有数据必须能追溯到年报原文
工作笔记记录所有页码
随时准备证明数据来源
```

### 原则4：单篇精品策略
```
❌ 旧策略：批量处理8个case，平均30分/case
✅ 新策略：逐个处理，确保每个90分+/case

质量提升才能真正提高效率
返工浪费的时间远超初次认真的时间
```

---

## 📊 时间预算

| 阶段 | 预计时间 | 累计时间 |
|------|---------|---------|
| 准备与定位 | 15分钟 | 15分钟 |
| Section 1 | 20分钟 | 35分钟 |
| Section 2 ⭐ | 60分钟 | 95分钟 |
| Section 3 | 30分钟 | 125分钟 |
| Section 4-6 | 30分钟 | 155分钟 |
| 完整性检查 | 15分钟 | 170分钟 |
| 交叉验证 | 10分钟 | 180分钟 |
| 最终审核 | 10分钟 | 190分钟 |
| 质量评分 | 5分钟 | 195分钟 |
| **总计** | **约3.25小时** | - |

**注**：
- 首次处理可能需要4小时
- 熟练后可缩短至2.5小时
- 但绝不牺牲质量换取速度

---

## 🎯 成功标准

**过程成功**：
✅ 所有数据有页码记录
✅ 所有验证公式通过
✅ 所有检查清单打勾
✅ 格式100%符合sample

**结果成功**：
✅ 自我评分≥216/240 (90%)
✅ Section 2得分≥100/117 (85%)
✅ 无明显错误和遗漏
✅ 可以自信提交

---

## 💡 经验总结

### 成功案例：val029（五粮液）
- Section 2: 82/117 (70.1%) - 相对最高
- 成功因素：
  - 数据提取认真
  - 计算相对准确
  - 格式基本正确
- 改进空间：
  - Interest Coverage格式化错误
  - 部分分析深度可提升

### 失败案例：val024（英国）
- Section 2: 8/117 (6.8%) - 最低
- 失败原因：
  - 数据可能编造（太整齐）
  - 计算可能错误
  - 未严格遵循sample
- 教训：
  - 绝不偷懒
  - 绝不编造
  - 绝不侥幸

---

*单Case质量保证流程 v3.6 - 质量优先，精益求精*
