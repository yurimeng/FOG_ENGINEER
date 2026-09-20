---
title: §G-8 IT Zone 配对 + §G-9 环境设计
parent: "[[../COOLING_SYSTEM_Guideline]]"
order: 5
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/cooling
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/COOLING_SYSTEM_Guideline.md"
source_anchors: []
---

## §G-8 IT Zone 与冷却区匹配 (IT Zone & Cooling Zone Matching)

### 8.1 Mandatory 1:1 Pairing

**Each IT Zone container must have its own dedicated Cooling Zone unit. N+1 and 2N redundancy are NOT offered for the Cooling Zone.**

| IT Zone Type | Cooling Zone Requirement | Cooling Capacity |
|-------------|------------------------|-----------------|
| AC40 | 1× Hybrid Cooling System | ~600kW class ^mdc-9505f3c65a |
| DC45 | 1× Hybrid Cooling System | ~1200kW class ^mdc-6b6519c430 |
| A32 | 1× Hybrid Cooling System | ~320kW class ^mdc-63bc494574 |

> Each cooling device is matched to one specific IT Zone device. Do not size one cooling unit to serve multiple IT Zone containers.

### 8.2 Redundancy Constraints

| Zone | N+1 | 2N | Notes |
|------|-----|----|-------|
| IT Zone | ❌ Not offered | ❌ Not offered | Each container independent |
| **Cooling Zone** | **❌ Not offered** | **❌ Not offered** | 1:1 pairing with IT Zone |
| Power Zone | ✅ Allowed (needs extra switchgear) | ✅ Allowed (needs extra switchgear) | — |

冷却层不提供冗余的硬约束同步登记在 [[#§G-11 冗余策略]] 与 [[#§G-18 上报规则]]。

---

## §G-9 环境设计 (Environmental Design)

Cooling systems must consider local environmental conditions.

Key factors:
- Ambient temperature
- Seasonal temperature variation
- Humidity
- Dust or environmental contamination
- Water availability

Cooling systems must operate reliably under extreme weather conditions. 极端条件下的运行要求见 [[#§G-13 极端条件运行]]。
