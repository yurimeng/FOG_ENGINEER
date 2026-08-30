---
title: "I400C40 Section 2: Product Positioning"
parent: "[[I400C40_Tech_Spec_EN]]"
order: 2
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/i400c40"
  - "#MDC"
created: 2026-07-28
source_file: "PUBLIC/Tech_Spec/I400C40_Tech_Spec_EN.md"
source_anchors:
  - "^sec-2-positioning"
---

## 2. Product Positioning ^sec-2-positioning

I400C40 is a **40ft containerized single-phase immersion modular data center** with **8× I50TS** immersion tanks, targeting high-performance AI inference, distributed training, and edge compute.

| Dimension | Positioning |
|-----------|-------------|
| Product family | IMMERSION (immersion) |
| IT Zone role | Standard MDC compute unit (mixable with L1240C45) |
| GPU platform | Primarily PCIe (H100 / H200 / 4090 / A100, etc.) |
| Network | Ethernet-first (10G/25G/100G/400G upgrade path) |
| UPS | **External (customer-supplied)** — not in I400C40 envelope |
| Full-system UL | **No** (use [[I400C45]] when UL is required) |

> **Cooling architecture (two loops + air branch):**
> - **Secondary (dielectric):** servers immersed → in-tank Dual CDU (HX) → heat to facility loop
> - **Primary (water / EG):** Hybrid Chiller or dry cooler rejects heat outdoors
> - **Air branch:** independent 1×10kW air-cooled rack + CRAC — **not shared** with immersion loops

```
IT Load → Dielectric Fluid (Tank) → Dual CDU (in-tank) → Facility Water / EG
                                              ↓
                         Hybrid Chiller or dry cooler (climate-selected)
```

| Product | Form factor | IT capacity | Cooling | UPS | UL |
|---------|-------------|-------------|---------|-----|-----|
| **I50TS** | Single tank | 45–50kW | Immersion | External | — |
| **I400C40** | 40ft | 360–400kW | Immersion | **External** | ❌ |
| **I400C45** | 45ft | 400kW | Immersion | Internal power bay | ✅ |
| **L1240C45** | 45ft | 1240kW | DLC cold plate | Internal | ✅ |

---
