---
tags:
  - #workspace/engineer
  - #type/process
  - #process/ats
---

# Capacity Planning Process
容量规划流程

---

## 1 Purpose

**⚠️ CRITICAL: This process defines both IT load and total facility load. These are NOT the same number.**

Estimate IT load and total facility load requirements.
Reference: [[POWER_LOAD|KB/POWER_LOAD]]

估算 IT 负载与整体电力负荷需求。

---

## 2 Inputs

GPU count
Server configuration
Network architecture
**UL compliance requirement**（如客户有 UL 合规需求，直接跳转 AC45 选型路径）

GPU数量
服务器配置
网络架构
**UL 合规需求**（如有，直接跳转 AC45 选型路径）

---

## 3 产品规格速查（容量规划参考）

| 产品 | IT 容量 | 集装箱规格 | UPS 放置 | UPS电池后备 | UL |
|------|---------|---------|---------|-----------|-----|
| A32 | 45–50kW | 单柜 | 外置（客户自备）| 外置 | — |
| AC40 | 400kW | 40ft | **外置（客户自备）** | ~10 分钟（客户自备 2×93LiG2）| ❌ |
| **AC45** | 400kW | 45ft | 内置（专用电力舱）| ~20 分钟（内置 2×93LiG2）| ✅ |
| DC45 | 1200kW | 45ft | 内置 | ~8 分钟（内置 3×93LiG2）| ✅ |

> ⚠️ **UPS 电池 vs BESS 电池：** 上表中"UPS电池后备"指 UPS 配套的 93LiG2 磷酸铁锂电池柜（分钟级瞬时切换）。BESS（如 Tesla Megapack / 国轩）是独立大型储能系统（小时级供电）。
> 选型提示：400kW + 无 UL → **AC40**（UPS及UPS电池外置，成本最优）；400kW + 需要 UL → **AC45**（UPS及UPS电池内置）；1200kW DLC + UL → **DC45**。

---

## 3 Process Steps

1 Calculate server power consumption

2 Calculate rack level power

3 Calculate cluster power

4 Calculate facility power

---

## 4 Outputs

IT load estimate
Total facility load estimate (IT load ÷ PUE)
Peak power requirement

IT负载估算
整体电力负荷估算（IT负载 ÷ PUE，场地电力接入容量）
峰值功率

---

## 5 Risks

Underestimated peak power
Incorrect redundancy assumptions
**Confusing IT load with total facility load**