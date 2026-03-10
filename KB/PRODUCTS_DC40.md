# DC40 – PowerPod with Direct Liquid Cooling
**适用对象：ACC（Advanced Computing Cluster）标准计算单元 IT Zone**  
**版本：V1.0**


## 1. 产品定位

DC40 是 40ft 容器，
支持 4 × 120kW DLC racks，
适用于高性能AI算力部署。

可两个DC40合并成一个Utility提供8*DLC Rack的方案，符合NVIDIA SU Best Practice

---

## 2. 核心参数

| 项目 | 参数 |
|------|------|
| IT Capacity | 480kW |
| Rack Count | 4 |
| Cooling | DLC |
| Inlet Temp | 24°C |
| Operation Load | 60kW |
| PUE | ~1.2 |

---

## 3. 冷却要求

必须配置：

- Dry cooler + DX
- 或 Heat Pump

不允许纯干冷器。

---

## 4. 电力路径

Input → PDC → DLC racks

---

## 5. 风险点

- 冷却温度敏感
- 管路泄漏风险
- 泵冗余必须N+1

---

## 6. 禁止场景

- 无DX能力场地
- 极高湿度环境

---

## 7. 扩展逻辑

可与AC40混合构建MDC。