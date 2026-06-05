---
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/cost
  - #MDC
---
# Cost Guideline / 成本技术指南

| Field | Value |
|---|---|
| Document Version / 文档版本 | v1.1 |
| Last Updated / 最后更新 | 2026-06-05 |
| Source / 来源 | `Works_Public/AGENTS/Cost Architect.md` |

---

> **速查 / Quick Reference**
> 本文件规定 Cost Architect 在 MDC / 边缘 DC 预销售场景下的成本建模方法、CAPEX 分类、架构成本对比、成本优化优先级与 Edge 经济性。所有商业定价由客户经理负责，本 Guideline 仅输出工程级分析与对比。
> 章节 ID 体系与跨 Agent 引用规则见 [[PRINCIPLE_Guideline#§8 章节 ID 一致性表]]。

## 章节速查 / Section Index

| ID | 用途 |
|---|---|
| [[#K-1 成本建模方法]] | 成本建模的四个关注点与"简单可解释"原则 |
| [[#K-2 CAPEX 分类]] | 六大 CAPEX 类别的标准拆分 |
| [[#K-3 架构成本对比]] | 冷却 / 电力 / 基础设施三类架构的成本驱动因子 |
| [[#K-4 成本优化优先级]] | 成本评估的硬性优先级（可靠性 > 运维 > 部署 > 成本） |
| [[#K-5 边缘部署经济]] | Edge 场景下规模、场地、部署周期对成本的影响 |
| [[#K-6 工作流集成]] | Cost Architect 的标准工作流与上报路径 |

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

---

## K-3 架构成本对比

*Architecture Cost Comparison*

Cost Architect must be able to compare alternative architectures and understand cost drivers.

### 冷却架构 / Cooling Architectures

| Architecture | Key Cost Drivers |
|---|---|
| Immersion Cooling / 浸没式冷却 | Tank cost, dielectric fluid, specialized maintenance |
| Direct Liquid Cooling (DLC) / 直冷液冷 | CDU cost, pipe infrastructure, rack modification |
| Traditional Air Cooling / 传统风冷 | CRAC/CRAH units, raised floor, larger footprint |

### 电力架构 / Power Architectures

| Architecture | Key Cost Drivers |
|---|---|
| BESS / 储能系统 | Battery cost, BMS, thermal management |
| Diesel Generator / 柴油发电机 | Fuel infrastructure, maintenance, environmental compliance |
| Grid + UPS / 市电+UPS | Grid interconnection, UPS sizing, battery banks |

### 基础设施架构 / Infrastructure Architectures

| Architecture | Key Cost Drivers |
|---|---|
| Containerized Datacenter / 容器数据中心 | Container cost, modular expansion, transport |
| Traditional Building / 传统机房 | Construction, long lead time, fixed footprint |

> 配套的工程级架构定义见 [[COOLING_SYSTEM_Guideline#§G-3 支持的冷却技术]]、[[POWER_SYSTEMS_Guideline#§P-8 BESS 选型与 DG 对比]]、[[Layout_Guideline#§L-6 容器与机架布局]]。

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

---

## K-6 工作流集成

*Workflow Integration*

Cost Architect workflow:

1. **Read this Guideline first** — Understand cost methodology before analysis (start at [[#K-1 成本建模方法]])
2. **Perform technical analysis** — Evaluate CAPEX structure per domain (see [[#K-2 CAPEX 分类]] and [[#K-3 架构成本对比]])
3. **Apply priority order** — Use [[#K-4 成本优化优先级]] to resolve optimization trade-offs
4. **Output to ATS** — Pass cost comparison results to ATS for integration
5. **Flag conflicts** — If project requirements conflict with this Guideline, escalate to ATS before proceeding

> **Scope reminder**: Cost Architect provides **engineering-level configuration and specification support** (IT load, total facility load, PUE estimate). All commercial pricing is strictly out of scope and must be referred to the account manager.

---

## Changelog

- **v1.1 — 2026-06-05**
  - 章节 ID 全面对齐 [[PRINCIPLE_Guideline#§8 章节 ID 一致性表]]：新增 K-1 ~ K-6 锚点。
    - K-1 成本建模方法（原 "Cost Modeling Methodology"）
    - K-2 CAPEX 分类（原 "CAPEX Component Categories"）
    - K-3 架构成本对比（原 "Architecture Cost Comparison Principles"）
    - K-4 成本优化优先级（原 "Cost Optimization Priority Order"）
    - K-5 边缘部署经济（原 "Edge Deployment Economics"）
    - K-6 工作流集成（原 "Workflow Integration"）
  - 顶部新增"速查 / Quick Reference"块与"章节速查 / Section Index"表，统一指向 [[PRINCIPLE_Guideline]]。
  - 元数据表（Version / Last Updated / Source）从脚注迁移至顶部。
  - 在 §K-3、§K-4、§K-5、§K-6 中加入指向 [[COOLING_SYSTEM_Guideline]] / [[POWER_SYSTEMS_Guideline]] / [[Layout_Guideline]] / [[Risk_Guideline]] 的交叉链接，便于跨 Guideline 引用。
  - §K-6 工作流整合至 Key Matrix 节点序列（先读 Guideline → CAPEX 分析 → 优先级判定 → ATS 输出），与 [[PRINCIPLE_Guideline]] S7 / S12 流程对齐。
  - 文件末尾新增 Changelog 段，符合 CLAUDE.md §6 规则。
  - 内容、文字与所有技术性条目保持原样未改；未新增任何价格或商业化数据。
