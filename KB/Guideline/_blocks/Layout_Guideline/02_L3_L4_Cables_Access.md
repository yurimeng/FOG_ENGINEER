---
title: "L-3/L-4 线缆敷设与维护可达性"
parent: "[[Layout_Guideline]]"
order: 2
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/layout
  - #layout
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/Layout_Guideline.md"
source_anchors:
  - "§L-3 线缆敷设标准"
  - "§L-4 维护可达性"
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
