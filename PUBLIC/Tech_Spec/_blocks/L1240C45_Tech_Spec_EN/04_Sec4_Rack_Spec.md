---
title: "L1240C45 Section 4: Rack Specifications"
parent: "[[L1240C45_Tech_Spec_EN]]"
order: 4
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/l1240c45"
  - "#thermal"
  - "#MDC"
created: 2026-06-18
source_file: "PUBLIC/Tech_Spec/L1240C45_Tech_Spec_EN.md"
source_anchors:
  - "^sec-4-rack-spec"
---

## 4. Rack Specifications ^sec-4-rack-spec

| Item | Parameter |
|------|-----------|
| Rack Type | 48U Standard Rack |
| Rack Depth | 1200mm |
| Rack Width | 800mm |
| Rack Quantity | 9 racks (8 DLC + 1 air-cooled) |
| Liquid Cooling | Side-Mounted Manifold |
| PDU Position | Rear-mounted |
| Rack Rear Door to Container Wall Gap | 350mm |
| Bottom Cable/Pipe Space | 350–400mm (no raised floor in power distribution zone) |

### 4.1 Cold-Plate Manifold Configuration

| Item | Parameter |
|------|-----------|
| Manifolds per rack | **2** (cold plates ≤ 100) / **3** (cold plates > 100, NVL72-class) |
| Branches per manifold | 20–50 |
| Design flow per branch | **1.6–2.1 L/min** (30%+ margin inside the 1–3 L/min spec) |
| Manifold inlet fitting | **PICV (Pressure-Independent Control Valve) + flow meter** (prevents inter-manifold imbalance) |
| Total manifolds (L1240C45) | **16–24** (8 racks × 2–3 manifolds/rack) ^mdc-c822127653 |
| Imbalance tolerance | ≤ 10% (within a manifold) / ≤ 15% (including inter-manifold) |

---
