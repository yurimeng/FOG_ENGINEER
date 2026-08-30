---
title: "L1240C45 第六节：配电规格"
parent: "[[L1240C45_Tech_Spec_CN]]"
order: 6
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/l1240c45"
  - "#thermal"
  - "#MDC"
created: 2026-06-18
source_file: "PUBLIC/Tech_Spec/L1240C45_Tech_Spec_CN.md"
source_anchors:
  - "^sec-6-power"
---

## 6. 配电规格 ^sec-6-power

### 6.1 POD 总配电

配电系统 SLD

![[PDC_SLD_EN_light.svg|SuOCbROt9ozRtAxyvDrcBiXnnqc.png]]

| 设备 | 数量 | 备注 |
|------|------|------|
| 进线柜（Incoming Switchgear） | 1面 | 主断路器 / 电流互感器 / 计量 |
| UPS 主机柜 | 1面 | 在线双变换，含静态旁路切换逻辑 |
| Bypass 旁路柜 | 1面 | 内含 MCCB + 机械 Locker（防止两路同时闭合） |
| 电池仓（BESS） | 独立配置 | 按备用时间计算容量 |
| 母线槽系统（Busbar） | 1套 | **SIEMENS 2500A** 封闭式插接式母线槽，含端头馈线箱 |

**Tap-off Unit（TOU）配置：**

| 负载类型 | 数量 | 单台电流 | MCB 规格 |
|------|------|------|------|
| DLC 水冷机柜 | 8台 | ~200A | 250A MCB |
| 风冷机柜 | 1台 | ~80A | 100A MCB |
| 主 CDU（≥1500 kW，二次泵 VFD） | 1台 | ~35A* | 50A MCB* |
| 顶置空调 STULZ OHS-084-DG-FC | 9台 | ~15A* | 20A MCB* |
| TCS 主循环泵 + RDHX 控制器 | 1组 | ~20A* | 32A MCB* |

> *电流/MCB 值为基于 V1.4 三支路冷却架构的估算上限，需 Power Engineer 在 BOM 锁定阶段按实际 nameplate 复核（CeilAir 9 台总压缩机输入 ~ 58 kW，含风扇 + 控制约 70 kW）。

### 6.2 机架 PDU

| 项目 | 参数 |
|------|------|
| 输入规格 | **60A 415V** |
| 输出接口 | **24位 C19 输出** |
| 保护功能 | **液磁空开（Magnetic Hydraulic Circuit Breaker）** |
| 电源线 | **1.5米 AWG 线缆**（出厂预装） |
| 安装位置 | 后置 |
| 监控功能 | 电流监测（PDU 面板显示） |

> **PDU 选型对比不在本文件呈现。** 竞品对比属内部分析材料，按 [[CLAUDE.md]] Hard Rule 3 不得出现在对客文档中；确有对比需求时向 ATS 索取内部分析。

---
