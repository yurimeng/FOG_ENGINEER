# EATON 9395XR-1500 UPS 产品知识文档

## 产品概述

**型号**: 9395XR-1500  
**类型**: 不间断电源 (UPS)  
**品牌**: EATON  
**功率**: 1500kVA 

---

## 外观接口说明

### 前面板 / 后面板接口

| 接口位置 | 接口名称 | 功能说明 |
|---------|---------|----------|
| 前面板 | Mini-slot 1/2/3 | 扩展槽位，用于安装额外功能模块 |
| 前面板 | USB Host | 连接配件用USB接口 |
| 前面板 | USB Device | 连接计算机用USB接口 |
| 前面板 | RS-232 端口 | 服务调试接口 |
| 前面板 | EPO (Emergency Power Off) | 紧急关机按钮 |
| 前面板 | Relay output | 继电器输出 |

---

## 电气接口

### 输入接口

| 接口类型 | 说明 |
|---------|------|
| **整流器输入 (Rectifier Input)** | L1 / L2 / L3 - 三相电源输入 |
| **旁路输入 (Bypass Input)** | L1 / L2 / L3 - 三相旁路电源 |

### 输出接口

| 接口类型 | 说明 |
|---------|------|
| **输出 (Output)** | L1 / L2 / L3 - 三相电源输出 |
| **电池 (Battery)** | Battery+ / Battery- / N - 直流电池接入 |

---

## 通信接口

- **BMS RS-485** - 电池管理系统通信
- **外部电池断开 (External battery breaker trip)** - 电池断开保护
- **外部并联接口 (External parallel connector)** - 并机使用

---

## 系统架构图

```
                    ┌─────────────────┐
                    │   整流器输入    │
                    │  L1 / L2 / L3  │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │     整流器      │
                    │   (Rectifier)   │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │     电池        │
                    │ Battery+ / N   │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │     逆变器      │
                    │   (Inverter)   │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │     输出       │
                    │  L1 / L2 / L3  │
                    └─────────────────┘

        ┌────────────────────────────────┐
        │          旁路 (Bypass)           │
        │       L1 / L2 / L3              │
        └────────────────────────────────┘
```

---
## UPS 电池柜

名称： 93LiG2 Lithium Battery System
型号：12-Module/Rack ｜ 93Li92S-100Ah-3PBFA
参数：
- Voltage：307.2
- Rate Energy kwh：63.897
- Change voltage V：331.2
- Charging current: 0.25c
- Dischage voltage V: 268.8
- Max Dischage Power: 322.56
- Dimensions: 600,900,2000
- Weight Kg：970



产品连接： https://www.eaton.com/content/dam/eaton/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/eaton-93li-lithium-battery/eaton-93li-g2-lithium-battery-system-brochure-en-anz.pdf



---

## 关键特性

1. **三相输入/输出** - 支持三相电系统
2. **电池管理** - 支持BMS RS-485监控
3. **并机支持** - 外部并联接口支持多机冗余
4. **紧急关机** - EPO快速切断
5. **扩展槽位** - Mini-slot可安装网络/干接点等模块

---

## 文件信息

- **文档版本**: 1.0
- **创建日期**: 2026-03-04
- **来源文件**: 
  - 9395XR-1500 Wiring Diagram
  - 前面板/后面板接口图
