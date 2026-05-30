# 财小析地区规范总索引 - 8大地区完整标准

> **创建日期**：2025-01-21
> **版本**：v1.0
> **状态**：✅ 8个地区规范全部完成

---

## 🎯 使用方法

### 第一步：确定地区
根据公司所在地/上市地确定使用哪个地区规范。

### 第二步：打开对应规范文档
找到该地区的完整规范文档，**完全按照该文档执行**。

### 第三步：逐项检查
使用文档中的质量检查清单，确保100%符合标准。

### 配套口径与取数文档
- 《数据口径与内容取数总则_3.6.md》
- 《样本取数路径_3.6.md》
- 《地区规范核对清单_3.6.md》

---

## 📚 8大地区规范文档

### 1️⃣ 美国地区 (Sample001)
**文档**：`美国地区完整规范_Sample001.md`
**Sample公司**：NVIDIA Corporation
**验证集案例**：val043 (Exxon Mobil)

**关键特征**：
- 语言：100%英文
- 货币：USD
- Multiplier：Millions
- 会计准则：US GAAP
- S1.3列标题：Field | **Value**
- S3.1列标题：**Field** | Answer
- S3.3列标题：**Field** | 2024 Report | 2023 Report

---

### 2️⃣ 英国地区 (Sample002)
**文档**：`英国地区完整规范_Sample002.md`
**Sample公司**：Chemring Group PLC
**验证集案例**：val024 (Fever-Tree Drinks PLC)

**关键特征**：
- 语言：100%英文
- 货币：GBP
- Multiplier：Millions
- 会计准则：IFRS
- **服务业特征**：COGS=N/A, Gross Profit=N/A, Gross Margin=N/A
- S1.3列标题：Field | **Answer**
- S3.1列标题：**Perspective** | Answer（带括号）
- S3.3列标题：**Field** | 2024 Report | 2023 Report
- 负数用括号：(335.8)

---

### 3️⃣ 中国地区 (Sample003)
**文档**：`中国地区完整规范_Sample003.md`
**Sample公司**：宁德时代新能源科技股份有限公司
**验证集案例**：val029 (五粮液)

**关键特征**：
- 语言：**双层**（框架英文+内容简体中文）
- 货币：CNY
- Multiplier：Thousands（千元）或Ones（元）
- 会计准则：中国企业会计准则
- S1.2列标题：Perspective | **公司全称2024年年度报告** | ...
- S1.3列标题：Field | **Answer**
- S3.1列标题：**Perspective** | Answer（带括号）
- S3.2列标题：Perspective | **2024年年度报告** | ...（无公司全称）
- S3.3列标题：Field | **公司全称2024年年度报告** | ...
- S2.5格式：**2024年分产品营业收入（千元）：...**

**⚠️ 严禁**：
- Section标题翻译成中文
- 财务科目名称翻译成中文
- 基础列标题翻译成中文

---

### 4️⃣ 香港地区 (Sample004)
**文档**：`香港地区完整规范_Sample004.md`
**Sample公司**：騰訊控股有限公司
**验证集案例**：val042 (美团)

**关键特征**：
- 语言：**双层**（框架英文+内容繁体中文）
- 货币：CNY或HKD
- Multiplier：Millions
- 会计准则：IFRS
- S1.3列标题：Field | **Value**
- S3.1列标题：**Perspective** | Answer（带括号）
- S3.3列标题：**Perspective** | 2024 Report | 2023 Report
- 负数用括号：(311,011)

**⚠️ 必须使用繁体中文**：
- 騰訊（不是腾讯）
- 營業（不是营业）
- 實現（不是实现）

---

### 5️⃣ 新加坡地区 (Sample005)
**文档**：`新加坡地区完整规范_Sample005.md`
**Sample公司**：Singapore Airlines Limited
**验证集案例**：val001 (IHH Healthcare)

**关键特征**：
- 语言：100%英文
- 货币：SGD或RM
- Multiplier：Millions
- 会计准则：SFRS/MFRS
- **航空/服务业**：COGS=N/A, Gross Profit=N/A
- S1.3列标题：Field | **Answer**
- S3.1列标题：**Field** | Answer
- S3.3列标题：**Field** | 2024 Report | 2023 Report
- 特殊概念：PATMI（合并净利润）
- 可能使用财年（非自然年）

---

### 6️⃣ 澳大利亚地区 (Sample006)
**文档**：`澳大利亚地区完整规范_Sample006.md`
**Sample公司**：CSL Limited
**验证集案例**：val036 (Telstra)

**关键特征**：
- 语言：100%英文
- 货币：USD或AUD（视公司而定）
- Multiplier：Millions
- 会计准则：IFRS (Australian)
- S1.3列标题：Field | **Value**
- S3.1列标题：**Perspective** | Answer（带括号）
- S3.3列标题：**Perspective** | 2024 Report | 2023 Report
- 负数用括号：(7,129)
- 可能使用财年（非自然年）

---

### 7️⃣ 马来西亚地区 (Sample007)
**文档**：`马来西亚地区完整规范_Sample007.md`
**Sample公司**：IJM Corporation Berhad
**验证集案例**：val010 (Maxis Berhad)

**关键特征**：
- 语言：100%英文
- 货币：MYR (RM)
- Multiplier：**Thousands**
- 会计准则：MFRS
- S1.3列标题：Field | **Answer**
- S3.1列标题：**Field** | Answer
- S3.2列标题：**Perspective Column** | 2024 Report | 2023 Report ⚠️⚠️
- S3.3列标题：Field | 2024 Report  | 2023 Report（**2个空格**）
- 负数用括号

**⚠️⚠️ 超级特殊**：
- S3.2用"Perspective Column"（唯一地区）
- S3.3的"2024 Report"后有2个空格

---

### 8️⃣ 印尼地区 (Sample008)
**文档**：`印尼地区完整规范_Sample008.md`
**Sample公司**：PT Garudafood Putra Putri Jaya Tbk
**验证集案例**：val018 (PT Indofood CBP)

**关键特征**：
- 语言：100%英文
- 货币：IDR (Rupiah)
- Multiplier：**Billions** ⚠️⚠️⚠️（唯一使用Billions的地区）
- 会计准则：Indonesian GAAP
- S1.3列标题：Field | **Value**
- S3.1列标题：**Perspective** | Answer（带括号）
- S3.3列标题：**Perspective** | 2024 Report | 2023 Report
- 负数用括号

**🚨 最关键警告**：
```
年报标注：Rp jutaan (百万盾)
实际含义：Millions IDR
转换填写：Billions IDR ✅

如果误用Millions，数值差1000倍！
Section 2得分会接近0分！
```

---

## 📊 快速对照表

### S1.3列标题对照
| 地区 | S1.3列标题 |
|------|-----------|
| 美国 | Field \| **Value** |
| 英国 | Field \| **Answer** |
| 中国 | Field \| **Answer** |
| 香港 | Field \| **Value** |
| 新加坡 | Field \| **Answer** |
| 澳大利亚 | Field \| **Value** |
| 马来西亚 | Field \| **Answer** |
| 印尼 | Field \| **Value** |

### S3.1列标题对照
| 地区 | S3.1列标题 | 括号说明 |
|------|-----------|---------|
| 美国 | **Field** \| Answer | 无 |
| 英国 | **Perspective** \| Answer | ✅ 有 |
| 中国 | **Perspective** \| Answer | ✅ 有 |
| 香港 | **Perspective** \| Answer | ✅ 有 |
| 新加坡 | **Field** \| Answer | 无 |
| 澳大利亚 | **Perspective** \| Answer | ✅ 有 |
| 马来西亚 | **Field** \| Answer | 无 |
| 印尼 | **Perspective** \| Answer | ✅ 有 |

### S3.2列标题对照
| 地区 | S3.2第一列标题 |
|------|--------------|
| 美国 | Perspective |
| 英国 | Perspective |
| 中国 | Perspective（内容列用"2024年年度报告"）|
| 香港 | Perspective |
| 新加坡 | Perspective |
| 澳大利亚 | Perspective |
| **马来西亚** | **Perspective Column** ⚠️ |
| 印尼 | Perspective |

### S3.3列标题对照
| 地区 | S3.3第一列标题 | 内容列标题 |
|------|--------------|-----------|
| 美国 | **Field** | 2024 Report \| 2023 Report |
| 英国 | **Field** | 2024 Report \| 2023 Report |
| 中国 | **Field** | **公司全称2024年年度报告** \| ... |
| 香港 | **Perspective** | 2024 Report \| 2023 Report |
| 新加坡 | **Field** | 2024 Report \| 2023 Report |
| 澳大利亚 | **Perspective** | 2024 Report \| 2023 Report |
| 马来西亚 | **Field** | 2024 Report  \| 2023 Report（2空格）|
| 印尼 | **Perspective** | 2024 Report \| 2023 Report |

### Multiplier对照
| 地区 | Multiplier | 备注 |
|------|-----------|------|
| 美国 | Millions | USD |
| 英国 | Millions | GBP |
| 中国 | **Thousands** | CNY（或Ones）|
| 香港 | Millions | CNY/HKD |
| 新加坡 | Millions | SGD/RM |
| 澳大利亚 | Millions | USD/AUD |
| 马来西亚 | **Thousands** | MYR |
| **印尼** | **Billions** ⚠️ | **IDR（唯一）** |

---

## 🔍 地区判断方法

### 方法1：通过公司名称后缀
```
Corporation / Inc. / LLC → 美国
PLC / Limited (UK) → 英国
股份有限公司 / 科技股份 → 中国
控股有限公司 / 集团有限公司 → 香港
Pte Ltd / Limited (SG) → 新加坡
Limited / Pty Ltd → 澳大利亚
Berhad / Sdn Bhd → 马来西亚
Tbk / PT → 印尼
```

### 方法2：通过年报语言
```
100%英文 → 美英新澳马印
简体中文+英文框架 → 中国
繁体中文+英文框架 → 香港
```

### 方法3：通过货币
```
USD → 美国（或澳大利亚跨国公司）
GBP → 英国
CNY → 中国/香港
SGD/RM → 新加坡/马来西亚
AUD → 澳大利亚
MYR → 马来西亚
IDR → 印尼
```

---

## ⚠️ 最容易出错的3个地区

### 🔴 1. 印尼（Multiplier错误）
**问题**：Multiplier判断错误，误用Millions导致数值差1000倍
**解决**：印尼必须用**Billions**，记住这是唯一用Billions的地区

### 🔴 2. 马来西亚（S3.2列标题）
**问题**：S3.2第一列标题写成"Perspective"
**解决**：马来西亚用**"Perspective Column"**（唯一地区）

### 🔴 3. 中国（语言分层）
**问题**：将Section标题、财务科目翻译成中文
**解决**：框架层（Section标题、科目名、基础列标题）必须英文

---

## 📖 使用示例

**假设处理：val043 Exxon Mobil**

```
Step 1: 确定地区
  公司：Exxon Mobil Corporation
  后缀：Corporation → 美国

Step 2: 打开文档
  打开：美国地区完整规范_Sample001.md

Step 3: 查看关键特征
  - Multiplier: Millions USD ✅
  - S1.3: Field | Value ✅
  - S3.1: Field | Answer ✅
  - S3.3: Field | 2024 Report | 2023 Report ✅

Step 4: 按规范执行
  严格按照文档中的每一项要求处理

Step 5: 质量检查
  使用文档中的检查清单逐项验证
```

---

## 🎯 核心原则

### 原则1：一地区一规范
- 确定地区后，只使用该地区规范
- 不要混用不同地区的标准
- 不要参考其他地区的sample

### 原则2：100%遵循规范
- 格式必须100%符合
- 列标题必须精确匹配
- 语言规则必须严格执行

### 原则3：数据质量第一
- 所有数据从年报提取
- Multiplier判断必须正确
- 财务指标计算准确

---

## 📁 文档结构

```
财小析_Pipeline规则库/
└── 地区规范/
    ├── README_地区规范总索引.md (本文档)
    ├── 美国地区完整规范_Sample001.md
    ├── 英国地区完整规范_Sample002.md
    ├── 中国地区完整规范_Sample003.md
    ├── 香港地区完整规范_Sample004.md
    ├── 新加坡地区完整规范_Sample005.md
    ├── 澳大利亚地区完整规范_Sample006.md
    ├── 马来西亚地区完整规范_Sample007.md
    └── 印尼地区完整规范_Sample008.md
```

---

## ✅ 使用检查清单

### 开始处理前
- [ ] 确定公司所属地区
- [ ] 打开对应地区规范文档
- [ ] 快速浏览关键特征
- [ ] 确认Multiplier和Currency

### 处理过程中
- [ ] 每个Section参考对应章节
- [ ] 列标题完全按照规范
- [ ] 语言规则严格执行
- [ ] 数据从年报准确提取

### 处理完成后
- [ ] 使用地区规范中的质量检查清单
- [ ] 验证所有格式正确
- [ ] 确认数据准确性
- [ ] 交叉验证合理性

---

*地区规范总索引 v1.0 - 让每个地区的报告都100%准确*

**记住：地区确定后，完全按照该地区规范执行！**
