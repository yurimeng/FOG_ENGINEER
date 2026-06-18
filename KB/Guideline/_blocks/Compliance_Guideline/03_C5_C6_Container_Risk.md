---
title: "C-5/C-6 容器数据中心与合规风险识别"
parent: "[[Compliance_Guideline]]"
order: 3
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/compliance
  - #compliance
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/Compliance_Guideline.md"
source_anchors:
  - "C-5 容器数据中心合规"
  - "C-6 合规风险识别"
---

## C-5 容器数据中心合规 / Container Datacenter Compliance

Containerized infrastructure must be evaluated for:

- **Structural integrity** — Wind load, seismic, transportation structural requirements
- **Electrical integration** — Busbar, cable routing, grounding within confined space
- **Cooling system safety** — Indoor/outdoor operation, humidity control
- **Emergency access and maintenance** — Egress pathways, maintenance clearance, fire exit requirements
- **Environmental ratings** — NEMA/IP ratings for enclosure protection

> 与 [[Layout_Guideline#§L-6 容器与机架布局]] 中的物理布局约束互为前置：合规结论必须基于已完成维护通道净空与扩展规划验证的布局版本。

---

## C-6 合规风险识别 / Compliance Risk Detection

Compliance Officer must flag the following risk conditions:

- Uncertified equipment in critical infrastructure
- Electrical design conflicts with local codes
- Insufficient safety isolation (HV/LV boundaries)
- Cooling systems introducing safety hazards (flood risk, condensation, refrigerant leaks)
- BESS thermal runaway propagation potential
- Missing or inadequate fire suppression coverage
- Non-compliant cable management and tray routing

> 上述任何一条被触发即对应 [[Risk_Guideline#§R-3 工程红旗]] 中的 Critical 或 High 风险，必须在 [[#C-8 工作流集成]] 的工作流中**立即上报 ATS**，不得通过降级风险等级规避升级。
