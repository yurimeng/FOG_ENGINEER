---
title: 交付周期 + 扩展逻辑 + UPS 型号说明
parent: "[[../AC40]]"
order: 4
tags:
  - #workspace/engineer
  - #type/product
  - #product/ac40
  - #power
  - #MDC
created: 2026-06-18
source_file: "PUBLIC/Products/AC40.md"
source_anchors: []
---

## 8. 交付周期

| 阶段 | 周期 | 说明 |
|------|------|------|
| 现场勘测 Site Survey | 15 天 | 现场条件评估 |
| 商务准备 Business Prep | 15 天 | 合同签署、付款、采购 |
| 生产制造 Manufacturing | 90–120 天 | 集装箱制造 + 设备集成 |
| 运输 Logistics | 45–60 天 | 海运 + 清关 |
| 部署安装 Deployment | 10–20 天 | 现场安装 + 调试 |
| **参考总周期** | **~185–230 天** | 合同签署后起算 |

---

## 9. 扩展逻辑

| 方向 | 说明 |
|------|------|
| MDC 混合 | 可与 DC45 混合构建 MDC |
| 横向扩展 | 增加 AC40 数量 |
| 纵向扩展 | 增加单柜 GPU 密度（需重新评估冷却）|

---

## 10. UPS 型号说明

| 产品       | UPS 型号            | 模块数    | 每模块   | 总 UPS 功率 | 发热量     | UPS 放置          | UPS 电池后备时间            |
| -------- | ----------------- | ------ | ----- | -------- | ------- | --------------- | --------------------- |
| **AC40** | EATON 9395XR-600  | 4 UPM  | 150kW | 600kW    | ~7.9kW  | **外置（客户自备）**    | ~10 分钟（客户自备 2×93LiG2） |
| **AC45** | EATON 9395XR-600  | 4 UPM  | 150kW | 600kW    | ~7.9kW  | 内置（专用电力舱），UL 合规 | ~20 分钟（内置 2×93LiG2）   |
| **DC45** | EATON 9395XR-1500 | 10 UPM | 150kW | 1500kW   | ~46.9kW | 内置，UL 合规        | ~8 分钟（内置 3×93LiG2）    |

> ⚠️ **UPS 电池 vs BESS 电池：** 上表中的"UPS 电池后备"指 UPS 配套的 93LiG2 电池柜（EATON 磷酸铁锂），用于提供分钟级瞬时切换后备。BESS（如 Tesla Megapack / 国轩）是独立的大型储能系统，提供小时级供电，两者完全不同。

电池型号均为 **EATON 93LiG2**（93Li92S-100Ah-3PBFA，332kW/柜）。
参考：[[UPS_EATON_9395XR|KB/UPS_EATON_9395XR]]
