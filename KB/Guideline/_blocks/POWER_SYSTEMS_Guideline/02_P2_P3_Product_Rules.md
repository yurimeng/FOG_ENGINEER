---
title: §P-2 产品对照表 + §P-3 关键规则
parent: "[[../POWER_SYSTEMS_Guideline]]"
order: 2
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/power
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/POWER_SYSTEMS_Guideline.md"
source_anchors: []
---

## P-2 产品对照表 (Product Reference Table)

| 产品 | IT负载 | 整体负荷（参考PUE） | 冷却系统功耗 | UPS损耗 |
|------|--------|-------------------|------------|---------|
| **A32** (单柜) | 45–50kW | ~46–56kW (PUE≈1.03–1.12) | ~2–4kW | 含于IT Zone内 ^mdc-b07d75e713 |
| **AC40** | 400kW IT | ~408–480kW (PUE≈1.02–1.20) | ~8–80kW | 含于IT Zone内 ^mdc-c6bee1ef9d |
| **L1240C45** | 1240kW IT | 随 PUE 变化，逐站点用 <https://mdcx.org> 计算 | ~85–435kW | 含于IT Zone内 ^mdc-0501089543 |

> **注意：** 整体负荷不包括 BESS、变压器损耗、外部开关设备等 BOP（Balance of Plant）负荷。

> 详细 IT Zone 形态见 [[PRINCIPLE_Guideline#§3 Zone 架构速查]]；IT↔Cooling 1:1 配对见 [[COOLING_SYSTEM_Guideline#G-8 IT Zone 与冷却区匹配]]。

---

## P-3 关键规则 (Critical Rules)

### 规则 1 — 必须主动澄清

**任何时候收到客户询问电力需求，工程师必须先确认客户说的是 IT 负载还是整体电力负荷。**

如果客户说"1.2MW"，必须追问：
> "您说的 1.2MW 是指 IT 设备负载，还是整个数据中心设施的总用电负荷？"

### 规则 2 — 输出时必须标注

**所有方案输出中，电力数据必须明确标注 IT 负载和整体电力负荷。**

输出格式：
```
IT负载:      xxx kW
整体电力负荷: xxx kW (PUE ≈ x.xx)
```

### 规则 3 — 不混用术语

**禁止将 IT 负载和整体电力负荷混用。**

错误示例：
> "系统 IT 负载 1.2MW，所以场地需要提供 1.2MW 电力。"

正确示例：
> "系统 IT 负载 1.2MW，在 PUE 1.15 条件下，整体电力负荷约为 1.38MW。场地电力接入容量应按整体负荷设计。"

### 规则 4 — IT Zone 与 Power Zone 的关系

| 区域 | 描述 | 对外输出 |
|------|------|---------|
| **IT Zone** (A32/AC40/AC45/DC45) | 包含服务器；UPS（AC45/DC45 内置；AC40 外置客户自备）| IT 负载（客户算力需求） ^mdc-80b16cbdeb |
| **Cooling Zone** | **Hybrid Cooling System**（干冷器+DX一体化） | 不单独对外报价 |
| **Power Zone** | BESS / 变压器 / 开关设备 | 容量规格（kW/MW） |

> 负荷定义错误的级联影响见 [[Risk_Guideline#R-4 负荷定义风险]]。


> ✅ **2026-08-30 Yuri 裁定已传导。** 交期只承诺 EXW（首批 120 天 / Scale 90 天，自下单起算），商务·运输·安装一律不承诺，另有假负载运行期 5–30 天（Supermicro 建议，不含在 EXW 内）；PUE 一律写 `1.0x`，逐站点用 <https://mdcx.org> 计算；质保为核心部件 EXW 起一年 + 按年服务费，ONSITE/NBD/24×7 以 Invoice 为准。基准：[[PRODUCT_SPEC_BASELINE]]。
