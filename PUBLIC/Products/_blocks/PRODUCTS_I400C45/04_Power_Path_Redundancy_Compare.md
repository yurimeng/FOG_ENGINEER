---
title: 电力路径 + 冗余 + AC45 vs AC40 vs DC45 对比
parent: "[[../I400C45]]"
order: 4
tags:
  - #workspace/engineer
  - #type/product
  - #product/i400c45
  - #power
  - #MDC
created: 2026-06-18
source_file: "PUBLIC/Products/I400C45.md"
source_anchors: []
---

## 6. 电力路径

```
Grid / BESS → PDC → UPS (EATON 9395XR-600) → PDC → Tanks → PDU
```

说明：
- UPS 及 UPS电池**内置于专用电力舱**（AC45 本体含 UPS），无需客户另行采购 ^mdc-4fa3dcad40
- UPS电池 2×93LiG2 置于电力舱内，提供约 20 分钟后备
- BESS 连接方式：Grid → BESS → AC45（Power Zone 负责，BESS 与 UPS电池完全不同） ^mdc-09241c3cb6
- 也支持 Grid → ATS → Generator → AC45（视客户场地条件） ^mdc-76b991beb6

### 6.1 网络与监控配置

参考：[[I400C40_NETWORK_CONF]]

![[I400C40_NETWORK_CONF.pdf]]

---

## 7. 冗余说明

> ⚠️ **重要区分：UPS 模块冗余 vs IT Zone 容器冗余**

| 层级 | 冗余描述 |
|------|---------|
| **UPS 模块** | 9395XR-600 内置 4 个功率模块，支持内部 N+1（单模块故障不影响运行）|
| **CDU** | 各 Tank 内置 Dual CDU，1+1 完全冗余 |
| **UPS 电池后备** | 2×93LiG2，共约 20 分钟后备（内置于电力舱；AC40 需客户外置自备） ^mdc-651d0a0438 |
| **IT Zone（AC45 集装箱）** | **无内部冗余** — 单台 AC45 独立运行，不含内部 N+1/2N ^mdc-61b94ac6f0 |
| **MDC 系统级** | 多台 AC45 并联 → 系统级冗余（N / N+1 / 2N 由集装箱数量决定） ^mdc-0c0799b8db |

> AC45 是一台完整的集装箱设备，不存在"多增加几个服务器"来增加冗余的概念。 ^mdc-a0f9aea404
> 如需更高可靠性，通过增加 AC45 集装箱数量实现。 ^mdc-fb72dc9661

---

## 8. AC45 vs AC40 vs DC45 对比 ^mdc-ebcbceea71

| 项目 | **AC45** | AC40 | DC45 ^mdc-a2518aa694 |
|------|----------|------|------|
| 集装箱规格 | **45ft** | 40ft | 45ft |
| 冷却类型 | **浸没式** | 浸没式 | DLC 直冷液冷 |
| IT 容量 | **400kW** | 400kW | 1240kW |
| Tank/Rack 数量 | 8×A32 | 8×A32 | 8×DLC（150kW/柜） ^mdc-8107f5a9c7 |
| UPS 型号 | 9395XR-600 | 9395XR-600 | 9395XR-1500 |
| UPS 放置 | **内置（专用电力舱）** | **外置（客户自备）** | 内置 |
| UPS 电池放置 | **内置（电力舱）** | **外置（客户自备）** | 内置 |
| UPS 电池后备时间 | **~20 分钟** | ~10 分钟（客户自备）| ~8 分钟 |
| UL 合规 | **✅ 是** | ❌ 否 | ✅ 是 |
| 二次侧进油温度（ΔT=8K） | ≤35°C | ≤35°C | 26–28°C（DLC 直冷） |
| 风冷机柜 | 10kW × 1 | 10kW × 1 | 210kW 风墙 |
| 整体电力负荷（参考）| ~440–500kW | ~440–480kW | ~1380–1560kW |

> ⚠️ **UPS 电池 vs BESS 电池：** 上表中"UPS 电池后备"指 UPS 配套的 93LiG2 磷酸铁锂电池柜（分钟级瞬时切换后备）。BESS（如 Tesla Megapack / 国轩）是独立大型储能系统（小时级供电），两者完全不同。

> **选型建议：**
> - 400kW + 无 UL 合规要求 → **AC40**（40ft，UPS及UPS电池外置，成本/尺寸最优） ^mdc-71c0f0c158
> - 400kW + 需要 UL 合规 → **AC45**（45ft，UPS及UPS电池内置，UL 认证） ^mdc-e0a16eb8a7
> - 1240kW DLC + UL 合规 → **DC45**（45ft，DLC 直冷，UPS及UPS电池内置，UL 认证） ^mdc-714930cf36
