---
tags:
  - #workspace/engineer
  - #type/reference
  - #product/dc45
---

# Reference Architecture — 1.2MW DLC AI Inference Unit
1.2MW 直冷液冷 AI 推理算力单元标准参考架构

Reference Architecture Version: v1.1
Last Updated: 2026-03-29

---

## 1. 架构概述

本参考架构为基于直冷液冷（DLC）的 AI 推理算力单元，适用于中大型边缘推理集群。

| 项目 | 内容 |
|------|------|
| IT 容量 | **1.2MW（1200kW）** |
| 产品形态 | 1× DC45 集装箱 |
| 冷却技术 | Direct Liquid Cooling（直冷液冷 DLC）|
| 散热方式 | **Hybrid Cooling System**（干冷器+DX一体化）+ 风墙 |
| 交付周期 | 约 195–305 天（含制造、海运、部署）|

---

## 2. IT负载 vs 整体电力负荷

| 项目 | 数值 | 说明 |
|------|------|------|
| **IT 负载** | 1200kW | 服务器、GPU 实际消耗 |
| **整体电力负荷** | ~1380–1560kW | 取决于 PUE（PUE 约 1.15–1.30）|
| PUE | **取决于环境温度** | 低温区 ~1.12–1.15；高温区 ~1.25–1.35 |

---

## 3. 计算架构

| 项目 | 参数 |
|------|------|
| 服务器类型 | GPU 服务器（如 NVIDIA B300 等 DLC 兼容服务器）|
| PSU 类型 | 单相 200–240V |
| 冷却方式 | 冷板式直冷液冷（Cold Plate DLC）|
| 服务器进口温度 | 24°C |
| 负载特性 | 高动态（AI 负载）|

---

## 4. 产品配置

本方案使用 **1× DC45**：

| 项目 | DC45 参数 |
|------|-----------|
| IT 容量 | 1200kW（8×150kW DLC Racks）|
| 风冷辅助 | 10kW × 1 |
| UPS | EATON 9395XR-1500（10 UPM × 150kW）|
| 电池 | 3× EATON 93LiG2（8 分钟后备）|
| 主 CDU | 1.2MW Rack CDU × 1 |
| 备用 CDU | 150kW In-Rack CDU（可选）|
| 风墙 | 3×70kW（2+1 工作方式），18–25°C |
| 冷却 | 干冷器 + DX（每台 DC45 独立配置）|
| Busbar | SIEMENS 1600A |

---

## 5. 电力架构

| 项目 | 参数 |
|------|------|
| 输入电压 | 415V AC / 3P + N + PE |
| 频率 | 50/60Hz |
| UPS | EATON 9395XR-1500（10 UPM，1500kW），内置于 DC45 |
| 电池后备 | 3× EATON 93LiG2，约 8 分钟 |
| BESS（推荐）| Grid → BESS → DC45 |
| 母线 | SIEMENS 1600A 封闭式母线 |
| 分支方式 | Tap-off 插接，每机柜 250A |

### 5.1 配电路径

```
Grid / BESS → PDC → UPS（9395XR-1500）→ PDC → Busbar（1600A）
    → Tap-off Unit（TOU，含 MCCB）→ DLC Racks → PDU → Server PSU
```

---

## 6. 液冷系统架构

```
Hybrid Cooling System
        ↓
Primary CDU（1.2MW）← DC45 内置
        ↓
Rack CDU（150kW）← 可选，每柜一台
        ↓
GPU Server（冷板）
```

---

## 7. 风墙冷却架构

| 项目 | 参数 |
|------|------|
| 风墙模组数量 | 3 台（2+1 工作方式）|
| 单台能力 | 70kW |
| 总能力 | 210kW |
| 出风温度 | 18–25°C（压缩机可加热/制冷）|
| 排风方式 | 负压排风（百叶窗 + EC 风机）|
| 总风量 | 60,000–80,000 CMH |
| 压差控制 | ΔP 5–15Pa（机柜前微正压，后侧负压）|

---

## 8. 冷却 Zone 配置

| 项目 | 配置 |
|------|------|
| 散热方式 | **Hybrid Cooling System**（必须）|
| 主 CDU | 1.2MW Rack CDU |
| 环境 >28°C | DX 强制启动 |
| 禁止 | 纯干冷器 |

参考：[[COOLING_SYSTEM_SOLUTION|KB/COOLING_SYSTEM_SOLUTION]]

---

## 9. 冗余说明

| 层级 | 冗余描述 |
|------|---------|
| **UPS 模块** | 9395XR-1500 内置 10 个功率模块，内部 N+1（单模块故障不影响运行）|
| **CDU** | 主 CDU + 可选 In-Rack CDU（可选 1+1 配置）|
| **风墙** | 3 台中 2+1 工作（单台风墙故障不影响运行）|
| **IT Zone（DC45）** | **无内部冗余** — 单台 DC45 独立运行 |
| **MDC 系统级** | 多台 DC45 并联 → 系统级冗余（由集装箱数量决定）|
| **Power Zone** | 可选 N+1/2N | 需要额外 Switchgear |

---

## 10. PUE 参考

| 环境条件 | 运行模式 | PUE 参考值 |
|----------|---------|-----------|
| 环境 <28°C | Hybrid Cooling（干冷优先）| ~1.12–1.15 |
| 环境 28–35°C | Hybrid Cooling（DX介入）+ 风墙 | ~1.20–1.28 |
| 环境 >35°C | Hybrid Cooling（DX主导）+ 风墙 | ~1.28–1.35 |

---

## 11. 标准输出格式（团队引用模板）

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reference Architecture — 1.2MW DLC AI Inference Unit
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

IT Load:       1200kW（1×DC45）
Total Load:    ~1380–1560kW（PUE≈1.15–1.30）
Product:       DC45（DLC Container，45ft）
Cooling:       DLC + Hybrid Cooling System + Air Wall
Power:         Grid + UPS（9395XR-1500）+ BESS（可选）
Redundancy:    UPS 模块 N+1 / 风墙 2+1（**IT Zone 本身无内部冗余**）
Delivery:      约 195–305 天（制造90-180d + 海运45-50d + 部署30-45d）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 12. 参考文档

- DC45 完整规格：[[PRODUCTS_DC45|KB/PRODUCTS_DC45]]
- MDC 组合标准：[[PRODUCTS_MDC|KB/PRODUCTS_MDC]]
- 冷却方案：[[COOLING_SYSTEM_SOLUTION|KB/COOLING_SYSTEM_SOLUTION]]
- UPS 规格：[[KB/AI Agent/Workspace-Engineer/KB/3RD-PARTY/Buildin/UPS_EATON_9395XR|KB/UPS_EATON_9395XR]]
