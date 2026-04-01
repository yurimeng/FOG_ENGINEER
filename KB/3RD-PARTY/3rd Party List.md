---
tags:
  - #workspace/engineer
  - #type/reference
  - #domain/supplier
Supplier Name:
Category: Reference
---

# 3rd Party List — 第三方产品和解决方案参考清单

版本：V1.2（2026-04-01 新增 Guideline 体系 + BESS 独立产品文档）

---

## 1. 分类体系说明

在 MDC 体系中，**IT Zone**（A32 / AC40 / DC45）是公司自主产品。
**Cooling Zone**、**Power Zone** 和 **Network Zone** 主要采用第三方成熟产品。

---

## 2. Cooling Zone — 冷却系统

> ⚠️ **引用规则：** 选型前必须先查阅 [[COOLING_SYSTEM_SOLUTION|KB/COOLING_SYSTEM_SOLUTION]]（冷却系统 Guideline），按其选型原则遍历子文件夹产品，最终组合完整解决方案。

### 2.1 Guideline（选型总则）

| 文件 | 说明 |
|------|------|
| [[COOLING_SYSTEM_SOLUTION\|KB/COOLING_SYSTEM_SOLUTION]] | 冷却 Zone 选型原则、架构对比、环境与 IT Zone 匹配规则 |

### 2.2 产品目录

| 类别 | 产品 | 供应商 | 说明 | 参考文档 |
|------|------|--------|------|---------|
| **散热方案（标准）** | 干冷器 + DX | — | MDC Cooling Zone 标准配置，所有 IT Zone 必须 | [[COOLING_SYSTEM_SOLUTION\|KB/COOLING_SYSTEM_SOLUTION]] |
| **散热方案（替代）** | 热泵 | — | 可替代 DX，同时加热和制冷 | [[COOLING_SYSTEM_SOLUTION\|KB/COOLING_SYSTEM_SOLUTION]] |
| **详细方案** | 干冷器 + DX 双冷源机组 | 泰铂 | MDC Cooling Zone 标准散热机组规格 | [[DRYCOOL_with_DX\|KB/DRYCOOL_with_DX]] |
| **集成冷站** | 600kW 集成冷站 | 三河同飞 | 一体化热泵冷源，含压缩机、水泵、控制系统 | [[Hybrid Cooler 600kW - 同飞\|KB/Hybrid Cooler 同飞]] |

### 2.3 冷却设备供应商参考

| 品牌/供应商 | 产品类型 | 备注 |
|------------|---------|------|
| 上海泰铂 | 干冷器 | 参考供应商 |
| 三河同飞 | 冷却设备 | 参考供应商 |
| 英维克股份 | 冷却设备 | 参考供应商 |

> ⚠️ 冷却设备选型需与 IT Zone 容量匹配，具体参数见产品文件。

---

## 3. Power Zone — 电力系统

> ⚠️ **引用规则：** 选型前必须先查阅 [[POWER_SYSTEMS_Guideline|KB/BESS/POWER_SYSTEMS_Guideline]]（电力系统 Guideline），按其选型原则遍历子文件夹产品，最终组合完整解决方案。

### 3.1 Guideline（选型总则）

| 文件 | 说明 |
|------|------|
| [[POWER_SYSTEMS_Guideline\|KB/BESS/POWER_SYSTEMS_Guideline]] | BESS 选型原则、UPS 选型逻辑、冗余策略、场景推荐 |

### 3.2 UPS（内置于 IT Zone）

| IT Zone | UPS 型号 | 模块数 | 每模块 | 总功率 | 发热量 | 参考文档 |
|---------|----------|--------|--------|--------|--------|---------|
| **AC40** | EATON 9395XR-600 | 4 UPM | 150kW | 600kW | ~7.9kW | [[UPS_EATON_9395XR\|KB/UPS_EATON_9395XR]] |
| **DC45** | EATON 9395XR-1500 | 10 UPM | 150kW | 1500kW | ~46.9kW | [[UPS_EATON_9395XR\|KB/UPS_EATON_9395XR]] |

> 注：UPS 型号数字代表总 UPS 功率（kW）。9395XR-600 ≠ 600kVA，而是 4×150kW = 600kW。

### 3.3 电池系统

| 品牌/型号 | 类型 | 每柜能量 | 每柜功率 | 适用 |
|----------|------|---------|---------|------|
| EATON 93LiG2（93Li92S-100Ah）| 磷酸铁锂 | 63.9kWh | 332kW | AC40 / DC45 |

### 3.4 BESS / 储能系统（独立产品文档）

| 品牌/型号 | 类型 | 适用场景 | 参考文档 |
|----------|------|---------|---------|
| TESLA Megapack 2 XL | 大型储能 | 城市边缘 / 高 ESG | [[TESLA MEGAPACK 2 XL\|KB/BESS/TESLA MEGAPACK 2 XL]] |
| 国轩 ESC480-125P261-UL | 工商业储能一体机 | 成本优化 / 国产方案 | [[Gotion ESC480-125P261-UL\|KB/BESS/Gotion ESC480]] |

### 3.5 电力设备

| 品牌/供应商 | 产品 | 说明 |
|------------|------|------|
| SIEMENS | 母线 Busbar | DC45 内置，1600A |
| SIEMENS | TOU（Tap-off Unit）| DC45 内置，含 MCCB |

---

## 4. Network Zone — 网络系统

> ⚠️ **引用规则：** 选型前必须先查阅 [[AC40_NETWORK_Guideline|KB/NETWORK/AC40_NETWORK_Guideline]]（网络系统 Guideline），按其选型原则遍历子文件夹产品，最终组合完整解决方案。

### 4.1 Guideline（选型总则）

| 文件 | 说明 |
|------|------|
| [[AC40_NETWORK_Guideline\|KB/NETWORK/AC40_NETWORK_Guideline]] | 网络架构原则、三层模型、交换机配置、安全要求 |

### 4.2 产品目录

| 类别 | 供应商/产品 | 说明 | 参考文档 |
|------|------------|------|---------|
| **布线系统** | 引澜（需求已确认）| 结构化布线，商用成熟产品，可直接采购 | [[PRODUCTS_NETWORK\|KB/PRODUCTS_NETWORK]] |
| **网络架构** | 三层网络模型 | 接入层/汇聚层/核心层 | [[AC40_NETWORK_Guideline\|KB/NETWORK_Guideline]] |
| **交换设备** | 按项目配置 | 支持 10G/25G/100G | 按项目配置 |
| **AC40 网络配置** | 参考配置 | AC40 集装箱网络端口定义及布线规范 | [[AC40_NETWORK_CONF.pdf\|KB/AC40_NETWORK_CONF.pdf]] |

---

## 5. Manufacturing & Assembly — 制造与组装

| 供应商 | 能力 | 备注 |
|--------|------|------|
| 三河同飞 | 冷却设备制造 | 参考供应商 |
| DSBJ（东山精密）| 制造 | 参考供应商 |
| 广东惠集 | 集装箱箱体制造 | **只做集装箱箱体**，其他所有件为客供，不做总集成 |
| 惟远能源 | 标准件供应 | **只做标准件，不定制**；定制需另签研发合同；未做过 UPS 和算力机柜一体 |

> ⚠️ 注意：广东惠集和惟远能源有明确的业务边界，方案设计时须注意不要超出其能力范围。

---

## 6. 引用规则

> ⚠️ 团队在引用第三方产品时，必须使用本清单中的标准产品。
> 如需引入清单以外的产品，必须经过 ATS 确认并更新本文件后方可使用。
> 产品选型必须与 IT Zone 类型（AC40/DC45）匹配。

---

## 7. 更新历史

| 日期 | 版本 | 变更内容 |
|------|------|---------|
| 2026-04-01 | V1.2 | 新增 Guideline 体系；BESS 目录独立，添加 Tesla Megapack 2 XL 和国轩产品文档；各 Zone 增加 Guideline 引用规则；同步更新 KB 路径引用 |
| 2026-03-29 | V1.1 | 统一命名结构；添加 UPS 型号（9395XR-600/1500）；增加冷却 Zone 标准配置说明 |
| 初始版本 | V1.0 | 初始第三方产品清单 |
