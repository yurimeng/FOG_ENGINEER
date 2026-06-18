---
title: "R-7 扩展与成本风险"
parent: "[[Risk_Guideline]]"
order: 4
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/risk
  - #risk
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/Risk_Guideline.md"
source_anchors:
  - "R-7 扩展与成本风险"
---

## R-7 扩展与成本风险 / Scalability & Cost Risk

Engineering designs must allow future system expansion **and** avoid hidden long-term costs. Evaluate both dimensions.

### 扩展风险 / Scalability Risks

| Scalability Risk | Detection Criteria |
|---|---|
| **Expansion limitations** | Physical space not reserved for additional racks/containers |
| **Infrastructure bottlenecks** | Cooling or power capacity at limit with current load |
| **Power scaling constraints** | No headroom in transformer or generator capacity |
| **Cooling scaling constraints** | Chiller or CDU at maximum with current configuration |

### 成本风险 / Cost Risks

Some architectures introduce hidden long-term costs. Evaluate:

- **Operational complexity risks** — Complex systems require more operator training and maintenance hours
- **Maintenance accessibility risks** — Poor layout increases mean time to repair (MTTR)
- **Infrastructure replacement risks** — Proprietary components with limited supply chains increase future replacement costs

> 扩展性规划与空间预留见 [[Layout_Guideline#§L-5 扩展与生命周期]]。
> 长期成本建模方法见 [[Cost_Guideline#§K-1 成本建模方法]]。
