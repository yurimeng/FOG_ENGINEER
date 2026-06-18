---
title: "R-3/R-4 工程红旗与负荷定义风险"
parent: "[[Risk_Guideline]]"
order: 2
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/risk
  - #risk
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/Risk_Guideline.md"
source_anchors:
  - "R-3 工程红旗"
  - "R-4 负荷定义风险"
---

## R-3 工程红旗 / Engineering Red Flags

> **The following conditions MUST trigger engineering warnings regardless of other analysis results.**

| Red Flag | Risk Type | Required Action |
|---|---|---|
| Unmitigated single point failures | Critical | Immediate escalation to ATS; blocks approval |
| Systems requiring highly specialized maintenance | High | Flag and recommend alternatives; escalate if no resolution |
| Infrastructure incompatible with deployment environment | High | Flag environmental mismatch; escalate to ATS |
| Architectures that limit future expansion | Medium-High | Document limitation; recommend expansion-capable alternative |
| Load definition unclear (IT load vs total facility load) | High | **Must flag if ambiguous** — incorrect load definition causes cascading design errors |
| No failover path for cooling in BESS deployments | Critical | Immediate escalation required |

> 工程红旗与合规风险的交叉点见 [[Compliance_Guideline#§C-6 合规风险识别]]。
> 上报触发条件汇总见 [[PRINCIPLE_Guideline#§1.6 上报原则 / Escalation Principle]]。

---

## R-4 负荷定义风险 / Load Definition Risk

> **CRITICAL WARNING**: Confusion between IT load and total facility load is a common source of design errors.

| Term | Definition | Risk if Confused |
|---|---|---|
| **IT Load** | Power consumed by compute equipment only | Cooling and power sized 2–4x too large if total load used |
| **Total Facility Load** | IT Load + Cooling + Lighting + Infrastructure overhead | Sizing errors, budget overruns, thermal imbalance |

Risk Auditor must **flag any unclear load definitions** before proceeding with analysis. Misaligned load definitions are a mandatory escalation item.

> 强制澄清规则见 [[PRINCIPLE_Guideline#§1.3 IT Load vs Total Facility Load 强制澄清 / Load Disambiguation]]。
> 详细定义与典型混淆场景见 [[POWER_SYSTEMS_Guideline#§P-1 IT 负载定义]] 与 [[POWER_SYSTEMS_Guideline#§P-4 典型混淆场景]]。
