---
title: "MDC Handbook — 系统设计原则"
parent: "[[MDC Engineering Handbook]]"
order: 3
tags:
  - #workspace/engineer
  - #type/engineering-handbook
  - #product/MDC
  - #architecture
  - #MDC
created: 2026-06-17
source_file: "KB/_COMMON/MDC Engineering Handbook.md"
source_anchors: []
---

# 3 System Design Principles（系统设计原则）

MDC 的系统设计原则旨在解决 AI Factory 基础设施面临的核心问题：**高密度算力、跨区域部署、能源效率、可靠性以及标准化交付。**

本章定义 MDC 在架构设计中的基本工程原则，这些原则适用于不同规模的算力集群，并指导 AC40、AC45、DC45 等模块的设计与实施。 ^mdc-60415c1c25

> **关联文档：** [[COOLING_SYSTEM_Guideline|KB/Guideline/COOLING_SYSTEM_Guideline]] · [[POWER_SYSTEMS_Guideline|KB/Guideline/POWER_SYSTEMS_Guideline]] · [[MDC/Reference Architecture/Site_Reference_Climate_Standard|KB/Reference Architecture/Site_Reference_Climate_Standard]]

***

## 3.1 全球环境适应性（Global Environmental Compatibility）

AI算力基础设施需要能够部署在不同的气候环境中，例如：

| 区域       | 气候特点                 |
| -------- | -------------------- |
| 欧洲 / 北美  | 冷凉气候，适合 Free Cooling |
| 澳大利亚     | 温暖气候，夏季高温            |
| 中亚       | 极端温差，冬季严寒            |
| UAE / 中东 | 高温、高沙尘               |

传统数据中心通常针对特定气候设计，而 MDC 的目标是实现 **跨气候环境部署能力**。

因此系统设计遵循以下原则：

**1 统一水温架构**

系统优先采用 **高温冷却水设计（High Temperature Cooling Loop）**：

典型设计范围：


| 维度        | Inlet   | Outlet  |
| --------- | ------- | ------- |
| Immersion | 32°C    | 36°C    |
| DLC       | 26-28°C | 36-38°C |


高温水系统可以显著提升以下能力：

- 提高 Free Cooling 使用比例
- 降低制冷设备功耗
- 提高系统整体能源效率

***

**2 混合制冷策略**

为了适应不同气候，MDC 冷却系统支持三种运行模式：

| 模式                 | 适用环境         |
| ------------------ | ------------ |
| Free Cooling       | 欧洲 / 北美      |
| Hybrid Cooling     | 澳大利亚 / 中亚    |
| Mechanical Cooling | UAE / 极端高温地区 |

通过 Hybrid Chiller 或 Dry Cooler + DX 系统组合，可以在不同环境下保持稳定运行。

***

**3 环境适应性设计**

系统在设计时需考虑以下环境因素：

- 高温环境
- 低温冻结风险
- 沙尘环境
- 电网稳定性差

例如：

- 冷却系统采用乙二醇混合液防止冻结
- 空气系统配置过滤系统防沙尘
- 电力系统具备独立运行能力

这些措施使 MDC 可以部署在 **电力资源丰富但基础设施较弱的地区**。

***

## 3.2 能源效率优先（PUE Optimization）

能源效率是 AI 数据中心最重要的指标之一。

MDC 的设计目标是：

```text
Immersion System PUE ≈ 1.04
DLC System PUE ≈ 1.15 – 1.20
```

实现这一目标的核心策略包括：

***

## 3.2.1 最大化液冷比例

空气冷却系统效率较低，因此 MDC 优先采用液冷技术：

- Immersion Cooling
- Direct Liquid Cooling (DLC)

液冷可以直接从芯片级别带走热量，大幅减少空气系统负担。

***

## 3.2.2 减少空气散热比例

在 AI GPU服务器中，大部分热量来自：

- GPU
- CPU
- HBM

这些组件可以通过液冷直接散热。

空气系统只需处理：

- 电源模块
- 网络设备
- 辅助组件

通过这种设计，可以将 **AIR HEAT比例(φ_air)控制在 8–27%**。

***

## 3.2.3 提高水温运行

传统数据中心通常采用：

```text
7°C – 18°C chilled water
```

而 MDC 系统设计为：

```text
26°C – 32°C cooling water
```

高温水系统具有以下优势：

- Dry Cooler 可以直接散热
- 减少压缩机制冷需求
- 提高 Free Cooling 比例

从而显著降低 PUE。

***

## 3.3 面向AI工作负载的可靠性设计

传统数据中心通常遵循 **Uptime Tier III / Tier IV** 架构。

然而 AI 工作负载与传统 IT 业务存在明显差异：

| 工作负载         | 特征     |
| ------------ | ------ |
| Web / Cloud  | 强 SLA  |
| AI Training  | 可中断    |
| AI Inference | 中等 SLA |

因此 MDC 的可靠性设计原则是：

**针对不同业务需求采用不同架构。**

***

## 3.3.1 AI Training

AI训练任务通常持续数小时或数天。

如果出现短暂中断：

- 可以重新启动任务
- 不会影响终端用户

因此训练集群可以采用：

**N+1 冗余架构**

而不需要传统 Tier IV 的 2N 架构。

***

## 3.3.2 AI Inference

AI推理通常需要提供实时服务，因此需要更高可靠性。

推理集群通常采用：

- 多区域部署
- 负载均衡
- 自动容错

基础设施层可以采用：

**Tier II 等级架构**

***

## 3.3.3 基础设施冗余策略

MDC 的冗余设计遵循以下原则：

| 系统   | 冗余策略        |
| ---- | ----------- |
| 电力系统 | N+1         |
| 冷却系统 | N+1         |
| 网络系统 | Dual Fabric |

这种设计在保证可靠性的同时，也避免了过度建设。

***

## 3.4 标准化交付（Standardized Deployment）

传统数据中心建设往往高度定制化，导致：

- 工程复杂
- 成本不确定
- 部署周期长

MDC 的设计目标是实现 **标准化交付模式**。

***

## 3.4.1 工厂预集成

MDC 模块在工厂完成以下系统集成：

- 电力系统
- 冷却系统
- 管道系统
- 控制系统

现场只需要完成：

- 电力接入
- 冷却接入
- 网络接入

即可投入运行。

***

## 3.4.2 标准接口

所有 MDC 模块采用标准接口设计，例如：

电力接口：

```text
10kV MV input
400-415V LV distribution
```

冷却接口：

```text
Supply / Return water connection
```

网络接口：

```text
Fiber uplink
```

标准接口可以显著简化现场安装。

***

## 3.4.3 模块化运维

MDC 的运维设计遵循 **模块化原则**：

- 每个模块可以独立维护
- 故障不会影响整个集群
- 设备更换简单

这种设计可以显著降低运维复杂度。

***

## 3.5 计算平台与冷却技术选型

MDC 支持两类主流 GPU 计算平台，分别对应不同的封装形态、功率密度与冷却技术。\
选型时需根据业务负载类型、功率密度需求与运维复杂度综合判断。

***

## 3.5.1 平台对比总览

| 维度     | PCIe 平台（AC40）                   | SXM 平台（DC45） ^mdc-46157bd9ce |
| ------ | ------------------------------- | ----------------------------------- |
| 典型 GPU | H100 PCIe / RTX 4090 / RTX 5090 | HGX H100/200 / B200/300 / GB200/300 |
| 封装形态   | PCIe 标准插卡                       | SXM 高密度模块                           |
| 互联方式   | 无 NVLink 依赖                     | NVLink / NVSwitch 高速互联              |
| 单机柜功率  | 40 – 80 kW / rack               | 100 – 150 kW / rack（及以上）            |
| 冷却技术   | Immersion Cooling（浸没式液冷）        | Direct Liquid Cooling（DLC 直接液冷）     |
| 冷却复杂度  | 低（无独立 CDU 链路）                   | 高（需 CDU、冷板水路、泄漏检测）                  |
| 网络复杂度  | 低                               | 高（需 InfiniBand / NVLink Fabric）     |
| 运维难度   | 低                               | 中高                                  |
| 适用场景   | AI 推理 / 分布式训练 / 边缘算力            | 大规模 AI 训练 / 高性能推理集群                 |

***

## 3.5.2 冷却技术说明

**Immersion Cooling（适用于 PCIe 平台）**

服务器整机浸入冷却液，热量由液体直接带走，无需风扇与冷板水路。

优势：

- 冷却效率高，可承受较高环境温度
- 机械结构简单，故障率低
- 维护成本低
- 技术已在 HPC 与矿场场景大规模验证

注意事项：

- 服务器需经过浸没兼容性验证
- 冷却液管理需纳入运维流程

***

**Direct Liquid Cooling（适用于 SXM 平台）**

冷板直接接触 GPU 模块表面，通过水路将热量导出至 CDU，再由 CDU 传递至外部冷却系统。

优势：

- 支持极高功率密度（100 – 150 kW / rack 及以上）
- 冷却精度高，可精确控制芯片结温

注意事项：

- CDU 需采用 2N 冗余设计
- 水路可靠性要求高，需配置泄漏检测系统
- 监控粒度需覆盖 node 级别与 loop 级别

***

## 3.5.3 选型建议

| 场景            | 推荐平台             | 理由                |
| ------------- | ---------------- | ----------------- |
| AI 推理为主       | PCIe + Immersion | 功率密度适中，运维简单，成本可控  |
| 大规模 AI 训练     | SXM + DLC        | 高带宽互联需求，功率密度高     |
| 混合负载（推理 + 训练） | AC40 + DC45 混合部署 | 按负载类型分区，兼顾效率与灵活性 ^mdc-8d6666af8c |
| 矿场改造 / 成本敏感场景 | PCIe + Immersion | 与矿场既有浸没冷却基础设施兼容性好 |

***

## 3.6 混合算力架构

在 AI Factory 场景中，不同类型 GPU 平台往往需要协同工作。

例如：

- PCIe GPU用于推理
- SXM GPU用于训练

因此 MDC 支持 **混合算力架构（Hybrid Compute Architecture）**。

不同类型计算模块可以在同一算力园区内部署，例如：

- AC40（Immersion Cluster） ^mdc-938ae98bdf
- DC45（DLC Cluster） ^mdc-79e0b7a814

这种架构可以在保证效率的同时，满足不同 AI 工作负载需求。

> **关联文档：** [[COOLING_SYSTEM_Guideline|KB/Guideline/COOLING_SYSTEM_Guideline]] · [[POWER_SYSTEMS_Guideline|KB/Guideline/POWER_SYSTEMS_Guideline]] · [[RA-002_Liquid_1.2MW|KB/Reference Architecture/EDGE_INFERENCE_DLC_1.2MW]]

# 4 Architecture（系统架构）
