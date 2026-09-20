---
title: "I400C40 Section 14: Key Specs Summary"
parent: "[[I400C40_Tech_Spec_EN]]"
order: 14
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/i400c40"
  - "#MDC"
created: 2026-07-28
source_file: "PUBLIC/Tech_Spec/I400C40_Tech_Spec_EN.md"
source_anchors:
  - "^sec-14-summary"
---

## 14. I400C40 Key Specifications Summary ^sec-14-summary

| Item | Spec |
|------|------|
| Container | **40ft HC** (~12,192 × 2,438 × 2,896 mm) ⏳ **#unconfirmed** (legacy AC40 V1.4, not covered by the baseline table; waiting on I400C40 DESIGN/ documents, expected TBD) ^mdc-a598989e46 |
| IT capacity | **360kW rec. / 400kW max** (8×I50TS @ 45/50kW) ^mdc-691824e421 |
| Air rack | 1 × 10kW |
| Rack space | 256RU / 232OU ⏳ **#unconfirmed** (legacy AC40 V1.4, not covered by the baseline table; waiting on I400C40 DESIGN/ documents, expected TBD) ^mdc-abbb3a8a72 |
| Cooling | **Single-phase immersion** + Dual CDU 1+1 + independent air |
| Secondary | Inlet ≤35°C / outlet ≈43°C / **ΔT=8K**; DC20 / S5LV |
| Primary | ≤32 / 37°C (ΔT=5K) ⛔ **conflict** (see §5.2; waiting on Cooling Engineer to confirm same temperatures, expected TBD); design WB 28°C ⛔ **conflict** **** (legacy AC40 V1.4, not covered by the baseline table; waiting on I400C40 DESIGN/ documents, expected TBD) ^mdc-5d4da582b6 |
| Secondary flow (box) | ≈ **87.8 / 97.6 m³/h** (360 / 400kW) ⛔ **conflict** (legacy AC40 V1.4, not covered by the baseline table; waiting on I400C40 DESIGN/ documents, expected TBD) ^mdc-168b2323a0 |
| Heat rejection | DB **≤24°C dry cooler**; **>24°C Hybrid** |
| Facility load | Varies with PUE — **computed per site at <https://mdcx.org>** ✅ adjudicated 2026-08-30 (the former ~400–480kW is void) |
| PUE | **`1.0x`** — no fixed value, no range; computed per site with the TCO / Designer at <https://mdcx.org> ✅ adjudicated 2026-08-30 (the former 1.05–1.10 / 1.15–1.20 figures are void); see §3 |
| UPS | EATON **9395XR-600**, **external** |
| UPS battery | **2×93LiG2**, ~**10 min** |
| In-box power | Dual feed + ATS; IT-PDC×2 (A/B) + PDC1 |
| PF | 0.9 (UPS output) |
| Network | Ethernet-first; 10G→400G |
| Ambient | -45°C to +45°C (reference) |
| Fire | FM-200 + ASSD/VESDA |
| Monitoring | MODBUS / SNMP / Web / Redfish |
| Full-system UL | **No** (use I400C45) ^mdc-1d320bb857 |
| Warranty | **Core components, one year from EXW**; annual service fee thereafter. Response level (ONSITE / NBD / 9×5 / 24×7) is **governed by the Invoice** ✅ adjudicated 2026-08-30 |
| Lead time | **120 days EXW first batch / 90 days EXW for Scale**; dummy-load burn-in 5–30 days (not covered by the EXW commitment); commercial, freight and installation carry no commitment ✅ adjudicated 2026-08-30 (the former ~185–230 days is void) |
| Operating weight | ~22–30T (structural calc) ⏳ **#unconfirmed** (legacy AC40 V1.4, not covered by the baseline table; waiting on I400C40 DESIGN/ documents, expected TBD) ^mdc-7ffa230298 |

### vs L1240C45 (one glance) ^mdc-349eb2ba48

| | I400C40 | L1240C45 ^mdc-f6812c20a7 |
|--|------|------|
| Cooling | Immersion | DLC + RDHX + CeilAir |
| IT | 0.36–0.40 MW | 1.24 MW |
| UPS | External 600kW | Internal 1500kW |
| Use | Inference / edge / cost-sensitive | Large training / high density |

### Open items

1. Dielectric density / DC20 cp; secondary flow finalization  
2. Dual-feed terminology vs project SLD  
3. Exact empty/operating weights  
4. Altitude derating  
5. Oil-drain lift SOP  
6. Project fire AHJ agent selection  
7. External UPS interface drawings (customer side)

---

## Changelog

| 日期 | 变更 |
|---|---|
| 2026-09-20 | 🧭 unconfirmed-048 改为 ⛔ conflict，未裁定赢家 |
| 2026-09-20 | 🧭 unconfirmed-047 改为 ⛔ conflict，未裁定赢家 |
