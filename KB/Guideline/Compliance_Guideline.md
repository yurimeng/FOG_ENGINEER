---
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/compliance
---

# Compliance Guideline / 合规技术指南

Document Version / 文档版本: v1.0
Last Updated / 最后更新: 2026-03-10
Source / 来源: `Works_Public/AGENTS/Compliance Officer.md`

---

## Applicable Scope / 适用范围

Compliance Officer evaluates compliance across the following domains:

| Domain / 领域 | Content / 内容 |
|---|---|
| Electrical safety / 电气安全 | UL, CSA, IEC, local codes |
| Cooling system safety / 冷却系统安全 | Thermal management, equipment safety |
| BESS / Energy storage / 储能系统 | Battery safety, thermal management, electrical isolation, fire suppression |
| Container datacenter / 容器数据中心 | Structural integrity, electrical integration, emergency access |
| Fire protection / 消防系统 | NFPA standards, fire suppression integration |
| Operational safety / 运维安全 | Safety procedures, certification requirements |

---

## Key Standards / 关键标准

Compliance Officer must be aware of and reference the following major industry standards:

### Electrical Safety / 电气安全

- **UL Standards** — Underwriters Laboratories safety requirements
- **CSA Standards** — Canadian Standards Association requirements
- **IEC Standards** — International Electrotechnical Commission standards
- **Local electrical codes** — Regional jurisdictional requirements

### Fire Protection / 消防

- **NFPA Fire Protection Standards** — National Fire Protection Association codes
  - NFPA 855 (Standard for the Installation of Stationary Energy Storage Systems)
  - Applicable fire suppression requirements for BESS and datacenter environments

---

## BESS / Energy Storage Compliance / 储能系统合规

Energy storage systems such as BESS require compliance evaluation including:

- **Battery safety standards** — Cell-level and pack-level certification
- **Thermal management safety** — Temperature control limits, thermal runaway prevention
- **Electrical isolation** — High-voltage isolation, grounding, and bonding requirements
- **Fire suppression integration** — Suppression systems compatible with battery chemistry
- **UL 9540** — Standard for Energy Storage Systems and Equipment
- **UL 9540A** — Test Method for Evaluating Thermal Runaway Fire Propagation in Battery Energy Storage Systems

> **Critical**: BESS thermal runaway risk must be addressed with proper suppression and monitoring before deployment.

---

## Datacenter Compliance / 数据中心合规

For datacenter infrastructure, compliance checks include:

| Area / 领域 | Key Requirements / 主要要求 |
|---|---|
| Power system safety / 电力系统安全 | UPS, PDU, and generator compliance |
| Cooling system safety / 冷却系统安全 | Chiller, CRAC/CRAH, pump safety |
| Battery system regulations / 储能系统规范 | BESS integration with facility power |
| Container datacenter requirements / 容器数据中心要求 | Prefabricated modular infrastructure |
| Operational safety / 运维安全 | Lockout/tagout, arc flash, PPE |

---

## Container Datacenter Compliance / 容器数据中心合规

Containerized infrastructure must be evaluated for:

- **Structural integrity** — Wind load, seismic, transportation structural requirements
- **Electrical integration** — Busbar, cable routing, grounding within confined space
- **Cooling system safety** — Indoor/outdoor operation, humidity control
- **Emergency access and maintenance** — Egress pathways, maintenance clearance, fire exit requirements
- **Environmental ratings** — NEMA/IP ratings for enclosure protection

---

## Compliance Risk Detection / 合规风险识别

Compliance Officer must flag the following risk conditions:

- Uncertified equipment in critical infrastructure
- Electrical design conflicts with local codes
- Insufficient safety isolation (HV/LV boundaries)
- Cooling systems introducing safety hazards (flood risk, condensation, refrigerant leaks)
- BESS thermal runaway propagation potential
- Missing or inadequate fire suppression coverage
- Non-compliant cable management and tray routing

---

## Certification Requirements Summary / 认证要求汇总

| System / 系统 | Required Certifications / 必需认证 |
|---|---|
| Electrical equipment / 电气设备 | UL, CSA, or IEC certification; CE marking where applicable |
| BESS / 储能系统 | UL 9540, UL 9540A; local utility interconnection approval |
| Fire suppression / 消防系统 | NFPA compliance; local fire marshal approval |
| Datacenter / 数据中心 | TIA-942 tier level requirements; local building codes |
| Container infrastructure / 容器设施 | Structural certification; transportation permits if mobile |

---

## Workflow Integration / 工作流集成

Compliance Officer workflow:

1. **Read this Guideline first** — Reference applicable standards before analysis
2. **Perform technical analysis** — Evaluate project requirements against standards in this document
3. **Output to ATS** — Pass compliance results (PASS / CONDITIONAL PASS / FAIL) to ATS for integration
4. **Flag conflicts** — If project requirements conflict with this Guideline, escalate to ATS before proceeding

> **Authority**: This Guideline is the authoritative reference for compliance domain decisions. Do not override these standards without ATS escalation.
