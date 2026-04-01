---
tags:
  - #workspace/engineer
  - #type/index
  - #system/feis
---

# Works_Public — 工程工作空间索引

> 本文件是 Works_Public 工作空间的导航索引，所有路径均为相对路径。
> 最后更新：2026-04-01

---

## 快速入口

| 文档 | 说明 |
|------|------|
| [[README]] | 工作空间总览、核心能力、设计原则 |
| [[IDENTITY]] | 系统身份：FEIS（Fog Engineering Intelligence System）|
| [[SOUL]] | 工程哲学 |
| [[0.PRINCIPLES]] | 工程原则（必读）|
| [[VERSION]] | 版本变更历史 |

---

## 组织架构

| 角色 | 文件 |
|------|------|
| [[AGENTS/AM]] | Account Manager — 客户经理 |
| [[AGENTS/ATS]] | Architecture & Technical Sales — 架构销售 |
| [[AGENTS/Cooling Engineer]] | 冷却工程师 |
| [[AGENTS/Power Engineer]] | 电力工程师 |
| [[AGENTS/Layout Planner]] | 布局规划师 |
| [[AGENTS/Cost Architect]] | 成本架构师 |
| [[AGENTS/Compliance Officer]] | 合规官 |
| [[AGENTS/Risk Auditor]] | 风险审计师 |

参考：[[AGENTS]]

---

## 流程（PROCESS）

### AM 流程

| 流程 | 说明 |
|------|------|
| [[PROCESS/AM/Lead Qualification Process]] | 线索甄别 |
| [[PROCESS/AM/Customer Discovery Process]] | 客户需求发现 |
| [[PROCESS/AM/Requirement Brief Process]] | 需求简报 |
| [[PROCESS/AM/ATS Handoff Process]] | ATS 交接 |

### ATS 流程

| 流程 | 说明 |
|------|------|
| [[PROCESS/ATS/ATS_WORKFLOW]] | ATS 总体工作流 |
| [[PROCESS/ATS/Customer Requirement Analysis]] | 客户需求分析 |
| [[PROCESS/ATS/Architecture Selection Process]] | 架构选型 |
| [[PROCESS/ATS/Capacity Planning Process]] | 容量规划 |
| [[PROCESS/ATS/Cooling Architecture Process]] | 冷却架构 |
| [[PROCESS/ATS/Design Guideline]] | 设计指南 |
| [[PROCESS/ATS/Proposal Generation Process]] | 方案生成（输出配置，**不含价格**）|
| [[PROCESS/ATS/Site Constraint Analysis]] | 场地约束分析 |

---

## 知识库（KB）

### 产品规格

| 产品 | 说明 | IT 容量 |
|------|------|---------|
| [[KB/PRODUCTS_AC40]] | 40ft 浸没式集装箱 | 400kW IT |
| [[KB/PRODUCTS_DC45]] | 45ft 直冷液冷集装箱 | 1200kW IT |
| [[KB/PRODUCTS_A32]] | 单柜浸没式液冷 Tank | 45–50kW IT |
| [[KB/PRODUCTS_MDC]] | 模块化数据中心集群组合标准 | Up to 5MW+ |

### 电力系统（KB/3RD-PARTY）

| 文件 | 说明 |
|------|------|
| [[KB/POWER_LOAD]] | IT 负载 vs 整体电力负荷定义（**必读**）|
| [[KB/3RD-PARTY/Buildin/UPS_EATON_9395XR]] | UPS 规格（9395XR-600 / 9395XR-1500）|
| [[KB/3RD-PARTY/BESS/POWER_SYSTEMS_Guideline]] | 电力系统选型总则 |
| [[KB/3RD-PARTY/BESS/TESLA MEGAPACK 2 XL]] | Tesla 大型储能 |
| [[KB/3RD-PARTY/BESS/Gotion ESC480-125P261-UL]] | 国轩工商业储能 |
| [[KB/3RD-PARTY/BESS/POWER_SYSTEMS_Guideline 1]] | 电力系统知识（BESS vs 柴油机对比）|

### 冷却系统（KB/3RD-PARTY/COOLING）

| 文件 | 说明 |
|------|------|
| [[KB/3RD-PARTY/COOLING/COOLING_SYSTEM_SOLUTION]] | 冷却 Zone 选型原则（**必读**）|
| [[KB/3RD-PARTY/COOLING/DRYCOOL_with_DX]] | 干冷器 + DX 详细规格 |
| [[KB/3RD-PARTY/COOLING/Hybrid Cooler 600kW - 同飞]] | 同飞集成冷站 |

### 网络系统（KB/3RD-PARTY/NETWORK）

| 文件 | 说明 |
|------|------|
| [[KB/3RD-PARTY/NETWORK/AC40_NETWORK_Guideline]] | 网络架构原则 |
| [[KB/3RD-PARTY/NETWORK/PRODUCTS_NETWORK]] | 网络产品清单 |
| [[KB/3RD-PARTY/NETWORK/AC40_NETWORK_CONF.pdf]] | AC40 网络配置参考图 |

### 第三方总清单

| 文件 | 说明 |
|------|------|
| [[KB/3RD-PARTY/3rd Party List]] | 第三方产品和解决方案总清单（含引用规则）|

---

## 参考架构

| 编号 | 名称 | IT 容量 | 产品 | 冷却 |
|------|------|---------|------|------|
| RA-001 | [[Reference Architecture/EDGE_INFERENCE_IMMERSION_0.5MW]] | 0.5MW | AC40 | Immersion |
| RA-002 | [[Reference Architecture/EDGE_INFERENCE_DLC_1.2MW]] | 1.2MW | DC45 | DLC |

参考：[[REFERENCE_ARCHITECTURE]]

---

## 工具（TOOLS）

| 工具 | 用途 | 访问权限 |
|------|------|---------|
| [[TOOLS/CAD_GUIDELINES]] | CAD 布局输出规范 | Engineering Agent |
| [[TOOLS/NOTION_WORKFLOW]] | 客户管理规范 | Engineering Agent |
| [[TOOLS/QUOTE_ENGINE]] | 报价引擎 | ⚠️ **仅供商务团队，禁止 Engineering Agent 访问** |

参考：[[TOOLS]]

---

## 项目记录（Projects）

| 项目 | 说明 |
|------|------|
| [[Projects/PQTech]] | PQTech 项目 |
| [[Projects/RiCloud]] | RiCloud B300 AI 算力集群 |
| [[Projects/8th_Power]] | 第八电力 |

---

## 关键规则速查

### ⚠️ 禁止事项

- ❌ 提供任何价格、成本估算或报价
- ❌ 推荐 A32 / AC40 / DC45 / MDC 以外的产品
- ❌ 使用纯干冷器方案（必须配 DX）
- ❌ 将 IT 负载和整体电力负荷混用

### 核心原则

- 配置输出优先，价格问题转 AM
- 只推荐 KB 内定义的产品组合
- 电力数据必须标注 IT 负载和整体电力负荷
- Wikilink 路径必须使用相对路径（`KB/...`，禁止使用绝对路径）

---

## 文件路径规范

```
✅ 正确示例：
[[KB/3RD-PARTY/COOLING/COOLING_SYSTEM_SOLUTION|KB/COOLING_SYSTEM_SOLUTION]]
[[KB/3RD-PARTY/Buildin/UPS_EATON_9395XR|KB/UPS_EATON_9395XR]]

❌ 错误示例（已废弃）：
[[KB/COOLING_SYSTEM_SOLUTION|KB/COOLING_SYSTEM_SOLUTION]]
[[KB/AI Agent/Workspace-Engineer/KB/3RD-PARTY/...]]
```
