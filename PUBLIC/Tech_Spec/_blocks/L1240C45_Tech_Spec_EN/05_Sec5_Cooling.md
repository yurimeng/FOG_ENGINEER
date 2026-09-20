---
title: "L1240C45 Section 5: Cooling System (Three-Branch TCS PG25)"
parent: "[[L1240C45_Tech_Spec_EN]]"
order: 5
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/l1240c45"
  - "#thermal"
  - "#MDC"
created: 2026-06-18
source_file: "PUBLIC/Tech_Spec/L1240C45_Tech_Spec_EN.md"
source_anchors:
  - "^sec-5-cooling"
---

## 5. Cooling System (Three-Branch TCS PG25 Architecture) ^sec-5-cooling

### 5.1 TCS Overview

| Item | Parameter |
|------|-----------|
| Circulating fluid | **PG25** (25% propylene-glycol/water; all wetted equipment must be PG-compatible) |
| TCS inlet temperature | 26–28°C |
| TCS design ΔT | 10 °C (CDU secondary) / 8 °C (RDHX branch) |
| Total circulating flow (S-Max) | ≈ 148 m³/h |
| Total circulating flow (φ_air = 8% case) | ≈ 154 m³/h ← design ceiling |
| Total heat rejected (S-Max) | ≈ 1352 kW |
| Total TDH | 19–25 m H₂O |
| TCS main pump | **Nameplate 200 m³/h @ 25 m H₂O, PG-compatible impeller/seals, VFD, 2N or N+1** |
| Outdoor-side heat-rejection baseline | **≥ 1700 kW** (hybrid dry-cooler + DX plate-HX combo) |

### 5.2 Primary CDU (Branch 1)

| Item | Parameter |
|------|-----------|
| Heat-rejection capacity | **≥ 1500 kW** |
| Secondary-side flow | **≥ 175 m³/h** |
| Secondary-side head | **≥ 220 kPa (≈ 22 m H₂O)** |
| Secondary pump | **VFD-driven** |
| Redundancy | **2N or N+1** secondary pumps |
| Branch 1 design flow (S-Max) | 78 m³/h |
| Branch 1 design flow (φ_air = 8% ceiling) | 98.6 m³/h |
| Branch 1 ΔP | 47–128 kPa (varies with φ_air) |
| Served load | 8 × DLC racks cold plates (109.5 kW liquid load per rack) |

### 5.3 RDHX Branch (Branch 2)

| Item | Parameter |
|------|-----------|
| Quantity & model | **9 × VERTIV CoolLoop DCD35 (passive)**: 8 on DLC rack rear doors + 1 on the air-cooled rack rear door |
| Nominal capacity per unit | 35 kW (max 66 kW) |
| Max airflow per unit | 11,200 m³/h |
| Max water flow per unit | 5.3 m³/h |
| Water connection | DN25 (1") |
| Operating air inlet range | datasheet 10–40°C ⚠️ L1240C45 S-Max 41–48°C exceeds limit by 1–8°C, under Vertiv review ^mdc-624e545e0e |
| Actual air-heat absorption (TCS 26–28°C) | 47–55% (ε ≈ 0.55 passive-RDHX physical ceiling) |
| Branch 2 design flow (PG25) | ≈ 21 m³/h |
| Branch 2 ΔP | 36–62 kPa |

### 5.4 Ceiling-Mounted CeilAir Branch (Branch 3)

| Item | Parameter |
|------|-----------|
| Quantity & model | **9 × STULZ OHS-084-DG-FC** (self-contained DX with free-cooling loop, EG/PG compatible) |
| Nominal total cooling per unit | 25.6 kW (80°F DB / 67°F WB / 50% RH) |
| Sensible cooling per unit (L1240C45 conditions, PG25 27°C) | ≈ 26 kW (+13% PG25 uplift + +10% return-air temperature correction + +5% low-humidity correction) ^mdc-40330ce224 |
| 9-unit total sensible | ≈ 234 kW |
| Compressor input per unit | 8.2 kW (datasheet) / ≈ 6.4 kW (after PG25 27°C uplift) |
| Condenser flow per unit | **5.41 m³/h** (23.8 GPM, locked from datasheet) |
| Condenser ΔP per unit | 41.5 kPa @ EG40 / ≈ 48 kPa (PG25 corrected, +15%) |
| Weight per unit | 250 kg (~ 2250 kg total roof load for 9 units; requires structural review) |
| Branch 3 design flow | **48.7 m³/h** |
| Branch 3 ΔP | 63–73 kPa |
| Installation | Evenly distributed along container roof (13.7 m length) |

### 5.5 Three-Branch Hydraulic Summary (PG25, S-Max)

| Branch | Design flow | Peak-case flow | ΔP | TCS heat recovered |
|--------|------------|----------------|-----|-------------------|
| Branch 1 — Primary CDU cold plates | 78 m³/h | 98.6 m³/h @ φ_air=8% | 47–128 kPa | 876 kW |
| Branch 2 — 9× RDHX | 21 m³/h | 21 m³/h | 36–62 kPa | ≈ 189 kW |
| Branch 3 — 9× CeilAir | 48.7 m³/h | 48.7 m³/h | 63–73 kPa | ≈ 287 kW (incl. ~58 kW compressor input) |
| **TCS Total** | **≈ 148 m³/h** | **≈ 154 m³/h** | TDH 19–25 m H₂O | **≈ 1352 kW** |

### 5.6 Control Strategy

| Control layer | Logic |
|---------------|-------|
| **Flow distribution** | Every branch has a **PICV (Pressure-Independent Control Valve)** that holds setpoint flow regardless of upstream ΔP swings |
| **Cold-plate branch → GPU interlock** | Branch 1 flow < 70 m³/h → GPU throttle to 80%; < 60 m³/h → GPU throttle to 60% |
| **RDHX branch** | Any single RDHX < 1.5 m³/h → that rack's GPUs throttle + alarm |
| **CeilAir branch** | Branch 3 < 40 m³/h → alarm + roof-supply temperature trending |
| **CeilAir redundancy** | All 9 roof positions are occupied — no N+1; failure mitigation relies on GPU throttling |
| **Free Cooling (FC)** | The -FC variant carries a free-cooling loop; L1240C45's 26–28°C TCS sits above typical FC activation thresholds (< 10°C), so FC stays dormant under normal operation ^mdc-56dd8a2f66 |

---
