---
title: "02_Cross_Rules — §1 跨 Guideline 通用强制规则"
parent: "[[PRINCIPLE_Guideline]]"
order: 2
tags:
  - #workspace/engineer
  - #type/principle
  - #product/general
  - #architecture
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/PRINCIPLE_Guideline.md"
source_anchors:
  - "§1"
---

# §1 跨 Guideline 通用强制规则 / Cross-Guideline Mandatory Rules

> 以下规则适用于**所有 Agent、所有项目场景**。违反将导致方案不合规。

## §1.1 无价格原则 / No-Price Rule

- **禁止**在任何 Guideline 文件、客户方案、对外输出中包含任何价格数字、报价区间、单价、合同金额。
- 客户问价 → 回复："*配置方案由我提供，价格由商务团队核算。请联系客户经理获取正式报价。*"
- **适用范围**: 所有 Guideline、所有 Agent、所有输出场景。

## §1.2 KB-only 产品原则 / KB-Only Product Rule

- **只允许**在核心产品线（A32 / AC40 / AC45 / DC45）或 `KB/3RD-PARTY/3rd Party List.md` 列出的供应商中选型。 ^mdc-bdee564d92
- 任何"建议使用 KB 之外的产品"必须先上报 ATS，再由 ATS 上报 AM。
- **适用范围**: 所有技术 Guideline（Cooling/Power/Network/Layout/Compliance/Cost）。

## §1.3 IT Load vs Total Facility Load 强制澄清 / Load Disambiguation

- 客户提及"X MW / X kW"时，**必须先明确**是 IT Load 还是 Total Facility Load。
- 所有方案输出必须**同时标注**两项数值（详见 `POWER_SYSTEMS_Guideline §P-3`）。
- **违反代价**: 负荷定义错误会引发冷却、UPS、电网申请的级联设计错误（详见 `Risk_Guideline §R-4`）。

## §1.4 KB 两步查询流程 / Two-Step KB Lookup (Universal)

> 任何 Zone（IT/Cooling/Power/Network）配置前必须遵循。

| Step | 动作 | 失败处理 |
|------|------|---------|
| **Step 1** | 读取对应 Guideline（`KB/Guideline/<CATEGORY>_Guideline.md`） | 缺失 → 上报 ATS |
| **Step 2** | 遍历 `KB/3RD-PARTY/<category>/` 找到产品文档 | 无匹配 → 上报 ATS |

**任何 Zone 选型在 Guideline 与产品文档之间出现冲突时，Guideline 优先。**

## §1.5 Zone 冗余规则 / Zone Redundancy Constraints (Universal)

| Zone | N+1 | 2N |
|------|-----|----|
| **IT Zone** | ❌ 不提供 | ❌ 不提供 |
| **Cooling Zone** | ❌ 不提供 | ❌ 不提供 |
| **Power Zone** | ✅ 允许（需额外 Switchgear） | ✅ 允许（需额外 Switchgear） |
| **Network Zone** | ✅ 链路与设备级冗余 | 视项目需求 |

> **关键**: 客户询问 N+1/2N 冷却或 IT 冗余时，**必须上报 ATS 而非自行承诺**。详细见 `COOLING_SYSTEM_Guideline §G-18`、`POWER_SYSTEMS_Guideline §P-9`。

## §1.6 上报原则 / Escalation Principle

任何 Agent 在以下情况**必须立即上报** ATS：

1. 项目需求与本 Principle Key Matrix 列出的某条章节规则冲突
2. 项目需求与具体 Guideline 章节规则冲突
3. KB 中无对应产品 / 标准可满足需求
4. 客户请求被 §1.1（无价格）、§1.2（KB-only）、§1.3（负荷澄清）、§1.5（Zone 冗余）禁止的方案
5. 检测到 Critical 级风险（见 `Risk_Guideline §R-1`）

> **禁止 Agent 自行决定违反 Guideline 的方案。** 上报 = 留痕；自行决定 = 责任。
