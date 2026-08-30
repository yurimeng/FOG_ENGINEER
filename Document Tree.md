---
title: Document Tree — Vault 文档树导航与重新组织建议
tags:
  - #workspace/admin
  - #type/index
  - #system/feis
  - #MDC
created: 2026-06-18
last_updated: 2026-08-30
doc_version: v0.2
audience: Yuri（仅内部 review 用）
status: draft — 待 review
---

# Document Tree — Vault 文档树导航与重新组织建议

> **本文件性质**:导航 + 重新组织建议文档。**不是命令**。用户 review 之后才决定是否 re-org。
> **范围**:仅盘点、不修改任何其他文件。
> **生成日期**:2026-06-18
>
> ⚠️ **2026-08-30 产品口径说明:** 本文件 §2 目录树与 §4 清单的产品命名已对齐现行基线 —— 两条产品线 **Liquid Cooling**(`L`)L1240C45 · L1800C45 · L450C20 与 **Immersion Cooling**(`I`)I400C45 · I400C40 · I200C20,**六 SKU 全部 `shipped`**(站点 `docs/PRODUCT-MATRIX.md` §5 D-19 gate · 2026-08-27),另有 I50TS 浸没槽体组件。命名基准 [[NAMING_MAP]]。
> **§5–§10 的重组建议、行动项与决策请求仍是 2026-06-18 的时点记录**,其中的旧名(A Series / D Series / DC45 Tech Spec 路径等)与已失效路径**保留原样**,不回溯改写。文件名本身一律未改。

---

## 1. Vault 总体介绍

本 vault 是 **FEIS(Fog Engineering Intelligence System)** —— Fog Computing 模组化边缘数据中心业务的售前工程知识库,基于 Obsidian + iCloud 同步。承载三类内容:

1. **产品对外文档**(External):Tech Spec、Pitch Deck、Reference Architecture 等需严格控制外发的内容
2. **内部技术资产**(Internal):产品 PRD、供应商资料、设计 Guideline、工程手稿、Agent/PROCESS 规则
3. **运营管理**(Admin/HR/Business):合同、成本、招聘、项目跟踪、市场周报

核心 hard rules:不输出价格 · KB-only 产品推荐 · 不做竞品对外比较 · IT Load vs Total Facility Load 必须澄清 · UPS ≠ BESS · 无静默编辑 Projects/ 与 KB/。

---

## 2. 当前目录结构(完整列出)

```
/  (vault root)
├── README.md
├── CLAUDE.md                         ← 项目级操作规则
├── PRINCIPLES.md                     ← 最高准则
├── SOUL.md · IDENTITY.md · USER.md · HEARTBEAT.md · VERSION.md
├── AGENTS.md                         ← 根级散落(内容为 AGENTS/ 简介)
├── FOG_Workspace_Summary.md          ← 内部快照(gitignored)
├── index.md                          ← 根级 index(gitignored)
├── generate_token_calc.py            ← 工具(gitignored)
├── Token_Calc_AC40_DC45_Haiyan.xlsx  ← 工具产物(gitignored)
│
├── AGENTS/                           ← 角色定义(8 个角色 + index + WORKFLOW)
│   ├── index.md · WORKFLOW.md
│   ├── AM.md · ATS.md · Compliance Officer.md · Cooling Engineer.md
│   ├── Cost Architect.md · Layout Planner.md · Market Researcher.md
│   ├── Power Engineer.md · Risk Auditor.md
│
├── PROCESS/                          ← 流程
│   ├── index.md
│   ├── AM/  ATS/  SUPPORT/
│   └── (Customer Discovery / Lead Qualification / Requirement Brief /
│        Proposal Generation / Requirement Analysis / Collaboration /
│        ATS Handoff 等子流程)
│
├── TOOLS/                            ← 工具与操作手册
│   ├── index.md · TOOLS.md
│   ├── CAD_GUIDELINES.md · CRM_WORKFLOW.md · KB_ACCESS.md
│   ├── LARK_CLI.md · QUOTE_ENGINE.md · TCO Calculator.md
│
├── KB/                               ← 知识库主体
│   ├── index.md · PRODUCTS_MDC.md · MDC Power Flow.png
│   ├── Guideline/                    ← 9 个 Guideline + _blocks/
│   ├── 3RD-PARTY/                    ← 供应商库
│   │   ├── 3rd Party List.md · STD_Supplier.md · index.md
│   │   ├── _blocks/                  ← 3rd_Party_List / STD_Supplier 块
│   │   ├── COOLING/(DESIGN/ + Suppliers/ + _blocks/)
│   │   ├── POWER/(UPS/ + Busbar/ + BESS/ + _blocks/)
│   ├── IMMERSION/                 ← Immersion Cooling 线:I400C45 / I400C40 / I200C20 + I50TS(槽体组件)
│   │   ├── PRODUCTS_I50TS.md · PRODUCTS_I400C40.md · PRODUCTS_I400C45.md
│   │   ├── Design/                   ← I50TS Flow / I400C40 Layout / NET 文档
│   │   ├── _blocks/PRODUCTS_I50TS|A40|A45/(01..07)
│   │   └── index.md
│   ├── LIQUID/L1240C45/                 ← Liquid Cooling 线(线内另有 L1800C45 / L450C20);以下为 L1240C45 子树
│   │   ├── PRODUCTS/(L1240C45 Tech Spec EN/CN · L1240C45_MDC_BOM · Racks.png)
│   │   ├── PRODUCTS/(MDC Engineering Handbook External · MDC_Product_Quick_Ref)
│   │   ├── DESIGN/(Design 准则 + Compliance + Hydronic + Thermal + BOM)
│   │   ├── DESIGN/_blocks/
│   │   ├── DC45 Layout/(TOP/FRONT/SIDE 视图)
│   │   ├── _archive/                 ← 旧版 DC45 PRD/Quick Spec/三支路评估
│   │   └── index.md
│
├── Reference Architecture/           ← RA-001 (Immersion 0.4MW) / RA-002 (DLC 1.2MW)
│   ├── index.md
│   ├── EDGE_INFERENCE_IMMERSION_0.4MW.md
│   ├── EDGE_INFERENCE_DLC_1.2MW.md
│   └── Site_Reference_Climate_Standard.md
│
├── Market/                           ← 市场分析(Diablo / 周报)
│   ├── index.md
│   ├── Market_Report.md
│   └── Diablo_400_市场分析报告.md
│
├── Projects/                         ← 项目跟踪
│   ├── project_list.md · _template_Project_Record.md
│   ├── 外发资料_最新/                ← 对外客户资料(CN/EN Tech Spec)
│   ├── 归档项目/(Orb2/ + Closed-Lost 模板)
│   ├── 自建算力项目/                 ← 占位
│   ├── 00_项目前期信息采集和方案引导/← 售前引导
│   ├── 8th_Power/ · BILT_Finland_70MW/(Site Info/01..05)
│   ├── Bitdeer/(RFI) · BTCT/(AIDC 方案) · Clutch_40MW/
│   ├── Crucible/(RFI) · Logy_Computer/ · Phoenix_Global/
│   ├── PQTech/(采访稿 / Truck Demo / Pudong / Haiyan Summary)
│   ├── PQTech/张江金融数据港边缘智算中心/
│   ├── RiCloud/(B300 网络方案 v1/v2) · Simple_Mining/(DG vs BESS + RFI)
│   └── Weekly_Plan/
│
├── Business_Documents/               ← 合同与法律(MSA Drafts + APPENDIX A-F)
│   ├── index.md
│   ├── MSA Draft CN/EN.md · MASTER_AGREEMENT_CN/EN.md
│   ├── APPENDIX_A..F_CN/EN.md
│   └── COST/Cost breakdown 260418.md
│
├── HRBP/                             ← 人事
│   ├── index.md · JD AI Startup Scout + Solution Pre-Sales(Intern).md
│   └── Intern in CA/                 ← 23 份简历 PDF/docx
│
├── ResoucePool/                      ← 客户/资源池(注意拼写)
│   ├── index.md
│   ├── End-USER/(智谱华章) · Investors/ · NCP/
│   ├── Power/(Mawson 3 个站点) · System_Integrator/(博大数据)
│
├── EXT-001-T2T3-deliverables/        ← 项目交付物
│   ├── t2t3-open-questions.md
│   └── t3-scale-envelope.md
│
├── Canvas/                           ← 画布 / 提案
│   ├── index.md · Proposal/index.md
│
├── memory/                           ← AI 事实记忆(gitignored)
│   └── FACT.md
│
├── .openclaw/                        ← 工作区状态(gitignored)
│   └── workspace-state.json
│
├── .claude/                          ← Claude Code 配置(gitignored)
├── .git/ · .gitignore · .gitattributes · .DS_Store
```

---

## 3. External vs Internal 分类总览

| 分类 | 数量级别 | 触达对象 | review 严格度 | 代表目录 |
|------|----------|----------|---------------|----------|
| **External** | ~20+ 文件 | 客户 / 投资者 / 媒体 | 严格(每篇外发前过审) | `KB/IMMERSION/PRODUCTS_*.md` · `KB/LIQUID/L1240C45/PRODUCTS/DC45 Tech Spec*` · `Reference Architecture/` · `Projects/外发资料_最新/` · `Business_Documents/PITCH DECK Flyer.md` · `Projects/PQTech/采访稿_新版.md` |
| **Internal** | ~200+ 文件 | 团队 + AI Agent | 中等 | `KB/Guideline/` · `KB/3RD-PARTY/` · `KB/LIQUID/L1240C45/DESIGN/` · `Projects/<name>/Project_Record.md` · `Business_Documents/*MSA/MASTER/APPENDIX` · `Market/` · `HRBP/` |
| **Meta/Admin** | ~15 文件 | Yuri + AI | 低(自用) | `CLAUDE.md` · `PRINCIPLES.md` · `SOUL.md` · `AGENTS.md` · `PROCESS/` · `TOOLS/` · `FOG_Workspace_Summary.md` |

> **关键判断**:"External" 不等于"已发布",而是"理论上可发布"。多数情况下已经过 Yuri 审阅定稿,任何改动都需要重新 review。

---

## 4. External 文档清单(对外发布)

| # | 当前路径 | 用途 | External? | 建议去留 |
|---|---------|------|-----------|---------|
| E01 | `KB/IMMERSION/PRODUCTS_I50TS.md` | I50TS 槽体组件 PRD 对外 | ✅ | 保留 External;位置 OK |
| E02 | `KB/IMMERSION/PRODUCTS_I400C40.md` | I400C40 标品 PRD 对外 | ✅ | 保留 External;位置 OK |
| E03 | `KB/IMMERSION/PRODUCTS_I400C45.md` | I400C45 标品 PRD 对外 | ✅ | 保留 External;位置 OK |
| E04 | `KB/LIQUID/L1240C45/PRODUCTS/L1240C45 Tech Spec EN.md` | L1240C45 Tech Spec 英文 | ✅ | 保留 External;**位置混乱**(见 §5.1) |
| E05 | `KB/LIQUID/L1240C45/PRODUCTS/L1240C45 Tech Spec CN.md` | L1240C45 Tech Spec 中文 | ✅ | 保留 External;**位置混乱** |
| E06 | `KB/_COMMON/MDC Engineering Handbook External.md` | 对外工程手册 | ✅ | 保留 External |
| E07 | `KB/_COMMON/MDC_Product_Quick_Ref.md` | 三平台快速对比 | ✅ | 保留 External(快速参考) |
| E08 | `Reference Architecture/EDGE_INFERENCE_IMMERSION_0.4MW.md` | RA-001 对外 | ✅ | 保留 External;位置 OK |
| E09 | `Reference Architecture/EDGE_INFERENCE_DLC_1.2MW.md` | RA-002 对外 | ✅ | 保留 External;位置 OK |
| E10 | `Reference Architecture/Site_Reference_Climate_Standard.md` | 三站点 + 6 站点气候 | ✅ | 保留 External(可作 appendix) |
| E11 | `Projects/外发资料_最新/L1240C45 Tech Spec CN.md` | CN Tech Spec V1.3 旧副本 | ⚠️ | **与 E04 重复**;建议删除(已 E04 标注"最新版 V1.4 见 KB/") |
| E12 | `Projects/外发资料_最新/L1240C45 Tech Spec EN.md` | EN Tech Spec V1.3 旧副本 | ⚠️ | **与 E04 重复**;建议删除 |
| E13 | `Business_Documents/PITCH DECK Flyer.md` | 对外 pitch | ✅ | 保留 External;**位置错位**(在 Business_Documents/) |
| E14 | `Projects/PQTech/采访稿_新版.md` | 媒体采访稿 | ✅ | 保留 External;在 Projects/ 合理 |
| E15 | `Market/Market_Report.md` | 市场周报 | ✅ | 保留 External(若每周发布) |
| E16 | `Market/Diablo_400_市场分析报告.md` | Diablo 400 市场分析 | ✅ | 保留 External |
| E17 | `KB/IMMERSION/_line/PRODUCTS_NETWORK.md` | 产品网络配置 | ⚠️ | Internal;非 External(对内设计) |
| E18 | `KB/LIQUID/L1240C45/PRODUCTS/L1240C45_MDC_BOM.md` | L1240C45 BOM | ⚠️ | **可对外**(若脱敏),目前混在 External 目录 |

> **判定规则**:文件有 "External" / "Handbook External" 字样、或明确是 Tech Spec / RA / Pitch / 采访稿 / 市场报告 → External。其他是 Internal。

---

## 5. Internal 文档清单(内部使用)

### 5.1 KB 内部技术资产

| # | 路径 | 用途 | Internal? | 建议 |
|---|------|------|-----------|------|
| I01 | `KB/Guideline/COOLING_SYSTEM_Guideline.md` | 冷却 Guideline | ✅ | 保留 |
| I02 | `KB/Guideline/POWER_SYSTEMS_Guideline.md` | 电力 Guideline | ✅ | 保留 |
| I03 | `KB/Guideline/Cost_Guideline.md` | 成本 Guideline | ✅ | 保留 |
| I04 | `KB/Guideline/Layout_Guideline.md` | 布局 Guideline | ✅ | 保留 |
| I05 | `KB/Guideline/Compliance_Guideline.md` | 合规 Guideline | ✅ | 保留 |
| I06 | `KB/Guideline/Risk_Guideline.md` | 风险 Guideline | ✅ | 保留 |
| I07 | `KB/Guideline/NETWORK_Guideline.md` | 网络 Guideline | ✅ | 保留 |
| I08 | `KB/Guideline/Marketing_Guideline.md` | 市场 Guideline | ✅ | 保留 |
| I09 | `KB/Guideline/PRINCIPLE_Guideline.md` | 原则 Guideline | ✅ | 保留 |
| I10 | `KB/Guideline/_blocks/*` | 上述 Guideline 的块文件 | ✅ | 保留 |
| I11 | `KB/3RD-PARTY/3rd Party List.md` | 第三方清单 | ✅ | 保留(Single Source) |
| I12 | `KB/3RD-PARTY/STD_Supplier.md` | 标准供应商表 | ✅ | 保留 |
| I13 | `KB/3RD-PARTY/COOLING/DESIGN/V5.md` × 4 | CDU/CRAH/Hybrid/RDHX 准则 | ✅ | 保留(部分是 .V5 旧版) |
| I14 | `KB/3RD-PARTY/COOLING/Suppliers/PRD-*.md` | 供应商 PRD | ✅ | 保留(决策依据) |
| I15 | `KB/3RD-PARTY/COOLING/Suppliers/TICA_*.md/xlsx` | TICA 澄清文件 | ✅ | 保留 |
| I16 | `KB/3RD-PARTY/BESS/Suppliers/*.md` | 电池供应商 | ✅ | 保留 |
| I17 | `KB/3RD-PARTY/UPS/Suppliers/Eaton/*(gitignored)` | Eaton UPS datasheet | ✅ | 保留 |
| I18 | `KB/3RD-PARTY/Busbar/Suppliers/Siemens/*(gitignored)` | Siemens 母线 | ✅ | 保留 |
| I19 | `KB/3RD-PARTY/_blocks/*` | 3rd Party 块 | ✅ | 保留 |
| I20 | `KB/IMMERSION/_line/*` | A 系列设计稿 | ✅ | 保留(部分 gitignored) |
| I21 | `KB/IMMERSION/_blocks/PRODUCTS_*/` | A 系列 PRD 块 | ✅ | 保留 |
| I22 | `KB/LIQUID/L1240C45/DESIGN/*` | D 系列设计稿 | ✅ | 保留(部分 gitignored) |
| I23 | `KB/LIQUID/L1240C45/DESIGN/_blocks/*` | D 系列设计块 | ✅ | 保留 |
| I24 | `KB/LIQUID/L1240C45/_archive/*` | 旧版归档 | ✅ | 保留(归档不删) |
| I25 | `KB/_COMMON/PRODUCTS_MDC.md` | MDC 旧版总览 | ⚠️ | **疑似过期**;review 后决定保留/归档 |
| I26 | `KB/MDC Power Flow.png` | MDC 电力流图 | ✅ | 保留(被引用) |
| I27 | `KB/index.md` | KB 顶层 index | ✅ | 保留 |
| I28 | `KB/3RD-PARTY/COOLING/DESIGN/.计算公式.md` | 计算公式(隐藏) | ✅ | 保留 |
| I29 | `KB/3RD-PARTY/COOLING/DESIGN/COOLING_DESIGN_v4_lockdown_plan.md` | 冷却设计 v4 lockdown | ✅ | 保留 |
| I30 | `KB/3RD-PARTY/COOLING/DESIGN/CDU FlowChart.png` | CDU 流程图 | ✅ | 保留 |

### 5.2 Projects 内部(项目跟踪)

| # | 路径 | 用途 | Internal? | 建议 |
|---|------|------|-----------|------|
| P01 | `Projects/project_list.md` | 项目状态 SoT | ✅ | **保留** — SoT |
| P02 | `Projects/_template_Project_Record.md` | 项目记录模板 | ✅ | 保留 |
| P03 | `Projects/归档项目/_template_ClosedLost.md` | Closed-Lost 模板 | ✅ | 保留 |
| P04 | `Projects/归档项目/Orb2/*` | 已归档项目 | ✅ | 保留 |
| P05 | `Projects/00_项目前期信息采集和方案引导/` | 售前引导 | ✅ | 保留 |
| P06 | `Projects/8th_Power/*` | 在跟项目 | ✅ | 保留 |
| P07 | `Projects/BILT_Finland_70MW/*` | 在跟项目 | ✅ | 保留 |
| P08 | `Projects/Bitdeer/*` | 在跟项目 | ✅ | 保留 |
| P09 | `Projects/BTCT/*` | 在跟项目 | ✅ | 保留 |
| P10 | `Projects/Clutch_40MW/` | 在跟项目 | ✅ | 保留 |
| P11 | `Projects/Crucible/*` | 在跟项目 | ✅ | 保留 |
| P12 | `Projects/Logy_Computer/*` | 在跟项目 | ✅ | 保留 |
| P13 | `Projects/Phoenix_Global/*` | 在跟项目 | ✅ | 保留 |
| P14 | `Projects/PQTech/*`(采访稿除外) | PQTech 项目记录 | ✅ | 保留 |
| P15 | `Projects/RiCloud/*` | 在跟项目 | ✅ | 保留 |
| P16 | `Projects/Simple_Mining/*` | 在跟项目 | ✅ | 保留 |
| P17 | `Projects/Weekly_Plan/*` | 周计划 | ✅ | 保留 |
| P18 | `Projects/自建算力项目/` | 占位 | ⚠️ | 长期空,review 是否删除占位 |
| P19 | `Projects/外发资料_最新/index.md` | 外发目录索引 | ✅ | **位置应改为 External/** |
| P20 | `Projects/PQTech/采访稿_新版.md` | 媒体稿 | ✅ External | 见 E14 |
| P21 | `Projects/外发资料_最新/L1240C45 Tech Spec CN/EN.md` | 旧版副本 | ⚠️ | **与 E04/E05 重复,建议删除** |

### 5.3 Business / HR / Market / Resource / Canvas

| # | 路径 | 用途 | Internal? | 建议 |
|---|------|------|-----------|------|
| B01 | `Business_Documents/MSA Draft CN/EN.md` | MSA 草稿 | ✅ | 保留 |
| B02 | `Business_Documents/MASTER_AGREEMENT_CN/EN.md` | 正式 MSA 模板 | ✅ | 保留 |
| B03 | `Business_Documents/APPENDIX_A..F_CN/EN.md` | 合同附录 6 套 | ✅ | 保留 |
| B04 | `Business_Documents/COST/Cost breakdown 260418.md` | 成本明细 | ✅ | 保留 |
| B05 | `Business_Documents/PITCH DECK Flyer.md` | Pitch Deck | ✅ External | **位置应改 External/** |
| H01 | `HRBP/Intern in CA/*` | 23 份简历 | ✅ | 保留 |
| H02 | `HRBP/JD AI Startup Scout + Solution Pre-Sales(Intern).md` | 招聘 JD | ✅ | 保留 |
| M01 | `Market/Market_Report.md` | 市场周报 | ✅ External | 保留 |
| M02 | `Market/Diablo_400_市场分析报告.md` | Diablo 分析 | ✅ External | 保留 |
| R01 | `ResoucePool/End-USER/智谱华章.md` | 终端用户 | ✅ | 保留 |
| R02 | `ResoucePool/Investors/·NCP/·System_Integrator/*` | 资源池 | ✅ | 保留 |
| R03 | `ResoucePool/Power/Mawson Site *.md` | 电力资源 | ✅ | 保留 |
| R04 | `ResoucePool/index.md` | 资源池索引 | ✅ | 保留 |
| R05 | `ResoucePool/End-USER/index.md` | 资源池-终端用户索引 | ✅ | 保留 |
| C01 | `Canvas/index.md` · `Canvas/Proposal/index.md` | 画布 | ✅ | 保留 |
| X01 | `EXT-001-T2T3-deliverables/t2t3-open-questions.md` | 项目交付物 | ✅ | 保留 |
| X02 | `EXT-001-T2T3-deliverables/t3-scale-envelope.md` | 项目交付物 | ✅ | 保留 |

### 5.4 工具与脚本(gitignored)

| # | 路径 | 用途 | 建议 |
|---|------|------|------|
| T01 | `generate_token_calc.py` | Token 计算脚本 | 保留 |
| T02 | `Token_Calc_AC40_DC45_Haiyan.xlsx` | Token 计算产物 | 保留 |
| T03 | `Projects/PQTech/Token_Calc_AC40_DC45_Haiyan_Summary.md` | Token 汇总(重复) | ⚠️ 考虑合并到 T02 |
| T04 | `memory/FACT.md` | AI 事实记忆 | 保留 |

### 5.5 散落的 Internal 文档

| # | 路径 | 问题 | 建议 |
|---|------|------|------|
| L01 | `AGENTS.md`(根级) | 内容是 AGENTS/ 简介,**散落在根级** | 移到 `AGENTS/_overview.md` 或合并到 `AGENTS/index.md` |
| L02 | `FOG_Workspace_Summary.md`(根级) | 内部快照,**散落根级** | 移到 `Admin/` 或 `_internal/` |
| L03 | `index.md`(根级) | 根级 index | **不要移**;这是 Obsidian 入口 |
| L04 | `CLAUDE.md` · `PRINCIPLES.md` · `SOUL.md` · `IDENTITY.md` · `USER.md` · `HEARTBEAT.md` · `VERSION.md`(根级) | 元规则 | **不要移**;Yuri 的私人生效点 |
| L05 | `KB/_COMMON/PRODUCTS_MDC.md` | 旧版 MDC 总览 | review 后决定保留/归档 |

---

## 6. Meta/Admin 文档(规则,系统级)

> 这层**不动**,Yuri 已固化位置。

| # | 路径 | 用途 | 移动建议 |
|---|------|------|----------|
| META01 | `CLAUDE.md` | Claude Code 项目级规则 | 不动 |
| META02 | `PRINCIPLES.md` | 最高准则 | 不动 |
| META03 | `SOUL.md` | AI 灵魂描述 | 不动 |
| META04 | `IDENTITY.md` | 身份定义 | 不动 |
| META05 | `USER.md` | 用户画像 | 不动 |
| META06 | `HEARTBEAT.md` | 心跳/活跃度 | 不动 |
| META07 | `VERSION.md` | 版本日志 | 不动 |
| META08 | `AGENTS/index.md` | 角色索引 | 不动 |
| META09 | `AGENTS/WORKFLOW.md` | 工作流 | 不动 |
| META10 | `PROCESS/index.md` · `AM/index.md` · `ATS/index.md` · `SUPPORT/index.md` | 流程索引 | 不动 |
| META11 | `TOOLS/index.md` · `TOOLS/TOOLS.md` | 工具索引 | 不动 |
| META12 | `README.md` | 仓库说明 | 不动 |

---

## 7. 重新组织建议

### 7.1 当前结构问题(明确)

1. **External 文档散落多处**:
   - `KB/LIQUID/L1240C45/PRODUCTS/L1240C45 Tech Spec CN/EN.md` —— 对外 Tech Spec 放在 KB/ 内部 PRODUCTS/ 目录,容易误以为是 Internal
   - `Business_Documents/PITCH DECK Flyer.md` —— 商务合同目录下混入对外 pitch
   - `Reference Architecture/` —— 顶层目录命名暗示是设计参考,但实际 RA 是对外发布件
   - `Projects/外发资料_最新/L1240C45 Tech Spec CN/EN.md` —— **与 KB 官方版重复**(E11/E12)

2. **Internal 文档混入 External 区**:
   - `KB/_COMMON/MDC Engineering Handbook External.md` —— 同目录下的 `MDC_Product_Quick_Ref.md` 和 `L1240C45_MDC_BOM.md` 是 Internal/半 External,**混在一起难以区分**

3. **散落的根级文件**:
   - `AGENTS.md`(根级)—— 散落根级,内容是 AGENTS/ 简介,易与 `AGENTS/index.md` 混淆
   - `FOG_Workspace_Summary.md`(根级)—— 内部快照,放在根级容易让人误以为是工作区说明

4. **命名不一致**:
   - `ResoucePool` 拼写错(应该是 `ResourcePool`),但因 gitignore 模式依赖此拼写,**不重命名**
   - `KB/3RD-PARTY/UPS/` 与 `KB/3RD-PARTY/Busbar/` 用下划线一致,但 `KB/3RD-PARTY/COOLING/Suppliers/` 没用子目录(部分供应商)vs `BESS/Suppliers/` 直接平铺

5. **空目录/占位目录**:
   - `Projects/自建算力项目/`(仅有 index.md)
   - `KB/3RD-PARTY/BESS/Suppliers/`(可能缺品类)
   - `KB/3RD-PARTY/UPS/Suppliers/`(有 `Eaton/`,但根 `Suppliers/index.md` 缺失)
   - `KB/3RD-PARTY/Busbar/Suppliers/`(根 `Suppliers/index.md` 缺失)

6. **重复文档**:
   - `Projects/外发资料_最新/L1240C45 Tech Spec CN/EN.md` 是 V1.3 旧版,KB 已有 V1.4
   - `KB/LIQUID/L1240C45/_archive/PRODUCTS_L1240C45.md` 是旧版 PRD(已归档,合理)
   - `KB/_COMMON/PRODUCTS_MDC.md` 与 `KB/LIQUID/L1240C45/PRODUCTS/index.md` 范围可能重叠

7. **合同 vs 工程文档的混淆**:
   - `MSA Draft CN/EN.md` 已正确归位到 `Business_Documents/`,但 `Projects/外发资料_最新/index.md` 第 16-18 行仍有 MSA 引用(应清理)

### 7.2 建议的目录结构(树状)

```
/  (vault root)
├── README.md
├── CLAUDE.md                  ← 元规则(不动)
├── PRINCIPLES.md              ← 最高准则(不动)
├── SOUL.md · IDENTITY.md · USER.md · HEARTBEAT.md · VERSION.md(不动)
├── index.md                   ← Obsidian 入口(不动)
├── Document Tree.md           ← 本文件
│
├── KB/                        ← 知识库(Internal)
│   ├── index.md
│   ├── Guideline/             ← 9 个 Guideline + _blocks/
│   ├── 3RD-PARTY/             ← 供应商库
│   │   ├── 3rd Party List.md · STD_Supplier.md
│   │   ├── COOLING/(DESIGN/ + Suppliers/ + _blocks/)
│   │   ├── POWER/(UPS/ + Busbar/ + BESS/)
│   │   ├── _blocks/
│   ├── Products/              ← 内部产品 PRD 块
│   │   ├── A Series/          ← A32 / AC40 / AC45 PRD
│   │   └── D Series/          ← DC45 PRD/设计/归档
│   ├── Layout/                ← MDC 电力流图 + 布局图
│   └── _archive/              ← 全局归档
│
├── External/                  ← 对外发布(新顶层目录)
│   ├── Tech_Spec/             ← L1240C45 Tech Spec EN/CN
│   ├── Reference_Architecture/← RA-001 / RA-002
│   ├── Pitch/                 ← PITCH DECK Flyer
│   ├── Datasheet/             ← 各产品 datasheet
│   ├── Marketing/             ← 市场周报 + 分析报告
│   └── Media/                 ← 采访稿
│
├── AGENTS/                    ← 角色定义(不动)
├── PROCESS/                   ← 流程(不动)
├── TOOLS/                     ← 工具(不动)
│
├── Projects/                  ← 项目跟踪
│   ├── _template/             ← 模板
│   ├── project_list.md        ← SoT
│   ├── <name>/                ← 各项目
│   ├── 归档项目/              ← Closed-Lost
│   └── Weekly_Plan/
│   ~~(移除:外发资料_最新/)~~  ← 内容已迁到 External/
│
├── Business_Documents/        ← 合同(不动,但 PITCH DECK Flyer 移走)
│
├── Market/                    ← 内部市场情报(可与 External/Marketing/ 合并)
├── HRBP/                      ← 人事(不动)
├── ResoucePool/               ← 资源池(不动,注意拼写)
├── EXT-001-T2T3-deliverables/ ← 项目交付物(不动)
├── Canvas/                    ← 画布(不动)
│
├── Admin/                     ← 新顶层(整合散落根级)
│   ├── AGENTS_overview.md     ← 根级 AGENTS.md 内容
│   └── FOG_Workspace_Summary.md
│
├── .git/ · .gitignore · .gitattributes · .DS_Store
├── .claude/ · .openclaw/ · memory/(均 gitignored)
```

### 7.3 具体迁移动作清单

> **优先级**:🔴 高 = 影响 External/Internal 分类正确性 · 🟡 中 = 影响可发现性 · 🟢 低 = 清理散落

| #   | 要移动的文件                                                          | 目标路径                                          | 理由                       | 风险                     | 优先级 |
| --- | --------------------------------------------------------------- | --------------------------------------------- | ------------------------ | ---------------------- | --- |
| M01 | `KB/LIQUID/L1240C45/PRODUCTS/L1240C45 Tech Spec EN.md`                 | `External/Tech_Spec/L1240C45_Tech_Spec_EN.md`     | External 应在 External/ 目录 | 高 — 大量 `[[...]]` 引用需更新 | 🔴  |
| M02 | `KB/LIQUID/L1240C45/PRODUCTS/L1240C45 Tech Spec CN.md`                 | `External/Tech_Spec/L1240C45_Tech_Spec_CN.md`     | 同上                       | 高                      | 🔴  |
| M03 | `Business_Documents/PITCH DECK Flyer.md`                        | `External/Pitch/PITCH_DECK_Flyer.md`          | Pitch 是对外                | 中 — 少量 `[[...]]` 引用    | 🟡  |
| M04 | `Projects/外发资料_最新/L1240C45 Tech Spec CN.md`                         | **删除**                                        | 重复(M01/M02 的 V1.4 已替代)   | 低 — index.md 已标注旧版     | 🟢  |
| M05 | `Projects/外发资料_最新/L1240C45 Tech Spec EN.md`                         | **删除**                                        | 重复                       | 低                      | 🟢  |
| M06 | `Projects/外发资料_最新/index.md`                                     | `External/index.md` 或删除(已无内容)                 | 目录已空                     | 低                      | 🟢  |
| M07 | `Market/Market_Report.md`                                       | `External/Marketing/Market_Report.md`         | 外部周报                     | 中                      | 🟡  |
| M08 | `Market/Diablo_400_市场分析报告.md`                                   | `External/Marketing/Diablo_400_市场分析报告.md`     | 外部报告                     | 中                      | 🟡  |
| M09 | `Reference Architecture/*.md`(3 个)                              | `External/Reference_Architecture/*`           | RA 对外                    | 高 — `[[...]]` 引用广泛     | 🟡  |
| M10 | `Projects/PQTech/采访稿_新版.md`                                     | `External/Media/PQTech_采访稿.md`                | 媒体稿                      | 中                      | 🟡  |
| M11 | `AGENTS.md`(根级)                                                 | `AGENTS/_overview.md` 或合并到 `AGENTS/index.md`  | 散落根级                     | 中 — `[[AGENTS]]` 引用    | 🟡  |
| M12 | `FOG_Workspace_Summary.md`(根级)                                  | `Admin/FOG_Workspace_Summary.md`              | 内部快照                     | 低 — gitignored         | 🟢  |
| M13 | `KB/_COMMON/PRODUCTS_MDC.md`                                            | **review** — 决定保留/归档                          | 疑似过期                     | 中                      | 🟡  |
| M14 | `KB/_COMMON/MDC_Product_Quick_Ref.md`             | `External/Datasheet/MDC_Product_Quick_Ref.md` | 快速参考对外                   | 中                      | 🟡  |
| M15 | `KB/_COMMON/MDC Engineering Handbook External.md` | `External/Pitch/MDC_Engineering_Handbook.md`  | 已是 External              | 中                      | 🟡  |
| M16 | `KB/LIQUID/L1240C45/PRODUCTS/L1240C45_MDC_BOM.md`                      | `External/Datasheet/L1240C45_MDC_BOM.md`          | BOM 对外                   | 中                      | 🟡  |
| M17 | `Projects/自建算力项目/`(空 index)                                     | **review** — 决定保留/删除                          | 长期空目录                    | 极低                     | 🟢  |
| M18 | `KB/3RD-PARTY/UPS/Suppliers/index.md`(缺失)                       | **创建** 占位                                     | 保持目录一致                   | 极低                     | 🟢  |
| M19 | `KB/3RD-PARTY/Busbar/Suppliers/index.md`(缺失)                    | **创建** 占位                                     | 同上                       | 极低                     | 🟢  |
| M20 | `Projects/外发资料_最新/index.md` 第 16-18 行 MSA 引用                    | **删除/修正** 引用                                  | 合同已归位                    | 低                      | 🟢  |

### 7.4 引用迁移预估

| 引用类型 | 估计数量 | 处理方式 |
|----------|----------|----------|
| `[[L1240C45_Tech_Spec_EN]]` 内部引用 | 10+ 处(M01) | 全部更新为目标路径,或保持文件名 + 移动(只需更新 index.md) |
| `[[L1240C45_Tech_Spec_CN]]` 内部引用 | 10+ 处(M02) | 同上 |
| `[[MSA Draft CN]]` / `[[MSA Draft EN]]` 引用 | 2 处(P19) | 已在 `Business_Documents/`,无需改;清理 index.md 残留 |
| `[[PITCH_DECK_Flyer]]` 引用 | 待扫 | 移到 `External/Pitch/` 后更新 |
| `[[EDGE_INFERENCE_*.md]]` 引用 | 待扫 | 移到 `External/Reference_Architecture/` 后更新 |

---

## 8. 决策检查清单(re-org 前要确认)

- [ ] **M01/M02 移动**:扫描所有 `[[...]]` 引用,列出 0 引用 / ≥1 引用清单
- [ ] **M03 移动**:扫描 `[[PITCH_DECK_Flyer]]` 引用
- [ ] **M04/M05 删除**:确认外发资料_最新/ 删除后无业务依赖
- [ ] **M07/M08 移动**:确认 Market/ 目录定位(Marketing Guideline 仍引用旧路径)
- [ ] **M09 移动**:扫描 `[[EDGE_INFERENCE_*.md]]` 引用
- [ ] **M11 移动**:扫描 `[[AGENTS]]` 引用(根级)vs `[[AGENTS/index]]`(目录)
- [ ] **M13 决定**:review `KB/_COMMON/PRODUCTS_MDC.md` 是否过期
- [ ] **gitignore 检查**:确认 M01-M03/M07-M10 的目标文件不在 gitignored 列表(如 design 文件、.md 后缀过滤等)
- [ ] **External 目录**:在 git 中是否需独立 .gitignore 规则?目前根 .gitignore 不限制 `External/`
- [ ] **CN/EN 同步**:EN/CN 配对文件必须同步移动、同步发布、版本号一致

### 8.1 git 跟踪 vs gitignore 区分

> **关键提示**:`.gitignore` 屏蔽区改动不入 git,无副作用;git 跟踪区改动会进 git,需要 review。

- **gitignored(改动安全)**:DESIGN/、COOLING/DESIGN/、Busbar/Suppliers/、UPS/Suppliers/、Business_Documents/、Canvas/、Market/、HRBP/、COST/、Projects/、Solutions Design/、FOG_Workspace_Summary.md、Token_Calc_*.xlsx、generate_token_calc.py、memory/、.openclaw/、.claude/
- **git 跟踪(改动需 review)**:KB/ 下的大部分 Guideline / 3rd Party List / STD_Supplier / IMMERSION / LIQUID/L1240C45 / _archive / Reference Architecture(部分)、AGENTS/、PROCESS/、TOOLS/、CLAUDE.md、PRINCIPLES.md、SOUL.md、IDENTITY.md、USER.md、HEARTBEAT.md、VERSION.md

---

## 9. 总结(给 Yuri 的 review 建议)

**推荐分阶段执行**:

**Phase 1(低风险,先做)**:
- M04/M05 删除重复旧版 Tech Spec
- M06 清理外发资料_最新/index.md(已无内容)
- M11 合并根级 AGENTS.md 到 AGENTS/index.md
- M12 把 FOG_Workspace_Summary.md 移到 Admin/
- M18/M19 创建缺失的 index.md 占位

**Phase 2(中风险,需要扫引用)**:
- M07/M08 移动 Market/ → External/Marketing/
- M09 移动 Reference Architecture/ → External/Reference_Architecture/
- M03 移动 PITCH DECK Flyer → External/Pitch/
- M10 移动 PQTech 采访稿 → External/Media/

**Phase 3(高风险,大改 External 结构)**:
- M01/M02 移动 DC45 Tech Spec → External/Tech_Spec/
- M14-M16 移动 PRODUCTS/ 下的对外件 → External/Datasheet/
- 整体引入 `External/` 顶层目录

**不做**(避免过度 re-org):
- 根级元文档(CLAUDE.md 等)不动
- AGENTS/、PROCESS/、TOOLS/ 不动
- KB/ 内部 Guideline 与 3RD-PARTY 不动(它们的 Internal 定位正确)
- Project 目录结构不动(项目命名空间稳定更重要)
- `ResoucePool` 拼写不动(gitignore 依赖)

---

## 10. 决策请求

Yuri 看完后,决定:

1. **是否启动 re-org?** YES
2. **是否采纳全部建议?还是只采纳 Phase 1?** YES
3. **是否有其他文档想重新归类?** YES
4. **新顶层 `External/` 目录名是否合适?**(备选:`Public/` / `Outbound/` / `_external/`) PUBLIC
5. **`KB/LIQUID/L1240C45/PRODUCTS/DC45 Tech Spec` 路径是否拆分为 External/?** —— 这是改动最大的部分 YES

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| v0.1 | 2026-06-18 | 初稿:扫描 vault 全量文件,生成 External/Internal 分类与重新组织建议,等待 Yuri review。 |
| v0.2 | 2026-08-30 | 产品口径对齐 2026-08-30 基线:§2 目录树 IMMERSION / LIQUID 注释改为两条产品线 + 六 SKU 新码;§4 External 清单 E01–E05 / E18 的用途列改用新码。§5–§10 重组建议与决策请求、`_archive/` 描述、文件名(含 `Token_Calc_AC40_DC45_Haiyan.xlsx`)中的旧名作为时点记录保留。 |
