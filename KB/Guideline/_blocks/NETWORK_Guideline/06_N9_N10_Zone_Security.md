---
title: "N-9/N-10 网络与 IT Zone 匹配与安全设计"
parent: "[[NETWORK_Guideline]]"
order: 6
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/network
  - #architecture
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/NETWORK_Guideline.md"
source_anchors:
  - "N-9 网络与 IT Zone 匹配"
  - "N-10 安全设计原则"
---

## N-9 网络与 IT Zone 匹配

| IT Zone | 推荐网络架构 | IB 需求 | 管理网络 |
|---------|------------|--------|---------|
| **A32**（独立）| 小型二层网络 | 可选 | 带内 + 带外 ^mdc-e9b2c4f81f |
| **AC40**（40ft）| 三层网络（接入/汇聚/核心）| 推荐（推理）| 带内 + 带外 ^mdc-bc75dd0c88 |
| **DC45**（45ft）| 三层网络 + IB 高速互联 | 必须（训练集群）| 带内 + 带外 ^mdc-b51c4d7b65 |
| **MDC 集群** | 多集群互联，大型 Fat Tree | 按集群需求 | 带内 + 带外 |

> IT Zone 容量与 UPS 配置见 [[POWER_SYSTEMS_Guideline#§P-2 产品对照表]]；IT↔Cooling 配对见 [[COOLING_SYSTEM_Guideline#§G-8 IT Zone 与冷却区匹配]]。

---

## N-10 安全设计原则

| 安全措施 | 说明 |
|---------|------|
| 网络分段 | VLAN 隔离不同业务区域 |
| 防火墙 | 边界部署，访问控制 |
| IDS/IPS | 入侵检测与防御 |
| 加密传输 | TLS/IPsec 加密管理流量 |
| 802.1X | 接入层设备认证 |

> 合规与认证要求汇总见 [[Compliance_Guideline#§C-7 认证要求汇总]]。
