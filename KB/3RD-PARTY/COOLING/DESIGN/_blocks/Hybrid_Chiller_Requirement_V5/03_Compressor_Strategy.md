---
title: "Hybrid Chiller V5 — 压缩机分级配置"
parent: "[[Hybrid Chiller Requirement V5]]"
order: 3
tags:
  - #workspace/engineer
  - #type/design-spec
  - #product/Hybrid-Chiller
  - #cooling
  - #MDC
created: 2026-06-17
source_file: "KB/3RD-PARTY/COOLING/DESIGN/Hybrid Chiller Requirement V5.md"
source_anchors: []
---

## 3. 压缩机分级配置

| 环境温度               | 工作压缩机数  | 运行模式         | 湿膜       | 制冷量           |
| ------------------ | ------- | ------------ | -------- | ------------- |
| ≤ −15°C            | 0（旁通保护） | L0 极寒保护      | 不启用      | 1200–1500 kW  |
| −15 ~ +10°C        | 0（自由冷）  | Free Cooling | 不启用      | 1200–1500 kW  |
| +10 ~ +25°C        | 1       | 混合           | 可选       | 1200–1500 kW  |
| +25 ~ +35°C        | 2       | 机械制冷主导       | 建议启用     | 1200–1500 kW  |
| **+35 ~ +46°C 极热** | 3       | 满载           | **必须启用** | 1200–1500 kW  |
| > +46°C（UAE 沙暴）    | 3 + 降额  | 应急降载         | 必须启用     | ≥ 1000 kW（降额） |

**冗余 N+1**（备机 ≤ 30s 自动切换，Lead/Lag 轮换，独立 HP/LP/过热/过流保护）。

**可接受压缩机类型**：变频涡旋 / 变频螺杆 / 磁悬浮离心（无油，高 IPLV）/ 气悬浮离心（无油，免维护）。
**调速范围**：10–100% 额定负荷；软启动。
**禁用制冷剂**：R22 / R404A / R507A。
**品牌**：Copeland / Bitzer / Danfoss / Turbocor / Smardt / HAIER Turbocor OEM。
