# AC40 – All-In-One PowerPod (Immersion)
**适用对象：MDC（Modular Datacenter Cluster）标准计算单元 IT Zone**  
**版本：V1.0**

## 1. 产品定位

AC40 是 40ft 容器，
支持 8 × 50kW Immersion Tank [[PRODUCTS_A32]] 
适用于高性能AI算力部署。


---

## 2. 核心参数

| 项目                  | 参数                                                |
| ------------------- | ------------------------------------------------- |
| IT Capacity         | 400kW                                             |
| Immersion Tank      | 50kW                                              |
| Tank  Qty           | 8                                                 |
| Air Cooled Rack     | 10kW                                              |
| Air Cooled Rack Qty | 1                                                 |
| Inlet               | 32°C                                              |
| Operation Load      | ～8kW                                              |
| UPS                 | EATON 9395 XR 500 **4个UPM，功率600kw**， 发热量7.9kW |
| Battery             | 2个93i机柜，332kW/个，共提供10min备用电                        |


---

## 3. 机柜详情
- 32RU/29RU
- 内阻Dual CDU，1+1 完全冗余

## 4. 冷却

###  Immersion冷却部分

- Dry cooler + DX
- 或 Heat Pump

不允许纯干冷器。

### 风冷部分
- 必须配置独立空调

---

## 4. 电力路径

Input → PDC → UPS → PDC → Tanks → PDU

---

## 5. 水路冗余

- 各TANK内置CDU，不再需要独立CDU
- 2N 系统

---

## 6. 布局

- 双排靠集装箱墙壁摆放，中间预留运维通道
- 机柜底部350～400管路，配电区域无地板架高

---

## 7. 扩展逻辑

可与DC45混合构建MDC。