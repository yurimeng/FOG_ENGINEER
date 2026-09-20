---
title: 可选 UPS / BESS 配置（替代 EATON 9395XR）
parent: "[[../I400C40]]"
order: 6
tags:
  - #workspace/engineer
  - #type/product
  - #product/i400c40
  - #power
  - #MDC
created: 2026-06-18
source_file: "PUBLIC/Products/I400C40.md"
source_anchors: []
---

## 14. 可选 UPS / BESS 配置（替代 EATON 9395XR）

> 本节为 AC40 标准配置 EATON 9395XR-600（**外置，客户自备**）之外的可选 UPS / BESS 方案，**仅在客户有特定品牌偏好或价格/交期约束时评估**。所有替代方案必须满足： ^mdc-f92ce98b82
> 1. 总功率 ≥ 600kW（与 8×A32 IT Zone 最大负荷匹配） ^mdc-efa70223ed
> 2. 外置安装条件（场地空间、散热、维护通道）
> 3. 满足 UL 2755 / IEC 62040 等认证
> 4. 后备时间 ≥ 10 分钟（与 §10 标准配置等同或更优）

### 14.1 可选 UPS：Vertiv™ Liebert® EXL S1

| 项目 | 参数 |
|------|------|
| 型号 | Vertiv™ Liebert® EXL S1 |
| 容量范围 | 250–400 kVA/kW |
| 单台尺寸 (W × H × D) | 1303 × 2009 × 914 mm |
| 备注 | 单台容量 250–400kW，**多台并机可达 600kW** |
| 资料链接 | [Liebert EXL S1](https://www.vertiv.com/en-us/products-catalog/critical-power/uninterruptible-power-supplies-ups/liebert-exl-s1-250-300-400-kvakw/#/models) |

> ⚠️ **TODO — 待 ATS 评估：**
> - 多台并机至 600kW 时的并机柜尺寸、冗余方案
> - AC40 外置场景下的场地空间、散热、维护通道要求 ^mdc-4801431e23
> - 与原 9395XR-600 在效率、发热量、谐波指标上的差异
> - UL 2755 / IEC 62040 认证状态确认

### 14.2 可选 BESS：Vertiv™ EnergyCore Li5

| 项目 | 参数 |
|------|------|
| 型号 | Vertiv™ EnergyCore Li5 Lithium-Ion Battery Cabinet |
| 单柜尺寸 (W × H × D) | 600 × 2000 × 750 mm |
| 备注 | 锂电池模块柜，10-module 配置 |
| 资料链接 | [Vertiv EnergyCore](https://www.vertiv.com/en-ca/products-catalog/critical-power/uninterruptible-power-supplies-ups/vertiv-energycore-10-module/) |

> ⚠️ **TODO — 待 ATS 评估：**
> - 与 Liebert EXL S1 UPS 配套的电池容量配置
> - 与 EATON 93LiG2 在功率密度、后备时间、热管理上的对比
> - AC40 外置场景下多柜并放的总占地与散热约束 ^mdc-971d268fb1

### 14.3 替代方案启用条件

仅当以下任一条件成立时启动替代方案评估：
- 客户明确指定非 EATON 品牌
- EATON 9395XR 交期 / 价格不满足项目要求
- 现场配电条件与 EATON 方案不兼容

> **默认配置仍为 EATON 9395XR-600 + 2×93LiG2（外置，客户自备）**，未经 ATS 评估与合规复核，不得擅自切换。
