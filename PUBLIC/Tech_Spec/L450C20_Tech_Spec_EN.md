---
tags:
  - "#MDC"
  - "#type/design-spec"
  - "#product/l450c20"
  - "#unconfirmed"
doc_version: v1.1
updated: 2026-08-30
audience: Sales / pre-sales / account managers / solution architects
sku_id: L450C20DR150
---

# L450C20 — Quick Tech Spec (English) ^mdc-965b30c3c6
**Dual-Loop Direct Liquid Cooled Containerized Data Center (20ft · 150 kW per rack)**

> **Audience:** Sales / pre-sales deliverable. Readers: account managers, pre-sales engineers, solution architects. **This edition contains a large number of ⏳ unconfirmed fields and must NOT be sent to customers as-is** — use [[L450C20_Tech_Spec_External]] for anything client-facing.
>
> **Companion editions:** [[L450C20_Tech_Spec_CN|中文版 / Chinese]] · [[L450C20_Tech_Spec_External|External / 对外输出版]]
>
> **Source of truth:** every product figure below comes from [[PRODUCT_SPEC_BASELINE]] (the six-SKU specification baseline). **Where parameters disagree, the baseline table wins**; where the baseline disagrees with the MDC site repo, the site repo wins. Confidence-marker semantics: [[UNCONFIRMED_Convention]] §2.
>
> **This edition is a single file; block splitting (`_blocks/`) is deferred until needed.** Anchors `^sec-1-layout` … `^sec-14-summary` are preserved, so block-level references of the form `[[L450C20_Tech_Spec_EN#^sec-5-cooling]]` continue to resolve.

Version: v1.1 | Date: 2026-08-30 | Full SKU ID: `L450C20DR150` | Status: `shipped` ^mdc-c2f2e707a6

> **v1.1 update — Yuri's rulings of 2026-08-30 are propagated here:**
> - **Temperatures (C-1 closed):** outdoor-plant supply 32–36 °C → CDU approach +4 °C → **GPU cold-plate inlet 36–40 °C**. The former "GPU 36–45 °C" ceiling of 45 was wrong and is now 40. This SKU shares that chain with L1800C45. The approved STULZ SCR 14103 W selection sheet (FWS 36/46 · TCS 40/50) is the **hot-end design point** of the chain and is consistent with the ruling — but its capacity, envelope and flow figures still **must not** be used for this SKU. ^mdc-e8b7232784
> - **PUE (C-2 closed):** always written **`1.0x`** — no fixed value, no range. Computed per site with the TCO / Designer at <https://mdcx.org>; Total Facility Load likewise carries no figure, while the IT Load vs Total Facility Load distinction is retained.
> - **Lead time (C-8 closed):** **120 days EXW** first batch, **90 days EXW** for Scale, counted from order placement; dummy-load burn-in period **5–30 days** (Supermicro recommendation, not covered by the EXW commitment); the commercial, freight and installation segments carry **no commitment**. The old ~185–230 days and the four-phase timeline are deleted.
> - **Warranty (C-9 closed):** core components for **one year from EXW**, annual service fee thereafter; ONSITE / NBD / 9×5 / 24×7 response levels are **governed by the Invoice** and are neither committed to nor defined here.
>
> **v1.0 first release — read this first (still valid):**
> 1. **L450C20 has the thinnest written basis of the three liquid-cooling SKUs.** The site's customer-facing pages disclose exactly four things: 450 kW IT capacity, 150 kW rack density, the dual-loop temperature levels (GPU 36–40 °C ✅ adjudicated 2026-08-30 / in-row CW 10/15 °C), and the UPS being outside the container. **Every other field has no source.** ^mdc-e738dd2eab
> 2. This SKU has **no DESIGN/ engineering documentation**. Cooling selection is fixed as to model and count (CDU 1× STULZ SCR 14103 W; in-row CW **4× STULZ CRS 320 CW / CW320**, raised from 2 on 2026-09-02), and **the per-unit ratings were frozen on 2026-09-08 against the vendor selection sheet** — see [[PRD-STULZ-CW320]] v2.0.
> 3. **Do not copy cooling parameters from [[L1800C45_Tech_Spec_EN|L1800C45]].** Both are dual loop at the same nominal temperatures, but L1800C45's SCR 14103 W (1200 kW per unit) and CRS 560 CW (57.3 kW per unit) were selected for 1800 kW in a 45ft shell; neither the capacity class nor the physical envelope fits a 20ft container. Baseline §1.2 marks CDU, in-row CW, secondary fluid and terminal composition for L450C20 as ⛔ **conflict** across the board. ^mdc-ee741dedcc
> 4. **Do not copy anything from [[L1240C45_Tech_Spec_EN|L1240C45]].** That is a different system entirely — single loop, UPS inside, 45ft. ^mdc-694014bdf1

---

## Document Navigation

| § | Section | Status in this edition |
|---|---------|------------------------|
| 1 | Layout | ⏳ drawings not issued |
| 2 | Product Positioning | ✅ |
| 3 | IT Capacity (incl. IT Load vs Total Facility Load) | partly ⏳ |
| 4 | Rack Specifications | mostly ⏳ |
| 5 | Cooling System (dual loop: warm-water GPU + CyberRow CW in-row units) | architecture ✅ / equipment ⏳ |
| 6 | Power Distribution (UPS outside the container) | partly ⏳ |
| 7 | Structural Specifications | mostly ⏳ |
| 8 | Network & Cable Management | ⏳ |
| 9 | Environmental & Compliance | ⏳ |
| 10 | Monitoring & Management System | ✅ |
| 11 | Fire Protection & Safety | ⏳ |
| 12 | Service & Support (lead time / warranty adjudicated) | ✅ adjudicated / partly ⏳ |
| 13 | Site & Installation Requirements | partly ⏳ |
| 14 | Key Specifications Summary | — |

> **This edition is a single file; block splitting is deferred until needed.**

---

## 1. Layout ^sec-1-layout

| Drawing | Status |
|---|---|
| TOP view | ⏳ **#unconfirmed** — waiting on the Layout Planner to issue the L450C20 `Layout/` three-view set (see the pending-documents list in [[KB/LIQUID/L450C20/index|L450C20 index]]), expected TBD ^mdc-22565e8e08 |
| FRONT view | ⏳ **#unconfirmed** — waiting on the Layout Planner to issue the L450C20 `Layout/` three-view set, expected TBD ^mdc-c0e5d58b0b |
| SIDE view | ⏳ **#unconfirmed** — waiting on the Layout Planner to issue the L450C20 `Layout/` three-view set, expected TBD ^mdc-0f1d6d1de9 |

> Packing density inside a 20ft shell is this SKU's central engineering problem: dual loop means **two independent pipework systems** (warm water plus chilled water) inside roughly 44% of the length available in a 45ft machine. Until the three-view set exists, no statement about the internal arrangement can stand.

---

## 2. Product Positioning ^sec-2-positioning

L450C20 is a **20ft dual-loop direct-liquid-cooled container**, up to 150 kW per rack and 450 kW IT per container. ^mdc-25d46ff39f

**The reason this SKU exists is a doorway.**

A 45ft High Cube is a steel box 13.7 m long and 2.99 m tall. There are many places it cannot enter: legacy buildings with barely three metres of clear height, rooftop plant rooms served only by a goods lift, campuses behind a height-restricted underpass, hill sites where a rural bend cannot be negotiated, dense urban plots where the crane has nowhere to stand. Those sites are not short of power and not short of demand — they are short of **a physical route a 45ft box can travel**.

L450C20 is built for exactly that: a 20ft standard shell, which puts transport, lifting and access back into the most ordinary category there is. ^mdc-4af5bd9736

**State the cost up front: it is more expensive per kW.** A dual-loop CDU, in-row CW, two pipework systems, controls, fire protection and monitoring — those fixed costs are amortised over 450 kW instead of 1240 kW or 1800 kW, so unit cost is necessarily higher. **That is not a defect; that is the price of fitting through the opening.** If a customer's site can take a 45ft container, they should buy a 45ft container. The only legitimate reason to choose L450C20 is that a 45ft container cannot get in. ^mdc-2f79b6d4c9

> **Do not describe this SKU as a stripped-down version.** L450C20 shares the dual-loop architecture and the GPU warm-water / in-row CW chilled-water scheme with L1800C45, and shares the `R150` density code with L1240C45. It is not a big container cut in half — it is a different shell, laid out from scratch. ^mdc-1dfdfc14cf

**Division of labour against the other two SKUs on the line:**

| SKU | When to pick it | Governing constraint |
|---|---|---|
| [[L1240C45_Tech_Spec_EN\|L1240C45]] | The site can take a 45ft box and has **no** separate electrical room; UPS and batteries should arrive with the container | UPS **inside**, 150 kW per rack, single-loop three-branch TCS (PG25, 26–28 °C) ^mdc-23481ec09e |
| [[L1800C45_Tech_Spec_EN\|L1800C45]] | The site can take a 45ft box and **already has** an electrical room; out of floor, not power, and wants maximum density per footprint | UPS **outside**, 220 kW per rack, dual loop ^mdc-51b054ca90 |
| **L450C20 (this document)** | **A 45ft box cannot get in.** Legacy buildings, rooftops, basements, height- or width-restricted haul routes | 20ft shell, 450 kW, 150 kW per rack, dual loop, UPS **outside** ^mdc-190e62d242 |

> **No competitor comparison.** The table above compares SKUs within our own line only.

---

## 3. IT Capacity ^sec-3-it-capacity

| Item | Parameter | Confidence |
|---|---|---|
| **Total IT capacity** | **450 kW** | ✅ site |
| Maximum rack density | **150 kW** (density code `R150`) | ✅ site |
| Rack count and composition | **3× 150 kW liquid, no air rack** (site profile l450.json) | ✅ ^mdc-5b14f34fb7 |
| GPU platforms | ⏳ **#unconfirmed** — **the site discloses GPU platforms only for L1240C45 and L1800C45, not for this SKU.** Waiting on the site product page or L450C20 `DESIGN/`, expected TBD | ⏳ ^mdc-ebb5d8b067 |
| Liquid / air load split (φ_air) | ⏳ **#unconfirmed** — waiting on the Cooling Engineer for the dual-loop heat-split calculation, expected TBD | ⏳ |

> 🔶 **derived note (must not be quoted as a specification):** 450 kW ÷ 150 kW per rack back-calculates to roughly 3 racks. Baseline §1.1 explicitly classifies that back-calculation as 🔶 derived and **it must not be issued to customers as a specification**.
>
> ⚠️ **Do not assume the GPU platforms match L1240C45's just because both carry `R150`.** GB300 NVL72 / B300 HGX is an explicit site disclosure *for L1240C45*; for L450C20 the site says nothing. Whether a 20ft shell can accommodate NVL72-class rack depth and service access is itself unverified. ^mdc-001d259a09

### 3.1 IT Load vs Total Facility Load ^sec-3-it-vs-facility

**This is the enforcement wording for [[CLAUDE.md]] Hard Rule 5. When a customer says "I need X MW", establish which of the two they mean before anything else.**

| Metric | Definition | L450C20 value | Confidence ^mdc-4b359a2c2d |
|---|---|---|---|
| **IT Load** | Electrical power actually consumed by servers / GPUs, excluding all cooling and distribution losses | **450 kW** | ✅ site |
| **Total Facility Load** | IT Load + CDU pump power + in-row CW fans + outdoor heat rejection + distribution losses + auxiliaries | **Varies with PUE — computed per site with the TCO / Designer at <https://mdcx.org>** | ✅ adjudicated |

> **PUE is written `1.0x` everywhere (adjudicated by Yuri, 2026-08-30 · C-2 closed).** No fixed value, no range, no "typical value". Facility load varies with PUE and is **computed per site with the TCO / Designer at <https://mdcx.org>** — that is the route to take when a customer needs a facility load for a utility application, **not a back-of-envelope conversion at PUE 1.15 or similar**.
>
> **The IT Load vs Total Facility Load distinction must be kept** ([[CLAUDE.md]] Hard Rule 5): customers buy compute against IT Load and apply for substation capacity and model electricity cost against Total Facility Load. **Only the facility-load figure is withheld.**

---

## 4. Rack Specifications ^sec-4-rack-spec

| Item | Parameter | Confidence |
|---|---|---|
| Maximum rack power | **150 kW** | ✅ site |
| Cooling method | Direct liquid cooling (cold plate), secondary side served by the CDU TCS loop | ✅ site |
| Rack quantity | **3** (3× 150 kW liquid, no air rack, site profile l450.json) | ✅ ^mdc-eb0d98c0af |
| Rack form factor (U height / depth / width) | ⏳ **#unconfirmed** — waiting on the Layout Planner to select the L450C20 rack; internal width and service clearance in a 20ft shell are hard constraints and 45ft values cannot be carried over, expected TBD | ⏳ ^mdc-22375b4d78 |
| Manifold configuration (per rack / branch flow / PICV) | ⏳ **#unconfirmed** — waiting on the Cooling Engineer for the secondary-side hydraulic distribution calculation, which requires the CDU selection first, expected TBD | ⏳ |
| Rack PDU rating | ⏳ **#unconfirmed** — waiting on the Power Engineer for the in-container distribution design (the UPS is outside; PDU upstream comes from the site PDC), expected TBD | ⏳ |

---

## 5. Cooling System (Dual-Loop Architecture) ^sec-5-cooling

### 5.1 Architecture overview — two independent loops

L450C20 is a **dual-loop (`D`)** product, sharing the architectural pattern of [[L1800C45_Tech_Spec_EN|L1800C45]]: two loops run in parallel inside the container, fully independent in fluid, temperature and hydraulics. ^mdc-a353a18493

| Loop | Load carried | Temperatures | Fluid | Terminal equipment |
|---|---|---|---|---|
| **Loop A — GPU-side warm water** | GPU / CPU cold-plate liquid load (the great majority of the IT heat) | **GPU cold-plate inlet 36–40 °C** ✅ adjudicated; outdoor-plant supply into the CDU primary side **32–36 °C**; CDU approach **+4 °C** | ⏳ **#unconfirmed** — waiting on the L450C20 CDU selection sheet to fix the secondary fluid (pure water / PG / EG), expected TBD | ⏳ CDU unselected ^mdc-9cc464a483 |
| **Loop B — In-row CW chilled water** | Residual room air load (whatever the cold plates do not take, power modules, network gear, auxiliaries) | **10 / 15 °C chilled water** | **Pure water, 0 % glycol** ✅ selection sheet 2026-09-08 | ✅ in-row CW fixed at **4× CRS 320 CW** |

**Why they have to be separate:** cold plates will happily take water in the 40 °C class; air-side terminals will not — bringing room return air down to a usable supply temperature requires coil water in the 10 °C class. Force both onto one loop and either the cold-plate side is stuck with cold water (throwing away free-cooling hours and driving up PUE) or the in-row CW side runs short of capacity. Decoupled, Loop A's 36–40 °C warm water can be rejected on dry coolers alone in most climates, while Loop B carries a far smaller chilled-water load.

> ## Dual-loop GPU-side temperature chain (adjudicated by Yuri, 2026-08-30 · C-1 closed)
>
> ```
> outdoor plant (dry cooler) supply   32–36 °C
>         ↓  into the CDU primary side (FWS)
>      CDU plate-HX approach          +4 °C
>         ↓  out of the CDU secondary side (TCS)
>   GPU cold-plate inlet              36–40 °C
> ```
>
> **The previously written "GPU 36–45 °C" had the wrong ceiling: 45 becomes 40.** The chain applies to **both L1800C45 and L450C20** — the two dual-loop, UPS-outside DLC solutions. ^mdc-afe337728d
>
> **Relationship to the approved STULZ SCR 14103 W selection sheet:** that sheet (FWS 36/46 °C · TCS 40/50 °C) takes the **hot-end design point** of this chain, with an approach of exactly 4 °C — **not a second set of temperatures, but the same chain evaluated at the worst case**. Note it was selected for L1800C45's 1200 kW class: **this SKU must not quote its capacity, envelope or flow figures**, only the temperature chain is shared. See [[PRODUCT_SPEC_BASELINE#^baseline-liquid-cooling]]. ^mdc-f68bd88c21

**Fitting a dual loop into a 20ft shell is this SKU's dominant engineering constraint.** Two pump sets, two pipework systems, two sets of external connections and two pressurisation / make-up arrangements all have to go inside roughly six metres — which is precisely why the CDU and in-row CW selections cannot be transplanted from the 45ft machines.

^sec-5-dual-loop

### 5.2 Loop A — CDU (GPU side)

| Item | Parameter | Confidence |
|---|---|---|
| GPU-side temperatures | **GPU cold-plate inlet 36–40 °C warm water**; outdoor-plant supply into the CDU primary side 32–36 °C; CDU approach +4 °C | ✅ adjudicated 2026-08-30 |
| CDU model | ⛔ **conflict** — **this SKU has no ATS-approved CDU of any kind**; waiting on the Cooling Engineer for a 450 kW-class selection and on the [[3rd Party List]] admission process, expected TBD | ⛔ **conflict** ^mdc-a81870e23f |
| Capacity per unit / quantity / redundancy | ⛔ **conflict** — waiting on the Cooling Engineer for a 450 kW-class CDU selection and on the [[3rd Party List]] admission process, expected TBD | ⛔ **conflict** ^mdc-96418a1475 |
| Specific FWS / TCS supply / return points | ⏳ **#unconfirmed** — the ruling fixes the band (FWS in 32–36 °C · approach +4 °C · TCS out 36–40 °C), but this SKU's specific supply / return points and ΔT still await the CDU selection sheet, expected TBD | ⏳ |
| Secondary fluid | ⏳ **#unconfirmed** — waiting on the CDU selection sheet (pure water / PG25 / EG); **must not default to L1800C45's pure water or L1240C45's PG25**, expected TBD | ⏳ ^mdc-2bf32d6f08 |
| Secondary flow / head / pressure drop | ⏳ **#unconfirmed** — waiting on the CDU selection sheet, expected TBD | ⏳ |
| Connection type and size | ⏳ **#unconfirmed** — waiting on the CDU selection sheet and vendor drawing, expected TBD | ⏳ |
| CDU envelope and weight | ⏳ **#unconfirmed** — waiting on the vendor drawing; **the installable envelope inside a 20ft shell is itself a selection constraint** and must be fixed jointly with the Layout Planner, expected TBD | ⏳ |

> ⚠️ **Do not quote any figure from [[PRD-STULZ-SCR14103W]].** That SCR 14103 W is 1200 kW per unit, 2,090 × 900 × 1,200 mm, 1,175 kg operating, selected for 1800 kW in a 45ft shell. 450 kW needs an entirely different capacity class, and the space and load headroom in a 20ft shell is not comparable.

### 5.3 Loop B — in-row CW (room side)

| Item | Parameter | Confidence |
|---|---|---|
| in-row CW temperatures | **10 / 15 °C chilled water** | ✅ site |
| In-row CW model and count | **4× STULZ CRS 320 CW (CW320)** — raised from 2 on 2026-09-02 (**two units were short on AIRFLOW, not on capacity**). Per-unit data frozen 2026-09-08 against the StulzSelect selection sheet. See [[PRD-STULZ-CW320]] v2.0 | ✅ |
| Capacity / airflow per unit | **Gross 33.6 kW · fan 4.5 kW · net 29.1 kW · 6,100 m³/h · EER 6.47** — condition: return 37 °C / 27 % rel. · chilled water 10/15 °C · 0 % glycol · ESP 0 Pa (StulzSelect selection sheet). ⚠️ **The three fans already run at 3,850 of 3,850 rpm — there is no airflow headroom at all.** The previous 35.8 / 34.3 / 6,400 figures and the derived 1.49 kW fan power are **superseded** | ✅ selection sheet |
| Quantity and redundancy model | **Four units. N+1 holds, but the margin is now thin.** Fleet: net **116.4 kW** / **24,400 m³/h** / fan **18.0 kW** / **23.2 m³/h**. With one unit out: 87.3 kW and **18,300 m³/h** against the worst demand of **18,043 m³/h** (3 racks × 10× B300) — **1.4 % of margin**, down from 6.4 % before the freeze. ⚠️ **This SKU is bound by AIRFLOW, not capacity; any airflow increase breaks N+1** | ✅ site profile · recomputed 2026-09-08 |
| Water flow / pressure drop / connections | Flow **5.8 m³/h** (selection sheet; the house formula 33.6/(1.163×5) = 5.78 confirms it) · **per-unit pressure drop 119 kPa** (coil 64 + DN25 two-way valve 33 + internal pipework 22) · **DN25 × 1** two-way valve ✅; ⏳ connection positions still pending the outline drawing | ✅ / ⏳ positions |
| Envelope and weight | **400 W × 1,950 H × 1,375 D mm · 190 kg** ✅ selection sheet 2026-09-08 (400 mm is the vendor's custom floor; the height is corrected from the provisional 2,000 to the 1,950 cabinet). Supply **380 V / 50 Hz / 3Ph / N / PE**. **Floor space for FOUR units inside a 20 ft shell still has to be checked** | ✅ / ⚠️ layout pending |
| Electrical supply and certification (CE / UL / CCC) | ⏳ **#unconfirmed** — waiting on STULZ for certificate numbers; **certification cannot be inferred from [[PRD-STULZ-CRS560CW]]** ([[PRD-STULZ-CeilAir]] is the precedent for the same vendor with CE absent), expected TBD | ⏳ |

> ✅ **Parameters frozen 2026-09-08.** The StulzSelect selection sheet has landed; thermal, hydraulic and dimensional data are all vendor values, so **per-unit performance figures may now be quoted**. Only acoustics and certification remain open ([[PRD-STULZ-CW320]] Q10 / Q5).
>
> ⚠️ **The headline risk is now whether FOUR units (400 × 1,950 × 1,375 mm, 190 kg each) fit a 20 ft shell** — the count went from 2 to 4 on 2026-09-02, so the floor width they occupy went from 800 to 1,600 mm.
>
> ⚠️ **Top risk: whether two units physically fit a 20 ft enclosure has not been checked.** Usable volume in 20 ft is far smaller than in 45 ft, and the sibling model on L1800C45 (CRS 560 CW) is a floor-standing cabinet at 254 kg per unit. See [[PRD-STULZ-CW320]] Q2. ^mdc-87cbff54cc

^sec-5-crah

### 5.4 Outdoor side and system level

| Item | Parameter | Confidence |
|---|---|---|
| Loop A outdoor heat-rejection form | Dry-cooler-led (32–36 °C supply gives long free-cooling hours), with mechanical topping at peak-climate sites | 🔶 derived — an engineering judgement drawn from the adjudicated 32–36 °C outdoor-plant supply level; design value, subject to final selection |
| Loop B outdoor heat-rejection form | Chiller plant (10/15 °C chilled water) | 🔶 derived — an engineering judgement drawn from the in-row CW 10/15 °C level; design value, subject to final selection |
| Terminal composition | ⏳ **#unconfirmed** — baseline §1.2 explicitly marks terminal composition for this SKU as ⏳; waiting on L450C20 `DESIGN/`, expected TBD | ⏳ ^mdc-73f26190ad |
| Total outdoor heat-rejection baseline | ⏳ **#unconfirmed** — waiting on the Cooling Engineer for the dual-loop outdoor heat balance (it must yield two separate figures, one per loop), expected TBD | ⏳ |
| PUE | **`1.0x`** — no fixed value, no range, no "typical value". Computed per site with the TCO / Designer at <https://mdcx.org>. Qualitatively: climates where dry coolers reject heat year-round sit at the low end, hotter sites need a hybrid chiller and PUE moves up — **but no number is given** | ✅ adjudicated |
| Control strategy and GPU interlocks | ⏳ **#unconfirmed** — waiting on L450C20 `DESIGN/` for the control strategy (flow floors, GPU throttle thresholds, dual-loop failure transfer), expected TBD | ⏳ ^mdc-1a2912f23c |

---

## 6. Power Distribution ^sec-6-power

### 6.1 Power boundary: the UPS is outside — that is a configuration, not a downgrade

**In the site's own words: *"that's a configuration, not a downgrade."***

On L450C20 the UPS, batteries and PDC sit **outside the container and are provided by the site**. On a 20ft shell that boundary choice is even more direct than on a 45ft one: **there is no second possibility inside the box.** ^mdc-639b7e31e3

A 20ft container's internal length is about 44% of a 45ft High Cube's. Fit compute racks, two dual-loop pump sets and pipework systems, distribution, fire protection and monitoring inside it, then carve out an electrical bay large enough for a UPS and a battery string, and 450 kW of IT capacity stops being achievable. Putting the power boundary outside buys back:

1. **All of the interior goes to compute and dual-loop pipework.** This is the precondition for 450 kW existing in a 20ft shell at all.
2. **Backup time is set by the site** against its own availability target, uncapped by the shell's volume.
3. **The electrical side can be expanded and maintained independently** — UPS expansion and battery replacement never touch the container.

> **Talk-track note:** if a customer asks "why doesn't this container include a UPS", the correct answer is "this SKU's power boundary is designed to sit outside so that the interior is entirely compute and dual-loop pipework", not "the UPS was left out". If the customer genuinely needs the boundary outside but does not want to build electrical infrastructure, MDCX's **standalone power module (UPS / battery / PDC) is in development** — all three liquid-cooling product pages on the site disclose this roadmap item, so it may be raised openly, but it **must not be committed as deliverable**.

### 6.2 Distribution parameters

| Item | Parameter | Confidence |
|---|---|---|
| UPS boundary | **Outside the container** — UPS / batteries / PDC supplied by the site | ✅ site |
| UPS model / battery autonomy | **Not applicable** (outside this SKU's delivery scope) | ✅ site |
| Supply voltages | **380 / 400 / 415 / 480 V AC** | ✅ site |
| 800 V HVDC | **Roadmap Q3 2026, not shipping today** — disclosable, not committable | ✅ site |
| In-container busbar | ⏳ **#unconfirmed** — waiting on the Power Engineer to select the in-container busbar (its rating depends on the site PDC feeder size and the rack count, neither of which is locked), expected TBD | ⏳ |
| Per-rack distribution (TOU / MCB ratings) | ⏳ **#unconfirmed** — waiting on the Power Engineer's distribution design; rack count and actual per-rack draw are undetermined, so no ratings can be stated, expected TBD | ⏳ |
| Cooling-equipment supply | ⏳ **#unconfirmed** — neither CDU nor in-row CW is selected; waiting on the Cooling Engineer to complete the selection and state pump and fan power, expected TBD | ⏳ |
| Power factor | ⏳ **#unconfirmed** — waiting on the Power Engineer (the UPS is off-container, so the value follows the site's UPS model), expected TBD | ⏳ |

---

## 7. Structural Specifications ^sec-7-structural

| Item | Parameter | Confidence |
|---|---|---|
| Container type | **20ft** | ✅ site |
| Exterior dimensions (L × W × H) | ⏳ **#unconfirmed** — the 20ft ISO nominal envelope 6,058 × 2,438 × 2,591 mm is **unconfirmed**, and the baseline does not establish whether this SKU uses a standard or a High Cube shell. Waiting on L450C20 `DESIGN/` or a vendor drawing, expected TBD | ⏳ ^mdc-8e3ab5a2dc |
| Interior clear height / usable width | ⏳ **#unconfirmed** — waiting on the L450C20 `Layout/` three-view set, expected TBD | ⏳ ^mdc-b14a965e14 |
| Empty weight | ⏳ **#unconfirmed** — waiting on the L450C20 `DESIGN/` structural load calculation and the factory weigh-out, expected TBD | ⏳ ^mdc-8ae427512b |
| Loaded weight (with IT) | ⏳ **#unconfirmed** — waiting on the L450C20 `DESIGN/` structural load calculation and the factory weigh-out, expected TBD | ⏳ ^mdc-bafa59e392 |
| Enclosure rating | ⏳ **#unconfirmed** — waiting on the L450C20 `DESIGN/` compliance checklist, expected TBD | ⏳ ^mdc-d275a2258c |

> ⚠️ **Exterior dimensions are the field customers ask about most and the one we can least afford to guess.** "Will it fit through my opening?" is the core scenario for this SKU — and baseline §1.4 explicitly marks the 20ft ISO nominal figures as unconfirmed. The correct handling: tell the customer that exterior dimensions follow the final drawings and will be provided during technical clarification, and collect their clearance height, width, turning radius and lifting conditions as RFI items. **Do not quote 6,058 × 2,438 × 2,591.**

---

## 8. Network & Cable Management ^sec-8-network

| Item | Parameter | Confidence |
|---|---|---|
| Cable penetration (top / bottom entry) | ⏳ **#unconfirmed** — waiting on the Layout Planner for the L450C20 penetration and tray design, expected TBD | ⏳ ^mdc-33ebd4774e |
| Cable tray position | ⏳ **#unconfirmed** — waiting on the Layout Planner for the L450C20 penetration and tray design, expected TBD | ⏳ ^mdc-4cdbb2162d |
| Fibre / network entry position | ⏳ **#unconfirmed** — waiting on the Layout Planner for the L450C20 penetration and tray design, expected TBD | ⏳ ^mdc-5afc482344 |

> Dual-loop pipework already claims a great deal of the ceiling and floor volume in a 20ft shell, so tray routing and penetration positions must be laid out together with the cooling pipework and cannot be defined before the cooling design is settled.

---

## 9. Environmental & Compliance ^sec-9-environment

| Item | Parameter | Confidence |
|---|---|---|
| Operating temperature range | ⏳ **#unconfirmed** — waiting on the L450C20 `DESIGN/` compliance checklist, expected TBD | ⏳ ^mdc-748ea1a7a4 |
| Operating humidity range | ⏳ **#unconfirmed** — waiting on the L450C20 `DESIGN/` compliance checklist, expected TBD | ⏳ ^mdc-2887bf712b |
| Operating altitude | ⏳ **#unconfirmed** — waiting on the L450C20 `DESIGN/` compliance checklist; altitude correction must be rechecked once the in-row CW is selected, expected TBD | ⏳ ^mdc-39f29965d1 |
| Whole-unit certification path (UL / CE / TUV) | ⏳ **#unconfirmed** — waiting on the Compliance Officer for the L450C20 whole-unit certification path, expected TBD | ⏳ ^mdc-89ffe98cf8 |
| CDU / in-row CW component certification | ⏳ **#unconfirmed** — the equipment is unselected, so no certificates can be requested yet; once selected, waiting on the vendors for model-by-model CE / UL / CCC certificate numbers, expected TBD | ⏳ |

> ⚠️ **Certification does not transfer by analogy** — neither from the L1240C45 / L1800C45 whole-unit paths, nor from another model by the same vendor ([[PRD-STULZ-CeilAir]] is the precedent for CE being absent). ^mdc-f097e5a31b

---

## 10. Monitoring & Management System ^sec-10-monitoring

| Item | Parameter | Confidence |
|---|---|---|
| **CIOS** | Included with every MDCX. Path-addressed telemetry, alarm-to-ticket, operations workflows, usage metering | ✅ site |
| CIOS open-source core | Apache-2.0 — **roadmap**; disclosable, not committable as delivered capability | ✅ site |
| Digital twin | **NVIDIA Omniverse**, live state projected onto the 3D model | ✅ site |
| DCM (compute marketplace) | **Roadmap · MVP in development** — **must not be committed to customers as a delivered capability** | ✅ site |
| CDU / in-row CW telemetry points and integration | ⏳ **#unconfirmed** — the equipment is unselected; once selected, waiting on the vendors for Modbus / BACnet point lists, expected TBD | ⏳ |
| BMS integration protocol | ⏳ **#unconfirmed** — waiting on L450C20 `DESIGN/` for the monitoring architecture, expected TBD | ⏳ |

---

## 11. Fire Protection & Safety ^sec-11-fire

| Item | Parameter | Confidence |
|---|---|---|
| Extinguishing agent | ⏳ **#unconfirmed** — waiting on the L450C20 `DESIGN/` fire-protection design, expected TBD | ⏳ |
| Detection system | ⏳ **#unconfirmed** — waiting on the L450C20 `DESIGN/` fire-protection design, expected TBD | ⏳ |
| Fire panel / manual pull station / horn-strobe | ⏳ **#unconfirmed** — waiting on the L450C20 `DESIGN/` fire-protection design, expected TBD | ⏳ |
| Access control | ⏳ **#unconfirmed** — waiting on the L450C20 `DESIGN/` fire-protection design, expected TBD | ⏳ |
| Leak detection and response (dual loop) | ⏳ **#unconfirmed** — waiting on `DESIGN/`; leak zoning, containment and interlock logic for two independent pipework systems in a 20ft shell must be defined separately, expected TBD | ⏳ |

---

## 12. Service & Support ^sec-12-service

### 12.1 Standard answer to a price enquiry

> **The configuration is produced by the MDCX engineering team; pricing is calculated by the commercial team. Please contact your account manager for a formal quotation.**
> （配置方案由 MDCX 工程团队提供，价格由商务团队核算，请联系客户经理获取正式报价。）

This document, and every KB product document, **contains no price information** ([[CLAUDE.md]] Hard Rule 1).

> **This SKU's "more expensive per kW" is a qualitative statement only and must never be quantified.** §2 notes that unit cost is higher than on the 45ft machines; that is product positioning and **constitutes no price or price-comparison information**. Any customer question about multiples, ratios or unit prices goes to the commercial team.

### 12.2 Lead time — ✅ adjudicated by Yuri, 2026-08-30 (C-8 closed)

**EXW is the only commitment; nothing else is committed.**

| Item | Value | Nature of commitment | Confidence |
|---|---|---|---|
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

### 12.3 Other delivery and service terms

| Item | Parameter | Confidence |
|---|---|---|
| Prefabrication ratio | **99% completed before leaving the factory** | ✅ site |
| Freight & customs | **Buyer's responsibility; MDCX does not estimate them and commits to no duration** | ✅ adjudicated |
| On-site installation & commissioning | **Not committed** (neither duration nor scope) | ✅ adjudicated |
| Availability design target | **Tier II investment reaching Tier III-class availability through differentiated redundancy** | ✅ site |
| Redundancy principle | **2N** where failure is expensive, **N+1** elsewhere — **no blanket 2N** | ✅ site |
| **Warranty scope and term** | **Core components, one year from EXW** | ✅ adjudicated |
| **Subsequent years** | **Annual service fee** | ✅ adjudicated |
| **Support SLA (ONSITE / NBD / 9×5 / 24×7 etc.)** | **Governed by the Invoice** — the KB and Tech Specs neither commit to nor define it; refer customer questions to the commercial team | ✅ adjudicated |

---

## 13. Site & Installation Requirements ^sec-13-site

| Item | Requirement | Confidence |
|---|---|---|
| **Electrical infrastructure the site must provide** | **UPS / batteries / PDC supplied by the site** (see §6.1 — this is the SKU's boundary definition) | ✅ site |
| Cooling interfaces the site must provide | Two independent services: **Loop A warm water (outdoor-plant supply 32–36 °C, GPU cold-plate inlet 36–40 °C)** plus **Loop B chilled water (10/15 °C)**. They cannot be combined | ✅ adjudicated 2026-08-30 |
| Cooling connection type and size | ⏳ **#unconfirmed** — follows from the vendor drawings once the CDU / in-row CW selection is complete, expected TBD | ⏳ |
| Freight & customs | Buyer's responsibility; **no duration is committed** | ✅ adjudicated |
| On-site installation & commissioning | **Not committed** | ✅ adjudicated |
| **Transport and access conditions** (this SKU's key RFI item) | ⏳ **#unconfirmed** — exterior dimensions and loaded weight are undetermined (see §7), so no access criterion can be stated; waiting on L450C20 `DESIGN/` and the vendor drawings. **The customer's clearance height, width, turning radius and crane positions must nevertheless be collected at RFI stage**, since they are the precondition for choosing this SKU at all, expected TBD | ⏳ |
| Ground load capacity | ⏳ **#unconfirmed** — depends on the loaded weight (see §7, undetermined); waiting on the structural load calculation, expected TBD | ⏳ |
| Ground levelness | ⏳ **#unconfirmed** — waiting on L450C20 `DESIGN/`, expected TBD | ⏳ |
| Maintenance clearances | ⏳ **#unconfirmed** — waiting on the Layout Planner; service space inside a 20ft shell is tight and may require more clearance outside the container, expected TBD | ⏳ |
| Site climate suitability | ⏳ **#unconfirmed** — the secondary fluid is undetermined (see §5.2); waiting on the CDU selection sheet and an ATS freeze-protection decision before cold-site boundaries can be judged, expected TBD | ⏳ |
| Noise boundary | ⏳ **#unconfirmed** — the in-row CW is unselected; waiting on the vendor selection sheet for sound power and sound pressure data, expected TBD | ⏳ |

---

## 14. Key Specifications Summary ^sec-14-summary

| Item | Parameter | Confidence |
|---|---|---|
| Full SKU ID | `L450C20DR150` | ✅ site |
| Status | `shipped` (D-19 gate · 2026-08-27) | ✅ site |
| Container type | **20ft** | ✅ site |
| Exterior dimensions | ⏳ **#unconfirmed** — the 20ft ISO nominal envelope is unconfirmed; waiting on `DESIGN/` or a vendor drawing, expected TBD | ⏳ |
| **IT capacity** | **450 kW** | ✅ site |
| Total Facility Load | Varies with PUE — **computed per site at <https://mdcx.org>** | ✅ adjudicated |
| Maximum rack density | **150 kW** (`R150`) | ✅ site |
| Rack count and composition | ⏳ **#unconfirmed** — waiting on the Liquid Designer profile JSON / `DESIGN/`, expected TBD | ⏳ |
| GPU platforms | ⏳ **#unconfirmed** — not disclosed by the site for this SKU, expected TBD | ⏳ |
| Loops | **Dual loop (`D`)** | ✅ site |
| Loop A (GPU side) | **GPU cold-plate inlet 36–40 °C**; outdoor-plant supply 32–36 °C; CDU approach +4 °C | ✅ adjudicated |
| Loop B (in-row CW side) | **10 / 15 °C chilled water** | ✅ site |
| Secondary fluid | ⏳ **#unconfirmed** — waiting on the CDU selection sheet, expected TBD | ⏳ |
| CDU | ⏳ **#unconfirmed** — no ATS-approved model yet; waiting on a Cooling Engineer selection plus the admission process, expected TBD | ⏳ |
| in-row CW | **4× STULZ CRS 320 CW (CW320)** — net 116.4 kW / 24,400 m³/h / fan 18.0 kW; per-unit data frozen 2026-09-08, see [[PRD-STULZ-CW320]] v2.0. ⚠️ N+1 airflow margin 1.4 % | ✅ |
| Terminal composition | ⏳ **#unconfirmed** — waiting on `DESIGN/`, expected TBD | ⏳ |
| Outdoor heat-rejection baseline | ⏳ **#unconfirmed** — waiting on the Cooling Engineer's dual-loop heat balance, expected TBD | ⏳ |
| PUE | **`1.0x`** — computed per site with the TCO / Designer at <https://mdcx.org>; no fixed value and no range | ✅ adjudicated |
| **UPS boundary** | **Outside the container** (UPS / batteries / PDC supplied by the site) — **a configuration, not a downgrade** | ✅ site |
| Supply voltages | 380 / 400 / 415 / 480 V AC (800 V HVDC is roadmap Q3 2026, not shipping today) | ✅ site |
| In-container busbar | ⏳ **#unconfirmed** — waiting on the Power Engineer's selection, expected TBD | ⏳ |
| Empty / loaded weight | ⏳ **#unconfirmed** — waiting on the structural load calculation and factory weigh-out, expected TBD | ⏳ |
| Environment (temp / humidity / altitude) | ⏳ **#unconfirmed** — waiting on the `DESIGN/` compliance checklist, expected TBD | ⏳ |
| Certification | ⏳ **#unconfirmed** — waiting on the Compliance Officer for the whole unit; components require selection first, then model-by-model vendor certificates, expected TBD | ⏳ |
| Fire protection | ⏳ **#unconfirmed** — waiting on the `DESIGN/` fire-protection design, expected TBD | ⏳ |
| Software | CIOS (included) · NVIDIA Omniverse digital twin (included) · DCM (roadmap, not committed) | ✅ site |
| Availability | Tier II investment → Tier III-class availability; 2N where failure is expensive, N+1 elsewhere | ✅ site |
| Lead time | **120 days EXW first batch / 90 days EXW for Scale** (from order placement); dummy-load burn-in 5–30 days (not covered by the EXW commitment); commercial, freight and installation carry **no commitment** | ✅ adjudicated |
| Warranty | **Core components, one year from EXW**; annual service fee thereafter; ONSITE / NBD / 9×5 / 24×7 response levels are **governed by the Invoice** | ✅ adjudicated |
| Price | **This document contains no pricing.** The configuration is produced by the MDCX engineering team; pricing is calculated by the commercial team — contact your account manager for a formal quotation | — |

---

## Changelog

| Version | Date | Summary |
|---|---|---|
| 2026-09-20 | 🧭 unconfirmed-170 改为 ⛔ conflict，未裁定赢家 |
| 2026-09-20 | 🧭 unconfirmed-194 已可关闭（已可关闭） |
| 2026-09-20 | 🧭 unconfirmed-195 已可关闭（已可关闭） |
| 2026-09-20 | 🧭 unconfirmed-226 改为 ⛔ conflict，未裁定赢家 |
| 2026-09-20 | 🧭 unconfirmed-227 改为 ⛔ conflict，未裁定赢家 |
| **v1.4** | **2026-09-08** | **In-row CW parameters frozen against the StulzSelect selection sheet; the vendor catalogue table is superseded.** Per unit: gross 35.8→**33.6**, fan 1.49 (derived)→**4.5** (and already at 3,850 rpm, no headroom), net 34.3→**29.1** kW, airflow 6,400→**6,100**, water 6.16→**5.8** m³/h; added **119 kPa per-unit pressure drop · DN25 valve · 400×1,950×1,375 · 190 kg · 380 V**. Also corrects the **count from 2 to 4** (decided 2026-09-02, never synced here): fleet net **116.4 kW** / **24,400 m³/h** / fan **18.0 kW**, and the **N+1 airflow margin falls from 6.4 % to 1.4 %**. Headline risk restated as the 20 ft floor layout for four units |
| v1.3 | 2026-09-02 | (backfilled) In-row CW raised from 2 to **4× CRS 320 CW** — two units were short on airflow, not on capacity |
| v1.2 | 2026-08-31 | In-row CW model changed from CRS 330 CW (withdrawn by STULZ) to **2× CRS 320 CW, N+1**. Catalogue ratings entered at return 37 °C / 25 % rel. · chilled **10/15 °C** · 0 % glycol: gross 35.8 kW, 6,400 m³/h, 6.16 m³/h water, width 400 mm (custom floor). Fan power 1.49 kW and net 34.3 kW remain derived; height × depth provisional |
| v1.1 | 2026-08-30 | **Yuri's four rulings of 2026-08-30 propagated ([[PRODUCT_SPEC_BASELINE]] v2.0).** (1) **The dual-loop GPU-side temperature chain is fixed**: outdoor-plant supply 32–36 °C → CDU approach +4 °C → GPU cold-plate inlet **36–40 °C**; the former "GPU 36–45 °C" ceiling of 45 becomes 40 (header note / §5.1 / §5.2 / §5.4 / §13 / §14), with a note that this SKU shares the chain with L1800C45 and that the approved STULZ SCR 14103 W selection sheet is its **hot-end design point** (its capacity and envelope still may not be borrowed). (2) **PUE is written `1.0x` everywhere** and Total Facility Load becomes "varies with PUE, computed per site with the TCO / Designer at <https://mdcx.org>" (§3.1 / §5.4 / §14); the former ⏳ becomes ✅, and the §3 IT Load vs Total Facility Load distinction is retained as a hard rule. (3) **Lead time is unified to 120 days EXW for the first batch and 90 days EXW for Scale, counted from order placement**, with a new dummy-load burn-in period of 5–30 days (Supermicro recommendation, outside the EXW commitment); the commercial, freight and installation segments carry no commitment. The §12.2 ⛔ two-basis table and "~185–230 days", and the four-phase cycle and "3–4 weeks on-site installation & commissioning" rows in §12.3 and §13, are **deleted**. (4) **Warranty is unified to core components for one year from EXW plus an annual service fee thereafter**, with ONSITE / NBD / 9×5 / 24×7 response levels governed by the Invoice (§12.3 / §14). |
| v1.1 | 2026-08-30 | Absorbed Yuri's adjudication and the site audit: in-row CW fixed at 2× STULZ CRS 330 CW (CW330) N+1, CDU at 1× SCR 14103 W, rack build at 3 liquid-cooled racks with no air rack (site `l450.json`); added the network-equipment placement note arising from the absent air rack and the "two units into 20 ft" risk flag |
| v1.0 | 2026-08-30 | First release. L450C20 English Tech Spec built on the 14-section structure of [[L1240C45_Tech_Spec_EN]], as a single file preserving anchors `^sec-1-layout` … `^sec-14-summary`. All figures sourced from [[PRODUCT_SPEC_BASELINE]]; the site discloses only IT capacity, rack density, dual-loop temperatures and the power boundary, so every other field is marked ⏳ line by line per [[UNCONFIRMED_Convention]], each naming who is waited on, for what, and by when. §5 records the in-row CW as suspected at first release ([[PRD-STULZ-CW320|CRS 330 CW, later renamed]]); §12 records the ⛔ lead-time basis conflict as it stands; §6.1 states positively that an external UPS is a configuration, not a downgrade; §3.1 explicitly separates IT Load from Total Facility Load; §7 forbids quoting the unconfirmed 20ft ISO nominal envelope. **No figure was borrowed from L1240C45 or L1800C45.** Section numbering, anchors and table row counts match [[L450C20_Tech_Spec_CN]] one-for-one. |
