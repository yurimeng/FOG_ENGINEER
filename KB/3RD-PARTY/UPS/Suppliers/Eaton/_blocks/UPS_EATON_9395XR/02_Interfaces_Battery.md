---
title: "02_Interfaces_Battery — §3 §4"
parent: "[[../../../UPS_EATON_9395XR]]"
order: 2
tags:
  - "#workspace/engineer"
  - "#type/ups-prd"
  - "#product/UPS"
  - "#power"
  - #MDC
created: 2026-06-18
source_file: "KB/3RD-PARTY/UPS/Suppliers/Eaton/UPS_EATON_9395XR.md"
source_anchors:
  - "§3"
  - "§4"
---

# §3. 外观接口说明

### 前面板接口

| 接口名称 | 功能说明 |
|---------|----------|
| Mini-slot 1/2/3 | 扩展槽位，用于安装额外功能模块 |
| USB Host | 连接配件用 USB 接口 |
| USB Device | 连接计算机用 USB 接口 |
| RS-232 端口 | 服务调试接口 |
| EPO（Emergency Power Off）| 紧急关机按钮 |
| Relay output | 继电器输出 |

### 后面板接口

| 接口名称 | 功能说明 |
|---------|----------|
| External parallel connector | 外部并机接口 |
| External battery breaker trip | 外部电池断路器跳闸 |
| BMS RS-485 | 电池管理系统通信接口 |
| SYNC Terminal | 同步端子 |
| Rectifier Input | 整流器输入 |

详细接口图参考：
- [[9395XR-1500-Rear-Exhaust-Connections|EATON 9395XR 接口定义]]
- [[9395XR-1500-Wiring-Diagram|EATON 9395XR 接线图]]

---

# §4. UPS 电池后备时间

UPS 电池型号：**EATON 93LiG2**（93Li92S-100Ah-3PBFA，332kW/柜）

| 产品 | UPS 电池配置 | IT 负载 | 后备时间 |
|------|-------------|---------|---------|
| AC40 | 2×93LiG2（外置，客户自备）| 400kW | ~10 分钟 ^mdc-4082c497c4 |
| AC45 | 2×93LiG2（内置）| 400kW | ~20 分钟 ^mdc-60187e2e7e |
| DC45 | 3×93LiG2（内置）| 1240kW | ~8 分钟 ^mdc-348ba3dac1 |

> ⚠️ **UPS 电池 vs BESS 电池：** 上表中"UPS电池"指 UPS 配套的 93LiG2 磷酸铁锂电池柜（分钟级瞬时切换后备）。BESS（如 Tesla Megapack / 国轩）是独立大型储能系统（小时级供电），两者完全不同。

电池系统详细参考：[[93Li-G2-Battery-Brochure|93Li G2 锂电池系统手册]]
