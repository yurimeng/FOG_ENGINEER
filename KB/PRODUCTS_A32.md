# A32 – Scalable Immersion Grid

## 1. 产品定位

A32 是 32RU OU-compatible immersion cooling tank，
单柜 IT 负载 45kW，最大50KW
采用 2N CDU 冗余设计，
面向边缘计算与高密度 GPU 部署。

---

## 2. 核心参数

| 项目           | 参数                      |
| ------------ | ----------------------- |
| IT Capacity  | 45kW，最大50KW             |
| Rack Units   | 32RU                    |
| Cooling Type | Single-phase Immersion  |
| CDU          | 2 × 45kW (2N redundant) |
| Inlet Temp   | 32–35°C                 |
| Outlet Temp  | 35–38°C                 |
| PUE          | ~1.04                   |
| Compatible   | OU,29OU (OCP)           |

---

## 3. 电力路径

INPUT → PDC → UPS (Optional) → A32 Tank → IT Servers

说明：
- A32 本体不包含UPS
- 支持外部PDC接入
- 可对接BESS或发电机系统

---

## 4. 热力路径

IT Load → Dielectric Fluid → Heat Exchanger → CDU → Dry Cooler / DX

设计逻辑：

- 若环境 <28°C：可纯干冷器
- 若环境 >28°C：必须增加DX或Heat Pump

---

## 5. 故障模式分析

| 故障 | 影响 | 风险等级 |
|------|------|----------|
| 单CDU故障 | 无影响（2N） | 低 |
| 双CDU故障 | 停机 | 高 |
| Dry cooler 失效 | 温度升高 | 高 |
| Pump 失效 | 过热 | 高 |

---

## 6. 适用场景

- 高密度GPU训练
- Edge deployment
- 干燥气候区域
- 电价高区域（低PUE优势）

---

## 7. 禁止场景

- 高湿无通风环境
- 无外部冷源场地
- 客户强制要求空气冷却

---

## 8. 扩展逻辑

多个A32可组成AC40模块。
单A32可独立部署。