---
title: "03_Power_Zone — §4 Power Zone 完整内容"
parent: "[[../3rd Party List]]"
order: 3
tags:
  - "#workspace/engineer"
  - "#type/3rd-party-list"
  - "#product/UPS"
  - "#power"
  - #MDC
created: 2026-06-18
source_file: "KB/3RD-PARTY/3rd Party List.md"
source_anchors:
  - "§4"
---

# §4. Power Zone — 电力系统

## 4.1 Guideline（选型总则）

> ⚠️ **引用规则：** 选型前必须先查阅 Guideline，再按其选型原则遍历子文件夹产品。

| 文件 | 说明 |
|------|------|
| [[../../KB/Guideline/POWER_SYSTEMS_Guideline]] | 电力 Zone 选型原则:BESS 选型逻辑、UPS 选型、冗余策略、场景推荐 |

## 4.1.1 DESIGN/ 子目录

| 文件 | 说明 |
|------|------|
| (暂无) | 电力 Zone 当前仅 Suppliers/ 有内容,设计准则见 [[../../KB/Guideline/POWER_SYSTEMS_Guideline]] |

## 4.1.2 Suppliers/ 子目录

| 文件 | 说明 |
|------|------|
| [[../../UPS/Suppliers/Eaton/UPS_EATON_9395XR]] | EATON 9395XR 系列 UPS(AC40/AC45/DC45 全覆盖)|
| `UPS/Suppliers/Eaton/*.pdf` | EATON 9395XR / 93LiG2 电池组 datasheet |
| [[../../BESS/Suppliers/TESLA MEGAPACK 2 XL]] | Tesla Megapack 兆瓦级 BESS |
| [[../../BESS/Suppliers/Gotion ESC480-125P261-UL]] | 国轩工商业储能一体机 |
| `Busbar/Suppliers/Siemens/*.pdf` | Siemens XL-III / XL-F 母线 datasheet |

## 4.2 UPS（IT Zone 标配）

| IT Zone | UPS 型号 | 模块数 | 每模块 | 总功率 | 发热量 | UPS 放置 | UPS电池后备时间 | 参考文档 | 状态 |
|---------|---------|--------|--------|--------|--------|---------|--------------|---------|------|
| **AC40** | EATON 9395XR-600 | 4 UPM | 150kW | 600kW | ~7.9kW | **外置(客户自备)** | ~10 分钟(客户自备 2×93LiG2) | [[../../UPS/Suppliers/Eaton/UPS_EATON_9395XR]] | ✅ |
| **AC45** | EATON 9395XR-600 | 4 UPM | 150kW | 600kW | ~7.9kW | 内置(专用电力舱),UL 合规 | ~20 分钟(内置 2×93LiG2) | [[../../UPS/Suppliers/Eaton/UPS_EATON_9395XR]] | ✅ |
| **DC45** | EATON 9395XR-1500 | 10 UPM | 150kW | 1500kW | ~46.9kW | 内置,UL 合规 | ~8 分钟(内置 3×93LiG2) | [[../../UPS/Suppliers/Eaton/UPS_EATON_9395XR]] | ✅ |

> 注：UPS 型号数字代表总 UPS 功率(kW)。9395XR-600 ≠ 600kVA,而是 4×150kW = 600kW。**AC40 UPS 及 UPS电池需客户外置自备;AC45/DC45 UPS 及 UPS电池内置于集装箱。**

> ⚠️ **UPS 电池 vs BESS 电池:** 上表中"UPS电池后备"指 UPS 配套的 93LiG2 磷酸铁锂电池柜(分钟级瞬时切换后备)。BESS(如 Tesla Megapack / 国轩)是独立大型储能系统(小时级供电),两者完全不同。

## 4.3 UPS 电池系统

| 品牌/型号 | 类型 | 每柜能量 | 每柜功率 | 适用 |
|----------|------|---------|---------|------|
| EATON 93LiG2(93Li92S-100Ah)| 磷酸铁锂 | 63.9kWh | 332kW | AC45 / DC45(内置);AC40(客户自备,外置)|

## 4.4 BESS / 储能系统

| 品牌/型号 | 类型 | 适用场景 | 参考文档 | 状态 |
|----------|------|---------|---------|------|
| TESLA Megapack 2 XL | 大型储能(集装箱级)| 城市边缘 / 高 ESG | [[../../BESS/Suppliers/TESLA MEGAPACK 2 XL]] | ✅ |
| 国轩 ESC480-125P261-UL | 工商业储能一体机 | 成本优化 / 国产方案 | [[../../BESS/Suppliers/Gotion ESC480-125P261-UL]] | ✅ |

## 4.5 电力设备

| 品牌/供应商 | 产品 | 说明 | 状态 |
|------------|------|------|------|
| SIEMENS | 母线 Busbar | DC45 内置,2500A | ✅ |
| SIEMENS | TOU(Tap-off Unit)| DC45 内置,含 MCCB | (待补 PRD) |
