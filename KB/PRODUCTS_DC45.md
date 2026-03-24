# DC45 – PowerPod with Direct Liquid Cooling
**适用对象：ACC（Advanced Computing Cluster）标准计算单元 IT Zone**  
**版本：V1.0**


## 1. 产品定位

DC45 是 45ft 容器，
支持 8 × 150kW DLC racks，
适用于高性能AI算力部署。


---

## 2. 核心参数

| 项目             | 参数                                                |
| -------------- | ------------------------------------------------- |
| IT Capacity    | 1200kW                                            |
| Rack Count     | 8                                                 |
| Cooling        | DLC                                               |
| Inlet Temp     | 24°C                                              |
| Operation Load | 240kW                                             |
| PUE            | ~1.15                                             |
| UPS            | EATON 9395 XR 1500 **10个UPM，功率1200kw**， 发热量46.9kW |
| Battery        | 4个93i机柜，300kW/个，共提供9min备用电                        |
| Major CDU      | 1.2 MW Rack CDU                                   |
| Backup CDU     | 150KW in-Rack CDU （optional）                      |

---

## 3. 机柜详情
- 42/47 U
- 侧置Manifold
- 后置PDU

## 4. 冷却

### DLC冷却部分

- Dry cooler + DX
- 或 Heat Pump

不允许纯干冷器。

### 风冷部分
- 必须配置风墙模块。
- 3个风墙模组，2+1 工作方式。单个功率70kW
- 风墙模组带压缩机，可加热和制冷，确保温度控制在18-25摄氏度

---

## 4. 电力路径

Input → PDC → UPS → PDC → Busbar → Tap-off Unit (TOU with MCCB) → DLC racks → PDU

---

## 5. 水路冗余

- DC45包含1个1.2MW CDU
- 可在机柜内选配150KW的inRack CDU
- 2N 系统

---

## 6. 布局

- 机柜采用深度1200，宽度720
- 机柜后门离集装箱墙600-800
- 前门保留足够空间运维

---

## 7. 扩展逻辑

可与AC40混合构建MDC。