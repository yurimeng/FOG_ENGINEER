---
tags:
  - #workspace/engineer
  - #type/version
  - #system/feis
  - #MDC
---
# Workspace Version

Workspace: Engineer Workspace
Product: Fog Computing Engineering AI
Version: v1.6.0
Release Date: 2026-04-10
Status: Active Development

Reference backup: ../KB_backup_20260409_v1.5.0

---

## v1.6.0 — Obsidian CLI 项目管理规范 (2026-04-10)

### 重大变更：项目文档管理强制使用 Obsidian CLI

**变更背景：** 原 Agent 直接读写项目文档，导致 INDEX 同步不一致、数据难以追踪。

### 新增文件

| 文件 | 类型 | 说明 |
|------|------|------|
| `Projects/INDEX.md` | NEW | 项目索引，包含必填字段状态表和项目总览 |
| `Market/` | NEW | 市场报告和博客草稿目录 |

### 核心规则新增

| 规则 | 位置 | 说明 |
|------|------|------|
| Obsidian CLI 强制使用 | `TOOLS.md` Section 8 | 读取+写入项目文档必须通过 CLI |
| MANDATORY RULES | `AGENTS/AM.md` | 5条强制规则，含 CLI 使用规范 |
| MANDATORY RULES | `AGENTS/ATS.md` | 3条强制规则，含 CLI 使用规范 |
| 必填字段清单 | `AGENTS/AM.md` Section 3.5.1 | 11个必填字段定义 |
| 缺失字段提醒机制 | `AGENTS/AM.md` Section 3.5.2 | AM 必须定期检查并跟进 |

### 项目必填字段规范

每个 `Project_Record.md` 必须包含：

| 字段 | 说明 | 必须/可选 |
|------|------|----------|
| 最终用户 | End User | 必须 |
| EPC | 工程承包商 | 如有 |
| 投资方 | Investor | 如有 |
| 中间人 | Intermediary | 如有 |
| 部署地点 | Location | 必须 |
| 项目进度 | Stage | 必须 |
| 规模 | Scale (IT Load) | 必须 |
| 部署方式 | Indoor/Outdoor | 必须 |
| 电力情况 | Power (可链接飞书) | 必须 |
| 最后交流时间 | Last Contact Date | 必须 |
| 最后交流进度 | Last Progress | 必须 |

### 项目进度阶段定义

```
Lead → Qualification → Technical Discussion → NDA → TS → QUOTE → Contract → Pay → Closed-Won/Lost
```

### 文件更新清单

| 文件 | 变更内容 |
|------|---------|
| `TOOLS.md` | 新增 Section 8 — Obsidian CLI 强制规则 |
| `AGENTS/AM.md` (v1.5) | 新增 MANDATORY RULES；必填字段；缺失提醒机制 |
| `AGENTS/ATS.md` (v1.5) | 新增 MANDATORY RULES；引用 TOOLS Section 8 |
| `Projects/INDEX.md` | **新建** — 项目索引含状态表和模板 |
| `Projects/Simple Mining/Project_Record.md` | 模板升级，新增必填字段状态表 |
| `Projects/Crucible/Project_Record.md` | 模板升级，新增必填字段状态表 |
| `README.md` | 完整重写，同步目录结构；新增第十二节项目管理规则 |

### Obsidian CLI 命令

```bash
# 读取
obsidian-cli run --task read --note "Works_Public/Projects/[项目名]/Project_Record.md"
obsidian-cli run --task read --note "Works_Public/Projects/INDEX.md"

# 写入
obsidian-cli run --task update --note "Works_Public/Projects/[项目名]/Project_Record.md"
obsidian-cli run --task update --note "Works_Public/Projects/INDEX.md"
```

### 市场文档路径

| 文档 | 路径 |
|------|------|
| 市场报告 | `Works_Public/Market/Market_Report.md` |
| 博客草稿 | `Works_Public/Market/Blog_Draft.md` |

---

## v1.5.0 — New Product: AC45 45ft Immersion Container (2026-04-09)

### 新增产品：AC45

**AC45 — All-In-One Immersion Container（45ft，UL Compliant）**

AC45 是 45ft 浸没式液冷集装箱，IT 容量 400kW（与 AC40 相同），核心差异：

| 差异项 | AC45 | AC40 | DC45 |
|--------|------|------|------|
| 集装箱规格 | **45ft** | 40ft | 45ft |
| UPS 放置 | **内置（专用电力舱）** | **外置（客户自备）** | 内置 |
| UPS 电池放置 | 内置 | **外置（客户自备）** | 内置 |
| UPS 电池后备时间 | **~20 分钟** | ~10 分钟（客户自备）| ~8 分钟 |
| UL 合规 | **✅ 是** | ❌ 否 | ✅ 是 |

### 重要更正：UPS 状态

> **⚠️ 本次更新同步更正了 AC40 UPS 状态的错误描述。**
> - **AC40：UPS 及 UPS 电池外置（客户自备）**，AC40 本体不含 UPS
> - **AC45：UPS 及 UPS 电池内置**于专用电力舱，UL 合规
> - **DC45：UPS 及 UPS 电池内置**，UL 合规

### AC45 核心参数

| 项目 | 参数 |
|------|------|
| IT 容量 | 400kW（8×A32 浸没槽）|
| 冷却类型 | 浸没式 |
| UPS | EATON 9395XR-600（4×150kW = 600kW）|
| UPS 放置 | 内置（专用电力舱，UL 合规）|
| UPS 电池 | 2×93LiG2，约 20 分钟后备（内置）|
| 合规 | UL 认证 |

> ⚠️ **UPS 电池 vs BESS 电池：** 本次更新全线增加了 UPS 电池与 BESS 电池的区分说明。UPS 电池（93LiG2）= 分钟级瞬时切换后备；BESS = 小时级独立储能系统，两者完全不同。

### 更新的关联文档

| 文件 | 变更内容 |
|------|---------|
| `KB/PRODUCTS_AC45.md` | **新建**，完整产品文档，含与 AC40/DC45 对比表 |
| `KB/3RD-PARTY/3rd Party List.md` | UPS 对比表新增 AC45 行，含后备时间列 |
| `README.md` | 产品速查表新增 AC45 行；目录树新增 PRODUCTS_AC45.md；禁止事项补充 AC45 |
| `VERSION.md` | 新增 v1.5.0 版本记录 |
| `KB/PRODUCTS_AC40.md` | 补充 AC45 vs AC40 vs DC45 三方对比 |
| `KB/PRODUCTS_DC45.md` | 补充 AC45 vs DC45 关系描述 |
| `KB/PRODUCTS_A32.md` | 关系表补充 AC45 |
| `KB/PRODUCTS_MDC.md` | IT Zone 表格补充 AC45；冷却 Zone 配置补充 AC45 |

### 选型原则更新

- AC40 vs AC45 选型：优先 AC40（成本/尺寸更低）；需要 UL 合规 → 选择 AC45
- AC45 冷却架构与 AC40 完全一致（Hybrid Cooling System）
- AC45 电力架构：9395XR-600 + 2×93LiG2，置于专用电力舱

---

## v1.4.0 — KB Structure Refactor: Guideline + Product Docs (2026-04-09)

### 目录结构重构：Guideline + 产品文档体系

**变更背景：** Agent 读取第三方 KB 的标准顺序为：3rd Party List → Guideline → 产品文档。原结构中 COOLING/NETWORK 类别未拆分设计原则与产品文档，结构不清。

### 新增文件

| 文件 | 类型 | 说明 |
|------|------|------|
| `COOLING/COOLING_SYSTEM_Guideline.md` | NEW Guideline | 冷却系统设计原则：架构分类（DX/螺杆/磁悬浮/热泵）、温度策略、IT Zone 匹配规则 |
| `NETWORK/NETWORK_Guideline.md` | NEW Guideline | 网络设计原则：三层架构、IB/ROCE 策略、带内/带外管理、安全设计 |
| `UPS/UPS_EATON_9395XR.md` | NEW（迁移）| Buildin/ → UPS/，路径更新 |

### 文件重构

| 文件 | 变更内容 |
|------|---------|
| `COOLING/DRYCOOL_with_DX.md` | 移除设计原则内容，保留产品方案参数 |
| `COOLING/COOLING_SYSTEM_SOLUTION.md` | **已删除**（内容已迁移至 Guideline + 各产品文档）|
| `NETWORK/PRODUCTS_NETWORK.md` | 重构为纯产品文档（引澜布线系统）|
| `NETWORK/AC40_NETWORK_Guideline.md` | 转为引澜产品参考文档 |
| `BESS/POWER_SYSTEMS_Guideline.md` | 标题统一为 "Guideline" 格式；BESS 产品改为 wiki-link；tag 改为 `guideline` |
| `3rd Party List.md` | 全面重写 V1.3；Guideline 引用规则明确化；各子目录结构同步更新 |

### 冷却系统重大规则更新

| 规则 | 变更 |
|------|------|
| **A32 纯干冷例外** | A32 独立部署在环境 <28°C 时允许纯干冷器（PUE 可低至 1.03）；AC40/DC45 及 A32 在集装箱内部署时仍禁止纯干冷 |
| **温度阈值统一** | 所有文件统一使用 ≥28°C 作为 DX 强制启动阈值 |
| **架构类型扩展** | 新增螺杆压缩机方案（≥300kW）和磁悬浮压缩机方案（能效优先场景）|

### 涉及文件清单

- README.md：KB 目录树更新；KB Agent 引用规则写入 BOOTSTRAP 说明；A32 例外规则写入禁止事项
- VERSION.md：本版本记录
- 3rd Party List.md → V1.3
- PRODUCTS_AC40.md：冷却部分 → 指向新 Guideline；UPS 链接 → UPS/
- PRODUCTS_DC45.md：冷却部分 → 指向新 Guideline；UPS 链接 → UPS/
- PRODUCTS_A32.md：明确"独立部署 vs 集装箱部署"区分；A32 例外规则写入产品文档
- PRODUCTS_MDC.md：冷却参考链接 → 新 Guideline
- BESS/POWER_SYSTEMS_Guideline.md：标题/格式/BESS wiki-link 全部更新
- Buildin/ → UPS/：目录重命名，UPS_EATON_9395XR.md 迁移完成

### Agent 验证结果

- 3-layer 导航流程正确（3rd Party List → Guideline → Product）
- 无 broken link，所有 wiki-link 指向有效文件
- 三个 Guideline 标题格式统一，tag 一致

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

### 交付周期 — 标准值修正（2026-05-22）
- 旧值：约195-305天（30天合同+90-180天制造+45-50天海运+30-45天部署）
- 新值：约185-230天（现场勘测15天+商务准备15天+生产制造90-120天+运输45-60天+部署安装10-20天）
- 涉及文件：所有含交付周期的文档（见变更清单）
- 原则：现场勘测和商务准备各占15天；生产制造90-120天；运输45-60天；部署安装10-20天

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
| 产品 | IT容量 | UPS型号 | UPS放置 | UPS电池后备 | UL | PUE |
|------|--------|---------|---------|-----------|-----|-----|
| A32 | 45–50kW | 外置 | 外置（客户自备）| 外置 | — | ~1.03–1.12 |
| AC40 | 400kW | 9395XR-600（4×150kW）| 外置（客户自备）| 2×93LiG2（~10min，客户自备）| ❌ | ~1.02–1.08（低温）/ ~1.15–1.20（高温）|
| AC45 | 400kW | 9395XR-600（4×150kW）| 内置（专用电力舱）| 2×93LiG2（~20min）| ✅ | ~1.02–1.08（低温）/ ~1.15–1.20（高温）|
| DC45 | 1240kW | 9395XR-1500（10×150kW）| 内置 | 3×93LiG2（~8min）| ✅ | ~1.07–1.15（低温）/ ~1.25–1.35（高温）|

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

# Standing Rules

> ⚠️ **本节为永久性规则，所有参与 Works_Public 维护的人员必须遵守。**

## SR-001：更新同步规则

**规则：** 任何对 Works_Public 知识库的更新（新增、修改、删除文件），**必须同步完成以下两件事**：

1. **更新 `README.md`**
   - 目录树结构（若涉及 KB/ 目录变更）
   - 产品信息（若涉及产品参数变更）
   - 禁止事项（若涉及新增禁止规则）
   - 其他受影响的描述性内容

2. **更新 `VERSION.md`**
   - 版本号递增（按 Semantic Versioning 规则）
   - 在 Version History 中新增变更记录条
   - 记录内容须包含：变更日期、涉及文件清单、变更摘要

**违规后果：** 未同步更新的变更视为不完整，Agent 在执行一致性检查时有权要求补充。

**生效日期：** 2026-04-09（v1.4.0 起生效）

---



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

---

*Document Version: v1.1 | Last Updated: 2026-04-12*
