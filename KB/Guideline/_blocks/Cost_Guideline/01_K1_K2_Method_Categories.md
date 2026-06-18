---
title: "K-1/K-2 成本建模方法与 CAPEX 分类"
parent: "[[Cost_Guideline]]"
order: 1
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/cost
  - #cost
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/Cost_Guideline.md"
source_anchors:
  - "K-1 成本建模方法"
  - "K-2 CAPEX 分类"
---

## K-1 成本建模方法

*Cost Modeling Methodology*

Cost modeling should focus on:

- **Major infrastructure components** — Identify the primary cost buckets in the system
- **Relative cost differences between architectures** — Compare options without providing absolute prices
- **Deployment complexity impact** — Assess how installation complexity affects total cost
- **Operational implications** — Model long-term operational expenditure where relevant

> Cost models must remain **simple and explainable**. Do not introduce unnecessary granularity. Cost Architect provides engineering-level cost analysis, not commercial pricing.

---

## K-2 CAPEX 分类

*CAPEX Categories*

Cost Architect must understand the typical CAPEX distribution of modular datacenter deployments.

| Category / 类别 | Examples / 示例 |
|---|---|
| Compute hardware / 计算设备 | Servers, GPUs, storage infrastructure |
| Cooling infrastructure / 冷却系统 | Chillers, CDU, immersion tanks, cooling towers |
| Electrical infrastructure / 电力系统 | UPS, PDU, transformers, generators, switchgear |
| Containers and structure / 容器与结构 | Prefabricated containers, racks, enclosures |
| Energy storage systems / 储能系统 | BESS units, battery packs, BMS |
| Deployment infrastructure / 部署基础设施 | Site prep, transport, installation labor |
