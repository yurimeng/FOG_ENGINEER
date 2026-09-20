---
tags:
  - "#MDC"
  - "#type/design-spec"
  - "#product/l1240c45"
  - "#unconfirmed"
doc_version: v1.6
updated: 2026-08-30
sku_id: L1240C45SUR150
---
# L1240C45 — Tech Spec ^mdc-0423c170df
**PowerPod with Direct Liquid Cooling (45ft Container)**

> **SKU identity:** short alias **L1240C45** · full SKU ID `L1240C45SUR150` · product line **Liquid Cooling (L)** · status **shipped**. Naming baseline: [[NAMING_MAP]]. ^mdc-42d4aeb0ee
>
> **Audience:** This document is a sales / pre-sales deliverable. Target readers: customers, account managers, solution architects. Parameters are normative; if any value conflicts with engineering design, escalate to [[STD_L1240C45|STD_L1240C45]] for the unified reference. Parameter source of truth: V1.4 (2026-05-21).
>
> **Source of truth:** product parameters follow [[PRODUCT_SPEC_BASELINE]] (six-SKU baseline table); **where this document disagrees with it, the baseline table governs**. Engineering-parameter disputes specific to L1240C45 still escalate through [[STD_L1240C45]]. ^mdc-1d63d1fd9f
>
> **Three companion editions:** English internal (this file) · 中文内部版 [[L1240C45_Tech_Spec_CN]] · external edition [[L1240C45_Tech_Spec_External]]
>
> ✅ **Yuri's rulings of 2026-08-30 are propagated here ([[PRODUCT_SPEC_BASELINE]] v2.0):** §3 PUE and Total Facility Load become `1.0x` / computed per site at <https://mdcx.org>; §12 lead time becomes 120 days EXW first batch, 90 days EXW for Scale, dummy-load burn-in 5–30 days, with no commitment on the commercial, freight or installation segments; §12 and §14 warranty becomes core components for one year from EXW plus an annual service fee, with response levels governed by the Invoice. The previous ⛔ lead-time conflict is closed.
>
> ⏳ **This document still carries a document-level `#unconfirmed`:** several rows remain TBD (§9.1 operating altitude, §13 on-site commissioning and local permits). Who / what / when for each is given in the relevant section. Marker semantics: [[UNCONFIRMED_Convention]] §2. **Do not release this edition as-is** — use the external edition for customers.

Version: V1.6 | Date: 2026-08-30 | Parameter baseline: V1.4 (2026-05-21)

> **V1.4 Update (per the then-current Three-Branch Cooling Reassessment V4; V4 is now dot-archived — the current revision is [[KB/LIQUID/L1240C45/DESIGN/L1240C45 三支路冷却重评估 V5|Three-Branch Cooling Reassessment V5]]):** ^mdc-e4c1ed5d81
> 1. CDU spec uprated: heat-rejection ≥ 1500 kW / secondary flow ≥ 175 m³/h / secondary head ≥ 220 kPa / VFD secondary pump / 2N or N+1 redundancy
> 2. TCS coolant locked as **PG25** (25% propylene glycol solution); TCS inlet 26–28°C
> 3. Three-branch cooling architecture defined: primary CDU cold plates / 9× VERTIV DCD35 passive RDHX / 9× STULZ OHS-084-DG-FC ceiling units
> 4. Outdoor-side total heat-rejection baseline ≥ 1700 kW
> 5. Cold-plate manifold lock: 2 per rack (≤100 cold plates) or 3 per rack (>100), 1.6–2.1 L/min per branch, PICV + flow meter on every manifold inlet

---

## Document Navigation

| § | Section | Block File |
|---|---------|------------|
| 1 | Layout / 布局图 | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/01_Sec1_Layout\|01_Sec1_Layout]] |
| 2 | Product Positioning | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/02_Sec2_Positioning\|02_Sec2_Positioning]] |
| 3 | IT Capacity | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/03_Sec3_IT_Capacity\|03_Sec3_IT_Capacity]] |
| 4 | Rack Specifications | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/04_Sec4_Rack_Spec\|04_Sec4_Rack_Spec]] |
| 5 | Cooling System (Three-Branch TCS PG25 Architecture) | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/05_Sec5_Cooling\|05_Sec5_Cooling]] |
| 6 | Power Distribution | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/06_Sec6_Power\|06_Sec6_Power]] |
| 7 | Structural Specifications | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/07_Sec7_Structural\|07_Sec7_Structural]] |
| 8 | Network & Cable Management | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/08_Sec8_Network\|08_Sec8_Network]] |
| 9 | Environmental & Compliance | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/09_Sec9_Environment\|09_Sec9_Environment]] |
| 10 | Monitoring & Management System | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/10_Sec10_Monitoring\|10_Sec10_Monitoring]] |
| 11 | Fire Protection & Safety | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/11_Sec11_Fire\|11_Sec11_Fire]] |
| 12 | Service & Support | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/12_Sec12_Service\|12_Sec12_Service]] |
| 13 | Site & Installation Requirements | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/13_Sec13_Site\|13_Sec13_Site]] |
| 14 | L1240C45 Key Specifications Summary | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/14_Sec14_Summary\|14_Sec14_Summary]] ^mdc-2959af9a87 |

---

## 1. Layout / 布局图 ^sec-1-layout
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/01_Sec1_Layout]]

## 2. Product Positioning ^sec-2-positioning
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/02_Sec2_Positioning]]

## 3. IT Capacity ^sec-3-it-capacity
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/03_Sec3_IT_Capacity]]

## 4. Rack Specifications ^sec-4-rack-spec
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/04_Sec4_Rack_Spec]]

## 5. Cooling System (Three-Branch TCS PG25 Architecture) ^sec-5-cooling
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/05_Sec5_Cooling]]

## 6. Power Distribution ^sec-6-power
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/06_Sec6_Power]]

## 7. Structural Specifications ^sec-7-structural
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/07_Sec7_Structural]]

## 8. Network & Cable Management ^sec-8-network
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/08_Sec8_Network]]

## 9. Environmental & Compliance ^sec-9-environment
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/09_Sec9_Environment]]

## 10. Monitoring & Management System ^sec-10-monitoring
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/10_Sec10_Monitoring]]

## 11. Fire Protection & Safety ^sec-11-fire
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/11_Sec11_Fire]]

## 12. Service & Support ^sec-12-service
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/12_Sec12_Service]]

## 13. Site & Installation Requirements ^sec-13-site
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/13_Sec13_Site]]

## 14. L1240C45 Key Specifications Summary ^sec-14-summary
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/14_Sec14_Summary]]

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| V1.6 | 2026-08-30 | **Yuri's four rulings of 2026-08-30 propagated ([[PRODUCT_SPEC_BASELINE]] v2.0).** (1) **PUE is written `1.0x` everywhere** — the §3 figures ~1.07–1.15 / ~1.25–1.35 and the ~1325–1675 kW Total Facility Load range are void, replaced by "varies with PUE, computed per site at <https://mdcx.org> (TCO / Designer)"; the §3 IT Load vs Total Facility Load distinction is retained as a hard rule. (2) **Lead time is unified to 120 days EXW for the first batch and 90 days EXW for Scale, counted from order placement**, with a new dummy-load burn-in period of 5–30 days (Supermicro recommendation, outside the EXW commitment); the commercial, freight and installation segments carry no commitment. The §12 "~185–230 days" figure and the four-phase deployment SOP table are **deleted**, and the previous ⛔ conflict block is replaced by the adjudicated wording. (3) **Warranty is unified to core components for one year from EXW plus an annual service fee thereafter**; "9×5 NBD" and "1 year / 9×5 NBD" are **deleted** from §12 and §14 — response levels are governed by the Invoice. (4) The dual-loop GPU-side temperature ruling (GPU 36–40 °C) does not apply to this single-loop 26–28 °C TCS SKU and nothing was changed for it. Block files 03 / 12 / 14 updated in step. |
| V1.5 | 2026-08-30 | Refreshed to the 2026-08-30 naming and data baseline. (1) Naming aligned to [[NAMING_MAP]]: DC45 → **L1240C45** across the title, body and block-file frontmatter `title` fields; historical changelog wording and legacy document-version citations are preserved per [[NAMING_MAP]] §4. (2) SKU identity line added at the top: full SKU ID `L1240C45SUR150` · Liquid Cooling line · status shipped. (3) CN / EN / External cross-links established. (4) Source-of-truth pointer added: parameters follow [[PRODUCT_SPEC_BASELINE]], the baseline table governs on conflict, and engineering-parameter disputes still escalate through [[STD_L1240C45]]. (5) **§6.3 "PDU Model Comparison" removed** — the table placed this product beside a competitor PDU in a document whose stated audience is customers, breaching [[CLAUDE.md]] Hard Rule 3 — and replaced with a one-line note. (6) A ⛔ conflict block was added above the §12 tables: "~185–230 days" (total on-site cycle) and baseline §3.1 "90 days EXW, buyer-arranged freight" are two different bases and neither may be quoted alone to a customer until adjudicated; **all existing figures retained**. (7) frontmatter gained `#unconfirmed` / `doc_version` / `updated` / `sku_id`. |
| V1.4 | 2026-05-21 | Sync with [[DESIGN/L1240C45 三支路冷却重评估 2026-05-21\|Rev 11 Three-Branch Cooling Reassessment]]: CDU uprated to ≥ 1500 kW / ≥ 175 m³/h / ≥ 220 kPa (VFD + 2N/N+1); TCS fluid locked at PG25; locked 9× DCD35 RDHX + 9× STULZ OHS-084-DG-FC; added §5 Cooling System and §4.1 cold-plate manifold; outdoor-side baseline ≥ 1700 kW. EN: server inlet temperature corrected to 26–28°C; Deployment SOP translated to English. |
| V1.3 | 2026-05-09 | Server inlet temperature revised from 24°C to 26–28°C (TCS range) |

---

*Document Version: V1.6 | Last Updated: 2026-08-30*
