# Quote Engine – Engineering Pricing Structure

> **⚠️ WARNING — Engineering Agent Access Prohibited**
> This tool is for commercial team use only.
> **Engineering agents (AM, ATS, Cooling Engineer, Power Engineer, etc.) are strictly prohibited from using this tool or providing any pricing information to clients.**
> All pricing inquiries must be redirected to the account manager.
> Reference: ./0.PRINCIPLES.md Principle 7 — NO PRICE.

## 1. 目标

生成结构化报价框架。
不是销售报价单，而是工程报价结构。

---

## 2. 输入参数

必须包括：

- 项目名称
- 地点
- IT容量
- 产品类型（A32 / AC40 / DC45 / MDC）
- 冗余级别
- 冷却方案
- 是否包含UPS
- 是否包含发电机

---

## 3. 成本拆分结构

### 3.1 设备成本

- IT模块
- 冷却系统
- 电力系统
- 消防系统
- 控制系统

---

### 3.2 集成成本

- 安装
- 线缆
- 管路
- 测试

---

### 3.3 运输成本

- EXW
- FOB
- CIF

---

### 3.4 认证成本

- UL
- CSA
- 本地验收

---

## 4. 冗余溢价逻辑

N → 基准

N+1 → +8–12%

2N → +25–40%

---

## 5. 利润率建议

标准范围：

15–30%

大型项目可降低至 12%

---

## 6. 输出结构

必须输出：

----------------------------------

Project:
Location:
Configuration:
IT Load:
Redundancy:
Cooling:
Power Architecture:

Lead Time:
Estimated Cost Breakdown:

Equipment:
Integration:
Logistics:
Certification:

Total EXW:
Total FOB:
Total CIF:

Risk Notes:
Expansion Capability:

----------------------------------

---

## 7. 风险控制

必须检查：

- 是否漏算UPS
- 是否漏算DX
- 是否忽略认证费用
- 是否忽略运输尺寸限制