---
title: "04_Key_Matrix_Part1 — §4.1 使用说明 + §4.2 矩阵 S1–S6"
parent: "[[PRINCIPLE_Guideline]]"
order: 4
tags:
  - #workspace/engineer
  - #type/principle
  - #product/general
  - #architecture
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/PRINCIPLE_Guideline.md"
source_anchors:
  - "§4.1"
  - "§4.2(S1-S6)"
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

## §4.2 主矩阵 / Main Matrix (S1–S6)

| # | 场景 / Scenario | AM | ATS | Cooling | Power |
|---|----------------|----|----|---------|-------|
| **S1** | 客户提及"X MW"负荷 | [[POWER_SYSTEMS_Guideline#§P-1 IT 负载与整体电力负荷\|§P-1]], [[POWER_SYSTEMS_Guideline#§P-3 关键规则\|§P-3]], [[Risk_Guideline#§R-4 负荷定义风险\|§R-4]] | [[POWER_SYSTEMS_Guideline#§P-1 IT 负载与整体电力负荷\|§P-1]], [[POWER_SYSTEMS_Guideline#§P-3 关键规则\|§P-3]], [[POWER_SYSTEMS_Guideline#§P-4 典型混淆场景\|§P-4]], [[Risk_Guideline#§R-4 负荷定义风险\|§R-4]] | [[POWER_SYSTEMS_Guideline#§P-1 IT 负载与整体电力负荷\|§P-1]] (冷却负荷输入) | [[POWER_SYSTEMS_Guideline#§P-1 IT 负载与整体电力负荷\|§P-1]], [[POWER_SYSTEMS_Guideline#§P-2 产品对照表\|§P-2]], [[POWER_SYSTEMS_Guideline#§P-3 关键规则\|§P-3]] |
| **S2** | 配置 IT Zone | [[POWER_SYSTEMS_Guideline#§P-2 产品对照表\|§P-2]] (规模/形态对齐) | [[COOLING_SYSTEM_Guideline#§G-8 IT Zone 与冷却区匹配\|§G-8]], [[POWER_SYSTEMS_Guideline#§P-2 产品对照表\|§P-2]], [[POWER_SYSTEMS_Guideline#§P-5 UPS 选型\|§P-5]], [[NETWORK_Guideline#§N-9 网络与 IT Zone 匹配\|§N-9]] | [[COOLING_SYSTEM_Guideline#§G-8 IT Zone 与冷却区匹配\|§G-8]] | [[POWER_SYSTEMS_Guideline#§P-2 产品对照表\|§P-2]], [[POWER_SYSTEMS_Guideline#§P-5 UPS 选型\|§P-5]] |
| **S3** | 设计 Cooling Zone | [[COOLING_SYSTEM_Guideline#§G-19 最终目标\|§G-19]] (项目目标), [[POWER_SYSTEMS_Guideline#§P-2 产品对照表\|§P-2]] (IT Load) | [[COOLING_SYSTEM_Guideline#§G-4 冷却架构优先级\|§G-4]], [[COOLING_SYSTEM_Guideline#§G-7 热排放系统\|§G-7]], [[COOLING_SYSTEM_Guideline#§G-8 IT Zone 与冷却区匹配\|§G-8]], [[COOLING_SYSTEM_Guideline#§G-10 热负荷计算\|§G-10]], [[COOLING_SYSTEM_Guideline#§G-14 产品选择\|§G-14]] | **必读全部** [[COOLING_SYSTEM_Guideline#§G-1 强制工作流程\|§G-1]] → [[COOLING_SYSTEM_Guideline#§G-19 最终目标\|§G-19]] | [[COOLING_SYSTEM_Guideline#§G-7 热排放系统\|§G-7]] (冷却功耗输入) |
| **S4** | 设计 Power Zone | [[POWER_SYSTEMS_Guideline#§P-4 典型混淆场景\|§P-4]], [[POWER_SYSTEMS_Guideline#§P-8 BESS 选型与 DG 对比\|§P-8]] (客户语言) | [[POWER_SYSTEMS_Guideline#§P-5 UPS 选型\|§P-5]], [[POWER_SYSTEMS_Guideline#§P-8 BESS 选型与 DG 对比\|§P-8]], [[POWER_SYSTEMS_Guideline#§P-9 冗余结构与拓扑\|§P-9]] | (无) | **必读全部** [[POWER_SYSTEMS_Guideline#§P-1 IT 负载与整体电力负荷\|§P-1]] → [[POWER_SYSTEMS_Guideline#§P-9 冗余结构与拓扑\|§P-9]] |
| **S5** | 设计 Network Zone | [[NETWORK_Guideline#§N-9 网络与 IT Zone 匹配\|§N-9]] (业务语言) | [[NETWORK_Guideline#§N-2 核心设计原则\|§N-2]], [[NETWORK_Guideline#§N-3 网络架构选型\|§N-3]], [[NETWORK_Guideline#§N-9 网络与 IT Zone 匹配\|§N-9]] | (无) | (无) |
| **S6** | 物理布局规划 | [[Layout_Guideline#§L-1 核心布局原则\|§L-1]] (项目约束) | [[Layout_Guideline#§L-1 核心布局原则\|§L-1]], [[Layout_Guideline#§L-2 维护通道净空\|§L-2]] | [[Layout_Guideline#§L-6 容器与机架布局\|§L-6]] (冷却设备布置) | [[Layout_Guideline#§L-6 容器与机架布局\|§L-6]] (电力设备布置) |

| # | 场景 | Layout | Cost | Compliance | Risk | Marketing |
|---|------|--------|------|------------|------|-----------|
| **S1** | 客户提及"X MW"负荷 | — | [[Cost_Guideline#§K-1 成本建模方法\|§K-1]] | [[Compliance_Guideline#§C-4 数据中心合规\|§C-4]] | [[Risk_Guideline#§R-4 负荷定义风险\|§R-4]] | — |
| **S2** | 配置 IT Zone | [[Layout_Guideline#§L-6 容器与机架布局\|§L-6]] | [[Cost_Guideline#§K-3 架构成本对比\|§K-3]] | [[Compliance_Guideline#§C-4 数据中心合规\|§C-4]] | [[Risk_Guideline#§R-1 风险分级方法\|§R-1]], [[Risk_Guideline#§R-7 扩展与成本风险\|§R-7]] | — |
| **S3** | 设计 Cooling Zone | [[Layout_Guideline#§L-6 容器与机架布局\|§L-6]] (冷却设备位置) | [[Cost_Guideline#§K-3 架构成本对比\|§K-3]] | [[Compliance_Guideline#§C-2 关键标准\|§C-2]], [[Compliance_Guideline#§C-4 数据中心合规\|§C-4]] | [[Risk_Guideline#§R-2 单点故障识别\|§R-2]] (冷却 SPOF) | — |
| **S4** | 设计 Power Zone | [[Layout_Guideline#§L-6 容器与机架布局\|§L-6]] (电力设备占地) | [[Cost_Guideline#§K-3 架构成本对比\|§K-3]] | [[Compliance_Guideline#§C-3 储能合规\|§C-3]], [[Compliance_Guideline#§C-7 认证要求汇总\|§C-7]] | [[Risk_Guideline#§R-2 单点故障识别\|§R-2]] (电力 SPOF) | — |
| **S5** | 设计 Network Zone | [[Layout_Guideline#§L-3 线缆敷设标准\|§L-3]] (网络布线) | [[Cost_Guideline#§K-3 架构成本对比\|§K-3]] | [[Compliance_Guideline#§C-2 关键标准\|§C-2]] | [[Risk_Guideline#§R-2 单点故障识别\|§R-2]] (网络 SPOF) | — |
| **S6** | 物理布局规划 | **必读全部** [[Layout_Guideline#§L-1 核心布局原则\|§L-1]] → [[Layout_Guideline#§L-7 工作流集成\|§L-7]] | (无) | [[Compliance_Guideline#§C-5 容器数据中心合规\|§C-5]] | [[Risk_Guideline#§R-5 运维风险评估\|§R-5]], [[Risk_Guideline#§R-6 部署风险评估\|§R-6]] | — |
