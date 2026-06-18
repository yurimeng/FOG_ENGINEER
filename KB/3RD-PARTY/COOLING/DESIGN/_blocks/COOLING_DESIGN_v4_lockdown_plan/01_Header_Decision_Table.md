---
title: 一句话决策表 + 现状盘点
parent: "[[../COOLING_DESIGN_v4_lockdown_plan]]"
order: 1
tags:
  - #workspace/engineer
  - #type/lockdown-plan
  - #cooling
  - #MDC
created: 2026-06-18
source_file: "KB/3RD-PARTY/COOLING/DESIGN/COOLING_DESIGN_v4_lockdown_plan.md"
source_anchors: []
---

## 0. 一句话决策表

| 项 | 你已锁定 | 待你抉择 | 我建议 |
|---|---|---|---|
| 应用基线 | DC45_Thermal_Assessment_6Sites（V2.0 / 6 站点 / 1240 kW IT）| — | 沿用，PUE 数值待 v4 重算 |
| 整体散热架构 | DC45 三支路重评估 2026-05-21（Rev 11）三支路 | — | 沿用三支路骨架 |
| 三支路命名 | Rack / CRAH / RDHx（对应 Rev 11 的 DLC / CeilAir / RDHx）| — | 已对齐 |
| 共享 TCS | **是**（单 TCS 二次侧服务三支路）| — | 与 v3.0 / 计算公式.md §4 一致 |
| TCS 进水温度（CDU 板换前）| **22°C** | **22°C 的"测量点"语义未定** | 见 §2 — 三种 Reading 选 1 |
| TCS 介质 | — | PG25 / EG-X / 纯水 | 取决于 Reading（见 §2）|
| 物理/结构/尺寸 Request | — | 见 §3–§6 锁定矩阵 | 大部分架构无关，可立即锁 |
| 热力 Request | — | 待架构决策后逐项重算 | 见 §7 待决清单 |

---

## 1. 现状盘点（你给的两份基础文件 + KB/3RD-PARTY/COOLING/DESIGN/ 全集）

### 1.1 基础文件（不动）

| 路径 | 当前版本 | v4 状态 |
|---|---|---|
| `KB/FOG D Series/DESIGN/DC45_Thermal_Assessment_6Sites.md` | V2.0（2026-05-22）| **基线沿用**，§2.4 / §3.4 / §4.x / §8 各站点表中 FWS 26–28°C 需在 v4 重算 PUE 后联动改 |
| `KB/FOG D Series/DESIGN/DC45 三支路冷却重评估 2026-05-21.md` | Rev 11 | **架构骨架沿用**，§1.3 / §2.x / §3.x / §4.x 中 TCS 26–28°C 全部需联动改 |

### 1.2 COOLING/DESIGN 目录全集

| 文件 | 类型 | 当前版本 | v4 处理 |
|---|---|---|---|
| `CDU_Requirement.md` | 物理设备需求 | **v3.0**（2026-06-05，本次会话刚改完）| §1.1 / §1.4 / §2.1 / §3.2 / §11 / 附录 B 需按 v4 架构再校核 |
| `Hybrid Chiller Requirement 技术规格需求书.md` | 物理设备需求 | V1.5 | §1.1 / §3 / §5 / §10 全部需重做（FWS 26–28°C → 22°C）|
| `RDHX_Requirement.md` | 物理设备需求 | v1.0 | §1 / §3 / §4 / §10 需重做（TCS 26–28°C → 22°C，吸热比例上修）|
| `CRAH_Requirement.md` | 物理设备需求 | v1.1 | **整份产品选型存疑**（CeilAir DG-FC 是 DX-冷凝架构，在 22°C TCS 下可能整体换技术路线 → 直冷水盘管 CRAH）|
| `CDU FlowChart.png` | 架构图 | — | v4 架构定后需重画 |
