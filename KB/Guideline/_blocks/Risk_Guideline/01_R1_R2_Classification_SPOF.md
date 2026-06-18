---
title: "R-1/R-2 风险分级与单点故障识别"
parent: "[[Risk_Guideline]]"
order: 1
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/risk
  - #risk
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/Risk_Guideline.md"
source_anchors:
  - "R-1 风险分级方法"
  - "R-2 单点故障识别"
---

## R-1 风险分级方法 / Risk Classification Methodology

Risk Auditor classifies identified risks into four levels:

| Level | Label | Definition |
|---|---|---|
| 🔵 Low / 低风险 | Recoverable issue with minimal impact | No impact on system reliability; addressable in normal maintenance cycles |
| 🟡 Medium / 中风险 | Significant issue requiring attention | Affects maintainability or efficiency; should be resolved before deployment |
| 🟠 High / 高风险 | Serious reliability or safety concern | May cause system failure or unsafe conditions; must be resolved before approval |
| 🔴 Critical / 严重风险 | Unacceptable — blocks deployment | Single point of failure or life-safety risk; immediate escalation to ATS required |

> **Critical risks must be escalated to ATS immediately. Do not proceed with analysis until Critical risks are acknowledged.**

> 上报原则与触发条件见 [[PRINCIPLE_Guideline#§1.6 上报原则 / Escalation Principle]]。当 R-1 识别为 Critical 时,直接触发 §1.6 第 5 条。

---

## R-2 单点故障识别 / Single Point of Failure Detection

Risk Auditor must actively detect potential single points of failure (SPOF) in all infrastructure domains.

### Power Systems / 电力系统

| SPOF Condition | Description |
|---|---|
| Single utility feed | No redundancy on primary power source |
| Single UPS system | No N+1 or parallel UPS configuration |
| Single PDU per rack | No redundant PDU path |
| No generator backup | Critical load without backup power |

> 电力 SPOF 的工程权衡与冗余拓扑见 [[POWER_SYSTEMS_Guideline#§P-9 冗余结构与拓扑]]。

### Cooling Systems / 冷却系统

| SPOF Condition | Description |
|---|---|
| Single chiller | No redundancy for cooling capacity |
| Single cooling loop | No secondary cooling path |
| CDU without backup | Single CDU feeding critical racks |
| No cross-connect between loops | No failover path for fluid cooling |

> 冷却 SPOF 的识别与冗余策略见 [[COOLING_SYSTEM_Guideline#§G-11 冗余策略]]。

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

> 网络 SPOF 缓解设计见 [[NETWORK_Guideline#§N-2 核心设计原则]]。
