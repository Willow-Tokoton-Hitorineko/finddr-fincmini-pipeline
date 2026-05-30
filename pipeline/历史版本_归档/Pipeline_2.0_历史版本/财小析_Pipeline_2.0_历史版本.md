# 小透 Pipeline 2.0 最终规则文档

**版本**：2.0  
**完成时间**：2025-10-16  
**学习来源**：
- 比赛要求CSV（Section 1-6）
- 样本集（sample001-008）
- 评分系统（DeepEval标准）
- 五粮液失分案例（109.93/240）
- 中国移动val030（高分版）
- 宁德时代数据口径分析

**目标**：批量处理验证集/测试集，确保每个case达到**92-95分**

---

## 🎯 核心优化规则（基于实战案例）

### 规则1：Net Profit口径选择（关键！）

**发现**：宁德时代sample003使用**合并净利润**（含少数股东损益），而非归母净利润

| 数据项 | 传统口径 | 比赛口径 | 差异 | 依据 |
|--------|---------|---------|------|------|
| Net Profit | 归属于母公司股东的净利润 | **合并净利润** | 含少数股东损益 | sample003实证 |
| Shareholders' Equity | 归属于母公司股东权益 | **所有者权益合计** | 含少数股东权益 | sample003实证 |

**小透2.0规则**：
```python
# S2.1 Net Profit提取
net_profit = grep("合并利润表", "四、净利润")  # 合并数
# 而非：归属于母公司股东的净利润

# S2.2 Shareholders' Equity提取
equity = grep("合并资产负债表", "所有者权益合计")  # 含少数股东
# 而非：归属于母公司股东权益

# 影响：
#   - Net Profit差异通常<1%
#   - Shareholders' Equity差异通常<1%
#   - 但需统一口径避免扣分
```

---

### 规则2：Multiplier智能判断（解决五粮液失分）

**五粮液失分25-30分根因**：全部标注`Units`而非`Ones`

**小透2.0规则**：
```python
def auto_multiplier(value, currency="CNY"):
    """
    自动判断Multiplier
    
    参数:
        value: 数值大小
        currency: 币种（CNY/USD等）
    
    返回:
        (multiplier, converted_value)
    """
    if currency == "CNY":
        # 中国公司：优先Thousands或Ones
        if value >= 100_000_000_000:  # ≥1000亿
            return "Ones", value  # 保留完整数字
        elif value >= 1_000_000_000:  # 10亿-1000亿
            return "Thousands", round(value / 1000, 2)
        elif value >= 1_000_000:  # 百万级
            return "Thousands", round(value / 1000, 2)
        else:
            return "Ones", value
    
    elif currency in ["USD", "GBP", "SGD"]:
        # 欧美公司：优先Millions
        if value >= 1_000_000:
            return "Millions", round(value / 1_000_000, 2)
        elif value >= 1_000:
            return "Thousands", round(value / 1_000, 2)
        else:
            return "Ones", value
    
    # 兜底
    return "Ones", value

# 示例：
# 五粮液Revenue: 89,175,178,323元
# → ("Ones", 89,175,178,323) 或 ("Thousands", 89,175,178)
# 禁止标注"Units"
```

---

### 规则3：S2.5数据回填策略（五粮液失分点）

**五粮液问题**：2022年数据全部填"N/A"，实际2023年报有2022对比列

**小透2.0规则**：
```python
def get_s25_data(year, 年报2024, 年报2023, 年报2022=None):
    """
    S2.5 Revenue by Product/Service获取策略
    
    优先级：
    1. 从对应年份年报提取
    2. 从后续年报的对比列提取
    3. 从前序年报提取
    4. 实在无数据才填"N/A"
    """
    if year == 2024:
        data = grep(年报2024, "分产品营业收入")
    elif year == 2023:
        data = grep(年报2024, "分产品.*2023") or grep(年报2023, "分产品营业收入")
    elif year == 2022:
        data = grep(年报2024, "分产品.*2022") \
            or grep(年报2023, "分产品.*2022") \  # ← 关键！
            or grep(年报2022, "分产品营业收入")
    
    return data if data else "N/A"
```

**实例**：五粮液2023年报第277行有2022年分产品收入对比表

---

### 规则4：S5.1董事薪酬必填（五粮液失分5-8分）

**五粮液问题**：全部董事填"N/A"，实际年报第725-728行有完整薪酬表

**小透2.0规则**：
```python
def extract_board_compensation():
    """
    S5.1 Board Composition提取策略
    """
    # Step 1: grep查找薪酬表
    table = grep("董事.*监事.*高级管理人员报酬")
    
    # Step 2: 提取字段
    #   - 姓名
    #   - 职务（合并多行职务，如"董事长/党委书记"）
    #   - 从公司获得的税前报酬总额
    
    # Step 3: 格式转换
    for person in table:
        if person.salary == 0 and person.from_related_party:
            total_income = "0（在关联方领取）"
        elif person.salary == 0:
            total_income = "0"
        else:
            # 保留原单位或转换
            total_income = f"{person.salary}万元"
            # 或转换：f"{person.salary * 10000} CNY"
    
    # Step 4: 选取人数
    #   - 最少3人（董事长+CEO+CFO）
    #   - 推荐5-8人（含独立董事代表）
    #   - 样本集多为3-10人
    
    return board_list
```

---

### 其他核心规则

**表头统一格式**：
```
所有S1.2/S3.2/S3.3/S4.1/S5.2/S6全部表格：

| Perspective | 2024 Report | 2023 Report |
| :---- | :---- | :---- |

强制标准：
- 年份：4位数字
- 单词：大写R开头的"Report"
- 分隔：一个空格
- 禁止：任何中文、公司名、年月日
```

**财务指标格式**：
```python
# 全部使用百分比格式（参考样本集）
ratios = {
    "Gross Margin": f"{value:.2f}%",      # 72.71%
    "Current Ratio": f"{value:.2f}%",     # 417.13%
    "ROE": f"{value:.2f}%",               # 91.46%
    # 禁止：倍数格式（如3.25x）
}
```

---

## ✅ 小透2.0自检清单

处理每个case后必检：

```
Section 1:
□ S1.1地址格式："City, Country"
□ S1.2表头："2024 Report"
□ S1.2每项60-200字
□ S1.3无披露填"N/A"

Section 2:
□ S2.1-2.3包含3年完整数据
□ S2.1 Net Profit用合并数
□ S2.2 Shareholders' Equity用所有者权益合计
□ S2.4严格12项，全部百分比格式
□ S2.5尽量补全3年数据（从多年报回填）
□ Total Assets = Total E+L（恒等校验）

Section 3-6:
□ 所有表头统一："2024 Report"
□ S5.2必须6项（含Improvements）
□ 文字字数达标
□ 负数用"-"号
```

---

**小透2.0 Pipeline最终规则文档完成！**  
**等待批量处理指令！** 🎯
