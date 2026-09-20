---
title: "Hybrid Chiller V5 — 性能与额定参数"
parent: "[[Hybrid Chiller Requirement V5]]"
order: 2
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

## 2. 性能与额定参数

| 参数 | 锁定值 | 备注 |
|---|---|---|
| **额定制冷量** | **≥ 1600 kW** | S-Max 1352 kW + 板换/管损/泵热 + 应急余量 |
| **FWS 供水（Chiller → CDU 一次入口）** | **22°C** | V1.6 锁定外制冷机出水；精度 ±0.5°C；前提是一次侧管路按 §6 保温 |
| **FWS 回水（CDU → Chiller）** | **32°C**（ΔT 10°C） | — |
| **FWS 流量** | **≥ 160 m³/h** | Astana 60% EG / cp 3.20 / ΔT 10 / 1600 kW 最严苛站点反推 + 2.5% 余量 |
| 系统工作压力 | ≥ 10 bar 设计压力 | 须通过水压测试 |
| **干冷器散热量（自由冷）** | **≥ 1700 kW @ 10°C 环境** | 与 [[CDU_Requirement V5]] §1 室外侧基线对齐 |
| 综合 COP（25°C 环境满载） | ≥ 3.5 | 含风机 / 水泵辅助 |
| 极热 COP（UAE 46°C 满载，湿膜启用） | ≥ 2.8 | — |
| 部分负荷 IPLV | ≥ 5.0 | AHRI 550/590 或 GB/T 18430 |
| 噪声 | ≤ 75 dB(A) @ 1m 满载 | 夜间可静音 |
| 外形 | 40/45ft ISO 集装箱框架 UH | 与 DC45 外部空间匹配 ^mdc-9c408eccde |
| 整机重量（运行）| ≤ 15,000 kg | — |
| 防护等级 | IP54（室外）| 含风机 / 控制柜 |
| 设计寿命 | ≥ 15 年（年维护 ≤ 2 次；UAE / 泰国 ≤ 6 月 / ≤ 2500 运行小时）| — |
