---
tags:
  - #workspace/engineer
  - #type/product
  - #product/mdc
---

# MDC – Modular Datacenter Cluster
模块化数据中心集群标准组合参考
版本：V1.1（2026-03-29 统一结构版）

---

## 1. MDC 定义

MDC（Modular Datacenter Cluster）是由多个模块组成的模块化数据中心。
每个 MDC 由三个 Zone 组成：

| Zone | 中文名 | 描述 |
|------|--------|------|
| **IT Zone** | 算力单元区 | 提供服务器容纳和 UPS，由 AC40 / DC45 组成 |
| **Cooling Zone** | 冷却单元区 | 外制冷，为 IT Zone 内服务器提供散热能力 |
| **Power Zone** | 电力单元区 | 后备电源系统，由 BESS 或柴油发电机提供 |

---

## 2. 架构图

```
Transformer → Switchgear → [Power Zone: BESS / Generator]
                          ↓
                    [IT Zone: AC40 / DC45]
                      ├── PDC → UPS → CDU → Tanks/Racks
                      ↓
              [Cooling Zone: Hybrid Cooling System（干冷器+DX一体化）]
```

---

## 3. IT Zone 产品对照

| 产品 | 规格 | IT 容量 | 冷却类型 | UPS 型号 | 电池后备 |
|------|------|---------|----------|----------|----------|
| **A32** | 单柜 | 45–50kW | 浸没式 | 外置（不含）| 外置 |
| **AC40** | 40ft 集装箱 | 400kW | 浸没式 | 9395XR-600 | 2×93LiG2（10min）|
| **DC45** | 45ft 集装箱 | 1200kW | DLC | 9395XR-1500 | 3×93LiG2（8min）|

参考：
- AC40 详细规格：[[PRODUCTS_AC40|KB/PRODUCTS_AC40]]
- DC45 详细规格：[[PRODUCTS_DC45|KB/PRODUCTS_DC45]]
- A32 详细规格：[[PRODUCTS_A32|KB/PRODUCTS_A32]]

---

## 4. 最小节点规格

| 等级 | IT 容量 | 典型配置 | 冷却方式 | 使用场景 |
|------|---------|---------|----------|----------|
| **Single** | 0.5MW | 8×AC40 或 ~10×DC45 | 浸没式 | 边缘推理 |
| **Small** | 1.2MW | ~3×DC45 或 ~3×AC40 | DLC / 浸没式 | 边缘推理 / 模型再训练 |
| **Medium** | 2–3MW | DC45 + AC40 混合 | 混合 | 区域级边缘节点 |
| **Large** | 5MW+ | 多个 MDC 并联 | 按需组合 | 数据中心级部署 |

---

## 5. 标准配置参考（团队引用标准）

> ⚠️ 以下为标准组合推荐。实际配置根据客户需求由 ATS 确认。

### 5.1 小规模边缘推理（0.5–1MW）

| 项目 | 配置 |
|------|------|
| 推荐产品 | AC40 |
| 数量 | 1–2 台 |
| IT 容量 | 400–800kW |
| 冷却 | 浸没式（干冷 + DX）|
| 电力 | Grid + UPS + BESS（推荐）/ 柴油发电机 |
| 冗余 | IT Zone 独立运行；Power Zone 可选 N+1 |

### 5.2 中等规模推理/训练（1–3MW）

| 项目 | 配置 |
|------|------|
| 推荐产品 | DC45 或 AC40+DC45 混合 |
| 数量 | 1–3 台 DC45，或混合组合 |
| IT 容量 | 1200–3600kW |
| 冷却 | DLC（干冷 + DX）|
| 电力 | Grid + UPS + BESS（推荐）|
| 冗余 | N+1（Power Zone 可升级 2N）|

### 5.3 大规模集群（3MW+）

| 项目 | 配置 |
|------|------|
| 推荐产品 | 多台 DC45 + AC40 组合 |
| 扩展方式 | 横向并联（增加集装箱数量）|
| IT 容量 | 3MW+ |
| 冷却 | 按集装箱类型独立配置 |
| 电力 | Grid + UPS + BESS（Power Zone N+1/2N）|

---

## 6. 冷却 Zone 配置标准

> 冷却 Zone 与 IT Zone **一对一配置**，每个 IT Zone 集装箱配置一套独立冷却设备。

| IT Zone | 冷却 Zone 配置 | 散热方式 |
|---------|---------------|----------|
| AC40（浸没式）| **Hybrid Cooling System**（干冷器+DX一体化）| 每台 AC40 独立配置 |
| DC45（DLC）| **Hybrid Cooling System**（干冷器+DX一体化）| 每台 DC45 独立配置 |

> ⚠️ **规则：不允许纯干冷器方案。** 无论 AC40 或 DC45，必须配置 Hybrid Cooling System（干冷器+DX一体化设备），确保环境温度 >28°C 时的散热能力。

参考：[[KB/3RD-PARTY/COOLING/COOLING_SYSTEM_SOLUTION|KB/COOLING_SYSTEM_SOLUTION]]

---

## 7. 电力 Zone 配置标准

| 架构 | 适用场景 | 特点 |
|------|---------|------|
| **Grid + UPS + BESS**（推荐）| 城市边缘 / 高 ESG 要求 / 电网不稳定 | 毫秒切换、稳压、模块化 |
| **Grid + UPS + 柴油发电机** | 偏远地区 / 长时备电需求（>8h）| 机械发电、长时间运行 |
| **Grid + UPS + BESS + 小型柴油** | 极端高可靠性需求 | BESS 覆盖瞬态 + 柴油兜底 |

> 参考：[[KB/3RD-PARTY/BESS/POWER_SYSTEMS_Guideline|KB/POWER_SYSTEMS_Guideline]]

---

## 8. 冗余设计规则

| Zone | 可选冗余 | 说明 |
|------|---------|------|
| **IT Zone** | **无内部冗余** | 每个容器独立运行；多容器之间可提供系统级 N+1/2N |
| **Cooling Zone** | **无内部冗余** | 每台冷却设备一对一服务对应 IT Zone；多套冷却设备之间无冗余共享 |
| **Power Zone** | **N+1 / 2N 可选** | 需要额外的 Switchgear 配置（成本增加）|

> ⚠️ **重要：** IT Zone 和 Cooling Zone 不提供 N+1 或 2N 冗余。每个容器/设备独立工作。如客户需要更高冗余，通过增加整个集装箱数量实现。
>
> **UPS 模块内部 N+1：** AC40/DC45 内置 UPS 模块（9395XR-600/1500）支持单模块故障不影响运行，但这不是 IT Zone 级别的冗余设计。

参考：[[ATS|AGENTS/ATS]]（Architecture Workflow, Step 3）

---

## 9. 交付周期

| 阶段 | 周期 | 说明 |
|------|------|------|
| 合同签署 + 预付款 | **30 天** | 合同签订后需支付预付款 |
| 制造（因量而定）| **90–180 天** | 集装箱数量越多，制造周期越长 |
| 海运 | **45–50 天** | 中国→北美主要港口参考时间 |
| 现场部署 | **30–45 天** | 场地准备、集装箱就位、系统调试 |
| **总周期（参考）** | **约 195–305 天** | 实际周期取决于项目规模 |

> ⚠️ **以上为单个集装箱单元参考周期。** MDC 集群（多台集装箱）因可并行制造，实际总周期与单台接近。详细周期需根据具体项目规模确认。

---

## 10. 网络 Zone 配置

网络设备由外部集成商提供（如"引澜"等），MDC 提供标准机柜空间和电源接口。

参考：[[KB/3RD-PARTY/NETWORK/PRODUCTS_NETWORK|KB/PRODUCTS_NETWORK]]

---

## 11. 设计原则

- **模块独立**：每个集装箱独立配置、独立运行
- **并联扩展**：通过增加集装箱数量实现容量扩展
- **分区消防**：每个集装箱独立消防系统
- **冗余供电**：UPS 内置于 IT Zone，BESS/发电机为 Power Zone

---

## 12. Power Flow

```
Grid Utility
    ↓
Transformer
    ↓
Switchgear / Breaker
    ↓
[BESS] ← 可选，Grid 不稳定或需要削峰时配置
    ↓
AC40 / DC45 IT Zone
    ├── PDC
    ├── UPS (EATON 9395XR)
    ├── CDU / 风墙
    └── 服务器负载
    ↓
Cooling Zone (Hybrid Cooling System)
```
