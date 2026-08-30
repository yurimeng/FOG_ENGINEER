---
title: "L1240C45 Section 12: Service & Support"
parent: "[[L1240C45_Tech_Spec_EN]]"
order: 12
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/l1240c45"
  - "#thermal"
  - "#MDC"
created: 2026-06-18
source_file: "PUBLIC/Tech_Spec/L1240C45_Tech_Spec_EN.md"
source_anchors:
  - "^sec-12-service"
---

## 12. Service & Support ^sec-12-service

> ✅ **Adjudicated by Yuri on 2026-08-30 (C-8 lead time / C-9 warranty closed).** Lead time commits to EXW only; the warranty covers core components for one year. The previous bases (~185–230 days including logistics, the four-phase deployment SOP table, 9×5 NBD) **have been deleted and are no longer quoted.** See [[PRODUCT_SPEC_BASELINE]] §3.1 and §3.3.

### 12.1 Lead time — EXW is the only commitment

| Item | Value | Nature of commitment |
|------|-------|------|
| **First-batch lead time** | **120 days EXW from order placement** | ✅ **Committed** |
| **Scale (expansion batch) lead time** | **90 days EXW** | ✅ **Committed** |
| **Dummy-load burn-in period** | **5–30 days** — prove out the power and cooling chain on a dummy load before real GPUs go in. Source: **Supermicro recommendation** | ⚠️ **Not covered by the EXW commitment** |
| Commercial cycle (contract / payment / procurement) | **Not committed** | ❌ no commitment |
| Freight and customs | **Not committed**; buyer's responsibility | ❌ no commitment |
| On-site installation and commissioning | **Not committed** | ❌ no commitment |

> **Lead-time wording rule:** the only committable figure is the EXW day count (120 days first batch / 90 days Scale, both counted from order placement). The commercial, freight and installation segments carry no commitment — no day counts, no ranges, no estimates; escalate customer follow-ups to the commercial team per [[CLAUDE.md]] §5.

### 12.2 Warranty and support

| Item | Parameter |
|------|-----------|
| Warranty scope and term | **Core components, one year from EXW** |
| Subsequent years | **Annual service fee** |
| Support SLA (ONSITE / NBD / 9×5 / 24×7 etc.) | **Governed by the Invoice** — the KB and Tech Specs neither commit to nor define it |
| On-site commissioning | Scope per contract |

---
