---
title: "I400C40 第二节：产品定位"
parent: "[[I400C40_Tech_Spec_CN]]"
order: 2
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/i400c40"
  - "#MDC"
created: 2026-07-28
source_file: "PUBLIC/Tech_Spec/I400C40_Tech_Spec_CN.md"
source_anchors:
  - "^sec-2-positioning"
---

## 2. 产品定位 ^sec-2-positioning

I400C40 是 **40ft 集装箱规格的单相浸没式液冷模块化数据中心**，内置 **8 × I50TS** 浸没槽，面向高性能 AI 推理、分布式训练与边缘算力部署。 ^mdc-978cf41c42

| 维度 | 定位 |
|------|------|
| 产品系列 | IMMERSION（浸没） |
| IT Zone 角色 | MDC 标准计算单元（可与 L1240C45 混合组集群） ^mdc-de226a7249 |
| GPU 平台 | 以 PCIe 为主（H100 / H200 / 4090 / A100 等） |
| 网络形态 | 以太网为主（10G/25G/100G/400G 可升级） |
| UPS | **外置（客户自备）** — 本体不含 UPS / UPS 电池 |
| UL 整机 | **否**（需要 UL 整机时选 [[I400C45]]） ^mdc-4cd0f94c5c |

> **冷却架构（两层）：**
> - **二次侧（介电液环路）**：服务器浸没于介电液 → Tank 内置 Dual CDU（板换）→ 将热排至一次侧
> - **一次侧（水侧 / 乙二醇）**：Hybrid Chiller 或纯干冷器将热量排至大气
> - **风冷支路**：独立 1×10kW 风冷机柜 + 精密空调，**不与浸没回路共用**

```
IT Load → Dielectric Fluid (Tank) → Dual CDU (in-tank) → Facility Water / EG
                                              ↓
                              Hybrid Chiller 或 纯干冷器（按站点气候选型）
```

**与同系列产品关系：**

| 产品 | 规格 | IT 容量 | 冷却 | UPS | UL |
|------|------|---------|------|-----|-----|
| **I50TS** | 单柜 | 45–50kW | 浸没 | 外置 | — ^mdc-a174d58fd6 |
| **I400C40** | 40ft | 360–400kW | 浸没 | **外置** | ❌ ^mdc-ca65d13ef5 |
| **I400C45** | 45ft | 400kW | 浸没 | 内置电力舱 | ✅ ^mdc-dfd92823ea |
| **L1240C45** | 45ft | 1240kW | DLC 冷板 | 内置 | ✅ ^mdc-ea4e8822d4 |

---
