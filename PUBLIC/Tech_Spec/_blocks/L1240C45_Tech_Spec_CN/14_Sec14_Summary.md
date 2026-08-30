---
title: "L1240C45 第十四节：主要参数汇总"
parent: "[[L1240C45_Tech_Spec_CN]]"
order: 14
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/l1240c45"
  - "#thermal"
  - "#MDC"
created: 2026-06-18
source_file: "PUBLIC/Tech_Spec/L1240C45_Tech_Spec_CN.md"
source_anchors:
  - "^sec-14-summary"
---

## 14. L1240C45 主要参数汇总 ^sec-14-summary

| 项目                | 参数                                    |
| ----------------- | ------------------------------------- |
| 集装箱规格             | 45ft 高箱（13,716mm × 2,438mm × 2,992mm） |
| IT 容量             | 1240kW（8 × 150kW DLC + 1 × 40kW 风冷）   |
| 冷却方式              | DLC（冷板式液冷）+ RDHX + 顶置 CeilAir，三支路 TCS PG25 并联 |
| 机柜数量              | 9（8 DLC + 1 风冷）                       |
| UPS 型号            | EATON 9395XR-1500（1500kW）             |
| UPS 电池后备          | ~8分钟（3×93LiG2）                        |
| Busbar            | SIEMENS 2500A                         |
| **CDU**           | **换热 ≥ 1500 kW / 二次侧 ≥ 175 m³/h / ≥ 220 kPa，VFD，2N 或 N+1** |
| **RDHX**          | **9 × VERTIV CoolLoop DCD35（被动型，DN25）** |
| **CeilAir**       | **9 × STULZ OHS-084-DG-FC（自含式 DX + FC，EG/PG 兼容）** |
| **TCS 循环液**       | **PG25（25% 丙二醇水溶液）** |
| **TCS 进水温度**      | **26–28°C** |
| **TCS 总循环流量**     | **≈ 148–154 m³/h** |
| **室外侧散热基线**       | **≥ 1700 kW**（混合干冷器 + DX 板换） |
| 机柜前进风温度           | 25–27°C（CeilAir DX 解耦）|
| PDU 输入            | 60A 415V                              |
| PDU 输出            | **24位 C19，液磁空开**                          |
| 空箱重量              | 约 16T                                 |
| 运行温度              | -45°C 至 +45°C                         |
| 运行湿度              | 参考标准数据中心                              |
| 灭火剂               | FM-200                                |
| 探测系统              | ASSD / VESDA                          |
| 门禁                | 支持刷卡/人脸识别                             |
| 监控                | PLC MODBUS / SNMP / Web               |
| 认证                | 器件通过 UL 认证，整机需 TUV 现场认证                 |
| 质保期               | 核心部件自 EXW 起 1 年；后续年份按年收取服务费。响应级别（ONSITE / NBD / 9×5 / 24×7）以 Invoice 为准 |
| 交期                | 首批 120 天 EXW；Scale 90 天 EXW；假负载运行期 5–30 天（不含在 EXW 承诺内） |
| PUE                 | `1.0x` —— 逐站点用 <https://mdcx.org> 计算 |

---
