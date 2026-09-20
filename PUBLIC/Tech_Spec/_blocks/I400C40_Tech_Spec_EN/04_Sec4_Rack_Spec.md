---
title: "I400C40 Section 4: Immersion Tank / Rack Spec"
parent: "[[I400C40_Tech_Spec_EN]]"
order: 4
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/i400c40"
  - "#MDC"
created: 2026-07-28
source_file: "PUBLIC/Tech_Spec/I400C40_Tech_Spec_EN.md"
source_anchors:
  - "^sec-4-rack-spec"
---

## 4. Immersion Tank / Rack Spec ^sec-4-rack-spec

### 4.1 I50TS immersion tank (single) ^mdc-5f08a87df5

| Item | Spec |
|------|------|
| Model | **I50TS** ^mdc-20a7018596 |
| Quantity | **8** |
| IT capacity | **45kW** recommended / **50kW** max |
| Rack units | **32RU / 29OU** (OCP compatible) |
| Cooling | Single-phase immersion |
| CDU | Built-in **Dual CDU, 1+1 (2N)** |
| Layout | Dual rows against walls, central aisle |
| Bottom piping space | **350–400mm** |

### 4.2 Server compatibility

| Item | Spec |
|------|------|
| Standards | **EIA 19″ / 21″ / OCP (Open Rack V3)** |
| Max server depth | **1000mm** |
| Server class | GPU servers primary |
| Example silicon | 4090 / A100 / H100 / H200 (project-specific) |
| Immersion path | Air-cooled retrofit or immersion-ready servers |

> Single source of truth: [[PUBLIC/Products/I50TS|I50TS server compatibility]]. ^mdc-8585967d31

### 4.3 Air-cooled rack

| Item | Spec |
|------|------|
| Qty / capacity | **1 × 10kW** |
| Rule | **Dedicated CRAC**; must not share immersion loops as sole path |

### 4.4 In-tank PDU (I50TS) ^mdc-6d9c6e3952

| Item | Spec |
|------|------|
| PDU output | ~**3000W**, 207–240Vac / 50–60Hz |
| Outlets | 16 (4×4), reserve 18–20 positions |
| Server power | **2 PDUs** front (dual cord), sealed tank feed-through |
| Control power | PSU to control box |

### 4.5 Lifting / O&M

| Component | Spec | Qty |
|-----------|------|-----|
| Chain hoist | Yalelift YLLHG 500-A, 500kg | 2 |
| Rail | #10 I-beam 100×63×9000mm | 2 |

> TBD: formal oil-drain / lift SOP.

---
