---
tags:
  - "#MDC"
  - "#type/design-spec"
  - "#product/i200c20"
  - "#unconfirmed"
doc_version: v1.1
updated: 2026-08-30
audience: Sales / pre-sales / account managers (internal deliverable — do not release in full)
sku_id: I200C20ST50
---

# I200C20 — Tech Spec (English)
**20ft single-phase immersion compute bay**

> **Audience:** Sales / pre-sales / account managers. This document contains ⏳ **#unconfirmed** rows and **must not be released to customers in full**; for customer-facing material use [[I200C20_Tech_Spec_External]].
>
> **Companion versions:** Chinese [[I200C20_Tech_Spec_CN]] · Customer-facing [[I200C20_Tech_Spec_External]]
>
> **Data source:** every product figure in this document comes from [[PRODUCT_SPEC_BASELINE]] (six-SKU baseline table v1.0 / 2026-08-30). Confidence markers are defined in [[UNCONFIRMED_Convention]] §2.
>
> **The baseline table settles parameter disputes.** Where this document disagrees with [[PRODUCT_SPEC_BASELINE]], the baseline wins; where the baseline disagrees with the MDC site repo `docs/PRODUCT-MATRIX.md`, the site repo wins. This document does not define SKU codes.
>
> ✅ **Yuri's rulings of 2026-08-30 are propagated here ([[PRODUCT_SPEC_BASELINE]] v2.0):** (1) **PUE is written `1.0x` everywhere** — the ≈1.05 in §5.3 is void and the §3.1 Total Facility Load moves from ⏳ to "varies with PUE, computed per site with the TCO / Designer at <https://mdcx.org>"; the IT Load vs Total Facility Load distinction is retained. (2) **Lead time**: **120 days EXW** first batch, **90 days EXW** for Scale (from order placement), dummy-load burn-in **5–30 days** (Supermicro recommendation, not covered by the EXW commitment), with **no commitment** on the commercial, freight or installation segments; the old ~185–230 days and the four-phase timeline are deleted. (3) **Warranty**: core components for **one year from EXW**, annual service fee thereafter; ONSITE / NBD / 9×5 / 24×7 response levels are **governed by the Invoice**. (4) The dual-loop GPU-side temperature ruling does not apply to the immersion line.
>
> **Related:** [[PUBLIC/Products/I50TS]] · [[KB/IMMERSION/I200C20/index]] · [[I400C45_Tech_Spec_EN]] · [[I400C40_Tech_Spec_EN]]

---

## Document Navigation

> **This edition is a single file; block splitting will be done if and when it is needed.** All section anchors (`^sec-1-layout` … `^sec-14-summary`) are preserved, so block references of the form `[[I200C20_Tech_Spec_EN#^sec-5-cooling]]` still resolve.

| § | Section | Anchor | Confidence at a glance |
|---|---------|--------|------------------------|
| 1 | Layout | `^sec-1-layout` | Whole section ⏳ |
| 2 | Product Positioning | `^sec-2-positioning` | ✅ |
| 3 | IT Capacity and Total Facility Load | `^sec-3-it-capacity` | ✅ + ⏳ |
| 4 | Immersion Tank (I50TS) Spec | `^sec-4-rack-spec` | Partly ⏳ |
| 5 | Cooling System | `^sec-5-cooling` | ✅ + 🔶 + ⏳ |
| 6 | Power Distribution | `^sec-6-power` | Mostly ⏳ |
| 7 | Structural Specifications | `^sec-7-structural` | Whole section ⏳ |
| 8 | Network & Cable Management | `^sec-8-network` | Whole section ⏳ |
| 9 | Environmental & Compliance | `^sec-9-environment` | Partly ⏳ |
| 10 | Monitoring & Management | `^sec-10-monitoring` | ✅ + ⏳ |
| 11 | Fire Protection & Safety | `^sec-11-fire` | Whole section ⏳ |
| 12 | Service, Delivery and Commercial Position | `^sec-12-service` | ✅ adjudicated |
| 13 | Site & Installation Requirements | `^sec-13-site` | Partly ⏳ |
| 14 | Key Specifications Summary | `^sec-14-summary` | Summary |

---

## 1. Layout #unconfirmed ^sec-1-layout

I200C20 is a **20ft compute bay**: four I50TS immersion tanks plus a service aisle. The electrical plant sits outside the box, so essentially the whole internal volume of the 20 feet is given over to tanks and service space — that is the premise for reaching 200 kW inside a 20ft form factor.

| Item | Spec | Confidence / closure |
|------|------|----------------------|
| Bay division | A single compute bay (4× I50TS); electrical plant outside the box | ✅ Site |
| Tank arrangement | ⏳ **#unconfirmed** | Waiting on the Layout Planner or I200C20 DESIGN/ for a general arrangement drawing (whether four tanks sit in one row or two inside 20ft is unconfirmed); expected TBD |
| Clear internal dimensions and aisle width | ⏳ **#unconfirmed** | Waiting on the Layout Planner for a clear-dimension table; expected TBD |
| Server lifting interface | ⏳ **#unconfirmed** | Waiting on the structural engineer for the I200C20 lifting interface drawing; expected TBD |
| Layout drawing / SVG | ⏳ **#unconfirmed** | Waiting on the Layout Planner to issue drawings (the vault holds no I200C20 layout asset today); expected TBD |

> ⚠️ **The "4+4 dual rows against the walls" arrangement in [[I400C40_Tech_Spec_EN#^sec-1-layout]] must not be quoted as the I200C20 layout** — that is the arrangement of a 40ft eight-tank box; the arrangement of a 20ft four-tank box has not been confirmed.

---

## 2. Product Positioning ^sec-2-positioning

**I200C20 is inference density for when 45 feet will not fit.**

The site conditions it addresses are specific: a clear patch inside an existing urban plant building, a rooftop, an underground car park, a legacy machine room being converted, a campus whose turning radii cannot take a 40 or 45ft box — **the site itself dictates 20 feet, and the compute requirement has not shrunk to match**. The I200C20 answer is not to lower density to suit the form factor, but to hold exactly the same **T50 per-tank density** as the I400 line inside 20 feet: four I50TS tanks, 50 kW each, 200 kW of IT.

**It is not a halved I400.** "Halved" implies one product scaled down proportionally, which produces the wrong expectation — half the price, half the configuration, half the performance. What is actually true is: **the same density, half the tank count, built for a different site constraint**. Customers choose I200C20 not usually because of budget but because **the site will not take a bigger box**; the two must not be conflated in a solution discussion.

| Dimension | Positioning | Confidence |
|-----------|-------------|------------|
| Product line | Immersion Cooling (single-phase immersion) | ✅ Site |
| Full SKU ID | `I200C20ST50` | ✅ Site |
| IT capacity | 200 kW | ✅ Site |
| Building blocks | 4× [[I50TS]] immersion tanks | ✅ Site |
| Per-tank density | **50 kW (T50) — identical to I400C45 / I400C40** | ✅ Site |
| Power boundary | **Outside the box** (customer / Power Zone side) | ✅ Site |
| Container | 20ft compute bay | ✅ Site |
| Status | shipped | ✅ Site |
| Typical use | Sites a 40/45ft box cannot reach: clear space inside existing plant buildings, rooftops, underground spaces, legacy machine-room conversions, access-restricted campuses | ✅ Site |

### 2.1 Wording rules (customer communication)

| ❌ Do not say | ✅ Say instead |
|---------------|----------------|
| A shrunken I400 / half-configuration / halved version | A 20ft compute bay at the same T50 density with half the tank count |
| Entry-level / stripped-down model | Built for sites a 40/45ft box cannot reach |
| Half the performance of an I400 | Same per-tank density as I400, with four tanks instead of eight |
| Estimate it at half the price | Pricing is calculated by the commercial team (see §12.1) |

### 2.2 How the three immersion SKUs relate

| SKU | Full SKU ID | Container | IT | Tanks | Per-tank density | UPS boundary |
|-----|-------------|-----------|-----|-------|------------------|--------------|
| I400C45 | `I400C45SUT50` | 45ft (with power bay) | 400 kW | 8× I50TS | 50 kW | Inside |
| I400C40 | `I400C40ST50` | 40ft | 400 kW | 8× I50TS | 50 kW | Outside |
| **I200C20** | `I200C20ST50` | **20ft** | **200 kW** | **4× I50TS** | **50 kW** | **Outside** |

> The three are **the same density at different scale**. The first selection question is not "how many kW" but "how long a box the site can take, and which side the power boundary sits on".

> ⚠️ **Note: I400C45 and I400C40 each include one 10 kW air-cooled rack; the I200C20 column of [[PRODUCT_SPEC_BASELINE]] lists no air-cooled rack.** This document therefore does not claim one. Whether I200C20 carries an air-cooled rack is ⏳ **#unconfirmed** — waiting on the site side or I200C20 DESIGN/ to state it, expected TBD.

---

## 3. IT Capacity and Total Facility Load ^sec-3-it-capacity

200 kW is **IT real power inside the tanks**, not the site service capacity. The I200C20 UPS sits outside the box, so UPS losses and battery heat **are not inside this container** but must still be counted in site capacity — a point especially easy to miss on 20ft projects, because customers tend to read "one 20-foot box" as "a small thing that needs no separate electrical planning".

| Item | Spec | Confidence |
|------|------|------------|
| IT capacity | **200 kW** | ✅ Site |
| Immersion tanks | 4× I50TS at 50 kW each (T50) | ✅ Site |
| GPU platforms | 4090 · 5090 · RTX PRO 6000 · H100 · H200 (PCIe) | ✅ Site |
| Maximum GPU count | ⏳ **#unconfirmed** — the site discloses 512 for the I400 line only; halving to 256 would be 🔶 derived, and **the baseline does not confirm this field** | Waiting on the site side to publish a GPU ceiling on the I200C20 product page; expected TBD |
| Rack space (RU / OU) | ⏳ **#unconfirmed** | Waiting on the site side or I50TS DESIGN/ to publish tank RU capacity; expected TBD |
| Power factor (UPS output) | ⏳ **#unconfirmed** | Waiting on the Power Engineer for the I200C20 electrical calculation sheet; expected TBD |

### 3.1 IT Load vs Total Facility Load ^sec-3-it-vs-facility

| Measure | Value | Meaning | Confidence |
|---------|-------|---------|------------|
| **IT Load** | **200 kW** | Real power drawn by servers / GPUs inside the four tanks | ✅ Site |
| **Total Facility Load** | Varies with PUE — **computed per site with the TCO / Designer at <https://mdcx.org>** | IT + in-tank CDU pump power + outdoor rejection + distribution losses + auxiliaries (the UPS is outside the box, so its losses land in site capacity, not in this container) | ✅ adjudicated |

> ⚠️ **PUE is written `1.0x` everywhere (adjudicated by Yuri, 2026-08-30 · C-2 closed).** Facility load varies with PUE and is **computed per site with the TCO / Designer at <https://mdcx.org>; no figure is given**. I400C45's former 440–500 kW is itself void, so **there is nothing to halve into 220–250 kW in the first place**.
>
> **Both measures must still be quoted** ([[CLAUDE.md]] Hard Rule 5). The correct customer-facing wording is: "IT load is 200 kW; total site power varies with PUE and is calculated per site against climate and heat-rejection selection at <https://mdcx.org>" — **with no facility-load number**.

---

## 4. Immersion Tank (I50TS) Spec ^sec-4-rack-spec

The building block of I200C20 is four [[I50TS]] single-phase immersion tanks — **the same tank used in I400C45 and I400C40**, only fewer of them. **I50TS is a tank component, not a SKU** (formerly A32).

| Item | Spec | Confidence / closure |
|------|------|----------------------|
| Tank model | **I50TS** (formerly A32) | ⏳ **#unconfirmed** — the code was derived KB-side from the Tank naming regex; waiting on the site side to enter it in the `docs/PRODUCT-MATRIX.md` Alias registry, expected TBD |
| Quantity per container | **4** | ✅ Site |
| IT capacity per tank | **50 kW** (T50) | ✅ Site |
| Cooling method | Single-phase immersion | ✅ Site |
| In-tank CDU | **Dual CDU · 2N** | ✅ Site |
| Oil-side ΔT | **8 K** | ✅ Site |
| Oil flow per tank | **≈11–12 m³/h** | ✅ Site |
| Supported GPU platforms | 4090 · 5090 · RTX PRO 6000 · H100 · H200 (PCIe) | ✅ Site |
| Tank external dimensions / RU / OU | ⏳ **#unconfirmed** | Waiting on the site side or I50TS DESIGN/ for a tank specification sheet; expected TBD |
| Dielectric fluid grade and properties | ⏳ **#unconfirmed** | Waiting on the Cooling Engineer for the I200C20 fluid selection and measured-property report; expected TBD |
| In-tank PDU specification | ⏳ **#unconfirmed** | Waiting on the Power Engineer for the I50TS PDU specification table; expected TBD |
| Max server depth / rack standards | ⏳ **#unconfirmed** | Waiting on the site side or I50TS DESIGN/ to publish the server compatibility table; expected TBD |

> **A common tank means common O&M practice**, but it **does not mean tank dimension figures may be carried across from the I400 documents** — those come from legacy product documents (A32 V1.4) that [[PRODUCT_SPEC_BASELINE]] does not cover.

---

## 5. Cooling System ^sec-5-cooling

Single-phase immersion: whole servers sit in dielectric fluid, the in-tank CDU plate heat exchangers hand that heat to facility water, and the outdoor plant rejects it to atmosphere. **On I200C20 this architecture is identical to I400 — only the tank count drops from eight to four** — which is exactly why a 20ft box can carry 200 kW without derating density.

### 5.1 Two loops

| Loop | Medium | Role | Confidence |
|------|--------|------|------------|
| Secondary (oil side) | Single-phase immersion dielectric fluid | Immerses the servers; rejects heat to facility water via the in-tank CDU plate HX | ✅ Site |
| Primary (facility water) | Facility water / glycol solution | Connects to the outdoor dry cooler or Hybrid Chiller | ✅ Site |
| Air branch | ⏳ **#unconfirmed** | The baseline lists no air-cooled rack for I200C20; waiting on the site side or DESIGN/ to state whether one is fitted, expected TBD | ⏳ |

```
IT Load → Dielectric fluid (4× I50TS) → Dual CDU plate HX (2N) → Facility water (temperatures unconfirmed)
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
| Container secondary flow (4 tanks) | **≈44–48 m³/h** | 🔶 **derived** — from 11–12 m³/h × 4; design value, subject to final selection |
| **Facility water temperatures** | ⏳ **#unconfirmed** | **The 32 / 37 °C figure has site evidence for I400C45 only and must not be applied to I200C20.** Waiting on the site side to publish temperatures on the I200C20 product page, or on the Cooling Engineer for a selection; expected TBD |
| Outdoor heat source | Dry coolers primarily; Hybrid Chiller added at peak-climate sites | ✅ Site |
| Facility-side ΔT / flow | ⏳ **#unconfirmed** | Waiting on the Cooling Engineer for the I200C20 primary-loop hydraulic calculation; expected TBD |
| Outdoor heat-rejection baseline (kW) | ⏳ **#unconfirmed** | Waiting on the Cooling Engineer for the I200C20 rejection calculation; expected TBD |
| Design ambient wet-bulb | ⏳ **#unconfirmed** | Waiting on the site side or I200C20 DESIGN/ to publish the design wet-bulb; expected TBD |

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
| Both CDUs fail | That tank shuts down; the other three are unaffected | High |
| Outdoor plant failure | Facility water temperature rises; derate or shut down | Medium |
| Fouled plate HX / filter | Reduced heat transfer, rising oil temperature | Medium |

> **Note that a four-tank box loses a larger share on a tank outage than an eight-tank box:** one tank down on I200C20 is 25% of compute, against 12.5% on an I400. This is a difference to explain during selection, not a defect — the unit of redundancy is still the container (see §6.2).

### 5.5 Heat-rejection configuration rule

Each I200C20 is paired **one-to-one** with its Cooling Zone outdoor plant; plant is not shared across containers. System-level availability is achieved by **adding containers**.

---

## 6. Power Distribution ^sec-6-power

The I200C20 power boundary is **outside the box**: UPS, batteries and PDC are supplied by the site or the Power Zone, and the container only receives an incoming feed. No power-bay volume is reserved inside the 20ft envelope — one of the reasons 200 kW of density fits inside 20 feet at all.

```
Grid / BESS / Generator → Customer-side UPS and distribution (outside) → I200C20 incomer
                                                                              ↓
                                                In-container distribution → 4× I50TS in-tank PDUs
```

| Item | Spec | Confidence / closure |
|------|------|----------------------|
| UPS boundary | **Outside the box** (site / customer supplies UPS, batteries, PDC) | ✅ Site |
| UPS capacity | **Not applicable** — baseline §2.3 records this field as not applicable; MDCX does not define a UPS capacity for this SKU | ✅ Site |
| Battery ride-through | ⏳ **#unconfirmed** | Waiting on the site side to publish an I200C20 ride-through position, or on the project to set it from the customer's UPS selection; expected TBD |
| UL compliance | ⏳ **#unconfirmed** | Waiting on the site side or the Compliance Officer to confirm the I200C20 full-system UL path (**the ✅ UL compliant of I400C45 must not be extrapolated**); expected TBD |
| Supply system (incoming voltage) | ⏳ **#unconfirmed** | Waiting on the site side to publish supply voltages on the immersion product pages (the 380 / 400 / 415 / 480 V AC row in baseline §1.3 covers the liquid line only); expected TBD |
| In-container topology (feeds / ATS / PDC) | ⏳ **#unconfirmed** | Waiting on the Power Engineer for the I200C20 single-line diagram; expected TBD |
| In-container electrical load schedule | ⏳ **#unconfirmed** | Waiting on the Power Engineer for the I200C20 load schedule; expected TBD |

> ⚠️ **UPS ≠ BESS.** UPS is minutes-scale ride-through; BESS is hours-scale storage. On I200C20 both sit outside the box, but they are different equipment and different procurement items and the terms are not interchangeable ([[CLAUDE.md]] Hard Rule 7).
>
> ⚠️ **Compliance responsibility for the customer-side UPS rests with the customer / integrator** and the boundary must be stated in the contract.

### 6.1 800 V HVDC

Baseline §1.3 records 800 V HVDC as Roadmap Q3 2026 — **not shipping today**. That row covers the liquid line; whether the immersion line follows the same position is ⏳ **#unconfirmed** — waiting on the site side to publish it on the immersion product pages, expected TBD. **HVDC availability must not be promised to customers.**

### 6.2 Redundancy model ^sec-6-redundancy

> **The container is the smallest unit of redundancy.** From [[PRODUCT_SPEC_BASELINE#^baseline-immersion-cooling]] §3.3.

| Layer | Redundancy | Confidence |
|-------|------------|------------|
| In-tank cooling (dual CDU per I50TS) | **2N** | ✅ Site |
| Single-container IT | **No IT redundancy** — a container is one whole; there is no in-box N+1 | ✅ Site |
| System level | **N / N+1 / 2N achieved by adding containers** | ✅ Site |
| Design objective | Tier II investment reaching Tier III-class availability through differentiated redundancy | ✅ Site |
| Redundancy principle | 2N where failure is expensive, N+1 everywhere else — **never global 2N** | ✅ Site |

**Where I200C20 has the redundancy advantage:** the 20ft form factor makes "add another container" a realistic path on a small site — two I200C20 units forming N+1 still sit inside a smaller transport and lifting envelope than one 40ft box. For a space-constrained customer who nonetheless needs availability, that is the real value of I200C20 rather than a compromise.

---

## 7. Structural Specifications #unconfirmed ^sec-7-structural

| Item | Spec | Confidence / closure |
|------|------|----------------------|
| Container | **20ft compute bay** | ✅ Site |
| External dimensions (L × W × H) | ⏳ **#unconfirmed** | Waiting on the site side or I200C20 DESIGN/ for an outline drawing (the 20ft ISO nominal figures are unconfirmed and **must not be inferred from an ISO table and quoted to a customer**); expected TBD |
| Empty weight | ⏳ **#unconfirmed** | Waiting on the structural engineer for a weighing report / structural calculation; expected TBD |
| Operating weight (fluid + IT) | ⏳ **#unconfirmed** | Waiting on the structural engineer for the structural calculation; expected TBD |
| Enclosure IP rating | ⏳ **#unconfirmed** | Waiting on the site side to publish, or on project-specific confirmation; expected TBD |
| Foundation loading and levelness | ⏳ **#unconfirmed** | Waiting on the structural engineer for foundation design criteria; expected TBD |

> ⚠️ **This entire section is unconfirmed, and it matters more on I200C20 than elsewhere** — its typical settings are rooftops, underground car parks and the inside of existing plant buildings, where **floor loading and clear height are the feasibility criteria themselves**. When a customer asks about dimensions or weight, follow [[UNCONFIRMED_Convention]] §5: answer "that parameter follows final selection and will be provided during technical clarification" and **give no number**; and write "structural verification required" into the proposal as a precondition.

---

## 8. Network & Cable Management #unconfirmed ^sec-8-network

| Item | Spec | Confidence / closure |
|------|------|----------------------|
| Default fabric / speeds / protocols | ⏳ **#unconfirmed** | Waiting on the site side or I200C20 DESIGN/ for a network configuration document; expected TBD |
| Cable entries and cable management | ⏳ **#unconfirmed** | Waiting on the site side or I200C20 DESIGN/ for penetration and tray drawings; expected TBD |
| Out-of-band management | ⏳ **#unconfirmed** | Waiting on the site side or I200C20 DESIGN/ to publish the OOB design; expected TBD |
| Switch mounting location | ⏳ **#unconfirmed** | Waiting on the site side or DESIGN/ to state it (the baseline lists no air-cooled rack for I200C20, so how switching is housed is undecided); expected TBD |

> [[PRODUCT_SPEC_BASELINE]] does not cover network fields for the immersion line. Where a project genuinely has network requirements, run a project-level design through [[NETWORK_Guideline]] — **do not quote another SKU's network configuration as an I200C20 specification**.

---

## 9. Environmental & Compliance ^sec-9-environment

| Item | Spec | Confidence / closure |
|------|------|----------------------|
| Heat-rejection climate gate | Historical extreme dry-bulb **≤ 24 °C** → dry coolers primarily; **> 24 °C** → add a Hybrid Chiller | ✅ Site |
| Warranty backing | Immersion line backed by the OEM; **Intel DataCenter Certified** | ✅ Site |
| Availability target | Tier II investment → Tier III-class availability (differentiated redundancy) | ✅ Site |
| UL compliance | ⏳ **#unconfirmed** | Waiting on the site side or the Compliance Officer to confirm the I200C20 UL path; expected TBD |
| Operating ambient temperature range | ⏳ **#unconfirmed** | Waiting on the site side or I200C20 DESIGN/ to publish the operating envelope; expected TBD |
| Operating humidity | ⏳ **#unconfirmed** | Waiting on the site side or I200C20 DESIGN/ to publish; expected TBD |
| Operating altitude / derating curve | ⏳ **#unconfirmed** | Waiting on the Power Engineer and Cooling Engineer for altitude derating; expected TBD |
| CE / local certification path | ⏳ **#unconfirmed** | Waiting on the Compliance Officer to confirm the market-access path for the target market; expected TBD |
| Indoor deployment compliance (plant buildings / underground) | ⏳ **#unconfirmed** | Waiting on the Compliance Officer to confirm fire and ventilation code fit for indoor placement (indoor settings are typical for I200C20); expected TBD |

> **No competitor comparison.** Customer-facing material must not quote non-MDCX product parameters for comparative advantage ([[CLAUDE.md]] Hard Rule 3).

---

## 10. Monitoring & Management ^sec-10-monitoring

| Item | Spec | Confidence / closure |
|------|------|----------------------|
| **CIOS** | Included with every MDCX. Path-addressed telemetry, alarm-to-ticket, O&M workflows, usage metering; open-source core Apache-2.0 (Roadmap) | ✅ Site |
| Digital twin | **NVIDIA Omniverse** — live state projected onto a 3D model | ✅ Site |
| DCM (compute marketplace) | **Roadmap · MVP in development** — **must not be committed to customers as a delivered capability** | ✅ Site |
| Protocol / interface list | ⏳ **#unconfirmed** | Waiting on the site side or the CIOS team for the I200C20 interface list; expected TBD |
| Monitoring point schedule | ⏳ **#unconfirmed** | Waiting on the Cooling Engineer and Power Engineer for the I200C20 point list; expected TBD |
| Fluid-level alarm tiers | ⏳ **#unconfirmed** | Waiting on I50TS DESIGN/ for the level-alarm setpoint table; expected TBD |

---

## 11. Fire Protection & Safety #unconfirmed ^sec-11-fire

| Item | Spec | Confidence / closure |
|------|------|----------------------|
| Clean agent type and concentration | ⏳ **#unconfirmed** | Waiting on the site side or I200C20 DESIGN/ for the fire protection design; expected TBD |
| Detection system | ⏳ **#unconfirmed** | Waiting on the same; expected TBD |
| Fire zoning principle | ⏳ **#unconfirmed** | Waiting on the same; expected TBD |
| Leak / spill containment design | ⏳ **#unconfirmed** | Waiting on I50TS DESIGN/ for containment and spill-response design; expected TBD |
| EPO / grounding / insulation monitoring | ⏳ **#unconfirmed** | Waiting on the Power Engineer for the electrical safety design; expected TBD |

> [[PRODUCT_SPEC_BASELINE]] does not cover fire protection fields for the immersion line. **I200C20's indoor deployment scenarios make fire protection a high-priority open item** — placed inside an existing plant building or an underground space, the container's fire system must interlock with the building's existing system; this is project-level design and must pass the local fire authority review.

---

## 12. Service, Delivery and Commercial Position ^sec-12-service

### 12.1 Price — the standard answer

> **配置方案由 MDCX 工程团队提供，价格由商务团队核算，请联系客户经理获取正式报价。**
> *(The configuration is provided by the MDCX engineering team; pricing is calculated by the commercial team — please contact your account manager for a formal quotation.)*

This document and every version of it **contain no price figures** ([[CLAUDE.md]] Hard Rule 1). **Note in particular: the fact that I200C20 carries half the IT capacity of an I400 must never be used to hint at a half-price range** — see the wording rules in §2.1.

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
| Scale-out | Add I200C20 units — **the 20ft form factor makes multi-container growth a real option on constrained sites**; system-level N / N+1 / 2N is set by container count (§6.2) |
| Mixed deployment | Cluster with I400C45 / I400C40 — the same I50TS tank means common O&M practice and common spares |
| Densification | A tank is already at the T50 ceiling; raising density requires re-validating cooling and power and is outside the standard product |

---

## 13. Site & Installation Requirements ^sec-13-site

I200C20's siting criteria differ from I400's. For I400 the first constraint is usually power and heat rejection; for I200C20 it is usually **structure and the access route** — floor loading, clear height, lifting radius, lift or ramp envelope. These must be verified during the proposal stage, not left to deployment.

| Item | Requirement | Confidence / closure |
|------|-------------|----------------------|
| Outdoor plant | One-to-one per container: dry coolers primarily, Hybrid Chiller at peak-climate sites. Plant is not shared across containers | ✅ Site |
| Climate gate | Historical extreme dry-bulb ≤ 24 °C permits the free-cooling route; above 24 °C the Hybrid Chiller's DX energy must be calculated and added to facility load | ✅ Site |
| Power connection | The customer supplies UPS, batteries and distribution; the container only receives an incoming feed | ✅ Site |
| Floor / slab loading | ⏳ **#unconfirmed** | Waiting on the structural engineer for operating weight and foundation criteria (see §7); **indoor and rooftop settings require a building structural review**; expected TBD |
| Floor levelness | ⏳ **#unconfirmed** | Waiting on the structural engineer for installation tolerances; expected TBD |
| Clearances / service aisles | ⏳ **#unconfirmed** | Waiting on the Layout Planner for I200C20 site clearance requirements; expected TBD |
| Road, clear height and lifting envelope | ⏳ **#unconfirmed** | Waiting on the structural engineer to confirm the 20ft transport envelope, lifting points and indoor access route; expected TBD |
| Fluid fill and hazmat | ⏳ **#unconfirmed** | Waiting on the Compliance Officer to confirm dielectric transport / storage / fill-and-drain requirements; expected TBD |
| Local permits | Planning, utility, fire, environmental — **project-specific confirmation**; indoor deployment additionally requires building and fire approvals | Project-dependent |

### 13.1 Zone boundaries

| Zone | Relation to I200C20 |
|------|---------------------|
| IT Zone | **I200C20 itself** (4× I50TS) |
| Power Zone | **UPS, batteries and PDC are all outside the box**, on the customer / Power Zone side |
| Cooling Zone | Outdoor dry cooler / Hybrid Chiller one-to-one, **not integrated inside the container** |

---

## 14. Key Specifications Summary ^sec-14-summary

| Item | Spec | Confidence |
|------|------|------------|
| Full SKU ID | `I200C20ST50` | ✅ |
| Container | 20ft compute bay | ✅ |
| IT Load | **200 kW** | ✅ |
| Total Facility Load | Varies with PUE — **computed per site at <https://mdcx.org>** (must not be halved from I400) | ✅ adjudicated |
| Immersion tanks | 4× I50TS at 50 kW each (T50) | ✅ |
| Per-tank density | **50 kW — identical to I400C45 / I400C40** | ✅ |
| GPU platforms | 4090 · 5090 · RTX PRO 6000 · H100 · H200 (PCIe) | ✅ |
| Maximum GPU count | ⏳ **#unconfirmed** | ⏳ |
| Cooling method | Single-phase immersion; dual CDU per tank, **2N** | ✅ |
| Oil-side ΔT | 8 K | ✅ |
| Oil flow per tank | ≈11–12 m³/h | ✅ |
| Container secondary flow | ≈44–48 m³/h (design value) | 🔶 derived |
| Facility water | ⏳ **#unconfirmed** — the 32 / 37 °C of I400C45 does not carry over | ⏳ |
| PUE | **`1.0x`** — computed per site with the TCO / Designer at <https://mdcx.org>; no fixed value and no range | ✅ adjudicated |
| Outdoor heat source | Dry coolers primarily; Hybrid Chiller at peak-climate sites | ✅ |
| UPS boundary | **Outside the box** (customer / Power Zone) | ✅ |
| Battery ride-through | ⏳ **#unconfirmed** | ⏳ |
| UL compliance | ⏳ **#unconfirmed** | ⏳ |
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
| 1 | ~~Total Facility Load range~~ **closed** | — | 2026-08-30 ruling: varies with PUE, computed per site at <https://mdcx.org>; no figure is given | closed |
| 2 | **Facility water temperatures** | Site side / Cooling Engineer | I200C20 primary temperatures (the 32/37 °C of I400C45 does not carry over) | TBD |
| 3 | Maximum GPU count | Site side | Disclosure on the I200C20 product page | TBD |
| 4 | Whether an air-cooled rack is fitted | Site side / DESIGN | Statement of whether I200C20 includes an air rack and how switching is housed | TBD |
| 5 | Battery ride-through position | Site side | I200C20 ride-through disclosure | TBD |
| 6 | UL compliance path | Site side / Compliance Officer | Confirmation of UL status | TBD |
| 7 | 20ft external dimensions, empty / operating weight | Structural engineer | Outline drawing + structural calculation (mandatory for indoor / rooftop cases) | TBD |
| 8 | Layout drawing and tank arrangement | Layout Planner | I200C20 general arrangement | TBD |
| 9 | Supply system and in-container topology | Power Engineer | Single-line diagram + load schedule | TBD |
| 10 | Fire design (including indoor interlock) | Site side / DESIGN | Fire protection design statement | TBD |
| 11 | Annual maintenance contract (AMC) detail | Commercial team | Invoice / contractual standard service terms (warranty term and SLA were closed by the 2026-08-30 ruling) | TBD |
| 12 | Whether the dummy-load burn-in happens at the factory or on site | ATS | Confirmation of where the 5–30 days is executed (does not affect the EXW commitment) | TBD |

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| v1.1 | 2026-08-30 | **Yuri's four rulings of 2026-08-30 propagated ([[PRODUCT_SPEC_BASELINE]] v2.0).** (1) **PUE is written `1.0x` everywhere**: the "≈1.05 + ≤24 °C dry-bulb boundary" in §5.3 is void and the §3.1 Total Facility Load moves from ⏳ to "varies with PUE, computed per site with the TCO / Designer at <https://mdcx.org>" (§3.1 / §5.3 / §14 / open item 1 in §14.1 closed); the §3 IT Load vs Total Facility Load distinction and the "do not halve from I400" caution are retained. (2) **Lead time is unified to 120 days EXW for the first batch and 90 days EXW for Scale, counted from order placement**, with a new dummy-load burn-in period of 5–30 days (Supermicro recommendation, outside the EXW commitment); the commercial, freight and installation segments carry no commitment. The §12.2 ⛔ two-position table and "~185–230 days", the §12.3 four-phase rows and "3–4 weeks on-site installation and commissioning", and the §14 ⛔ lead-time row are **deleted**. (3) **Warranty is unified to core components for one year from EXW plus an annual service fee thereafter**, with ONSITE / NBD / 9×5 / 24×7 response levels governed by the Invoice (§12.3 / §14). (4) Open items 11 / 12 in §14.1 are rewritten accordingly. The dual-loop GPU-side temperature ruling does not apply to the immersion line. |
| v1.0 | 2026-08-30 | First release. I200C20 English pre-sales Tech Spec built on the 14-section I400C40 structure; every product figure taken from [[PRODUCT_SPEC_BASELINE]] v1.0 and marked row by row against the four confidence levels of [[UNCONFIRMED_Convention]]; §2 states positively that this is not a halved I400 and gives wording rules; §3.1 and §5.2 explicitly forbid carrying the I400C45 facility load and 32/37 °C temperatures across; §5 binds PUE 1.05 to the ≤24 °C dry-bulb boundary; §6.2 records the immersion redundancy model; §12 records the ⛔ lead-time conflict and the standard price answer. Section-for-section and row-for-row parallel to [[I200C20_Tech_Spec_CN]]. This edition is a single file; block splitting will be done if and when it is needed. |
