---
title: "02_Cooling_Zone — §3 Cooling Zone 完整内容"
parent: "[[../3rd Party List]]"
order: 2
tags:
  - "#workspace/engineer"
  - "#type/3rd-party-list"
  - "#product/Hybrid-Chiller"
  - "#cooling"
  - #MDC
created: 2026-06-18
source_file: "KB/3RD-PARTY/3rd Party List.md"
source_anchors:
  - "§3"
---

# §3. Cooling Zone — 冷却系统

## 3.1 Guideline（选型总则）

> ⚠️ **引用规则：** 选型前必须先查阅 Guideline，再按其选型原则遍历子文件夹产品。

| 文件 | 说明 |
|------|------|
| [[../../KB/Guideline/COOLING_SYSTEM_Guideline]] | 冷却 Zone 选型原则：架构分类（DX/螺杆/磁悬浮/热泵）、环境温度策略、IT Zone 匹配规则、A32 纯干冷例外 ^mdc-cb2108a8f6 |

## 3.1.1 DESIGN/ 子目录

| 文件 | 说明 |
|------|------|
| [[RDHX_Requirement V5]] | RDHx 技术规格需求书(规范 L1240C45 后门换热器选型与设计) ^mdc-7098d10e8e |
| [[CDU_Requirement V5]] | CDU 技术规格需求书(规范 I400C40 浸没 CDU 和 L1240C45 DLC Rack CDU 选型)。**scope 不含 L1800C45** —— 该 SKU 见 [[PRD-STULZ-SCR14103W]] ^mdc-cd567d8489 |
| [[CRAH_Requirement V5]] | CRAH 技术规格需求书(规范 L1240C45 顶置 DX CRAH 选型)。**scope 不含 L1800C45** —— 该 SKU 见 [[PRD-STULZ-CRS560CW]] ^mdc-297cbccc15 |
| [[Hybrid Chiller Requirement V5]] | L1240C45 大型 Hybrid Chiller 规格需求书(1200–1500kW) ^mdc-3a9b07b829 |
| `.计算公式.md` | L1240C45 仿真引擎公式参考 —— **已点前缀归档**(CLAUDE.md §8),不作为现行基线引用 ^mdc-db1afdff0f |
| [[COOLING_DESIGN_v4_lockdown_plan]] | v4 Reading 决策期间工作底稿 |

## 3.1.2 Suppliers/ 子目录

| 文件                                                               | 说明                                                                                                                                       |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| [[PRD-Vertiv-RDHx]]                                              | VERTIV DCD35 被动 RDHx 售前 PRD                                                                                                              |
| [[PRD-STULZ-CeilAir]]                                            | STULZ OHS-084-DG-FC 顶置 DX CRAH 候选 PRD(基于厂家 Engineering Manual 2018 版; **UL only, 60Hz, 无 CE**)                                           |
| [[PRD-STULZ-CRS560CW]]                                           | STULZ CRS 560 CW **CyberRow CW 列间冷冻水空调** PRD(**L1800C45** × 2 台, 与 CRS 320 CW × 6 混配; 净 54.7 kW/台 · 10/15 °C; ✅ ATS approved 2026-08-30) ^mdc-7a015acc2d |
| [[PRD-STULZ-SCR14103W]]                                          | STULZ SCR 14103 W **CDU** PRD(**L1800C45** GPU 侧 · 1200 kW · FWS 36/46 · TCS 40/50; ✅ ATS approved 2026-08-30) ^mdc-13153022f2 |
| [[PRD-STULZ-CW320]]                                              | STULZ CRS 320 CW(CW320) **CyberRow CW 列间冷冻水空调** PRD(**L1800C45** × 6 + **L450C20** × 4; 站点记净 29.1 kW/台, 选型书 2026-09-08) ^mdc-ae56d585a0 |
| [[PRD-同飞-Chiller-600KW]]                                         | 三河同飞 600 kW 集成冷站 PRD(AC40 标配) ^mdc-72432cdf28 |
| [[PRD-泰铂-Chiller]]                                               | 泰铂干冷器+DX 散热方案 PRD(AC40/AC45 标配) ^mdc-961624a20c |
| [[TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.3]] | TICA TAMFV430.3ALF5 Chiller 内部技术评审(候选引入, V2.3)                                                                                           |
| [[TICA_Clarification_Email_Drafts]]                              | TICA 投标澄清邮件草稿(已外发)                                                                                                                       |
| `TICA风冷磁浮冷水机组技术参数表&配置表.xlsx`                                     | TICA 厂家 xlsx 主源(2026-06-06 更新, 含 Catalog + 配置表更新电气部分 两个 sheet)                                                                           |
| `风冷磁浮冷水机组技术参数表&配置表.csv`                                          | TICA CSV 1 — 系统参数(历史投标资料)                                                                                                                |
| `自然冷却风冷螺杆式冷水机组.csv`                                              | TICA CSV 2 — 配置/部件 BOM(历史投标资料)                                                                                                           |

## 3.2 产品目录

| 类别 | 产品 | 供应商 | 说明 | 参考文档 | 状态 |
|------|------|--------|------|---------|------|
| **干冷器 + DX** | Hybrid Cooling System（AC40/AC45 标准配置）| ~~泰铂~~ | 干冷器 + DX 双冷源,AC40/AC45 标配 | [[PRD-泰铂-Chiller\|PRD-泰铂-Chiller (历史归档)]] | ⛔ **已移出** (2026-06-16 — 创建规则时入库, 未走正式 ATS 评审; PRD 文档保留为历史归档, 不构成采购推荐) ^mdc-f8fb25441a |
| **集成冷站** | 600kW 集成冷站 | ~~三河同飞~~ | 螺杆式压缩机,一体化热泵冷源(**AC40 标配**)| [[PRD-同飞-Chiller-600KW\|PRD-同飞-Chiller-600KW (历史归档)]] | ⛔ **已移出** (2026-06-16 — 创建规则时入库, 未走正式 ATS 评审; PRD 文档保留为历史归档, 不构成采购推荐) ^mdc-e06d4e5086 |
| **Hybrid Chiller** | 大型 Hybrid Chiller(DC45 专用)| TICA(主供) | 额定制冷量 ≥1600 kW(**DC45 标配,600kW 冷站不适用 DC45**)| [[TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.3\|TICA V2.2]] | ✅ 已经review完成 (2026-06-11 ATS Full Pass; P1 关注内容待 TICA 提供) ^mdc-3f94646dc3 |
| **CDU（AC40/AC45 浸没式）** | 内阻 Dual CDU | 三河同飞 / 待确认 | AC40/AC45 浸没回路,1+1 冗余 | [[CDU_Requirement V5]] | ⏳ 正在review ^mdc-cd76948c2a |
| **CDU（DC45 DLC）** | Rack CDU,≥1500kW | 待全球招标 | DC45 DLC 主回路,VFD 泵,2N/N+1 冗余 | [[CDU_Requirement V5]] | ⏳ 正在review ^mdc-54a5664920 |
| **CDU（L1800C45 DLC）** | STULZ SCR 14103 W | STULZ | L1800C45 GPU 侧暖水回路,1200 kW/台,FWS 36/46 °C · TCS 40/50 °C,板换 ×2 + 泵 ×3,Tri-Clamp 4" 接口;**台数/冗余(Q1) · 泵可用扬程仅 0.2 m(Q2) · 纯水无防冻(Q3) · 认证(Q4) 四项 P0 未闭环** | [[PRD-STULZ-SCR14103W]] | ✅ **ATS approved** (2026-08-30) ^mdc-3bd0b0b02c |
| **CyberRow CW 列间空调（小机型）** | STULZ CRS 320 CW(CW320) | STULZ | **L1800C45 × 6**(与 CRS 560 CW × 2 混配) + **L450C20 × 4**(N+1); 站点记净 29.1 kW/台(PRD v2.0 2026-09-08 选型书); 单台规格 ✅ PRD v2.0（净 29.1 kW / 风机 4.5 kW） | [[PRD-STULZ-CW320]] | ✅ 归属台数已定 / ✅ 单台规格 ^mdc-91ee582d14 |
| **CyberRow CW 列间空调（大机型）** | STULZ CRS 560 CW(非标版) | STULZ | **L1800C45 × 2**, 与 CRS 320 CW × 6 混配共 8 台; 净 54.7 kW/台(毛 57.3), 11,200 m³/h, 冷冻水 10/15 °C, 400V/50Hz; 左/右侧向送风列间机; 台数/冗余(Q1) · 认证(Q4) 为 P0 | [[PRD-STULZ-CRS560CW]] | ✅ **ATS approved** (2026-08-30) ^mdc-9c772eae71 |
| **顶置空调** | STULZ OHS-084-DG-FC | STULZ | DC45 舱内残余热处理,9 台(PG25 兼容);**UL/CETL 已认证(60Hz 专用), CE / 50Hz 缺席, 欧洲/亚太 50Hz 客户 Q1 闭环前不得报价** | [[PRD-STULZ-CeilAir]] | ⏳ 正在review (Q1 50Hz/CE 待 STULZ 回复) ^mdc-05cc7b6f69 |
| **后门换热器** | Vertiv DCD35 被动 RDHx | VERTIV | DC45 机柜后门余热回收,9 台 | [[PRD-Vertiv-RDHx]] | ⏳ 正在review (Q1 待 VERTIV 回复) ^mdc-a89b32ecf8 |
| **RDHx 规格** | RDHx 技术规格需求书 | — | 规范 RDHx 选型与设计要求 | [[RDHX_Requirement V5]] | (规范) |
| **CRAC 规格** | 列间空调 技术规格需求书 | — | 规范 列间空调选型与设计要求 | [[CRAH_Requirement V5]] | (规范) |

> ⚠️ **冷却系统容量匹配规则：**
> - AC40(IT 400kW)→ 600kW 集成冷站 ✅ (但 600kW 集成冷站当前供应商三河同飞已 ⛔ 移出, AC40 冷站需重启 ATS 评审) ^mdc-bf0be9df4a
> - DC45(IT 1240kW)→ 需要 ≥1600kW Hybrid Chiller,**600kW 冷站不满足 DC45 需求** ^mdc-d4a591604c
> - **L1800C45(IT 1800kW · 双环路)**→ GPU 侧 **2× STULZ SCR 14103 W**;列间侧 **2× CRS 560 CW + 6× CRS 320 CW**(混配共 8 台, 净冷量 329.1 kW, 10/15 °C)。**冗余归属未锁定,见两份 PRD 的 Q1** ^mdc-51c5ecf876
> - **L450C20(IT 450kW · 双环路)**→ GPU 侧 **1× STULZ SCR 14103 W**;列间侧 **4× CRS 320 CW**(N+1, 单台承载全负荷)。✅ CRS 320 CW 单台规格 ✅ PRD v2.0 2026-09-08。见 [[PRD-STULZ-CW320]] ^mdc-65d4483355
> - 所有冷却产品选型须符合 [[../../KB/Guideline/COOLING_SYSTEM_Guideline]] 的架构分类与 IT Zone 匹配规则

## 3.5 已移出供应商历史 (V1.9 新增)

| 移出日期 | 供应商 | 产品 | 移出原因 | 归档文档 |
|---------|--------|------|---------|---------|
| 2026-06-16 | 泰铂(上海)| 干冷器 + DX | 创建规则时入库(PRD 文档已存在),未走正式 ATS 评审; 不构成采购推荐 | `PRD-泰铂-Chiller.md` (保留为历史归档) |
| 2026-06-16 | 三河同飞 | 600 kW 螺杆式集成冷站 | 创建规则时入库(PRD 文档已存在),未走正式 ATS 评审; 不构成采购推荐 | `PRD-同飞-Chiller-600KW.md` (保留为历史归档) |

> **重新引入流程:** 如需重新启用上述任一供应商, 须按 [[Hybrid Chiller Requirement V5]] 流程走正式 ATS 评审 + Risk/Compliance 评估 + 更新本文件状态为 ⏳ 正在review. 评审通过前不得在项目方案中引用.

## 3.3 架构类型速查

| 架构类型 | 压缩机 | 适用制冷量 |
|---------|--------|-----------|
| DX 方案 | 涡旋式 | <300kW |
| 螺杆压缩机方案 | 螺杆式 | 300–600kW |
| 磁悬浮压缩机方案 | 磁悬浮 | 能效优先 |
| 热泵方案 | 热泵机组 | 极寒/精确温控 |

## 3.4 供应商参考

| 品牌/供应商 | 产品类型 | 备注 |
|------------|---------|------|
| ~~泰铂(上海)~~ | ~~干冷器 + DX~~ | ⛔ **已移出** (2026-06-16, 创建规则时入库) |
| ~~三河同飞~~ | ~~冷却设备、集成冷站~~ | ⛔ **已移出** (2026-06-16, 创建规则时入库) |
| 英维克股份 | 冷却设备 | 参考供应商 |
| VERTIV | RDHx | 评审中(候选) |
| STULZ | 顶置 DX 空调(OHS-084) | 评审中(候选) —— Q1 50Hz/CE 待回复 |
| STULZ | CyberRow CW 列间空调(CRS 560 CW / CRS 320 CW) · CDU(SCR 14103 W) | ✅ **ATS approved** (2026-08-30) —— L1800C45 / L450C20 冷却选型 ^mdc-6a94708e8a |
| STULZ | 吊顶 DX 空调(OHS-084) | ⏳ 正在 review —— **CE / 50Hz 缺席**, 仅 L1240C45 ^mdc-4d16f7b0b0 |
| TICA(天加)| Hybrid Chiller | ✅ 已经review完成 (2026-06-11 ATS Full Pass) |

## Changelog

| 日期 | 变更 |
|---|---|
| 2026-09-20 | 🧭 unconfirmed-174 已可关闭，已回写来源值（已可关闭） |
| 2026-09-20 | 🧭 unconfirmed-124 已可关闭，已回写来源值（已可关闭） |
