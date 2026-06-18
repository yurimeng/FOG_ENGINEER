---
title: "K-3 架构成本对比"
parent: "[[Cost_Guideline]]"
order: 2
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/cost
  - #cost
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/Cost_Guideline.md"
source_anchors:
  - "K-3 架构成本对比"
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
