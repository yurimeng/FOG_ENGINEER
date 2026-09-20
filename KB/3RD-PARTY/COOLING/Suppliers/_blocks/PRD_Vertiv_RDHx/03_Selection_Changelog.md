---
title: 03_Selection_Changelog — 选型建议 + Changelog
parent: "[[PRD-Vertiv-RDHx]]"
order: 3
tags:
  - "#workspace/engineer"
  - "#type/prd"
  - "#product/RDHx"
  - "#thermal"
  -
created: 2026-06-18
source_file: KB/3RD-PARTY/COOLING/Suppliers/PRD-Vertiv-RDHx.md
source_anchors:
  - 选型建议
  - Changelog
---

# 选型建议(供售前参考)

| IT Zone | 推荐型号 | 数量 | 备注 |
|---------|----------|------|------|
| **DC45**(DLC 三支路 Branch 2) | DCD35 被动型 / 600mm 宽 / 2000 或 2200mm 高 | **9 套** | 单门实际吸热 **~ 22 kW @ TCS 26°C 单点**（ε=0.55 ε-NTU 实算，吸热 55%）;详见 [[../../DESIGN/RDHX_Requirement#^rdhx-3-1-locked]] 与 [[../../../LIQUID/L1240C45/DESIGN/L1240C45 三支路冷却重评估 V4]] §3.2 ^mdc-61c640b347 |
| 其他场景(若有)| DCD50 被动型 / 800mm 宽 | 待评估 | 单门设计吸热取决于 GPU 排气温度与 TCS 进水 |

> ⚠️ **吸热数字的两种口径**：
> - **80% 吸热假设**（早期售前数字）：单门 40–45 kW（即把空气热的 80% 视为目标）。**该假设已被物理校核否定** — DCD35 被动型 ε ≈ 0.53（由 datasheet 最大冷量 66 kW 反推），在 TCS 暖水 + 被动型条件下要求 ε ≥ 0.86 才能达 80%，**物理不可达**。
> - **ε-NTU 实算**（当前 V4 设计口径）：DC45 DLC S-Max 工况（T_air_in=43.3°C, TCS=26°C）下单门吸热 **22.3 kW，吸热比例 55%**。这是被动型 DCD35 的物理上限。 ^mdc-c1aa81180c
> - **售前外发数字必须用 ε-NTU 实算**，不再使用 80% 假设；CeilAir/CDU 选型已按 22 kW/门兜底，与 80% 假设下的 40–45 kW 差距 **~ 50%**，会严重高估 RDHx 回收能力。

---

# Changelog

| Version | Date | Summary |
|---------|------|---------|
| v1.1 | 2026-06-06 | 选型建议表加 ε-NTU 实算注解：单门 22 kW @ TCS 26°C 单点（55%）取代早期 40–45 kW（80% 假设）。原 80% 假设已被物理校核否定（需 ε ≥ 0.86 物理不可达）。售前外发数字以 22 kW 为准。 |
| v1.0 | 2026-06-06 | 初版(重组时)。添加 audience 块(人)+ 品牌定位段 + BLOB 锚点(`^prd-vertiv-table`)+ 选型建议表。参数全部沿用 VERTIV datasheet,未改。 |

---

*Document Version: v1.1 | Last Updated: 2026-06-06*
