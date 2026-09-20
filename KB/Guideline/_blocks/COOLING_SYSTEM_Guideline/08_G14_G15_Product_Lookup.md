---
title: §G-14 产品选择 + §G-15 KB 查询与验证
parent: "[[../COOLING_SYSTEM_Guideline]]"
order: 8
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/cooling
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/COOLING_SYSTEM_Guideline.md"
source_anchors: []
---

## §G-14 产品选择 (Product Selection)

Only products listed in `KB/3RD-PARTY/COOLING/` may be selected.

**权威清单是 [[3rd Party List]] → [[02_Cooling_Zone]]。** 下表是速查视图，状态以该清单为准。

| Product | Supplier | 适配 SKU | Key Specs | 状态 | Reference |
|---------|---------|---------|-----------|------|----------|
| Hybrid Chiller TAMFV430.3ALF5 | TICA(天加) | L1240C45 | ≥1600 kW; 磁悬浮; FWS 22→32 °C | ✅ ATS Full Pass 2026-06-11 | [[TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.3]] ^mdc-60d5326230 |
| CDU SCR 14103 W | STULZ | **L1800C45** | 1200 kW; FWS 36/46 °C; TCS 40/50 °C; 板换×2 + 泵×3; Tri-Clamp 4" | ✅ ATS approved 2026-08-30 | [[PRD-STULZ-SCR14103W]] ^mdc-3c877c08d0 |
| CyberRow CW 列间空调 CRS 560 CW | STULZ | **L1800C45 × 2** | 净 61.6 kW/台(毛 64.2); 冷冻水 10/15 °C; 11,200 m³/h; 左/右侧向送风; 400V/50Hz | ✅ ATS approved 2026-08-30 | [[PRD-STULZ-CRS560CW]] ^mdc-acd43bc58d |
| CyberRow CW 列间空调 CRS 320 CW(CW320) | STULZ | **L1800C45 × 6 · L450C20 × 4** | 站点记净 29.1 kW/台(毛 36, user-supplied); 其余参数为缩放推导 | ✅ 归属台数已定 · ✅ 单台规格 ✅ PRD v2.0 2026-09-08 | [[PRD-STULZ-CW320]] ^mdc-089b6a4cbe |
| RDHX CoolLoop DCD35 | VERTIV | L1240C45 | 被动式; 35 kW 标称; DN25; ε ≈ 0.55 | ⏳ 正在 review | [[PRD-Vertiv-RDHx]] ^mdc-2f0c94d289 |
| **CRAH（吊顶）** CeilAir OHS-084-DG-FC | STULZ | **仅 L1240C45** | 顶置自含 DX + FC; PG25 冷凝。**与上两行的列间机是不同机型类别，不可互换** | ⏳ 正在 review（**CE / 50 Hz 缺席，欧洲/亚太 50 Hz 客户闭环前不得报价**） | [[PRD-STULZ-CeilAir]] ^mdc-4e837c9ad1 |
| DRYCOOL_with_DX | ~~泰铂~~ | — | 600kW class; IP55; C3防腐; 涡旋压缩机 | ⛔ 已移出 2026-06-16（未走正式 ATS 评审） | [[PRD-泰铂-Chiller\|历史归档]] |
| Hybrid Cooler 600kW | ~~三河同飞~~ | — | 600kW; 螺杆压缩机; -15°C~45°C; IP54 | ⛔ 已移出 2026-06-16（同上） | [[PRD-同飞-Chiller-600KW\|历史归档]] |

> ⚠️ **⛔ 已移出与 ⏳ #unconfirmed 的产品不得进入 BOM 或方案。** 移出项重新引入须走正式 ATS 评审 + Risk/Compliance 评估。
> ⚠️ **L1800C45 / L450C20 尚无专属 列间空调 / CDU Requirement**，选型目前只有 PRD、无需求书基线。规格取值见 [[PRODUCT_SPEC_BASELINE]] §1.2。 ^mdc-7580902576

**关键部件选型原则 / Component Selection Principles:**

| 部件 | 选型要求 |
|------|---------|
| 压缩机 | 涡旋式（≤300kW）/ 螺杆式（≥300kW）/ 磁悬浮（能效优先）|
| 风机 | EC 风机（如德国施乐佰）|
| 水泵 | 变频控制，2+1 备份 |
| 防护等级 | IP54 / IP55（按项目需求）|
| 防腐等级 | C3（标准）/ C4/C5（定制）|
| 控制方式 | 变频调节 + 自动判断自然冷优先 + 故障隔离报警 |

**If no product in `KB/3RD-PARTY/COOLING/` meets project requirements, escalate to ATS before proceeding.** 上报流程见 [[#§G-18 上报规则]]。

---

## §G-15 KB 查询与验证 (KB Lookup & Verify)

### Two-Step Lookup Process

> **Step 1 → Guideline:** Read this file (`COOLING_SYSTEM_Guideline`) first — it defines mandatory architecture rules, IT Zone matching requirements, and prohibited configurations.
> **Step 2 → Products:** Traverse `./KB/COOLING/` to verify individual product parameters match the project requirements.

### Step 1 — This Guideline (Authoritative)

This file is the authoritative source for:
- Permitted cooling architectures (site historical max dry-bulb ≤24°C → pure dry cooler permitted; >24°C → dry cooler + DX / Hybrid mandatory)
- DX activation threshold (≥28°C ambient)
- IT Zone to Cooling Zone matching rules
- Hybrid Cooling System design principles
- Environmental operating ranges

**If a proposed product or configuration contradicts this Guideline, flag and escalate to ATS before proceeding.**

### Step 2 — Product Verification

Check `KB/3RD-PARTY/COOLING/Suppliers/` for product specs. Vendor 范围以 [[3rd Party List]] 为准。

> **Step 3 — 置信度核查（2026-08-30 新增）：** 引用任何参数前，确认它在源文档中不是 ⏳ `#unconfirmed` 或 ⛔ `conflict`。规则见 [[UNCONFIRMED_Convention]]；产品侧参数以 [[PRODUCT_SPEC_BASELINE]] 为准。

## Changelog

| 日期 | 变更 |
|---|---|
| 2026-09-20 | 🧭 unconfirmed-128 已可关闭，已回写来源值（已可关闭） |
