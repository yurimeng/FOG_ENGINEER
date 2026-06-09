---
tags:
  - "#workspace/engineer"
  - "#type/standard"
  - "#domain/supplier"
  - "#scope/3rd-party"
  - #MDC
doc_version: v1.0
created: 2026-06-06
status: ACTIVE — 供应商管理体系(全 3RD-PARTY 类别)
audience: 工程师 + AI(读), 商务 + 售前(用)
---
# STD_Supplier — 供应商管理体系

> **Audience:** 主受众工程师 + AI(用于评审/对齐/追溯);次受众商务与售前(用于选型/推进/状态查询)。
> **No marketing text.** 不写"为什么选 Vertiv", 只列"已审/待审/缺口"。

## 0. 标准定位 ^std-supplier-0-positioning

本文档是 FOG 3RD-PARTY 区的**统一供应商管理体系入口**。覆盖:

```
STD_Supplier (本表)
   │
   ├── 跨类别: COOLING / POWER / NETWORK
   │
   ├── 行维度: 产品类别 × IT Zone (如 "CDU × DC45")
   │
   ├── 列维度: 要求 → 链接产品(PRD) → 解决方案(Reference Architecture) → 供应商 → 状态
   │
   ├── 横向引用 → [[../FOG D Series/DESIGN/STD_DC45]] 统一参数表
   │
   └── 未来扩展 → A Series / Design / STD (预留接口, 当前未建)
```

> **铁律:** 本文档**不**作为参数值书写处。参数值**只**出现在源文档(主要为 Requirement / PRD / Tech Spec)。
> 修改任何参数, 须先改源文档, 再回本文档更新引用地址。

---

## 1. 供应商管理体系表(Unified Supplier Table) ^std-supplier-1-table

> **读取规则:**
> - **要求:** 该 (产品类别 × IT Zone) 组合的核心技术/容量要求(摘要)。
> - **链接产品:** 跳转到供应商的售前产品文档(PRD-* / UPS_EATON / Gotion / Tesla / Siemens 等)。
> - **Reference Architecture:** 跳转到 KB 内已有的 Reference Architecture 文件, 表明"在哪个客户场景中用过/适用"。
> - **供应商名称:** 文本字段, 当前已选定的供应商品牌。
> - **状态:** `正在review`(已发需求/待回复) / `已经review完成`(基线锁定, 可入 BOM)。
>
> **本表是视图, 不是数据源。** 详细规格请点 "链接产品" 跳到源文档。

### 1.1 冷却子系统 ^std-supplier-1-1-cooling

| # | 要求(摘要)| 链接产品(PRD) | Reference Architecture | 供应商 | 状态 |
|---|---------|---------------|------------------------|--------|------|
| 1 ^std-row-1-cdu-dc45 | **CDU ≥ 1500 kW / PG25 二次侧** | [[COOLING/DESIGN/CDU_Requirement#^cdu-2-1-pump-spec\|CDU Requirement v3.1 §2.1]] | [[../../Reference Architecture/EDGE_INFERENCE_DLC_1.2MW]] | 待全球招标(Vertiv/同飞参考) | ⏳ 正在review (Q1 v3.0 重发待厂家回复) |
| 2 ^std-row-2-rdhx-dc45 | **RDHX 被动 / ε ≥ 0.55 / PG25 兼容** | [[COOLING/Suppliers/PRD-Vertiv-RDHx#^prd-vertiv-table]] | [[../../Reference Architecture/EDGE_INFERENCE_DLC_1.2MW]] | VERTIV | ⏳ 正在review (Q1 进风温度待 VERTIV 确认) |
| 3 ^std-row-3-crah-dc45 | **CRAH 顶置 DX + PG25 冷凝** | [[COOLING/Suppliers/PRD-STULZ-CeilAir#^prd-stulz-084-table\|PRD-STULZ-CeilAir §1 (OHS-084-DG-FC 25.6 kW Total, 31.1 kW FC @ 45°F EGT)]] | [[../../Reference Architecture/EDGE_INFERENCE_DLC_1.2MW]] | STULZ(OHS-084-DG-FC) | ⏳ 正在review (Q1 PG25 性能曲线待 STULZ 回复; **60Hz 专用, CE / 50Hz 缺席, 欧洲/亚太 50Hz 客户 Q1 闭环前不得报价**) |
| 4 ^std-row-4-chiller-dc45 | **Hybrid Chiller ≥ 1600 kW / 22→32°C FWS** | [[COOLING/DESIGN/Hybrid Chiller Requirement 技术规格需求书#^chiller-3-rated-params\|Chiller V1.6 §3]] | [[../../Reference Architecture/EDGE_INFERENCE_DLC_1.2MW]] | TICA(评审候选) | ⏳ 正在review (Q24/Q31 P0 待厂家回复; Q34 v1.3 电气配件已闭环, [[COOLING/Suppliers/TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review#^tica-v13-electrical\|v1.3 §2.2 电气配件]] 已更新) |
| 5 ^std-row-5-600kw-ac40 | **600 kW 集成冷站 (AC40 标配)** | [[COOLING/Suppliers/PRD-同飞-Chiller-600KW#^prd-tonfei-600kw]] | [[../../Reference Architecture/EDGE_INFERENCE_IMMERSION_0.4MW]] | 三河同飞 | ✅ 已经review完成 |
| 6 ^std-row-6-taibao-ac40 | **干冷器 + DX 散热方案 (AC40/AC45 标准)** | [[COOLING/Suppliers/PRD-泰铂-Chiller#^prd-taibao-positioning]] | [[../../Reference Architecture/EDGE_INFERENCE_IMMERSION_0.4MW]] | 泰铂(上海) | ✅ 已经review完成 |

### 1.2 电力子系统(UPS / BESS / 母线) ^std-supplier-1-2-power

| # | 要求(摘要)| 链接产品(PRD) | Reference Architecture | 供应商 | 状态 |
|---|---------|---------------|------------------------|--------|------|
| 7 ^std-row-7-ups-dc45 | **UPS ≥ 1500 kW / 8 min 后备 (DC45)** | [[UPS/Suppliers/Eaton/UPS_EATON_9395XR#^prd-eaton-overview]] | [[../../Reference Architecture/EDGE_INFERENCE_DLC_1.2MW]] | EATON(9395XR-1500) | ✅ 已经review完成 |
| 8 ^std-row-8-ups-ac40 | **UPS 600 kW / 10–20 min 后备 (AC40/AC45)** | [[UPS/Suppliers/Eaton/UPS_EATON_9395XR#^prd-eaton-overview]] | [[../../Reference Architecture/EDGE_INFERENCE_IMMERSION_0.4MW]] | EATON(9395XR-600) | ✅ 已经review完成 |
| 9 ^std-row-9-bess-mw | **BESS 兆瓦级 / 小时级 (DC45 / 大型站点)** | [[BESS/Suppliers/TESLA MEGAPACK 2 XL#^prd-tesla-megapack]] | — | Tesla(Megapack 2 XL) | ✅ 已经review完成 |
| 10 ^std-row-10-bess-ci | **BESS 工商业一体机 / 国产方案** | [[BESS/Suppliers/Gotion ESC480-125P261-UL#^prd-gotion-specs]] | — | 国轩(ESC480-125P261-UL) | ✅ 已经review完成 |
| 11 ^std-row-11-busbar-dc45 | **2500A 母线 / 集装箱内置** | [[Busbar/Suppliers/Siemens/XL-III-Dense-Busbar\|Siemens XL-III Dense Busbar]] | [[../../Reference Architecture/EDGE_INFERENCE_DLC_1.2MW]] | Siemens(XL-III) | ✅ 已经review完成 |

---

## 2. 交叉引用(与 STD_DC45 / 未来 A Series STD)

### 2.1 与 [[../FOG D Series/DESIGN/STD_DC45]] 的关系

| 视角 | STD_DC45 | STD_Supplier(本文档) |
|------|----------|---------------------|
| 范围 | DC45 单一产品的统一参数表 | 全 3RD-PARTY 跨产品的供应商管理 |
| 行维度 | 参数(如"CDU 容量")| (产品类别 × IT Zone) 组合 |
| 列维度 | 权威值 / 源文档(BLOB) | 要求 / 链接产品 / RA / 供应商 / 状态 |
| 权威值来源 | V1.4 Tech Spec EN/CN | 链接的 PRD 文档 |
| 状态 | 参数冲突的 unconfirmed 标记 | 供应商 review 状态 |

**双向链接约定:**
- STD_DC45 中每条 "供应商" 相关参数(如 CDU / RDHx / CeilAir)→ 跳回本文档 §1 查供应商状态。
- 本文档每行 "要求" 字段 → 与 STD_DC45 §2 统一参数表对齐(摘要, 不重复数值)。

### 2.2 与未来 A Series / Design / STD 的预留接口

> **unconfirmed:** A Series STD 当前未建。本文档预留 `A-Series STD` 链接位, 待 A Series Design/STD 创建后回填。

未来 A Series / Design / STD 应:
- 独立维护 A Series 自己的产品类别(目前 A32 / AC40 / AC45)
- 在 §"供应商管理" 中反向链接本文档(STD_Supplier)
- A32 / AC40 / AC45 的供应商已部分体现在本文档(行 #5, #6, #8), A Series STD 启用后应整体迁入

---

## 3. 状态管理规则 ^std-supplier-3-status

| 状态 | 定义 | 触发条件 |
|------|------|----------|
| ⏳ 正在review | 文档存在 + 关键缺口未闭环 | 需求书/澄清邮件已发, P0 项未回复 |
| ✅ 已经review完成 | 文档存在 + 关键参数闭环 | 规格书锁定 OR 产品已可入 BOM |

**状态升级规则:**
- "正在review" → "已经review完成" 须满足:
  1. 需求书版本号 ≥ 1.x 锁定版
  2. 关键 P0 项已书面回复并入档
  3. 链接产品文档已建 / 已存在

**状态降级规则:**
- 若已 locked 的供应商被新需求覆盖(如 Reading 决策 / 容量升级), 状态回退 "正在review" + 在 §3 标注降级原因。

---

## 4. 旧版本与归档

> 当前 3RD-PARTY 区**未发现明确旧版本文件**(前次重组已清理)。若后续发现重复 / 旧版, 须在 3RD-PARTY/_archive/ 建独立目录(由本表反向追溯)。

---

## 5. Changelog

| Version | Date | Summary |
|---------|------|---------|
| v1.2 | 2026-06-06 | §1.1 行 3 (CRAH × DC45) 链接产品(PRD)字段更新: 从 `CRAH_Requirement v1.2 §2` 指向 `PRD-STULZ-CeilAir §1 (OHS-084-DG-FC 25.6 kW Total, 31.1 kW FC @ 45°F EGT)` (基于厂家 Engineering Manual 2018 版 85 页 PDF 提取);状态说明追加 "60Hz 专用, CE / 50Hz 缺席" 警示。STULZ 仍 ⏳ 正在review (Q1 50Hz/CE 闭环是市场准入阻塞项)。 |
| v1.1 | 2026-06-06 | TICA 评审文档重命名: `TICA_Hybrid_Chiller_Configuration_Review` → `TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review`(含产品型号); §1.1 行 4 状态说明同步刷新, 引用 v1.3 电气配件更新段 `^tica-v13-electrical`。Q34 闭环反映到本表, 但 TICA 整体仍 ⏳ 正在review(因 Q24/Q31 P0 + Q33 旁通阀 + Q35 干冷器规格仍未闭环)。 |
| v1.0 | 2026-06-06 | 初版。覆盖 11 个 (产品类别 × IT Zone) 组合;COOLING 5 行 / POWER 6 行(含 UPS/BESS/Busbar)。与 STD_DC45 双向引用约定落地;A Series STD 预留接口。 |

---

*Document Version: v1.2 | Last Updated: 2026-06-06*
