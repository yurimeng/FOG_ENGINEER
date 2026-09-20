---
title: 产品定位 + 核心参数 + IT 负荷
parent: "[[../I50TS]]"
order: 1
tags:
  - #workspace/engineer
  - #type/product
  - #product/i50ts
  - #MDC
created: 2026-06-18
source_file: "PUBLIC/Products/I50TS.md"
source_anchors: []
---

## 1. 产品定位

A32 是 32RU OU-compatible 浸没式液冷单机柜，单柜 IT 负载推荐 45kW / 最大 50kW，采用 2N CDU 冗余设计，面向边缘计算与高密度 GPU 部署。 ^mdc-2e746659e4

可单独部署，也可 8 台组合成 AC40 集装箱。 ^mdc-d61d7d4ec8

---

## 2. 核心参数

| 项目 | 参数 |
|------|------|
| IT 容量 | **推荐 45kW / 最大 50kW**（2N 散热冗余） |
| Rack Units | 32RU / 29OU（OCP 兼容） |
| 冷却类型 | 单相浸没式液冷 |
| CDU 配置 | 2 × 50kW（**2N 冗余**），各 Tank 内置 |
| 二次侧进/出油温 | **进油 ≤35°C / 出油 ≈43°C，ΔT=8K**（标品运行工况；详见 [[PUBLIC/Products/I50TS#5.4 二次侧散热校核|§5.4 散热校核]]，待流速验证） ^mdc-66750b4aa4 |
| 一次侧进/出水温 | ≤32 / 37°C（ΔT=5K）|
| 设计环境湿球温度 | 28°C |
| 冷却液 | **Castrol DC20** 或 **Shell S5LV**（S5LV 比热容 2.306 kJ/kg·℃）|
| PUE | **`1.0x`（逐站点用 <https://mdcx.org> 计算）** —— 不给固定值、不给区间（2026-08-30 裁定） |

> ⚠️ 散热量为推荐工况 45kW、极限工况 50kW。最大散热能力与设定温度取决于外制冷的流量与浸没进液温度（受服务器耐受度限制）。

### 服务器兼容性

| 项目 | 参数 |
|------|------|
| 机架标准 | 兼容 EIA 19″ / 21″ / OCP（Open Rack V3）|
| 最大服务器深度 | 1000mm |
| 容量 | 32RU / 29OU |
| 服务器类型 | 以 GPU 服务器为主 |
| 兼容芯片 | 4090 / A100 / H100 |
| 浸没方式 | 支持风冷服务器改造浸没，及 Immersion-ready 服务器浸没 |

---

## 3. IT负载 vs 整体电力负荷

| 项目 | 数值 | 说明 |
|------|------|------|
| **IT 负载** | 45–50kW | 服务器、GPU 实际消耗 |
| **整体电力负荷** | ~46–56kW | 取决于 PUE（PUE 约 1.03–1.12） |


> ✅ **2026-08-30 Yuri 裁定已传导。** 交期只承诺 EXW（首批 120 天 / Scale 90 天，自下单起算），商务·运输·安装一律不承诺，另有假负载运行期 5–30 天（Supermicro 建议，不含在 EXW 内）；PUE 一律写 `1.0x`，逐站点用 <https://mdcx.org> 计算；质保为核心部件 EXW 起一年 + 按年服务费，ONSITE/NBD/24×7 以 Invoice 为准。基准：[[PRODUCT_SPEC_BASELINE]]。
