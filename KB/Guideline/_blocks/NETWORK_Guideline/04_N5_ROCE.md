---
title: "N-5 ROCE 设计原则"
parent: "[[NETWORK_Guideline]]"
order: 4
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/network
  - #architecture
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/NETWORK_Guideline.md"
source_anchors:
  - "N-5 ROCE 设计原则"
---

## N-5 ROCE 设计原则

### N-5.1 适用场景

| 场景 | ROCE 必要性 |
|------|------------|
| **以太网环境下的 RDMA 需求** | 推荐（替代 IB 的低成本方案）|
| **多租户云环境** | 推荐 |
| **混合集群（IB + 以太网）**| 边界互通 |

### N-5.2 ROCE 版本选型

| 版本 | 说明 |
|------|------|
| **RoCEv1** | L2 层 RDMA，仅同一广播域内 |
| **RoCEv2** | L3 层 RDMA，支持跨子网（推荐）|

### N-5.3 ROCE 网络设计要点

- **DCB（Differential Congestion Notification）必须开启**: PFC（Priority Flow Control）+ ECN（Explicit Congestion Notification）
- 网络设备（交换机）必须支持 DCB
- 推荐使用无损以太网（Lossless Ethernet）
- 优先级队列规划：存储流量高优先级，AI 训练流量最高优先级

> IB 与 RoCE 的协同部署边界见 [[#N-4 IB 设计原则]]。
