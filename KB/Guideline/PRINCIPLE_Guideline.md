---
tags:
  - #workspace/engineer
  - #type/principle
  - #status/authoritative
  - #MDC
---
# ⚙️ PRINCIPLE — FOG/KB/Guideline 索引与执行准则 / Index & Operating Contract

Document Version / 文档版本: v1.0
Last Updated / 最后更新: 2026-06-05
Status / 状态: **Authoritative — 所有 Agent 加载后必读**

> **本文件是 `KB/Guideline/` 目录的总入口。** 它不重复具体技术规则，而是告诉每个 Agent：
> 1. 在什么场景下应该阅读哪份 Guideline 的哪一节（精确到 § 级别）
> 2. 每份 Guideline 内部的章节 ID 体系（用于跨文件稳定引用）
> 3. 跨 Guideline 之间的优先级与冲突处理
>
> **违反本 Principle 中 Key Matrix 列出的章节约束，等同于违反 Guideline 本身。** Agent 在执行任何工程任务前必须完成 Key Matrix 中对应行的章节阅读。

---

# §0 文件定位 / Document Position

| 项目 | 说明 |
|------|------|
| **作用** | `KB/Guideline/` 目录下所有 Guideline 文件的索引、操作合约、跨文件优先级声明 |
| **与 SOUL/PRINCIPLES.md 关系** | `SOUL/PRINCIPLES.md` 定义系统级工程哲学与角色原则；本文件定义 Guideline 层的访问与执行规则。两者不冲突时均须遵守，冲突时以 `SOUL/PRINCIPLES.md` 为准 |
| **与 AGENTS/*.md 关系** | 每个 Agent 的角色定义文件会引用本文件；Agent 在执行任务时必须先读本文件，再按本文件的 Key Matrix 进入对应 Guideline 章节 |
| **更新原则** | Key Matrix 中任何条目的变更必须同步更新本文件的 Changelog，并通知所有 Agent 维护者 |

---

# §1 跨 Guideline 通用强制规则 / Cross-Guideline Mandatory Rules

> 以下规则适用于**所有 Agent、所有项目场景**。违反将导致方案不合规。

## §1.1 无价格原则 / No-Price Rule

- **禁止**在任何 Guideline 文件、客户方案、对外输出中包含任何价格数字、报价区间、单价、合同金额。
- 客户问价 → 回复："*配置方案由我提供，价格由商务团队核算。请联系客户经理获取正式报价。*"
- **适用范围**: 所有 Guideline、所有 Agent、所有输出场景。

## §1.2 KB-only 产品原则 / KB-Only Product Rule

- **只允许**在核心产品线（A32 / AC40 / AC45 / DC45）或 `KB/3RD-PARTY/3rd Party List.md` 列出的供应商中选型。
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

---

# §2 文件清单与章节 ID 体系 / File Index & Section ID Schema

> 每份 Guideline 使用独立字母前缀，**保证跨文件引用绝对稳定**。

| # | 文件 | ID 前缀 | 章节范围 | 一句话定位 |
|---|------|---------|---------|-----------|
| 1 | **PRINCIPLE_Guideline**（本文件） | §1–§9 | 全局 | KB/Guideline 索引与执行合约 |
| 2 | [[COOLING_SYSTEM_Guideline]] | G-1 ~ G-19 | 冷却系统 | IT↔Cooling 配对、Hybrid 冷却、DX 激活、产品选型 |
| 3 | [[POWER_SYSTEMS_Guideline]] | P-1 ~ P-9 | 电力系统 | IT/Total 负荷、UPS、BESS vs DG、拓扑、冗余 |
| 4 | [[NETWORK_Guideline]] | N-1 ~ N-12 | 网络 | 三层架构、IB/ROCE、带内/带外、与 IT Zone 匹配 |
| 5 | [[Compliance_Guideline]] | C-1 ~ C-8 | 合规 | UL/CSA/IEC/NFPA、BESS、数据中心、容器 DC、认证矩阵 |
| 6 | [[Cost_Guideline]] | K-1 ~ K-6 | 成本 | 建模方法、CAPEX 分类、架构对比、优化优先级、Edge 经济性 |
| 7 | [[Layout_Guideline]] | L-1 ~ L-7 | 布局 | 容器与机架、通道净空、线缆、维护、扩展、浸没槽/DLC |
| 8 | [[Risk_Guideline]] | R-1 ~ R-7 | 风险 | 4 级分类、SPOF 识别、红旗、负荷风险、运维/部署/扩展/成本 |
| 9 | [[Marketing_Guideline]] | M-1 ~ M-6 | 市场 | 关注领域、周报、博客、竞品框架、信息源、禁止行为 |

> **引用约定**: 跨文件引用使用 `[[FILENAME#§ID 标题]]`，例如 `[[COOLING_SYSTEM_Guideline#G-7 Heat Rejection Systems]]`。
> 本文件 Key Matrix 表格内的"列项"使用 `G-7`、`P-3`、`C-1` 等短码，对应上方完整章节。

---

# §3 Zone 架构速查 / Zone Architecture Quick Reference

> Agent 在选型阶段确认 Zone 配置时使用。

## §3.1 IT Zone 内置产品

| IT Zone | 形态 | IT Load | UPS 状态 | 对应冷却容量 |
|---------|------|---------|---------|-------------|
| **A32** | 单柜 | 45–50 kW | 内置 | ~320 kW Hybrid |
| **AC40** | 40 ft 容器 | 400 kW | 外置（客户自备，9395XR-600） | ~600 kW Hybrid |
| **AC45** | 40 ft 容器 | 400 kW | 内置（9395XR-600） | ~600 kW Hybrid |
| **DC45** | 45 ft 容器 | 1240 kW | 内置（9395XR-1500） | ~1200 kW Hybrid |

**详细规范**：`KB/PRODUCTS/` 与 `POWER_SYSTEMS_Guideline §P-2`。

## §3.2 Zone 间物理连接

```
[Power Zone] ——市电 / BESS / DG——▶ [IT Zone] ——冷却液/热回水——▶ [Cooling Zone]
                                              │
                                              └─[Network Zone]──▶ 外部 / 其他集群
```

**关键约束**:

- IT ↔ Cooling = **1:1 强制配对**（详见 `COOLING_SYSTEM_Guideline §G-8`）
- Power Zone 与 IT Zone 拓扑 = `Grid → BESS → IT Zone` 或 `Grid + ATS + DG`
- Network Zone 与 IT Zone 拓扑参考 `NETWORK_Guideline §N-9`

---

# §4 Key Matrix — Agent × 场景 必读章节矩阵 / Mandatory Sections by Agent × Scenario

> **这是本文件的核心交付物。** 任何 Agent 接到任务后，必须：
> 1. 在矩阵的"场景"列中找到匹配的工作场景
> 2. 在该行对应的 Agent 列中读取列出的所有章节（精确到 G-/P-/N-/C-/K-/L-/R-/M- 编号）
> 3. **未完成阅读前不得进入设计、输出、对外沟通阶段**

## §4.1 矩阵使用说明

- **"必读"标记 (§)** 表示该章节中的规则是硬约束。Agent 在场景中必须**逐条核验**。
- **"参考"标记 (ref)** 表示该章节提供背景知识，建议阅读。
- **"—"** 表示该 Agent 在该场景下不直接涉及，无需阅读。
- **"上报"** 表示该场景下 Agent 必须将决策权交给 ATS，不得自行设计。

## §4.2 主矩阵 / Main Matrix

| # | 场景 / Scenario | AM | ATS | Cooling | Power | Layout | Cost | Compliance | Risk | Marketing |
|---|----------------|----|----|---------|-------|--------|------|------------|------|-----------|
| **S1** | 客户提及"X MW"负荷（需澄清 IT vs Total） | [[POWER_SYSTEMS_Guideline#§P-1 IT 负载与整体电力负荷\|§P-1]], [[POWER_SYSTEMS_Guideline#§P-3 关键规则\|§P-3]], [[Risk_Guideline#§R-4 负荷定义风险\|§R-4]] | [[POWER_SYSTEMS_Guideline#§P-1 IT 负载与整体电力负荷\|§P-1]], [[POWER_SYSTEMS_Guideline#§P-3 关键规则\|§P-3]], [[POWER_SYSTEMS_Guideline#§P-4 典型混淆场景\|§P-4]], [[Risk_Guideline#§R-4 负荷定义风险\|§R-4]] | [[POWER_SYSTEMS_Guideline#§P-1 IT 负载与整体电力负荷\|§P-1]] (冷却负荷输入) | [[POWER_SYSTEMS_Guideline#§P-1 IT 负载与整体电力负荷\|§P-1]], [[POWER_SYSTEMS_Guideline#§P-2 产品对照表\|§P-2]], [[POWER_SYSTEMS_Guideline#§P-3 关键规则\|§P-3]] | — | [[Cost_Guideline#§K-1 成本建模方法\|§K-1]] | [[Compliance_Guideline#§C-4 数据中心合规\|§C-4]] | [[Risk_Guideline#§R-4 负荷定义风险\|§R-4]] | — |
| **S2** | 配置 IT Zone（AC40/AC45/DC45/A32） | [[POWER_SYSTEMS_Guideline#§P-2 产品对照表\|§P-2]] (规模/形态对齐) | [[COOLING_SYSTEM_Guideline#§G-8 IT Zone 与冷却区匹配\|§G-8]], [[POWER_SYSTEMS_Guideline#§P-2 产品对照表\|§P-2]], [[POWER_SYSTEMS_Guideline#§P-5 UPS 选型\|§P-5]], [[NETWORK_Guideline#§N-9 网络与 IT Zone 匹配\|§N-9]] | [[COOLING_SYSTEM_Guideline#§G-8 IT Zone 与冷却区匹配\|§G-8]] | [[POWER_SYSTEMS_Guideline#§P-2 产品对照表\|§P-2]], [[POWER_SYSTEMS_Guideline#§P-5 UPS 选型\|§P-5]] | [[Layout_Guideline#§L-6 容器与机架布局\|§L-6]] | [[Cost_Guideline#§K-3 架构成本对比\|§K-3]] | [[Compliance_Guideline#§C-4 数据中心合规\|§C-4]] | [[Risk_Guideline#§R-1 风险分级方法\|§R-1]], [[Risk_Guideline#§R-7 扩展与成本风险\|§R-7]] | — |
| **S3** | 设计 Cooling Zone（架构、容量、配对） | [[COOLING_SYSTEM_Guideline#§G-19 最终目标\|§G-19]] (项目目标), [[POWER_SYSTEMS_Guideline#§P-2 产品对照表\|§P-2]] (IT Load) | [[COOLING_SYSTEM_Guideline#§G-4 冷却架构优先级\|§G-4]], [[COOLING_SYSTEM_Guideline#§G-7 热排放系统\|§G-7]], [[COOLING_SYSTEM_Guideline#§G-8 IT Zone 与冷却区匹配\|§G-8]], [[COOLING_SYSTEM_Guideline#§G-10 热负荷计算\|§G-10]], [[COOLING_SYSTEM_Guideline#§G-14 产品选择\|§G-14]] | **必读全部** [[COOLING_SYSTEM_Guideline#§G-1 强制工作流程\|§G-1]] → [[COOLING_SYSTEM_Guideline#§G-19 最终目标\|§G-19]]（详见 G-15 流程） | [[COOLING_SYSTEM_Guideline#§G-7 热排放系统\|§G-7]] (冷却功耗输入) | [[Layout_Guideline#§L-6 容器与机架布局\|§L-6]] (冷却设备位置) | [[Cost_Guideline#§K-3 架构成本对比\|§K-3]] | [[Compliance_Guideline#§C-2 关键标准\|§C-2]], [[Compliance_Guideline#§C-4 数据中心合规\|§C-4]] | [[Risk_Guideline#§R-2 单点故障识别\|§R-2]] (冷却 SPOF) | — |
| **S4** | 设计 Power Zone（UPS / BESS / DG / 拓扑） | [[POWER_SYSTEMS_Guideline#§P-4 典型混淆场景\|§P-4]], [[POWER_SYSTEMS_Guideline#§P-8 BESS 选型与 DG 对比\|§P-8]] (客户语言) | [[POWER_SYSTEMS_Guideline#§P-5 UPS 选型\|§P-5]], [[POWER_SYSTEMS_Guideline#§P-8 BESS 选型与 DG 对比\|§P-8]], [[POWER_SYSTEMS_Guideline#§P-9 冗余结构与拓扑\|§P-9]] | (无) | **必读全部** [[POWER_SYSTEMS_Guideline#§P-1 IT 负载与整体电力负荷\|§P-1]] → [[POWER_SYSTEMS_Guideline#§P-9 冗余结构与拓扑\|§P-9]] | [[Layout_Guideline#§L-6 容器与机架布局\|§L-6]] (电力设备占地) | [[Cost_Guideline#§K-3 架构成本对比\|§K-3]] | [[Compliance_Guideline#§C-3 储能合规\|§C-3]], [[Compliance_Guideline#§C-7 认证要求汇总\|§C-7]] | [[Risk_Guideline#§R-2 单点故障识别\|§R-2]] (电力 SPOF) | — |
| **S5** | 设计 Network Zone（架构、IB/ROCE、带内/带外） | [[NETWORK_Guideline#§N-9 网络与 IT Zone 匹配\|§N-9]] (业务语言) | [[NETWORK_Guideline#§N-2 核心设计原则\|§N-2]], [[NETWORK_Guideline#§N-3 网络架构选型\|§N-3]], [[NETWORK_Guideline#§N-9 网络与 IT Zone 匹配\|§N-9]] | (无) | (无) | [[Layout_Guideline#§L-3 线缆敷设标准\|§L-3]] (网络布线) | [[Cost_Guideline#§K-3 架构成本对比\|§K-3]] | [[Compliance_Guideline#§C-2 关键标准\|§C-2]] | [[Risk_Guideline#§R-2 单点故障识别\|§R-2]] (网络 SPOF) | — |
| **S6** | 物理布局规划 | [[Layout_Guideline#§L-1 核心布局原则\|§L-1]] (项目约束) | [[Layout_Guideline#§L-1 核心布局原则\|§L-1]], [[Layout_Guideline#§L-2 维护通道净空\|§L-2]] | [[Layout_Guideline#§L-6 容器与机架布局\|§L-6]] (冷却设备布置) | [[Layout_Guideline#§L-6 容器与机架布局\|§L-6]] (电力设备布置) | **必读全部** [[Layout_Guideline#§L-1 核心布局原则\|§L-1]] → [[Layout_Guideline#§L-7 工作流集成\|§L-7]] | (无) | [[Compliance_Guideline#§C-5 容器数据中心合规\|§C-5]] | [[Risk_Guideline#§R-5 运维风险评估\|§R-5]], [[Risk_Guideline#§R-6 部署风险评估\|§R-6]] | — |
| **S7** | 多架构成本对比 | [[Cost_Guideline#§K-4 成本优化优先级\|§K-4]] (客户决策) | [[COOLING_SYSTEM_Guideline#§G-3 支持的冷却技术\|§G-3]], [[POWER_SYSTEMS_Guideline#§P-8 BESS 选型与 DG 对比\|§P-8]], [[Cost_Guideline#§K-3 架构成本对比\|§K-3]], [[Cost_Guideline#§K-4 成本优化优先级\|§K-4]] | [[COOLING_SYSTEM_Guideline#§G-3 支持的冷却技术\|§G-3]], [[COOLING_SYSTEM_Guideline#§G-5 浸没式冷却\|§G-5]], [[COOLING_SYSTEM_Guideline#§G-6 直冷液冷\|§G-6]] | [[POWER_SYSTEMS_Guideline#§P-8 BESS 选型与 DG 对比\|§P-8]] | (无) | **必读全部** [[Cost_Guideline#§K-1 成本建模方法\|§K-1]] → [[Cost_Guideline#§K-6 工作流集成\|§K-6]] | (无) | [[Risk_Guideline#§R-7 扩展与成本风险\|§R-7]] | — |
| **S8** | 合规审查（UL / CE / NFPA） | [[Compliance_Guideline#§C-1 适用范围\|§C-1]], [[Compliance_Guideline#§C-7 认证要求汇总\|§C-7]] (客户要求) | [[Compliance_Guideline#§C-1 适用范围\|§C-1]], [[Compliance_Guideline#§C-7 认证要求汇总\|§C-7]] | [[Compliance_Guideline#§C-2 关键标准\|§C-2]] (制冷剂、IP 等级), [[Compliance_Guideline#§C-4 数据中心合规\|§C-4]] | [[Compliance_Guideline#§C-3 储能合规\|§C-3]] | [[Compliance_Guideline#§C-5 容器数据中心合规\|§C-5]] | (无) | **必读全部** [[Compliance_Guideline#§C-1 适用范围\|§C-1]] → [[Compliance_Guideline#§C-8 工作流集成\|§C-8]] | [[Risk_Guideline#§R-3 工程红旗\|§R-3]] | — |
| **S9** | 风险评审 / SPOF 识别 | [[Risk_Guideline#§R-1 风险分级方法\|§R-1]] | [[Risk_Guideline#§R-1 风险分级方法\|§R-1]], [[Risk_Guideline#§R-3 工程红旗\|§R-3]] | [[COOLING_SYSTEM_Guideline#§G-11 冗余策略\|§G-11]], [[Risk_Guideline#§R-2 单点故障识别\|§R-2]] | [[POWER_SYSTEMS_Guideline#§P-9 冗余结构与拓扑\|§P-9]], [[Risk_Guideline#§R-2 单点故障识别\|§R-2]] | [[Risk_Guideline#§R-6 部署风险评估\|§R-6]] | [[Risk_Guideline#§R-7 扩展与成本风险\|§R-7]] | [[Compliance_Guideline#§C-6 合规风险识别\|§C-6]] | **必读全部** [[Risk_Guideline#§R-1 风险分级方法\|§R-1]] → [[Risk_Guideline#§R-7 扩展与成本风险\|§R-7]] | — |
| **S10** | 市场情报 / 博客 / 竞品研究 | [[Marketing_Guideline#§M-1 关注领域\|§M-1]] (项目方向) | (无) | (无) | (无) | (无) | (无) | (无) | (无) | **必读全部** [[Marketing_Guideline#§M-1 关注领域\|§M-1]] → [[Marketing_Guideline#§M-6 禁止行为\|§M-6]] |
| **S11** | 项目文档更新（Project Record / RFI） | 见 `AGENTS/AM.md` §4-5 | 见 `AGENTS/ATS.md` §4 | — | — | — | — | — | — | — |
| **S12** | 触发上报条件（任意 §1.6 触发） | [[COOLING_SYSTEM_Guideline#§G-18 上报规则\|§G-18]], [[POWER_SYSTEMS_Guideline#§P-9 冗余结构与拓扑\|§P-9]], [[NETWORK_Guideline#§N-11 禁止事项\|§N-11]], [[Compliance_Guideline#§C-8 工作流集成\|§C-8]], [[Risk_Guideline#§R-3 工程红旗\|§R-3]] | 同左 + 整合判断 | [[COOLING_SYSTEM_Guideline#§G-17 工程警告条件\|§G-17]], [[COOLING_SYSTEM_Guideline#§G-18 上报规则\|§G-18]] | [[POWER_SYSTEMS_Guideline#§P-9 冗余结构与拓扑\|§P-9]] | [[Layout_Guideline#§L-7 工作流集成\|§L-7]] | [[Cost_Guideline#§K-6 工作流集成\|§K-6]] | [[Compliance_Guideline#§C-8 工作流集成\|§C-8]] | [[Risk_Guideline#§R-1 风险分级方法\|§R-1]], [[Risk_Guideline#§R-3 工程红旗\|§R-3]] | [[Marketing_Guideline#§M-6 禁止行为\|§M-6]] |

## §4.3 关键场景补充说明 / Scenario Notes

### S1 — 负荷澄清场景

**触发条件**: 客户用 "X MW / X kW / 容量" 描述需求。**所有 Agent 在第一次响应前**必须完成 §P-1 阅读并主动澄清。

**输出格式约束**（详见 [[POWER_SYSTEMS_Guideline#§P-3 关键规则|§P-3]]）:
```
IT 负载:         xxx kW
整体电力负荷:    xxx kW (PUE ≈ x.xx)
```

### S3 — Cooling Zone 设计

冷却 Agent **必须**完整阅读 §G-1 → §G-19（按 G-15 两步查询流程）。**任何"客户特别要求"（如纯干冷器、N+1 冷却冗余、超过 KB 范围的设备容量）必须按 §G-18 上报**。

### S4 — Power Zone 设计

电力 Agent **必须**完整阅读 §P-1 → §P-9。**UPS 型号与 IT Zone 强绑定**（详见 §P-5），**禁止替换**。BESS 选型场景下必须给出 §P-8 选型决策表中的推荐方案+理由。

### S9 — 风险评审

**Critical 级风险 (R-1) 一旦识别必须立即上报 ATS，不得继续分析**。

### S10 — 市场研究

Market Researcher **不向 AM/ATS 输出技术内容**。所有产出写入 `/Market/` 目录，遵守 §M-6 禁止行为（无价格、无客户信息、不贬低竞品）。

---

# §5 上报决策树 / Escalation Decision Tree

```
客户需求进入
   │
   ▼
[是否触及 §1.6 触发条件?]
   │                        │
   YES                       NO
   │                        │
   ▼                        ▼
[立即上报 ATS]      [进入 Key Matrix 场景匹配]
                            │
                            ▼
                  [按场景完成必读章节阅读]
                            │
                            ▼
                  [按章节规则进行设计/分析]
                            │
                            ▼
                  [是否产生与 Guideline 冲突?]
                            │            │
                            YES           NO
                            │            │
                            ▼            ▼
                      [上报 ATS]   [按规范输出给 ATS/AM]
```

> 上报 = 留痕。自行决定 = 责任。

---

# §6 跨 Guideline 冲突处理 / Cross-Guideline Conflict Resolution

| 冲突类型 | 处理规则 |
|---------|---------|
| **本 Principle vs 具体 Guideline** | 具体 Guideline 优先（本 Principle 提供索引与执行规则，不重复技术约束） |
| **Guideline A vs Guideline B** | 涉及安全/合规 → 合规侧优先；涉及可靠性 → 工程现实优先；不确定 → 上报 ATS |
| **Guideline vs KB 产品文档** | Guideline 优先（详见 [[COOLING_SYSTEM_Guideline#§G-15 KB 查询与验证|§G-15]]、`AGENTS/ATS.md` §4.3） |
| **Guideline vs SOUL/PRINCIPLES.md** | SOUL/PRINCIPLES.md 优先 |
| **Guideline vs 客户需求** | Guideline 是硬约束，需求冲突时**必须上报**而非自行调整 Guideline |
| **同一 Guideline 内旧版本 vs 新版本** | 以文件头部 "Last Updated" 字段标注的版本为准 |

---

# §7 维护规则 / Maintenance Rules

| 规则 | 说明 |
|------|------|
| **新增章节 ID** | 必须按现有前缀（G-/P-/N-/C-/K-/L-/R-/M-）继续编号 |
| **章节重命名** | 必须同步更新本文件 §2 章节范围与 §4 Key Matrix 中所有引用 |
| **章节删除** | 必须在本文件 Changelog 留痕；Key Matrix 中所有引用该章节的单元格必须清除或迁移 |
| **新增 Guideline 文件** | 必须在 §2 文件清单新增一行；在 §4 Key Matrix 中按需新增 Agent × 场景列项 |
| **本 Principle 变更** | 必须更新 Changelog 并在内部 broadcast；不修改本文件则 Key Matrix 视为权威 |

---

# §8 章节 ID 一致性表 / Section ID Cross-Reference

> Agent 在引用时使用下表中的"短码"。本表是 §2 与 §4 的合并视图。

| 短码 | 含义 | 完整章节标题 | 所在文件 |
|------|------|------------|---------|
| G-1 | 强制工作流程 | §G-1 强制工作流程 | COOLING_SYSTEM_Guideline |
| G-2 | 冷却范围 | §G-2 热工工程范围 | COOLING_SYSTEM_Guideline |
| G-3 | 冷却技术分类 | §G-3 支持的冷却技术 | COOLING_SYSTEM_Guideline |
| G-4 | 优先级 | §G-4 冷却架构优先级 | COOLING_SYSTEM_Guideline |
| G-5 | 浸没式 | §G-5 浸没式冷却 | COOLING_SYSTEM_Guideline |
| G-6 | DLC | §G-6 直冷液冷 | COOLING_SYSTEM_Guideline |
| G-7 | 热排放 | §G-7 热排放系统 | COOLING_SYSTEM_Guideline |
| G-8 | IT↔Cooling 配对 | §G-8 IT Zone 与冷却区匹配 | COOLING_SYSTEM_Guideline |
| G-9 | 环境设计 | §G-9 环境设计 | COOLING_SYSTEM_Guideline |
| G-10 | 热负荷计算 | §G-10 热负荷计算 | COOLING_SYSTEM_Guideline |
| G-11 | 冗余策略 | §G-11 冗余策略 | COOLING_SYSTEM_Guideline |
| G-12 | 容器冷却 | §G-12 容器冷却 | COOLING_SYSTEM_Guideline |
| G-13 | 极端条件 | §G-13 极端条件运行 | COOLING_SYSTEM_Guideline |
| G-14 | 产品选择 | §G-14 产品选择 | COOLING_SYSTEM_Guideline |
| G-15 | KB 查询 | §G-15 KB 查询与验证 | COOLING_SYSTEM_Guideline |
| G-16 | 验证清单 | §G-16 验证清单 | COOLING_SYSTEM_Guideline |
| G-17 | 警告条件 | §G-17 工程警告条件 | COOLING_SYSTEM_Guideline |
| G-18 | 上报规则 | §G-18 上报规则 | COOLING_SYSTEM_Guideline |
| G-19 | 最终目标 | §G-19 最终目标 | COOLING_SYSTEM_Guideline |
| P-1 | 负荷定义 | §P-1 IT 负载与整体电力负荷 | POWER_SYSTEMS_Guideline |
| P-2 | 产品对照 | §P-2 产品对照表 | POWER_SYSTEMS_Guideline |
| P-3 | 关键规则 | §P-3 关键规则 | POWER_SYSTEMS_Guideline |
| P-4 | 混淆场景 | §P-4 典型混淆场景 | POWER_SYSTEMS_Guideline |
| P-5 | UPS 选型 | §P-5 UPS 选型 | POWER_SYSTEMS_Guideline |
| P-6 | 电池技术 | §P-6 UPS 电池技术对比 | POWER_SYSTEMS_Guideline |
| P-7 | DG 选型 | §P-7 柴油发电机选型 | POWER_SYSTEMS_Guideline |
| P-8 | BESS / DG | §P-8 BESS 选型与 DG 对比 | POWER_SYSTEMS_Guideline |
| P-9 | 冗余拓扑 | §P-9 冗余结构与拓扑 | POWER_SYSTEMS_Guideline |
| N-1 | 文件定位 | §N-1 文件定位 | NETWORK_Guideline |
| N-2 | 设计原则 | §N-2 核心设计原则 | NETWORK_Guideline |
| N-3 | 架构选型 | §N-3 网络架构选型 | NETWORK_Guideline |
| N-4 | IB 原则 | §N-4 IB 设计原则 | NETWORK_Guideline |
| N-5 | ROCE 原则 | §N-5 ROCE 设计原则 | NETWORK_Guideline |
| N-6 | 带内管理 | §N-6 带内管理网络 | NETWORK_Guideline |
| N-7 | 带外管理 | §N-7 带外管理网络 | NETWORK_Guideline |
| N-8 | 带内带外对比 | §N-8 带内 vs 带外管理对比 | NETWORK_Guideline |
| N-9 | IT Zone 匹配 | §N-9 网络与 IT Zone 匹配 | NETWORK_Guideline |
| N-10 | 安全设计 | §N-10 安全设计原则 | NETWORK_Guideline |
| N-11 | 禁止事项 | §N-11 禁止事项 | NETWORK_Guideline |
| N-12 | 参考文档 | §N-12 参考文档 | NETWORK_Guideline |
| C-1 | 适用范围 | §C-1 适用范围 | Compliance_Guideline |
| C-2 | 关键标准 | §C-2 关键标准 | Compliance_Guideline |
| C-3 | 储能合规 | §C-3 储能系统合规 | Compliance_Guideline |
| C-4 | 数据中心合规 | §C-4 数据中心合规 | Compliance_Guideline |
| C-5 | 容器 DC 合规 | §C-5 容器数据中心合规 | Compliance_Guideline |
| C-6 | 风险识别 | §C-6 合规风险识别 | Compliance_Guideline |
| C-7 | 认证矩阵 | §C-7 认证要求汇总 | Compliance_Guideline |
| C-8 | 工作流集成 | §C-8 工作流集成 | Compliance_Guideline |
| K-1 | 建模方法 | §K-1 成本建模方法 | Cost_Guideline |
| K-2 | CAPEX 分类 | §K-2 CAPEX 分类 | Cost_Guideline |
| K-3 | 架构对比 | §K-3 架构成本对比 | Cost_Guideline |
| K-4 | 优化优先级 | §K-4 成本优化优先级 | Cost_Guideline |
| K-5 | Edge 经济 | §K-5 边缘部署经济 | Cost_Guideline |
| K-6 | 工作流集成 | §K-6 工作流集成 | Cost_Guideline |
| L-1 | 布局原则 | §L-1 核心布局原则 | Layout_Guideline |
| L-2 | 通道净空 | §L-2 维护通道净空 | Layout_Guideline |
| L-3 | 线缆标准 | §L-3 线缆敷设标准 | Layout_Guideline |
| L-4 | 维护可达 | §L-4 维护可达性 | Layout_Guideline |
| L-5 | 扩展规划 | §L-5 扩展规划 | Layout_Guideline |
| L-6 | 容器机架 | §L-6 容器与机架布局 | Layout_Guideline |
| L-7 | 工作流集成 | §L-7 工作流集成 | Layout_Guideline |
| R-1 | 风险分级 | §R-1 风险分级方法 | Risk_Guideline |
| R-2 | SPOF 识别 | §R-2 单点故障识别 | Risk_Guideline |
| R-3 | 工程红旗 | §R-3 工程红旗 | Risk_Guideline |
| R-4 | 负荷风险 | §R-4 负荷定义风险 | Risk_Guideline |
| R-5 | 运维风险 | §R-5 运维风险评估 | Risk_Guideline |
| R-6 | 部署风险 | §R-6 部署风险评估 | Risk_Guideline |
| R-7 | 扩展成本 | §R-7 扩展与成本风险 | Risk_Guideline |
| M-1 | 关注领域 | §M-1 关注领域 | Marketing_Guideline |
| M-2 | 周报结构 | §M-2 市场周报结构 | Marketing_Guideline |
| M-3 | 博客结构 | §M-3 博客草稿结构 | Marketing_Guideline |
| M-4 | 竞品框架 | §M-4 竞品研究框架 | Marketing_Guideline |
| M-5 | 信息源 | §M-5 信息来源 | Marketing_Guideline |
| M-6 | 禁止行为 | §M-6 禁止行为 | Marketing_Guideline |

---

# §9 变更日志 / Changelog

> v1.0 变更：新建 `PRINCIPLE_Guideline.md`，作为 `KB/Guideline/` 目录的索引与执行合约。引入 Key Matrix（§4），按 Agent × 场景列出必读章节。所有章节引用使用 § 前缀短码，可在 §8 反查到完整标题与文件位置。

---

*Document Version: v1.0 | Last Updated: 2026-06-05*
