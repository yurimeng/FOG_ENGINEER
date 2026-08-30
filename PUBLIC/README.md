---
tags:
  - "#workspace/engineer"
  - "#type/index"
  - "#MDC"
audience: 人 + 工程师 + AI
---
# PUBLIC / README — 对外发布资料入口

> 本目录用于存放**对外可发布**的工程资料(客户、合作伙伴、公开渠道)。
> 与内部知识库 `KB/` 严格分离:内部设计稿、评估、模板归档在 `KB/`,成稿后下放到 `PUBLIC/`。
>
> **产品口径:** 两条产品线 —— **Liquid Cooling**(`L`)L1240C45 · L1800C45 · L450C20，**Immersion Cooling**(`I`)I400C45 · I400C40 · I200C20，六 SKU **全部 `shipped`**(站点 `docs/PRODUCT-MATRIX.md` §5 D-19 gate · 2026-08-27);另有 I50TS 浸没槽体**组件**。命名基准 [[NAMING_MAP]],规格基准 [[PRODUCT_SPEC_BASELINE]]。
> 下方「Phase 2 移动清单」「跨引用更新」与 Changelog 中的旧名(A32 / AC40 / AC45 / DC45)属**迁移历史记录**,保留原样。

## 目录结构

| 子目录 | 内容 | 状态 |
|--------|------|------|
| `PUBLIC/Tech_Spec/` | 六 SKU Tech Spec CN/EN/External —— Liquid Cooling：`L1240C45_*` · `L1800C45_*` · `L450C20_*`；Immersion Cooling：`I400C45_*` · `I400C40_*` · `I200C20_*`；含 `_blocks/` 分块 | 六 SKU 齐备 ✅ |
| `PUBLIC/Products/` | I50TS / I400C40 / I400C45 PRD + `_blocks/` | Phase 2 ✅ |
| `PUBLIC/Reference_Architecture/` | RA-001 (Immersion Cooling 0.4MW · I400C40) / RA-002 (Liquid Cooling 1.2MW · L1240C45) / RA-003 (Immersion Cooling 0.2MW All-in-One · I200C20) / Site Reference Climate | Phase 2 ✅ / RA-003 增补 ✅ |
| `PUBLIC/Pitch/` | PITCH DECK Flyer | Phase 2 ✅ |
| `PUBLIC/Media/` | PQTech 采访稿 v2 + `_blocks/PQTech_Interview/` | Phase 2 ✅ |

## Phase 2 移动清单 (2026-06-18)

**已迁出 / 源位置已空:**

| # | 原路径 | 新路径 | 备注 |
|---|--------|--------|------|
| 1 | `KB/LIQUID/L1240C45/PRODUCTS/L1240C45 Tech Spec EN.md` | `PUBLIC/Tech_Spec/L1240C45_Tech_Spec_EN.md` | 重命名(空格 → 下划线) |
| 2 | `KB/LIQUID/L1240C45/PRODUCTS/L1240C45 Tech Spec CN.md` | `PUBLIC/Tech_Spec/L1240C45_Tech_Spec_CN.md` | 重命名 |
| 3 | `KB/LIQUID/L1240C45/PRODUCTS/_blocks/L1240C45_Tech_Spec_EN/` | `PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_EN/` | 14 块 |
| 4 | `KB/LIQUID/L1240C45/PRODUCTS/_blocks/L1240C45_Tech_Spec_CN/` | `PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/` | 14 块 |
| 5 | `KB/IMMERSION/PRODUCTS_I50TS.md` | `PUBLIC/Products/I50TS.md` | 重命名(短名) |
| 6 | `KB/IMMERSION/PRODUCTS_I400C40.md` | `PUBLIC/Products/I400C40.md` | 重命名(短名) |
| 7 | `KB/IMMERSION/PRODUCTS_I400C45.md` | `PUBLIC/Products/I400C45.md` | 重命名(短名) |
| 8 | `KB/IMMERSION/_blocks/PRODUCTS_A{32,40,45}/` | `PUBLIC/Products/_blocks/PRODUCTS_A{32,40,45}/` | 6+6+7=19 块 |
| 9 | `Reference Architecture/EDGE_INFERENCE_IMMERSION_0.4MW.md` | `PUBLIC/Reference_Architecture/RA-001_Immersion_0.4MW.md` | 重命名为 RA-001 |
| 10 | `Reference Architecture/EDGE_INFERENCE_DLC_1.2MW.md` | `PUBLIC/Reference_Architecture/RA-002_Liquid_1.2MW.md` | 重命名为 RA-002 |
| 11 | `Reference Architecture/Site_Reference_Climate_Standard.md` | `PUBLIC/Reference_Architecture/Site_Reference_Climate_Standard.md` | 名称不变 |
| 12 | `Business_Documents/PITCH DECK Flyer.md` | `PUBLIC/Pitch/PITCH_DECK_Flyer.md` | 重命名(空格 → 下划线) |
| 13 | `Projects/PQTech/采访稿_新版.md` | `PUBLIC/Media/PQTech_Interview_v2.md` | 重命名为 v2 |
| 14 | `Projects/PQTech/_blocks/PQTech_Interview/` | `PUBLIC/Media/_blocks/PQTech_Interview/` | 5 块 |

**未动(Phase 3 决策):**
- `Projects/外发资料_最新/DC45 Tech Spec {EN,CN}.md` (V1.3 旧副本,疑似重复)
- `Market/Market_Report.md` (内部周报,非对外)
- `Market/Diablo_400_市场分析报告.md` (本期未在范围内)
- `KB/_COMMON/MDC Engineering Handbook External.md` (已用 External 命名,实际属 KB 内)

## 跨引用更新

- 82 处 wikilink 替换(51 个 .md 文件),主要在 `MDC_Handbook_Index.md` (10)、`KB/LIQUID/L1240C45/PRODUCTS/index.md` (7)、`Document Tree.md` (4)、`KB/_COMMON/PRODUCTS_MDC.md` (3) 等
- 52 个块文件 frontmatter `source_file:` 字段已更新
- 19 个 A 系列块文件 `parent: [[../PRODUCTS_Axx]]` 已更新为短名
- 5 个 PQTech 块文件 `parent: [[../../采访稿_新版]]` 已更新为 `[[PQTech_Interview_v2]]`
- 2 个 DC45 Tech Spec 父文件中 `[[../DESIGN/...]]` 相对路径修复(改为 vault 相对路径)

## 内部对照

- 内部知识库入口:[[MDC/index|FOG index]] · [[MDC/KB/index|KB index]]
- Tech Spec 旧副本:见 `Projects/外发资料_最新/`(Phase 3 决定删除或保留)
- Reference Architecture 旧顶层目录:已空(仅 `index.md` + `Proposal_Canvas_Template.canvas` + `Icon`)

## 命名与目录约定

- 顶层子目录按**文档类型**组织(产品 / 架构 / 营销),不按产品线。
- 内部资料**禁止**复制进 `PUBLIC/`;下放时由 ATS 审核去敏。
- `PUBLIC/README.md` 是唯一索引,新内容必须在此登记。
- 重命名规则:文件名无空格,使用下划线分隔(例:`L1240C45_Tech_Spec_EN.md`)。
- RA 编号:RA-001 / RA-002 / ...(按入库顺序)。

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| v1.0 | 2026-06-18 | 骨架建立(Phase 1)。待 Phase 2/3 决定 Tech Spec / RA / Pitch 搬迁。 |
| v1.1 | 2026-06-18 | Phase 2 完成:DC45 Tech Spec (EN+CN, 28 块) / A32-AC40-AC45 (19 块) / 3 RA / Pitch / PQTech 采访稿全部迁入。82 处 wikilink 更新。 |
| v1.2 | 2026-07-28 | 新增 AC40 Tech Spec CN/EN（与 DC45 同构 14 节 + 28 块），入口 `PUBLIC/Tech_Spec/AC40_Tech_Spec_{CN,EN}.md`。 |
| v1.3 | 2026-08-30 | 目录结构表对齐 2026-08-30 产品基线：Tech_Spec 改为六 SKU CN/EN/External 列举、Products 改用 I50TS / I400C40 / I400C45 新码、Reference_Architecture 补 RA-003 并标注对应 SKU；文首加产品口径说明。迁移清单与 Changelog 历史条目未改。 |

---

*Document Version: v1.3 | Last Updated: 2026-08-30*
