---
title: "I400C40 第八节：网络与线缆管理"
parent: "[[I400C40_Tech_Spec_CN]]"
order: 8
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/i400c40"
  - "#MDC"
created: 2026-07-28
source_file: "PUBLIC/Tech_Spec/I400C40_Tech_Spec_CN.md"
source_anchors:
  - "^sec-8-network"
---

## 8. 网络与线缆管理 ^sec-8-network

| 项目 | 参数 |
|------|------|
| 典型网络形态 | **以太网**（AI 推理 / 分布式训练场景；非默认 InfiniBand） |
| 速率支持 | 10G / 25G / 100G / **400G 可升级** |
| 协议 | IPv4 / IPv6；未来可扩展 IB（项目定制） |
| 电缆穿舱口 | 支持顶部 / 底部 / 侧面进线（以图纸为准） |
| 线缆管理 | 柜顶桥架 / 走线槽；强弱电分区 |
| 带外管理 | BMC / IPMI / iLO / iDRAC 独立管理网布线 |
| 网络设备 | 交换机 / 防火墙等由项目或集成商配置；MDC 提供机柜空间与电源接口 |

![[I400C40_NETWORK_CONF_v1.svg]]
*I400C40 网络与监控配置示意*

参考：[[KB/IMMERSION/I400C40/I400C40_NETWORK_CONF]] · [[NETWORK_Guideline]] · [[KB/IMMERSION/_line/PRODUCTS_NETWORK]]

### 8.1 布线能力（项目集成）

| 类别 | 说明 |
|------|------|
| 光纤 | 预端接光缆、LC/SC/MPO |
| 铜缆 | Cat6A / Cat7 / Cat8 |
| 配线架 | ODF / 铜缆配线架 |
| 标准 | TIA-568 · ISO/IEC 11801 · IEEE 802.3 |

### 8.2 与各 Zone 配合

| Zone | 网络需求 |
|------|----------|
| IT Zone | 服务器高速互联 + 带外 |
| Cooling Zone | CDU / 干冷器 / Chiller 监控接入 |
| Power Zone | UPS / BESS 带外管理 |

---
