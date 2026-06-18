---
title: "C-3/C-4 储能系统与数据中心合规"
parent: "[[Compliance_Guideline]]"
order: 2
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/compliance
  - #compliance
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/Compliance_Guideline.md"
source_anchors:
  - "C-3 储能系统合规"
  - "C-4 数据中心合规"
---

## C-3 储能系统合规 / BESS Compliance

Energy storage systems such as BESS require compliance evaluation including:

- **Battery safety standards** — Cell-level and pack-level certification
- **Thermal management safety** — Temperature control limits, thermal runaway prevention
- **Electrical isolation** — High-voltage isolation, grounding, and bonding requirements
- **Fire suppression integration** — Suppression systems compatible with battery chemistry
- **UL 9540** — Standard for Energy Storage Systems and Equipment
- **UL 9540A** — Test Method for Evaluating Thermal Runaway Fire Propagation in Battery Energy Storage Systems

> **Critical**: BESS thermal runaway risk must be addressed with proper suppression and monitoring before deployment.

BESS vs DG 的系统级对比见 [[POWER_SYSTEMS_Guideline#§P-8 BESS 选型与 DG 对比]]；具体 BESS 产品 KB 文档（已通过 [[#C-7 认证要求汇总]] 矩阵验证）位于 `KB/3RD-PARTY/BESS/`，例如 [[Gotion ESC480-125P261-UL]]。

---

## C-4 数据中心合规 / Datacenter Compliance

For datacenter infrastructure, compliance checks include:

| Area / 领域 | Key Requirements / 主要要求 |
|---|---|
| Power system safety / 电力系统安全 | UPS, PDU, and generator compliance |
| Cooling system safety / 冷却系统安全 | Chiller, CRAC/CRAH, pump safety |
| Battery system regulations / 储能系统规范 | BESS integration with facility power |
| Container datacenter requirements / 容器数据中心要求 | Prefabricated modular infrastructure |
| Operational safety / 运维安全 | Lockout/tagout, arc flash, PPE |

> **负荷澄清要求**: 涉及"X MW / X kW"需求时，必须先按 [[POWER_SYSTEMS_Guideline#§P-1 IT 负载定义]] 区分 IT Load 与 Total Facility Load 再做合规判断，避免因负荷定义错误导致合规域被错配（详见 [[Risk_Guideline#§R-4 负荷定义风险]]）。
