---
tags:
  - #workspace/engineer
  - #type/index
  - #system/feis
---

# Works_Public / 工作空间索引

> **Engineer Workspace — Fog Computing Pre-Sales Engineering Agent System**
>
> 面向模块化数据中心（MDC）的售前工程 Agent 系统，用于技术方案设计、电力与冷却系统选型、产品配置输出（不含价格）、客户技术管理与风险审查。

---

## 目录结构 / Directory Tree

```
Works_Public/
│
├── index.md                    ← 本文件 / This file
├── README.md                   ← 系统总览 / System Overview
├── SOUL.md                     ← 系统灵魂与愿景 / System Soul & Vision
├── PRINCIPLES.md               ← 工程原则（最高准则）/ Engineering Principles (Highest Authority)
├── IDENTITY.md                 ← 系统身份定义 / System Identity
├── VERSION.md                  ← 版本记录 / Version History
├── HEARTBEAT.md               ← 健康检查机制 / Health Check
├── USER.md                    ← 用户信息 / User Profile
├── AGENTS.md                  ← Agent 角色总览 / Agent Roles Overview
│
├── AGENTS/                     ← 角色定义文件（8个）/ Agent Definition Files
│   ├── WORKFLOW.md             ← 工作流总览 / Workflow Overview
│   ├── AM.md                   ← Account Manager / 客户经理
│   ├── ATS.md                  ← Architecture & Technical Sales / 架构技术销售
│   ├── Power Engineer.md       ← 电力工程师 / Power Engineer
│   ├── Cooling Engineer.md     ← 冷却工程师 / Cooling Engineer
│   ├── Layout Planner.md       ← 布局规划师 / Layout Planner
│   ├── Cost Architect.md      ← 成本架构师 / Cost Architect
│   ├── Compliance Officer.md   ← 合规官 / Compliance Officer
│   └── Risk Auditor.md        ← 风险审计师 / Risk Auditor
│
├── KB/                         ← 知识库 / Knowledge Base
│   ├── Guideline/              ← 各领域技术指南（6个）/ Domain Technical Guidelines
│   │   ├── COOLING_SYSTEM_Guideline.md
│   │   ├── POWER_SYSTEMS_Guideline.md
│   │   ├── Compliance_Guideline.md
│   │   ├── Cost_Guideline.md
│   │   ├── Layout_Guideline.md
│   │   └── Risk_Guideline.md
│   │
│   ├── 3RD-PARTY/             ← 第三方产品文档 / Third-Party Product Documents
│   │   ├── 3rd Party List.md   ← 第三方供应商总览 / Supplier Directory
│   │   ├── BESS/               ← 储能系统 / Battery Energy Storage
│   │   ├── COOLING/            ← 冷却系统 / Cooling Systems
│   │   ├── NETWORK/            ← 网络系统 / Network Systems
│   │   └── UPS/                ← 不间断电源 / UPS
│   │
│   ├── PRODUCTS_*.md           ← 产品手册（4型）/ Product Manuals
│   │   ├── PRODUCTS_MDC.md     ← 模块化数据中心总览 / MDC Overview
│   │   ├── PRODUCTS_AC40.md    ← AC40 产品手册 / AC40 Product Manual
│   │   ├── PRODUCTS_AC45.md    ← AC45 产品手册 / AC45 Product Manual
│   │   └── PRODUCTS_DC45.md    ← DC45 产品手册 / DC45 Product Manual
│   │
│   └── BOM/                    ← 物料清单 / Bill of Materials
│       └── DC45_MDC_BOM.md     ← DC45 物料清单 / DC45 BOM
│
├── PROCESS/                    ← 流程定义 / Process Definitions
│   ├── AM/                     ← 客户经理流程 / Account Manager Processes
│   │   ├── Lead Qualification Process.md
│   │   ├── Customer Discovery Process.md
│   │   ├── Requirement Brief Process.md
│   │   └── ATS Handoff Process.md
│   ├── ATS/                    ← 架构师流程 / Architecture Processes
│   │   ├── Requirement Analysis.md
│   │   ├── Collaboration Process.md
│   │   └── Proposal Generation Process.md
│   └── WORKFLOW/               ← 通用工作流 / General Workflows
│       └── WORKFLOW.md
│
├── Projects/                   ← 项目记录 / Project Records
│   ├── INDEX.md                ← 项目总索引 / Project Index
│   ├── BTCT/                   ← BTCT 项目
│   ├── Bitdeer/               ← Bitdeer 项目
│   ├── Crucible/              ← Crucible 项目
│   ├── PQTech/                ← PQTech 项目
│   ├── RiCloud/               ← RiCloud 项目
│   ├── 8th_Power/             ← 8th_Power 项目
│   └── Simple_Mining/          ← Simple_Mining 项目
│
├── Reference Architecture/      ← 参考架构 / Reference Architectures
│   ├── EDGE_INFERENCE_IMMERSION_0.5MW.md   ← 浸没式 0.5MW 参考架构
│   └── EDGE_INFERENCE_DLC_1.2MW.md          ← 直冷液冷 1.2MW 参考架构
│
├── Market/                     ← 市场资料 / Market Intelligence
│   ├── Market_Report.md        ← 市场周报 / Weekly Market Report
│   └── Blog_Draft.md           ← 博客草稿 / Blog Drafts
│
└── TOOLS/                      ← 工具说明 / Tool Documentation
    ├── TOOLS.md                ← 工具总览 / Tools Overview
    ├── CRM_WORKFLOW.md         ← 客户档案管理规则 / Customer File Management Rules
    ├── KB_ACCESS.md            ← 知识库访问指南 / KB Access Guide
    ├── QUOTE_ENGINE.md         ← 报价引擎（仅供商务团队）/ Quote Engine
    ├── CAD_GUIDELINES.md       ← CAD 制图规范 / CAD Guidelines
    └── NOTION_WORKFLOW.md      ← Notion 工作流 / Notion Workflow
```

---

## 核心文件说明 / Core Files

| 文件 | 说明 |
|------|------|
| [[PRINCIPLES]] | **最高准则**。所有 Agent 必须首先加载并遵守，包含 12 条工程原则（含 KB 访问规范、客户档案管理、参考架构优先）|
| [[SOUL]] | 系统灵魂与愿景。定义 Engineer Workspace 的设计哲学和核心理念 |
| [[AGENTS]] | 角色索引。指向 `/AGENTS/` 目录下所有角色定义文件 |
| [[README]] | 系统总览。功能定位、11条原则、Agent体系、工作流、禁止事项一览 |
| [[IDENTITY]] | 系统身份。定义 AI Agent 在执行工程任务时的人格与行为准则 |
| [[AGENTS/WORKFLOW]] | 工作流总览。7 阶段工程工作流和决策权威层级 |
| [[PROCESS/WORKFLOW/WORKFLOW]] | 原始流程文件归档（参考） |

---

## 角色快速入口 / Agent Quick Access

> 加载角色时，必须先阅读 [[PRINCIPLES]]，再阅读 [[AGENTS/WORKFLOW]]，最后加载对应角色文件。

| 角色 | 文件 | Guideline |
|------|------|----------|
| 工程工作流总览 | [[AGENTS/WORKFLOW]] | — |
| 客户经理 / AM | [[AGENTS/AM]] | 按需读取 Guideline |
| 架构技术销售 / ATS | [[AGENTS/ATS]] | 读取 `./PROCESS/ATS/` 流程 + 6 个 Guideline |
| 电力工程师 / Power Engineer | [[AGENTS/Power Engineer]] | `/KB/Guideline/POWER_SYSTEMS_Guideline` |
| 冷却工程师 / Cooling Engineer | [[AGENTS/Cooling Engineer]] | `/KB/Guideline/COOLING_SYSTEM_Guideline` |
| 布局规划师 / Layout Planner | [[AGENTS/Layout Planner]] | `/KB/Guideline/Layout_Guideline` |
| 成本架构师 / Cost Architect | [[AGENTS/Cost Architect]] | `/KB/Guideline/Cost_Guideline` |
| 合规官 / Compliance Officer | [[AGENTS/Compliance Officer]] | `/KB/Guideline/Compliance_Guideline` |
| 风险审计师 / Risk Auditor | [[AGENTS/Risk Auditor]] | `/KB/Guideline/Risk_Guideline` |

---

## 产品线 / Product Line

| 产品 | 说明 | 手册 |
|------|------|------|
| **MDC** | 模块化数据中心总览 | [[PRODUCTS_MDC]] |
| **AC40** | 交流 40kW 高密度计算节点 | [[PRODUCTS_AC40]] |
| **AC45** | 交流 45kW 高密度计算节点 | [[PRODUCTS_AC45]] |
| **DC45** | 直流 45kW 直冷液冷节点 | [[PRODUCTS_DC45]] |

---

## 知识库结构 / Knowledge Base Structure

### Guideline 层（权威技术依据）

所有技术决策必须首先查阅对应 Guideline：

| Guideline | 领域 | 关键内容 |
|-----------|------|---------|
| `COOLING_SYSTEM_Guideline` | 冷却系统 | 冷却选型、干冷器+DX、液冷、热管理 |
| `POWER_SYSTEMS_Guideline` | 电力系统 | BESS vs 柴油机、UPS 选型、电网集成 |
| `Compliance_Guideline` | 合规审查 | UL/CSA/IEC/NFPA 标准、储能合规 |
| `Cost_Guideline` | 成本分析 | CAPEX 分类、架构成本对比、优化优先级 |
| `Layout_Guideline` | 物理布局 | 布局原则、通道净空、线缆敷设 |
| `Risk_Guideline` | 风险审计 | 四级风险、SPOF 识别、工程红旗 |

### 产品层（选型依据）

详细产品信息见 [[PRODUCTS_MDC]]。

```
KB/3RD-PARTY/
├── BESS/      ← 储能系统
├── COOLING/   ← 冷却设备
├── NETWORK/   ← 网络设备
└── UPS/       ← 不间断电源
```

---

## 协作流程 / Collaboration Flow

详细协作流程和 7 阶段工作流说明，参见 [[AGENTS/WORKFLOW]]。

---

## 关键约束 / Key Constraints

| 规则 | 说明 | 参考 |
|------|------|------|
| **NO PRICE** | 严禁提供任何价格数字、报价或成本估算 | Principle 7 |
| **IT Load vs Total Facility Load** | 必须区分两个负荷定义，不得混用 | Principle 8 |
| **Modular Only** | 严禁定制化。所有产品必须遵循 [[PRODUCTS_MDC]] | Principle 3 |
| **Obsidian CLI** | 所有项目文档操作必须使用 Obsidian CLI | Principle 10 |
| **客户档案管理** | 必须遵循 /TOOLS/CRM_WORKFLOW | Principle 11 |
| **ATS Integration** | 所有专家输出必须经 ATS 整合 | [[AGENTS/WORKFLOW]] |
