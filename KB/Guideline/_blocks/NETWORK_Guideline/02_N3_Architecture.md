---
title: "N-3 网络架构选型"
parent: "[[NETWORK_Guideline]]"
order: 2
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/network
  - #architecture
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/NETWORK_Guideline.md"
source_anchors:
  - "N-3 网络架构选型"
---

## N-3 网络架构选型

### N-3.1 三层网络模型

MDC 网络架构遵循典型的**三层网络模型**:

| 层级 | 功能 | 说明 |
|------|------|------|
| **接入层（Access）** | 服务器节点高速互联 | 交换机直接连接服务器，支持 10G/25G/100G |
| **汇聚层（Aggregation）** | 跨服务器流量汇聚 | 聚合多个接入层交换机流量 |
| **核心层（Core）** | 跨集群/外部连接 | 连接汇聚层与外部网络 |

### N-3.2 网络拓扑选型

| 拓扑类型 | 适用场景 | 优势 | 劣势 |
|---------|---------|------|------|
| **传统三层** | 中小型集群（<50节点）| 结构清晰，易管理 | 延迟较高 |
| **Fat Tree** | 中大型集群 | 延迟低，可扩展 | 成本较高 |
| **Dragonfly** | 超大规模集群（AI 训练）| 极低延迟，极高带宽 | 设计复杂 |

> 拓扑选型与 IT Zone 形态的对应关系见 [[#N-9 网络与 IT Zone 匹配]]。
