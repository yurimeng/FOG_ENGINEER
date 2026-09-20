---
title: "I400C40 Section 6: Power Distribution"
parent: "[[I400C40_Tech_Spec_EN]]"
order: 6
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/i400c40"
  - "#MDC"
created: 2026-07-28
source_file: "PUBLIC/Tech_Spec/I400C40_Tech_Spec_EN.md"
source_anchors:
  - "^sec-6-power"
---

## 6. Power Distribution ^sec-6-power

### 6.1 System power path

```
Grid / BESS → External UPS (EATON 9395XR-600) → In-container PDC → Tanks / PDUs
                ↑
         Optional: ATS ← Generator
```

| Item | Notes |
|------|-------|
| UPS placement | **External (customer-supplied)** — not inside I400C40 ^mdc-2bfad2c1a9 |
| Standard UPS | EATON **9395XR-600** (4×150kW = 600kW), heat ~**7.9kW** |
| UPS batteries | Customer **2×93LiG2** (332kW each), ~**10 min** |
| BESS path | Grid → BESS → I400C40 (Power Zone; **BESS ≠ UPS battery**) ^mdc-368f488653 |

### 6.2 In-container topology

| Item | Notes |
|------|-------|
| Feeds | **Two inputs** per container |
| Facility PDC | Dual feeds via **ATS** → CDUs, CRAC, outdoor plant, auxiliaries |
| IT PDCs | **Two boards**, one per feed → **two PDUs per tank** (A/B) |

> Voltage references: 480V-3P (US) / 400–415V-3P common. Clarify project definition of dual sources.

### 6.3 UPS product comparison

| Product | UPS | Placement | Battery |
|---------|-----|-----------|---------|
| **I400C40** | 9395XR-600 | **External** | ~10 min (2×93LiG2) ^mdc-f28dce07cc |
| I400C45 | 9395XR-600 | Internal power bay | ~20 min ^mdc-8f0456f939 |
| L1240C45 | 9395XR-1500 | Internal | ~8 min (3×93LiG2) ^mdc-6f7d48ee5a |

### 6.4 Optional UPS / battery

Vertiv Liebert EXL S1 + EnergyCore Li5 only if brand/lead-time forces it; ATS + compliance review required. Default remains EATON.

### 6.5 Electrical load schedule (415VAC reference)

Source: I400C40 workload sheet. ^mdc-b736bcab47

**PDC1 (facility) ~57.9kW:** 8×1.7kW Tank-CDU, 2×15kW tower (reference), 10kW CRAC, lighting/fire/monitoring/fresh air, 10kW spare.

**IT-PDC1 / IT-PDC2 each ~381kW:** 8×45kW tanks + 5kW IT rack + 16kW switches.

| Item | Value | Interpretation |
|------|-------|----------------|
| IT-PDC1+2 nameplate sum | ~762kW | **Dual-feed capability**, not concurrent IT |
| Concurrent IT | **360–400kW** | Matches §3 |
| PDC1 auxiliaries | ~57.9kW | Includes outdoor plant references |
| Workbook “total” | ~819.9kW | **Do not treat as concurrent site kW** |

Breaker/cable sizes are design-stage references; verify short-circuit, installation method, voltage drop. External UPS losses counted separately.

### 6.6 Redundancy layers

| Layer | Redundancy |
|-------|------------|
| UPS modules (9395XR-600) | Internal **N+1** among 4 UPMs |
| Tank CDU | **1+1 / 2N** |
| I400C40 IT Zone container | **No internal N+1/2N** ^mdc-95957b0893 |
| MDC system | Multi-container N / N+1 / 2N |

---
