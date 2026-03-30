

---
tags:
  - #workspace/engineer
  - #type/reference
  - #product/mdc
---

# REFERENCE_ARCHITECTURE — 标准参考架构索引

本文档列出工程工作区的标准参考架构，供团队在售前设计中快速引用。

版本：V1.1（2026-03-29 统一版）

---

## 参考架构列表

| 编号 | 名称 | IT 容量 | 产品 | 冷却类型 | PUE 参考 | 适用场景 |
|------|------|---------|------|---------|---------|---------|
| RA-001 | 0.5MW 浸没式推理单元 | 0.5MW | 1×AC40 | 浸没式 | ~1.08–1.20（取决于温度）| 边缘推理 |
| RA-002 | 1.2MW DLC 推理单元 | 1.2MW | 1×DC45 | 直冷液冷 DLC | ~1.12–1.35（取决于温度）| 中大型推理集群 |

---

## RA-001 — 0.5MW Immersion AI Inference Unit

**文件名**: [[Reference Architecture/EDGE_INFERENCE_IMMERSION_0.5MW]]

**核心参数速查：**

```
IT Load:        500kW（1×AC40）
Total Load:     ~540–600kW
Cooling:        Immersion + **Hybrid Cooling System**
Power:          Grid + UPS（EATON 9395XR-600）+ BESS
Redundancy:     UPS 模块 N+1 / CDU 1+1（**IT Zone 本身无内部冗余**）
Delivery:       约 195–305 天（制造90-180d + 海运45-50d + 部署30-45d）
```

**特征：** 浸没式液冷，PUE 极低（低温区 ~1.08），适合 GPU 推理

---

## RA-002 — 1.2MW DLC AI Inference Unit

**文件名**: [[Reference Architecture/EDGE_INFERENCE_DLC_1.2MW]]

**核心参数速查：**

```
IT Load:        1200kW（1×DC45）
Total Load:     ~1380–1560kW
Cooling:        DLC + **Hybrid Cooling System** + Air Wall
Power:          Grid + UPS（EATON 9395XR-1500）+ BESS
Redundancy:     UPS 模块 N+1 / 风墙 2+1（**IT Zone 本身无内部冗余**）
Delivery:       约 195–305 天（制造90-180d + 海运45-50d + 部署30-45d）
```

**特征：** 直冷液冷，高密度 DLC，适合 GPU 推理/训练

---

## 未来扩展架构

| 名称 | IT 容量 | 状态 |
|------|---------|------|
| 3MW GPU Training Cluster | 3MW | 规划中 |
| 10MW Modular AI Datacenter | 10MW | 规划中 |
| Immersion HPC Cluster | 待定 | 规划中 |

---

## 引用规则

> ⚠️ 所有参考架构中的 PUE 均为**参考值**，实际 PUE 取决于：
> - 环境温度
> - 散热方式（干冷器 vs DX vs 热泵）
> - 负载率
>
> 所有输出必须标注：**IT 负载 + 整体电力负荷 + PUE 范围**
>
> 参考：[[KB/POWER_LOAD.md|KB/POWER_LOAD]]

---

## 版本历史

| 日期 | 版本 | 变更内容 |
|------|------|---------|
| 2026-03-29 | V1.1 | 统一格式；PUE 改为变量；添加标准输出模板 |
| 初始版本 | V1.0 | 初始参考架构索引 |
