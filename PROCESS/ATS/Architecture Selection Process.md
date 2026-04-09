---
tags:
  - #workspace/engineer
  - #type/process
  - #process/ats
---

# Architecture Selection Process
系统架构选择流程

---

## 1 Purpose

Select the optimal infrastructure architecture based on requirements and constraints.

根据需求和约束条件选择最优基础设施架构。

---

## 2 Inputs

Customer requirements  
Site constraints  
Compute capacity  
Power availability

---

## 3 Process Steps

1 Determine compute architecture

2 Determine power architecture

3 Determine cooling architecture

4 Determine infrastructure type

---

## 4 Outputs

Selected architecture blueprint

架构选择方案

---

## 5 Key Decisions

**浸没式 vs DLC：**
- 400kW 级：AC40（40ft）/ AC45（45ft，UL 合规）→ 浸没式
- 1200kW 级：DC45（45ft）→ DLC 直冷液冷

**AC40 vs AC45：**
- 无 UL 合规要求 → AC40（40ft，UPS及UPS电池外置，成本/尺寸最优）
- **需要 UL 认证** → AC45（45ft，UPS及UPS电池内置，UL 合规）

**BESS vs Generator**
**Container vs building**

---

## 6 Risks

Over-engineering  
Unnecessary redundancy  
High CAPEX architecture