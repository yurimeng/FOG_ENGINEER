---
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/risk
  - #MDC
---
# Risk Guideline / 风险审计技术指南

Document Version / 文档版本: v1.1
Last Updated / 最后更新: 2026-06-05
Source / 来源: `Works_Public/AGENTS/Risk Auditor.md`

---

> **速查 / Quick Reference**: 本文件定义 FOG 风险审计 (Risk Auditor) 的风险分级方法、SPOF 识别标准、工程红旗、负荷/运维/部署/扩展与成本风险评估框架,以及与 ATS 的工作流集成规则。
>
> 跨文件总入口与执行合约见 [[PRINCIPLE_Guideline]];Agent × 场景必读矩阵见 [[PRINCIPLE_Guideline#§4 Key Matrix — Agent × 场景必读表]]。

---

## 章节速查 / Section Index

| ID | 标题 | 用途 |
|----|------|------|
| [[#R-1 风险分级方法]] | 4 级风险分类与升级原则 | 评估每个发现的风险等级,确定是否需要立即上报 ATS |
| [[#R-2 单点故障识别]] | Power / Cooling / Control / Network 各域 SPOF 识别标准 | 主动检测所有基础设施域的潜在单点故障 |
| [[#R-3 工程红旗]] | 强制触发工程警告的 6 类条件 | 任何一项命中即必须升级或阻止审批 |
| [[#R-4 负荷定义风险]] | IT Load vs Total Facility Load 混淆风险 | 客户口径含混时强制澄清,避免级联设计错误 |
| [[#R-5 运维风险评估]] | 维护复杂度/技能/备件/故障隔离 | 评估方案在真实环境中的可维护性 |
| [[#R-6 部署风险评估]] | 偏远站点/基础设施受限/恶劣环境/技术支持 | 评估部署环境对架构选择的约束 |
| [[#R-7 扩展与成本风险]] | 扩展空间/基础设施瓶颈/隐藏长期成本 | 评估方案的扩展性与长期 TCO 风险 |

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

---

## R-5 运维风险评估 / Operational Risk Evaluation

Infrastructure solutions must remain maintainable in real-world environments.

| Evaluation Factor | What to Assess |
|---|---|
| **Maintenance complexity** | Can standard technicians maintain this? Is specialized training required? |
| **Required technician skill level** | Is on-site staff qualified for the technology? |
| **Spare part availability** | Are critical spares available within acceptable lead time? |
| **Failure isolation capability** | Can a single component failure be isolated without taking down the whole system? |

> 维护通道净空与可维护性对运维风险的影响见 [[Layout_Guideline#§L-2 维护通道净空]]。

---

## R-6 部署风险评估 / Deployment Risk Assessment

Risk Auditor evaluates risks related to deployment environments:

| Environment Factor | Risk Consideration |
|---|---|
| **Remote sites** | Limited access for maintenance; spares logistics complexity |
| **Limited infrastructure availability** | Site may lack adequate power or cooling utility capacity |
| **Harsh environmental conditions** | Temperature extremes, humidity, dust; equipment must be rated accordingly |
| **Limited technical support** | Personnel on-site may not have specialized skills; favor simpler architectures |

> 环境适应性与恶劣工况要求见 [[COOLING_SYSTEM_Guideline#§G-12 环境运行范围]] 与 [[Compliance_Guideline#§C-5 容器数据中心合规]]。

---

## R-7 扩展与成本风险 / Scalability & Cost Risk

Engineering designs must allow future system expansion **and** avoid hidden long-term costs. Evaluate both dimensions.

### 扩展风险 / Scalability Risks

| Scalability Risk | Detection Criteria |
|---|---|
| **Expansion limitations** | Physical space not reserved for additional racks/containers |
| **Infrastructure bottlenecks** | Cooling or power capacity at limit with current load |
| **Power scaling constraints** | No headroom in transformer or generator capacity |
| **Cooling scaling constraints** | Chiller or CDU at maximum with current configuration |

### 成本风险 / Cost Risks

Some architectures introduce hidden long-term costs. Evaluate:

- **Operational complexity risks** — Complex systems require more operator training and maintenance hours
- **Maintenance accessibility risks** — Poor layout increases mean time to repair (MTTR)
- **Infrastructure replacement risks** — Proprietary components with limited supply chains increase future replacement costs

> 扩展性规划与空间预留见 [[Layout_Guideline#§L-5 扩展与生命周期]]。
> 长期成本建模方法见 [[Cost_Guideline#§K-1 成本建模方法]]。

---

## 工作流集成 / Workflow Integration

Risk Auditor workflow:

1. **Read this Guideline first** — Understand risk classification and SPOF criteria before analysis
2. **Perform technical analysis** — Evaluate all risk domains per this document
3. **Output to ATS** — Pass risk assessment results to ATS for integration
4. **Flag conflicts** — If project requirements conflict with this Guideline, escalate to ATS before proceeding

> **Authority**: This Guideline defines the authoritative risk classification methodology. Do not downgrade risk levels to avoid escalation. If in doubt, escalate.

> Agent 角色边界见 [[PRINCIPLE_Guideline#§0 文件定位 / Document Position]];风险评审在 S9 场景(详见 [[PRINCIPLE_Guideline#§4 Key Matrix — Agent × 场景必读表]])下为必读全章节。

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-03-10 | 初始版本。源文件 `Works_Public/AGENTS/Risk Auditor.md`;包含 4 级风险分级、Power/Cooling/Control/Network SPOF 识别、6 类工程红旗、IT vs Total 负荷混淆、运维/部署/扩展/成本评估与工作流集成。 |
| v1.1 | 2026-06-05 | 结构规范化:章节 ID 对齐 [[PRINCIPLE_Guideline#§8 章节 ID 一致性表]] (R-1 风险分级方法 / R-2 单点故障识别 / R-3 工程红旗 / R-4 负荷定义风险 / R-5 运维风险评估 / R-6 部署风险评估 / R-7 扩展与成本风险);新增"速查"与"章节速查"索引;将原"Scalability Risk Analysis"与"Cost Risk Evaluation"合并至 R-7 扩展与成本风险;补充与 [[COOLING_SYSTEM_Guideline]]、[[POWER_SYSTEMS_Guideline]]、[[NETWORK_Guideline]]、[[Compliance_Guideline]]、[[Layout_Guideline]]、[[Cost_Guideline]] 及 [[PRINCIPLE_Guideline]] 的 [[#§ID 标题]] 交叉引用;Changelog 移至文件末尾。 |
