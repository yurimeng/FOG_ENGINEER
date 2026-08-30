---
tags:
  - "#MDC"
  - "#type/design-spec"
  - "#product/l1800c45"
  - "#unconfirmed"
doc_version: v1.1
updated: 2026-08-30
audience: Sales / pre-sales / account managers / solution architects
sku_id: L1800C45DR220
---

# L1800C45 — Quick Tech Spec (English)
**Dual-Loop Direct Liquid Cooled Containerized Data Center (45ft High Cube · 220 kW per rack)**

> **Audience:** Sales / pre-sales deliverable. Readers: account managers, pre-sales engineers, solution architects. **This edition contains ⏳ unconfirmed fields and must NOT be sent to customers as-is** — use [[L1800C45_Tech_Spec_External]] for anything client-facing.
>
> **Companion editions:** [[L1800C45_Tech_Spec_CN|中文版 / Chinese]] · [[L1800C45_Tech_Spec_External|External / 对外输出版]]
>
> **Source of truth:** every product figure below comes from [[PRODUCT_SPEC_BASELINE]] (the six-SKU specification baseline). **Where parameters disagree, the baseline table wins**; where the baseline disagrees with the MDC site repo, the site repo wins. Confidence-marker semantics: [[UNCONFIRMED_Convention]] §2.
>
> **This edition is a single file; block splitting (`_blocks/`) is deferred until needed.** Anchors `^sec-1-layout` … `^sec-14-summary` are preserved, so block-level references of the form `[[L1800C45_Tech_Spec_EN#^sec-5-cooling]]` continue to resolve.

Version: v1.1 | Date: 2026-08-30 | Full SKU ID: `L1800C45DR220` | Status: `shipped`

> **v1.1 update — Yuri's rulings of 2026-08-30 are propagated here:**
> - **Temperatures (C-1 closed):** outdoor-plant supply 32–36 °C → CDU approach +4 °C → **GPU cold-plate inlet 36–40 °C**. The former "GPU 36–45 °C" ceiling of 45 was wrong and is now 40. The approved STULZ SCR 14103 W selection sheet (FWS 36/46 · TCS 40/50) is the **hot-end design point** of that chain, consistent with the ruling — not a second set of temperatures.
> - **PUE (C-2 closed):** always written **`1.0x`** — no fixed value, no range. Computed per site with the TCO / Designer at <https://mdcx.org>; Total Facility Load likewise carries no figure, while the IT Load vs Total Facility Load distinction is retained.
> - **Lead time (C-8 closed):** **120 days EXW** first batch, **90 days EXW** for Scale, counted from order placement; dummy-load burn-in period **5–30 days** (Supermicro recommendation, not covered by the EXW commitment); the commercial, freight and installation segments carry **no commitment**. The old ~185–230 days and the four-phase timeline are deleted.
> - **Warranty (C-9 closed):** core components for **one year from EXW**, annual service fee thereafter; ONSITE / NBD / 9×5 / 24×7 response levels are **governed by the Invoice** and are neither committed to nor defined here.
>
> **v1.0 first release — notes (still valid):**
> 1. This SKU has **no DESIGN/ engineering documentation yet.** Capacity, density, temperature levels and the power boundary are taken from the site's customer-facing wording (`PRODUCT-MATRIX.md` D-13 · `llms-full.txt`).
> 2. Two cooling devices are ATS-approved with written vendor backing: CDU = **STULZ SCR 14103 W** ([[PRD-STULZ-SCR14103W]]), 列间空调 = **STULZ CRS 560 CW** ([[PRD-STULZ-CRS560CW]]). Those two PRDs are currently the only written basis for this SKU's cooling selection.
> 3. **No L1800C45-specific CDU / 列间空调 Requirement exists.** The current [[CDU_Requirement V5]] / [[CRAH_Requirement V5]] are scoped to L1240C45 and **do not apply here** — temperatures run about 14 K higher, the fluid is pure water, and the connections are Tri-Clamp.
> 4. Structural, environmental, network, fire and service fields are all ⏳ **#unconfirmed**, pending DESIGN/. **Do not backfill them from L1240C45.**

---

## Document Navigation

| § | Section | Status in this edition |
|---|---------|------------------------|
| 1 | Layout | ⏳ drawings not issued |
| 2 | Product Positioning | ✅ |
| 3 | IT Capacity (incl. IT Load vs Total Facility Load) | partly ⏳ |
| 4 | Rack Specifications | mostly ⏳ |
| 5 | Cooling System (dual loop: warm-water GPU + CyberRow CW in-row units) | ✅ equipment approved |
| 6 | Power Distribution (UPS outside the container) | partly ⏳ |
| 7 | Structural Specifications | partly ⏳ |
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
| TOP view | ⏳ **#unconfirmed** — waiting on the Layout Planner to issue the L1800C45 `Layout/` three-view set (see the pending-documents list in [[KB/LIQUID/L1800C45/index|L1800C45 index]]), expected TBD |
| FRONT view | ⏳ **#unconfirmed** — waiting on the Layout Planner to issue the L1800C45 `Layout/` three-view set, expected TBD |
| SIDE view | ⏳ **#unconfirmed** — waiting on the Layout Planner to issue the L1800C45 `Layout/` three-view set, expected TBD |

> **Do not substitute L1240C45's `TOP.svg` / `FRONT.jpg` / `SIDE.jpg`.** Both are 45ft High Cube shells, but L1800C45 is dual-loop, has its UPS outside the container, and its upper module has been raised from 600 mm to 900 mm (to pull the primary-side interconnect headers inboard). The internal arrangements are not interchangeable.
>
> The site repo carries a 3D / hero animation project at `DC45_3D/L1800_Hero.blend`. It is usable as customer-facing presentation material but is **not an engineering drawing**.

---

## 2. Product Positioning ^sec-2-positioning

L1800C45 is a **45ft High Cube dual-loop direct-liquid-cooled container**, up to 220 kW per rack and 1800 kW IT per container, aimed at rack-scale SXM / NVLink GPU systems such as GB300 NVL72 and B300 HGX.

**The reason this SKU exists fits in one sentence: you are out of floor, not out of power.**

The typical buyer already has the substation capacity — an MV feed on the campus, spare transformer headroom, sometimes a finished electrical room — but does not have enough floor area, ceiling height or slab capacity to spread out a field of 100 kW-class air-cooled or single-loop liquid racks. L1800C45 uses **220 kW per rack** to compress the same compute into the same 45ft footprint: each container slot returns 1800 kW of IT rather than 1240 kW. When the site charges by the square metre, or when building height and floor loading cap the expansion, that density delta is the decision variable.

**Division of labour against the other two SKUs on the line:**

| SKU | When to pick it | Governing constraint |
|---|---|---|
| [[L1240C45_Tech_Spec_EN\|L1240C45]] | The site has **no** separate electrical room and wants UPS + batteries + busbar to arrive with the container as one closed delivery | UPS **inside**, 150 kW per rack, single-loop three-branch TCS (PG25, 26–28 °C) |
| **L1800C45 (this document)** | The site **already has** — or is willing to build — an electrical room, and wants maximum IT density per footprint | UPS **outside**, 220 kW per rack, dual loop (GPU 36–40 °C warm water + 列间空调 10/16 °C chilled water) |
| [[L450C20_Tech_Spec_EN\|L450C20]] | Sites a 45ft high-cube simply **cannot enter**: legacy buildings, rooftops, basements, height- or width-restricted haul routes | 20ft shell, 450 kW, dual loop, UPS outside |

**The dual loop is this SKU's architectural watershed.** L1240C45 hangs cold plates, rear-door heat exchangers and ceiling units off a single 26–28 °C PG25 TCS. L1800C45 instead puts the GPU cold-plate load on a **36–40 °C warm-water** loop (long free-cooling hours on dry coolers outdoors) and gives the residual air-side load its own **independent 10/16 °C chilled-water** in-row CW loop. The two loops are decoupled in fluid, temperature and hydraulics, and neither constrains the other — that is the system complexity you pay for pushing a rack to 220 kW, and it is also where the energy return comes from.

> **No competitor comparison.** The table above compares SKUs within our own line only.

---

## 3. IT Capacity ^sec-3-it-capacity

| Item | Parameter | Confidence |
|---|---|---|
| **Total IT capacity** | **1800 kW** | ✅ site |
| Maximum rack density | **220 kW** (density code `R220`) | ✅ site |
| Rack count and composition | **8× 220 kW liquid-cooled + 1× 40 kW air-cooled = 9 racks** | ✅ site Designer profile `l1800.json` |
| GPU platforms | GB300 NVL72 · B300 HGX (SXM / NVLink) | ✅ site |
| Liquid / air load split (φ_air) | ⏳ **#unconfirmed** — waiting on the Cooling Engineer for the dual-loop heat-split calculation (it sets the 列间空调 quantity, see [[PRD-STULZ-CRS560CW]] Q1), expected TBD | ⏳ |

> 🔶 **derived note (must not be quoted as a specification):** 1800 kW ÷ 220 kW per rack back-calculates to roughly 8–9 racks. Baseline §1.1 explicitly classifies that back-calculation as 🔶 derived and **it must not be issued to customers as a specification**.
>
> ⚠️ The [[Projects/台山_7.5MW_L1800/Project_Record|Taishan 7.5 MW project]] records a volumetric planning figure of "16 IT rack positions per container". **That is a project-side rack-position plan, not a product rack-count specification** (16 × 220 kW ≫ 1800 kW). The two must not be cited for each other.

### 3.1 IT Load vs Total Facility Load ^sec-3-it-vs-facility

**This is the enforcement wording for [[CLAUDE.md]] Hard Rule 5. When a customer says "I need X MW", establish which of the two they mean before anything else.**

| Metric | Definition | L1800C45 value | Confidence |
|---|---|---|---|
| **IT Load** | Electrical power actually consumed by servers / GPUs, excluding all cooling and distribution losses | **1800 kW** | ✅ site |
| **Total Facility Load** | IT Load + CDU pump power + 列间空调 fans + outdoor heat rejection + distribution losses + auxiliaries | **Varies with PUE — computed per site with the TCO / Designer at <https://mdcx.org>** | ✅ adjudicated |

> **PUE is written `1.0x` everywhere (adjudicated by Yuri, 2026-08-30 · C-2 closed).** No fixed value, no range, no "typical value" — it is computed per site with the TCO / Designer at <https://mdcx.org>. L1240C45's former 1.15–1.20 / 1.07–1.35 figures are void, so **there is no PUE number to port across in the first place**.
>
> **The IT Load vs Total Facility Load distinction must be kept** ([[CLAUDE.md]] Hard Rule 5): customers buy compute against IT Load and apply for substation capacity and model electricity cost against Total Facility Load. **Only the facility-load figure is withheld.**
>
> **Known component figures** (usable for engineering estimates, not a complete facility load):
> - CDU pump set **20.0 kW per unit** (3 × CM 25-2 @ 6.7 kW, ✅ [[PRD-STULZ-SCR14103W]] §2.4) — unit count undetermined, so total pump power is undetermined
> - 列间空调 total input **2.6 kW per unit** (i.e. fan power, ✅ [[PRD-STULZ-CRS560CW]] §2.1) — unit count undetermined, so total fan power is undetermined

---

## 4. Rack Specifications ^sec-4-rack-spec

| Item | Parameter | Confidence |
|---|---|---|
| Maximum rack power | **220 kW** | ✅ site |
| Cooling method | Direct liquid cooling (cold plate), secondary side served by the CDU TCS loop | ✅ site |
| Rack quantity | ⏳ **#unconfirmed** — waiting on L1800C45 `DESIGN/` or the site Liquid Designer profile JSON, expected TBD | ⏳ |
| Rack form factor (U height / depth / width) | ⏳ **#unconfirmed** — waiting on the Layout Planner to select the L1800C45 rack, expected TBD | ⏳ |
| Manifold configuration (per rack / branch flow / PICV) | ⏳ **#unconfirmed** — waiting on the Cooling Engineer for the secondary-side hydraulic distribution calculation (same batch as the [[PRD-STULZ-SCR14103W]] Q2 pump-head margin check), expected TBD | ⏳ |
| Rack PDU rating | ⏳ **#unconfirmed** — waiting on the Power Engineer for the in-container distribution design (the UPS is outside; PDU upstream comes from the site PDC), expected TBD | ⏳ |

> **Do not borrow figures from [[L1240C45_Tech_Spec_EN]] §4.** L1240C45's 48U / 1200 mm deep / 800 mm wide / 2–3 manifolds per rack / 1.6–2.1 L/min per branch are all values inside a 150 kW single-loop PG25 system. At 220 kW per rack, pure-water secondary fluid and 40/50 °C temperatures, every one of them has to be recomputed.

---

## 5. Cooling System (Dual-Loop Architecture) ^sec-5-cooling

### 5.1 Architecture overview — two independent loops

L1800C45 is a **dual-loop (`D`)** product. Two loops run in parallel inside the container, fully independent in fluid, temperature and hydraulics:

| Loop | Load carried | Temperatures | Fluid | Terminal equipment |
|---|---|---|---|---|
| **Loop A — GPU-side warm water** | GPU / CPU cold-plate liquid load (the great majority of the IT heat) | **GPU cold-plate inlet 36–40 °C** ✅ adjudicated; outdoor-plant supply into the CDU primary side **32–36 °C**; CDU approach **+4 °C**. The approved CDU selection point FWS 36/46 °C · TCS 40/50 °C is the **hot-end design point** of that band | **Pure water, 0% glycol** | Cold plates + **STULZ SCR 14103 W** CDU |
| **Loop B — In-row CW chilled water** | Residual room air load (whatever the cold plates do not take, power modules, network gear, auxiliaries) | **10 / 16 °C chilled water** | **Pure water, 0% glycol** | **STULZ CRS 560 CW** room-level downflow precision air conditioners |

**Why they have to be separate:** cold plates will happily take water in the 40 °C class; air-side terminals will not — dropping a 36 °C return down to a 21 °C supply requires coil water in the 10 °C class. Force both onto one loop and either the cold-plate side is stuck with cold water (throwing away free-cooling hours and driving up PUE) or the in-row CW side runs short of capacity (supply temperature goes out of control). Decoupled, Loop A's 36–40 °C warm water can be rejected on dry coolers alone in most climates with mechanical cooling only as a topper, while Loop B carries a far smaller chilled-water load and a correspondingly smaller chiller. **That is the price of a 220 kW rack, and it is also the payoff.**

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
> **The previously written "GPU 36–45 °C" had the wrong ceiling: 45 becomes 40.**
>
> **Relationship to the approved STULZ SCR 14103 W selection sheet:** the selection sheet (FWS 36/46 °C · TCS 40/50 °C) takes the **hot-end design point** of that band, with an approach of exactly 4 °C, fully consistent with this ruling — **it is not a second set of temperatures, it is the same chain evaluated at the worst case**. See [[PRODUCT_SPEC_BASELINE#^baseline-liquid-cooling]].

> **The cooling baselines are not interchangeable with L1240C45's.** L1240C45 is a single-loop three-branch TCS (PG25 · 26–28 °C · DN100 flanges · self-contained ceiling DX). L1800C45 sits roughly 14 K higher, uses **pure water**, terminates the CDU in **Tri-Clamp** fittings, and uses an all-water **CW-type 列间空调 with no compressor**. See the delta tables in [[PRD-STULZ-SCR14103W]] §4 and [[PRD-STULZ-CRS560CW]] §4.

^sec-5-dual-loop

### 5.2 Loop A — CDU: STULZ SCR 14103 W ✅ ATS approved (2026-08-30)

Plate heat exchangers isolate the primary FWS (site / dry-cooler side) from the secondary TCS (cold-plate side), so site water quality never reaches the cold plates. Full parameters in [[PRD-STULZ-SCR14103W]].

| Item | Parameter | Confidence |
|---|---|---|
| Model | **STULZ SCR 14103 W** (FWS / TCS connections up) | ✅ ATS approved |
| Capacity per unit | **1200 kW** | ✅ selection sheet |
| FWS inlet / outlet | **36 / 46 °C** | ✅ selection sheet |
| TCS inlet / outlet | **40 / 50 °C** (40 °C supplied to the cold plates, 50 °C returned) | ✅ selection sheet |
| Fluid (primary / secondary) | **Pure water / pure water, glycol 0 / 0 %** | ✅ selection sheet |
| Plate heat exchangers | 2 units · approach **4 °C** · heat-transfer margin **41 %** | ✅ selection sheet |
| FWS / TCS total flow | **103.8 / 103.8 m³/h** (1.44 LPM/kW) | ✅ selection sheet |
| FWS / TCS total pressure drop | **140 / 195 kPa** | ✅ selection sheet |
| TCS ESP (selection input) | 150 kPa | ✅ selection sheet |
| Pump set | 3 × **CM 25-2** · 6.7 kW each · **20.0 kW total** · 3,515 rpm | ✅ selection sheet |
| Available head margin | **0.2 m** (34.7 m max / 34.5 m used) ⚠️ **P0 watch item** | ✅ selection sheet |
| Control-valve pressure drop | 80 kPa | ✅ selection sheet |
| Dry / operating weight | **950 kg / 1,175 kg** | ✅ vendor drawing |
| Dimensions (H × W × D) | **2,090 × 900 × 1,200 mm** (including base tray) | ✅ vendor drawing |
| Connections | 4 × DN100 (130 mm) **Tri-Clamp** · DIN 32676-B (ISO 1127), **top exit** | ✅ vendor drawing |
| Pipework material | Stainless steel | ✅ vendor drawing |
| Electrical supply | 3Ph / N / PE / 380 V / 50 Hz | ✅ selection sheet |
| **Unit count and redundancy model (N+1 / 2N)** | ⏳ **#unconfirmed** — waiting on ATS / Cooling Engineer for the 1800 kW IT ÷ 1200 kW per unit sizing and redundancy calculation, and for a ruling on whether the three in-unit pumps are 2+1 or 3 in parallel ([[PRD-STULZ-SCR14103W]] Q1, P0), expected TBD | ⏳ |
| Whether the secondary head margin forces a re-selection | ⏳ **#unconfirmed** — waiting on the Cooling Engineer to compute actual secondary-side resistance (pipework + headers + rack manifolds + PICV) and on STULZ to re-run the selection ([[PRD-STULZ-SCR14103W]] Q2, P0), expected TBD | ⏳ |
| Freeze-protection strategy for cold sites | ⏳ **#unconfirmed** — both primary and secondary sides are pure water with **no antifreeze**; waiting on an ATS decision between trace heating / drain-down / switching to PG, and its heat-transfer impact ([[PRD-STULZ-SCR14103W]] Q3, P0), expected TBD | ⏳ |

> ⚠️ **The available pump head margin is only 0.2 m (≈ 2 kPa).** If the real resistance of secondary pipework, headers, rack manifolds and PICVs exceeds the selection assumptions, it consumes the entire margin. This is the **primary P0 risk** on this SKU's cooling side and must be closed before any solution is quoted.

^sec-5-cdu

### 5.3 Loop B — 列间空调: STULZ CRS 560 CW ✅ ATS approved (2026-08-30)

Room-level downflow chilled-water precision air conditioner: **all-water coil plus a two-way control valve, no compressor and no refrigerant charge inside the unit.** Full parameters in [[PRD-STULZ-CRS560CW]].

| Item | Parameter | Confidence |
|---|---|---|
| Model | **STULZ CRS 560 CW** (non-standard variant) | ✅ ATS approved |
| Total / sensible capacity per unit | **57.3 / 57.3 kW** — **fully sensible**, no dehumidification headroom | ✅ selection sheet |
| Net total / net sensible capacity | 54.7 / 54.7 kW (after deducting fan heat gain) | ✅ selection sheet |
| Return-air temperature / humidity | **36 °C / 25 % rel.** | ✅ selection sheet |
| Supply-air temperature | **21 °C** (ΔT = 15 K) | ✅ selection sheet |
| Airflow / face velocity | **11,200 m³/h** / 2.7 m/s | ✅ selection sheet |
| Water inlet / outlet | **10.0 / 16.0 °C chilled water** | ✅ selection sheet |
| Water flow | **8.2 m³/h** | ✅ selection sheet |
| Fluid | **Pure water, 0% glycol** | ✅ selection sheet |
| Total water-side pressure drop | **52 kPa** (coil 12 + DN32 two-way valve 26 + pipework 14) | ✅ selection sheet |
| Fans | 3 × VBS0355STRHZ · 4.5 kW nominal each · 2,393 rpm operating · 320 Pa total air-side drop | ✅ selection sheet |
| Total input / EER | **2.6 kW** / **21.04 kW/kW** | ✅ selection sheet |
| Sound power / sound pressure (2 m free field) | 87.8 / 67.6 dB(A) | ✅ selection sheet |
| Dimensions (H × W × D) / weight | **2,000 × 600 × 1,375 mm** (1,950 mm cabinet + adjustable feet) / **254 kg** dry | ✅ selection sheet + drawing |
| Electrical supply | **400 V / 50 Hz / 3Ph / N / PE** — free of the 60 Hz / missing-CE blocker seen on [[PRD-STULZ-CeilAir]] | ✅ selection sheet |
| Water connections | 1 inlet + 1 outlet, **1.5" male thread**, lower side of the unit (centres 608 / 763 mm above the base) | ✅ vendor drawing |
| Altitude basis | 0 m — any non-zero altitude requires re-selection | ✅ selection sheet |
| **Unit count and redundancy model (N+1 / 2N)** | ⏳ **#unconfirmed** — waiting on ATS / Cooling Engineer to lock the L1800C45 in-row CW total heat load before quantities can be set ([[PRD-STULZ-CRS560CW]] Q1, P0), expected TBD | ⏳ |
| Capacity decay curve under ±2 °C chilled-water drift | ⏳ **#unconfirmed** — waiting on STULZ to supply it ([[PRD-STULZ-CRS560CW]] Q2), expected TBD | ⏳ |
| Whether the integrated humidifier is fitted / water and drain requirements | ⏳ **#unconfirmed** — waiting on STULZ to confirm ([[PRD-STULZ-CRS560CW]] Q3), expected TBD | ⏳ |
| Change list of the "non-standard variant" against the catalogue unit | ⏳ **#unconfirmed** — waiting on a written statement from STULZ ([[PRD-STULZ-CRS560CW]] Q7), expected TBD | ⏳ |

^sec-5-crah

### 5.4 Outdoor side and system level

| Item | Parameter | Confidence |
|---|---|---|
| Loop A outdoor heat-rejection form | Dry-cooler-led (36/46 °C warm water gives long free-cooling hours), with mechanical topping at peak-climate sites | 🔶 derived — an engineering judgement drawn from the FWS 36/46 °C warm-water level; design value, subject to final selection |
| Loop B outdoor heat-rejection form | Chiller plant (10/16 °C chilled water) | 🔶 derived — an engineering judgement drawn from the in-row CW 10/16 °C level; design value, subject to final selection |
| Total outdoor heat-rejection baseline | ⏳ **#unconfirmed** — waiting on the Cooling Engineer for the dual-loop outdoor heat balance (it must yield two separate figures, one per loop), expected TBD | ⏳ |
| PUE | **`1.0x`** — no fixed value, no range, no "typical value". Computed per site with the TCO / Designer at <https://mdcx.org>. Qualitatively: climates where dry coolers reject heat year-round sit at the low end, hotter sites need a hybrid chiller and PUE moves up — **but no number is given** | ✅ adjudicated |
| Control strategy and GPU interlocks | ⏳ **#unconfirmed** — waiting on L1800C45 `DESIGN/` for the control strategy (flow floors, GPU throttle thresholds, dual-loop failure transfer), expected TBD | ⏳ |
| CDU / 列间空调 control point lists | ⏳ **#unconfirmed** — waiting on STULZ for Modbus / BACnet point lists and the CIOS telemetry integration ([[PRD-STULZ-SCR14103W]] Q6 · [[PRD-STULZ-CRS560CW]] Q5), expected TBD | ⏳ |

> **Do not cite L1240C45's "outdoor heat-rejection baseline ≥ 1700 kW".** That figure is the sum for 1240 kW IT on a single-loop PG25 system plus nine ceiling DX compressors' input. Load composition, temperature levels and terminal types all differ here.

---

## 6. Power Distribution ^sec-6-power

### 6.1 Power boundary: the UPS is outside — that is a configuration, not a downgrade

**In the site's own words: *"that's a configuration, not a downgrade."***

On L1800C45 the UPS, batteries and PDC sit **outside the container and are provided by the site**. Nothing has been removed; a boundary has been deliberately chosen, and it points at a very specific buyer: **a site that already has an electrical room, or is willing to build one.**

Moving the UPS out buys back three things:

1. **All of the interior goes to compute.** No electrical bay is carved out of the 45ft shell, so the same footprint holds 1800 kW of IT rather than 1240 kW — this is exactly how "out of floor, not power" from §2 gets implemented.
2. **Backup time stops being capped by the shell.** With the UPS inside, battery capacity is limited by the electrical bay's volume (~8 min on L1240C45). Outside, the site sets backup time against its own availability target — five minutes, or fifteen minutes paired with gensets.
3. **The electrical side can be expanded and maintained independently.** Decoupling the electrical room from the compute container means UPS expansion, battery replacement and PDC rework never touch the container.

> **Talk-track note:** if a customer asks "why does L1240C45 have a UPS and L1800C45 does not", the correct answer is "these two SKUs serve different site boundaries", not "L1800C45 is missing a UPS". If the customer genuinely needs the boundary outside but does not want to build electrical infrastructure, MDCX's **standalone power module (UPS / battery / PDC) is in development** — all three liquid-cooling product pages on the site disclose this roadmap item, so it may be raised openly, but it **must not be committed as deliverable**.

### 6.2 Distribution parameters

| Item | Parameter | Confidence |
|---|---|---|
| UPS boundary | **Outside the container** — UPS / batteries / PDC supplied by the site | ✅ site |
| UPS model / battery autonomy | **Not applicable** (outside this SKU's delivery scope) | ✅ site |
| Supply voltages | **380 / 400 / 415 / 480 V AC** | ✅ site |
| 800 V HVDC | **Roadmap Q3 2026, not shipping today** — disclosable, not committable | ✅ site |
| In-container busbar | ⏳ **#unconfirmed** — waiting on the Power Engineer to select the in-container busbar (its rating depends on the site PDC feeder size and the rack count, neither of which is locked), expected TBD | ⏳ |
| Per-rack distribution (TOU / MCB ratings) | ⏳ **#unconfirmed** — waiting on the Power Engineer's distribution design; rack count and actual per-rack draw are undetermined, so no ratings can be stated, expected TBD | ⏳ |
| Cooling-equipment supply | CDU 3Ph/N/PE 380 V/50 Hz (pump set 20.0 kW per unit) · 列间空调 400 V/50 Hz/3Ph/N/PE (2.6 kW per unit) — **quantities undetermined, totals undetermined** | ✅ per-unit / ⏳ totals |
| Power factor | ⏳ **#unconfirmed** — waiting on the Power Engineer (the UPS is off-container, so the value follows the site's UPS model), expected TBD | ⏳ |

> **Do not borrow any of L1240C45's SIEMENS 2500A busbar, EATON 9395XR-1500 UPS or 3 × 93LiG2 batteries.** Those are selections inside a "UPS in the container" architecture and are incompatible with this SKU's power boundary.

---

## 7. Structural Specifications ^sec-7-structural

| Item | Parameter | Confidence |
|---|---|---|
| Container type | **45ft High Cube** | ✅ site |
| Exterior dimensions (L × W × H) | **13,716 × 2,438 × 2,992 mm** | 🔶 **derived** — same 45ft High Cube shell as L1240C45, taken from the ISO standard envelope. **Design value, subject to final drawings** |
| Upper module height | Raised from 600 mm to **900 mm** (primary-side interconnect headers pulled inboard) | ✅ KB ([[KB/LIQUID/L1800C45/index|L1800C45 index]]) |
| Interior clear height / usable width | ⏳ **#unconfirmed** — waiting on the L1800C45 `Layout/` three-view set, expected TBD | ⏳ |
| Empty weight | ⏳ **#unconfirmed** — waiting on the L1800C45 `DESIGN/` structural load calculation and the factory weigh-out, expected TBD | ⏳ |
| Loaded weight (with IT) | ⏳ **#unconfirmed** — waiting on the L1800C45 `DESIGN/` structural load calculation and the factory weigh-out, expected TBD | ⏳ |
| Enclosure rating | ⏳ **#unconfirmed** — waiting on the L1800C45 `DESIGN/` compliance checklist, expected TBD | ⏳ |

> **Do not borrow L1240C45's "~16 T empty / ~20–25 T loaded".** This SKU has no UPS and no batteries (lighter) but adds a CDU (1,175 kg operating per unit), 列间空调s (254 kg per unit) and two independent pipework systems (heavier). The net direction has not been computed and cannot be assumed.
>
> **Known fixed load items** (usable as inputs to a floor-loading check, not as a container weight): CDU operating weight **1,175 kg per unit** (✅), 列间空调 dry weight **254 kg per unit** (✅). Quantities undetermined.

---

## 8. Network & Cable Management ^sec-8-network

| Item | Parameter | Confidence |
|---|---|---|
| Cable penetration (top / bottom entry) | ⏳ **#unconfirmed** — waiting on the Layout Planner for the L1800C45 penetration and tray design, expected TBD | ⏳ |
| Cable tray position | ⏳ **#unconfirmed** — waiting on the Layout Planner for the L1800C45 penetration and tray design, expected TBD | ⏳ |
| Fibre / network entry position | ⏳ **#unconfirmed** — waiting on the Layout Planner for the L1800C45 penetration and tray design, expected TBD | ⏳ |

> NVLink and InfiniBand cable density on GB300 NVL72 / B300 HGX is materially higher than on PCIe machines; the penetration and tray design cannot be carried over from L1240C45.

---

## 9. Environmental & Compliance ^sec-9-environment

| Item | Parameter | Confidence |
|---|---|---|
| Operating temperature range | ⏳ **#unconfirmed** — waiting on the L1800C45 `DESIGN/` compliance checklist, expected TBD | ⏳ |
| Operating humidity range | ⏳ **#unconfirmed** — waiting on the L1800C45 `DESIGN/` compliance checklist, expected TBD | ⏳ |
| Operating altitude | ⏳ **#unconfirmed** — waiting on `DESIGN/`; note the in-row CW selection basis is **0 m altitude** and any non-zero site requires STULZ to re-run the selection ([[PRD-STULZ-CRS560CW]] §2.1 · Q6), expected TBD | ⏳ |
| Whole-unit certification path (UL / CE / TUV) | ⏳ **#unconfirmed** — waiting on the Compliance Officer for the L1800C45 whole-unit certification path, expected TBD | ⏳ |
| CDU component certification (CE / UL / CCC and certificate numbers) | ⏳ **#unconfirmed** — waiting on STULZ to supply them ([[PRD-STULZ-SCR14103W]] Q4, P0), expected TBD | ⏳ |
| 列间空调 component certification (CE / UL / CCC and certificate numbers) | ⏳ **#unconfirmed** — waiting on STULZ to supply them ([[PRD-STULZ-CRS560CW]] Q4, P0), expected TBD | ⏳ |

> ⚠️ **Certification does not transfer by analogy.** [[PRD-STULZ-CeilAir]] is the precedent for "same vendor, CE absent"; certificate numbers must be obtained model by model. The CRS 560 CW's 400 V / 50 Hz supply is free of CeilAir's market-access blocker, but **that is not the same as holding CE**.

---

## 10. Monitoring & Management System ^sec-10-monitoring

| Item | Parameter | Confidence |
|---|---|---|
| **CIOS** | Included with every MDCX. Path-addressed telemetry, alarm-to-ticket, operations workflows, usage metering | ✅ site |
| CIOS open-source core | Apache-2.0 — **roadmap**; disclosable, not committable as delivered capability | ✅ site |
| Digital twin | **NVIDIA Omniverse**, live state projected onto the 3D model | ✅ site |
| DCM (compute marketplace) | **Roadmap · MVP in development** — **must not be committed to customers as a delivered capability** | ✅ site |
| CDU / 列间空调 telemetry points and integration | ⏳ **#unconfirmed** — waiting on STULZ for Modbus / BACnet point lists ([[PRD-STULZ-SCR14103W]] Q6 · [[PRD-STULZ-CRS560CW]] Q5), expected TBD | ⏳ |
| BMS integration protocol | ⏳ **#unconfirmed** — waiting on L1800C45 `DESIGN/` for the monitoring architecture, expected TBD | ⏳ |

---

## 11. Fire Protection & Safety ^sec-11-fire

| Item | Parameter | Confidence |
|---|---|---|
| Extinguishing agent | ⏳ **#unconfirmed** — waiting on the L1800C45 `DESIGN/` fire-protection design, expected TBD | ⏳ |
| Detection system | ⏳ **#unconfirmed** — waiting on the L1800C45 `DESIGN/` fire-protection design, expected TBD | ⏳ |
| Fire panel / manual pull station / horn-strobe | ⏳ **#unconfirmed** — waiting on the L1800C45 `DESIGN/` fire-protection design, expected TBD | ⏳ |
| Access control | ⏳ **#unconfirmed** — waiting on the L1800C45 `DESIGN/` fire-protection design, expected TBD | ⏳ |
| Leak detection and response (dual loop) | ⏳ **#unconfirmed** — waiting on `DESIGN/`; leak zoning and interlock logic across two independent pipework systems must be defined separately, expected TBD | ⏳ |

---

## 12. Service & Support ^sec-12-service

### 12.1 Standard answer to a price enquiry

> **The configuration is produced by the MDCX engineering team; pricing is calculated by the commercial team. Please contact your account manager for a formal quotation.**
> （配置方案由 MDCX 工程团队提供，价格由商务团队核算，请联系客户经理获取正式报价。）

This document, and every KB product document, **contains no price information** ([[CLAUDE.md]] Hard Rule 1).

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

> Payment terms and lead-time detail are read from the commercial templates per [[CLAUDE.md]] §5 and are **not inlined in the KB**.

---

## 13. Site & Installation Requirements ^sec-13-site

| Item | Requirement | Confidence |
|---|---|---|
| **Electrical infrastructure the site must provide** | **UPS / batteries / PDC supplied by the site** (see §6.1 — this is the SKU's boundary definition) | ✅ site |
| Cooling interfaces the site must provide | Two independent services: **Loop A warm water (36/46 °C class)** plus **Loop B chilled water (10/16 °C)**. They cannot be combined | ✅ derived from the approved selection duty points |
| CDU connection type | 4 × DN100 **Tri-Clamp** (DIN 32676-B), **top exit** — site pipework must be matched with sanitary clamps, not flanges | ✅ vendor drawing |
| 列间空调 connection type | 1 inlet + 1 outlet, **1.5" male thread** | ✅ vendor drawing |
| Freight & customs | Buyer's responsibility; **no duration is committed** | ✅ adjudicated |
| On-site installation & commissioning | **Not committed** | ✅ adjudicated |
| Ground load capacity | ⏳ **#unconfirmed** — depends on the loaded weight (see §7, undetermined); waiting on the structural load calculation, expected TBD | ⏳ |
| Ground levelness | ⏳ **#unconfirmed** — waiting on L1800C45 `DESIGN/`, expected TBD | ⏳ |
| Maintenance clearances | ⏳ **#unconfirmed** — waiting on the Layout Planner; note that the top-exit CDU connection scheme has not yet been reconciled with the 900 mm upper-module lift ([[PRD-STULZ-SCR14103W]] Q5), expected TBD | ⏳ |
| Site climate suitability | ⏳ **#unconfirmed** — both primary and secondary sides run **pure water with no antifreeze**, so cold-site boundaries cannot be set until the freeze-protection strategy exists ([[PRD-STULZ-SCR14103W]] Q3, P0), expected TBD | ⏳ |
| Noise boundary | 列间空调 sound power 87.8 dB(A) / 67.6 dB(A) at 2 m per unit; **multi-unit superposition and shell attenuation pending a Layout review** | ✅ per-unit / ⏳ combined |

---

## 14. Key Specifications Summary ^sec-14-summary

| Item | Parameter | Confidence |
|---|---|---|
| Full SKU ID | `L1800C45DR220` | ✅ site |
| Status | `shipped` (D-19 gate · 2026-08-27) | ✅ site |
| Container type | 45ft High Cube | ✅ site |
| Exterior dimensions | 13,716 × 2,438 × 2,992 mm | 🔶 derived (design value) |
| **IT capacity** | **1800 kW** | ✅ site |
| Total Facility Load | Varies with PUE — **computed per site at <https://mdcx.org>** | ✅ adjudicated |
| Maximum rack density | **220 kW** (`R220`) | ✅ site |
| Rack count and composition | **8× 220 kW liquid-cooled + 1× 40 kW air-cooled = 9 racks** | ✅ site Designer profile `l1800.json` |
| GPU platforms | GB300 NVL72 · B300 HGX (SXM / NVLink) | ✅ site |
| Loops | **Dual loop (`D`)** | ✅ site |
| Loop A (GPU side) | **GPU cold-plate inlet 36–40 °C**; outdoor-plant supply 32–36 °C; CDU approach +4 °C. The approved CDU duty point FWS 36/46 · TCS 40/50 °C is the hot-end design point | ✅ adjudicated / selection sheet |
| Loop B (in-row CW side) | **10 / 16 °C chilled water** | ✅ site |
| Secondary fluid | **Pure water, 0% glycol** | ✅ selection sheet |
| **CDU** | **STULZ SCR 14103 W** · 1200 kW per unit · 103.8 m³/h · Tri-Clamp DN100 top exit · 20.0 kW pump set | ✅ ATS approved |
| **列间空调** | **STULZ CRS 560 CW** · 57.3 kW per unit (net 54.7) · 11,200 m³/h · 8.2 m³/h · 52 kPa · 400 V/50 Hz | ✅ ATS approved |
| CDU / 列间空调 quantities and redundancy | ⏳ **#unconfirmed** — waiting on ATS / Cooling Engineer calculations (Q1 in both PRDs, both P0), expected TBD | ⏳ |
| Outdoor heat-rejection baseline | ⏳ **#unconfirmed** — waiting on the Cooling Engineer's dual-loop heat balance, expected TBD | ⏳ |
| PUE | **`1.0x`** — computed per site with the TCO / Designer at <https://mdcx.org>; no fixed value and no range | ✅ adjudicated |
| **UPS boundary** | **Outside the container** (UPS / batteries / PDC supplied by the site) — **a configuration, not a downgrade** | ✅ site |
| Supply voltages | 380 / 400 / 415 / 480 V AC (800 V HVDC is roadmap Q3 2026, not shipping today) | ✅ site |
| In-container busbar | ⏳ **#unconfirmed** — waiting on the Power Engineer's selection, expected TBD | ⏳ |
| Empty / loaded weight | ⏳ **#unconfirmed** — waiting on the structural load calculation and factory weigh-out, expected TBD | ⏳ |
| Environment (temp / humidity / altitude) | ⏳ **#unconfirmed** — waiting on the `DESIGN/` compliance checklist, expected TBD | ⏳ |
| Certification | ⏳ **#unconfirmed** — waiting on the Compliance Officer for the whole unit and on STULZ for component certificate numbers, expected TBD | ⏳ |
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
| v1.2 | 2026-08-30 | Absorbed the site audit: rack build fixed at 8× 220 kW liquid + 1× 40 kW air = 9 racks, CDU at 2× SCR 14103 W, 列间空调 at 4× CRS 560 CW (site `l1800.json`). Unit counts move from ⏳ to ✅; redundancy models remain ⏳ |
| v1.1 | 2026-08-30 | **Yuri's four rulings of 2026-08-30 propagated ([[PRODUCT_SPEC_BASELINE]] v2.0).** (1) **The dual-loop GPU-side temperature chain is fixed**: outdoor-plant supply 32–36 °C → CDU approach +4 °C → GPU cold-plate inlet **36–40 °C**; the former "GPU 36–45 °C" ceiling of 45 becomes 40 (§2 / §5.1 / §14), with a note that the approved STULZ SCR 14103 W selection sheet (FWS 36/46 · TCS 40/50) is the **hot-end design point** of that chain and is consistent with the ruling; the former ⛔ becomes ✅ adjudicated. (2) **PUE is written `1.0x` everywhere** and Total Facility Load becomes "varies with PUE, computed per site with the TCO / Designer at <https://mdcx.org>" (§3.1 / §5.4 / §14); the former ⏳ becomes ✅, and the §3 IT Load vs Total Facility Load distinction is retained as a hard rule. (3) **Lead time is unified to 120 days EXW for the first batch and 90 days EXW for Scale, counted from order placement**, with a new dummy-load burn-in period of 5–30 days (Supermicro recommendation, outside the EXW commitment); the commercial, freight and installation segments carry no commitment. The §12.2 ⛔ two-basis table and "~185–230 days", and the four-phase cycle and "3–4 weeks on-site installation & commissioning" rows in §12.3 and §13, are **deleted**. (4) **Warranty is unified to core components for one year from EXW plus an annual service fee thereafter**, with ONSITE / NBD / 9×5 / 24×7 response levels governed by the Invoice (§12.3 / §14). |
| v1.0 | 2026-08-30 | First release. L1800C45 English Tech Spec built on the 14-section structure of [[L1240C45_Tech_Spec_EN]], as a single file preserving anchors `^sec-1-layout` … `^sec-14-summary`. All figures sourced from [[PRODUCT_SPEC_BASELINE]]; cooling equipment parameters mirrored from the ATS-approved [[PRD-STULZ-SCR14103W]] and [[PRD-STULZ-CRS560CW]]. Structural / environmental / network / fire / service fields marked ⏳ line by line per [[UNCONFIRMED_Convention]], each naming who is waited on, for what, and by when; §12 records the ⛔ lead-time basis conflict as it stands; §6.1 states positively that an external UPS is a configuration, not a downgrade; §3.1 explicitly separates IT Load from Total Facility Load. **No figure was borrowed from L1240C45.** Section numbering, anchors and table row counts match [[L1800C45_Tech_Spec_CN]] one-for-one. |
