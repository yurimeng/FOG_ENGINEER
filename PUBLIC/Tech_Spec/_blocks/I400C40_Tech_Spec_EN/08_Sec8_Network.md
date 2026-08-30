---
title: "I400C40 Section 8: Network"
parent: "[[I400C40_Tech_Spec_EN]]"
order: 8
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/i400c40"
  - "#MDC"
created: 2026-07-28
source_file: "PUBLIC/Tech_Spec/I400C40_Tech_Spec_EN.md"
source_anchors:
  - "^sec-8-network"
---

## 8. Network & Cable Management ^sec-8-network

| Item | Spec |
|------|------|
| Default fabric | **Ethernet** (not default InfiniBand) |
| Speeds | 10G / 25G / 100G / **400G upgrade path** |
| Protocols | IPv4/IPv6; IB optional (custom) |
| Cable entries | Top / bottom / side (per drawings) |
| Cable management | Overhead tray; power/data separation |
| OOB | BMC / IPMI / iLO / iDRAC dedicated management network |
| Active gear | Project / integrator supplied; MDC provides space + power |

![[I400C40_NETWORK_CONF_v1.svg]]

Refs: I400C40_NETWORK_CONF · NETWORK_Guideline · PRODUCTS_NETWORK

---
