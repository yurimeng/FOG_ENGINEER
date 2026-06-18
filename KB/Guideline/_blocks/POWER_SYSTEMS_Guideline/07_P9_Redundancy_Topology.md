---
title: §P-9 冗余结构与拓扑
parent: "[[../POWER_SYSTEMS_Guideline]]"
order: 7
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/power
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/POWER_SYSTEMS_Guideline.md"
source_anchors: []
---

## P-9 冗余结构与拓扑 (Redundancy & Topology)

### 冗余结构等级

| 等级 | 说明 |
|------|------|
| **N** | 无冗余 |
| **N+1** | 标准冗余 |
| **2N** | 完全双路冗余 |

> Power Zone 可选 N+1 或 2N（需要额外的 Switchgear，成本增加）。IT Zone 和 Cooling Zone 不提供 N+1/2N 冗余。详见 [[PRINCIPLE_Guideline#§1.5 Zone 冗余规则]]。

### Zone 冗余约束

| Zone | N+1 | 2N |
|------|-----|----|
| **IT Zone** | ❌ 不提供 | ❌ 不提供 |
| **Cooling Zone** | ❌ 不提供 | ❌ 不提供 |
| **Power Zone** | ✅ 允许（需额外 Switchgear） | ✅ 允许（需额外 Switchgear） |
| **Network Zone** | ✅ 链路与设备级冗余 | 视项目需求 |

> **关键**: 客户询问 N+1/2N 冷却或 IT 冗余时，**必须上报 ATS 而非自行承诺**。

### 拓扑

Power Zone 与 IT Zone 标准拓扑：
- `Grid → BESS → IT Zone`（BESS 串联主供电路径，详见 [[#P-8 BESS 选型与 DG 对比|§P-8]]）
- `Grid + ATS + DG`（DG 并联备用电源）
- `Grid → BESS → IT Zone` 或 `Grid + ATS + DG`

> Zone 间物理连接示意见 [[PRINCIPLE_Guideline#§3 Zone 架构速查]]。

---

### 引用 / References

本文件是 SOUL.md 和 PRINCIPLES.md 的补充文件。
所有 Agent 在进行电力相关沟通时，必须引用本文件。
Key Matrix 中 Power Engineer 的必读章节见 [[PRINCIPLE_Guideline#§4 Key Matrix — Agent × 场景 必读章节矩阵]]（场景 S4）。
