---
title: §P-4 典型混淆场景 + §P-5 UPS 选型
parent: "[[../POWER_SYSTEMS_Guideline]]"
order: 3
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/power
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/POWER_SYSTEMS_Guideline.md"
source_anchors: []
---

## P-4 典型混淆场景 (Common Confusion Scenarios)

### 场景 1：客户说"1.2MW 集群"

客户意图：通常指 IT 负载（GPU 算力）
工程师动作：确认是否为 IT 负载；如果是，计算整体电力负荷（约 1.38–1.56MW）

### 场景 2：客户说"场地有 2MW 电"

客户意图：通常指场地电力接入容量（整体负荷能力）
工程师动作：计算可支持的 IT 负载（PUE=1.15 → IT ≈ 1.74MW）；推荐 AC40×4 或 DC45×1 配置

### 场景 3：北美场地申请 Permit

客户意图：通常指整体电力容量（需申请 Utility 容量）
工程师动作：必须输出整体电力负荷（kW），并说明 IT 负载（kW），供客户向 Utility 申请容量

---

## P-5 UPS 选型 (UPS Selection)

> 本节为 Power Engineer 的 UPS 选型规则。设计前必须先满足前文 "[[#P-1 IT 负载与整体电力负荷|§P-1]]" 的澄清规则，再执行 UPS 选型。

### Power 总体设计原则

- AC45 / DC45：UPS 及 UPS 电池**内置**于集装箱，提供分钟级瞬时切换后备，UL 合规
- AC40：UPS 及 UPS 电池**需客户外置自备**，AC40 本体不含 UPS

### UPS 型号标准

| IT Zone | UPS 型号 | 模块数 | 总功率 | UPS 放置 | UPS 电池后备时间 |
|---------|----------|--------|--------|---------|--------------|
| **AC40** | EATON 9395XR-600 | 4 UPM | 600kW | **外置（客户自备）** | ~10 分钟（客户自备 2×93LiG2）|
| **AC45** | EATON 9395XR-600 | 4 UPM | 600kW | 内置（专用电力舱），UL 合规 | ~20 分钟（内置 2×93LiG2）|
| **DC45** | EATON 9395XR-1500 | 10 UPM | 1500kW | 内置，UL 合规 | ~8 分钟（内置 3×93LiG2）|

> ⚠️ UPS 型号数字 = kW（不是 kVA）。UPS 电池 ≠ BESS：UPS 电池是分钟级，BESS 是小时级。

参考：[[UPS_EATON_9395XR|KB/3RD-PARTY/UPS/Eaton/UPS_EATON_9395XR]]

### UPS 选型逻辑

- **容量公式**：UPS 容量 ≥ IT Load ÷ PF × 1.2（AC45/DC45 已内置；AC40 需客户按此公式外置选型）
- **型号标准化**：AC40/AC45 用 9395XR-600；DC45 用 9395XR-1500
- **认证**：EATON 9395XR 系列已具备 UL 认证
- **绑定约束**：UPS 型号与 IT Zone 强绑定，禁止替换。
