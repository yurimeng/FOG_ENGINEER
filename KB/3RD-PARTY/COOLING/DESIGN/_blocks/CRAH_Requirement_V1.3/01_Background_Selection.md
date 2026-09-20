---
title: "CRAH v1.3 — 文件说明 + 平台背景 + 选型"
parent: "[[CRAH_Requirement v1.3]]"
order: 1
tags:
  - #workspace/engineer
  - #type/design-spec
  - #product/CRAH
  - #cooling
  - #MDC
created: 2026-06-17
source_file: "KB/3RD-PARTY/COOLING/DESIGN/.CRAH_Requirement v1.3.md"
source_anchors: []
---

## 0. 文件说明

本文档分为两部分：

- **✅ 我方设计规格**：已确定的技术参数，将作为合同规格写入
- **❓ 需 STULZ 确认项**：评估中发现的不一致或需供应商书面确认的参数，须 STULZ 回复后纳入正式规格书

**关键术语**：本文档所称 "CRAH"（Computer Room Air Handler）特指 DC45 顶部均匀排布的吊顶精密空调单元，物理实现为 STULZ OHS-084-DG-FC 自含式 DX。功能上承担机房残余空气热处理（≠ 传统 CRAH 全 CW 盘管型，自带压缩机）。 ^mdc-77dccbf28d

---

## 1. 平台与系统背景

| 项 | 值 |
|---|---|
| 适用产品 | DC45（45ft DLC 集装箱，8× 150 kW DLC 机柜 + 1× 风冷机柜） ^mdc-bfd0aad01b |
| GPU 平台 | NVIDIA GB300 NVL72 / DGX B300 |
| IT 容量 | 1240 kW（8× DLC 150 kW）+ 40 kW（风冷柜） |
| 冷却架构 | 三支路：主 CDU 液冷 / RDHx 后门风热回收 / **CRAH 顶置 CeilAir** |
| TCS 循环液 | **PG25（25% 丙二醇水溶液）**，ρ ≈ 1020 kg/m³，cp ≈ 3.95 kJ/(kg·K) |
| **TCS 进水设计值（CeilAir 冷凝侧进液）** | **26°C 单点**（V4 §1.3 锁定：FWS 22°C + CDU 板换 approach 4°C → TCS 26°C）；设计 / BOM / S-Max 校核**均按 26°C 工况进行** |
| TCS 设计 ΔT | 冷凝侧实际 ΔT ≈ 5–6°C @ datasheet 锁定流量 5.41 m³/h（287 kW / 9 ÷ (1020 × 3.95 × 5.41/3600) ≈ 5.3 K）|
| 机柜进风目标温度 | **25–27°C**（CRAH 出风混合后机房送风温度） |
| 机房回风工况（估算） | ~ 32°C DB / ~ 35% RH（封闭集装箱，低湿源） |

---

## 2. CRAH 选型与数量（✅ 我方锁定） ^crah-2-selection

| 项 | 值 | 备注 |
|---|---|---|
| **型号** | **STULZ CeilAir OHS-084-DG-FC** | 自含式吊顶 DX + 乙二醇/PG 冷凝 + 自由冷却 |
| **数量** | **9 台**（顶部均匀分布于 IT zone 上方） | 1 单元/机柜上方 |
| **冗余等级** | **N（无 N+1）** | 顶部空间已饱和，失效预案靠 GPU 降载 |
| **承载结构** | DC45 顶部钢梁，单台 250 kg × 9 = **2250 kg 顶置载荷** | ⚠️ 见 §11 Q5 ^mdc-c44f83456f |
| **配置版本** | **-DG-FC**（PG 兼容 + 含 Free Cooling 回路） | 不接受 -DW（水冷）或非 FC 版本 |

> **不接受替代选型**：本采购明确锁定 OHS-084-DG-FC。任何主动替换为 -DW、非 -FC、或他厂同级产品均须经 ATS 评审重出 BOM。

---

## 3. 热工性能（⚠️ 部分待确认） ^crah-3-thermal
