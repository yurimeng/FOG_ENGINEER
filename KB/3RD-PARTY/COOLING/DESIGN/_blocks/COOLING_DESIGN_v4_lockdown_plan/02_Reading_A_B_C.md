---
title: 架构歧义 — Reading A / B / C
parent: "[[../COOLING_DESIGN_v4_lockdown_plan]]"
order: 2
tags:
  - #workspace/engineer
  - #type/lockdown-plan
  - #cooling
  - #MDC
created: 2026-06-18
source_file: "KB/3RD-PARTY/COOLING/DESIGN/COOLING_DESIGN_v4_lockdown_plan.md"
source_anchors: []
---

## 2. 架构歧义 — 你 22°C 的"测量点"是哪个？

你说："TCS 进水温度（CDU 板换前）: 22°C"。三种自洽 Reading，物理与造价完全不同：

### Reading A — 保守（v3.0 + 单点修订）

- **22°C = FWS 供水**（Chiller → CDU 一次侧入口），与上轮 v3.0 一致
- CDU 板换保留：LMTD ≥ 6°C，UA ≥ 250 kW/K
- **TCS（二次/送支路）= 28°C 设计点**，与三支路上游 26–28°C 区间一致
- **两介质**：FWS = 站点 EG，TCS = PG25
- 共享 TCS：与现状一致（一个 TCS 二次环路服务三支路）
- 改动量：CDU = 已完成 v3.0；Chiller 升 v1.6（FWS 出水改 22°C）；RDHx/CRAH 几乎不动
- 优点：保留机房 PG25 安全、保留压力隔离、改动最小
- 缺点：TCS 还是 28°C 上限，CeilAir CRAH 在 S-Max × 28°C 还是 −7% 缺口，与你的"22°C 共享 TCS"语义不强一致

### Reading B — 激进（单环路 + 取消板换）

- **22°C = 三支路实际进水**（Rack/CRAH/RDHx 都见 22°C）
- CDU 板换**取消或仅做流体过滤/分配**，无热交换功能
- **单一流体贯穿**：Chiller / CDU / 三支路 = 同一介质（EG-X 或 PG25 或纯水，按站点冰点定）
- 共享 TCS：单环路、三支路并联，与 `计算公式.md §4` "single shared TCS loop" 引擎模型一致
- 改动量：**最大** — Chiller 全重做、CDU 退化为分配器、CRAH 几乎确定换技术路线（DX → 直冷水盘管）
- 优点：所有支路进水温度 = 22°C，CeilAir 缺口、RDHx 吸热 47–55% 上限等问题全部解除；hydraulics 简化为单泵单流体
- 缺点：机房不再有 PG25 隔离层（若用 EG-X，机房进 EG，安全/法规复杂）；Chiller PUE 全部回炉重算（22°C 出水的 free-cooling 阈值远低于 28°C，PUE 上升显著）

### Reading C — 折中（保板换做流体隔离，温差近零）

- **22°C = FWS 供水**，但 CDU 板换 **UA 极大**（≥ 1500 kW/K），LMTD ≤ 1°C
- **TCS = 23°C**（近似 22°C，机房介质仍 PG25）
- 板换只做流体隔离 + 压力隔离，**不做温度分级**
- 共享 TCS：一个 PG25 二次环路服务三支路（与 v3.0 一致）
- 改动量：大 — CDU 板换 UA 从 250 → 1500 kW/K（5–6 倍体积/造价）；Chiller 升 v1.6；RDHx/CRAH 按 23°C 重算
- 优点：保留 PG25 机房介质安全 + 给三支路接近 22°C 的冷水
- 缺点：CDU 板换是 BOM 大头（成本翻几倍）；空间占用大

### 我的建议

如果你的目标是 **匹配引擎模型 + 给冷板/RDHx/CRAH 都灌 22°C 冷水**：选 **Reading B**。
如果你的目标是 **保机房 PG25 安全 + 22°C 实际达到支路**：选 **Reading C**。
如果你的目标是 **最小改动 + 22°C 仅指 Chiller 出水**：选 **Reading A**（= 已完成的 CDU v3.0）。

下文 §3–§6 物理/结构/尺寸 Request 锁定矩阵 **大部分架构无关**，可在你选定 Reading 之前就先锁。
