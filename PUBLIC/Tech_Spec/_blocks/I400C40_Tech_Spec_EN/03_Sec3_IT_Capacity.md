---
title: "I400C40 Section 3: IT Capacity"
parent: "[[I400C40_Tech_Spec_EN]]"
order: 3
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/i400c40"
  - "#MDC"
created: 2026-07-28
source_file: "PUBLIC/Tech_Spec/I400C40_Tech_Spec_EN.md"
source_anchors:
  - "^sec-3-it-capacity"
---

## 3. IT Capacity ^sec-3-it-capacity

| Item | Spec |
|------|------|
| **IT capacity (recommended)** | **360kW** (8 × I50TS × 45kW) ^mdc-096c6adecc |
| **IT capacity (maximum)** | **400kW** (8 × I50TS × 50kW) ^mdc-7c71253e51 |
| Immersion tanks | 8 × I50TS (45kW rec. / 50kW max, 2N CDU thermal redundancy) ^mdc-ef44f696eb |
| Air-cooled rack | 1 × **10kW** (independent air path) |
| Rack space | **256RU / 232OU** (8 × 32RU) ⏳ **#unconfirmed** — taken from the legacy AC40 V1.4 baseline; not covered by [[PRODUCT_SPEC_BASELINE]]. Waiting on I400C40 DESIGN/ engineering documents (shop drawings / weighing report / structural calculation) to be issued and written back to the baseline table — expected TBD ^mdc-1ffaf297d2 |
| Secondary oil in/out | **Inlet ≤35°C / outlet ≈43°C, ΔT=8K** |
| Facility water in/out | **≤32 / 37°C (ΔT=5K)** ⛔ **conflict** — [[PRODUCT_SPEC_BASELINE]] §2.2 carries site evidence for I400C45 only; the same temperatures for I400C40 are derived. Waiting on Cooling Engineer to confirm whether I400C40 runs the same water temperatures and to write it back to the baseline table — expected TBD ^mdc-401ba944f4 |
| Design wet-bulb | **28°C** ⏳ **#unconfirmed** — taken from the legacy AC40 V1.4 baseline; not covered by [[PRODUCT_SPEC_BASELINE]]. Waiting on I400C40 DESIGN/ engineering documents (shop drawings / weighing report / structural calculation) to be issued and written back to the baseline table — expected TBD ^mdc-55b15e5c28 |
| Power factor (UPS output) | **0.9** |

### IT Load vs Total Facility Load

| Item | Value | Notes |
|------|-------|-------|
| **IT load** | 360kW rec. / 400kW max | Servers / GPUs in immersion tanks |
| **Total facility load** | Varies with PUE — **computed per site at <https://mdcx.org>** | ✅ adjudicated 2026-08-30 (C-2 closed). The former "~400–480kW" range is void |
| **PUE** | **`1.0x`** | ✅ adjudicated 2026-08-30. **No fixed value, no range, no "typical value"** — computed per site at <https://mdcx.org> (TCO / Designer). The former "~1.05–1.10 / ~1.15–1.20" figures are void |

> **IT Load ≠ Total Facility Load.** Clarify customer "400kW" claims. External UPS losses and battery HVAC are **outside** the I400C40 box but must be in site capacity. **This distinction is a hard rule ([[CLAUDE.md]] Hard Rule 5) and is retained; the facility-load figure itself is not given.** ^mdc-f7eb75ab1e
>
> Qualitatively: climates where dry coolers reject heat year-round sit at the low end; hotter sites need a hybrid chiller and PUE moves up. **No numbers are given.** See [[PRODUCT_SPEC_BASELINE#^baseline-pue]].

### Relationship to electrical load schedule

In-container 415VAC schedule is in §6 (source: I400C40 workload sheet). IT-PDC1 / IT-PDC2 are each ~381kW — that is **A/B dual-feed capability** (two PDUs per tank), **not** simultaneous 762kW IT real power. Concurrent IT remains **360–400kW**. ^mdc-cddd196253

---

## Changelog

| 日期 | 变更 |
|---|---|
| 2026-09-20 | 🧭 unconfirmed-064 改为 ⛔ conflict，未裁定赢家 |
