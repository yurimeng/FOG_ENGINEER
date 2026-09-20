---
title: "03_File_Index — §2 文件清单与章节 ID 体系 + §3 Zone 架构速查"
parent: "[[PRINCIPLE_Guideline]]"
order: 3
tags:
  - #workspace/engineer
  - #type/principle
  - #product/general
  - #architecture
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/PRINCIPLE_Guideline.md"
source_anchors:
  - "§2"
  - "§3"
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
| **A32** | 单柜 | 45–50 kW | 内置 | ~320 kW Hybrid ^mdc-59a7410aa4 |
| **AC40** | 40 ft 容器 | 400 kW | 外置（客户自备，9395XR-600） | ~600 kW Hybrid ^mdc-91947176ca |
| **AC45** | 40 ft 容器 | 400 kW | 内置（9395XR-600） | ~600 kW Hybrid ^mdc-ae8cc1b119 |
| **DC45** | 45 ft 容器 | 1240 kW | 内置（9395XR-1500） | ~1200 kW Hybrid ^mdc-61fe654028 |

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
