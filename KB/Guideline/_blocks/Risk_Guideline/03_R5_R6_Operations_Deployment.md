---
title: "R-5/R-6 运维与部署风险评估"
parent: "[[Risk_Guideline]]"
order: 3
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/risk
  - #risk
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/Risk_Guideline.md"
source_anchors:
  - "R-5 运维风险评估"
  - "R-6 部署风险评估"
---

## R-5 运维风险评估 / Operational Risk Evaluation

Infrastructure solutions must remain maintainable in real-world environments.

| Evaluation Factor | What to Assess |
|---|---|
| **Maintenance complexity** | Can standard technicians maintain this? Is specialized training required? |
| **Required technician skill level** | Is on-site staff qualified for the technology? |
| **Spare part availability** | Are critical spares available within acceptable lead time? |
| **Failure isolation capability** | Can a single component failure be isolated without taking down the whole system? |

> 维护通道净空与可维护性对运维风险的影响见 [[Layout_Guideline#§L-2 维护通道净空]]。

---

## R-6 部署风险评估 / Deployment Risk Assessment

Risk Auditor evaluates risks related to deployment environments:

| Environment Factor | Risk Consideration |
|---|---|
| **Remote sites** | Limited access for maintenance; spares logistics complexity |
| **Limited infrastructure availability** | Site may lack adequate power or cooling utility capacity |
| **Harsh environmental conditions** | Temperature extremes, humidity, dust; equipment must be rated accordingly |
| **Limited technical support** | Personnel on-site may not have specialized skills; favor simpler architectures |

> 环境适应性与恶劣工况要求见 [[COOLING_SYSTEM_Guideline#§G-12 环境运行范围]] 与 [[Compliance_Guideline#§C-5 容器数据中心合规]]。
