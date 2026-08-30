---
title: "I400C40 Section 5: Cooling"
parent: "[[I400C40_Tech_Spec_EN]]"
order: 5
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/i400c40"
  - "#MDC"
created: 2026-07-28
source_file: "PUBLIC/Tech_Spec/I400C40_Tech_Spec_EN.md"
source_anchors:
  - "^sec-5-cooling"
---

## 5. Cooling (Immersion + Hybrid Rejection) ^sec-5-cooling

### 5.1 Architecture

| Loop | Medium | Role |
|------|--------|------|
| Secondary | Castrol **DC20** / Shell **S5LV** dielectric | Immerse IT; heat via in-tank CDU HX |
| Primary | ~25% vol. EG water (design) | Facility loop to outdoor rejection |
| Air | Air | 1×10kW rack + CRAC, independent |

![[I50TS Flow_v1.svg]]
*I50TS / I400C40 thermal path*

### 5.2 Design conditions (standard product)

| Item | Spec |
|------|------|
| Design wet-bulb | **28°C** ⏳ **#unconfirmed** — taken from the legacy AC40 V1.4 baseline; not covered by [[PRODUCT_SPEC_BASELINE]]. Waiting on I400C40 DESIGN/ engineering documents (shop drawings / weighing report / structural calculation) to be issued and written back to the baseline table — expected TBD |
| Secondary oil | **Inlet ≤35°C / outlet ≈43°C, ΔT=8K** |
| Facility water | **≤32 / 37°C (ΔT=5K)** ⏳ **#unconfirmed** — [[PRODUCT_SPEC_BASELINE]] §2.2 carries site evidence for I400C45 only; the same temperatures for I400C40 are derived. Waiting on Cooling Engineer to confirm whether I400C40 runs the same water temperatures and to write it back to the baseline table — expected TBD |
| Coolant | DC20 or S5LV (S5LV cp = **2.306 kJ/kg·°C**) |
| Design basis | [[COOLING_SYSTEM_Guideline]] |

### 5.3 In-tank CDU (secondary)

| Item | Spec |
|------|------|
| Config | **2 CDUs per tank**, mirrored hot-standby |
| Per CDU | 2× pumps + 1× plate HX + sensors + e-3way |
| Redundancy | **1+1 / 2N** |
| Service | Hot-swap pumps/HX; drainable before removal |

### 5.4 Secondary flow check (I50TS §5.4)

Using S5LV cp and ΔT=8°C (ρ≈0.8 kg/L provisional):

| Case | Tank Q | Vol. flow V |
|------|--------|-------------|
| Recommended | 45kW | ≈ **11.0 m³/h** |
| Maximum | 50kW | ≈ **12.2 m³/h** |

**Full container (8 tanks):**

| Case | Total Q | Secondary total flow |
|------|---------|----------------------|
| Recommended | 360kW | ≈ **87.8 m³/h** ⏳ **#unconfirmed** — taken from the legacy AC40 V1.4 baseline; not covered by [[PRODUCT_SPEC_BASELINE]]. Waiting on I400C40 DESIGN/ engineering documents (shop drawings / weighing report / structural calculation) to be issued and written back to the baseline table — expected TBD |
| Maximum | 400kW | ≈ **97.6 m³/h** ⏳ **#unconfirmed** (legacy AC40 V1.4, not covered by the baseline table; waiting on I400C40 DESIGN/ documents, expected TBD) |

> ⚠️ Density/cp verification pending; validate pumps, HX, and velocity at ΔT=8K / inlet ≤35°C.

### 5.5 Outdoor heat rejection (site climate)

| Condition | Selection |
|-----------|-----------|
| Extreme dry-bulb **≤24°C** | **Dry cooler only (free cooling)** |
| Extreme dry-bulb **>24°C** | **Hybrid Chiller** (dry + DX) |

> Per [[COOLING_SYSTEM_Guideline]] §G-7. One Cooling Zone per I400C40; system N+1 via more containers, not shared chillers.

### 5.6 Air branch

Independent 1×10kW rack + CRAC (~10kW in electrical schedule).

### 5.7 Failure modes

| Failure | Impact | Risk |
|---------|--------|------|
| Single CDU | None (2N) | Low |
| Dual CDU | Tank outage | High |
| Single pump in CDU | Auto flow control | Low |
| Hybrid / dry cooler loss | Temperature rise / derate | Medium |
| Fouled HX / filter | Reduced heat transfer | Medium |

### 5.8 Controls

Temperature setpoints, pump VFD, primary valves; monitoring of oil temps, level, conductivity, pressure; SNMP / Modbus / Redfish.

---
