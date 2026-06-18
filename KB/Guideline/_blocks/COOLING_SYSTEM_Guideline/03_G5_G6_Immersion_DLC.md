---
title: §G-5 浸没式冷却 + §G-6 直冷液冷
parent: "[[../COOLING_SYSTEM_Guideline]]"
order: 3
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/cooling
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/COOLING_SYSTEM_Guideline.md"
source_anchors: []
---

## §G-5 浸没式冷却 (Immersion Cooling)

Immersion cooling is the preferred cooling method for high-density computing workloads.

**Advantages:**
- High thermal efficiency
- Uniform heat removal
- Reduced mechanical complexity
- Elimination of large air handling systems

**Particularly suitable for:**
- AI training clusters
- GPU dense compute
- High power density racks

---

## §G-6 直冷液冷 (Direct Liquid Cooling)

DLC is appropriate when:
- Hardware cannot be immersed
- Standard rack infrastructure must be preserved
- Cooling must be integrated with existing datacenter environments

DLC systems typically require:
- Cold plate loops
- Coolant distribution units (CDU)
- External heat rejection systems

与 [[#§G-7 热排放系统]] 配合选择外部散热方案。
