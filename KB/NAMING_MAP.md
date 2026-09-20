---
tags:
  - "#workspace/engineer"
  - "#type/reference"
  - #MDC
doc_version: v1.1
updated: 2026-08-30
---
# KB 命名基准 — 旧名 ↔ 新名

> **基准来源（唯一权威）：** MDC 站点仓库 `docs/rules/NAMING.md`（Locked · D-11）与 `docs/PRODUCT-MATRIX.md`（Locked · D-13）。
> KB 不自行定义 SKU；本表只做映射。**Agent 不得自造 SKU 码。**

## 1. 产品线

| 旧称 | 新称（对客） | 线码 | KB 目录 |
|---|---|---|---|
| FOG D Series · DLC · Direct Liquid Cooling | **Liquid Cooling** | `L` | `KB/LIQUID/` |
| FOG A Series · Immersion · AC-line | **Immersion Cooling** | `I` | `KB/IMMERSION/` |

## 2. 产品

| KB 旧名 | 短别名（目录/文件名用） | 全 SKU ID | 线 | IT kW | 尺寸 | 状态 | KB 目录 |
|---|---|---|---|---|---|---|---|
| DC45 | **L1240C45** | `L1240C45SUR150` | Liquid | 1240 | 45ft | shipped | `KB/LIQUID/L1240C45/` ^mdc-ae8ee12a95 |
| — | **L1800C45** | `L1800C45DR220` | Liquid | 1800 | 45ft | shipped | `KB/LIQUID/L1800C45/` ^mdc-bb13d4357a |
| — | **L450C20** | `L450C20DR150` | Liquid | 450 | 20ft | shipped | `KB/LIQUID/L450C20/` ^mdc-65e13c271c |
| AC45 | **I400C45** | `I400C45SUT50` | Immersion | 400 | 45ft | shipped | `KB/IMMERSION/I400C45/` ^mdc-61027cb923 |
| AC40 | **I400C40** | `I400C40ST50` | Immersion | 400 | 40ft | shipped | `KB/IMMERSION/I400C40/` ^mdc-1fbb0ef3aa |
| AC20 | **I200C20** | `I200C20ST50` | Immersion | 200 | 20ft | shipped | `KB/IMMERSION/I200C20/` ^mdc-fe5c1accb9 |
| A32 | **I50TS** | `I50TS` | Immersion | 50 (max) | 单槽 | 组件 | `KB/IMMERSION/I50TS/` ^mdc-e065faf7fe |

### I50TS 的推导（KB 侧新增，需站点侧确认） ^mdc-2a8e4c8e48

A32 未出现在 `docs/PRODUCT-MATRIX.md` 中。按 `NAMING.md §2.5` 独立槽体正则 ^mdc-a5a1422290
`^[LI][1-9][0-9]*T[SD]U?$` 推导：**I**（浸没）+ **50**（IT Load 50 kW Max，见
[[I50TS Technical Requirement]]）+ **T**（Tank 格式，无尺寸段、无密度段）+ **S**（单环路）+ 无 `U`（不含 UPS） ^mdc-007245510c
→ **`I50TS`**。 ^mdc-6d2bbb499e

> ⚠️ **待办：** 此码尚未写入 MDC `docs/PRODUCT-MATRIX.md` 的 Alias registry。上线对客材料前需由站点侧锁定。

## 3. 显示规则（D-13）

对客界面一律「友好标题 + 括号内短别名」，全 SKU 小字在下：

```
1240 Liquid Cooling Container with UPS (L1240C45) ^mdc-70d784ce18
L1240C45SUR150 ^mdc-217718d854
45 ft · up to 150 kW/rack
```

- SKU ID 与短别名**不翻译**（中英同码）。
- 改动 功率 / 环路 / UPS / 密度 / 尺寸 ⇒ **新 SKU ID**，旧码转 `archived`，不得原地改义。

## 4. 本次迁移未改动的部分

- **正文行文**中出现的旧名（DC45 / AC40 / AC45 / A32）在历史档案、供应商往来、Projects 记录里属事实记录，**保留原样**。 ^mdc-174e3779b9
- **SVG 图纸内的文字标签**（`I400C40 Layout_v1.svg` 等）仍为旧名，需重出图。 ^mdc-4ccf5c9bd5
- `_to_delete/` 下为迁移后清空的旧目录壳，确认无误后手工删除。

---

## Changelog

| 日期 | 变更 |
|---|---|
| 2026-08-17 | 首版。按 MDC `NAMING.md` D-11 / `PRODUCT-MATRIX.md` D-13 重排 KB 产品目录 |
| 2026-08-30 | §2 状态列 draft → shipped（L1800C45 / L450C20 / I200C20），对齐 `PRODUCT-MATRIX.md` §5 D-19 gate（2026-08-27） |
