---
tags:
  - #workspace/engineer
  - #type/version
  - #system/feis
---

# Workspace Version

Workspace: Engineer Workspace
Product: Fog Computing Engineering AI
Version: v1.1.0
Release Date: 2026-03-29
Status: Active Development

Reference backup: ../KB_backup_20260329_200742

---

# Version History

## v1.3.0 — Critical Corrections Round 4 (2026-03-29)

### IT Zone Redundancy — Fatal Error Fixed
- AC40/DC45 作为容器**无内部冗余设计**，不能通过增加服务器实现冗余
- UPS 模块内部 N+1（单模块故障不影响运行）≠ IT Zone 级别冗余
- IT Zone 冗余通过增加集装箱数量实现（系统级冗余）
- 涉及文件：PRODUCTS_AC40.md, PRODUCTS_DC45.md, PRODUCTS_MDC.md, Reference Architecture (both), DESIGN_GUIDELINE.md

### Cooling Naming — Hybrid Cooling System 统一命名
- "干冷器 + DX"（两个独立设备）→ "**Hybrid Cooling System**"（一个集成设备）
- 涉及文件：所有包含冷却描述的文件

### 交付周期 — 错误数字修正
- 错误：75-90天
- 正确：约195-305天（30天合同+90-180天制造+45-50天海运+30-45天部署）
- 涉及文件：USER.md, Reference Architecture (both)

## v1.2.0 — Product Information Unification (2026-03-29)

### Product Files Restructured
- PRODUCTS_AC40.md: 结构统一；UPS 型号更正为 9395XR-600；PUE 改为变量；新增 IT负载/整体电力负荷对照表
- PRODUCTS_DC45.md: 结构统一；UPS 型号更正为 9395XR-1500；PUE 改为变量；新增 IT负载/整体电力负荷对照表
- PRODUCTS_A32.md: 结构统一；PUE 改为变量；扩展逻辑补充完整；与 AC40/DC45 关系表
- PRODUCTS_MDC.md: 全面重写；新增标准配置参考（Small/Medium/Large）；冗余规则明确（IT Zone 无内部 N+1）；Power/Cooling Zone 标准配置

### Third-Party Products Unified
- UPS_EATON_9395XR.md: 全面重写；同时覆盖 9395XR-600（AC40）和 9395XR-1500（DC45）；电池配置表更新
- COOLING_SYSTEM_SOLUTION.md: 命名统一（"ACC" → "MDC Cooling Zone"）；结构统一；禁止纯干冷器规则强化
- DRYCOOL_with_DX.md: 命名统一；结构统一
- 3rd Party List.md: 全面重写；新增 Cooling Zone 标准配置；UPS 型号明确；供应商能力边界说明
- POWER_SYSTEMS_SOLUTION.md: UPS 型号引用更新（9395XR-600/1500）

### Reference Architecture Unified
- EDGE_INFERENCE_IMMERSION_0.5MW.md: 全面重写；标准输出模板；PUE 变量化；UPS 型号明确
- EDGE_INFERENCE_DLC_1.2MW.md: 全面重写；修正"DLC"非"immersion"；PUE 变量化；标准输出模板
- REFERENCE_ARCHITECTURE.md: 全面重写；新增速查表；引用规则强化

### Design Guideline Corrected
- AC40 IT容量：360kW → 400kW
- PUE：固定数字 → 变量（取决于环境温度）
- 删除 "HC45"（不存在的产品名）
- 删除"透明计算"成本估算相关内容（Principle 7）
- 删除 ROI/TCO 讨论要求（Principle 7）
- 强化不提供价格原则

### Key Numbers Now Standardized
| 产品 | IT容量 | UPS型号 | 电池后备 | PUE |
|------|--------|---------|---------|-----|
| A32 | 45–50kW | 外置 | 外置 | ~1.03–1.12 |
| AC40 | 400kW | 9395XR-600（4×150kW）| 2×93LiG2（~10min）| ~1.08–1.20 |
| DC45 | 1200kW | 9395XR-1500（10×150kW）| 3×93LiG2（~8min）| ~1.12–1.35 |

## v1.1.0 — Team Refactor (2026-03-29)

Core principle updates:
- Principle 7: NO PRICE — absolute prohibition on any price, cost estimate, or quotation
- Principle 8: IT Load vs Total Facility Load — mandatory clarification and dual-output rule
- New file: ./KB/POWER_LOAD.md (IT负载与整体电力负荷定义)

Agent updates:
- AGENTS.md: KB-only product portfolio rule added (A32/AC40/DC45/MDC only)
- AGENTS.md: "Do NOT educate clients" rule added
- AGENTS.md: Hard Boundaries section added (what we do NOT do)
- ATS.md: Configuration output format specified (no price figures)
- ATS.md: IT Load / Total Load clarification required in all outputs
- Cost Architect.md: Refocused from cost estimation to configuration specification
- Risk Auditor.md: Load definition risk added as risk category
- BOOTSTRAP.md: CONFIGURATION mode for pricing inquiries (redirects to AM)
- BOOTSTRAP.md: Price interception rule added

Process updates:
- Proposal Generation Process: Cost estimation removed, configuration spec added
- Capacity Planning Process: IT load and total facility load outputs separated
- Customer Requirement Analysis: Power demand clarification added
- Cooling Architecture Process: IT load vs total facility load reference added
- WORKFLOW.md: Proposal Stage renamed to "Configuration only — NO price"
- DECISION_TREE.md: KB-only portfolio constraint noted

## v1.0.0 — Initial Release
First structured release of the Engineering Workspace.

Includes:

Core System Files
- IDENTITY
- SOUL
- PRINCIPLES
- BOOTSTRAP
- HEARTBEAT

Agent Structure
- AM
- ATS
- Cooling Engineer
- Power Engineer
- Layout Planner
- Cost Architect
- Compliance Officer
- Risk Auditor

Knowledge Base
- A32
- AC40
- DC45
- MDC

Third Party Knowledge
- Cooling Systems
- Power Systems
- Networking
- UPS Eaton 9395XR

Process Libraries
- Pre-sales flow
- Client management
- Certification standards

Tools
- CAD Guidelines
- Notion Workflow
- Quote Engine

---

# Versioning Rules

Versioning follows Semantic Versioning.

Format:

MAJOR.MINOR.PATCH

MAJOR
Breaking architecture changes.

MINOR
New capabilities or modules added.

PATCH
Small improvements, bug fixes, documentation updates.

---

# Compatibility

This workspace is designed for:

OpenClaw Agent Framework

Recommended model capability:

- reasoning LLM
- tool calling
- document retrieval