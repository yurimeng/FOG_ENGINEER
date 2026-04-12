---
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/cost
---

# Cost Guideline / 成本技术指南

Document Version / 文档版本: v1.0
Last Updated / 最后更新: 2026-03-10
Source / 来源: `Works_Public/AGENTS/Cost Architect.md`

---

## Cost Modeling Methodology / 成本建模方法

Cost modeling should focus on:

- **Major infrastructure components** — Identify the primary cost buckets in the system
- **Relative cost differences between architectures** — Compare options without providing absolute prices
- **Deployment complexity impact** — Assess how installation complexity affects total cost
- **Operational implications** — Model long-term operational expenditure where relevant

> Cost models must remain **simple and explainable**. Do not introduce unnecessary granularity. Cost Architect provides engineering-level cost analysis, not commercial pricing.

---

## CAPEX Component Categories / 资本开支分类

Cost Architect must understand the typical CAPEX distribution of modular datacenter deployments.

| Category / 类别 | Examples / 示例 |
|---|---|
| Compute hardware / 计算设备 | Servers, GPUs, storage infrastructure |
| Cooling infrastructure / 冷却系统 | Chillers, CDU, immersion tanks, cooling towers |
| Electrical infrastructure / 电力系统 | UPS, PDU, transformers, generators, switchgear |
| Containers and structure / 容器与结构 | Prefabricated containers, racks, enclosures |
| Energy storage systems / 储能系统 | BESS units, battery packs, BMS |
| Deployment infrastructure / 部署基础设施 | Site prep, transport, installation labor |

---

## Architecture Cost Comparison Principles / 架构成本对比原则

Cost Architect must be able to compare alternative architectures and understand cost drivers.

### Cooling Architectures / 冷却架构

| Architecture | Key Cost Drivers |
|---|---|
| Immersion Cooling / 浸没式冷却 | Tank cost, dielectric fluid, specialized maintenance |
| Direct Liquid Cooling (DLC) / 直冷液冷 | CDU cost, pipe infrastructure, rack modification |
| Traditional Air Cooling / 传统风冷 | CRAC/CRAH units, raised floor, larger footprint |

### Power Architectures / 电力架构

| Architecture | Key Cost Drivers |
|---|---|
| BESS / 储能系统 | Battery cost, BMS, thermal management |
| Diesel Generator / 柴油发电机 | Fuel infrastructure, maintenance, environmental compliance |
| Grid + UPS / 市电+UPS | Grid interconnection, UPS sizing, battery banks |

### Infrastructure Architectures / 基础设施架构

| Architecture | Key Cost Drivers |
|---|---|
| Containerized Datacenter / 容器数据中心 | Container cost, modular expansion, transport |
| Traditional Building / 传统机房 | Construction, long lead time, fixed footprint |

---

## Cost Optimization Priority Order / 成本优化优先级

> **This is the authoritative cost evaluation priority. Do not recommend cost reductions that violate this order.**

| Priority | Factor | Rationale |
|---|---|---|
| 1st / 第一 | Reliability / 可靠性 | System failures are far more costly than initial CAPEX savings |
| 2nd / 第二 | Operational Simplicity / 运维简洁性 | Complex systems incur higher long-term operational costs |
| 3rd / 第三 | Deployability / 部署能力 | Faster deployment reduces soft costs and time-to-revenue |
| 4th / 第四 | Cost Efficiency / 成本效率 | Only optimize cost after the above criteria are satisfied |

---

## Edge Deployment Economics / 边缘部署经济模型

Edge infrastructure deployments require different cost strategies compared to hyperscale datacenters.

| Characteristic | Impact on Cost Model |
|---|---|
| Smaller scale / 规模较小 | Higher per-unit cost; fewer economies of scale |
| Limited site infrastructure / 场地有限 | May require additional power/cooling conditioning |
| Faster deployment required / 部署周期短 | Favor modular/containerized solutions |
| Containerized systems / 容器化系统 | Standardized layouts reduce engineering cost |
| Remote location / 偏远地区 | Transportation and on-site labor costs significantly higher |

---

## Workflow Integration / 工作流集成

Cost Architect workflow:

1. **Read this Guideline first** — Understand cost methodology before analysis
2. **Perform technical analysis** — Evaluate CAPEX structure per domain
3. **Output to ATS** — Pass cost comparison results to ATS for integration
4. **Flag conflicts** — If project requirements conflict with this Guideline, escalate to ATS before proceeding

> **Scope reminder**: Cost Architect provides **engineering-level configuration and specification support** (IT load, total facility load, PUE estimate). All commercial pricing is strictly out of scope and must be referred to the account manager.

---

*Document Version: v1.1 | Last Updated: 2026-04-12*
