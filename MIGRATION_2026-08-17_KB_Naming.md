---
tags:
  - "#workspace/engineer"
  - "#type/report"
  - #MDC
doc_version: v1.0
updated: 2026-08-17
---
# MDC-KB 命名重整 迁移报告

**日期：** 2026-08-17
**基准：** MDC 站点仓库 `docs/rules/NAMING.md`（Locked · D-11）+ `docs/PRODUCT-MATRIX.md`（Locked · D-13）
**范围：** `KB/`、`PUBLIC/`，以及全仓指向它们的链接（`Projects/`、`AGENTS/`、`PROCESS/`、`Reference Architecture/` 等仅改链接，不改内容）
**决策档位：** B 档 —— 目录+文件名重命名、结构性引用全量同步；正文行文叙述中的旧名保留

---

## 1. 命名映射

### 1.1 产品线

| 旧称 | 新称（对客） | 线码 | KB 目录 |
|---|---|---|---|
| FOG D Series · DLC · Direct Liquid Cooling | **Liquid Cooling** | `L` | `KB/LIQUID/` |
| FOG A Series · Immersion · AC-line | **Immersion Cooling** | `I` | `KB/IMMERSION/` |

### 1.2 产品

| KB 旧名 | 短别名 | 全 SKU ID | 线 | IT kW | 尺寸 | 状态 | KB 目录 |
|---|---|---|---|---|---|---|---|
| DC45 | **L1240C45** | `L1240C45SUR150` | Liquid | 1240 | 45ft | shipped | `KB/LIQUID/L1240C45/` |
| — | **L1800C45** | `L1800C45DR220` | Liquid | 1800 | 45ft | draft | `KB/LIQUID/L1800C45/` |
| — | **L450C20** | `L450C20DR150` | Liquid | 450 | 20ft | draft | `KB/LIQUID/L450C20/` |
| AC45 | **I400C45** | `I400C45SUT50` | Immersion | 400 | 45ft | shipped | `KB/IMMERSION/I400C45/` |
| AC40 | **I400C40** | `I400C40ST50` | Immersion | 400 | 40ft | shipped | `KB/IMMERSION/I400C40/` |
| AC20 | **I200C20** | `I200C20ST50` | Immersion | 200 | 20ft | draft | `KB/IMMERSION/I200C20/` |
| A32 | **I50TS** ⚠️ | `I50TS` | Immersion | 50 max | 单槽 | 组件 | `KB/IMMERSION/I50TS/` |

⚠️ **`I50TS` 是本次新推导的码，站点侧尚未锁定。** A32 不在 `PRODUCT-MATRIX.md` 里。按 `NAMING.md §2.5`
独立槽体正则 `^[LI][1-9][0-9]*T[SD]U?$` 推：**I**（浸没）+ **50**（IT Load 50 kW Max，见
`I50TS Technical Requirement.md`）+ **T**（Tank 格式，无尺寸段、无密度段）+ **S**（单环路）+ 无 `U`（不含 UPS）。
**上对客材料前需由站点侧写入 Alias registry。**

---

## 2. 目录结构（迁移后）

```
KB/
├── NAMING_MAP.md                    ← 新建：旧名↔新名唯一映射
├── index.md                         ← 重写
├── LIQUID/                          ← 原 FOG D Series
│   ├── index.md                     ← 新建：产品线入口
│   ├── L1240C45/                    ← 原 FOG D Series 全部内容
│   │   ├── index.md
│   │   ├── DESIGN/                  (STD_L1240C45 / 准则 / 评估 / 合规 / PRD + _blocks)
│   │   ├── PRODUCTS/                (Tech Spec CN·EN / BOM / SLD / Racks)
│   │   ├── Layout/                  ← 原 "DC45 Layout/"
│   │   └── _archive/
│   ├── L1800C45/index.md            ← 新建 draft 占位
│   └── L450C20/index.md             ← 新建 draft 占位
├── IMMERSION/                       ← 原 FOG A Series
│   ├── index.md                     ← 重写
│   ├── I400C40/                     (工作负荷 / NETWORK_CONF / Layout)
│   ├── I400C45/                     (Layout)
│   ├── I200C20/index.md             ← 新建 draft 占位
│   ├── I50TS/                       (Technical Requirement / Flow)
│   └── _line/                       (PRODUCTS_NETWORK / CHANGELOG)
├── _COMMON/                         ← 新建：跨产品文档
│   ├── index.md
│   ├── PRODUCTS_MDC.md              ← 原 KB/PRODUCTS_MDC.md
│   ├── MDC Engineering Handbook.md          + _blocks/
│   ├── MDC Engineering Handbook External.md + _blocks/
│   ├── MDC_Handbook_Index.md
│   ├── MDC_Standards_Compilation.md
│   └── MDC_Product_Quick_Ref.md
├── 3RD-PARTY/                       ← 未动
└── Guideline/                       ← 未动

PUBLIC/
├── Products/  A32→I50TS.md · AC40→I400C40.md · AC45→I400C45.md（含 _blocks/PRODUCTS_*）
├── Tech_Spec/ AC40_→I400C40_ · DC45_→L1240C45_（CN/EN 各含 _blocks）
└── Reference_Architecture/ RA-002_DLC_1.2MW → RA-002_Liquid_1.2MW
```

---

## 3. 实际改动量

| 项 | 数量 |
|---|---|
| 目录 / 文件移动与重命名 | **69** |
| 结构性引用重写（wikilink、embed、`source_file:`、`parent:`、tag、canvas、yaml） | **约 1 600 处 / 290 个文件** |
| 新建入口文档 | **12**（NAMING_MAP + 各级 index） |
| 重写文档 | `CLAUDE.md`（硬规则 #2、#5、§0、§2）、`KB/index.md`、`PRODUCTS_MDC.md` 产品表 |
| 顺手修复的历史断链 | **8 处** |

### 3.1 `CLAUDE.md` 硬规则 #2 更新

```diff
- Only recommend products in the core line (A32 / AC40 / AC45 / DC45) …
+ Only recommend products in the core line —
+   Liquid Cooling: L1240C45 · L1800C45 · L450C20
+   Immersion Cooling: I400C45 · I400C40 · I200C20 · I50TS
+ — or listed in KB/3RD-PARTY/3rd Party List.md.
+ Naming baseline: KB/NAMING_MAP.md. Never invent SKU codes.
```

§2 同时从「所有规格在 `KB/PRODUCTS/`」（该路径本就不存在）改为按 **产品线 → SKU** 的实际路径表。

---

## 4. 验证

用链接解析器对**迁移前快照**与**迁移后**做同口径对比（解析 vault 相对路径、`../` 相对路径、
隐藏归档文件、多种扩展名）：

| | 断链种类 | 断链处数 |
|---|---|---|
| 迁移前 | 183 | 300 |
| 迁移后 | **177** | **292** |
| **净新增** | **0** | **0** |

- **本次迁移未产生任何新断链。**
- 另修复 8 处历史断链（`../../FOG A Series/PRODUCTS_AC40` 之类指错目录的链接、`SIDE.svg` 实为 `SIDE.jpg`）。
- 剩余 292 处断链为迁移前既有问题，主要是：指向点号隐藏归档文件（`CDU_Requirement v3.2`、
  `CRAH_Requirement v1.3`、`Hybrid Chiller Requirement 技术规格需求书`）、`Reference Architecture/` 下缺失的
  文档、以及 `Projects/天然气压差发电/` 的相对路径错误。**与本次改动无关，未处理。**

---

## 5. 遗留项 / 需要你决定

| # | 项 | 说明 |
|---|---|---|
| 1 | **`I50TS` 需站点侧确认** | 写入 MDC `docs/PRODUCT-MATRIX.md` 的 Alias registry 后才能上对客材料 |
| 2 | **git 未提交** | 本次改动全部在工作区。通过设备桥无法写 `.git/index.lock`（Operation not permitted），需你在本机 `git add -A && git commit` |
| 3 | **graphify 未重建** | 沙箱内无 graphify CLI 且无外网。需在本机 `graphify update .`，否则 `graphify-out/graph.json` 仍是旧路径 |
| 4 | **`_to_delete/`** | 迁移后清空的旧目录壳（`FOG D Series`、`FOG A Series`、`IMMERSION__stage`，仅剩 `.DS_Store` / `Icon`）。确认后手工删除——设备桥不允许删文件 |
| 5 | **SVG 图纸内文字仍是旧名** | `I400C40 Layout_v1.svg`、`I400C45 Layout_v1.svg`、`I50TS Flow_v1.svg`、`I400C40_NETWORK_CONF_v1.svg`，以及 `Projects/PQTech/…/_assets/AC40_Layout_v1.svg` 等。需重出图 |
| 6 | **对外交付件未改名** | `Projects/外发资料_最新/DC45 Tech Spec EN.md` 等已发给客户的文件保留原名（交付记录）。是否随新命名重新出版本由你定 |
| 7 | **正文旧名保留** | 按 B 档，历史档案（`_archive/`）、供应商往来、`Projects/` 记录里的 DC45 / AC40 / AC45 / A32 属事实记录，未逐句替换 |
| 8 | **仓库有 99 个迁移前就已修改未提交的文件** | 提交时注意区分：那部分不是本次改动 |

---

## Changelog

| 日期 | 变更 |
|---|---|
| 2026-08-17 | 首版。按 MDC `NAMING.md` D-11 / `PRODUCT-MATRIX.md` D-13 重排 KB 产品目录与命名 |
