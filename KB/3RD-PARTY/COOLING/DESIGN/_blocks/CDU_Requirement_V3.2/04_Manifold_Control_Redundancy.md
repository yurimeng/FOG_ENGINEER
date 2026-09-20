---
title: "CDU v3.2 — Manifold + 控制 + 冗余"
parent: "[[CDU_Requirement v3.2]]"
order: 4
tags:
  - #workspace/engineer
  - #type/design-spec
  - #product/CDU
  - #cooling
  - #MDC
created: 2026-06-17
source_file: "KB/3RD-PARTY/COOLING/DESIGN/.CDU_Requirement v3.2.md"
source_anchors: []
---

## 5. 冷板支路 Manifold 配置（✅ 锁定）

Branch 1 在 manifold 总管下游，进入每个 DLC 机柜后，**每 rack 内部冷板 manifold 配置**如下：

| 项 | 规格 |
|---|---|
| 每 rack manifold 数量 | **2 个**（冷板 ≤ 100）/ **3 个**（冷板 > 100，NVL72-class） |
| 每 manifold 分支数 | 20–50 |
| 每分支设计流量 | **1.6–2.1 L/min**（在 1–3 L/min 规格内 30%+ 余量） |
| 每 manifold 入口 | **PICV + 流量计**（防双 manifold 间不平衡） |
| 总 manifold 数量（DC45 整机）| **16–24 个**（8 rack × 2–3 manifold/rack） ^mdc-ee8e50d855 |
| 不平衡率 | ≤ 10%（单 manifold 内）/ ≤ 15%（manifold 间）|

> 注：rack 内 manifold 由 GPU 平台 OEM 或 DLC 集成商提供，**不属于 CDU 供货范围**，但 CDU 二次侧的扬程余量必须覆盖该 manifold 阻力。

---

## 6. CDU 控制与通信规格（✅ 锁定）

| 参数 | 要求 |
|------|------|
| 本地控制器 | PLC + 彩色触摸屏（≥ 7"），支持中英文 |
| 控制模式 | 本地手动 / 自动 / 远程（Modbus RTU/TCP）|
| 二次泵控制 | **VFD 闭环控制**，可由以下任一信号驱动：(1) 二次侧总管 ΔP；(2) Branch 1 流量；(3) 外部 BMS 指令 |
| 监控参数 | 一次侧进/出水温度、流量、ΔP；二次侧进/出水温度、流量、ΔP；二次泵频率与运行小时数；板换两侧 ΔP；膨胀罐压力 |
| 远程通信 | **Modbus TCP / BACnet**（兼容 FOG BMS）；干接点告警接口 |
| 数据记录 | 本地存储 ≥ 30 天历史数据，USB / 网络导出 |
| 告警分级 | 预警 / 故障 / 紧急，三级告警体系 |
| 联动接口 | 与 DC45 BMS 联动，接收 GPU 负荷信号（0–10V 或 4–20mA），输出 PICV 设定值 ^mdc-28b492784e |
| 流量保护联动 | Branch 1 流量 < 70 m³/h → 输出 BMS 信号触发 GPU 降载 80%；< 60 m³/h → 触发 GPU 降载 60% |

---

## 7. 冗余与可靠性要求（✅ 锁定）

| 参数 | 值 | 备注 |
|---|---|---|
| **二次泵冗余** | **2N 或 N+1**（最少 2 台，任一台 100% 满足设计流量） | Rev 11 锁定 |
| ~~一次泵冗余（如 CDU 自带）~~ | ~~N+1~~ | ✅ **不适用（v2.1 锁定 Rev.C 决策）**：CDU 不自带 FWS 一次泵；一次泵冗余由 [[Hybrid Chiller Requirement 技术规格需求书\|Chiller V1.5]] §10 统筹（2N + VFD）|
| 板式换热器 | 单台或双台并联（供应商方案） | 双台并联便于在线维护 |
| 控制平面冗余 | 双控制器热备，主备自动切换 |
| VFD 冗余 | 二次泵每台独立 VFD；任一 VFD 故障，备用泵自动启动 |
| 故障响应 | 单台泵故障 → 备用泵自动接管（≤ 5 秒切换） |
| 设计寿命 | ≥ 10 年 |
| MTBF | ≥ 50,000 小时 |

---

## 8. 环境规格（✅ 锁定）
