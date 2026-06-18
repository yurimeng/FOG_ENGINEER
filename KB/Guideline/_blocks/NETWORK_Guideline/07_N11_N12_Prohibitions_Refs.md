---
title: "N-11/N-12 禁止事项与参考文档"
parent: "[[NETWORK_Guideline]]"
order: 7
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/network
  - #architecture
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/NETWORK_Guideline.md"
source_anchors:
  - "N-11 禁止事项"
  - "N-12 参考文档"
---

## N-11 禁止事项

- ❌ 带外管理网络不得与带内管理网络共用物理链路
- ❌ IB 和以太网不得混用同一交换机（除非网关设备）
- ❌ 禁止不带冗余的单点网络链路
- ❌ 禁止不带 BMC/IPMI 的服务器入网

> 上报触发条件见 [[PRINCIPLE_Guideline#§1.6 上报原则]] 与 SPOF 识别 [[Risk_Guideline#§R-2 单点故障识别]]。

---

## N-12 参考文档

- 网络产品（引澜布线系统）：[[PRODUCTS_NETWORK]]
- AC40 网络端口配置：[[AC40_NETWORK_CONF|KB/3RD-PARTY/NETWORK/AC40_NETWORK_CONF]]（PDF 元数据伴侣）
- AC40 产品规格：[[AC40]]
- DC45 产品规格：[[PRODUCTS_DC45]]
- MDC 标准组合：[[PRODUCTS_MDC]]
- 索引与执行准则：[[PRINCIPLE_Guideline]]
- 相关：[[COOLING_SYSTEM_Guideline]]、[[POWER_SYSTEMS_Guideline]]、[[Risk_Guideline]]、[[Compliance_Guideline]]
