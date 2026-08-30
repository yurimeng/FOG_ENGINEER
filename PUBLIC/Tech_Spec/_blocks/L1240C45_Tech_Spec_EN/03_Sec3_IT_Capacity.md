---
title: "L1240C45 Section 3: IT Capacity"
parent: "[[L1240C45_Tech_Spec_EN]]"
order: 3
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/l1240c45"
  - "#thermal"
  - "#MDC"
created: 2026-06-18
source_file: "PUBLIC/Tech_Spec/L1240C45_Tech_Spec_EN.md"
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
| **Total Facility Load** | Varies with PUE — **computed per site at <https://mdcx.org>** | ✅ adjudicated 2026-08-30 (C-2 closed). The former "~1325–1675kW" range is void |
| **PUE** | **`1.0x`** | ✅ adjudicated 2026-08-30. **No fixed value, no range, no "typical value"** — computed per site at <https://mdcx.org> (TCO / Designer). The former "~1.07–1.15 / ~1.25–1.35" figures are void |

> **IT Load ≠ Total Facility Load.** This distinction is a hard rule ([[CLAUDE.md]] Hard Rule 5) and is retained: IT Load determines how much compute is bought; Total Facility Load determines the substation application and the electricity cost model. **But no facility-load figure is given** — it is computed per site with the TCO / Designer at <https://mdcx.org>.
>
> Qualitatively: sites cool enough for the ceiling-unit compressors to stage partially off sit at the low end; hot, DX-dominant sites move PUE up. **No numbers are given.** See [[PRODUCT_SPEC_BASELINE#^baseline-pue]].

---
