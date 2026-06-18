---
title: "DC45 Section 2: Product Positioning"
parent: "[[DC45_Tech_Spec_EN]]"
order: 2
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/dc45"
  - "#thermal"
  - "#MDC"
created: 2026-06-18
source_file: "PUBLIC/Tech_Spec/DC45_Tech_Spec_EN.md"
source_anchors:
  - "^sec-2-positioning"
---

## 2. Product Positioning ^sec-2-positioning

DC45 is a **45ft containerized modular data center with Direct Liquid Cooling (DLC)**, employing cold-plate liquid cooling technology for ultra-high-density AI/HPC cluster deployments.

![[PDC_SLD_EN_light.svg|SuOCbROt9ozRtAxyvDrcBiXnnqc.png]]

> **Cooling Architecture**: DC45 uses a **three-branch parallel TCS loop on PG25**, with all heat carried to the outdoor side (hybrid dry-cooler + DX) via the TCS secondary loop:
> - **Branch 1 — Primary CDU cold-plate loop**: 73% liquid-cooled heat from 8× DLC racks
> - **Branch 2 — 9× passive RDHX**: absorbs 47–55% of rear-door exhaust air heat
> - **Branch 3 — 9× ceiling-mounted STULZ OHS-084-DG-FC**: handles residual room air heat + UPS/auxiliary heat

---
