---
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/layout
  - #MDC
---
# Layout Guideline / 布局规划技术指南

| Field | Value |
|---|---|
| Document Version / 文档版本 | v1.2 |
| Last Updated / 最后更新 | 2026-06-05 |
| Source / 来源 | `Works_Public/AGENTS/Layout Planner.md` |

---

## 速查 / Quick Reference

本 Guideline 定义 Layout Planner 在容器与机架布局、维护通道净空、线缆敷设、维护可达性、扩展规划及浸没/DLC 专项布局上的设计原则与约束。总体设计原则与跨 Agent 工作流详见 [[PRINCIPLE_Guideline]]。

---

## 章节速查 / Section Index

| 章节 ID | 标题 | 一句话目的 |
|---|---|---|
| [[#§L-1 核心布局原则]] | 核心布局原则 | 可达性、隔离、热管理、线缆规范、扩展预留五大原则 |
| [[#§L-2 维护通道净空]] | 维护通道净空 | 维护通道设计与最小净空要求 |
| [[#§L-3 线缆敷设标准]] | 线缆敷设标准 | 电力 / 网络 / 控制线缆分桥架与冗余预留 |
| [[#§L-4 维护可达性]] | 维护可达性 | 机架、浸没槽、CDU、备件可达性规则 |
| [[#§L-5 扩展规划]] | 扩展规划 | 模块化扩容路径与空间预留要求 |
| [[#§L-6 容器与机架布局]] | 容器与机架布局 | 容器、机架、浸没槽、DLC 机架的物理布局策略 |
| [[#§L-7 工作流集成]] | 工作流集成 | Layout Planner 与 ATS 的协作流程与边界 |

---

## §L-1 核心布局原则 / Core Layout Principles

| Principle | Requirement |
|---|---|
| **Accessibility / 可达性** | All critical equipment must be accessible for maintenance. Service pathways must allow safe technician access at all times. |
| **Isolation / 隔离** | Critical systems should be spatially separated where possible to reduce cascading failure risk. |
| **Thermal Awareness / 热管理意识** | Equipment placement must support proper airflow and thermal management. Do not block supply/return paths. |
| **Cable Discipline / 线缆规范** | Power and network cables must be routed in an organized and maintainable manner. |
| **Expansion Margin / 扩展预留** | Layouts must reserve space for future infrastructure growth. |

相关章节：[[#§L-2 维护通道净空]] · [[#§L-3 线缆敷设标准]] · [[#§L-5 扩展规划]]

---

## §L-2 维护通道净空 / Service Corridor Clearance

Maintenance corridors must be designed from the beginning and must support:

- **Equipment replacement** — Clearance for removing and installing rack-mount or floor-standing equipment
- **Pump maintenance** — Clear access to cooling pumps, CDU units, and fluid handling components
- **Electrical inspection** — Space for qualified personnel to perform arc-flash-safe electrical work
- **Emergency egress** — Corridors must not be obstructed; NFPA life safety codes apply

> **Minimum clearance must be maintained** at all times. Corridors blocked by temporary equipment are non-compliant.

相关合规要求参见 [[Compliance_Guideline#§C-5 容器数据中心合规]]。

---

## §L-3 线缆敷设标准 / Cable Routing Standards

Cable infrastructure must follow structured routing paths. Separate pathways should be considered for:

| Cable Type | Routing Requirement |
|---|---|
| **Power cables / 电力线缆** | Dedicated trays; maintain separation from data cables |
| **Network cables / 网络线缆** | Protected trays; avoid proximity to high-voltage conduits |
| **Control system cables / 控制系统线缆** | Separate from power; may require shielded routing |

- Cable trays must be positioned to **minimize interference with cooling infrastructure**
- Vertical and horizontal cable management must be planned together
- Reserve **spare capacity** in cable trays for future expansion (minimum 30% spare)

网络布线进一步要求详见 [[NETWORK_Guideline#§N-2 核心设计原则]]。

---

## §L-4 维护可达性 / Maintenance Accessibility

- All rack-mounted equipment must be accessible from the front and rear
- Immersion tanks require dedicated service clearance on at least two sides
- CDU units must have clearance for tube connections and pump replacement
- Spare parts storage must be planned within or adjacent to the equipment area
- Equipment layout must support **single-technician maintenance** where possible

运维风险关联参见 [[Risk_Guideline#§R-5 运维风险评估]]。

---

## §L-5 扩展规划 / Expansion Planning

Layouts must support future expansion. Expansion strategies may include:

- Adding additional containers in a modular row
- Adding immersion tanks to an existing cooling loop
- Adding rack rows with minimal reconfiguration
- Extending cable trays and power distribution

> **Space planning must anticipate future infrastructure growth.** Layouts that cannot accommodate at least one future expansion cycle are non-compliant.

扩展与成本风险评估参见 [[Risk_Guideline#§R-7 扩展与成本风险]]。

---

## §L-6 容器与机架布局 / Container & Rack Layout

### Container Infrastructure Layout / 容器基础设施布局

Containerized deployments require highly optimized spatial planning.

Typical container components:
- Compute racks or immersion tanks
- Power distribution systems (PDU, busbar)
- Cooling interfaces (CDU connections, fluid headers)
- Network switches and patch panels
- Maintenance corridors

> Layouts must ensure technicians can **safely access all equipment** without entering restricted or high-voltage zones.

### Rack Layout Strategy / 机架布局策略

Rack placement must consider:

| Factor | Guideline |
|---|---|
| **Power density** | High-density racks (>30kW) require dedicated cooling delivery |
| **Cooling topology** | Rack rows should align with CRAH/CDU supply headers |
| **Maintenance access** | End-of-row racks preferred for heavy equipment access |
| **Cable routing distance** | Keep horizontal cable runs under 100m for structured cabling |
| **Hot/cold aisle alignment** | Strict hot-aisle/cold-aisle separation is mandatory for air-cooled zones |

### Immersion Tank Placement / 浸没式液冷槽布局

Immersion tanks require special layout considerations:

| Factor | Requirement |
|---|---|
| **Tank service clearance** | Minimum 1.2m clearance on service side of each tank |
| **Fluid handling access** | Reserve space for dielectric fluid drums and fill equipment |
| **Pump maintenance access** | Direct line-of-sight to pump modules for removal |
| **Cooling pipe routing** | Pipe headers must not block maintenance corridors |
| **Spill containment** | Floor containment or tank secondary containment required |

> Adequate space must be reserved for **safe fluid management** and emergency response.

### DLC Rack Layout / 直冷液冷机架布局

DLC (Direct Liquid Cooling) racks require careful coordination between:

- Cooling loops (supply and return headers)
- CDU placement (positioned to minimize hose/pipe runs)
- Pipe routing (avoid congestion at rack tops)
- Maintenance access (valve and fitting access clearance)

> Layouts must avoid pipe congestion and ensure **full serviceability of all connection points**.

冷却架构与 IT Zone 匹配规则参见 [[COOLING_SYSTEM_Guideline#§G-8 IT Zone 与冷却区匹配]]；电力设备占地参见 [[POWER_SYSTEMS_Guideline#§P-2 产品对照表]]。

---

## §L-7 工作流集成 / Workflow Integration

Layout Planner workflow:

1. **Read this Guideline first** — Understand layout rules before design
2. **Review Product Catalog** — Reference `./KB/` for container and rack dimensions
3. **Perform technical analysis** — Design layout per domain requirements
4. **Output to ATS** — Pass layout results to ATS for integration
5. **Flag conflicts** — If project requirements conflict with this Guideline, escalate to ATS before proceeding

> **Domain reminder**: Layout Planner focuses exclusively on **physical infrastructure layout** — container placement, equipment positioning, cable routing, and service accessibility. Do not attempt to perform work outside your domain.

跨 Agent 工作流与上报机制详见 [[PRINCIPLE_Guideline]]。

---

## Changelog

### v1.2 — 2026-06-05
- 章节 ID 与 [[PRINCIPLE_Guideline#§8 章节 ID 一致性表]] 对齐：所有章节增加 L-1 ~ L-7 前缀。
- 新增「速查 / Quick Reference」与「章节速查 / Section Index」表。
- 将原「Container Infrastructure Layout」「Rack Layout Strategy」「Immersion Tank Placement」「DLC Rack Layout」四节合并为 §L-6《容器与机架布局》，保留全部原始表格与内容。
- 章节标题统一为「§L-X 中文标题 / English Title」格式。
- 新增跨 Guideline 引用：Compliance §C-5、NETWORK §N-2、Risk §R-5/§R-7、COOLING §G-8、POWER §P-2。
- 文件末尾新增 Changelog 区块（按 CLAUDE.md §6 规则）。

### v1.1 — 2026-04-12
- 初版结构调整。

### v1.0 — 2026-03-10
- 初稿，源自 `Works_Public/AGENTS/Layout Planner.md`。
