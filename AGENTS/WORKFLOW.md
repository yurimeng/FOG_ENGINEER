---
tags:
  - #workspace/engineer
  - #type/process
  - #process/workflow
  - #system/feis
---

# Engineering Workspace Workflow / 工程工作流总览

Document Version: v2.0
Source: Works_Public/PROCESS/WORKFLOW/WORKFLOW.md（2026-04-10 归档）
Last Updated: 2026-03-10

> **加载说明 / Loading Note**：本文档定义 Engineer Workspace 的整体工作流程，描述不同 Agent 与 Process 如何协同，将客户需求转化为完整的基础设施方案。加载本文件前，必须先阅读 [[PRINCIPLES]]。

---

# 1 工作流阶段 / Workflow Stages

工程工作流程分为 **7 个阶段**：

| Stage | 名称 EN | 名称 CN | 负责 Agent | 主要 Process | 输出 |
|-------|--------|--------|-----------|-------------|------|
| 1 | Lead Qualification | 销售机会筛选 | AM | [[PROCESS/AM/Lead Qualification Process]] | 合格项目机会 |
| 2 | Customer Discovery | 客户需求发现 | AM | [[PROCESS/AM/Customer Discovery Process]] | 客户需求记录 |
| 3 | Requirement Structuring | 需求结构化 | AM | [[PROCESS/AM/Requirement Brief Process]] | 客户需求摘要 |
| 4 | Architecture Design | 架构设计 | ATS | [[PROCESS/ATS/Requirement Analysis]] | 架构蓝图 |
| 5 | Engineering Design | 工程设计 | ATS + Specialists | Specialist Guideline + PROCESS | 工程设计方案 |
| 6 | Governance Review | 工程审查 | Compliance Officer + Risk Auditor | Compliance_Guideline + Risk_Guideline | 审核通过的工程方案 |
| 7 | Proposal Generation | 方案输出 | ATS | [[PROCESS/ATS/Proposal Generation Process]] | 客户技术方案（不含价格） |

---

# 2 阶段详情 / Stage Details

## Stage 1 — Lead Qualification（销售机会筛选）

| 项目 | 内容 |
|------|------|
| 负责 | AM |
| Process | [[PROCESS/AM/Lead Qualification Process]] |
| 目标 | 判断该项目是否值得投入资源 |
| 输出 | Qualified Opportunity（合格项目机会） |

---

## Stage 2 — Customer Discovery（客户需求发现）

| 项目 | 内容 |
|------|------|
| 负责 | AM |
| Process | [[PROCESS/AM/Customer Discovery Process]] |
| 目标 | 理解客户需求和限制条件 |
| 输出 | Customer Requirement Notes（客户需求记录） |

---

## Stage 3 — Requirement Structuring（需求结构化）

| 项目 | 内容 |
|------|------|
| 负责 | AM |
| Process | [[PROCESS/AM/Requirement Brief Process]] |
| 目标 | 将客户需求整理为结构化需求文档 |
| 输出 | Customer Requirement Brief（客户需求摘要） |

---

## Stage 4 — Architecture Design（架构设计）

| 项目 | 内容 |
|------|------|
| 负责 | ATS |
| Process | [[PROCESS/ATS/Requirement Analysis]] |
| 目标 | 确定最优基础设施架构 |
| 输出 | Architecture Blueprint（架构蓝图） |

ATS 进行架构选型后，通过 [[PROCESS/ATS/Collaboration Process]] 向各专家分派任务。

---

## Stage 5 — Engineering Design（工程设计）

| 项目 | 内容 |
|------|------|
| 负责 | ATS + Engineering Specialists |
| Agent | Power Engineer / Cooling Engineer / Layout Planner / Cost Architect |
| Process | Specialist Guideline（各自领域 Guideline）+ PROCESS |
| 目标 | 形成完整工程方案 |
| 输出 | Engineering Design Package（工程设计方案） |

### 专家分派规则

| 触发条件 | 所需专家 |
|---------|---------|
| 高功率密度 | Cooling Engineer + Power Engineer |
| 单市电接入点 | Power Engineer |
| 复杂部署/空间约束 | Layout Planner |
| ESG / 城市优先 | Cost Architect |
| 偏远/严苛环境 | Compliance Officer + Risk Auditor |
| 全面架构审查 | 全部专家 |

---

## Stage 6 — Governance Review（工程审查）

| 项目 | 内容 |
|------|------|
| 负责 | Compliance Officer / Risk Auditor |
| Process | Compliance_Guideline / Risk_Guideline |
| 目标 | 确保方案符合规范、可靠且可运维 |
| 输出 | Approved Engineering Solution（审核通过的工程方案） |

---

## Stage 7 — Proposal Generation（方案输出）

| 项目 | 内容 |
|------|------|
| 负责 | ATS |
| Process | [[PROCESS/ATS/Proposal Generation Process]] |
| 目标 | 生成客户技术方案（仅配置，不含价格） |
| 输出 | 客户技术方案（IT负载、整体电力负荷、产品型号、PUE范围、冗余等级） |

> ⚠️ **禁止输出任何价格、成本估算或报价。参见 [[PRINCIPLES]] Principle 7 — NO PRICE。**

---

# 3 决策权威 / Decision Authority

| 层级 | 权威说明 |
|------|---------|
| **ATS** | 架构权威，最终技术决策 |
| **Engineering Specialists** | 专业领域建议，ATS 整合后生效 |
| **Compliance Officer** | 可否决不合规设计 |
| **Risk Auditor** | 风险不可接受时，可建议重新设计 |

最终方案必须平衡：可靠性、合规性、运维可行性、成本效率。（参见 [[PRINCIPLES]] Principle 9 — Decision Priority）

---

# 4 工作流图 / Workflow Diagram

```
Client
  │
  ▼
┌─────────────────────────────────────┐
│ Stage 1-3: AM                       │
│ Lead Qualification                   │
│ Customer Discovery                   │
│ Requirement Structuring              │
└───────────────┬─────────────────────┘
                ▼
┌─────────────────────────────────────┐
│ Stage 4: ATS                         │
│ Architecture Design                  │
│ Specialist Delegation                │
└───────────────┬─────────────────────┘
                ▼
┌─────────────────────────────────────┐
│ Stage 5: ATS + Specialists           │
│ Engineering Design                  │
│ Power / Cooling / Layout / Cost     │
└───────────────┬─────────────────────┘
                ▼
┌─────────────────────────────────────┐
│ Stage 6: Governance Review           │
│ Compliance Officer + Risk Auditor    │
└───────────────┬─────────────────────┘
                ▼
┌─────────────────────────────────────┐
│ Stage 7: ATS                         │
│ Proposal Generation（不含价格）       │
└───────────────┬─────────────────────┘
                ▼
              Client
```
