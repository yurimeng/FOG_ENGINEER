---
title: "I400C40 Section 10: Monitoring"
parent: "[[I400C40_Tech_Spec_EN]]"
order: 10
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/i400c40"
  - "#MDC"
created: 2026-07-28
source_file: "PUBLIC/Tech_Spec/I400C40_Tech_Spec_EN.md"
source_anchors:
  - "^sec-10-monitoring"
---

## 10. Monitoring & Management ^sec-10-monitoring

| Item | Spec |
|------|------|
| Architecture | PLC / controller + open protocols |
| Protocols | **MODBUS / TCP/IP**; device **SNMP / Modbus / Redfish** |
| Remote | **SNMP / Web** |
| DCIM / BMS | MODBUS integration (project) |

### Points

Power (V/I/P, external UPS status, EPO); environment (T/RH); cooling (oil in/out, primary temps, pumps, level, conductivity, pressure); fire; access control.

Liquid level: High / Normal / Low / Low-low with escalating response.

![[I400C40_NETWORK_CONF_v1.svg]]

---
