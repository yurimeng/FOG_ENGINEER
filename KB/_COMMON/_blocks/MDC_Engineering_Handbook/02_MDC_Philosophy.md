---
title: "MDC Handbook — 设计理念（MDC Philosophy）"
parent: "[[MDC Engineering Handbook]]"
order: 2
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

# 2 MDC Philosophy（MDC设计理念）

MDC（Modular Data Center）是一种面向 **AI Factory 算力生产模式** 的基础设施架构。其核心目标是将传统数据中心从 **大型定制工程（Construction Project）** 转变为 **可工业化生产的算力基础设施模块（Infrastructure Appliance）**。

在这种模式下，数据中心不再是一次性建设的大型建筑，而是由多个标准化算力模块组成，可以像工业设备一样：

- 标准化生产
- 快速部署
- 按需扩展

MDC 的设计理念围绕以下几个核心原则展开。

***

## 2.1 算力基础设施产品化（Infrastructure as Product）

传统数据中心通常被视为 **工程项目（Project）**：

- 每个数据中心独立设计
- 大量现场施工
- 依赖本地工程条件

这种模式导致：

- 部署周期长（12 – 24个月）
- 成本不可预测
- 复制困难，难以规模化交付

MDC 的核心理念是将数据中心转变为 **产品化基础设施（Infrastructure Appliance）**：

| 维度     | 传统数据中心          | MDC             |
| ------ | --------------- | --------------- |
| 设计模式   | 项目定制，每站独立设计     | 标准化产品，工厂预集成     |
| 建设方式   | 大量现场施工，依赖本地工程条件 | 工厂完成主要集成，现场仅做接入 |
| 部署周期   | 12 – 24个月       | 75 – 90天        |
| 扩展方式   | 整体扩建，规划周期长      | 按模块线性扩展，按需增长    |
| 成本可预测性 | 低，受现场条件影响大      | 高，出厂即可确定成本结构    |
| 复制能力   | 低，每站重新设计        | 高，同一模块可快速复制部署   |
|        |                 |                 |

通过产品化设计，MDC 可以实现：

- **大规模标准化生产**：模块在工厂完成系统集成与测试
- **快速复制部署**：同一产品规格可在不同场地重复交付
- **可预测的成本结构**：减少现场变量对造价的影响

这使 MDC 更适合 AI Factory 对算力基础设施 **快速交付、按需扩展** 的核心需求。

***

## 2.2 模块化架构（Modular Architecture）

MDC 将数据中心拆分为多个 **功能独立的模块**。

每个模块都具备完整的功能能力，并可以独立运行。

典型 MDC 架构包括：

- 计算模块
- 冷却模块
- 电力模块
- 网络模块

通过模块化设计，可以实现：

- **线性扩展（Linear Scaling）**
- **快速部署（Rapid Deployment）**
- **故障隔离（Fault Isolation）**

在模块化架构下，算力基础设施可以像工业产线一样逐步扩展。

***

## 2.3 快速部署（Rapid Deployment）

AI算力需求变化速度极快，因此算力基础设施必须具备快速部署能力。

MDC 的设计目标是：

**从运输到运行的部署周期控制在 75 – 90 天以内。**

实现这一目标的关键手段包括：

- 工厂预集成（Factory Integration）
- 标准化接口（Standard Interface）
- 最小化现场施工（Minimal Onsite Work）

在现场部署阶段，通常只需要完成：

- 电力接入
- 冷却系统接入
- 网络接入

即可投入运行。

***

## 2.4 高密度算力支持（High Density Compute）

AI GPU服务器的功率密度正在快速上升。

现代AI机柜功率密度已经达到：

**80kW – 150kW / rack**

未来可能进一步提高。

因此 MDC 的设计原则之一是：

**原生支持高密度计算。**

为实现这一目标，MDC 采用以下策略：

- 优先采用液冷技术（DLC / Immersion）
- 最大化热量捕获比例
- 减少空气散热比例
- 使用高温水冷却系统

这种架构能够显著提高冷却效率，并降低能源消耗。

***

## 2.5 最小化场地依赖（Site Agnostic Deployment）

传统数据中心通常依赖复杂的基础设施，例如：

- 大型建筑
- 完整的机电系统
- 复杂冷却设施

MDC 的设计目标是：

**降低对场地基础设施的依赖。**

MDC 模块通常只需要以下外部条件即可运行：

- 电力接入
- 冷却系统接口
- 网络接入

这使 MDC 可以部署在多种环境中，例如：

- 工业园区
- 矿场场地
- 能源基地
- 偏远地区

从而显著提高算力基础设施的部署灵活性。

***

## 2.6 按需扩展（Demand Driven Scaling）

传统数据中心通常采用 **预建设模式**：

一次性建设大量机房空间，然后逐步部署服务器。

这种模式在 AI 时代存在较高风险：

- 算力需求不确定
- GPU供应不稳定
- 技术迭代快速

MDC 采用 **模块化扩展模式**：

算力基础设施可以按模块逐步扩展。

例如：

- 1 个模块
- 4 个模块
- 16 个模块
- 64 个模块

每个模块都可以独立运行，同时也可以组成更大的算力集群。

这种方式可以有效降低：

- 资本投入风险
- 建设周期风险
- 技术迭代风险

***

## 2.7 面向AI Factory的算力基础设施

AI Factory 的核心目标是持续生产 AI 算力。

因此算力基础设施必须具备：

- 高效率
- 高可靠性
- 高扩展能力

MDC 正是为这一目标设计的基础设施架构。

在这种模式下：

- 每个 MDC 模块都是一个算力生产单元
- 多个 MDC 模块可以组成算力集群
- 整个系统可以像工业生产线一样扩展

从而构建面向未来的 **AI算力工厂基础设施**。

> **关联文档：** [[RA-002_Liquid_1.2MW|KB/Reference Architecture/EDGE_INFERENCE_DLC_1.2MW]] · [[RA-001_Immersion_0.4MW|KB/Reference Architecture/EDGE_INFERENCE_IMMERSION_0.4MW]] · [[MDC_Product_Quick_Ref|KB/_COMMON/MDC_Product_Quick_Ref]]

# 3 System Design Principles（系统设计原则）
