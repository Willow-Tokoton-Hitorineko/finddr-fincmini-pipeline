# 财小析Pipeline 3.2 - AI快速使用指南

## 🚨 30秒快速上手 - 杜绝偷懒版

**版本**: Pipeline 3.2  
**核心**: 杜绝偷懒行为，严格数据提取

### 立即执行的3个关键点
1. **绝不偷懒**: S5.1必须提取真实董事薪酬数据
2. **严格搜索**: 使用remuneration/compensation/salary关键词
3. **标准格式**: 严格按照对应sample格式执行

## 🔍 S5.1董事薪酬提取流程（重点）

### Step 1: 关键词搜索
```
搜索关键词：
- remuneration
- compensation  
- director.*fee
- executive.*pay
- salary
- board.*compensation
```

### Step 2: 数据提取
```markdown
| Name | Position | Total Income |
| :---- | :---- | :---- |
| [真实姓名] | [具体职位] | [具体金额+货币] |
```

### Step 3: 地区适配
- 🇺🇸 美国: 通常有详细的proxy statement
- 🇬🇧 英国: Annual Report中的remuneration report
- 🇨🇳 中国: 年报中的董事薪酬表（万元）
- 🇸🇬 新加坡/马来西亚: RM千为单位
- 🇮🇩 印尼: 可能是BOC+BOD合计金额

## 📋 地区快速识别

| 地区标识 | Sample | 货币 | Multiplier | 特征 |
|----------|--------|------|------------|------|
| 🇺🇸 | sample001 | USD | Millions | Form 10-K, SEC |
| 🇬🇧 | sample002 | GBP | Millions | UK Corporate Governance |
| 🇨🇳 | sample003 | CNY | Thousands | 中文年报，归母转合并 |
| 🇸🇬🇲🇾 | sample005 | RM | Millions | PATMI概念 |
| 🇮🇩 | sample008 | IDR | Millions | BOC/BOD合并 |

## ⚡ 快速执行模板

### 1. 确定地区和Sample
```
公司地区 → 对应Sample → 格式标准
```

### 2. Section 1格式
```markdown
# Section 1: Company Overview

## S1.1: Basic Information
| Field | Value |
| :---- | :---- |
| Company Name | [提取真实公司名] |
| Establishment Date | [提取或N/A] |
| Headquarters Location | [提取真实地址] |

## S1.2: Core Competencies
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Innovation Advantages | [详细描述] | [详细描述] |
| Product Advantages | [详细描述] | [详细描述] |
| Brand Recognition | [详细描述] | [详细描述] |
| Reputation Ratings | [详细描述] | [详细描述] |
```

### 3. Section 2财务数据
```markdown
## S2.1: Income Statement
| Field | 2024 | 2023 | 2022 | Multiplier | Currency |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Revenue | [数值] | [数值] | [数值] | [Thousands/Millions] | [货币] |
```

### 4. Section 5治理结构
```markdown
## S5.1: Board Composition
| Name | Position | Total Income |
| :---- | :---- | :---- |
| [真实姓名] | [具体职位] | [金额+货币] |

## S5.2: Internal Controls
| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |
| Risk assessment procedures | [描述] | [描述] |
| Control activities | [描述] | [描述] |
| Monitoring mechanisms | [描述] | [描述] |
| Identified material weaknesses | [描述] | [描述] |
| Improvements | [描述] | [描述] |
| Effectiveness | [描述] | [描述] |
```

## 🚨 Pipeline 3.2严禁行为

### ❌ 绝对禁止
1. **S5.1填写N/A** - 必须搜索真实数据
2. **使用外部信息** - 严禁使用年报外的任何信息
3. **推理补充信息** - 严禁基于常识推理填写S1.3
4. **偷懒复制粘贴** - 每个数据都要验证
5. **格式不标准** - 必须按sample执行
6. **数据口径错误** - 必须用合并净利润

### ✅ 必须执行
1. **认真搜索董事薪酬** - 使用多个关键词
2. **提取真实数据** - 包含货币单位
3. **严格格式标准** - 按地区sample执行
4. **完整计算指标** - 12项财务指标全部计算

## 🔧 常用搜索命令

### 董事薪酬搜索
```
grep_search: "remuneration|compensation|director.*fee"
grep_search: "executive.*pay|salary|board.*compensation"
```

### 财务数据搜索
```
grep_search: "Revenue|Net Income|Total Assets"
grep_search: "营业收入|净利润|总资产" (中文公司)
```

## 📊 质量检查清单

### 🚨 Pipeline 3.2新增
- [ ] S5.1是否提取了真实董事信息？
- [ ] S5.1薪酬是否包含货币单位？
- [ ] 是否搜索了薪酬相关关键词？
- [ ] 是否避免了偷懒填写N/A？

### 基础检查
- [ ] 格式是否按对应sample？
- [ ] Section 2是否有Multiplier/Currency列？
- [ ] 财务指标是否全部计算？
- [ ] 数据口径是否正确？
- [ ] S1.3是否只使用年报明确披露的信息？
- [ ] 是否杜绝了外部信息和推理？

## 🎯 成功标准

- **数据准确性**: 100%真实提取
- **格式标准性**: 严格按sample执行
- **完整性**: 不遗漏任何必填项
- **质量**: 杜绝偷懒行为

---

**记住：Pipeline 3.2的核心就是杜绝偷懒，严格执行！** 🚀
