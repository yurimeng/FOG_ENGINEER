---
title: "CDU V5 — 三支路 PICV/Manifold + 冗余/控制/材质/安装"
parent: "[[CDU_Requirement V5]]"
order: 3
tags:
  - #workspace/engineer
  - #type/design-spec
  - #product/CDU
  - #cooling
  - #MDC
created: 2026-06-17
source_file: "KB/3RD-PARTY/COOLING/DESIGN/CDU_Requirement V5.md"
source_anchors: []
---

## 4. 三支路 PICV / Manifold（外部独立安装）

| 支路 | 设计流量 | **PICV 量程** | 控制反馈 |
|---|---|---|---|
| Branch 1（DLC 冷板）| 78–99 m³/h | **0–110 m³/h** | 冷板 ΔT |
| Branch 2（9× RDHX）| 8.4–22.4 m³/h | **0–30 m³/h** | RDHx 进/出水温 |
| Branch 3（9× CeilAir）| 48.7 m³/h（恒）| **0–55 m³/h** | 启停 / 固定流量 |

**PICV 通用要求**：电动 2–10V 或 4–20mA；流量精度 ±5%；关断 Class IV；PG25 兼容；工作压差 30–400 kPa；集成超声波/电磁流量计 ±2%；Modbus RTU 或 4–20mA。

**外部分配 manifold**：304 SS，DN100 主管，主管 ΔP ≤ 10 kPa @ 175 m³/h；顶端排气 / 底端排水。

**冷板 manifold（rack 内部，由 GPU OEM / DLC 集成商提供）**：
- 每 rack **2 个**（冷板 ≤ 100）/ **3 个**（NVL72-class > 100）
- 每分支设计流量 **1.6–2.1 L/min**（1–3 规格内 30%+ 余量）
- 每 manifold 入口装 PICV + 流量计；不平衡率 ≤ 10% 单 / ≤ 15% 间

---

## 5. 冗余 / 控制 / 材质 / 安装

| 项 | 锁定 |
|---|---|
| 板换 | 单台或双台并联（供应商方案）|
| 二次泵 | 2N 或 N+1，VFD 独立，单台故障 ≤ 5s 切换 |
| 一次泵 | **不在 CDU 范围**（Chiller 集成 §10）|
| 控制器 | PLC + ≥7" 触摸屏，中英文；本地/自动/远程；Modbus TCP / BACnet |
| 监控参数 | 一次/二次进出水温、流量、ΔP；二次泵频率与运行时；板换两侧 ΔP；膨胀罐压力 |
| 流量保护联动 | B1 < 70 m³/h → GPU 降载 80%；< 60 m³/h → GPU 60% |
| 板片 | 316L 不锈钢，PG25 兼容 |
| 二次泵叶轮/密封 | PG25 兼容（机械密封 EPDM 或 FKM；不接受 NBR）|
| 法兰 | PN16 / Class 150，PG 兼容垫片 |
| 占地 | ≤ 2.5m × 1.2m |
| 重量 | 供应商提供干/湿重 |
| 维护空间 | 正面 ≥ 800mm / 侧 ≥ 600mm / 顶 ≥ 500mm |
| MTBF / 寿命 | ≥ 50,000 小时 / ≥ 10 年 |
