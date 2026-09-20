---
title: "CRAH V5 — 文件说明 + 系统背景 + 选型与数量"
parent: "[[CRAH_Requirement V5]]"
order: 1
tags:
  - #workspace/engineer
  - #type/design-spec
  - #product/CRAH
  - #cooling
  - #MDC
created: 2026-06-17
source_file: "KB/3RD-PARTY/COOLING/DESIGN/CRAH_Requirement V5.md"
source_anchors: []
---

## 1. 系统背景

**适用设备：** STULZ CeilAir OHS-084-DG-FC（自含式吊顶 DX，乙二醇/PG 冷凝 + 自由冷却）
**应用场景：** DC45 三支路 Branch 3 — 9 台顶部均匀布置 ^mdc-b09e8cb6f0

| 边界 | 锁定值 |
|---|---|
| 适用产品 | DC45（45ft DLC 集装箱） ^mdc-4b98ac2049 |
| IT 容量 | 1240 kW（8× DLC 150 + 40 风冷）|
| 介质 | **PG25（25% 丙二醇）** |
| **TCS 进水（冷凝侧进液）** | **26°C 单点**（V5 锁定）|
| TCS 设计 ΔT | 冷凝侧实际 ≈ 5–6°C @ datasheet 锁定流量 5.41 m³/h |
| 机柜进风目标 | **25–27°C**（CRAH 出风 ~18°C 与机房混合后）|
| 机房回风（估算）| ~32°C DB / ~35% RH（封闭集装箱低湿源）|

---

## 2. CRAH 选型与数量

| 项 | 锁定值 |
|---|---|
| **型号** | **STULZ CeilAir OHS-084-DG-FC**（自含式 DX + PG 冷凝 + Free Cooling）|
| **数量** | **9 台**（顶部均匀分布，1 单元/机柜上方）|
| **冗余等级** | **N（无 N+1）** — 顶部空间已饱和 |
| **承载结构** | 单台 250 kg × 9 = **2250 kg 顶置载荷** ⚠️ |
| **配置版本** | **-DG-FC**（PG 兼容 + Free Cooling 回路）；不接受 -DW / 非 -FC 版本 |

> 不接受替代选型；任何主动替换须经 ATS 评审重出 BOM。
