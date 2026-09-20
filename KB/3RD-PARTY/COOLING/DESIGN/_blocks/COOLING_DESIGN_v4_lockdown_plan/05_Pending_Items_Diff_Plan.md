---
title: §7 待决清单 + §8 联动变更预告
parent: "[[../COOLING_DESIGN_v4_lockdown_plan]]"
order: 5
tags:
  - #workspace/engineer
  - #type/lockdown-plan
  - #cooling
  - #MDC
created: 2026-06-18
source_file: "KB/3RD-PARTY/COOLING/DESIGN/COOLING_DESIGN_v4_lockdown_plan.md"
source_anchors: []
---

## 7. 待架构决策后逐项锁定（汇总）

下列所有项必须在 Reading（A/B/C）确认后才能写入正式 Request：

| # | 项 | A | B | C |
|---|---|---|---|---|
| T1 | 流体（机房侧） | PG25 | 单一流体（待定）| PG25 |
| T2 | 流体（户外侧） | 站点 EG | 同 T1 | 站点 EG |
| T3 | CDU 板换 | 保留 / LMTD ≥ 6°C | 取消 | 保留 / LMTD ≤ 1°C |
| T4 | CDU 板换 UA | ≥ 250 kW/K | n/a | ≥ 1500 kW/K |
| T5 | FWS 供水温度 | 22°C | n/a | 22°C |
| T6 | TCS 至支路温度 | 28°C | 22°C | 23°C |
| T7 | 各支路 ΔT | DLC 10 / RDHx 8 / CeilAir-DG | DLC 10 / RDHx 8 / CW-CRAH 8–10 | 同 B |
| T8 | CRAH 技术路线 | DX（CeilAir）| **CW 盘管** | **CW 盘管** |
| T9 | RDHx 吸热比例 | 47–55%（27°C 水）| **65–71%**（22°C 水）| **62–68%**（23°C 水）|
| T10 | 全年 PUE 重算（6 站点）| 微调 | 大改 | 中改 |
| T11 | CeilAir 缺口（S-Max × 高温）| −7% 兜底 GPU 降载 | 解除 | 解除 |
| T12 | Chiller free-cool 阈值 | T_amb ≤ ~23°C（FWS 22°C） | T_amb ≤ ~17°C（出水 22°C → return ~32°C → 限 ~17°C ⚠️） | 同 B |

> ⚠️ **PUE 风险提示**：22°C 出水的 free-cooling 限制远低于 v1.5 的 26–28°C 设计。Kemi 的 ~5200 h 自由冷可能下降 30–40%；UAE 的全年加权 PUE 可能从 1.34–1.38 升至 1.40–1.45。**这是 v4 的最大 trade-off**。

---

## 8. 6Sites + 三支路重评估 — 联动变更预告（不在本次锁定范围）

| 文档 | 待 v4 改的章节 | 改动量 |
|---|---|---|
| `L1240C45_Thermal_Assessment_6Sites.md` | §2.4 TCS 28°C 兜底 / §3.1 工况层级 / §3.4 温度边界 / §4.x 各站点 PUE / §5 跨站对比 / §7 各站点配置 / §8 上游对接面 | 大改（PUE 数值全部重算）|
| `L1240C45 三支路冷却重评估 2026-05-21.md` | §0.5 三个问题答复 / §1.3 边界假设 / §2.x 全部 ε-NTU 实算 / §3.x RDHx + CRAH 能力 / §4.x 三支路流量 ΔP / §5 工程结论 / §6 单 CDU 校核 | 中–大改 ^mdc-f0f957c0a9 |
| `L1240C45 Hydronic & Thermal Design Criteria` | §9.x 流量 / §12 TCS 28°C Forbidden（解除？ in B/C）| 中改 ^mdc-7b10fe5598 |
| `L1240C45 Tech Spec CN / EN` | TCS 进水温度 26–28 → 22 | 小改 ^mdc-739a9ac0b9 |
| `Quick Tech Spec` / `PRODUCTS_L1240C45` | 同上 | 小改 |
| `计算公式.md`（引擎文档）| 与新架构对齐（§4 已是单环路口径 — A 偏离 / B 对齐 / C 偏离）| 看是否要解释偏离 |
