---
type: meta
title: "FOG Hot Cache"
updated: 2026-08-30T00:00:00Z
tags:
  - #workspace/engineer
  - #type/heartbeat
  - #system/feis
---

# FOG — Hot Cache

> **谁在用：** FOG 工作区里任何 Agent / 任何外部 Claude 会话读 vault 时，先看这份 ~500 字摘要，再决定要不要深读。

## Last Updated
2026-08-30. **产品口径基线同步**：六个 SKU **全部 `shipped`** —— 站点 `docs/PRODUCT-MATRIX.md` §5 的 D-19 gate（2026-08-27）一次性放行原为 draft 的 I200C20 / L1800C45 / L450C20；治理层与导航层（CLAUDE.md / _navigation.md / README / PRINCIPLES / SOUL / AGENTS）的产品线与状态表述已同步。同时新增 [[UNCONFIRMED_Convention]] `#unconfirmed` 标注规范（文档级 / 章节级 / 行级三粒度 + ✅ / 🔶 derived / ⏳ #unconfirmed / ⛔ conflict 四级置信度），六 SKU 规格唯一上游为 [[PRODUCT_SPEC_BASELINE]]。

2026-06-24. 重建 transport（obsidian-cli v0.2.3 已绑定 YurimengKB）+ 写完本 hot cache；扫描了 FOG 全部灵魂层文件（IDENTITY/SOUL/PRINCIPLES/AGENTS/PROCESS/KB 入口/Projects 索引）。

## FOG 一句话
**FEIS** — Fog Engineering Intelligence System。Fog Computing 模块化边缘数据中心（MDC/浸没/DLC/Edge AI）的**售前工程决策中枢**，不是聊天机器人。范围硬约束：**不报价 / 仅 KB 内产品 / IT Load vs Total Load 必区分 / UPS≠BESS / 改 KB 或 Projects 先问 Yuri**。

## 灵魂层 wiki 页（已存在，可直接引用）
- [[MDC/README]] — 工作区总览 + 12 条原则摘要 + 9 Agent 角色表 + 7 阶段工作流
- [[MDC/IDENTITY]] — FEIS 系统身份（v1.2，2026-05-19）
- [[MDC/SOUL]] — 工程哲学（13 条灵魂条款 + BOOTSTRAP 启动顺序 + 模式识别 + 价格拦截）
- [[PRINCIPLES]] — 12 条工程原则 v1.2（Reliability / Simplicity / Modular / Thermal / Edge / Standard / NO PRICE / IT-vs-Total / Decision Priority / KB Access / Customer File / Reference Architecture First）
- [[MDC/AGENTS]] — 9 Agent 组织图 + 决策权威层级
- [[MDC/HEARTBEAT]] — 心跳钩子（当前为空）
- [[index]] — FOG 子目录总索引
- [[project_list]] — 活跃项目快照（8 活跃 / 2 Closed / 3 需补 Project_Record）

## 当前活跃项目（2026-06-18 快照）
- **自建算力项目**（Fog + BTCT/德同/周鸿祎/BILT）— 试点 0.5–10MW，BTCT 方案基本完成（0611）
- **BILT_Finland_70MW** — 20+50MW DC45，等待上游供电方案 12 周
- **Phoenix_Global** — Abu Dhabi 240MW + Oman 27MW 加密转 AI，拒绝浸没坚持 DLC
- **PQTech** — 上海张江 1.2MW/H200 AC40
- **Simple_Mining** — Iowa DC45 Pair，consulting 合同待签
- **Logy_Computer** — 哈萨克斯坦阿拉木图 DC45，PUE 1.4× 上限
- **8th_Power** — 美 500kW AC40+RTX PRO 6000S，关注 UL/CSA 合规
- 待补 Project_Record：Clutch_40MW / RiCloud / BTCT

## KB 子区入口
`FOG/KB/` 下：3RD-PARTY / IMMERSION / LIQUID / Guideline / _COMMON（PRODUCTS_MDC.md · PRODUCT_SPEC_BASELINE.md · UNCONFIRMED_Convention.md）/ NAMING_MAP.md
**两条产品线，六 SKU 全部 `shipped`**（命名基准 [[NAMING_MAP]]，规格基准 [[PRODUCT_SPEC_BASELINE]]）：
- **Liquid Cooling**（线码 `L`，[[KB/LIQUID/index]]）：L1240C45 · L1800C45 · L450C20
- **Immersion Cooling**（线码 `I`，[[KB/IMMERSION/index]]）：I400C45 · I400C40 · I200C20，另有 I50TS 浸没槽体**组件**（非 SKU，站点 Alias registry 未收录 ⏳ #unconfirmed）
- 旧名对照：DC45→L1240C45 · AC45→I400C45 · AC40→I400C40 · AC20→I200C20 · A32→I50TS。旧名只在 `_archive/` / `Projects/` / 供应商往来里作为历史记录保留。
**注意：** FOG 内部有两套命名并行 —— KB/ 这套是 README.md 和 SOUL/IDENTITY 用的；`FOG/01_Agents/`、`FOG/02_Products/` 这套数字前缀路径被 `_inventory_FOG.md` 用，是另一个目录（417 md 文件）。两者都需要从 [[MDC/index]] 出发，不要假设某个产品文件路径。

## 结构化事实层（不是 wiki，但是事实源）
**`FOG/graphify-out/`** —— AST-only 的知识图谱，**0 token cost** 自动生成（2026-06-24）
- `graph.json` (622KB)：**713 节点 / 711 links / 87 community / 41 hyperedges**
  - 节点类型：402 concept · 248 document · 30 rationale · 20 image · 11 paper · 2 code
  - link 关系：`references` / `conceptually_related_to` 等，带 `EXTRACTED`(1.0) 或 `INFERRED`(0.84–0.95) confidence
- `GRAPH_REPORT.md` (39KB)：人类可读报告，含 Community Hubs / God Nodes / Surprising Connections / Hyperedges
- `.graphify_labels.json`：87 community 的 id→名字映射
- `manifest.json`：每个 .md 的 mtime + ast_hash（用来检测变更）
- **职责分工**：wiki 页 = 描述"是什么 / 为什么"（人类语义）；graph.json = "哪些文件 / 概念 / 节点互相引用"（机器结构）。**两者不复制事实**——wiki 写人类判断，graph 存文件级引用关系。
- **冲突规则**：当 wiki 页与 graph 节点标签冲突时，**以 wiki 页正文为准**（wiki 是最终语义）；graph 只用作"导航发现"和"关系搜索"，不是事实裁判。
- 重生成：`cd FOG && graphify update .`（AST-only，0 token cost）
- **速查页** [[_graph_index]]（按 13 主题分组：A_FEIS / B_Product / C_Cooling / D_Power / E_Network / F_Compliance / G_Cost / H_Workflow / I_Vendors / J_Project / K_Layout / L_Guidelines_Meta / M_Marketing）

## Active Threads
- 用户（Yuri）当前在做的事：让 WIKI 了解 FOG 工作区 → 引导到 graphify 作为事实源，避免双库冲突
- 本会话已建 transport、扫描灵魂层、写 hot.md + _navigation.md，下一步：建 communities 速查页引用 graph.json
- 待确认：是否要把 FOG 内 `01_Agents/02_Products/03_Solutions/04_Processes/05_Projects/99_Internal/` 这套数字前缀目录并入 wiki 体系，还是保持现状
- 待确认：FOG/KB/ 与 FOG/02_Products/ 是否功能重复（inventory 显示部分内容同名 dup）
- 待确认：graph.html 是 553KB 的可视图，是否需要在 README 里加一个链接供 Obsidian 内部打开