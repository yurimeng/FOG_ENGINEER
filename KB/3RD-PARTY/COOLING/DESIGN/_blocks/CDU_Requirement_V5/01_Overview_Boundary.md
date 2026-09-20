---
title: "CDU V5 — 文件说明 + 系统背景与边界条件"
parent: "[[CDU_Requirement V5]]"
order: 1
tags:
  - #workspace/engineer
  - #type/design-spec
  - #product/CDU
  - #cooling
  - #MDC
created: 2026-06-17
source_file: "KB/3RD-PARTY/COOLING/DESIGN/CDU_Requirement V5.md"
source_anchors: []
---

## 1. 系统背景与边界条件

**适用产品：** DC45（45ft DLC 集装箱，8× 150 kW DLC 机柜 + 1× 风冷机柜） ^mdc-24b95f75c4
**GPU 平台：** NVIDIA GB300 NVL72 / DGX B300（或同等 DLC 平台）
**IT 容量：** 1240 kW（8× 150 + 40）
**DLC 液冷比例 φ_air：** 设计上限 27%（S-Max），护栏 ≥ 8%

| 边界 | 锁定值 |
|---|---|
| **一次侧介质** | 站点 EG（UAE 25% / TX 40% / Kemi 55% / Astana 60%）|
| **二次侧介质** | **PG25（25% 丙二醇）** |
| **介质边界** | CDU 板式换热器（两侧不直接连通） |
| **FWS 供水（Chiller → CDU）** | **22°C 单点**（精度 ±0.5°C，前提：一次侧管路按 §6 保温）|
| **FWS 回水（CDU → Chiller）** | **32°C**（ΔT 10°C） |
| **CDU 板换接近温差（Approach）** | **4°C**（LMTD 设计上限） |
| **TCS 供水（CDU → 三支路）** | **26°C 单点** = FWS 22 + Approach 4 |
| **TCS 回水（三支路 → CDU）** | **36°C**（冷板 ΔT 10°C） |
| **主泵归属** | TCS 主泵 = CDU 自带；FWS 主泵 = [[Hybrid Chiller Requirement V5]] §10 集成 |

### 1.1 三支路热负荷边界（TCS 26°C 单点，φ_air 全场景）

| 场景 | φ_air | DLC 液冷 | RDHX 吸热 | CeilAir 负荷 | **CDU 总热** |
|---|---|---|---|---|---|
| S-Low | 10% | 1080 | 88.0 | 126.0 | 1331 kW |
| S-Mid | 15% | 1020 | 121.0 | 153.0 | 1337 kW |
| S-High | 20% | 960 | 154.0 | 180.0 | 1342 kW |
| **S-Max** | **27%** | 876 | 200.2 | 217.8 | **1350 kW** |
| **CDU 护栏** | **8%** | **1104** ← 冷板最大 | 74.8 | 115.2 | 1329 kW |

> 反直觉：φ_air 越低，冷板支路流量需求越大。CDU 必须按 φ_air=8% 工况设计冷板支路供应能力。
