---
title: §P-8 BESS 选型与 DG 对比（上）
parent: "[[../POWER_SYSTEMS_Guideline]]"
order: 5
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/power
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/POWER_SYSTEMS_Guideline.md"
source_anchors: []
---

## P-8 BESS 选型与 DG 对比 (BESS Selection & DG Comparison)

> **来源**：Works_Public/Projects/Simple_Mining/DG vs BESS.md
>
> 以下内容是从客户项目中提取的通用电力架构知识，已固化为知识库标准内容。

### 背景 / Background

在与客户讨论备用电力架构时，柴油发电机（DG）和电池储能系统（BESS）是两种主要方案。

本节定义两者的对比框架，并解释在特定电网环境下（如 MISO 区域）的选型逻辑。

### BESS 的核心优势

| 特性 | 说明 |
|------|------|
| 环保 | 零排放，无需燃料储备 |
| 响应速度 | 毫秒级切换，无启动延迟 |
| 维护 | 维护需求远低于 DG |
| ESG 友好 | 符合 Net Zero 和 ESG 目标 |
| 场景灵活 | 适合短中期断电（分钟级到小时级） |

### Grid Curtailment — 电网限电机制

### 定义

**Curtailment（限电）**：电网在供应紧张时，要求大用户减少用电或切换自备电源。

常见触发条件：
1. 电网需求超过供应
2. 输电容量不足
3. 紧急电网状态

### 典型参数

| 指标 | 数值 |
|------|------|
| 提前通知时间 | 至少 2 小时 |
| 单次事件最长持续 | 约 6 小时 |
| 高发时段 | 夏季用电高峰 |

> ⚠️ 这也是为什么 Hyperscale 数据中心通常配置备用发电机。

### BESS 在 Curtailment 中的作用

```
正常情况：
  Grid → Data Center

Curtailment 时：
  Grid ↓（下降）
  BESS → Data Center（补充）

GPU 无需停机。
```

BESS 作为缓冲层，确保在电网限电期间 IT 负载持续运行。

### Demand Response — 需求响应

### 两种参与模式

| 模式 | 说明 |
|------|------|
| **Demand Response** | 电网发信号要求减少用电，数据中心配合降低功率 |
| **Interruptible Rate** | 电价更便宜，条件是电网可要求停电 |

### AI 数据中心的优势

AI 计算的特点：
- 很多 workload 是 **batch / training**
- 可以暂停、降低 GPU 利用率、延迟任务

因此 AI 数据中心可以参与需求响应：

```
Grid 紧张
  ↓
Reduce load 20–30%
  ↓
几小时后恢复
  ↓
电网支付补偿
```

### BESS + Curtailable Load — 新型架构趋势

### 核心洞察

在风电比例高的电网区域（如 MISO），出现新趋势：

> AI 数据中心采用 **BESS + Curtailable Load** 替代传统 DG

原因：
- 风电波动大，电价波动大
- Curtailment 机会多
- AI 负载可调节

### 架构对比

| 架构 | 说明 |
|------|------|
| 传统架构 | Utility → UPS/BESS → Diesel Generator（DG）|
| 新型架构 | Utility → BESS → IT Load（含 Curtailable 响应能力）|

### 战略意义

AI 数据中心正在被重新定义为：

> **Flexible Load Resource（灵活负荷资源）**
> 而不是：
> **Critical Load（关键负荷）**

这是电力市场的一个重大变化，使 BESS 成为更有吸引力的选择。
