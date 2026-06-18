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

## 目录结构

| 子目录 | 内容 | 状态 |
|--------|------|------|
| `PUBLIC/Tech_Spec/` | DC45 Tech Spec EN/CN + `_blocks/` 14 块 | Phase 2 ✅ |
| `PUBLIC/Products/` | A32 / AC40 / AC45 PRD + `_blocks/` | Phase 2 ✅ |
| `PUBLIC/Reference_Architecture/` | RA-001 (Immersion 0.4MW) / RA-002 (DLC 1.2MW) / Site Reference Climate | Phase 2 ✅ |
| `PUBLIC/Pitch/` | PITCH DECK Flyer | Phase 2 ✅ |
| `PUBLIC/Media/` | PQTech 采访稿 v2 + `_blocks/PQTech_Interview/` | Phase 2 ✅ |

## Phase 2 移动清单 (2026-06-18)

**已迁出 / 源位置已空:**

| # | 原路径 | 新路径 | 备注 |
|---|--------|--------|------|
| 1 | `KB/FOG D Series/PRODUCTS/DC45 Tech Spec EN.md` | `PUBLIC/Tech_Spec/DC45_Tech_Spec_EN.md` | 重命名(空格 → 下划线) |
| 2 | `KB/FOG D Series/PRODUCTS/DC45 Tech Spec CN.md` | `PUBLIC/Tech_Spec/DC45_Tech_Spec_CN.md` | 重命名 |
| 3 | `KB/FOG D Series/PRODUCTS/_blocks/DC45_Tech_Spec_EN/` | `PUBLIC/Tech_Spec/_blocks/DC45_Tech_Spec_EN/` | 14 块 |
| 4 | `KB/FOG D Series/PRODUCTS/_blocks/DC45_Tech_Spec_CN/` | `PUBLIC/Tech_Spec/_blocks/DC45_Tech_Spec_CN/` | 14 块 |
| 5 | `KB/FOG A Series/PRODUCTS_A32.md` | `PUBLIC/Products/A32.md` | 重命名(短名) |
| 6 | `KB/FOG A Series/PRODUCTS_AC40.md` | `PUBLIC/Products/AC40.md` | 重命名(短名) |
| 7 | `KB/FOG A Series/PRODUCTS_AC45.md` | `PUBLIC/Products/AC45.md` | 重命名(短名) |
| 8 | `KB/FOG A Series/_blocks/PRODUCTS_A{32,40,45}/` | `PUBLIC/Products/_blocks/PRODUCTS_A{32,40,45}/` | 6+6+7=19 块 |
| 9 | `Reference Architecture/EDGE_INFERENCE_IMMERSION_0.4MW.md` | `PUBLIC/Reference_Architecture/RA-001_Immersion_0.4MW.md` | 重命名为 RA-001 |
| 10 | `Reference Architecture/EDGE_INFERENCE_DLC_1.2MW.md` | `PUBLIC/Reference_Architecture/RA-002_DLC_1.2MW.md` | 重命名为 RA-002 |
| 11 | `Reference Architecture/Site_Reference_Climate_Standard.md` | `PUBLIC/Reference_Architecture/Site_Reference_Climate_Standard.md` | 名称不变 |
| 12 | `Business_Documents/PITCH DECK Flyer.md` | `PUBLIC/Pitch/PITCH_DECK_Flyer.md` | 重命名(空格 → 下划线) |
| 13 | `Projects/PQTech/采访稿_新版.md` | `PUBLIC/Media/PQTech_Interview_v2.md` | 重命名为 v2 |
| 14 | `Projects/PQTech/_blocks/PQTech_Interview/` | `PUBLIC/Media/_blocks/PQTech_Interview/` | 5 块 |

**未动(Phase 3 决策):**
- `Projects/外发资料_最新/DC45 Tech Spec {EN,CN}.md` (V1.3 旧副本,疑似重复)
- `Market/Market_Report.md` (内部周报,非对外)
- `Market/Diablo_400_市场分析报告.md` (本期未在范围内)
- `KB/FOG D Series/PRODUCTS/MDC Engineering Handbook External.md` (已用 External 命名,实际属 KB 内)

## 跨引用更新

- 82 处 wikilink 替换(51 个 .md 文件),主要在 `MDC_Handbook_Index.md` (10)、`KB/FOG D Series/PRODUCTS/index.md` (7)、`Document Tree.md` (4)、`KB/PRODUCTS_MDC.md` (3) 等
- 52 个块文件 frontmatter `source_file:` 字段已更新
- 19 个 A 系列块文件 `parent: [[../PRODUCTS_Axx]]` 已更新为短名
- 5 个 PQTech 块文件 `parent: [[../../采访稿_新版]]` 已更新为 `[[PQTech_Interview_v2]]`
- 2 个 DC45 Tech Spec 父文件中 `[[../DESIGN/...]]` 相对路径修复(改为 vault 相对路径)

## 内部对照

- 内部知识库入口:[[../index|FOG index]] · [[../KB/index|KB index]]
- Tech Spec 旧副本:见 `Projects/外发资料_最新/`(Phase 3 决定删除或保留)
- Reference Architecture 旧顶层目录:已空(仅 `index.md` + `Proposal_Canvas_Template.canvas` + `Icon`)

## 命名与目录约定

- 顶层子目录按**文档类型**组织(产品 / 架构 / 营销),不按产品线。
- 内部资料**禁止**复制进 `PUBLIC/`;下放时由 ATS 审核去敏。
- `PUBLIC/README.md` 是唯一索引,新内容必须在此登记。
- 重命名规则:文件名无空格,使用下划线分隔(例:`DC45_Tech_Spec_EN.md`)。
- RA 编号:RA-001 / RA-002 / ...(按入库顺序)。

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| v1.0 | 2026-06-18 | 骨架建立(Phase 1)。待 Phase 2/3 决定 Tech Spec / RA / Pitch 搬迁。 |
| v1.1 | 2026-06-18 | Phase 2 完成:DC45 Tech Spec (EN+CN, 28 块) / A32-AC40-AC45 (19 块) / 3 RA / Pitch / PQTech 采访稿全部迁入。82 处 wikilink 更新。 |

---

*Document Version: v1.1 | Last Updated: 2026-06-18*
