---
title: 冷却架构
parent: "[[../I400C45]]"
order: 3
tags:
  - #workspace/engineer
  - #type/product
  - #product/i400c45
  - #cooling
  - #MDC
created: 2026-06-18
source_file: "PUBLIC/Products/I400C45.md"
source_anchors: []
---

## 5. 冷却架构

### 5.1 浸没冷却部分

| 项目 | 参数 |
|------|------|
| Tank 型号 | A32，50kW/柜 ^mdc-b585ca54b4 |
| Tank 数量 | 8 |
| 热交换器 | CDU（内置于 Tank），2N 冗余 |
| 散热方式 | **历史最高（极端）干球温度 ≤24°C → 纯干冷器（Free Cooling）；>24°C → Hybrid Cooling System**（干冷器 + DX 一体化）或热泵 |
| 二次侧 Tank 流量 | 单 Tank ≈11.0 m³/h（45kW）/ ≈12.2 m³/h（50kW）；整箱 8× ≈87.8 / ≈97.6 m³/h，详见 [[I50TS#5.4 二次侧散热校核\|A32 §5.4]] ^mdc-13478224eb |
| 设计原则 | [[COOLING_SYSTEM_Guideline]] |

### 5.2 电力舱散热

| 项目 | 参数 |
|------|------|
| UPS 发热量 | ~7.9kW |
| 电池发热量 | 纳入 CDU 热负荷 |
| 散热方式 | 电力舱独立散热通道，纳入整体冷却方案 |
| 设计要求 | 电力舱需独立进风/排风，避免与 IT Zone 热气流混合 |

### 5.3 风冷部分

| 项目 | 参数 |
|------|------|
| 机柜数量 | 1 个（10kW）|
| 散热要求 | 必须配置独立风冷空调，不与浸没冷却共用 |

### 5.4 水路冗余

| 项目 | 参数 |
|------|------|
| CDU 架构 | 各 Tank 内置 CDU，无需独立 CDU |
| 冗余设计 | 整体 2N 冗余设计 |
