---
title: "I400C40 Section 13: Site & Installation"
parent: "[[I400C40_Tech_Spec_EN]]"
order: 13
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/i400c40"
  - "#MDC"
created: 2026-07-28
source_file: "PUBLIC/Tech_Spec/I400C40_Tech_Spec_EN.md"
source_anchors:
  - "^sec-13-site"
---

## 13. Site & Installation Requirements ^sec-13-site

| Item | Requirement |
|------|-------------|
| Floor loading | Support **operating weight** (~22–30T class + dynamic; **structural calc rules**) ⏳ **#unconfirmed** (legacy AC40 V1.4, not covered by the baseline table; waiting on I400C40 DESIGN/ documents, expected TBD) ^mdc-a5b433c558 |
| Levelness | **±0.5°** |
| Clearances | Service, lift, piping, fire access |
| Cooling | One outdoor plant per box: dry cooler **or** Hybrid; hydraulic design required |
| Power | Dual feeds, external UPS room/container, tray/duct |
| External UPS pad | Space, cooling, aisle for 9395XR-600 + 2×93LiG2 |
| Fluid logistics | Dielectric transport, storage, fill/drain, environmental compliance |
| Roads / crane | 40ft transport envelope and lift plan |
| Permits | Planning, utility, fire, environmental — **project-specific** |

### Siting guidance

Prefer extreme DB ≤24°C for dry-cooler PUE; hot/humid sites need Hybrid + DX energy in facility load. Weak grids: BESS (hours) + UPS (minutes) layered. Long primary loops raise pump power — hydraulic study required. Reserve corridors for multi-box expansion.

### Zone boundaries

| Zone | Relation to I400C40 ^mdc-9d7375a68b |
|------|------------------|
| IT Zone | **I400C40 itself** ^mdc-cd20664941 |
| Cooling Zone | Outdoor plant 1:1 — not fully inside 40ft envelope |
| Power Zone | External UPS/batteries, BESS, genset, switchyard |

---
