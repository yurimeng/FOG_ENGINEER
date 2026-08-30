---
tags:
  - "#MDC"
  - "#type/design-spec"
  - "#product/i400c40"
  - "#unconfirmed"
doc_version: v1.6
updated: 2026-08-30
sku_id: I400C40ST50
---
# I400C40 — Tech Spec
**All-In-One Immersion Container (40ft)**

> **SKU identity:** short alias **I400C40** · full SKU ID `I400C40ST50` · product line **Immersion Cooling (I)** · status **shipped**. Naming baseline: [[NAMING_MAP]].
>
> **Audience:** Sales / pre-sales deliverable. Readers: customers, account managers, solution architects. Parameters are normative; if they conflict with engineering design, escalate to [[PUBLIC/Products/I400C40|I400C40 product PRD]] and [[PUBLIC/Products/I50TS|I50TS]]. Parameter baseline: **V1.0 (2026-07-28)**, sourced from AC40 V1.4 / A32 V1.4.
>
> **Source of truth:** product parameters follow [[PRODUCT_SPEC_BASELINE]] (six-SKU baseline table); **where this document disagrees with it, the baseline table governs**. Several figures here come from the legacy AC40 / A32 V1.4 baseline that the table does not yet cover; they are marked row by row per [[UNCONFIRMED_Convention]].
>
> **Three companion editions:** English internal (this file) · 中文内部版 [[I400C40_Tech_Spec_CN]] · external edition [[I400C40_Tech_Spec_External]]
>
> ✅ **Yuri's rulings of 2026-08-30 are propagated here ([[PRODUCT_SPEC_BASELINE]] v2.0):** §3 / §14 PUE and facility load become `1.0x` / computed per site at <https://mdcx.org> (the former ⛔ PUE conflict is closed); §12 lead time becomes 120 days EXW first batch, 90 days EXW for Scale, dummy-load burn-in 5–30 days, with no commitment on the commercial, freight or installation segments (the former ⛔ lead-time conflict is closed); §12 / §14 warranty becomes core components for one year from EXW plus an annual service fee, with response levels governed by the Invoice.
>
> ⏳ **This document still carries a document-level `#unconfirmed`:** envelope dimensions / weights, facility-water temperatures, container flow rates, design wet-bulb and rack space remain ⏳ unconfirmed. Who / what / when for each is given in the notes column of the relevant section table. **Do not release this edition as-is** — use the external edition for customers.
>
> **Internal engineering detail:** [[PUBLIC/Products/I400C40]] · [[PUBLIC/Products/I50TS]] · [[KB/IMMERSION/I400C40/I400C40 工作负荷]] · [[COOLING_SYSTEM_Guideline]]

Version: V1.6 | Date: 2026-08-30 | Parameter baseline: V1.0 (2026-07-28)

> **V1.0 first release (aligned to AC40/A32 V1.4):**
> 1. IT capacity locked: **recommended 360kW / max 400kW** (8×I50TS, formerly A32, at 45/50kW) + 1×10kW air-cooled rack
> 2. Cooling: single-phase immersion + in-tank Dual CDU (1+1); secondary **inlet ≤35°C / outlet ≈43°C / ΔT=8K**; facility water ≤32/37°C (ΔT=5K)
> 3. Heat rejection: site extreme dry-bulb **≤24°C → dry cooler only**; **>24°C → Hybrid Chiller**
> 4. UPS: **external (customer-supplied)** EATON 9395XR-600 + 2×93LiG2 (~10 min) — not inside I400C40
> 5. **No full-system UL listing** (select [[PUBLIC/Products/I400C45|I400C45]] when UL is mandatory)

---

## Document Navigation

| § | Section | Block File |
|---|---------|------------|
| 1 | Layout | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/01_Sec1_Layout\|01_Sec1_Layout]] |
| 2 | Product Positioning | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/02_Sec2_Positioning\|02_Sec2_Positioning]] |
| 3 | IT Capacity | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/03_Sec3_IT_Capacity\|03_Sec3_IT_Capacity]] |
| 4 | Immersion Tank / Rack Spec | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/04_Sec4_Rack_Spec\|04_Sec4_Rack_Spec]] |
| 5 | Cooling (Immersion + Hybrid Rejection) | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/05_Sec5_Cooling\|05_Sec5_Cooling]] |
| 6 | Power Distribution | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/06_Sec6_Power\|06_Sec6_Power]] |
| 7 | Structural Specifications | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/07_Sec7_Structural\|07_Sec7_Structural]] |
| 8 | Network & Cable Management | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/08_Sec8_Network\|08_Sec8_Network]] |
| 9 | Environmental & Compliance | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/09_Sec9_Environment\|09_Sec9_Environment]] |
| 10 | Monitoring & Management | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/10_Sec10_Monitoring\|10_Sec10_Monitoring]] |
| 11 | Fire Protection & Safety | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/11_Sec11_Fire\|11_Sec11_Fire]] |
| 12 | Service & Support | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/12_Sec12_Service\|12_Sec12_Service]] |
| 13 | Site & Installation | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/13_Sec13_Site\|13_Sec13_Site]] |
| 14 | I400C40 Key Specs Summary | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/14_Sec14_Summary\|14_Sec14_Summary]] |

---

## 1. Layout ^sec-1-layout
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/01_Sec1_Layout]]

## 2. Product Positioning ^sec-2-positioning
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/02_Sec2_Positioning]]

## 3. IT Capacity ^sec-3-it-capacity
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/03_Sec3_IT_Capacity]]

## 4. Immersion Tank / Rack Spec ^sec-4-rack-spec
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/04_Sec4_Rack_Spec]]

## 5. Cooling (Immersion + Hybrid Rejection) ^sec-5-cooling
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/05_Sec5_Cooling]]

## 6. Power Distribution ^sec-6-power
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/06_Sec6_Power]]

## 7. Structural Specifications ^sec-7-structural
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/07_Sec7_Structural]]

## 8. Network & Cable Management ^sec-8-network
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/08_Sec8_Network]]

## 9. Environmental & Compliance ^sec-9-environment
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/09_Sec9_Environment]]

## 10. Monitoring & Management ^sec-10-monitoring
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/10_Sec10_Monitoring]]

## 11. Fire Protection & Safety ^sec-11-fire
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/11_Sec11_Fire]]

## 12. Service & Support ^sec-12-service
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/12_Sec12_Service]]

## 13. Site & Installation ^sec-13-site
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/13_Sec13_Site]]

## 14. I400C40 Key Specs Summary ^sec-14-summary
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_EN/14_Sec14_Summary]]

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| V1.6 | 2026-08-30 | **Yuri's four rulings of 2026-08-30 propagated ([[PRODUCT_SPEC_BASELINE]] v2.0).** (1) **PUE is written `1.0x` everywhere** — the §3 and §14 figures "cool ~1.05–1.10 / hot ~1.15–1.20" and the ~400–480 kW facility load are void, replaced by "varies with PUE, computed per site at <https://mdcx.org> (TCO / Designer)"; the former ⛔ PUE conflict is closed; the §3 IT Load vs Total Facility Load distinction is retained as a hard rule. (2) **Lead time is unified to 120 days EXW for the first batch and 90 days EXW for Scale, counted from order placement**, with a new dummy-load burn-in period of 5–30 days (Supermicro recommendation, outside the EXW commitment); the commercial, freight and installation segments carry no commitment. The §12 "~185–230 days" figure, the four-phase deployment SOP table and the §14 deployment row are **deleted**, and the previous ⛔ conflict block is replaced by the adjudicated wording. (3) **Warranty is unified to core components for one year from EXW plus an annual service fee thereafter**; "9×5 NBD" and its ⏳ markers are **deleted** from §12 and §14 — response levels are governed by the Invoice. (4) The dual-loop GPU-side temperature ruling does not apply to the immersion line and nothing was changed for it. Block files 03 / 12 / 14 updated in step. |
| V1.5 | 2026-08-30 | Refreshed to the 2026-08-30 naming and data baseline. (1) Naming aligned to [[NAMING_MAP]]: AC40 → **I400C40**, A32 → **I50TS**, AC45 → **I400C45**, DC45 → **L1240C45** across the title, body and block-file frontmatter `title` fields; a one-off "formerly A32" note is kept at the tank's first mention; historical changelog wording and the "AC40 V1.4 / A32 V1.4" legacy-baseline citations are preserved per [[NAMING_MAP]] §4. (2) SKU identity line added at the top: full SKU ID `I400C40ST50` · Immersion Cooling line · status shipped. (3) CN / EN / External cross-links established. (4) Source-of-truth pointer added: parameters follow [[PRODUCT_SPEC_BASELINE]] and the baseline table governs on conflict. (5) A ⛔ conflict block was added above the §12 tables (EXW vs total on-site cycle; **figures retained**). (6) Confidence re-marked per [[UNCONFIRMED_Convention]], **values kept, markers only added**: facility water ≤32/37 °C (ΔT=5K) ⏳; envelope 12,192×2,438×2,896 mm, 12–16 T empty / 22–30 T operating, 256RU/232OU, container flow 87.8 / 97.6 m³/h and 28 °C design wet-bulb all ⏳ (legacy AC40 V1.4, not covered by the baseline table); **PUE marked ⛔ conflict** with the "historic extreme dry-bulb ≤ 24 °C" applicability boundary added on the same row as the figures; 1-year warranty / 9×5 NBD ⏳ (no source in baseline §3.3). (7) frontmatter gained `#unconfirmed` / `doc_version` / `updated` / `sku_id`. |
| V1.0 | 2026-07-28 | First release. AC40 pre-sales Tech Spec mirrored to DC45 14-section structure; parameters aligned to AC40/A32 V1.4. |

---

*Document version: V1.6 | Last updated: 2026-08-30*
