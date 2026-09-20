---
title: "01_Overview_Module_Design — §0 §1 §2"
parent: "[[../../../UPS_EATON_9395XR]]"
order: 1
tags:
  - "#workspace/engineer"
  - "#type/ups-prd"
  - "#product/UPS"
  - "#power"
  - #MDC
created: 2026-06-18
source_file: "KB/3RD-PARTY/UPS/Suppliers/Eaton/UPS_EATON_9395XR.md"
source_anchors:
  - "§0"
  - "^prd-eaton-overview"
  - "§1"
  - "§2"
---

# §0. 型号速查表 ^prd-eaton-overview

> **本文档为 EATON 9395XR 系列 UPS 产品文档。UPS 选型原则请参考 [[../../../../KB/Guideline/POWER_SYSTEMS_Guideline]]。**

| 产品搭配 | UPS 型号 | 模块数（UPM）| 每模块功率 | 总 UPS 功率 | 发热量 |
|---------|----------|------------|-----------|-----------|--------|
| **AC40** | 9395XR-**600** | 4 UPM | 150kW | 600kW | ~7.9kW ^mdc-0cd6ba8ceb |
| **AC45** | 9395XR-**600** | 4 UPM | 150kW | 600kW | ~7.9kW ^mdc-697b240334 |
| **DC45** | 9395XR-**1500** | 10 UPM | 150kW | 1500kW | ~46.9kW ^mdc-d023c592f4 |

> "600"和"1500"数字代表总 UPS 功率（kW），即模块数量 × 每模块 150kW。

---

# §1. 产品概述

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

# §2. 模块化设计

9395XR 采用模块化 UPM（Universal Power Module）架构：

| 模块 | 功率 | 说明 |
|------|------|------|
| 9395XR-600 | 4 × 150kW = 600kW | AC40 / AC45 使用 ^mdc-615f98cfb1 |
| 9395XR-1500 | 10 × 150kW = 1500kW | DC45 使用 ^mdc-b30252bb8f |

**冗余特性：**
- 单模块故障不影响整体运行（N+1 内部冗余）
- 模块支持热插拔
