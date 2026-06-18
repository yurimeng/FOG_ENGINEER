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

| Product | Supplier | Key Specs | Reference |
|---------|---------|-----------|----------|
| DRYCOOL_with_DX | 泰铂 | 600kW class; IP55; C3防腐; 涡旋压缩机 | [[PRD-泰铂-Chiller\|KB/3RD-PARTY/COOLING/DRYCOOL_with_DX]] |
| Hybrid Cooler 600kW | 三河同飞 | 600kW; 螺杆压缩机; -15°C~45°C; IP54 | [[PRD-同飞-Chiller-600KW\|KB/3RD-PARTY/COOLING/Hybrid Cooler 600kW - 同飞]] |

> 备注：上述两条 PRD 链接的源文件当前不在 `KB/3RD-PARTY/COOLING/`（已迁移或拆分）。引用前请用 `KB/3RD-PARTY/3rd Party List.md` 重新定位最新 supplier 目录。

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

Check `KB/3RD-PARTY/COOLING/` subfolder for product specs. Vendor 范围以 [[KB/3RD-PARTY/3rd Party List]] 为准。
