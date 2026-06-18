---
title: §P-1 IT 负载与整体电力负荷
parent: "[[../POWER_SYSTEMS_Guideline]]"
order: 1
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/power
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/POWER_SYSTEMS_Guideline.md"
source_anchors: []
---

## P-1 IT 负载与整体电力负荷 (IT Load & Total Facility Load)

### 背景 / Background

在与客户沟通时，**IT负载**与**整体电力负荷**是两个完全不同的概念。
客户通常询问的是"需要多少电"，但这个数字在不同语境下含义不同。

本节定义这两个术语的精确含义，并规定工程师团队在与客户沟通时必须主动确认的概念。

### IT 负载 (IT Load)

**定义：** 服务器、GPU、存储等计算设备实际消耗的电力。

**包含内容：**
- GPU 运行功率
- CPU 运行功率
- 内存 / 存储设备功率
- 服务器内 PSU 损耗（通常约 90–92% 效率）

**不包括：**
- UPS 系统损耗
- 冷却系统（CDU、干冷器、风墙）功率
- 照明、控制系统等辅助负载

**单位：** kW

**客户常见问法：**
- "我需要 1.2MW 的算力集群"
- "我要建一个数据中心，容量多少？"
- "买多少 GPU？"

### 整体电力负荷 / Total Facility Load

**定义：** 整个数据中心设施消耗的全部电力，包括 IT 设备、冷却、UPS、消防、照明等所有系统的总用电。

**包含内容：**
- IT 负载
- UPS 系统损耗（通常 2–5%）
- 冷却系统功率（CDU、水泵、干冷器、风墙）
- 照明
- 控制系统
- 其他辅助设备

**整体电力负荷 = IT负载 ÷ PUE**

**单位：** kW 或 MW

**客户常见问法：**
- "场地能提供多少电力？"
- "我们需要申请多少 kVA 的电网容量？"
- "这个数据中心总耗电多少？"
