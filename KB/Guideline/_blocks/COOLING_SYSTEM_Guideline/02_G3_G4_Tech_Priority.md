---
title: §G-3 支持的冷却技术 + §G-4 冷却架构优先级
parent: "[[../COOLING_SYSTEM_Guideline]]"
order: 2
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/cooling
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/COOLING_SYSTEM_Guideline.md"
source_anchors: []
---

## §G-3 支持的冷却技术 (Supported Cooling Technologies)

Cooling Engineer has expertise in:

- **Immersion Cooling** — preferred for high-density compute
- **Direct Liquid Cooling (DLC)** — for hardware that cannot be immersed
- **Rear Door Heat Exchangers**
- **Air Cooling Systems** — legacy deployments only
- **Hybrid Cooling System**（干冷器+DX一体化）
- **DX Systems**（DX 是 Hybrid Cooling 的组成部分）
- **Hybrid Cooling Architectures**

Each technology has specific advantages and deployment conditions.

### §G-3.1 冷却架构分类 (Architecture Classification)

| 架构类型 | 压缩机方案 | 适用场景 | 优势 | 劣势 |
|---------|-----------|---------|------|------|
| **DX 方案** | 涡旋式压缩机 | 标准高温散热 | 全年可用、高温兜底 | DX 增加辅助功耗 |
| **螺杆压缩机方案** | 螺杆式压缩机 | 大型集成冷站（≥300kW）| 能效高、可靠性强 | 成本较高、适合大型设备 |
| **磁悬浮压缩机方案** | 磁悬浮变频压缩机 | 能效优先场景 | 极高能效、低噪音 | 成本高、技术要求高 |
| **热泵方案** | 热泵机组 | 极寒或精确温控场景 | 可加热可制冷 | 能耗高于纯干冷器 |

### §G-3.2 按制冷量选型参考 (Capacity-based Selection)

| 制冷量范围 | 推荐架构 | 推荐压缩机 |
|-----------|---------|----------|
| <100kW | DX 方案 / 热泵 | 涡旋式 |
| 100–300kW | DX 方案 / 热泵 | 涡旋式 / 螺杆式 |
| 300–600kW | 螺杆压缩机方案 / DX 方案 | 螺杆式 |
| >600kW | 螺杆压缩机方案 / 磁悬浮 | 螺杆式 / 磁悬浮 |

> 注：以上为参考选型，实际方案根据项目需求和供应商能力确定。

---

## §G-4 冷却架构优先级 (Cooling Architecture Priority)

Evaluate cooling technologies in this order:

| Priority | Technology | Applicable Scenario |
|---------|-----------|-------------------|
| 1 | Immersion Cooling | High-density compute, AI training clusters, GPU-dense workloads |
| 2 | Direct Liquid Cooling (DLC) | Hardware cannot be immersed, standard rack infrastructure required |
| 3 | Air Cooling | Low density, legacy deployments only |

Higher thermal efficiency solutions should be preferred when compatible with workload and infrastructure constraints. 详见 [[#§G-5 浸没式冷却]] 与 [[#§G-6 直冷液冷]]。
