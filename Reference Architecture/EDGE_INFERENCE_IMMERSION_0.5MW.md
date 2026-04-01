---
tags:
  - #workspace/engineer
  - #type/reference
  - #product/ac40
---

# Reference Architecture — 0.5MW Immersion AI Inference Unit
0.5MW 浸没式 AI 推理算力单元标准参考架构

Reference Architecture Version: v1.1
Last Updated: 2026-03-29

---

## 1. 架构概述

本参考架构为基于浸没式液冷的 AI 推理算力单元，适用于边缘推理部署。

| 项目 | 内容 |
|------|------|
| IT 容量 | **0.5MW（500kW）** |
| 产品形态 | 1× AC40 集装箱 |
| 冷却技术 | 浸没式液冷（Immersion Cooling）|
| 散热方式 | **Hybrid Cooling System**（干冷器+DX一体化）|
| 交付周期 | 约 195–305 天（含制造、海运、部署）|

---

## 2. IT负载 vs 整体电力负荷

| 项目 | 数值 | 说明 |
|------|------|------|
| **IT 负载** | 500kW | 服务器、GPU 实际消耗 |
| **整体电力负荷** | ~540–600kW | 取决于 PUE（PUE 约 1.08–1.20）|
| PUE | **取决于环境温度** | 低温区 ~1.08–1.10；高温区（DX 运行）~1.15–1.20 |

---

## 3. 计算架构

| 项目 | 参数 |
|------|------|
| 服务器规格 | 双路 CPU，1.5TB RAM |
| GPU | 8 × NVIDIA RTX PRO 6000 Blackwell Server Edition |
| 服务器数量 | 64 台 |
| GPU 总数 | 512 GPUs |
| 单服务器 GPU | 8 × |
| 网络 | NVIDIA BlueField-3 DPU，OCP 25G × 1 |
| 服务器形态 | 4U |
| 主要用途 | AI 推理 |

---

## 4. 产品配置

本方案使用 **1× AC40**：

| 项目 | AC40 参数 |
|------|-----------|
| IT 容量 | 400kW（8×50kW A32 Tank）|
| 风冷辅助 | 10kW × 1 |
| UPS | EATON 9395XR-600（4 UPM × 150kW）|
| 电池 | 2× EATON 93LiG2（10 分钟后备）|
| CDU | 内阻 Dual CDU（2N 冗余）|
| 冷却 | **Hybrid Cooling System** |

> 注：单台 AC40 IT 容量为 400kW，1.2MW 方案需 3×AC40。

---

## 5. 冷却架构

| 项目 | 参数 |
|------|------|
| 冷却技术 | 浸没式液冷（Immersion）|
| Tank 型号 | A32，50kW/柜 |
| Tank 数量 | 8 台（组成 AC40）|
| 热交换器 | CDU（内置于 Tank），2N 冗余 |
| 散热方式 | **Hybrid Cooling System**（必须）|
| 进液温度 | 32–35°C |
| 出液温度 | 35–38°C |

---

## 6. 电力架构

| 项目 | 参数 |
|------|------|
| 电网连接 | Grid Utility |
| UPS | EATON 9395XR-600（4 UPM，600kW），内置于 AC40 |
| 电池后备 | 2× EATON 93LiG2，约 10 分钟 |
| 储能（BESS）| 1MW BESS（可选，Grid 不稳定地区推荐）|
| 功率路径 | Grid → BESS → Switchgear → AC40 |

---

## 7. 冗余策略

| 系统 | 冗余级别 | 说明 |
|------|---------|------|
| **UPS 模块** | 内部 N+1（4 模块）| 单模块故障不影响运行 |
| **CDU** | Dual CDU，1+1 | 完全冗余 |
| **IT Zone（AC40）** | **无内部冗余** | 单台 AC40 独立运行 |
| BESS（可选）| 可配置 N+1 | 按客户可靠性要求 |

---

## 8. PUE 参考

| 环境条件 | 运行模式 | PUE 参考值 |
|----------|---------|-----------|
| 环境 <28°C | Hybrid Cooling（干冷优先）| ~1.08–1.10 |
| 环境 28–35°C | Hybrid Cooling（DX 介入）| ~1.12–1.18 |
| 环境 >35°C | Hybrid Cooling（DX 主导）| ~1.18–1.25 |

---

## 9. 标准输出格式（团队引用模板）

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reference Architecture — 0.5MW Immersion AI Inference Unit
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

IT Load:       500kW（≈1×AC40）
Total Load:    ~540–600kW（PUE≈1.08–1.20）
Product:       AC40（Immersion Container，40ft）
Cooling:       Immersion + **Hybrid Cooling System**
Power:         Grid + UPS（9395XR-600）+ BESS（可选）
Redundancy:    UPS 模块 N+1 / CDU 2N（**IT Zone 本身无内部冗余**）
Delivery:      约 195–305 天（制造90-180d + 海运45-50d + 部署30-45d）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 10. 参考文档

- AC40 完整规格：[[PRODUCTS_AC40|KB/PRODUCTS_AC40]]
- A32 完整规格：[[PRODUCTS_A32|KB/PRODUCTS_A32]]
- MDC 组合标准：[[PRODUCTS_MDC|KB/PRODUCTS_MDC]]
- 冷却方案：[[KB/3RD-PARTY/COOLING/COOLING_SYSTEM_SOLUTION|KB/COOLING_SYSTEM_SOLUTION]]
- UPS 规格：[[KB/3RD-PARTY/Buildin/UPS_EATON_9395XR|KB/UPS_EATON_9395XR]]
