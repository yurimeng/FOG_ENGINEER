---
title: "I400C40 Section 9: Environment & Compliance"
parent: "[[I400C40_Tech_Spec_EN]]"
order: 9
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/i400c40"
  - "#MDC"
created: 2026-07-28
source_file: "PUBLIC/Tech_Spec/I400C40_Tech_Spec_EN.md"
source_anchors:
  - "^sec-9-environment"
---

## 9. Environmental & Compliance ^sec-9-environment

### 9.1 Operating environment

| Item | Spec |
|------|------|
| Ambient (reference) | **-45°C to +45°C** (project climate study) |
| Humidity | Typical DC 40–60% RH non-condensing for air space |
| Altitude | **TBD** (derate cooling/electrical as needed) |
| Design wet-bulb | **28°C** ⏳ **#unconfirmed** (legacy AC40 V1.4, not covered by the baseline table; waiting on I400C40 DESIGN/ documents, expected TBD) ^mdc-bd7ad4f706 |
| Heat-rejection climate gate | Extreme DB **≤24°C** dry cooler; **>24°C** Hybrid |

### 9.2 Fit / no-fit scenarios

| Scenario | Fit |
|----------|-----|
| Dense GPU inference / distributed training | Yes |
| Edge / high power cost (low PUE) | Yes |
| Dry cool climates (DB ≤24°C) | Yes (best PUE) |
| Uncontrolled high humidity enclosure | **No** |
| No outdoor heat rejection plant possible | **No** |
| Customer mandates pure air cooling only | **No** |

### 9.3 Certification

| Item | Status |
|------|--------|
| **Full-system UL** | **❌ Not I400C40 standard** — use **I400C45** ^mdc-31e5f31e64 |
| Component UL | Per BOM / supply chain |
| Field certification | TUV / local AHJ as project requires |
| Enclosure rating | Project-custom |
| External UPS | Customer/integrator responsibility under contract (IEC 62040, etc.) |

### 9.4 I400C40 vs I400C45 compliance ^mdc-c56e26d86f

| | I400C40 | I400C45 ^mdc-ba8058eaa5 |
|--|------|------|
| Form factor | 40ft | 45ft |
| UPS | External | Internal power bay |
| UL full system path | No | Yes |

---
