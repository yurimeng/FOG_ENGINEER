---
tags:
  - #workspace/engineer
  - #type/3rd-party
  - #product/ups
  - #supplier/eaton
  - #product/9395xr
---

# EATON 9395XR UPS Series / 伊顿 9395XR UPS 系列

> **本文档为 EATON 9395XR 系列 UPS 产品文档。UPS 选型原则请参考 [[POWER_SYSTEMS_Guideline|KB/3RD-PARTY/BESS/POWER_SYSTEMS_Guideline]]。**

---

## 0. 型号速查表

| 产品搭配 | UPS 型号 | 模块数（UPM）| 每模块功率 | 总 UPS 功率 | 发热量 |
|---------|----------|------------|-----------|-----------|--------|
| **AC40** | 9395XR-**600** | 4 UPM | 150kW | 600kW | ~7.9kW |
| **AC45** | 9395XR-**600** | 4 UPM | 150kW | 600kW | ~7.9kW |
| **DC45** | 9395XR-**1500** | 10 UPM | 150kW | 1500kW | ~46.9kW |

> "600"和"1500"数字代表总 UPS 功率（kW），即模块数量 × 每模块 150kW。

---

## 1. 产品概述

| 项目 | 参数 |
|------|------|
| **型号** | EATON 9395XR 系列 |
| **类型** | 在线双变换不间断电源（UPS） |
| **品牌** | EATON |
| **架构** | 模块化功率模块（UPM）设计，支持 N+1 冗余 |
| **效率 (ESS)** | 99% |
| **效率 (双变换)** | 97.5% |
| **扩展方式** | 垂直扩展 / 水平扩展 |

---

## 2. 模块化设计

9395XR 采用模块化 UPM（Universal Power Module）架构：

| 模块 | 功率 | 说明 |
|------|------|------|
| 9395XR-600 | 4 × 150kW = 600kW | AC40 / AC45 使用 |
| 9395XR-1500 | 10 × 150kW = 1500kW | DC45 使用 |

**冗余特性：**
- 单模块故障不影响整体运行（N+1 内部冗余）
- 模块支持热插拔

---

## 3. 外观接口说明

### 前面板接口

| 接口名称 | 功能说明 |
|---------|----------|
| Mini-slot 1/2/3 | 扩展槽位，用于安装额外功能模块 |
| USB Host | 连接配件用 USB 接口 |
| USB Device | 连接计算机用 USB 接口 |
| RS-232 端口 | 服务调试接口 |
| EPO（Emergency Power Off）| 紧急关机按钮 |
| Relay output | 继电器输出 |

### 后面板接口

| 接口名称 | 功能说明 |
|---------|----------|
| External parallel connector | 外部并机接口 |
| External battery breaker trip | 外部电池断路器跳闸 |
| BMS RS-485 | 电池管理系统通信接口 |
| SYNC Terminal | 同步端子 |
| Rectifier Input | 整流器输入 |

详细接口图参考：
- [[9395XR-1500-Rear-Exhaust-Connections|EATON 9395XR 接口定义]]
- [[9395XR-1500-Wiring-Diagram|EATON 9395XR 接线图]]

---

## 4. UPS 电池后备时间

UPS 电池型号：**EATON 93LiG2**（93Li92S-100Ah-3PBFA，332kW/柜）

| 产品 | UPS 电池配置 | IT 负载 | 后备时间 |
|------|-------------|---------|---------|
| AC40 | 2×93LiG2（外置，客户自备）| 400kW | ~10 分钟 |
| AC45 | 2×93LiG2（内置）| 400kW | ~20 分钟 |
| DC45 | 3×93LiG2（内置）| 1240kW | ~8 分钟 |

> ⚠️ **UPS 电池 vs BESS 电池：** 上表中"UPS电池"指 UPS 配套的 93LiG2 磷酸铁锂电池柜（分钟级瞬时切换后备）。BESS（如 Tesla Megapack / 国轩）是独立大型储能系统（小时级供电），两者完全不同。

电池系统详细参考：[[93Li-G2-Battery-Brochure|93Li G2 锂电池系统手册]]

---

## 5. 与 FOG 产品搭配

| FOG 产品 | UPS 放置 | UPS 电池放置 | 适用场景 |
|---------|---------|-------------|---------|
| **AC40** | 外置（客户自备）| 外置（客户自备）| 无 UL 合规需求 |
| **AC45** | 内置（专用电力舱）| 内置（专用电力舱）| 需要 UL 合规 |
| **DC45** | 内置 | 内置 | 1240kW 大功率，UL 合规 |

参考：[[PRODUCTS_AC40|KB/PRODUCTS_AC40]] | [[PRODUCTS_AC45|KB/PRODUCTS_AC45]] | [[PRODUCTS_DC45|KB/PRODUCTS_DC45]]

---

## 6. 参考文档

| 文档 | 说明 |
|------|------|
| [[9395XR-1500-Top-Exhaust-Dimensions]] | 9395XR-1500 顶部出风尺寸图 |
| [[9395XR-1500-Rear-Exhaust-Connections]] | 9395XR-1500 后面板接口定义 |
| [[9395XR-1500-Wiring-Diagram]] | 9395XR-1500 接线图 |
| [[93Li-G2-Battery-Brochure]] | 93Li G2 锂电池系统手册 |
| [[9395XR-1500-Chinese-Manual]] | 9395XR UPS 中文版手册 |

---

*Document Version: v1.1 | Last Updated: 2026-04-12*
