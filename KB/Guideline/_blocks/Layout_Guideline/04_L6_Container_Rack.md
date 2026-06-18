---
title: "L-6 容器与机架布局"
parent: "[[Layout_Guideline]]"
order: 4
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/layout
  - #layout
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/Layout_Guideline.md"
source_anchors:
  - "§L-6 容器与机架布局"
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
