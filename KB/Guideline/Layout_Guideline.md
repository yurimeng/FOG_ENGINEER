---
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/layout
---

# Layout Guideline / 布局规划技术指南

Document Version / 文档版本: v1.0
Last Updated / 最后更新: 2026-03-10
Source / 来源: `Works_Public/AGENTS/Layout Planner.md`

---

## Container and Rack Placement Principles / 容器与机架布局原则

### Core Layout Principles / 核心布局原则

| Principle | Requirement |
|---|---|
| **Accessibility / 可达性** | All critical equipment must be accessible for maintenance. Service pathways must allow safe technician access at all times. |
| **Isolation / 隔离** | Critical systems should be spatially separated where possible to reduce cascading failure risk. |
| **Thermal Awareness / 热管理意识** | Equipment placement must support proper airflow and thermal management. Do not block supply/return paths. |
| **Cable Discipline / 线缆规范** | Power and network cables must be routed in an organized and maintainable manner. |
| **Expansion Margin / 扩展预留** | Layouts must reserve space for future infrastructure growth. |

---

## Service Corridor Clearance Requirements / 维护通道净空要求

Maintenance corridors must be designed from the beginning and must support:

- **Equipment replacement** — Clearance for removing and installing rack-mount or floor-standing equipment
- **Pump maintenance** — Clear access to cooling pumps, CDU units, and fluid handling components
- **Electrical inspection** — Space for qualified personnel to perform arc-flash-safe electrical work
- **Emergency egress** — Corridors must not be obstructed; NFPA life safety codes apply

> **Minimum clearance must be maintained** at all times. Corridors blocked by temporary equipment are non-compliant.

---

## Cable Routing Standards / 线缆敷设标准

Cable infrastructure must follow structured routing paths. Separate pathways should be considered for:

| Cable Type | Routing Requirement |
|---|---|
| **Power cables / 电力线缆** | Dedicated trays; maintain separation from data cables |
| **Network cables / 网络线缆** | Protected trays; avoid proximity to high-voltage conduits |
| **Control system cables / 控制系统线缆** | Separate from power; may require shielded routing |

- Cable trays must be positioned to **minimize interference with cooling infrastructure**
- Vertical and horizontal cable management must be planned together
- Reserve **spare capacity** in cable trays for future expansion (minimum 30% spare)

---

## Maintenance Accessibility Rules / 维护可达性规则

- All rack-mounted equipment must be accessible from the front and rear
- Immersion tanks require dedicated service clearance on at least two sides
- CDU units must have clearance for tube connections and pump replacement
- Spare parts storage must be planned within or adjacent to the equipment area
- Equipment layout must support **single-technician maintenance** where possible

---

## Expansion Planning Constraints / 扩展规划约束

Layouts must support future expansion. Expansion strategies may include:

- Adding additional containers in a modular row
- Adding immersion tanks to an existing cooling loop
- Adding rack rows with minimal reconfiguration
- Extending cable trays and power distribution

> **Space planning must anticipate future infrastructure growth.** Layouts that cannot accommodate at least one future expansion cycle are non-compliant.

---

## Container Infrastructure Layout / 容器基础设施布局

Containerized deployments require highly optimized spatial planning.

Typical container components:
- Compute racks or immersion tanks
- Power distribution systems (PDU, busbar)
- Cooling interfaces (CDU connections, fluid headers)
- Network switches and patch panels
- Maintenance corridors

> Layouts must ensure technicians can **safely access all equipment** without entering restricted or high-voltage zones.

---

## Rack Layout Strategy / 机架布局策略

Rack placement must consider:

| Factor | Guideline |
|---|---|
| **Power density** | High-density racks (>30kW) require dedicated cooling delivery |
| **Cooling topology** | Rack rows should align with CRAH/CDU supply headers |
| **Maintenance access** | End-of-row racks preferred for heavy equipment access |
| **Cable routing distance** | Keep horizontal cable runs under 100m for structured cabling |
| **Hot/cold aisle alignment** | Strict hot-aisle/cold-aisle separation is mandatory for air-cooled zones |

---

## Immersion Tank Placement / 浸没式液冷槽布局

Immersion tanks require special layout considerations:

| Factor | Requirement |
|---|---|
| **Tank service clearance** | Minimum 1.2m clearance on service side of each tank |
| **Fluid handling access** | Reserve space for dielectric fluid drums and fill equipment |
| **Pump maintenance access** | Direct line-of-sight to pump modules for removal |
| **Cooling pipe routing** | Pipe headers must not block maintenance corridors |
| **Spill containment** | Floor containment or tank secondary containment required |

> Adequate space must be reserved for **safe fluid management** and emergency response.

---

## DLC Rack Layout / 直冷液冷机架布局

DLC (Direct Liquid Cooling) racks require careful coordination between:

- Cooling loops (supply and return headers)
- CDU placement (positioned to minimize hose/pipe runs)
- Pipe routing (avoid congestion at rack tops)
- Maintenance access (valve and fitting access clearance)

> Layouts must avoid pipe congestion and ensure **full serviceability of all connection points**.

---

## Workflow Integration / 工作流集成

Layout Planner workflow:

1. **Read this Guideline first** — Understand layout rules before design
2. **Review Product Catalog** — Reference `./KB/` for container and rack dimensions
3. **Perform technical analysis** — Design layout per domain requirements
4. **Output to ATS** — Pass layout results to ATS for integration
5. **Flag conflicts** — If project requirements conflict with this Guideline, escalate to ATS before proceeding

> **Domain reminder**: Layout Planner focuses exclusively on **physical infrastructure layout** — container placement, equipment positioning, cable routing, and service accessibility. Do not attempt to perform work outside your domain.

---

*Document Version: v1.1 | Last Updated: 2026-04-12*
