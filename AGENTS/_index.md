---
tags:
  - #workspace/engineer
  - #type/agent-index
  - #product/general
  - #MDC
---
# FOG/AGENTS / _index

新 Agent 上线阅读入口总览。原 `AGENTS/index.md` 极简目录保留不动,本文件为导航层。

---

## 1 阅读顺序(Index-First 原则,6 步)

按此顺序依次阅读,可建立完整心智模型:

1. `/PRINCIPLES.md` — 顶层原则(NO PRICE / KB-only / IT vs Total Load 等)
2. `/AGENTS/WORKFLOW.md` — 端到端协作流(7 Stage)
3. `/AGENTS/<role>.md` — 本角色定义、I/O、边界
4. `/KB/Guideline/<domain>_Guideline.md` — 领域设计原则
5. `/KB/3RD-PARTY/3rd Party List.md` → 具体产品 doc
6. `/PROCESS/<role>/*.md` — 本角色执行 SOP

---

## 2 最小阅读清单(6 文件,~50 min)

| 步骤 | 文件 | 估计时间 |
|------|------|---------|
| 1 | `/PRINCIPLES.md` | 12 min |
| 2 | `/AGENTS/WORKFLOW.md` | 5 min |
| 3 | `/AGENTS/<role>.md` | 10 min |
| 4 | `/KB/Guideline/<domain>_Guideline.md` | 15 min |
| 5 | `/KB/3RD-PARTY/3rd Party List.md` | 5 min |
| 6 | `/PROCESS/<role>/*.md` | 5 min |
| **合计** | | **~50 min** |

---

## 3 Agent 角色矩阵(9 Agent I/O 边界)

| Agent | 输入 | 输出 | 关键边界 |
|-------|------|------|----------|
| AM | 客户原始沟通 | Customer Requirement Brief → ATS;Project Record;Market Intel | 不设计技术方案 |
| ATS | 客户需求 + RFI | 整合后架构(产品/IT Load/Total Load/PUE/冗余/扩展)→ AM | 不出价格;唯一对外输出 |
| Power Engineer | ATS 任务 | 电力架构/BESS/UPS/冗余/负荷 → ATS | UPS 由 IT Zone 固定 |
| Cooling Engineer | ATS 任务 | 冷却架构/热负荷/1:1 配对 → ATS | N only(不冗余) |
| Layout Planner | ATS 任务 | 容器布局/设备摆放/维护净空 → ATS | 1:1 空间配对 |
| Cost Architect | ATS 任务 | CAPEX 结构/相对成本对比 → ATS | 不出绝对价格 |
| Compliance Officer | ATS 任务 | PASS/CONDITIONAL/FAIL → ATS | 不可设计,持 veto |
| Risk Auditor | 整合架构 | 风险分级/SPOF/红旗 → ATS | 不可设计,Critical 阻断 |
| Market Researcher | 独立 | `/Market/*` 输出 | 独立运作,不参与技术决策 |

---

## 4 协作流图谱

```
Client
  ↓
AM (Stage 1-3: Lead Qual → Discovery → Brief)
  ↓
ATS (Stage 4-7: 架构选型 → 专家分派 → 整合 → 提案)
  ├─→ Power Engineer ────┐
  ├─→ Cooling Engineer ──┤
  ├─→ Layout Planner ────┤
  ├─→ Cost Architect ────┤
  ├─→ Compliance Officer ┤  (Stage 6 治理审查)
  └─→ Risk Auditor ──────┘
  ↓
AM → Client
```

---

## 5 PROCESS 流程索引

**AM 流程**(4 个,`/PROCESS/AM/`):
- Lead Qualification Process
- Customer Discovery Process
- Requirement Brief Process
- ATS Handoff Process

**ATS 流程**(3 个,`/PROCESS/ATS/`):
- Requirement Analysis
- Collaboration Process
- Proposal Generation Process

**SUPPORT 流程**:`/PROCESS/SUPPORT/` 目录当前为空,预留扩展。

---

## 6 关键交叉引用

| 入口 | 引用 | 去向 |
|------|------|------|
| PRINCIPLES P8 | [[POWER_SYSTEMS_Guideline]] | IT Load vs Total Load |
| PRINCIPLES P10 | [[MDC/AGENTS]] [[KB/PRODUCTS]] | Index-First |
| ATS §4.3 | [[COOLING_SYSTEM_Guideline]] | Zone 两步查询 |
| ATS §5.2 | 6 专家 Guideline 速查表 | 专家调度 |
| AM §4.1 | [[_Platform/Tools/Tools]] | Obsidian CLI |
| Collaboration §3.1 | [[POWER_SYSTEMS_Guideline]] | RFI 必澄清项 |

---

## 7 重要发现(PM 视角,5 个)

| # | 发现 | 影响 |
|---|------|------|
| 1 | PRINCIPLES P10 要求"必须用 Obsidian CLI" | 实际我们用 Read/Edit/Write 直读;**协议与实际不符** |
| 2 | `AGENTS/` 与 `PROCESS/` 职责有重叠 | AGENTS 讲角色(who),PROCESS 讲流程(how) |
| 3 | `PROCESS/SUPPORT/` 目录为空 | 预留,当前无内容 |
| 4 | PRINCIPLES 引用的 `[[FOG/...]]` 老路径与当前 vault 不完全一致 | 老 Works_Public 结构残留 |
| 5 | `AGENTS/index.md` 极简(7 行)与 `_index.md` 形成"目录+导航"二元结构 | 本计划产物 |

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-06-18 | 初始版本:8 章节 + 9 Agent I/O 矩阵 + 5 个 PM 发现;新 Agent 上线阅读入口总览 |
