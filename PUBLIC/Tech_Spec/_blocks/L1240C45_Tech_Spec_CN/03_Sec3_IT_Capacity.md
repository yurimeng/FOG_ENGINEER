---
title: "L1240C45 第三节：IT 容量"
parent: "[[L1240C45_Tech_Spec_CN]]"
order: 3
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/l1240c45"
  - "#thermal"
  - "#MDC"
created: 2026-06-18
source_file: "PUBLIC/Tech_Spec/L1240C45_Tech_Spec_CN.md"
source_anchors:
  - "^sec-3-it-capacity"
---

## 3. IT 容量 ^sec-3-it-capacity

| 项目 | 参数 |
|------|------|
| **IT 总容量** | **1240kW** |
| DLC 机柜 | 8 × 150kW（每柜 150kW，73% 液冷 / 27% 风冷） |
| 风冷机柜 | 1 × 40kW |
| TCS 进水温度 | **26–28°C**（CDU 二次侧供水至冷板/RDHX/CeilAir 冷凝器）|
| 机柜前进风温度 | **25–27°C**（CeilAir DX 蒸发出风 12–18°C，与 TCS 水温解耦）|
| 服务器排气温度 | **41–48°C**（满载 S-Max 工况，超 DCD35 datasheet 标定 40°C 上限，Vertiv 复核中）|
| DLC 风冷比例 (φ_air) | 设计上限 **27%**，CDU 护栏 ≥ **8%** |
| 功率因数（UPS 输出侧） | 0.9 |

### IT负载 vs 整体电力负荷

| 项目 | 数值 | 说明 |
|------|------|------|
| **IT 负载** | 1240kW | 服务器、GPU 实际消耗 |
| **整体电力负荷（Total Facility Load）** | 随 PUE 变化，**逐站点用 <https://mdcx.org> 计算** | ✅ 2026-08-30 裁定（关闭 C-2）。原「~1325–1675kW」区间作废 |
| **PUE** | **`1.0x`** | ✅ 2026-08-30 裁定。**不给固定值、不给区间、不给「典型值」**，逐站点计算，入口 <https://mdcx.org>（TCO / Designer）。原「~1.07–1.15 / ~1.25–1.35」全部作废 |

> **IT Load ≠ Total Facility Load。** 这个区分是硬规则（[[CLAUDE.md]] Hard Rule 5），必须保留：IT 负载决定买到多少算力，设施总负荷决定变电容量申请与电费测算。**但设施负荷不给数字** —— 逐站点用 <https://mdcx.org> 的 TCO / Designer 计算。
>
> 定性可说：环境温度较低、顶置机组压缩机可部分停机的站点落在低端；高环温、DX 主导的站点 PUE 上移。**但不给数。** 见 [[PRODUCT_SPEC_BASELINE#^baseline-pue]]。

---
