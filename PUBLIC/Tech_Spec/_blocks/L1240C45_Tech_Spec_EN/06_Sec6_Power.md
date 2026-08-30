---
title: "L1240C45 Section 6: Power Distribution"
parent: "[[L1240C45_Tech_Spec_EN]]"
order: 6
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/l1240c45"
  - "#thermal"
  - "#MDC"
created: 2026-06-18
source_file: "PUBLIC/Tech_Spec/L1240C45_Tech_Spec_EN.md"
source_anchors:
  - "^sec-6-power"
---

## 6. Power Distribution ^sec-6-power

### 6.1 POD Main Distribution

Power Distribution SLD

![[PDC_SLD_EN_light.svg|SuOCbROt9ozRtAxyvDrcBiXnnqc.png]]

| Device | Qty | Notes |
|--------|-----|-------|
| Incoming Switchgear | 1 panel | Main breaker / CT / metering |
| UPS Main Cabinet | 1 panel | Online double-conversion, includes static bypass transfer logic |
| Bypass Panel | 1 panel | Contains MCCB + mechanical interlock (prevents both paths closing simultaneously) |
| Battery Bank (BESS) | Standalone config | Capacity based on backup time requirement |
| Busbar System | 1 set | **SIEMENS 2500A** enclosed plug-in busbar, includes end feed box |

**Tap-off Unit (TOU) Configuration:**

| Load Type | Qty | Current per Unit | MCB Rating |
|-----------|-----|-----------------|------------|
| DLC Water-Cooled Racks | 8 | ~200A | 250A MCB |
| Air-Cooled Rack | 1 | ~80A | 100A MCB |
| Main CDU (≥1500 kW, VFD secondary pump) | 1 | ~35A* | 50A MCB* |
| Ceiling-Mounted STULZ OHS-084-DG-FC | 9 | ~15A* | 20A MCB* |
| TCS Main Circulating Pump + RDHX Controllers | 1 group | ~20A* | 32A MCB* |

> *Current and MCB values are upper-bound estimates derived from the V1.4 three-branch cooling architecture. Power Engineer must verify against actual nameplate ratings at BOM lock (9× CeilAir total compressor input ≈ 58 kW; including fans + controls ≈ 70 kW).

### 6.2 Rack PDU

| Item | Parameter |
|------|-----------|
| Input Rating | **60A 415V** |
| Output Interface | **24-position C19 Output** |
| Protection | **Magnetic Hydraulic Circuit Breaker** |
| Power Cable | **1.5m AWG Cable** (factory pre-installed) |
| Installation Position | Rear-mounted |
| Monitoring | Current monitoring (PDU panel display) |

> **PDU model comparison is not presented in this document.** Competitor comparison is internal analysis and must not appear in customer-facing documents per [[CLAUDE.md]] Hard Rule 3; request the internal analysis from ATS if a comparison is genuinely needed.

---
