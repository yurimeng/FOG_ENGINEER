---
tags:
  - "#MDC"
  - "#type/design-spec"
  - "#product/dc45"

---
# DC45 — Quick Tech Spec
**PowerPod with Direct Liquid Cooling (45ft Container)**

> **Audience:** This document is a sales / pre-sales deliverable. Target readers: customers, account managers, solution architects. Parameters are normative; if any value conflicts with engineering design, escalate to [[KB/FOG D Series/DESIGN/STD_DC45|STD_DC45]] for the unified reference. Parameter source of truth: V1.4 (2026-05-21).
>
> **配套中文版:** [[DC45_Tech_Spec_CN]]

Version: V1.4 | Date: 2026-05-21

> **V1.4 Update (per [[KB/FOG D Series/DESIGN/DC45 三支路冷却重评估 V4|DC45 Three-Branch Cooling Reassessment V4]]):**
> 1. CDU spec uprated: heat-rejection ≥ 1500 kW / secondary flow ≥ 175 m³/h / secondary head ≥ 220 kPa / VFD secondary pump / 2N or N+1 redundancy
> 2. TCS coolant locked as **PG25** (25% propylene glycol solution); TCS inlet 26–28°C
> 3. Three-branch cooling architecture defined: primary CDU cold plates / 9× VERTIV DCD35 passive RDHX / 9× STULZ OHS-084-DG-FC ceiling units
> 4. Outdoor-side total heat-rejection baseline ≥ 1700 kW
> 5. Cold-plate manifold lock: 2 per rack (≤100 cold plates) or 3 per rack (>100), 1.6–2.1 L/min per branch, PICV + flow meter on every manifold inlet

---

## Document Navigation

| § | Section | Block File |
|---|---------|------------|
| 1 | Layout / 布局图 | [[_blocks/DC45_Tech_Spec_EN/01_Sec1_Layout\|01_Sec1_Layout]] |
| 2 | Product Positioning | [[_blocks/DC45_Tech_Spec_EN/02_Sec2_Positioning\|02_Sec2_Positioning]] |
| 3 | IT Capacity | [[_blocks/DC45_Tech_Spec_EN/03_Sec3_IT_Capacity\|03_Sec3_IT_Capacity]] |
| 4 | Rack Specifications | [[_blocks/DC45_Tech_Spec_EN/04_Sec4_Rack_Spec\|04_Sec4_Rack_Spec]] |
| 5 | Cooling System (Three-Branch TCS PG25 Architecture) | [[_blocks/DC45_Tech_Spec_EN/05_Sec5_Cooling\|05_Sec5_Cooling]] |
| 6 | Power Distribution | [[_blocks/DC45_Tech_Spec_EN/06_Sec6_Power\|06_Sec6_Power]] |
| 7 | Structural Specifications | [[_blocks/DC45_Tech_Spec_EN/07_Sec7_Structural\|07_Sec7_Structural]] |
| 8 | Network & Cable Management | [[_blocks/DC45_Tech_Spec_EN/08_Sec8_Network\|08_Sec8_Network]] |
| 9 | Environmental & Compliance | [[_blocks/DC45_Tech_Spec_EN/09_Sec9_Environment\|09_Sec9_Environment]] |
| 10 | Monitoring & Management System | [[_blocks/DC45_Tech_Spec_EN/10_Sec10_Monitoring\|10_Sec10_Monitoring]] |
| 11 | Fire Protection & Safety | [[_blocks/DC45_Tech_Spec_EN/11_Sec11_Fire\|11_Sec11_Fire]] |
| 12 | Service & Support | [[_blocks/DC45_Tech_Spec_EN/12_Sec12_Service\|12_Sec12_Service]] |
| 13 | Site & Installation Requirements | [[_blocks/DC45_Tech_Spec_EN/13_Sec13_Site\|13_Sec13_Site]] |
| 14 | DC45 Key Specifications Summary | [[_blocks/DC45_Tech_Spec_EN/14_Sec14_Summary\|14_Sec14_Summary]] |

---

## 1. Layout / 布局图 ^sec-1-layout
![[_blocks/DC45_Tech_Spec_EN/01_Sec1_Layout]]

## 2. Product Positioning ^sec-2-positioning
![[_blocks/DC45_Tech_Spec_EN/02_Sec2_Positioning]]

## 3. IT Capacity ^sec-3-it-capacity
![[_blocks/DC45_Tech_Spec_EN/03_Sec3_IT_Capacity]]

## 4. Rack Specifications ^sec-4-rack-spec
![[_blocks/DC45_Tech_Spec_EN/04_Sec4_Rack_Spec]]

## 5. Cooling System (Three-Branch TCS PG25 Architecture) ^sec-5-cooling
![[_blocks/DC45_Tech_Spec_EN/05_Sec5_Cooling]]

## 6. Power Distribution ^sec-6-power
![[_blocks/DC45_Tech_Spec_EN/06_Sec6_Power]]

## 7. Structural Specifications ^sec-7-structural
![[_blocks/DC45_Tech_Spec_EN/07_Sec7_Structural]]

## 8. Network & Cable Management ^sec-8-network
![[_blocks/DC45_Tech_Spec_EN/08_Sec8_Network]]

## 9. Environmental & Compliance ^sec-9-environment
![[_blocks/DC45_Tech_Spec_EN/09_Sec9_Environment]]

## 10. Monitoring & Management System ^sec-10-monitoring
![[_blocks/DC45_Tech_Spec_EN/10_Sec10_Monitoring]]

## 11. Fire Protection & Safety ^sec-11-fire
![[_blocks/DC45_Tech_Spec_EN/11_Sec11_Fire]]

## 12. Service & Support ^sec-12-service
![[_blocks/DC45_Tech_Spec_EN/12_Sec12_Service]]

## 13. Site & Installation Requirements ^sec-13-site
![[_blocks/DC45_Tech_Spec_EN/13_Sec13_Site]]

## 14. DC45 Key Specifications Summary ^sec-14-summary
![[_blocks/DC45_Tech_Spec_EN/14_Sec14_Summary]]

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| V1.4 | 2026-05-21 | Sync with [[DESIGN/DC45 三支路冷却重评估 2026-05-21\|Rev 11 Three-Branch Cooling Reassessment]]: CDU uprated to ≥ 1500 kW / ≥ 175 m³/h / ≥ 220 kPa (VFD + 2N/N+1); TCS fluid locked at PG25; locked 9× DCD35 RDHX + 9× STULZ OHS-084-DG-FC; added §5 Cooling System and §4.1 cold-plate manifold; outdoor-side baseline ≥ 1700 kW. EN: server inlet temperature corrected to 26–28°C; Deployment SOP translated to English. |
| V1.3 | 2026-05-09 | Server inlet temperature revised from 24°C to 26–28°C (TCS range) |

---

*Document Version: V1.4 | Last Updated: 2026-05-21*
