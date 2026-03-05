# AC40 – All-In-One PowerPod (Immersion)
**适用对象：ACC（Advanced Computing Cluster）标准计算单元 IT Zone**  
**版本：V1.0**

## 1. 产品定位

AC40 是 40ft 集装箱模块，
包含 8 × A32，
集成 PDC、消防系统、辅助空调。

面向 360-400kW 级边缘数据中心。

---

## 2. 核心参数

| 项目 | 参数 |
|------|------|
| IT Capacity | 360kW 最大400KW|
| A32 Tanks | 8 Units |
| Operation Load | 40kW |
| Cooling | Immersion + Dry Cooler |
| PUE | ~1.04 |
| Container | 40ft |

---

## 3. 电力路径

Input → PDC → UPS → A32 Tanks
已内置UPS


---

## 4. 热力路径

A32 → Dry Cooler / DX

判断逻辑：

if ambient_99% < 28°C:
    Dry cooler sufficient
else:
    DX required

---

## 5. 结构布局原则

- 中央冷却管道
- 两侧A32排列
- 通道宽度 >900mm
- 消防喷淋覆盖全部IT区域

---

## 6. 故障模式

| 故障 | 影响 |
|------|------|
| 单A32失效 | 局部损失 |
| Dry cooler失效 | 全局温升 |
| PDC故障 | 全局断电 |

---

## 7. 适用场景

- 快速部署
- 无传统机房场地
- 电力基础设施完善区域

---

## 8. 扩展逻辑

多个AC40组成MDC。


## TECH SPEC
Items,Specification
Container,"- 40ft ISO HC container: 12,192mm (L) × 2,438mm (W) × 2,896mm (H)
- External cooling units can be stacked or placed alongside"
IT Load Capacity,"- Total IT load: 500kW (standard), with customized versions supporting up to 1MW"
Server Capacity,"- 4 liquid-cooled server cabinets: 42U, 19-inch, 600mm(W)×1,400mm(D)×2,000mm(H), 120kW/rack, supporting servers up to 1,000mm depth
- 1 air-cooled network cabinet: 42U, 600mm(W)×1,400mm(D)×2,000mm(H), 20kW/rack"
Cooling Capacity,"- Primary: 500kW (standard), with customized versions exceeding 1MW
- Secondary: CDU,120kW/pcs, rack-mounted,24°C/44°C"
Power Input,- 3-phase 380V/415V/480V AC 50/60Hz
Redundancy,"- Cooling: 2N redundancy
- Power supply: 2N redundancy"
Ambient Environment,"- Designed for dry-bulb temperature ≤35°C
- External cooling configurations adjustable for project-specific conditions, chiller, dry cooler+DX"