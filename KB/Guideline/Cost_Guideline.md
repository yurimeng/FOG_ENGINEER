---
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/cost
  - #MDC
---
# Cost Guideline / 成本技术指南

> **执行摘要**:本文件规定 Cost Architect 在 MDC / 边缘 DC 预销售场景下的成本建模方法、CAPEX 分类、架构成本对比、成本优化优先级与 Edge 经济性。所有商业定价由客户经理负责,本 Guideline 仅输出工程级分析与对比。章节 ID 体系与跨 Agent 引用规则见 [[PRINCIPLE_Guideline#§8 章节 ID 一致性表]]。

## 文档导航

| 块 | 主题 | 包含章节 |
|----|------|---------|
| [[01_K1_K2_Method_Categories]] | K-1/K-2 成本建模方法与 CAPEX 分类 | K-1, K-2 |
| [[02_K3_Architecture_Comparison]] | K-3 架构成本对比 | K-3 |
| [[03_K4_K5_Priority_Edge]] | K-4/K-5 成本优化优先级与边缘部署经济 | K-4, K-5 |
| [[04_K6_Workflow]] | K-6 工作流集成 | K-6 |

---

## 1. 成本建模方法与 CAPEX 分类
![[01_K1_K2_Method_Categories]]

## 2. 架构成本对比
![[02_K3_Architecture_Comparison]]

## 3. 成本优化优先级与边缘部署经济
![[03_K4_K5_Priority_Edge]]

## 4. 工作流集成
![[04_K6_Workflow]]

---

## Changelog

- **v1.2 — 2026-06-17**
  - 结构拆分。原 6 个 H2 章节拆分为 4 个独立块文件,存放于 `_blocks/Cost_Guideline/`。保留全部 K-1 ~ K-6 章节 ID 与交叉引用。frontmatter 不变。
- **v1.1 — 2026-06-05**
  - 章节 ID 全面对齐 [[PRINCIPLE_Guideline#§8 章节 ID 一致性表]]:新增 K-1 ~ K-6 锚点。
  - 顶部新增"速查 / Quick Reference"块与"章节速查 / Section Index"表,统一指向 [[PRINCIPLE_Guideline]]。
  - 元数据表(Version / Last Updated / Source)从脚注迁移至顶部。
  - 在 §K-3、§K-4、§K-5、§K-6 中加入交叉链接。
  - §K-6 工作流整合至 Key Matrix 节点序列。
  - 文件末尾新增 Changelog 段,符合 CLAUDE.md §6 规则。
  - 内容、文字与所有技术性条目保持原样未改;未新增任何价格或商业化数据。
