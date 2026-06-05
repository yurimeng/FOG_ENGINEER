---
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/compliance
  - #MDC
---
# Compliance Guideline / 合规技术指南

Document Version / 文档版本: v1.1
Last Updated / 最后更新: 2026-06-05
Source / 来源: `Works_Public/AGENTS/Compliance Officer.md`

---

> **速查 / Quick Reference**: 本文件为 FOG 边缘数据中心预销售工程中**合规与认证**领域的权威 Guideline。Compliance Officer 在执行任何 UL / CSA / IEC / NFPA / 容器结构 / BESS 认证审查前必须完整阅读。文件索引与执行合约见 [[PRINCIPLE_Guideline#§4 Key Matrix — Agent × 场景 必读章节矩阵]]；合规场景 S8 列出了本 Guideline 的全部必读章节。

---

## 章节速查 / Section Index

| 章节 | 标题 | 一句话目的 |
|------|------|-----------|
| [[#C-1 适用范围]] | Applicable Scope | 定义 Compliance Officer 评估的合规域边界 |
| [[#C-2 关键标准]] | Key Standards | 列出 UL / CSA / IEC / NFPA 等关键标准与子规 |
| [[#C-3 储能系统合规]] | BESS Compliance | BESS / 储能系统合规评估要点 |
| [[#C-4 数据中心合规]] | Datacenter Compliance | 数据中心基础设施合规检查矩阵 |
| [[#C-5 容器数据中心合规]] | Container Datacenter Compliance | 容器 / 预制化数据中心的结构与环境合规 |
| [[#C-6 合规风险识别]] | Compliance Risk Detection | 必须 flag 的合规风险条件清单 |
| [[#C-7 认证要求汇总]] | Certification Requirements | 各子系统必需认证汇总矩阵 |
| [[#C-8 工作流集成]] | Workflow Integration | Compliance Officer 工作流与上报机制 |

---

## C-1 适用范围 / Applicable Scope

Compliance Officer evaluates compliance across the following domains:

| Domain / 领域 | Content / 内容 |
|---|---|
| Electrical safety / 电气安全 | UL, CSA, IEC, local codes |
| Cooling system safety / 冷却系统安全 | Thermal management, equipment safety |
| BESS / Energy storage / 储能系统 | Battery safety, thermal management, electrical isolation, fire suppression |
| Container datacenter / 容器数据中心 | Structural integrity, electrical integration, emergency access |
| Fire protection / 消防系统 | NFPA standards, fire suppression integration |
| Operational safety / 运维安全 | Safety procedures, certification requirements |

> Compliance Officer 拥有对合规结论的 **veto 权力**（详见 `AGENTS/Compliance Officer.md`）。当 [[#C-6 合规风险识别]] 中的任一红旗被触发时，结论即为 FAIL，必须上报 ATS。

---

## C-2 关键标准 / Key Standards

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

> 制冷剂选型与 IP 防护等级涉及 [[COOLING_SYSTEM_Guideline#§G-9 环境设计]]；电气隔离细节涉及 [[POWER_SYSTEMS_Guideline#§P-5 UPS 选型]]。跨域冲突时按 [[PRINCIPLE_Guideline#§6 跨 Guideline 冲突处理]] 处理：涉及安全/合规 → 合规侧优先。

---

## C-3 储能系统合规 / BESS Compliance

Energy storage systems such as BESS require compliance evaluation including:

- **Battery safety standards** — Cell-level and pack-level certification
- **Thermal management safety** — Temperature control limits, thermal runaway prevention
- **Electrical isolation** — High-voltage isolation, grounding, and bonding requirements
- **Fire suppression integration** — Suppression systems compatible with battery chemistry
- **UL 9540** — Standard for Energy Storage Systems and Equipment
- **UL 9540A** — Test Method for Evaluating Thermal Runaway Fire Propagation in Battery Energy Storage Systems

> **Critical**: BESS thermal runaway risk must be addressed with proper suppression and monitoring before deployment.

BESS vs DG 的系统级对比见 [[POWER_SYSTEMS_Guideline#§P-8 BESS 选型与 DG 对比]]；具体 BESS 产品 KB 文档（已通过 [[#C-7 认证要求汇总]] 矩阵验证）位于 `KB/3RD-PARTY/BESS/`，例如 [[Gotion ESC480-125P261-UL]]。

---

## C-4 数据中心合规 / Datacenter Compliance

For datacenter infrastructure, compliance checks include:

| Area / 领域 | Key Requirements / 主要要求 |
|---|---|
| Power system safety / 电力系统安全 | UPS, PDU, and generator compliance |
| Cooling system safety / 冷却系统安全 | Chiller, CRAC/CRAH, pump safety |
| Battery system regulations / 储能系统规范 | BESS integration with facility power |
| Container datacenter requirements / 容器数据中心要求 | Prefabricated modular infrastructure |
| Operational safety / 运维安全 | Lockout/tagout, arc flash, PPE |

> **负荷澄清要求**: 涉及"X MW / X kW"需求时，必须先按 [[POWER_SYSTEMS_Guideline#§P-1 IT 负载定义]] 区分 IT Load 与 Total Facility Load 再做合规判断，避免因负荷定义错误导致合规域被错配（详见 [[Risk_Guideline#§R-4 负荷定义风险]]）。

---

## C-5 容器数据中心合规 / Container Datacenter Compliance

Containerized infrastructure must be evaluated for:

- **Structural integrity** — Wind load, seismic, transportation structural requirements
- **Electrical integration** — Busbar, cable routing, grounding within confined space
- **Cooling system safety** — Indoor/outdoor operation, humidity control
- **Emergency access and maintenance** — Egress pathways, maintenance clearance, fire exit requirements
- **Environmental ratings** — NEMA/IP ratings for enclosure protection

> 与 [[Layout_Guideline#§L-6 容器与机架布局]] 中的物理布局约束互为前置：合规结论必须基于已完成维护通道净空与扩展规划验证的布局版本。

---

## C-6 合规风险识别 / Compliance Risk Detection

Compliance Officer must flag the following risk conditions:

- Uncertified equipment in critical infrastructure
- Electrical design conflicts with local codes
- Insufficient safety isolation (HV/LV boundaries)
- Cooling systems introducing safety hazards (flood risk, condensation, refrigerant leaks)
- BESS thermal runaway propagation potential
- Missing or inadequate fire suppression coverage
- Non-compliant cable management and tray routing

> 上述任何一条被触发即对应 [[Risk_Guideline#§R-3 工程红旗]] 中的 Critical 或 High 风险，必须在 [[#C-8 工作流集成]] 的工作流中**立即上报 ATS**，不得通过降级风险等级规避升级。

---

## C-7 认证要求汇总 / Certification Requirements

| System / 系统 | Required Certifications / 必需认证 |
|---|---|
| Electrical equipment / 电气设备 | UL, CSA, or IEC certification; CE marking where applicable |
| BESS / 储能系统 | UL 9540, UL 9540A; local utility interconnection approval |
| Fire suppression / 消防系统 | NFPA compliance; local fire marshal approval |
| Datacenter / 数据中心 | TIA-942 tier level requirements; local building codes |
| Container infrastructure / 容器设施 | Structural certification; transportation permits if mobile |

**认证矩阵使用规则**:

1. 在项目立项时由 Compliance Officer 完成本表逐行核验。
2. 任何系统行存在"必需认证缺失"或"认证过期"时，结论 = CONDITIONAL PASS 或 FAIL，不得记为 PASS。
3. 与 [[PRINCIPLE_Guideline#§4 Key Matrix — Agent × 场景 必读章节矩阵]] 场景 S8 中的客户要求（UL / CE / NFPA）逐项对齐。

---

## C-8 工作流集成 / Workflow Integration

Compliance Officer workflow:

1. **Read this Guideline first** — Reference applicable standards before analysis
2. **Perform technical analysis** — Evaluate project requirements against standards in this document
3. **Output to ATS** — Pass compliance results (PASS / CONDITIONAL PASS / FAIL) to ATS for integration
4. **Flag conflicts** — If project requirements conflict with this Guideline, escalate to ATS before proceeding

> **Authority**: This Guideline is the authoritative reference for compliance domain decisions. Do not override these standards without ATS escalation.

**结论状态语义**:

| 状态 | 含义 | 上游处理 |
|------|------|---------|
| **PASS** | 所有 [[#C-7 认证要求汇总]] 与 [[#C-2 关键标准]] 均满足，无 [[#C-6 合规风险识别]] 红旗 | ATS 直接整合 |
| **CONDITIONAL PASS** | 主路径合规，但有遗留项需客户/施工方在交付前补齐 | ATS 整合并附条件清单 |
| **FAIL** | 任一 Critical 红旗触发，或 [[#C-7 认证要求汇总]] 中存在必需认证缺失 | 阻断：立即上报 ATS，由 ATS 上报 AM |

> 触发 [[PRINCIPLE_Guideline#§1.6 上报原则]] 时，按 §1.6 顺序执行；本文件 §C-8 自身即是 §1.6 第 1 条的落地流程。

---

## Changelog

> v1.1 变更：按 [[PRINCIPLE_Guideline#§8 章节 ID 一致性表]] 对齐章节 ID 为 C-1 ~ C-8（标题后缀统一为"适用范围 / 关键标准 / 储能系统合规 / 数据中心合规 / 容器数据中心合规 / 合规风险识别 / 认证要求汇总 / 工作流集成"）；新增"速查 / Quick Reference"、"章节速查 / Section Index"块；为 [[#C-2 关键标准]] 追加与 [[COOLING_SYSTEM_Guideline#§G-9 环境设计]]、[[POWER_SYSTEMS_Guideline#§P-5 UPS 选型]] 的跨域引用；为 [[#C-3 储能系统合规]] 追加与 [[POWER_SYSTEMS_Guideline#§P-8 BESS 选型与 DG 对比]] 的交叉引用；为 [[#C-4 数据中心合规]] 强化 [[POWER_SYSTEMS_Guideline#§P-1 IT 负载定义]] 与 [[Risk_Guideline#§R-4 负荷定义风险]] 引用；为 [[#C-5 容器数据中心合规]] 追加与 [[Layout_Guideline#§L-6 容器与机架布局]] 的前置约束说明；为 [[#C-6 合规风险识别]] 强化与 [[Risk_Guideline#§R-3 工程红旗]] 的升级路径；为 [[#C-7 认证要求汇总]] 增加"认证矩阵使用规则"与 [[PRINCIPLE_Guideline#§4 Key Matrix — Agent × 场景 必读章节矩阵]] S8 的对齐说明；为 [[#C-8 工作流集成]] 显式定义 PASS / CONDITIONAL PASS / FAIL 三态语义并引用 [[PRINCIPLE_Guideline#§1.6 上报原则]]。结构按 [[PRINCIPLE_Guideline#§7 维护规则]] 规范化：YAML → H1 → 元数据 → Quick Reference → Section Index → 章节正文 → Changelog。版本 v1.0 → v1.1，Last Updated 更新至 2026-06-05。

---

*Document Version: v1.1 | Last Updated: 2026-06-05*
