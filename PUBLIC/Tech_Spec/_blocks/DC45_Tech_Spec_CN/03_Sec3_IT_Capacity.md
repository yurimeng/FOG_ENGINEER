---
title: "DC45 第三节：IT 容量"
parent: "[[DC45_Tech_Spec_CN]]"
order: 3
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/dc45"
  - "#thermal"
  - "#MDC"
created: 2026-06-18
source_file: "PUBLIC/Tech_Spec/DC45_Tech_Spec_CN.md"
source_anchors:
  - "^sec-3-it-capacity"
---

## 3. IT 容量 ^sec-3-it-capacity

| 项目 | 参数 |
|------|------|
| **IT 总容量** | **1240kW** |
| DLC 机柜 | 8 × 150kW（每柜 150kW，73% 液冷 / 27% 风冷） |
| 风冷机柜 | 1 × 40kW |
| TCS 进水温度 | **26–28°C**（CDU 二次侧供水至冷板/RDHX/CeilAir 冷凝器）|
| 机柜前进风温度 | **25–27°C**（CeilAir DX 蒸发出风 12–18°C，与 TCS 水温解耦）|
| 服务器排气温度 | **41–48°C**（满载 S-Max 工况，超 DCD35 datasheet 标定 40°C 上限，Vertiv 复核中）|
| DLC 风冷比例 (φ_air) | 设计上限 **27%**，CDU 护栏 ≥ **8%** |
| 功率因数（UPS 输出侧） | 0.9 |

### IT负载 vs 整体电力负荷

| 项目 | 数值 | 说明 |
|------|------|------|
| **IT 负载** | 1240kW | 服务器、GPU 实际消耗 |
| **整体电力负荷** | ~1325–1675kW | 取决于 PUE |
| **PUE（低温区，干冷器优先）** | ~1.07–1.15 | 环境温度较低时，CeilAir 压缩机部分启停 |
| **PUE（高温区，DX 主导）** | ~1.25–1.35 | 环境温度较高时，CeilAir 9 台压缩机 ~58 kW |

---
