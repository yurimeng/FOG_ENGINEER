---
title: "05_Key_Matrix_Part2 — §4.2 矩阵 S7–S12 + §4.3 关键场景补充说明"
parent: "[[PRINCIPLE_Guideline]]"
order: 5
tags:
  - #workspace/engineer
  - #type/principle
  - #product/general
  - #architecture
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/PRINCIPLE_Guideline.md"
source_anchors:
  - "§4.2(S7-S12)"
  - "§4.3"
---

## §4.2 主矩阵 (续 S7–S12)

| # | 场景 / Scenario | AM | ATS | Cooling | Power | Layout |
|---|----------------|----|----|---------|-------|--------|
| **S7** | 多架构成本对比 | [[Cost_Guideline#§K-4 成本优化优先级\|§K-4]] (客户决策) | [[COOLING_SYSTEM_Guideline#§G-3 支持的冷却技术\|§G-3]], [[POWER_SYSTEMS_Guideline#§P-8 BESS 选型与 DG 对比\|§P-8]], [[Cost_Guideline#§K-3 架构成本对比\|§K-3]], [[Cost_Guideline#§K-4 成本优化优先级\|§K-4]] | [[COOLING_SYSTEM_Guideline#§G-3 支持的冷却技术\|§G-3]], [[COOLING_SYSTEM_Guideline#§G-5 浸没式冷却\|§G-5]], [[COOLING_SYSTEM_Guideline#§G-6 直冷液冷\|§G-6]] | [[POWER_SYSTEMS_Guideline#§P-8 BESS 选型与 DG 对比\|§P-8]] | (无) |
| **S8** | 合规审查 | [[Compliance_Guideline#§C-1 适用范围\|§C-1]], [[Compliance_Guideline#§C-7 认证要求汇总\|§C-7]] | [[Compliance_Guideline#§C-1 适用范围\|§C-1]], [[Compliance_Guideline#§C-7 认证要求汇总\|§C-7]] | [[Compliance_Guideline#§C-2 关键标准\|§C-2]], [[Compliance_Guideline#§C-4 数据中心合规\|§C-4]] | [[Compliance_Guideline#§C-3 储能合规\|§C-3]] | [[Compliance_Guideline#§C-5 容器数据中心合规\|§C-5]] |
| **S9** | 风险评审 / SPOF 识别 | [[Risk_Guideline#§R-1 风险分级方法\|§R-1]] | [[Risk_Guideline#§R-1 风险分级方法\|§R-1]], [[Risk_Guideline#§R-3 工程红旗\|§R-3]] | [[COOLING_SYSTEM_Guideline#§G-11 冗余策略\|§G-11]], [[Risk_Guideline#§R-2 单点故障识别\|§R-2]] | [[POWER_SYSTEMS_Guideline#§P-9 冗余结构与拓扑\|§P-9]], [[Risk_Guideline#§R-2 单点故障识别\|§R-2]] | [[Risk_Guideline#§R-6 部署风险评估\|§R-6]] |
| **S10** | 市场情报 / 博客 / 竞品研究 | [[Marketing_Guideline#§M-1 关注领域\|§M-1]] (项目方向) | (无) | (无) | (无) | (无) |
| **S11** | 项目文档更新 | 见 `AGENTS/AM.md` §4-5 | 见 `AGENTS/ATS.md` §4 | — | — | — |
| **S12** | 触发上报条件 | [[COOLING_SYSTEM_Guideline#§G-18 上报规则\|§G-18]], [[POWER_SYSTEMS_Guideline#§P-9 冗余结构与拓扑\|§P-9]], [[NETWORK_Guideline#§N-11 禁止事项\|§N-11]], [[Compliance_Guideline#§C-8 工作流集成\|§C-8]], [[Risk_Guideline#§R-3 工程红旗\|§R-3]] | 同左 + 整合判断 | [[COOLING_SYSTEM_Guideline#§G-17 工程警告条件\|§G-17]], [[COOLING_SYSTEM_Guideline#§G-18 上报规则\|§G-18]] | [[POWER_SYSTEMS_Guideline#§P-9 冗余结构与拓扑\|§P-9]] | [[Layout_Guideline#§L-7 工作流集成\|§L-7]] |

| # | 场景 | Cost | Compliance | Risk | Marketing |
|---|------|------|------------|------|-----------|
| **S7** | 多架构成本对比 | **必读全部** [[Cost_Guideline#§K-1 成本建模方法\|§K-1]] → [[Cost_Guideline#§K-6 工作流集成\|§K-6]] | (无) | [[Risk_Guideline#§R-7 扩展与成本风险\|§R-7]] | — |
| **S8** | 合规审查 | (无) | **必读全部** [[Compliance_Guideline#§C-1 适用范围\|§C-1]] → [[Compliance_Guideline#§C-8 工作流集成\|§C-8]] | [[Risk_Guideline#§R-3 工程红旗\|§R-3]] | — |
| **S9** | 风险评审 | [[Risk_Guideline#§R-7 扩展与成本风险\|§R-7]] | [[Compliance_Guideline#§C-6 合规风险识别\|§C-6]] | **必读全部** [[Risk_Guideline#§R-1 风险分级方法\|§R-1]] → [[Risk_Guideline#§R-7 扩展与成本风险\|§R-7]] | — |
| **S10** | 市场研究 | (无) | (无) | (无) | **必读全部** [[Marketing_Guideline#§M-1 关注领域\|§M-1]] → [[Marketing_Guideline#§M-6 禁止行为\|§M-6]] |
| **S11** | 项目文档更新 | — | — | — | — |
| **S12** | 触发上报条件 | [[Cost_Guideline#§K-6 工作流集成\|§K-6]] | [[Compliance_Guideline#§C-8 工作流集成\|§C-8]] | [[Risk_Guideline#§R-1 风险分级方法\|§R-1]], [[Risk_Guideline#§R-3 工程红旗\|§R-3]] | [[Marketing_Guideline#§M-6 禁止行为\|§M-6]] |

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
