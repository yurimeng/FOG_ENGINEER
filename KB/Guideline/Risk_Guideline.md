---
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/risk
---

# Risk Guideline / 风险审计技术指南

Document Version / 文档版本: v1.0
Last Updated / 最后更新: 2026-03-10
Source / 来源: `Works_Public/AGENTS/Risk Auditor.md`

---

## Risk Classification Methodology / 风险分级方法

Risk Auditor classifies identified risks into four levels:

| Level | Label | Definition |
|---|---|---|
| 🔵 Low / 低风险 | Recoverable issue with minimal impact | No impact on system reliability; addressable in normal maintenance cycles |
| 🟡 Medium / 中风险 | Significant issue requiring attention | Affects maintainability or efficiency; should be resolved before deployment |
| 🟠 High / 高风险 | Serious reliability or safety concern | May cause system failure or unsafe conditions; must be resolved before approval |
| 🔴 Critical / 严重风险 | Unacceptable — blocks deployment | Single point of failure or life-safety risk; immediate escalation to ATS required |

> **Critical risks must be escalated to ATS immediately. Do not proceed with analysis until Critical risks are acknowledged.**

---

## Single Point of Failure Detection Criteria / 单点故障识别标准

Risk Auditor must actively detect potential single points of failure (SPOF) in all infrastructure domains.

### Power Systems / 电力系统

| SPOF Condition | Description |
|---|---|
| Single utility feed | No redundancy on primary power source |
| Single UPS system | No N+1 or parallel UPS configuration |
| Single PDU per rack | No redundant PDU path |
| No generator backup | Critical load without backup power |

### Cooling Systems / 冷却系统

| SPOF Condition | Description |
|---|---|
| Single chiller | No redundancy for cooling capacity |
| Single cooling loop | No secondary cooling path |
| CDU without backup | Single CDU feeding critical racks |
| No cross-connect between loops | No failover path for fluid cooling |

### Control Systems / 控制系统

| SPOF Condition | Description |
|---|---|
| Single BMS controller | No redundant control path |
| No manual override | No local control capability if BMS fails |
| Single network path to controllers | No out-of-band management redundancy |

### Network Infrastructure / 网络基础设施

| SPOF Condition | Description |
|---|---|
| Single network switch | No redundant switching layer |
| Single ISP connection | No diverse uplink |
| No intra-DC redundancy | No alternate path between rack rows |

---

## Engineering Red Flags / 工程红旗

> **The following conditions MUST trigger engineering warnings regardless of other analysis results.**

| Red Flag | Risk Type | Required Action |
|---|---|---|
| Unmitigated single point failures | Critical | Immediate escalation to ATS; blocks approval |
| Systems requiring highly specialized maintenance | High | Flag and recommend alternatives; escalate if no resolution |
| Infrastructure incompatible with deployment environment | High | Flag environmental mismatch; escalate to ATS |
| Architectures that limit future expansion | Medium-High | Document limitation; recommend expansion-capable alternative |
| Load definition unclear (IT load vs total facility load) | High | **Must flag if ambiguous** — incorrect load definition causes cascading design errors |
| No failover path for cooling in BESS deployments | Critical | Immediate escalation required |

---

## Load Definition Risk Awareness / 负荷定义风险认知

> **CRITICAL WARNING**: Confusion between IT load and total facility load is a common source of design errors.

| Term | Definition | Risk if Confused |
|---|---|---|
| **IT Load** | Power consumed by compute equipment only | Cooling and power sized 2–4x too large if total load used |
| **Total Facility Load** | IT Load + Cooling + Lighting + Infrastructure overhead | Sizing errors, budget overruns, thermal imbalance |

Risk Auditor must **flag any unclear load definitions** before proceeding with analysis. Misaligned load definitions are a mandatory escalation item.

---

## Operational Risk Evaluation / 运维风险评估

Infrastructure solutions must remain maintainable in real-world environments.

| Evaluation Factor | What to Assess |
|---|---|
| **Maintenance complexity** | Can standard technicians maintain this? Is specialized training required? |
| **Required technician skill level** | Is on-site staff qualified for the technology? |
| **Spare part availability** | Are critical spares available within acceptable lead time? |
| **Failure isolation capability** | Can a single component failure be isolated without taking down the whole system? |

---

## Deployment Risk Assessment / 部署风险评估

Risk Auditor evaluates risks related to deployment environments:

| Environment Factor | Risk Consideration |
|---|---|
| **Remote sites** | Limited access for maintenance; spares logistics complexity |
| **Limited infrastructure availability** | Site may lack adequate power or cooling utility capacity |
| **Harsh environmental conditions** | Temperature extremes, humidity, dust; equipment must be rated accordingly |
| **Limited technical support** | Personnel on-site may not have specialized skills; favor simpler architectures |

---

## Scalability Risk Analysis / 扩展风险评估

Engineering designs must allow future system expansion.

| Scalability Risk | Detection Criteria |
|---|---|
| **Expansion limitations** | Physical space not reserved for additional racks/containers |
| **Infrastructure bottlenecks** | Cooling or power capacity at limit with current load |
| **Power scaling constraints** | No headroom in transformer or generator capacity |
| **Cooling scaling constraints** | Chiller or CDU at maximum with current configuration |

---

## Cost Risk Evaluation / 成本风险评估

Some architectures introduce hidden long-term costs. Evaluate:

- **Operational complexity risks** — Complex systems require more operator training and maintenance hours
- **Maintenance accessibility risks** — Poor layout increases mean time to repair (MTTR)
- **Infrastructure replacement risks** — Proprietary components with limited supply chains increase future replacement costs

---

## Workflow Integration / 工作流集成

Risk Auditor workflow:

1. **Read this Guideline first** — Understand risk classification and SPOF criteria before analysis
2. **Perform technical analysis** — Evaluate all risk domains per this document
3. **Output to ATS** — Pass risk assessment results to ATS for integration
4. **Flag conflicts** — If project requirements conflict with this Guideline, escalate to ATS before proceeding

> **Authority**: This Guideline defines the authoritative risk classification methodology. Do not downgrade risk levels to avoid escalation. If in doubt, escalate.
