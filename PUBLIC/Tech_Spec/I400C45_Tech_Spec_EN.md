---
tags:
  - "#MDC"
  - "#type/design-spec"
  - "#product/i400c45"
  - "#unconfirmed"
doc_version: v1.1
updated: 2026-08-30
audience: Sales / pre-sales / account managers (internal deliverable — do not release in full)
sku_id: I400C45SUT50
---

# I400C45 — Tech Spec (English)
**All-In-One Immersion Container · 45ft single-phase immersion container with dedicated power bay**

> **Audience:** Sales / pre-sales / account managers. This document contains ⏳ **#unconfirmed** rows and **must not be released to customers in full**; for customer-facing material use [[I400C45_Tech_Spec_External]].
>
> **Companion versions:** Chinese [[I400C45_Tech_Spec_CN]] · Customer-facing [[I400C45_Tech_Spec_External]]
>
> **Data source:** every product figure in this document comes from [[PRODUCT_SPEC_BASELINE]] (six-SKU baseline table v1.0 / 2026-08-30). Confidence markers are defined in [[UNCONFIRMED_Convention]] §2.
>
> **The baseline table settles parameter disputes.** Where this document disagrees with [[PRODUCT_SPEC_BASELINE]], the baseline wins; where the baseline disagrees with the MDC site repo `docs/PRODUCT-MATRIX.md`, the site repo wins. This document does not define SKU codes.
>
> ✅ **Yuri's rulings of 2026-08-30 are propagated here ([[PRODUCT_SPEC_BASELINE]] v2.0):** (1) **PUE is written `1.0x` everywhere** — the ≈1.05 in §5.3 and the ~440–500 kW facility load in §3.1 are void, replaced by a per-site calculation with the TCO / Designer at <https://mdcx.org>; the IT Load vs Total Facility Load distinction is retained. (2) **Lead time**: **120 days EXW** first batch, **90 days EXW** for Scale (from order placement), dummy-load burn-in **5–30 days** (Supermicro recommendation, not covered by the EXW commitment), with **no commitment** on the commercial, freight or installation segments; the old ~185–230 days and the four-phase timeline are deleted. (3) **Warranty**: core components for **one year from EXW**, annual service fee thereafter; ONSITE / NBD / 9×5 / 24×7 response levels are **governed by the Invoice**. (4) The dual-loop GPU-side temperature ruling does not apply to the immersion line.
>
> **Related:** [[PUBLIC/Products/I400C45]] · [[PUBLIC/Products/I50TS]] · [[KB/IMMERSION/I400C45/index]] · [[I400C40_Tech_Spec_EN]]

---

## Document Navigation

> **This edition is a single file; block splitting will be done if and when it is needed.** All section anchors (`^sec-1-layout` … `^sec-14-summary`) are preserved, so block references of the form `[[I400C45_Tech_Spec_EN#^sec-5-cooling]]` still resolve.

| § | Section | Anchor | Confidence at a glance |
|---|---------|--------|------------------------|
| 1 | Layout | `^sec-1-layout` | Partly ⏳ |
| 2 | Product Positioning | `^sec-2-positioning` | ✅ |
| 3 | IT Capacity and Total Facility Load | `^sec-3-it-capacity` | ✅ |
| 4 | Immersion Tank (I50TS) Spec | `^sec-4-rack-spec` | Partly ⏳ |
| 5 | Cooling System | `^sec-5-cooling` | ✅ + 🔶 |
| 6 | Power Distribution | `^sec-6-power` | Partly ⏳ |
| 7 | Structural Specifications | `^sec-7-structural` | Whole section ⏳ |
| 8 | Network & Cable Management | `^sec-8-network` | Whole section ⏳ |
| 9 | Environmental & Compliance | `^sec-9-environment` | Partly ⏳ |
| 10 | Monitoring & Management | `^sec-10-monitoring` | ✅ + ⏳ |
| 11 | Fire Protection & Safety | `^sec-11-fire` | Whole section ⏳ |
| 12 | Service, Delivery and Commercial Position | `^sec-12-service` | ✅ adjudicated |
| 13 | Site & Installation Requirements | `^sec-13-site` | Partly ⏳ |
| 14 | Key Specifications Summary | `^sec-14-summary` | Summary |

---

## 1. Layout ^sec-1-layout

I400C45 is a **two-bay container**: the forward section of the 45ft box is the **compute bay**, the aft section is the **dedicated power bay**. Inside the compute bay, 8 I50TS immersion tanks sit in two rows against the side walls, four per side, with a service aisle down the middle; a single 10 kW air-cooled rack carries switching and any auxiliary gear that cannot be immersed. The power bay holds the 600 kW EATON UPS and two 93LiG2 battery cabinets — **that is the entire content of the five extra feet I400C45 has over I400C40**.

![[KB/IMMERSION/I400C45/I400C45 Layout_v1.svg]]
*I400C45 layout schematic (8× I50TS dual row + service aisle + dedicated power bay)*

| Item | Spec | Confidence / closure |
|------|------|----------------------|
| Bay division | Compute bay (8× I50TS + 1× 10 kW air rack) + dedicated power bay (UPS + batteries) | ✅ Site |
| Tank arrangement | Two rows against the walls, central service aisle | ✅ Site |
| Clear internal dimensions of compute / power bay | ⏳ **#unconfirmed** | Waiting on the site side or I400C45 DESIGN/ for a general arrangement drawing and clear-dimension table; expected TBD |
| Server lifting interface (rail / hoist spec) | ⏳ **#unconfirmed** | Waiting on the structural engineer for the I400C45 lifting interface drawing; expected TBD |

---

## 2. Product Positioning ^sec-2-positioning

**I400C45 is the complete inference package: the compute and the power land together.** It packages a 400 kW immersion compute core and 600 kW of UPS / battery ride-through into one 45ft box, so the delivery boundary is settled in a single step — the site provides a utility feed and an outdoor heat-rejection interface, and nothing inside the box requires the customer to separately procure, separately select, or separately permit electrical plant. For a site with no existing switchroom, or one unwilling to run a standalone UPS project for a single compute module, this is the shortest path to energization.

| Dimension | Positioning | Confidence |
|-----------|-------------|------------|
| Product line | Immersion Cooling (single-phase immersion) | ✅ Site |
| Full SKU ID | `I400C45SUT50` | ✅ Site |
| IT capacity | 400 kW | ✅ Site |
| Building blocks | 8× [[I50TS]] immersion tanks + 1× 10 kW air-cooled rack | ✅ Site |
| Per-tank density | 50 kW (T50) | ✅ Site |
| Power boundary | **Inside the box** — 45ft dedicated power bay carries UPS and batteries | ✅ Site |
| UL compliance | ✅ UL compliant | ✅ Site |
| Status | shipped | ✅ Site |
| Typical use | Dense AI inference; sites with no existing switchroom that need the power boundary delivered with the box; UL-mandatory markets | ✅ Site |

### 2.1 What separates I400C45 from I400C40 — two things only

> **Site wording:** *"They share the same 400 kW, eight-tank core."*

The difference between I400C45 and [[I400C40_Tech_Spec_EN|I400C40]] is **only the power boundary and those five feet (= the volume of the power bay)**. The eight-tank core, the oil loop, the in-tank CDU redundancy and the cooling rules are **identical**. Do not describe them as two generations or two cooling architectures.

| Item | I400C45 | I400C40 |
|------|---------|---------|
| Eight-tank immersion core | **Identical** | **Identical** |
| Oil loop and cooling rules | **Identical** | **Identical** |
| Container | 45ft (with dedicated power bay) | 40ft |
| UPS boundary | Inside (600 kW EATON + 2× 93LiG2, ~20 min) | Outside (customer-supplied 600 kW, ~10 min) |
| UL compliance | ✅ UL compliant | Baseline records "—" (not a deliverable of this SKU) |

**Selection rule:** the site has not yet built distribution and ride-through for this 400 kW, or the market mandates full-system UL → I400C45. The site already has an established electrical architecture and has paid for UPS and batteries elsewhere → [[I400C40_Tech_Spec_EN|I400C40]].

### 2.2 How the three immersion SKUs relate

| SKU | Full SKU ID | Container | IT | Tanks | Per-tank density | UPS boundary |
|-----|-------------|-----------|-----|-------|------------------|--------------|
| **I400C45** | `I400C45SUT50` | 45ft (with power bay) | 400 kW | 8× I50TS | 50 kW | Inside |
| I400C40 | `I400C40ST50` | 40ft | 400 kW | 8× I50TS | 50 kW | Outside |
| I200C20 | `I200C20ST50` | 20ft | 200 kW | 4× I50TS | 50 kW | Outside |

> The three are **the same density at different scale**. I200C20 is not a halved I400 — see [[I200C20_Tech_Spec_EN#^sec-2-positioning]].

---

## 3. IT Capacity and Total Facility Load ^sec-3-it-capacity

400 kW is **IT real power inside the tanks**, not the site service capacity. Any customer who says "400 kW" must be asked which one they mean — that is a hard rule of this knowledge base, not a stylistic preference.

| Item | Spec | Confidence |
|------|------|------------|
| IT capacity | **400 kW** | ✅ Site |
| Immersion tanks | 8× I50TS at 50 kW each (T50) | ✅ Site |
| Air-cooled rack | 1× 10 kW | ✅ Site |
| Maximum GPU count | **512 PCIe GPUs** | ✅ Site |
| GPU platforms | 4090 · 5090 · RTX PRO 6000 Blackwell SE · H100 · H200 (PCIe 4U 8-GPU) | ✅ Site |
| Rack space (RU / OU) | ⏳ **#unconfirmed** | Waiting on the site side or I50TS DESIGN/ to publish tank RU capacity; expected TBD |
| Power factor (UPS output) | ⏳ **#unconfirmed** | Waiting on the Power Engineer for the I400C45 electrical calculation sheet; expected TBD |

### 3.1 IT Load vs Total Facility Load ^sec-3-it-vs-facility

| Measure | Value | Meaning | Confidence |
|---------|-------|---------|------------|
| **IT Load** | **400 kW** | Real power drawn by servers / GPUs inside the eight tanks | ✅ Site |
| **Total Facility Load** | Varies with PUE — **computed per site with the TCO / Designer at <https://mdcx.org>** | IT + in-tank CDU pump power + outdoor rejection (dry cooler / Hybrid Chiller) + UPS losses + distribution losses + in-container auxiliaries | ✅ adjudicated |

> **Always quote both numbers.** Customers buy compute against IT Load and apply for substation capacity and model electricity cost against Total Facility Load. Because the I400C45 UPS sits inside the box, UPS losses and battery-cabinet heat **are counted inside this container's facility load** — the opposite of I400C40.
>
> ⚠️ **PUE is written `1.0x` everywhere (adjudicated by Yuri, 2026-08-30 · C-2 closed).** The former ~440–500 kW facility-load range and the ≈1.05 in §5 are **both void**. Total Facility Load varies with PUE and is **computed per site with the TCO / Designer at <https://mdcx.org>; no figure is given**.
>
> **The IT Load vs Total Facility Load distinction must still be kept** ([[CLAUDE.md]] Hard Rule 5) — always state that these are two different measures; only the facility-side number now comes from the calculator.

---

## 4. Immersion Tank (I50TS) Spec ^sec-4-rack-spec

The building block of I400C45 is eight [[I50TS]] single-phase immersion tanks. **I50TS is a tank component, not a SKU** (formerly A32; the legacy name survives only in `_archive/`, `Projects/` and supplier correspondence).

| Item | Spec | Confidence / closure |
|------|------|----------------------|
| Tank model | **I50TS** (formerly A32) | ⏳ **#unconfirmed** — the code was derived KB-side from the Tank naming regex; waiting on the site side to enter it in the `docs/PRODUCT-MATRIX.md` Alias registry, expected TBD |
| Quantity per container | **8** | ✅ Site |
| IT capacity per tank | **50 kW** (T50) | ✅ Site |
| Cooling method | Single-phase immersion | ✅ Site |
| In-tank CDU | **Dual CDU · 2N** | ✅ Site |
| Oil-side ΔT | **8 K** | ✅ Site |
| Oil flow per tank | **≈11–12 m³/h** | ✅ Site |
| Supported GPU platforms | 4090 · 5090 · RTX PRO 6000 Blackwell SE · H100 · H200 (PCIe 4U 8-GPU) | ✅ Site |
| Tank external dimensions / RU / OU | ⏳ **#unconfirmed** | Waiting on the site side or I50TS DESIGN/ for a tank specification sheet; expected TBD |
| Dielectric fluid grade and properties (cp / density) | ⏳ **#unconfirmed** | Waiting on the Cooling Engineer for the I400C45 fluid selection and measured-property report; expected TBD |
| In-tank PDU specification | ⏳ **#unconfirmed** | Waiting on the Power Engineer for the I50TS PDU specification table; expected TBD |
| Max server depth / rack standards | ⏳ **#unconfirmed** | Waiting on the site side or I50TS DESIGN/ to publish the server compatibility table; expected TBD |

> **Note:** no tank dimension, RU count or fluid property figure has been carried over from [[I400C40_Tech_Spec_EN]]. Those figures originate in legacy product documents (AC40/A32 V1.4) that [[PRODUCT_SPEC_BASELINE]] does not cover, and may not be quoted as I400C45 specifications until the baseline confirms them.

---

## 5. Cooling System ^sec-5-cooling

I400C45 uses **single-phase immersion**: whole servers sit in dielectric fluid, the in-tank CDU plate heat exchangers hand that heat to facility water, and the outdoor plant rejects it to atmosphere. There are no server fans, no hot and cold aisles, and no in-container heat balance that depends on airflow — this is the physical premise for the very low PUE the immersion architecture reaches at low dry-bulb sites (**the specific PUE is computed per site — see §5.3**).

### 5.1 Two loops

| Loop | Medium | Role | Confidence |
|------|--------|------|------------|
| Secondary (oil side) | Single-phase immersion dielectric fluid | Immerses the servers; rejects heat to facility water via the in-tank CDU plate HX | ✅ Site |
| Primary (facility water) | Facility water / glycol solution | Connects to the outdoor dry cooler or Hybrid Chiller | ✅ Site |
| Air branch | Air | 1× 10 kW air-cooled rack, **does not share a heat path with the immersion loops** | ✅ Site |

```
IT Load → Dielectric fluid (inside I50TS) → Dual CDU plate HX (2N) → Facility water 32 / 37 °C
                                                                            ↓
                              Dry coolers primarily; Hybrid Chiller added at peak-climate sites
```

### 5.2 Design conditions

| Item | Spec | Confidence |
|------|------|------------|
| Cooling method | Single-phase immersion | ✅ Site |
| In-tank CDU configuration | **Dual CDU per tank · fully redundant 2N** | ✅ Site |
| Oil-side ΔT | **8 K** | ✅ Site |
| Oil flow per tank | **≈11–12 m³/h** | ✅ Site |
| Container secondary flow (8 tanks) | **≈88–96 m³/h** | 🔶 **derived** — from 11–12 m³/h × 8; design value, subject to final selection |
| **Facility water temperatures** | **32 / 37 °C warm water** | ✅ Site — **of the three immersion SKUs only I400C45 has site evidence for this**; it must not be applied laterally to I400C40 / I200C20 |
| Outdoor heat source | Dry coolers primarily; Hybrid Chiller added at peak-climate sites | ✅ Site |
| Facility-side ΔT / flow | ⏳ **#unconfirmed** | Waiting on the Cooling Engineer for the I400C45 primary-loop hydraulic calculation; expected TBD |
| Outdoor heat-rejection baseline (kW) | ⏳ **#unconfirmed** | Waiting on the Cooling Engineer for the I400C45 rejection calculation; expected TBD |
| Design ambient wet-bulb | ⏳ **#unconfirmed** | Waiting on the site side or I400C45 DESIGN/ to publish the design wet-bulb; expected TBD |

### 5.3 PUE and the boundary it is valid within ^sec-5-pue

| Item | Spec | Confidence |
|------|------|------------|
| PUE | **`1.0x`** — **no fixed value, no range, no "typical value". Computed per site with the TCO / Designer at <https://mdcx.org>** | ✅ adjudicated |

> **PUE is written `1.0x` everywhere (adjudicated by Yuri, 2026-08-30 · C-2 closed).** There is no single PUE figure for the immersion line; the final value is set by site conditions and **must be computed per site**. The former "≈1.05 / ≤24 °C dry-bulb boundary" wording is void and **is no longer quoted**.
>
> Qualitatively: climates where dry coolers reject heat year-round sit at the low end; hotter sites need a hybrid chiller and PUE moves up accordingly. **No specific number is given.** Give customers the <https://mdcx.org> link, not a figure. See [[PRODUCT_SPEC_BASELINE#^baseline-pue]].

### 5.4 Redundancy and failure modes

| Failure | Impact | Risk |
|---------|--------|------|
| Single CDU failure | None (2N — the other CDU carries the whole tank) | Low |
| Both CDUs fail | That tank shuts down; the other seven are unaffected | High |
| Outdoor plant failure | Facility water temperature rises; derate or shut down | Medium |
| Fouled plate HX / filter | Reduced heat transfer, rising oil temperature | Medium |

> **In-tank cooling is 2N; in-container IT is not.** A single container carries no IT redundancy — see the redundancy model in §6.3.

### 5.5 Heat-rejection configuration rule

Each I400C45 is paired **one-to-one** with its Cooling Zone outdoor plant; plant is not shared across containers. System-level availability is achieved by **adding containers**, not by sharing a heat sink.

---

## 6. Power Distribution ^sec-6-power

The I400C45 power boundary is **inside the box**. The 600 kW EATON UPS and two 93LiG2 battery cabinets are installed in the dedicated power bay; the customer only brings utility power (and optionally a generator / BESS) to the container's incoming panel.

### 6.1 Power path

```
Grid (optional ATS ← Generator / BESS)
        ↓
I400C45 dedicated power bay: EATON UPS 600 kW + 2× 93LiG2 batteries (~20 min)
        ↓
In-container PDC → 8× I50TS in-tank PDUs (A/B feeds) + 10 kW air rack + auxiliaries
```

| Item | Spec | Confidence / closure |
|------|------|----------------------|
| UPS boundary | **Inside the box** (45ft dedicated power bay) | ✅ Site |
| UPS capacity / brand | **600 kW · EATON** | ✅ Site |
| Battery ride-through | **~20 min** (internal, 2× 93LiG2) | ✅ Site / KB |
| UL compliance | ✅ **UL compliant** | ✅ Site |
| Specific UPS model | ⏳ **#unconfirmed** | Waiting on the site side or the Power Engineer to confirm the I400C45 UPS model; expected TBD |
| Supply system (incoming voltage) | ⏳ **#unconfirmed** | Waiting on the site side to publish supply voltages on the immersion product pages (the 380 / 400 / 415 / 480 V AC row in baseline §1.3 covers the liquid line only); expected TBD |
| Busway / PDC specification | ⏳ **#unconfirmed** | Waiting on the Power Engineer for the I400C45 single-line diagram and calculation sheet; expected TBD |
| In-container electrical load schedule | ⏳ **#unconfirmed** | Waiting on the Power Engineer for the I400C45 load schedule; expected TBD |

> ⚠️ **UPS ≠ BESS.** 93LiG2 provides minutes-scale ride-through; BESS is hours-scale storage, belongs to the Power Zone and is not inside this container. The two terms are not interchangeable ([[CLAUDE.md]] Hard Rule 7).

### 6.2 800 V HVDC

Baseline §1.3 records 800 V HVDC as Roadmap Q3 2026 — **not shipping today**. That row covers the liquid line; whether the immersion line follows the same position is ⏳ **#unconfirmed** — waiting on the site side to publish it on the immersion product pages, expected TBD. **HVDC availability must not be promised to customers.**

### 6.3 Redundancy model ^sec-6-redundancy

> **The container is the smallest unit of redundancy.** This is the immersion line's redundancy position, from [[PRODUCT_SPEC_BASELINE#^baseline-immersion-cooling]] §3.3.

| Layer | Redundancy | Confidence |
|-------|------------|------------|
| In-tank cooling (dual CDU per I50TS) | **2N** | ✅ Site |
| Single-container IT | **No IT redundancy** — a container is one whole; there is no in-box N+1 | ✅ Site |
| System level | **N / N+1 / 2N achieved by adding containers** | ✅ Site |
| Design objective | Tier II investment reaching Tier III-class availability through differentiated redundancy | ✅ Site |
| Redundancy principle | 2N where failure is expensive, N+1 everywhere else — **never global 2N** | ✅ Site |

**How to answer the customer:** when a customer asks "is it 2N", the answer is not yes or no but "at which layer". In-tank cooling is 2N. At the IT layer the unit of redundancy is the container — N+1 means buying N+1 containers, 2N means buying 2N containers. What the customer buys with redundancy money is then usable compute, not idle equipment inside a box.

---

## 7. Structural Specifications #unconfirmed ^sec-7-structural

| Item | Spec | Confidence / closure |
|------|------|----------------------|
| Container | **45ft (with dedicated power bay)** | ✅ Site |
| External dimensions (L × W × H) | ⏳ **#unconfirmed** | Waiting on the site side or I400C45 DESIGN/ for an outline drawing (the 45ft ISO nominal figures are unconfirmed and **must not be inferred from an ISO table and quoted to a customer**); expected TBD |
| Empty weight | ⏳ **#unconfirmed** | Waiting on the structural engineer for a weighing report / structural calculation; expected TBD |
| Operating weight (fluid + IT) | ⏳ **#unconfirmed** | Waiting on the structural engineer for the structural calculation; expected TBD |
| Enclosure IP rating | ⏳ **#unconfirmed** | Waiting on the site side to publish, or on project-specific confirmation; expected TBD |
| Foundation loading and levelness | ⏳ **#unconfirmed** | Waiting on the structural engineer for foundation design criteria; expected TBD |

> ⚠️ **This entire section is unconfirmed.** When a customer asks about dimensions or weight, follow [[UNCONFIRMED_Convention]] §5: answer "that parameter follows final selection and will be provided during technical clarification" and **give no number**. In particular, do not take the 40ft dimensions and weights from [[I400C40_Tech_Spec_EN#^sec-7-structural]], adjust the length, and present the result as I400C45.

---

## 8. Network & Cable Management #unconfirmed ^sec-8-network

| Item | Spec | Confidence / closure |
|------|------|----------------------|
| Default fabric / speeds / protocols | ⏳ **#unconfirmed** | Waiting on the site side or I400C45 DESIGN/ for a network configuration document; expected TBD |
| Cable entries and cable management | ⏳ **#unconfirmed** | Waiting on the site side or I400C45 DESIGN/ for penetration and tray drawings; expected TBD |
| Out-of-band management | ⏳ **#unconfirmed** | Waiting on the site side or I400C45 DESIGN/ to publish the OOB design; expected TBD |

> [[PRODUCT_SPEC_BASELINE]] does not cover network fields for the immersion line. Where a project genuinely has network requirements, run a project-level design through [[NETWORK_Guideline]] — **do not quote another SKU's network configuration as an I400C45 specification**.

---

## 9. Environmental & Compliance ^sec-9-environment

| Item | Spec | Confidence / closure |
|------|------|----------------------|
| Heat-rejection climate gate | Historical extreme dry-bulb **≤ 24 °C** → dry coolers primarily; **> 24 °C** → add a Hybrid Chiller | ✅ Site |
| UL compliance | ✅ **UL compliant** | ✅ Site |
| Warranty backing | Immersion line backed by the OEM; **Intel DataCenter Certified** | ✅ Site |
| Availability target | Tier II investment → Tier III-class availability (differentiated redundancy) | ✅ Site |
| Operating ambient temperature range | ⏳ **#unconfirmed** | Waiting on the site side or I400C45 DESIGN/ to publish the operating envelope; expected TBD |
| Operating humidity | ⏳ **#unconfirmed** | Waiting on the site side or I400C45 DESIGN/ to publish; expected TBD |
| Operating altitude / derating curve | ⏳ **#unconfirmed** | Waiting on the Power Engineer and Cooling Engineer for altitude derating; expected TBD |
| CE / local certification path | ⏳ **#unconfirmed** | Waiting on the Compliance Officer to confirm the market-access path for the target market; expected TBD |
| Dielectric fluid environmental / hazmat compliance | ⏳ **#unconfirmed** | Waiting on the Compliance Officer to confirm the fluid MSDS and local hazmat filing requirements; expected TBD |

> **No competitor comparison.** Customer-facing material must not quote non-MDCX product parameters for comparative advantage ([[CLAUDE.md]] Hard Rule 3).

---

## 10. Monitoring & Management ^sec-10-monitoring

| Item | Spec | Confidence / closure |
|------|------|----------------------|
| **CIOS** | Included with every MDCX. Path-addressed telemetry, alarm-to-ticket, O&M workflows, usage metering; open-source core Apache-2.0 (Roadmap) | ✅ Site |
| Digital twin | **NVIDIA Omniverse** — live state projected onto a 3D model | ✅ Site |
| DCM (compute marketplace) | **Roadmap · MVP in development** — **must not be committed to customers as a delivered capability** | ✅ Site |
| Protocol / interface list | ⏳ **#unconfirmed** | Waiting on the site side or the CIOS team for the I400C45 interface list (Modbus / SNMP / Redfish coverage); expected TBD |
| Monitoring point schedule | ⏳ **#unconfirmed** | Waiting on the Cooling Engineer and Power Engineer for the I400C45 point list; expected TBD |
| Fluid-level alarm tiers | ⏳ **#unconfirmed** | Waiting on I50TS DESIGN/ for the level-alarm setpoint table; expected TBD |

---

## 11. Fire Protection & Safety #unconfirmed ^sec-11-fire

| Item | Spec | Confidence / closure |
|------|------|----------------------|
| Clean agent type and concentration | ⏳ **#unconfirmed** | Waiting on the site side or I400C45 DESIGN/ for the fire protection design; expected TBD |
| Detection system | ⏳ **#unconfirmed** | Waiting on the same; expected TBD |
| Fire zoning principle | ⏳ **#unconfirmed** | Waiting on the same; expected TBD |
| Leak / spill containment design | ⏳ **#unconfirmed** | Waiting on I50TS DESIGN/ for containment and spill-response design; expected TBD |
| EPO / grounding / insulation monitoring | ⏳ **#unconfirmed** | Waiting on the Power Engineer for the electrical safety design; expected TBD |

> [[PRODUCT_SPEC_BASELINE]] does not cover fire protection fields for the immersion line. Final agent type, concentration and interlock logic must comply with the **fire code of the deployment jurisdiction** and pass the local fire authority review; this is project-level design and is not frozen in a product-level Tech Spec.

---

## 12. Service, Delivery and Commercial Position ^sec-12-service

### 12.1 Price — the standard answer

> **配置方案由 MDCX 工程团队提供，价格由商务团队核算，请联系客户经理获取正式报价。**
> *(The configuration is provided by the MDCX engineering team; pricing is calculated by the commercial team — please contact your account manager for a formal quotation.)*

This document and every version of it **contain no price figures** ([[CLAUDE.md]] Hard Rule 1). Payment terms, discounts and quotation validity are read from the commercial templates and are never inlined in the KB.

### 12.2 Lead time — ✅ adjudicated by Yuri, 2026-08-30 (C-8 closed)

**EXW is the only commitment; nothing else is committed.**

| Item | Value | Nature of commitment | Confidence |
|------|-------|------|------|
| **First-batch lead time** | **120 days EXW from order placement** | ✅ **Committed** | ✅ adjudicated |
| **Scale (expansion batch) lead time** | **90 days EXW** | ✅ **Committed** | ✅ adjudicated |
| **Dummy-load burn-in period** | **5–30 days** — prove out the power and cooling chain on a dummy load before real GPUs go in. Source: **Supermicro recommendation** | ⚠️ **Not covered by the EXW commitment** | ✅ adjudicated |
| Commercial cycle (contract / payment / procurement) | **Not committed** | ❌ no commitment | ✅ adjudicated |
| Freight and customs | **Not committed**; buyer's responsibility | ❌ no commitment | ✅ adjudicated |
| On-site installation and commissioning | **Not committed** | ❌ no commitment | ✅ adjudicated |

> **Lead-time wording rules** ([[PRODUCT_SPEC_BASELINE]] §3.1):
> 1. The only committable figure is the EXW day count — **120 days** for the first batch, **90 days** for Scale, both counted from **order placement**.
> 2. **The commercial, freight and installation segments carry no commitment** — no day counts, no ranges, no estimates. Escalate customer follow-ups to the commercial team per [[CLAUDE.md]] §5.
> 3. **The dummy-load burn-in period of 5–30 days is listed separately** and is explicitly outside the EXW commitment — prove out the power and cooling chain on a dummy load rather than commissioning on the customer's compute assets.
> 4. **All previous bases are void and have been deleted**: "~185–230 days including logistics", "90 days EXW up to 120", the survey → manufacturing → ocean freight → installation four-phase timeline and "3–4 weeks on-site commissioning" no longer appear in this document.

### 12.3 Delivery process and service

| Item | Spec | Confidence / closure |
|------|------|----------------------|
| Prefabrication rate | **99% completed before leaving the factory** | ✅ Site |
| Freight and customs | Buyer's responsibility; MDCX does not estimate and commits to no duration | ✅ adjudicated |
| On-site installation and commissioning | **Not committed** (neither duration nor scope) | ✅ adjudicated |
| Warranty backing | Immersion line backed by the OEM; Intel DataCenter Certified | ✅ Site |
| **Warranty scope and term** | **Core components, one year from EXW** | ✅ adjudicated |
| **Subsequent years** | **Annual service fee** | ✅ adjudicated |
| **Support SLA (ONSITE / NBD / 9×5 / 24×7 etc.)** | **Governed by the Invoice** — the KB and Tech Specs neither commit to nor define it; refer customer questions to the commercial team | ✅ adjudicated |

### 12.4 Expansion logic

| Direction | Notes |
|-----------|-------|
| Scale-out | Add I400C45 units; system-level N / N+1 / 2N is set by container count (§6.3) |
| Mixed deployment | Cluster with I400C40 / I200C20 — the eight-tank core is identical, so O&M practice is common |
| Densification | A tank is already at the T50 ceiling; raising density requires re-validating cooling and power and is outside the standard product |

---

## 13. Site & Installation Requirements ^sec-13-site

| Item | Requirement | Confidence / closure |
|------|-------------|----------------------|
| Outdoor plant | One-to-one per container: dry coolers primarily, Hybrid Chiller at peak-climate sites. Plant is not shared across containers | ✅ Site |
| Climate gate | Historical extreme dry-bulb ≤ 24 °C permits the free-cooling route; above 24 °C the Hybrid Chiller's DX energy must be calculated and added to facility load | ✅ Site |
| Power connection | Utility feed terminates at the container; UPS and batteries are inside, so **the customer needs no separate UPS room** | ✅ Site |
| Floor loading | ⏳ **#unconfirmed** | Waiting on the structural engineer for operating weight and foundation criteria (see §7); expected TBD |
| Floor levelness | ⏳ **#unconfirmed** | Waiting on the structural engineer for installation tolerances; expected TBD |
| Clearances / service aisles | ⏳ **#unconfirmed** | Waiting on the Layout Planner for I400C45 site clearance requirements; expected TBD |
| Road and lifting envelope | ⏳ **#unconfirmed** | Waiting on the structural engineer to confirm the 45ft transport envelope and lifting points; expected TBD |
| Fluid fill and hazmat | ⏳ **#unconfirmed** | Waiting on the Compliance Officer to confirm dielectric transport / storage / fill-and-drain requirements; expected TBD |
| Local permits | Planning, utility, fire, environmental — **project-specific confirmation** | Project-dependent |

### 13.1 Zone boundaries

| Zone | Relation to I400C45 |
|------|---------------------|
| IT Zone | **I400C45 itself** (8× I50TS + 10 kW air rack) |
| Power Zone | **UPS and batteries are inside the box**; utility, generator, BESS and switchyard sit on the customer / Power Zone side |
| Cooling Zone | Outdoor dry cooler / Hybrid Chiller one-to-one, **not fully integrated inside the container** |

---

## 14. Key Specifications Summary ^sec-14-summary

| Item | Spec | Confidence |
|------|------|------------|
| Full SKU ID | `I400C45SUT50` | ✅ |
| Container | 45ft (with dedicated power bay) | ✅ |
| IT Load | **400 kW** | ✅ |
| Total Facility Load | Varies with PUE — **computed per site at <https://mdcx.org>** | ✅ adjudicated |
| Immersion tanks | 8× I50TS at 50 kW each (T50) | ✅ |
| Air-cooled rack | 1× 10 kW | ✅ |
| Maximum GPU count | 512 PCIe GPUs | ✅ |
| GPU platforms | 4090 · 5090 · RTX PRO 6000 Blackwell SE · H100 · H200 | ✅ |
| Cooling method | Single-phase immersion; dual CDU per tank, **2N** | ✅ |
| Oil-side ΔT | 8 K | ✅ |
| Oil flow per tank | ≈11–12 m³/h | ✅ |
| Container secondary flow | ≈88–96 m³/h (design value) | 🔶 derived |
| Facility water | **32 / 37 °C warm water** | ✅ |
| PUE | **`1.0x`** — computed per site with the TCO / Designer at <https://mdcx.org>; no fixed value and no range | ✅ adjudicated |
| Outdoor heat source | Dry coolers primarily; Hybrid Chiller at peak-climate sites | ✅ |
| UPS boundary | **Inside the box** (dedicated power bay) | ✅ |
| UPS capacity | 600 kW · EATON | ✅ |
| Battery ride-through | ~20 min (2× 93LiG2) | ✅ |
| UL compliance | ✅ UL compliant | ✅ |
| Redundancy model | 2N in-tank; no IT redundancy in a single box; system level by adding boxes | ✅ |
| Software | CIOS (standard) + NVIDIA Omniverse digital twin | ✅ |
| Prefabrication rate | 99% completed before leaving the factory | ✅ |
| External dimensions / weight | ⏳ **#unconfirmed** | ⏳ |
| Lead time | **120 days EXW first batch / 90 days EXW for Scale** (from order placement); dummy-load burn-in 5–30 days (not covered by the EXW commitment); commercial, freight and installation carry **no commitment** | ✅ adjudicated |
| Warranty | **Core components, one year from EXW**; annual service fee thereafter; ONSITE / NBD / 9×5 / 24×7 response levels are **governed by the Invoice** | ✅ adjudicated |
| Price | **No figure appears anywhere** — see §12.1 | — |

### 14.1 Open items (to be closed)

| # | Open item | Waiting on | Waiting for | Expected |
|---|-----------|-----------|-------------|----------|
| 1 | I50TS code entered in the Alias registry | Site side | `docs/PRODUCT-MATRIX.md` update | TBD |
| 2 | 45ft external dimensions, empty / operating weight | Structural engineer | Outline drawing + structural calculation | TBD |
| 3 | Dielectric fluid grade and measured properties | Cooling Engineer | Selection report + measured density / cp | TBD |
| 4 | Facility-side ΔT, flow and outdoor rejection baseline | Cooling Engineer | Primary hydraulic and rejection calculations | TBD |
| 5 | Supply system, busway and in-container load schedule | Power Engineer | Single-line diagram + load schedule | TBD |
| 6 | Network configuration and OOB design | Site side / DESIGN | Network configuration document | TBD |
| 7 | Fire design (agent / detection / zoning / containment) | Site side / DESIGN | Fire protection design statement | TBD |
| 8 | Operating temperature, humidity, altitude derating | Cooling + Power Engineer | Environmental envelope and derating curves | TBD |
| 9 | Annual maintenance contract (AMC) detail | Commercial team | Invoice / contractual standard service terms (warranty term and SLA were closed by the 2026-08-30 ruling) | TBD |
| 10 | Whether the dummy-load burn-in happens at the factory or on site | ATS | Confirmation of where the 5–30 days is executed (does not affect the EXW commitment) | TBD |

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| v1.1 | 2026-08-30 | **Yuri's four rulings of 2026-08-30 propagated ([[PRODUCT_SPEC_BASELINE]] v2.0).** (1) **PUE is written `1.0x` everywhere**: the "≈1.05 + ≤24 °C dry-bulb boundary" in §5.3 and the ~440–500 kW Total Facility Load in §3.1 are **void**, replaced by "varies with PUE, computed per site with the TCO / Designer at <https://mdcx.org>" (§3.1 / §5 / §5.3 / §14); the §3 IT Load vs Total Facility Load distinction is retained as a hard rule. (2) **Lead time is unified to 120 days EXW for the first batch and 90 days EXW for Scale, counted from order placement**, with a new dummy-load burn-in period of 5–30 days (Supermicro recommendation, outside the EXW commitment); the commercial, freight and installation segments carry no commitment. The §12.2 ⛔ two-position table and "~185–230 days", the §12.3 four-phase rows and "3–4 weeks on-site installation and commissioning", and the §14 ⛔ lead-time row are **deleted**. (3) **Warranty is unified to core components for one year from EXW plus an annual service fee thereafter**, with ONSITE / NBD / 9×5 / 24×7 response levels governed by the Invoice; the three ⏳ warranty / support rows in §12.3 are rewritten to the adjudicated wording. (4) Open items 9 / 10 in §14.1 are rewritten accordingly (warranty and lead time are closed; replaced by AMC terms and where the dummy-load burn-in is executed). The dual-loop GPU-side temperature ruling does not apply to the immersion line. |
| v1.0 | 2026-08-30 | First release. I400C45 English pre-sales Tech Spec built on the 14-section I400C40 structure; every product figure taken from [[PRODUCT_SPEC_BASELINE]] v1.0 and marked row by row against the four confidence levels of [[UNCONFIRMED_Convention]]; §3 separates IT Load from Total Facility Load explicitly; §5 binds PUE 1.05 to the ≤24 °C dry-bulb boundary; §6.3 records the immersion redundancy model; §12 records the ⛔ lead-time conflict and the standard price answer. Section-for-section and row-for-row parallel to [[I400C45_Tech_Spec_CN]]. This edition is a single file; block splitting will be done if and when it is needed. |
