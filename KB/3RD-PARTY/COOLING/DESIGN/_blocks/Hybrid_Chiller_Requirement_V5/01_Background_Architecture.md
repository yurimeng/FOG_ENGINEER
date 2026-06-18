---
title: "Hybrid Chiller V5 — 项目背景 + 适用场景 + 四级架构"
parent: "[[Hybrid Chiller Requirement V5]]"
order: 1
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

## 1. 适用场景与架构

**适用：** Direct-to-Chip 液冷 · IT 负载 1.2–1.5 MW · 容器化 MDC DC45
**6 站点：** 极热干燥（UAE Dubai）/ 极热湿润（泰国 Chiang Mai）/ 温带大陆（美国 Texas）/ 极寒（芬兰 Kemi）/ 极端双向温差（哈萨克斯坦 Astana）

### 1.1 冷却架构概述

- **介质：** 乙二醇混合液（EG，浓度按站点附录 A）
- **介质边界：** Chiller 一次侧 = EG；**CDU 板式换热器为介质隔离边界**；CDU 二次侧 = PG25（不在本规格书范围）
- **Chiller 功能：** 为 CDU 一次侧（FWS）提供稳定冷冻水供应，覆盖 CDU 三支路总散热（S-Max 1350 kW + 板换/管损/泵热 ≈ 1400 kW，**含余量按 ≥ 1600 kW 设计**）

### 1.2 四级混合冷却架构

| 层级 | 技术手段 | 环境温度 | 典型站点 |
|---|---|---|---|
| L0 | 旁通阀 + 可选加热模块 | ≤ −15°C 极寒 | Kemi / TX 冬季 / Astana |
| L1 | 干冷器自由冷却 | −15 ~ +10°C | Kemi 春秋 / TX 冬季 |
| L2 | 干冷器 + 压缩机混合 | +10 ~ +35°C | TX 春秋 / 泰国凉季 |
| L3 | 湿膜辅助 + 满载压缩机 | > 35°C 极热 | UAE 夏 / TX 夏 / 泰国 |

> 干冷器为必配；旁通阀必配；湿膜与加热模块为可选（UAE / 泰国强烈建议湿膜；Astana 加热模块**强制必配**）。
