---
title: §G-10 热负荷计算 + §G-11 冗余策略
parent: "[[../COOLING_SYSTEM_Guideline]]"
order: 6
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/cooling
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/COOLING_SYSTEM_Guideline.md"
source_anchors: []
---

## §G-10 热负荷计算 (Thermal Load Calculation)

Cooling Engineer must evaluate total thermal load.

**Components:**
- IT heat load
- Pump systems
- Auxiliary equipment
- Electrical conversion losses

**Sizing rule:** Cooling capacity ≥ Peak IT heat load × 1.1 (minimum 10% margin)

**PUE 设计值参考 / PUE Reference (per IT Zone × ambient band):**

| IT Zone | 低温区（干冷优先）| 高温区（DX 辅助）|
|---------|-----------------|-----------------|
| **A32**（独立部署）| ~1.03–1.05 | ~1.08–1.12 |
| **AC40** | ~1.02–1.08 | ~1.15–1.20 |
| **AC45** | ~1.02–1.08 | ~1.15–1.20 |
| **DC45** | ~1.07–1.15 | ~1.25–1.35 |

> PUE 受环境温度、负载率、散热方案等多因素影响，以上为参考值，禁止作为固定承诺数字。

---

## §G-11 冗余策略 (Redundancy Strategy)

Cooling redundancy follows practical engineering principles:

- N+1 for critical pumps (where applicable within the container)
- Redundant circulation loops where necessary
- Independent cooling modules for container deployments
- Full duplication of cooling plants should be **avoided** unless operational requirements justify the complexity

**⚠️ Cooling Zone does NOT offer N+1 or 2N.** Each cooling device works with one IT Zone device. 配对约束见 [[#§G-8 IT Zone 与冷却区匹配]]，客户问及 N+1/2N 时按 [[#§G-18 上报规则]] 上报。
