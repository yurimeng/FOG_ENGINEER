---
title: UPS / BESS 方案（标准 + 可选 + 比较）
parent: "[[../AC45]]"
order: 6
tags:
  - #workspace/engineer
  - #type/product
  - #product/ac45
  - #power
  - #MDC
created: 2026-06-18
source_file: "PUBLIC/Products/AC45.md"
source_anchors: []
---

## 11. UPS / BESS 方案

AC45 电力舱 UPS 与 UPS 电池有**标准配置（EATON 9395XR-600 + 93LiG2）**与**可选配置（Vertiv Liebert EXL S1 + EnergyCore Li5）**两套方案。**默认采用 EATON 标准配置**，仅当客户明确指定非 EATON 品牌、EATON 交期/价格不满足项目要求、或现场配电条件不兼容时启动可选方案评估。

### 11.1 标准配置：EATON 9395XR-600 + 93LiG2

| 项目 | 参数 |
|------|------|
| UPS 型号 | EATON **9395XR-600** |
| 模块数 | 4 UPM（每模块 150kW） |
| 总 UPS 功率 | 600kW |
| 发热量 | ~7.9kW |
| UPS 放置 | **内置（专用电力舱）**，满足 UL 合规 |
| UPS 电池型号 | EATON 93LiG2（93Li92S-100Ah-3PBFA，332kW/柜） |
| UPS 电池配置 | 2 × 93LiG2 机柜（共 664kW） |
| 后备时间 | **~20 分钟**（内置于电力舱） |
| 功率因数 | 0.9（UPS 输出侧） |
| 资料引用 | [[KB/3RD-PARTY/UPS/Suppliers/Eaton/UPS_EATON_9395XR|Eaton 9395XR]] |

> ⚠️ **UPS 电池 vs BESS 电池：** "UPS 电池后备"指 UPS 配套的 93LiG2 磷酸铁锂电池柜（**分钟级**瞬时切换后备）。BESS（如 Tesla Megapack / 国轩）是独立大型储能系统（**小时级**供电），两者完全不同。参见 [[PUBLIC/Products/AC45#8. AC45 vs AC40 vs DC45 对比|第 8 节对比表]]。

### 11.2 可选配置：Vertiv™ Liebert® EXL S1 + EnergyCore Li5

| 项目                    | 参数                                                                                                                                                                                                                                                                                                       |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UPS 型号                | Vertiv™ Liebert® EXL S1                                                                                                                                                                                                                                                                                  |
| 容量范围                  | 250–400 kVA/kW（**多台并机可达 600kW**）                                                                                                                                                                                                                                                                         |
| 单台尺寸 (W × H × D)      | 1303 × 2009 × 914 mm                                                                                                                                                                                                                                                                                     |
| BESS 型号               | Vertiv™ EnergyCore Li5 Lithium-Ion Battery Cabinet                                                                                                                                                                                                                                                       |
| BESS 单柜尺寸 (W × H × D) | 600 × 2000 × 750 mm                                                                                                                                                                                                                                                                                      |
| BESS 配置               | 10-module                                                                                                                                                                                                                                                                                                |
| 资料链接                  | [Liebert EXL S1](https://www.vertiv.com/en-us/products-catalog/critical-power/uninterruptible-power-supplies-ups/liebert-exl-s1-250-300-400-kvakw/#/models) · [EnergyCore](https://www.vertiv.com/en-ca/products-catalog/critical-power/uninterruptible-power-supplies-ups/vertiv-energycore-10-module/) |

> ⚠️ **TODO — 待 ATS 评估：**
> - 多台并机至 600kW 时的并机柜尺寸、冗余方案
> - 与 AC45 电力舱尺寸匹配性（多台 + 并机柜 + 电池柜的整体占地）
> - 与 EATON 93LiG2 在功率密度、后备时间、热管理上的对比
> - UL 2755 / IEC 62040 认证状态确认

### 11.3 EATON vs Vertiv 比较

| 比较项       | **EATON 9395XR-600（标准）**                | Vertiv Liebert EXL S1（可选）       |
| --------- | --------------------------------------- | ------------------------------- |
| **总功率**   | 600kW（4×150kW 模块）                       | 600kW（多台并机，250–400kW/台）         |
| **架构**    | 模块化（4 UPM，支持内部 N+1）                     | 多台并机架构                          |
| **单台尺寸**  | 单机 600kW 一体化                            | 1303×2009×914 mm / 台            |
| **后备时间**  | ~20 分钟（2×93LiG2）                        | 取决于 EnergyCore Li5 柜数与配置        |
| **UL 合规** | ✅ 已认证                                   | ⚠️ 待 ATS 确认 UL 2755 / IEC 62040 |
| **电力舱适配** | 内置单台 + 2 电池柜（AC45 设计）                   | 内置单台 + 2 电池柜（AC45 设计）           |
| **运行验证**  | 已有 AC40/DC45 项目验证                       | ⚠️ 无 AC45 项目验证先例                |
| **供应商生态** | EATON 93LiG2 与 Vertiv EnergyCore 均为磷酸铁锂 |                                 |
| **优势**    | 模块 N+1 冗余、单机 600kW 简洁、电力舱设计已匹配          | 模块更小适合分期部署                      |
| **劣势**    | 整机 600kW，单点维修需整机停机维护                    |                                 |

### 11.4 替代方案启用条件

仅当以下任一条件成立时启动替代方案评估：
- 客户明确指定非 EATON 品牌
- EATON 9395XR 交期 / 价格不满足项目要求
- 现场配电条件与 EATON 方案不兼容

> **默认配置仍为 EATON 9395XR-600 + 2×93LiG2**，未经 ATS 评估与合规复核，不得擅自切换。
