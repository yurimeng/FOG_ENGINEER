---
title: "CDU V5 — 容量水力锁定 + 接口规格"
parent: "[[CDU_Requirement V5]]"
order: 2
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

## 2. CDU 容量与水力锁定

| 参数 | 锁定值 | 余量 / 备注 |
|---|---|---|
| **换热量** | **≥ 1500 kW** | +11% vs S-Max 1350 kW |
| **板换 LMTD（设计点）** | **≥ 4°C** | FWS 22/32 + TCS 26/36，两端 ΔT 均 4K → LMTD=4 |
| **板换 UA（硬指标）** | **≥ 375 kW/K** | = 1500/4，+50% vs v3.1 250 kW/K（板片数 / 流道 ~1.5× 放大）|
| **板换 Q 闭环（出厂测试）** | (A) FWS 22→32 / TCS 36→26：Q ≥ 1500 kW； (B) FWS 22→32 / TCS 34→24：Q ≥ 1330 kW（φ_air=8% 护栏 VFD 节能工况）| 两组堆栈必须覆盖 |
| **二次侧额定流量** | **≥ 175 m³/h** | +12% vs φ_air=8% 工况 155.7 m³/h |
| **二次侧额定扬程** | **≥ 220 kPa**（≈22 m H₂O）| +17% vs 188 kPa（含主管+阀+滤）|
| **二次泵驱动** | **VFD**，调速范围 ≥ 70–100% | — |
| **二次泵控制目标** | TCS 供水 ≤ 26°C PID 闭环 | 下浮至 24°C 时降频节能 |
| **二次泵冗余** | **2N 或 N+1** | 单台失效不停机 |
| **一次侧设计流量** | **≥ 160 m³/h** | Astana 60% EG / cp 3.20 / ΔT 10 / 1500 kW 反推 + 2.4% 余量 |
| **一次侧最大工况流量** | ≥ 175 m³/h | Astana 极寒预热 |
| **系统工作压力** | ≤ 10 bar | — |

---

## 3. 接口规格

CDU 本体仅设置 **4 个水管接口**；三支路 PICV / 平衡阀 / 隔离阀 / 流量计**全部独立安装于现场管路**，不集成于 CDU。

| 接口 | 编号 | 管径 | 法兰 | 流量 | ΔP | 设计温度 | 介质 |
|---|---|---|---|---|---|---|---|
| 一次供水（Chiller → CDU）| P-IN | **DN100** | PN16 / Class 150 | 160–175 m³/h | ≤ 15 kPa | **22°C** | 站点 EG |
| 一次回水（CDU → Chiller）| P-OUT | DN100 | PN16 / Class 150 | 160–175 m³/h | ≤ 15 kPa | **32°C** | 站点 EG |
| 二次供水（CDU → manifold）| S-OUT | DN100 | PN16 / Class 150 | 149–175 m³/h | ≤ 20 kPa | **26°C 单点** | PG25 |
| 二次回水（manifold → CDU）| S-IN | DN100 | PN16 / Class 150 | 149–175 m³/h | ≤ 20 kPa | **36°C** | PG25 |

> 法兰位置建议侧出；接口距地 500–1200 mm；正前方维护空间 ≥ 600 mm。
> **一次侧管路前提**：100m FWS 管路（DN200 主干 95m + DN100 CDU 接入 5m）须按 §6 保温（≥50mm 岩棉），否则 22°C ±0.5°C 控制带被污染，吃光 4°C approach 预算。
