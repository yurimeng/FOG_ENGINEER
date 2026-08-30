---
title: "Hybrid Chiller V1.6 — 项目背景 + 整体方案架构"
parent: "[[Hybrid Chiller Requirement V1.6]]"
order: 1
tags:
  - #workspace/engineer
  - #type/design-spec
  - #product/Hybrid-Chiller
  - #cooling
  - #MDC
created: 2026-06-17
source_file: "KB/3RD-PARTY/COOLING/DESIGN/.Hybrid Chiller Requirement V1.6.md"
source_anchors: []
---

## 1. 项目背景与目标

本需求书面向 Hybrid Chiller（混合冷水机组）制造商，旨在为模块化数据中心（MDC）产品线的 DC45 型号采购一款高效、可扩展的冷却解决方案。

DC45 采用 Direct-to-Chip（DtC）液冷技术，为高密度 GPU/AI 加速计算平台（如 NVIDIA GB300 NVL72）提供冷却。整机 IT 功耗目标为 1.2 – 1.5 MW，布置于标准化集装箱内。

本规格书覆盖五类典型气候站点：**极热干燥（UAE）、极热湿润（泰国）、温带大陆（美国德克萨斯）、极寒（芬兰 Kemi）、极端双向温差（哈萨克斯坦 Astana）**，供应商须就所报产品说明其在各类气候下的适配性与性能数据。

### 1.1 冷却架构概述

- **冷却介质（Chiller 侧）：** 乙二醇混合液（EG，防冻液浓度根据站点气候调整，见附录 A）
- **介质边界：** Chiller 一次侧（本规格书覆盖）= EG；**CDU 板式换热器为介质隔离边界**；CDU 二次侧 = PG25 25% 丙二醇（见 [[CDU_Requirement]] v2.1，不在本规格书范围）
- 冷却方式：Direct-to-Chip（板式换热器直接连接服务器冷板）
- 末端设备（CDU 二次侧三支路）：① 8 台 GB300 NVL72 DLC 液冷机架（Branch 1）② 9 台 VERTIV DCD35/50 RDHX 后门（Branch 2）③ 9 台 STULZ OHS-084-DG-FC CeilAir 顶置 CRAH 冷凝侧（Branch 3）
- **Chiller 功能：** 为 CDU 一次侧（外部 TCS）提供稳定冷冻水供应，覆盖 CDU 全部三支路总散热（S-Max 1350 kW + 板换/管损/泵热 ≈ 1400 kW，含余量按 ≥ 1,600 kW 设计；S-Max 数值按 [[../../LIQUID/L1240C45/DESIGN/L1240C45 三支路冷却重评估 V4|V4 锁定]] §4.4 / §6.2，对应 TCS 26°C 单点 + 4°C CDU 板换接近温差）

---

## 2. Hybrid Chiller 整体方案架构

本方案采用四级混合冷却架构：旁通阀温度保护为极寒工况兜底，干冷器（Dry Cooler）为基础散热手段，机械压缩制冷为辅助补偿手段，湿膜蒸发冷却为可选强化手段。

### 2.1 架构层级

| 层级 | 技术手段 | 适用环境温度 | 典型站点 | 说明 |
|------|----------|------------|---------|------|
| Level 0 | **旁通阀 + 可选加热模块** | **≤ –15°C（极寒）** | **Kemi FI、TX冬季** | 旁通干冷器，防止供水过冷；加热模块可选配 |
| Level 1 | 干冷器自由冷却 | –15°C ~ +10°C | Kemi FI春秋、TX冬季 | 100% 自然散热，压缩机关闭，COP 最优（≥ 15） |
| Level 2 | 干冷器 + 压缩机制冷（混合） | +10°C ~ +35°C | TX春秋、泰国最凉季 | 按温度梯度逐步投入压缩机，COP 3.5–8.0 |
| Level 3 | 湿膜蒸发辅助（可选）+ 满负荷压缩机 | **> 35°C（极热）** | **UAE夏季、TX夏季、泰国全年** | 湿膜降低进气温度；UAE夏季须满载3台压缩机 |

> **注：** 干冷器为必配；旁通阀为必配；湿膜蒸发冷却和加热模块为可选配置项，由买方在订单时确认是否选配。UAE / 泰国站点**强烈建议**选配湿膜模块。

---

