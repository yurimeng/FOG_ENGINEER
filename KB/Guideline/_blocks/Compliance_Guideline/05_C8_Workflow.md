---
title: "C-8 工作流集成"
parent: "[[Compliance_Guideline]]"
order: 5
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/compliance
  - #compliance
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/Compliance_Guideline.md"
source_anchors:
  - "C-8 工作流集成"
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
