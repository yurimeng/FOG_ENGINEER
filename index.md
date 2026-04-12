---
tags:
  - #workspace/engineer
  - #type/index
  - #system/feis
---

# FOG Workspace / 目录索引

> 本目录索引列出所有在 Git 版本控制下的文件（已排除 `.gitignore` 中的目录：Projects/、KB/BOM、Canvas/、Market/、HRBP、ResoucePool、SupplyChain、COST/）。

---

## 文件总览

```
FOG/
├── .gitignore
├── index.md                        ← 本文件
├── README.md                        ← 工作区说明
├── SOUL.md                          ← 工程哲学
├── IDENTITY.md                      ← 系统身份
├── PRINCIPLES.md                    ← 11条工程原则
├── VERSION.md                       ← 版本记录
├── USER.md                          ← 用户画像
├── HEARTBEAT.md                     ← 心跳文件
│
├── AGENTS/                          ← Agent 角色定义
│   ├── AM.md / ATS.md / Power Engineer.md / Cooling Engineer.md
│   ├── Layout Planner.md / Cost Architect.md / Compliance Officer.md
│   ├── Risk Auditor.md / Market Researcher.md
│   ├── WORKFLOW.md                  ← 工作流总览
│   └── index.md
│
├── KB/                              ← 知识库
│   ├── Guideline/                   ← 6大领域技术指南
│   │   ├── Compliance_Guideline.md
│   │   ├── COOLING_SYSTEM_Guideline.md
│   │   ├── Cost_Guideline.md
│   │   ├── Layout_Guideline.md
│   │   ├── Marketing_Guideline.md
│   │   ├── POWER_SYSTEMS_Guideline.md
│   │   ├── Risk_Guideline.md
│   │   ├── COOLING_SYSTEM_SOLUTION/
│   │   └── index.md
│   │
│   ├── 3RD-PARTY/                   ← 第三方产品文档
│   │   ├── 3rd Party List.md
│   │   │
│   │   ├── BESS/
│   │   │   ├── Gotion ESC480-125P261-UL.md
│   │   │   ├── POWER_SYSTEMS_Guideline.md
│   │   │   ├── TESLA MEGAPACK 2 XL.md
│   │   │   └── index.md
│   │   │
│   │   ├── Busbar/
│   │   │   ├── Siemens/
│   │   │   │   ├── index.md
│   │   │   │   ├── White-Paper-Busbar.pdf
│   │   │   │   ├── XL-F-Product-Spec.pdf
│   │   │   │   └── XL-III-Dense-Busbar.pdf
│   │   │   └── index.md
│   │   │
│   │   ├── COOLING/
│   │   │   ├── COOLING_SYSTEM_Guideline.md
│   │   │   ├── DRYCOOL_with_DX.md
│   │   │   ├── Hybrid Cooler 600kW - 同飞.md
│   │   │   └── index.md
│   │   │
│   │   ├── NETWORK/
│   │   │   ├── AC40_NETWORK_CONF.pdf
│   │   │   ├── AC40_NETWORK_Guideline.md
│   │   │   ├── NETWORK_Guideline.md
│   │   │   ├── PRODUCTS_NETWORK.md
│   │   │   └── index.md
│   │   │
│   │   └── UPS/
│   │       ├── Eaton/
│   │       │   ├── 9395XR-1500-Chinese-Manual.pdf
│   │       │   ├── 9395XR-1500-Rear-Exhaust-Connections.pdf
│   │       │   ├── 9395XR-1500-Top-Exhaust-Dimensions.pdf
│   │       │   ├── 9395XR-1500-Wiring-Diagram.pdf
│   │       │   ├── 93Li-G2-Battery-Brochure.pdf
│   │       │   ├── UPS_EATON_9395XR.md
│   │       │   └── index.md
│   │       └── index.md
│   │
│   ├── PRODUCTS_A32.md
│   ├── PRODUCTS_AC40.md
│   ├── PRODUCTS_AC45.md
│   ├── PRODUCTS_DC45.md
│   ├── PRODUCTS_MDC.md
│   ├── KB_Relation.canvas
│   ├── DC45 Racks.png
│   └── MDC Power Flow.png
│
├── PROCESS/                         ← 流程定义
│   ├── AM/
│   │   ├── ATS Handoff Process.md
│   │   ├── Customer Discovery Process.md
│   │   ├── Lead Qualification Process.md
│   │   ├── Requirement Brief Process.md
│   │   └── index.md
│   ├── ATS/
│   │   ├── Collaboration Process.md
│   │   ├── Proposal Generation Process.md
│   │   ├── Requirement Analysis.md
│   │   └── index.md
│   └── SUPPORT/
│       └── index.md
│
├── Reference Architecture/           ← 参考架构
│   ├── EDGE_INFERENCE_DLC_1.2MW.md
│   ├── EDGE_INFERENCE_DLC_1.2MW.md.bak
│   ├── EDGE_INFERENCE_IMMERSION_0.5MW.md
│   ├── EDGE_INFERENCE_IMMERSION_0.5MW.md.bak
│   ├── Proposal_Canvas_Template.canvas
│   └── index.md
│
├── Solutions Design/                ← 方案设计
│   ├── DC45 FrontView.canvas
│   ├── DC45 Layout 需求.md
│   ├── DC45 Racks.png
│   └── index.md
│
├── TOOLS/                           ← 工具说明
│   ├── CAD_GUIDELINES.md
│   ├── CRM_WORKFLOW.md
│   ├── KB_ACCESS.md
│   ├── QUOTE_ENGINE.md
│   ├── TOOLS.md
│   └── index.md
│
└── AGENTS.md
```

---

## .gitignore 内容

以下目录/文件被 Git 忽略：

| 模式 | 说明 |
|------|------|
| `.DS_Store` | macOS 系统文件 |
| `.openclaw/` | Obsidian 自动保存状态 |
| `Projects/` | 项目管理文件 |
| `KB/BOM` | 物料清单 |
| `Canvas/` | Canvas 文件 |
| `Market/` | 市场文件 |
| `HRBP` | 人力资源文件 |
| `ResoucePool` | 资源池 |
| `SupplyChain` | 供应链文件 |
| `COST` | 成本文件 |
| `Index.md` | 大写版本索引 |

---

*Document Version: v1.0 | Last Updated: 2026-04-12*
