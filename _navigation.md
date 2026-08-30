---
type: overview
title: "FOG Wiki-style Navigation"
updated: 2026-08-30T00:00:00Z
tags:
  - #workspace/engineer
  - #type/navigation
  - #system/feis
---

# FOG — Wiki-style Navigation

> FOG 内部已经有一个隐式的 wiki（README/IDENTITY/SOUL/PRINCIPLES/AGENTS/PROCESS/KB/Projects）。本文件是**导航总图**：把所有可作为 wiki 入口的页面用统一约定串起来，避免下游 Agent 找不到起点。
>
> 入口原则：**永远从 [[MDC/index]] 出发**，再用本文件定位到具体子域。

---

## 1. 灵魂层（启动必读）

启动顺序（来自 [[MDC/SOUL]] §BOOTSTRAP）：

```
1. [[IDENTITY]]         → 系统身份 FEIS
2. [[SOUL]]             → 工程哲学 + 启动规则 + 模式识别 + 价格拦截
3. [[PRINCIPLES]]       → 12 条工程原则（最高准则）
4. [[AGENTS]]           → 9 角色组织 + 决策权威
5. [[HEARTBEAT]]        → 心跳钩子（当前空）
6. [[README]]           → 工作区总览（principles 摘要 + 角色表 + 工作流）
```

⚠️ **每次回复前自检：** 不报价 / 不推 KB 外产品 / 不混 IT vs Total Load / UPS vs BESS / 改 KB 或 Projects 先问 Yuri

---

## 2. 子域入口（按业务域）

| 域 | 入口 | 用途 |
|----|------|------|
| 角色 | [[MDC/AGENTS]] → [[AM]] / [[ATS]] / [[Cooling Engineer]] / [[Power Engineer]] / [[Layout Planner]] / [[Cost Architect]] / [[Compliance Officer]] / [[Risk Auditor]] / [[Market Researcher]] | 9 个 Agent 角色定义 |
| 工作流 | [[WORKFLOW]] | 7 阶段工程工作流（Lead Qual → Discovery → Requirement → Arch → Engineering → Governance → Proposal） |
| 流程 | [[MDC/PROCESS/index]] → [[PROCESS/AM/]] / [[PROCESS/ATS/]] / [[PROCESS/SUPPORT/]] | AM/ATS/支持流程 |
| 产品 KB | [[MDC/KB/index]] → [[KB/LIQUID/index]] / [[KB/IMMERSION/index]] · [[_COMMON/PRODUCTS_MDC]] | 产品手册入口。两条线：**Liquid Cooling**（`L`）L1240C45 · L1800C45 · L450C20；**Immersion Cooling**（`I`）I400C45 · I400C40 · I200C20（六 SKU 均 shipped）+ I50TS 槽体组件 |
| 产品基准 | [[PRODUCT_SPEC_BASELINE]] · [[NAMING_MAP]] · [[UNCONFIRMED_Convention]] | 六 SKU 规格唯一上游 · 旧名↔新名映射 · `#unconfirmed` 标注规范 |
| 第三方 KB | [[MDC/KB/3RD-PARTY/index]] → [[3rd Party List]] | BESS / Busbar / COOLING / NETWORK / UPS 第三方清单 |
| 技术指南 | [[MDC/KB/Guideline/index]] → COOLING / POWER_SYSTEMS / LAYOUT / COMPLIANCE / RISK / COST / MARKETING | 7 个领域 Guideline |
| 参考架构 | [[MDC/Reference Architecture/index]] → RA-001 (0.4MW 浸没) / RA-002 (1.2MW DLC) | 已验证的预工程配置 |
| 工具 | [[MDC/TOOLS/TOOLS]] → [[CRM_WORKFLOW]] / [[KB_ACCESS]] / [[QUOTE_ENGINE]] | CRM/KB 访问/报价引擎（商务专用）|
| 项目 | [[project_list]] → 各项目目录 | 客户项目（修改需 Yuri 确认）|
| 方案设计 | [[Solutions Design/index]] | 方案设计稿 |
| 画布 | [[KB_Relation.canvas]] | KB 关系图 |

---

## 3. 关键约束速查

- **NO PRICE** — [[PRINCIPLES]] §7 / [[MDC/SOUL]] §13 / [[MDC/CLAUDE]] §1.1。任何价格询问回复："配置方案由我提供，价格由商务团队根据您确认的配置单独核算。请联系您的客户经理获取正式报价。"
- **KB-only products** — [[PRINCIPLES]] §3 / [[MDC/CLAUDE]] §1.2
- **IT Load vs Total Facility Load** — [[PRINCIPLES]] §8 / [[MDC/SOUL]] §12。例：L1240C45 单箱 IT=1240kW；Total Facility Load 随 PUE 变化，逐站点用 <https://mdcx.org> 计算（PUE 一律写 `1.0x`）
- **Decision Priority** — Safety > Compliance > Reliability > Simplicity > Cost（[[PRINCIPLES]] §9）
- **Reference Architecture First** — [[PRINCIPLES]] §12；匹配就**直接采用**，禁止重设计
- **KB Access Protocol** — [[PRINCIPLES]] §10；Index-First 原则（任何 KB 操作先看 [[MDC/index]] → 子域 index → 具体文件）

---

## 4. 知识冲突优先级

来自 [[MDC/SOUL]] §BOOTSTRAP：
```
1. KNOWLEDGE_BASE（最高）
2. PROCESS
3. TOOLS
4. Memory 记录（最低）
```

---

## 5. 目录命名双轨说明 ⚠️

FOG 内部存在**两套并行目录命名**，下游 Agent 不要假设路径：

| 命名 | 位置 | 谁在用 |
|------|------|--------|
| `KB/`, `AGENTS/`, `PROCESS/`, `Projects/` | `FOG/KB/`、`FOG/AGENTS/`、`FOG/PROCESS/`、`FOG/Projects/` | README.md / SOUL / IDENTITY / PRINCIPLES / 根 CLAUDE.md |
| `01_Agents/02_Products/03_Solutions/04_Processes/05_Projects/99_Internal/` | `FOG/01_Agents/` 等 | `_inventory_FOG.md`（417 md 文件、325 唯一、80 dup 组）|

inventory 显示两套之间有**重复内容**（如 SPEC 文档、AGENTS 角色定义）。如果你看到这两个路径下都有同名或近名文件，**不要假设是两份独立文档**——先 diff 一下，可能一份是归档版本（点前缀隐藏或 `_archive/`）。

---

## 6. 文档维护规则（来自 [[MDC/README]]）

| 变更类型 | 必同步 |
|---------|--------|
| KB 目录结构变更 | [[MDC/index]] + [[MDC/README]] |
| 新增流程文件 | [[WORKFLOW]] |
| 产品参数变更 | 对应 PRODUCTS_*.md |
| 重大系统变更 | [[VERSION]] |
| 客户档案变更 | [[CRM_WORKFLOW]] |

---

## 7. 此文件的使用约定

- `hot.md` = ~500 字**热缓存**（任何会话先读）
- `_navigation.md` = 跨子域**导航总图**（找到入口后再读具体 wiki 页）
- `_graph_index.md` = graph.json community 速查（**事实层**，本文件创建）
- 具体 wiki 页 = README / IDENTITY / SOUL / PRINCIPLES / AGENTS / PROCESS / KB / Projects（**已存在**，不要重新写）
- wiki-ingest 新内容时：先更新 `hot.md` 和 `_navigation.md`，再创建新页

---

## 8. 事实层：graphify-out（机器结构，权威引用图）

**和 wiki 是两套互补的层，不是重复：**

| 层 | 文件 | 角色 | 更新方式 |
|----|------|------|---------|
| **语义层（wiki）** | README / IDENTITY / SOUL / PRINCIPLES / AGENTS / hot.md / _navigation.md / _graph_index.md | "是什么 / 为什么"，人类可读 | Claude 维护 |
| **结构层（graph）** | `FOG/graphify-out/graph.json` + `GRAPH_REPORT.md` + `.graphify_labels.json` + `manifest.json` | "哪些文件/节点互相引用"，机器可读 | AST 解析，**0 token cost** |

**graph.json 当前状态（2026-06-24）：**
- 713 节点 / 711 links / 87 community / 41 hyperedges
- 节点类型分布：402 concept · 248 document · 30 rationale · 20 image · 11 paper · 2 code
- link confidence：`EXTRACTED` (1.0) / `INFERRED` (0.84–0.95)
- 关系类型：`references` / `conceptually_related_to` 等

**冲突解决规则：**
1. 当 wiki 页面与 graph 节点标签/分类冲突 → **以 wiki 正文为准**（graph 是导航工具，不是事实裁判）
2. 当 graph 显示两个文件互相引用、但 README 没说 → **看 graph**（它是引用发现工具）
3. graph 节点命名是 normalized（kebab-case），**不要拿 norm_label 当最终标签** —— 看 `label` 字段

**何时重新生成 graph：**
- FOG/ 下任何 .md 文件 mtime 变 → `cd FOG && graphify update .`（AST-only，0 token cost，几秒）
- 改完 KB/PRODUCTS 或 AGENTS 文件后建议跑一次，保持 manifest.json 同步

**目录约定：**
```
FOG/graphify-out/
├── graph.json              # 主图（622KB）
├── GRAPH_REPORT.md         # 人类可读报告（39KB，含 God Nodes / Surprising Connections）
├── graph.html              # 可视化（553KB，浏览器打开）
├── .graphify_labels.json   # community id→名字映射
├── manifest.json           # 每个 .md 的 mtime + ast_hash
├── cost.json               # 历次运行成本（一直 0）
└── cache/                  # 解析缓存
```

---

*Created: 2026-06-24 | Owner: FEIS bot | Last Updated: 2026-08-30*

> **2026-08-30 更新：** §2 产品 KB 入口改为两条产品线 + 六 SKU（全部 `shipped`，站点 `docs/PRODUCT-MATRIX.md` §5 D-19 gate · 2026-08-27），并补 [[KB/LIQUID/index]] / [[KB/IMMERSION/index]] 与产品基准入口；§3 IT-vs-Total 例子改用 L1240C45。