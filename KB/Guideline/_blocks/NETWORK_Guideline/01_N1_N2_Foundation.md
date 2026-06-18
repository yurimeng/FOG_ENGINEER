---
title: "N-1/N-2 文件定位与核心设计原则"
parent: "[[NETWORK_Guideline]]"
order: 1
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/network
  - #architecture
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/NETWORK_Guideline.md"
source_anchors:
  - "N-1 文件定位"
  - "N-2 核心设计原则"
---

## N-1 文件定位

> **本文档为网络系统设计原则（Guideline），定义网络架构选型、IB/ROCE 策略、带内/带外管理原则和产品匹配规则。**
> 具体产品参数请查阅各产品文档。

| 项目 | 说明 |
|------|------|
| **Supplier Name** | — |
| **Category** | Network System Design Guideline |
| **适用对象** | MDC 模块化数据中心集群（Network Zone）设计选型总则 |
| **版本** | V1.3（2026-06-05 章节 ID 归位与结构标准化） |
| **总入口** | 统一执行准则与章节 ID 体系见 [[PRINCIPLE_Guideline]] |

**引用顺序**:
1. [[NETWORK_Guideline]] ← 本文档（位于 `KB/Guideline/`）
2. 按架构类型查阅对应产品文档（位于 `KB/3RD-PARTY/NETWORK/`）

> 跨文件引用规范: 详见 [[PRINCIPLE_Guideline#§2 文件清单与章节 ID 体系]]。

---

## N-2 核心设计原则

| 原则 | 说明 |
|------|------|
| **分层架构** | 接入层 / 汇聚层 / 核心层三层模型 |
| **AI 负载优先** | 网络设计优先满足 GPU 集群高速互联需求 |
| **管理分离** | 带内管理网络与业务网络物理隔离 |
| **高可靠冗余** | 关键链路和设备支持冗余配置 |

> 详细分层实现见 [[#N-3 网络架构选型]]；管理分离与高可靠冗余见 [[#N-6 带内管理网络]]、[[#N-7 带外管理网络]]、[[#N-8 带内 vs 带外管理对比]]。
