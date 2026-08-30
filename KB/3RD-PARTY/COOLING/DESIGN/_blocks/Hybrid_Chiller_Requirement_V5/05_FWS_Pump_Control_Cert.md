---
title: "Hybrid Chiller V5 — FWS 主泵 + 一次侧管路 + 控制/通信/认证"
parent: "[[Hybrid Chiller Requirement V5]]"
order: 5
tags:
  - #workspace/engineer
  - #type/design-spec
  - #product/Hybrid-Chiller
  - #cooling
  - #MDC
created: 2026-06-17
source_file: "KB/3RD-PARTY/COOLING/DESIGN/Hybrid Chiller Requirement V5.md"
source_anchors:
  - "^chiller-10-fws-pump"
---

## 6. 冷冻水泵（FWS 主泵 — Chiller 集成） ^chiller-10-fws-pump

> **归属决策（[[../../LIQUID/L1240C45/DESIGN/L1240C45 Hydronic & Thermal Design Criteria]] Rev.C §9.2 锁定）**：FWS 主泵由 Chiller 集成提供，CDU 不自带一次泵。

| 参数 | 锁定值 |
|---|---|
| 冗余 | **2N 推荐**（双泵并联 50% 各，单泵故障自动切至 100%；定期轮换）|
| 类型 | 卧式离心 / 管道泵，VFD 压差恒定控制 |
| **单泵流量** | ≥ 80 m³/h（2N 合计 ≥ 160 m³/h）|
| **扬程** | **≥ 25 mH₂O ≈ 245 kPa**（含 FWS 主管 + Chiller 蒸发器 + CDU 板换一次侧 + 现场管路）|
| 防护 | IP55 |
| 品牌 | Grundfos / Wilo / Armstrong |
| 介质适配 | 泵壳 / 叶轮 / 机械密封按站点 EG 25–60% 适配；−54 ~ +50°C；Astana 须 60% EG 长期可靠性测试 |
| 附件 | 每台独立隔离阀 / 止回阀 / 软接头 / 压力表；泵组共用 Y 型过滤 DN100，精度 ≤ 0.5 mm |

### 6.1 一次侧管路联动要求（V5 主文件 §6 / [[CDU_Requirement V5]] §6 同步）

> **设计前提声明**：Chiller FWS 出水 22°C ±0.5°C 控制精度不应被一次侧管路温度漂移污染。供应商须知悉以下保温要求并在技术资料中显式声明本前提（管路保温由 BOM 集成商负责，不在 Chiller 供货范围）：

- 100m FWS 管路 = DN200 主干 95m（户外）+ DN100 CDU 接入 5m（IT zone 内）
- 保温 ≥ 50 mm 岩棉（k ≤ 0.040）或 ≥ 30 mm PIR/PUR（k ≤ 0.022 等效）
- 户外护壳 + UAE/Thailand 防潮层 + Kemi/Astana 可选电伴热 ≤ 10 W/m
- 热胀冷缩补偿（每 25–30m 波纹补偿器或 U 型弯）
- 红外热成像验收（表面 vs 环境温差 ≤ 3K）

> **联动结论**：Chiller 出水 22°C ±0.5°C + V5 §6 保温 → CDU 进水实际漂移 ≤ 0.1 K（远小于 ±0.5°C 控制带）。若不做保温，30% 负载下 Astana 极寒 CDU 进水漂移可达 −3.8 K，吃光 4°C approach 全部预算。

---

## 7. 控制系统 / 通信 / 认证

| 项 | 锁定 |
|---|---|
| 本地控制器 | 内置 PLC + ≥7" 彩色触摸屏，中英文切换；手动 / 自动 / 远程；本地数据 ≥ 30 天 + USB 导出 |
| 远程通信 | Modbus RTU + RS485（必），Modbus TCP（选配）|
| 干接点告警 | ≥ 4 路（压缩机故障 / 高压 / 低压 / 传感器异常）|
| 接口 | DN100 冷水供回（PN ≥ 10 bar）；DN25 补水/排水；DN20 湿膜补水；制冷剂施拉德阀（按所选制冷剂匹配）|
| 控制逻辑 | 供水温度 PID 闭环（响应 ≤ 60s）；按环境温度自动分级投切压缩机（迟滞 ±2°C）|
| **认证（强制）** | **CE**（2006/42/EC + 2014/35/EU + 2014/30/EU + PED 2014/68/EU 欧洲）+ **UL 1995 等效**（北美）+ EN 378 / ASHRAE 15 制冷剂泄漏 |
