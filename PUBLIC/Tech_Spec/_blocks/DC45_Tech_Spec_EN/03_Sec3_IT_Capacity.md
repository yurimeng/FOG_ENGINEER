---
title: "DC45 Section 3: IT Capacity"
parent: "[[DC45_Tech_Spec_EN]]"
order: 3
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/dc45"
  - "#thermal"
  - "#MDC"
created: 2026-06-18
source_file: "PUBLIC/Tech_Spec/DC45_Tech_Spec_EN.md"
source_anchors:
  - "^sec-3-it-capacity"
---

## 3. IT Capacity ^sec-3-it-capacity

| Item | Parameter |
|------|-----------|
| **Total IT Capacity** | **1240kW** |
| DLC Racks | 8 × 150kW (150kW per rack, 73% liquid-cooled / 27% air-cooled) |
| Air-Cooled Rack | 1 × 40kW |
| TCS Inlet Temperature | **26–28°C** (CDU secondary supply to cold plates / RDHX / CeilAir condensers) |
| Rack Front Intake Temperature | **25–27°C** (CeilAir DX evaporator output 12–18°C, decoupled from TCS water temperature) |
| Server Exhaust Temperature | **41–48°C** at S-Max (exceeds DCD35 datasheet 40°C inlet ceiling by 1–8°C; under Vertiv review) |
| DLC Air-Cool Ratio (φ_air) | Design upper limit **27%**, CDU guardrail ≥ **8%** |
| Power Factor (UPS Output Side) | 0.9 |

### IT Load vs. Total Facility Load

| Item | Value | Notes |
|------|-------|-------|
| **IT Load** | 1240kW | Actual server/GPU consumption |
| **Total Facility Load** | ~1325–1675kW | Depends on PUE |
| **PUE (Low temp zone, dry cooler priority)** | ~1.07–1.15 | Low ambient; CeilAir compressors partially stage off |
| **PUE (High temp zone, DX-dominant)** | ~1.25–1.35 | High ambient; 9× CeilAir compressors run ~58 kW total |

---
