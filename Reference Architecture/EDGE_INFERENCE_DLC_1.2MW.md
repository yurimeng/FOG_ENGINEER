---
tags:
  - #workspace/engineer
  - #type/reference
  - #product/dc45
---

# Reference Architecture — 1.2MW DLC AI Inference Unit
1.2MW 直冷液冷 AI 推理算力单元标准参考架构

Reference Architecture Version: v1.2
Last Updated: 2026-05-09

---

## 1. 架构概述

本参考架构为基于直冷液冷（DLC）的 AI 推理算力单元，适用于中大型边缘推理集群。

| 项目 | 内容 |
|------|------|
| IT 容量 | **1.2MW（1240kW）** |
| 产品形态 | 1× DC45 集装箱 |
| 冷却技术 | Direct Liquid Cooling（直冷液冷 DLC）|
| 散热方式 | **Hybrid Cooling System**（干冷器+DX一体化）+ FCU |
| 交付周期 | **~185–230 天（参考值）** |

---

## 2. IT负载 vs 整体电力负荷

| 项目 | 数值 | 说明 |
|------|------|------|
| **IT 负载** | 1240kW | 服务器、GPU 实际消耗 |
| **整体电力负荷** | ~1325–1675kW | 取决于 PUE（PUE 约 1.07–1.35）|
| PUE | **取决于环境温度** | 低温区 ~1.07–1.15；高温区 ~1.25–1.35 |

---

## 3. 计算架构

| 项目 | 参数 |
|------|------|
| 服务器类型 | GPU 服务器（如 NVIDIA B300 等 DLC 兼容服务器）|
| PSU 类型 | 单相 200–240V |
| 冷却方式 | 冷板式直冷液冷（Cold Plate DLC）|
| 服务器进口温度 | 26–28°C |
| 负载特性 | 高动态（AI 负载）|

---

## 4. 产品配置

本方案使用 **1× DC45**：

| 项目 | DC45 参数 |
|------|-----------|
| IT 容量 | 1240kW（8×150kW DLC Racks + 1×40kW 风冷）|
| 风冷辅助 | 40kW × 1 |
| UPS | EATON 9395XR-1500（10 UPM × 150kW）|
| 电池 | 3× EATON 93LiG2（8 分钟后备）|
| 主 CDU | 1.2MW Rack CDU × 1 |
| 备用 CDU | 150kW In-Rack CDU（可选）|
| FCU | **12×40kW**（根据环境温度动态调整），18–25°C |
| 冷却 | 干冷器 + DX（每台 DC45 独立配置）|
| Busbar | SIEMENS 2500A |

---

## 5. 电力架构

| 项目 | 参数 |
|------|------|
| 输入电压 | 415V AC / 3P + N + PE |
| 频率 | 50/60Hz |
| UPS | EATON 9395XR-1500（10 UPM，1500kW），内置于 DC45 |
| UPS 电池 | 3× EATON 93LiG2，内置于 DC45，约 8 分钟后备（**UPS 电池**，与 BESS 电池完全不同）|
| BESS（推荐）| Grid → BESS → DC45 |
| 母线 | SIEMENS 2500A 封闭式母线 |
| 分支方式 | Tap-off 插接，每机柜 250A |

### 5.1 配电路径

Grid / BESS → PDC → UPS（9395XR-1500）→ PDC → Busbar（2500A）
    → Tap-off Unit（TOU，含 MCCB）→ DLC Racks → PDU → Server PSU

详细电力分配和热力分析参见：https://dc45-cooling-calc.pages.dev/

---

## 6. 液冷系统架构

Hybrid Cooling System
        ↓
Primary CDU（1.2MW）← DC45 内置
        ↓
Rack CDU（150kW）← 可选，每柜一台
        ↓
GPU Server（冷板）

---

## 7. FCU 散热架构

| 项目 | 参数 |
|------|------|
| FCU 模组数量 | **12 台**（根据环境温度动态调整）|
| 单台能力 | 40kW |
| 总能力 | **480kW** |
| 工作模式 | 低温区（<28°C）：部分 FCU 运行；高温区（≥28°C）：全载运行 |
| 出风温度 | 18–25°C（压缩机可加热/制冷）|
| 排风方式 | 负压排风（百叶窗 + EC 风机）|
| 总风量 | 60,000–80,000 CMH |
| 压差控制 | ΔP 5–15Pa（机柜前微正压，后侧负压）|

> **注：** FCU 数量根据环境温度动态调整。低温环境可减少运行数量以节省能耗；高温环境需全载运行。详细电力分配和热力分析参见冷却计算工具：https://dc45-cooling-calc.pages.dev/

---

## 7.1 原厂 OEM 机柜适配

DC45 支持**不预装 DLC 机柜**，客户可后续自行安装原厂 OEM 机柜。

| 项目 | 参数 |
|------|------|
| 最大机柜宽度 | 800mm |
| 最大机柜深度 | 1200mm |
| 最大机柜高度 | 2300mm |
| 兼容品牌 | SMCI（超微）、HPE（慧与）、DELL（戴尔）、Lenovo（联想）等标准 19 英寸机柜 |
| 适配方式 | 预留液冷歧管（Manifold）接口和配电接口，支持后装 |

> **注意：** 原厂 OEM 机柜需自行确认与 DC45 液冷管路的兼容性。

---

## 8. 冷却 Zone 配置

| 项目 | 配置 |
|------|------|
| 散热方式 | **Hybrid Cooling System**（必须）|
| 主 CDU | 1.2MW Rack CDU |
| 环境 >28°C | DX 强制启动 |
| 禁止 | 纯干冷器 |

参考：[[FOG/KB/Guideline/COOLING_SYSTEM_Guideline|KB/Guideline/COOLING_SYSTEM_Guideline]]

---

## 9. 冗余说明

| 层级 | 冗余描述 |
|------|---------|
| **UPS 模块** | 9395XR-1500 内置 10 个功率模块，内部 N+1（单模块故障不影响运行）|
| **CDU** | 主 CDU + 可选 In-Rack CDU（可选 1+1 配置）|
| **FCU** | 12 台中根据环境温度调整运行数量（部分 FCU 故障不影响整体）|
| **IT Zone（DC45）** | **无内部冗余** — 单台 DC45 独立运行 |
| **MDC 系统级** | 多台 DC45 并联 → 系统级冗余（由集装箱数量决定）|
| **Power Zone** | 可选 N+1/2N | 需要额外 Switchgear |

---

## 10. PUE 参考

| 环境条件 | 运行模式 | PUE 参考值 |
|----------|---------|-----------|
| 环境 <28°C | Hybrid Cooling（干冷优先）| ~1.07–1.15 |
| 环境 28–35°C | Hybrid Cooling（DX介入）+ FCU | ~1.15–1.25 |
| 环境 >35°C | Hybrid Cooling（DX主导）+ FCU | ~1.25–1.35 |

---

## 11. 标准输出格式（团队引用模板）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reference Architecture — 1.2MW DLC AI Inference Unit
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

IT Load:       1240kW（1×DC45）
Total Load:    ~1325–1675kW（PUE≈1.07–1.35）
Product:       DC45（DLC Container，45ft）
Cooling:       DLC + Hybrid Cooling System + FCU（12×40kW 动态调整）
Power:         Grid + UPS（9395XR-1500）+ BESS（可选）
OEM Rack:      支持 SMCI/HPE/DELL/Lenovo（宽800×深1200×高2300mm）
Redundancy:    UPS 模块 N+1 / FCU 动态配置（**IT Zone 本身无内部冗余**）
Delivery:      **~185–230 天**（参考值：现场勘测 15d + 商务准备 15d + 生产制造 90–120d + 运输 45–60d + 部署安装 10–20d）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

---

## 12. 参考文档

- DC45 完整规格：[[PRODUCTS_DC45|KB/PRODUCTS_DC45]]
- MDC 组合标准：[[PRODUCTS_MDC|KB/PRODUCTS_MDC]]
- 冷却方案：[[FOG/KB/Guideline/COOLING_SYSTEM_Guideline|KB/Guideline/COOLING_SYSTEM_Guideline]]
- UPS 规格：[[UPS_EATON_9395XR|KB/3RD-PARTY/UPS/UPS_EATON_9395XR]]
- 冷却计算工具：https://dc45-cooling-calc.pages.dev/

---

*Document Version: v1.2 | Last Updated: 2026-05-09*
