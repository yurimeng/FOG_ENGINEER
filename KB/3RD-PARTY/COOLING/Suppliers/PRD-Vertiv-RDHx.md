---
tags:
  - "#workspace/engineer"
  - "#type/3rd-party"
  - "#product/cooling"
  - "#supplier/vertiv"
  - "#component/rdhx"
  - #MDC
doc_version: v1.1
supplier: VERTIV
category: RDHx (Rear Door Heat Exchanger)
applicable_zone: DC45
status: ⏳ 正在review (Q1 进风温度待 VERTIV 书面确认,见 [[../DESIGN/RDHX_Requirement#^rdhx-11-open-issues]])
audience: 人(销售/售前/选型工程师)
---
# VERTIV DCD 35/50 RDHx — 产品 PRD (售前/选型)

> **Audience:** 人(销售/售前/选型工程师)。读者应已有 MDC / DLC 基础认知,本文件用于在客户外发 / 内部选型时快速对答。
> **品牌定位:** VERTIV(原 Emerson Network Power) — 全球数据中心热管理一线品牌。Rear Door Heat Exchanger 行业标杆。
> **本文档角色:** 售前侧的产品参数表(datasheet mirror)+ 我方评估/澄清项标注。

## 品牌定位与应用场景

- **品牌定位:** VERTIV 是全球数据中心热管理与供电基础设施一线厂商,在后门换热器(RDHx)细分市场具备长期产品线积累。
- **我方应用:** DC45 三支路冷却 Branch 2 — 9 套被动型后门换热器 (8× DLC 柜 + 1× 风冷柜),见 [[../DESIGN/RDHX_Requirement#^rdhx-1-platform]]。
- **客户价值:** 被动型(zero fan power)降低 PUE;模块化设计支持在线维护;PG25 兼容(已要求 VERTIV 书面证明)。
- **当前评审状态:** ⏳ 正在review — 关键 P0 项(进风 41–48°C 工况许可、水侧 ΔP 曲线、PG25 不锈钢歧管兼容性)见 [[../DESIGN/RDHX_Requirement#^rdhx-11-open-issues]] Q1–Q6。

---

## DCD 35/50 被动散热系统参数对比表 ^prd-vertiv-table

| **参数类别**           | **DCD35 被动型** | **DCD50 被动型** |
| ------------------ | ------------- | ------------- |
| 名义制冷量 (kW)         | 35            | 50            |
| 宽度 (mm)            | 600/800       | 800 (750)     |
| 高度 (mm)            | 2000/2200     | 2000/2200     |
| 最大设计风量 (m³/h)      | 11200         | 14500         |
| 最大制冷能力 (kW)        | 66            | 85            |
| 管径接口               | 1”            | 1”            |
| 最大水流量 (m³/h)       | 5.3           | 5.3           |
| 名义功耗               | 550 W         | 700 W         |
| 运行噪声 (dB(A))       | 74            | 76            |
| 运行进风温度             | 10–+40℃       | 10–+40℃       |
| 存储温度范围             | -30–+50℃      | -30–+50℃      |
| 最大运行压力             | 10 bar        | 10 bar        |
| 运行电压               | 208/230 VAC   | 208/230 VAC   |
| 额定电流               | 16 A           | 16 A           |
| 被动型单元尺寸 (W_D_H mm) | 600_120_1954  | 800_120_1954  |
| 主动型单元尺寸 (W_D_H mm) | 420_125_1954  | 580_125_1954  |
| 适配机柜名义高度 (mm)      | 2000/2200     | 2000/2200     |
| 适配机柜宽度 (mm)        | 600/800       | 800           |
| 被动型单元干重 (kg)       | 73            | 93            |
| 被动型单元运行重 (kg)      | 88            | 111            |
| 主动式模块重量 (kg)       | 40            | 45            |

---

## 选型建议(供售前参考)

| IT Zone | 推荐型号 | 数量 | 备注 |
|---------|----------|------|------|
| **DC45**(DLC 三支路 Branch 2) | DCD35 被动型 / 600mm 宽 / 2000 或 2200mm 高 | **9 套** | 单门实际吸热 **~ 22 kW @ TCS 26°C 单点**（ε=0.55 ε-NTU 实算，吸热 55%）;详见 [[../DESIGN/RDHX_Requirement#^rdhx-3-1-locked]] 与 [[../../../FOG D Series/DESIGN/DC45 三支路冷却重评估 V4]] §3.2 |
| 其他场景(若有)| DCD50 被动型 / 800mm 宽 | 待评估 | 单门设计吸热取决于 GPU 排气温度与 TCS 进水 |

> ⚠️ **吸热数字的两种口径**：
> - **80% 吸热假设**（早期售前数字）：单门 40–45 kW（即把空气热的 80% 视为目标）。**该假设已被物理校核否定** — DCD35 被动型 ε ≈ 0.53（由 datasheet 最大冷量 66 kW 反推），在 TCS 暖水 + 被动型条件下要求 ε ≥ 0.86 才能达 80%，**物理不可达**。
> - **ε-NTU 实算**（当前 V4 设计口径）：DC45 DLC S-Max 工况（T_air_in=43.3°C, TCS=26°C）下单门吸热 **22.3 kW，吸热比例 55%**。这是被动型 DCD35 的物理上限。
> - **售前外发数字必须用 ε-NTU 实算**，不再使用 80% 假设；CeilAir/CDU 选型已按 22 kW/门兜底，与 80% 假设下的 40–45 kW 差距 **~ 50%**，会严重高估 RDHx 回收能力。

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| v1.1 | 2026-06-06 | 选型建议表加 ε-NTU 实算注解：单门 22 kW @ TCS 26°C 单点（55%）取代早期 40–45 kW（80% 假设）。原 80% 假设已被物理校核否定（需 ε ≥ 0.86 物理不可达）。售前外发数字以 22 kW 为准。 |
| v1.0 | 2026-06-06 | 初版(重组时)。添加 audience 块(人)+ 品牌定位段 + BLOB 锚点(`^prd-vertiv-table`)+ 选型建议表。参数全部沿用 VERTIV datasheet,未改。 |

---

*Document Version: v1.1 | Last Updated: 2026-06-06*
