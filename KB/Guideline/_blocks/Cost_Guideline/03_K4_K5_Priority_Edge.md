---
title: "K-4/K-5 成本优化优先级与边缘部署经济"
parent: "[[Cost_Guideline]]"
order: 3
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/cost
  - #cost
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/Cost_Guideline.md"
source_anchors:
  - "K-4 成本优化优先级"
  - "K-5 边缘部署经济"
---

## K-4 成本优化优先级

*Cost Optimization Priority*

> **This is the authoritative cost evaluation priority. Do not recommend cost reductions that violate this order.**

| Priority | Factor | Rationale |
|---|---|---|
| 1st / 第一 | Reliability / 可靠性 | System failures are far more costly than initial CAPEX savings |
| 2nd / 第二 | Operational Simplicity / 运维简洁性 | Complex systems incur higher long-term operational costs |
| 3rd / 第三 | Deployability / 部署能力 | Faster deployment reduces soft costs and time-to-revenue |
| 4th / 第四 | Cost Efficiency / 成本效率 | Only optimize cost after the above criteria are satisfied |

> 优先级冲突时的上报路径见 [[#K-6 工作流集成]]；当优化建议触及可靠性或合规底线时，应同时引用 [[Risk_Guideline#§R-3 工程红旗]]。

---

## K-5 边缘部署经济

*Edge Deployment Economics*

Edge infrastructure deployments require different cost strategies compared to hyperscale datacenters.

| Characteristic | Impact on Cost Model |
|---|---|
| Smaller scale / 规模较小 | Higher per-unit cost; fewer economies of scale |
| Limited site infrastructure / 场地有限 | May require additional power/cooling conditioning |
| Faster deployment required / 部署周期短 | Favor modular/containerized solutions |
| Containerized systems / 容器化系统 | Standardized layouts reduce engineering cost |
| Remote location / 偏远地区 | Transportation and on-site labor costs significantly higher |

> Edge 场景下扩展与成本风险另见 [[Risk_Guideline#§R-7 扩展与成本风险]]；IT 负载与场地电力容量的澄清口径见 [[POWER_SYSTEMS_Guideline#§P-1 IT 负载定义]]。
