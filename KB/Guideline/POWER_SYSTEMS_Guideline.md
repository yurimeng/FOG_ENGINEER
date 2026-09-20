---
tags:
  - #workspace/engineer
  - #type/reference
  - #domain/power
  - #MDC
---
# POWER_SYSTEMS_Guideline — 电力系统设计原则

| 字段 | 值 |
|------|-----|
| Document Version | v1.3 |
| Last Updated | 2026-06-05 |
| Source | FOG KB 内部 + Works_Public/Projects/Simple_Mining/DG vs BESS.md |

> 本文件为 Power Zone 设计与选型的权威 Guideline，覆盖 IT 负载/整体负荷定义、UPS / BESS / 柴油机选型、DG vs BESS 战略与技术对比。Power Engineer 在执行任何电力工作前必须先阅读本文件。

---

## 速查 / Quick Reference

电力系统 Guideline：定义 IT Load vs Total Facility Load、UPS/BESS/DG 选型、拓扑与冗余规则。入口见 [[PRINCIPLE_Guideline]]；场景必读章节见 [[PRINCIPLE_Guideline#§4 Key Matrix — Agent × 场景 必读章节矩阵]]；章节 ID 短码见 [[PRINCIPLE_Guideline#§8 章节 ID 一致性表]]。

---

## 章节速查 / Section Index

| ID | 标题 | 用途 |
|----|------|------|
| [[#P-1 IT 负载与整体电力负荷\|§P-1]] | IT 负载与整体电力负荷 | IT Load / Total Facility Load 精确定义、计算公式、典型问法 |
| [[#P-2 产品对照表\|§P-2]] | 产品对照表 | A32 / AC40 / AC45 / DC45 IT 与整体负荷、冷却功耗对照 ^mdc-8ae3566e97 |
| [[#P-3 关键规则\|§P-3]] | 关键规则 | 主动澄清、输出标注、不混用术语、Zone 关系 |
| [[#P-4 典型混淆场景\|§P-4]] | 典型混淆场景 | 客户常见"X MW"话术的判别与工程师动作 |
| [[#P-5 UPS 选型\|§P-5]] | UPS 选型 | EATON 9395XR 型号标准化、容量公式、UL 合规 |
| [[#P-6 UPS 电池技术对比\|§P-6]] | UPS 电池技术对比 | VRLA / Li-ion / 超级电容对比 |
| [[#P-7 柴油发电机选型\|§P-7]] | 柴油发电机选型 | DG 优势、顾虑、Standby/Prime rating、NFPA 110 |
| [[#P-8 BESS 选型与 DG 对比\|§P-8]] | BESS 选型与 DG 对比 | BESS 优势、Grid Curtailment、Demand Response、选型决策表 |
| [[#P-9 冗余结构与拓扑\|§P-9]] | 冗余结构与拓扑 | N / N+1 / 2N、Zone 冗余约束、Power Zone 拓扑 |

---

## 文档导航

| # | 块 | 用途 |
|---|----|------|
| 1 | §P-1 IT 负载与整体电力负荷 | IT Load / Total Facility Load 精确定义、计算公式、典型问法 |
| 2 | §P-2 产品对照表 + §P-3 关键规则 | A32/AC40/DC45 对照 + 4 条关键规则 ^mdc-3a23a9e0f7 |
| 3 | §P-4 典型混淆场景 + §P-5 UPS 选型 | 3 个混淆场景 + EATON 9395XR 标准化 |
| 4 | §P-6 UPS 电池技术 + §P-7 柴油发电机选型 | VRLA / Li-ion / 超级电容 + DG 4 顾虑 + NFPA 110 |
| 5 | §P-8 BESS 选型与 DG 对比（上）| BESS 优势 + Curtailment + Demand Response + Flexible Load |
| 6 | §P-8 BESS 选型决策 + 系统级对比（下）| 选型决策表 + 16 项系统级对比表 |
| 7 | §P-9 冗余结构与拓扑 | N/N+1/2N + Zone 约束 + 拓扑 + 引用 |

---

## 1. §P-1 IT 负载与整体电力负荷

![[01_P1_IT_vs_Total]]

## 2. §P-2 产品对照表 + §P-3 关键规则

![[02_P2_P3_Product_Rules]]

## 3. §P-4 典型混淆场景 + §P-5 UPS 选型

![[03_P4_P5_Confusion_UPS]]

## 4. §P-6 UPS 电池技术 + §P-7 柴油发电机选型

![[04_P6_P7_Battery_DG]]

## 5. §P-8 BESS 选型与 DG 对比（上）

![[05_P8_BESS_DG_Comparison]]

## 6. §P-8 BESS 选型决策 + 系统级对比（下）

![[06_P8_BESS_Selection_Decision]]

## 7. §P-9 冗余结构与拓扑

![[07_P9_Redundancy_Topology]]

---

## Changelog

> v1.3 变更（2026-06-05）：
> - 章节 ID 对齐 [[PRINCIPLE_Guideline#§8 章节 ID 一致性表]]，采用 P-1 ~ P-9 体系；
> - 新增 YAML frontmatter、Version/Last Updated/Source 元数据表、Quick Reference、Section Index；
> - 各节标题加 ID 前缀（§P-1 IT 负载与整体电力负荷 / §P-2 产品对照表 / §P-3 关键规则 / §P-4 典型混淆场景 / §P-5 UPS 选型 / §P-6 UPS 电池技术对比 / §P-7 柴油发电机选型 / §P-8 BESS 选型与 DG 对比 / §P-9 冗余结构与拓扑）；
> - 跨文件引用统一为 [[Filename#§ID 标题]] 形式，新增指向 [[PRINCIPLE_Guideline]] / [[COOLING_SYSTEM_Guideline#G-8 IT Zone 与冷却区匹配|COOLING_SYSTEM_Guideline §G-8]] / [[Risk_Guideline#R-4 负荷定义风险|Risk_Guideline §R-4]] / [[Compliance_Guideline#C-3 储能系统合规|Compliance_Guideline §C-3]] 的内部链接；
> - §P-9 整合原"§7 冗余结构"内容并补全 Zone 冗余约束表与拓扑段。

> v1.2 变更：合并原 KB/3RD-PARTY/BESS/POWER_SYSTEMS_Guideline 的技术选型详则（UPS 公式 / 电池技术 / 柴油机 / 冗余 / 系统对比表）；修正文件首行错误标题"POWER_LOAD.md"为正确的"POWER_SYSTEMS_Guideline"。
