---
title: §G-7 热排放系统
parent: "[[../COOLING_SYSTEM_Guideline]]"
order: 4
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/cooling
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/COOLING_SYSTEM_Guideline.md"
source_anchors: []
---

## §G-7 热排放系统 (Heat Rejection Systems)

### Permitted Configurations

| Method | Status | Notes |
|--------|--------|-------|
| **Hybrid Cooling System**（干冷器+DX一体化） | ✅ REQUIRED when site historical max dry-bulb >24°C | Standard configuration |
| Pure Dry Cooler（纯干冷器 / Free Cooling） | ✅ Permitted when site historical (extreme) max dry-bulb **≤24°C** | Free cooling 满足一次侧 ≤32°C 供水；>24°C 不允许 |
| 冷却塔 | ✅ Permitted | Requires adequate water supply |

### Selection Criterion & DX Activation Rule

**放型判据（是否需要 DX 硬件）：以站点历史（极端）最高干球温度为界——≤24°C 可放型纯干冷器（Free Cooling）；>24°C 必须采用 Hybrid Cooling System（干冷器 + DX）。**

**运行激活（DX 何时投入）：在已安装 Hybrid 系统的前提下，DX 随实时环境温度 ≥28°C 自动投入调节。**

- 放型判据（24°C）与运行激活阈值（28°C）为两个不同概念：前者决定是否配置 DX 硬件，后者决定 DX 何时运行。
- 当站点历史最高干球 ≤24°C 放型为纯干冷器时，无 DX 硬件，不适用 28°C 运行激活规则。

### Environment-based Operating Modes / 环境温度与运行模式

#### AC40 / AC45 / DC45（外制冷系统动态调节）

| 环境温度 | 运行模式 | 说明 |
|----------|---------|------|
| <28°C | 干冷器优先，DX 关闭或低负荷 | 自然冷优先，能效最高 |
| 28–35°C | 干冷器 + DX 共同运行 | 混合模式，PUE 中等 |
| >35°C | DX 主导，干冷器辅助 | 高温兜底，确保散热 |

#### A32 独立部署放型与运行模式

| 站点历史最高（极端）干球温度 | 放型 / 运行模式 | 说明 |
|----------|---------|------|
| ≤24°C | 纯干冷器（Free Cooling，允许放型）| 自然冷满足一次侧 ≤32°C，PUE 可低至 1.03 |
| >24°C | Hybrid（干冷器 + DX）/ 热泵 | 必须配置 DX 辅助散热；DX 随实时环境 ≥28°C 投入 |

### Selection Factors

- Climate conditions
- Water availability
- Power efficiency goals
- Operational complexity
