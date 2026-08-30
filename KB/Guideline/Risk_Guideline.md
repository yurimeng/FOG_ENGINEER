---
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/risk
  - #MDC
---
# Risk Guideline / 风险审计技术指南

> **执行摘要**:本文件定义 FOG 风险审计(Risk Auditor)的风险分级方法、SPOF 识别标准、工程红旗、负荷/运维/部署/扩展与成本风险评估框架,以及与 ATS 的工作流集成规则。跨文件总入口与执行合约见 [[PRINCIPLE_Guideline]];Agent × 场景必读矩阵见 [[PRINCIPLE_Guideline#§4 Key Matrix — Agent × 场景必读表]]。

## 文档导航

| 块 | 主题 | 包含章节 |
|----|------|---------|
| [[01_R1_R2_Classification_SPOF]] | R-1/R-2 风险分级与单点故障识别 | R-1, R-2 |
| [[02_R3_R4_RedFlags_Load]] | R-3/R-4 工程红旗与负荷定义风险 | R-3, R-4 |
| [[03_R5_R6_Operations_Deployment]] | R-5/R-6 运维与部署风险评估 | R-5, R-6 |
| [[04_R7_Scalability_Cost]] | R-7 扩展与成本风险 | R-7 |
| [[05_Workflow_Integration]] | 工作流集成 | — |

---

## 1. 风险分级与单点故障识别
![[01_R1_R2_Classification_SPOF]]

## 2. 工程红旗与负荷定义风险
![[02_R3_R4_RedFlags_Load]]

## 3. 运维与部署风险评估
![[03_R5_R6_Operations_Deployment]]

## 4. 扩展与成本风险
![[04_R7_Scalability_Cost]]

## 5. 工作流集成
![[05_Workflow_Integration]]

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.2 | 2026-06-17 | 结构拆分。原 7 个 H2 章节 + 工作流集成拆分为 5 个独立块文件,存放于 `_blocks/Risk_Guideline/`。保留全部 R-1 ~ R-7 章节 ID 与交叉引用。frontmatter 不变。 |
| v1.1 | 2026-06-05 | 结构规范化:章节 ID 对齐 [[PRINCIPLE_Guideline#§8 章节 ID 一致性表]] (R-1 风险分级方法 / R-2 单点故障识别 / R-3 工程红旗 / R-4 负荷定义风险 / R-5 运维风险评估 / R-6 部署风险评估 / R-7 扩展与成本风险);新增"速查"与"章节速查"索引;将原"Scalability Risk Analysis"与"Cost Risk Evaluation"合并至 R-7 扩展与成本风险;补充与 [[COOLING_SYSTEM_Guideline]]、[[POWER_SYSTEMS_Guideline]]、[[NETWORK_Guideline]]、[[Compliance_Guideline]]、[[Layout_Guideline]]、[[Cost_Guideline]] 及 [[PRINCIPLE_Guideline]] 的 [[#§ID 标题]] 交叉引用;Changelog 移至文件末尾。 |
| v1.0 | 2026-03-10 | 初始版本。源文件 `Works_Public/AGENTS/Risk Auditor.md`;包含 4 级风险分级、Power/Cooling/Control/Network SPOF 识别、6 类工程红旗、IT vs Total 负荷混淆、运维/部署/扩展/成本评估与工作流集成。 |
