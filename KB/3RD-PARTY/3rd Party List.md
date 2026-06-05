---
tags:
  - "#workspace/engineer"
  - "#type/reference"
  - "#domain/supplier"
  - #MDC
Supplier Name:
Category: Reference
doc_version: v1.7
audience: 人(销售/售前/选型工程师) + 工程师+AI(供应商管理体系查询)
---
# 3rd Party List — 第三方产品和解决方案参考清单

版本：V1.7（2026-06-06 新增 [[COOLING/Suppliers/PRD-STULZ-CeilAir]] (候选 Candidate 状态, 基于 STULZ《CeilAir Engineering Manual》2018 版 85 页 PDF 提取 OHS-084-DG-FC 全部参数; §3.2 STULZ 行添加"UL/CETL 已认证(60Hz 专用), CE / 50Hz 缺席"警示; STULZ 状态由"待 STULZ 回复"细化为"Q1 50Hz/CE 待 STULZ 回复"); V1.6 TICA 评审文档重命名: `TICA_Hybrid_Chiller_Configuration_Review` → `TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review`(含产品型号); 新增 `TICA风冷磁浮冷水机组技术参数表&配置表.xlsx` 厂家更新版主源; CSVs 标记为历史投标资料; V1.5 重组:建立 DESIGN/ + Suppliers/ 二级分类;新增 [[STD_Supplier]] 统一供应商管理体系入口;2 个冷却 CSV 移至 COOLING/Suppliers/;保持 CLAUDE.md Hard Rule 6 无静默改）

---

## 1. 分类体系说明

在 MDC 体系中，**IT Zone**（A32 / AC40 / AC45 / DC45）是公司自主产品。
**Cooling Zone**、**Power Zone** 和 **Network Zone** 主要采用第三方成熟产品。

### 1.1 二级目录结构（V1.5 新增）

```
3RD-PARTY/
├── STD_Supplier.md             ← ★ 统一供应商管理体系入口
├── BESS/{DESIGN,Suppliers}/
├── Busbar/{DESIGN,Suppliers}/
├── UPS/{DESIGN,Suppliers}/
└── COOLING/{DESIGN,Suppliers}/
```

- **DESIGN/**  — R&D 设计准则/需求书(受众:工程师 + AI)
- **Suppliers/**  — 供应商产品 PRD / 选型记录(受众:人)

---

## 2. Agent 引用规则（重要）

> **Agent 在读取第三方产品时的标准顺序：**
> 1. 查询 [[3rd Party List|3rd Party List]] ← 本文件
> 2. 查询 [[STD_Supplier|STD_Supplier]] ← **V1.5 新增**:跨类别供应商管理体系
> 3. 查询对应类别的 **Guideline**（设计原则）
> 4. 在子文件夹中查找合适的产品文档，匹配解决方案

---

## 3. Cooling Zone — 冷却系统

### 3.1 Guideline（选型总则）

> ⚠️ **引用规则：** 选型前必须先查阅 Guideline，再按其选型原则遍历子文件夹产品。

| 文件 | 说明 |
|------|------|
| [[FOG/KB/Guideline/COOLING_SYSTEM_Guideline]] | 冷却 Zone 选型原则：架构分类（DX/螺杆/磁悬浮/热泵）、环境温度策略、IT Zone 匹配规则、A32 纯干冷例外 |

### 3.1.1 DESIGN/ 子目录

| 文件 | 说明 |
|------|------|
| [[COOLING/DESIGN/RDHX_Requirement]] | RDHx 技术规格需求书(规范 DC45 后门换热器选型与设计) |
| [[COOLING/DESIGN/CDU_Requirement]] | CDU 技术规格需求书(规范 AC40 浸没 CDU 和 DC45 DLC Rack CDU 选型) |
| [[COOLING/DESIGN/CRAH_Requirement]] | CRAH 技术规格需求书(规范 CRAH 选型与设计) |
| [[COOLING/DESIGN/Hybrid Chiller Requirement 技术规格需求书]] | DC45 大型 Hybrid Chiller 规格需求书(1200–1500kW) |
| [[COOLING/DESIGN/计算公式]] | DC45 仿真引擎公式参考 |
| [[COOLING/DESIGN/COOLING_DESIGN_v4_lockdown_plan]] | v4 Reading 决策期间工作底稿 |

### 3.1.2 Suppliers/ 子目录

| 文件 | 说明 |
|------|------|
| [[COOLING/Suppliers/PRD-Vertiv-RDHx]] | VERTIV DCD35 被动 RDHx 售前 PRD |
| [[COOLING/Suppliers/PRD-STULZ-CeilAir]] | STULZ OHS-084-DG-FC 顶置 DX CRAH 候选 PRD(基于厂家 Engineering Manual 2018 版; **UL only, 60Hz, 无 CE**) |
| [[COOLING/Suppliers/PRD-同飞-Chiller-600KW]] | 三河同飞 600 kW 集成冷站 PRD(AC40 标配) |
| [[COOLING/Suppliers/PRD-泰铂-Chiller]] | 泰铂干冷器+DX 散热方案 PRD(AC40/AC45 标配) |
| [[COOLING/Suppliers/TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review]] | TICA TAMFV430.3ALF5 Chiller 内部技术评审(候选引入, v1.3 电气配件已更新) |
| [[COOLING/Suppliers/TICA_Clarification_Email_Drafts]] | TICA 投标澄清邮件草稿(已外发) |
| `TICA风冷磁浮冷水机组技术参数表&配置表.xlsx` | TICA 厂家 xlsx 主源(2026-06-06 更新, 含 Catalog + 配置表更新电气部分 两个 sheet) |
| `风冷磁浮冷水机组技术参数表&配置表.csv` | TICA CSV 1 — 系统参数(历史投标资料) |
| `自然冷却风冷螺杆式冷水机组.csv` | TICA CSV 2 — 配置/部件 BOM(历史投标资料) |

### 3.2 产品目录

| 类别 | 产品 | 供应商 | 说明 | 参考文档 | 状态 |
|------|------|--------|------|---------|------|
| **干冷器 + DX** | Hybrid Cooling System（AC40/AC45 标准配置）| 泰铂 | 干冷器 + DX 双冷源,AC40/AC45 标配 | [[COOLING/Suppliers/PRD-泰铂-Chiller]] | ✅ 已经review完成 |
| **集成冷站** | 600kW 集成冷站 | 三河同飞 | 螺杆式压缩机,一体化热泵冷源(**AC40 标配**)| [[COOLING/Suppliers/PRD-同飞-Chiller-600KW]] | ✅ 已经review完成 |
| **Hybrid Chiller** | 大型 Hybrid Chiller(DC45 专用)| 待全球招标 | 额定制冷量 ≥1600 kW(**DC45 标配,600kW 冷站不适用 DC45**)| [[COOLING/DESIGN/Hybrid Chiller Requirement 技术规格需求书]] | ⏳ 正在review (TICA 候选) |
| **CDU（AC40/AC45 浸没式）** | 内阻 Dual CDU | 三河同飞 / 待确认 | AC40/AC45 浸没回路,1+1 冗余 | [[COOLING/DESIGN/CDU_Requirement]] | ⏳ 正在review |
| **CDU（DC45 DLC）** | Rack CDU,≥1500kW | 待全球招标 | DC45 DLC 主回路,VFD 泵,2N/N+1 冗余 | [[COOLING/DESIGN/CDU_Requirement]] | ⏳ 正在review |
| **顶置空调** | STULZ OHS-084-DG-FC | STULZ | DC45 舱内残余热处理,9 台(PG25 兼容);**UL/CETL 已认证(60Hz 专用), CE / 50Hz 缺席, 欧洲/亚太 50Hz 客户 Q1 闭环前不得报价** | [[COOLING/Suppliers/PRD-STULZ-CeilAir]] | ⏳ 正在review (Q1 50Hz/CE 待 STULZ 回复) |
| **后门换热器** | Vertiv DCD35 被动 RDHx | VERTIV | DC45 机柜后门余热回收,9 台 | [[COOLING/Suppliers/PRD-Vertiv-RDHx]] | ⏳ 正在review (Q1 待 VERTIV 回复) |
| **RDHx 规格** | RDHx 技术规格需求书 | — | 规范 RDHx 选型与设计要求 | [[COOLING/DESIGN/RDHX_Requirement]] | (规范) |
| **CRAC 规格** | CRAH 技术规格需求书 | — | 规范 CRAH 选型与设计要求 | [[COOLING/DESIGN/CRAH_Requirement]] | (规范) |

> ⚠️ **冷却系统容量匹配规则：**
> - AC40(IT 400kW)→ 600kW 集成冷站 ✅
> - DC45(IT 1240kW)→ 需要 ≥1600kW Hybrid Chiller,**600kW 冷站不满足 DC45 需求**
> - 所有冷却产品选型须符合 [[FOG/KB/Guideline/COOLING_SYSTEM_Guideline]] 的架构分类与 IT Zone 匹配规则

### 3.3 架构类型速查

| 架构类型 | 压缩机 | 适用制冷量 |
|---------|--------|-----------|
| DX 方案 | 涡旋式 | <300kW |
| 螺杆压缩机方案 | 螺杆式 | 300–600kW |
| 磁悬浮压缩机方案 | 磁悬浮 | 能效优先 |
| 热泵方案 | 热泵机组 | 极寒/精确温控 |

### 3.4 供应商参考

| 品牌/供应商 | 产品类型 | 备注 |
|------------|---------|------|
| 泰铂(上海)| 干冷器 + DX | 参考供应商 |
| 三河同飞 | 冷却设备、集成冷站 | 参考供应商 |
| 英维克股份 | 冷却设备 | 参考供应商 |
| VERTIV | RDHx | 评审中(候选) |
| STULZ | 顶置空调 | 评审中(候选) |
| TICA(天加)| Hybrid Chiller | 评审中(候选,3rd Party List 增补流程中) |

---

## 4. Power Zone — 电力系统

### 4.1 Guideline（选型总则）

> ⚠️ **引用规则：** 选型前必须先查阅 Guideline，再按其选型原则遍历子文件夹产品。

| 文件 | 说明 |
|------|------|
| [[FOG/KB/Guideline/POWER_SYSTEMS_Guideline]] | 电力 Zone 选型原则:BESS 选型逻辑、UPS 选型、冗余策略、场景推荐 |

### 4.1.1 DESIGN/ 子目录

| 文件 | 说明 |
|------|------|
| (暂无) | 电力 Zone 当前仅 Suppliers/ 有内容,设计准则见 [[FOG/KB/Guideline/POWER_SYSTEMS_Guideline]] |

### 4.1.2 Suppliers/ 子目录

| 文件 | 说明 |
|------|------|
| [[UPS/Suppliers/Eaton/UPS_EATON_9395XR]] | EATON 9395XR 系列 UPS(AC40/AC45/DC45 全覆盖)|
| `UPS/Suppliers/Eaton/*.pdf` | EATON 9395XR / 93LiG2 电池组 datasheet |
| [[BESS/Suppliers/TESLA MEGAPACK 2 XL]] | Tesla Megapack 兆瓦级 BESS |
| [[BESS/Suppliers/Gotion ESC480-125P261-UL]] | 国轩工商业储能一体机 |
| `Busbar/Suppliers/Siemens/*.pdf` | Siemens XL-III / XL-F 母线 datasheet |

### 4.2 UPS（IT Zone 标配）

| IT Zone | UPS 型号 | 模块数 | 每模块 | 总功率 | 发热量 | UPS 放置 | UPS电池后备时间 | 参考文档 | 状态 |
|---------|---------|--------|--------|--------|--------|---------|--------------|---------|------|
| **AC40** | EATON 9395XR-600 | 4 UPM | 150kW | 600kW | ~7.9kW | **外置(客户自备)** | ~10 分钟(客户自备 2×93LiG2) | [[UPS/Suppliers/Eaton/UPS_EATON_9395XR]] | ✅ |
| **AC45** | EATON 9395XR-600 | 4 UPM | 150kW | 600kW | ~7.9kW | 内置(专用电力舱),UL 合规 | ~20 分钟(内置 2×93LiG2) | [[UPS/Suppliers/Eaton/UPS_EATON_9395XR]] | ✅ |
| **DC45** | EATON 9395XR-1500 | 10 UPM | 150kW | 1500kW | ~46.9kW | 内置,UL 合规 | ~8 分钟(内置 3×93LiG2) | [[UPS/Suppliers/Eaton/UPS_EATON_9395XR]] | ✅ |

> 注：UPS 型号数字代表总 UPS 功率(kW)。9395XR-600 ≠ 600kVA,而是 4×150kW = 600kW。**AC40 UPS 及 UPS电池需客户外置自备;AC45/DC45 UPS 及 UPS电池内置于集装箱。**

> ⚠️ **UPS 电池 vs BESS 电池:** 上表中"UPS电池后备"指 UPS 配套的 93LiG2 磷酸铁锂电池柜(分钟级瞬时切换后备)。BESS(如 Tesla Megapack / 国轩)是独立大型储能系统(小时级供电),两者完全不同。

### 4.3 UPS 电池系统

| 品牌/型号 | 类型 | 每柜能量 | 每柜功率 | 适用 |
|----------|------|---------|---------|------|
| EATON 93LiG2(93Li92S-100Ah)| 磷酸铁锂 | 63.9kWh | 332kW | AC45 / DC45(内置);AC40(客户自备,外置)|

### 4.4 BESS / 储能系统

| 品牌/型号 | 类型 | 适用场景 | 参考文档 | 状态 |
|----------|------|---------|---------|------|
| TESLA Megapack 2 XL | 大型储能(集装箱级)| 城市边缘 / 高 ESG | [[BESS/Suppliers/TESLA MEGAPACK 2 XL]] | ✅ |
| 国轩 ESC480-125P261-UL | 工商业储能一体机 | 成本优化 / 国产方案 | [[BESS/Suppliers/Gotion ESC480-125P261-UL]] | ✅ |

### 4.5 电力设备

| 品牌/供应商 | 产品 | 说明 | 状态 |
|------------|------|------|------|
| SIEMENS | 母线 Busbar | DC45 内置,2500A | ✅ |
| SIEMENS | TOU(Tap-off Unit)| DC45 内置,含 MCCB | (待补 PRD) |

---

## 5. Network Zone — 网络系统

> **V1.5 状态:** 网络类文档整体迁移至 [[FOG/KB/FOG A Series/Design/|FOG A Series/Design/]],此处不再列出(参见 `[[FOG/KB/FOG A Series/index]]`)。
> 网络 Zone 选型原则:见 Guideline(已删除)→ 当前由各 IT Zone 设计文档自带。

---

## 6. Manufacturing & Assembly — 制造与组装

| 供应商 | 能力 | 备注 |
|--------|------|------|
| 三河同飞 | 冷却设备制造 | 参考供应商 |
| DSBJ(东山精密)| 制造 | 参考供应商 |
| 广东惠集 | 集装箱箱体制造 | **只做箱体**,其他所有件为客供,**不做总集成** |
| 惟远能源 | 标准件供应 | **只做标准件,不定制**;定制需另签研发合同;未做过 UPS 和算力机柜一体 |

> ⚠️ 注意：广东惠集(箱体)和惟远能源(标准件)有明确的业务边界,方案设计时须注意不要超出其能力范围。三河同飞专注冷却设备,DSBJ 专注制造。

---

## 7. 禁止事项

- ❌ 禁止引入清单以外的第三方产品(须经 ATS 确认并更新本文件后方可使用)
- ❌ 禁止冷却 Zone 与 IT Zone 容量不匹配
- ❌ AC40/DC45 禁止纯干冷器作为唯一散热方式
- ❌ 带外管理网络不得与带内管理网络共用物理链路

---

## 8. 统一供应商管理体系入口(NEW V1.5)

> 跨类别查询供应商评审状态时,使用 [[STD_Supplier|STD_Supplier]]。
> 本文件 §3 / §4 中的"状态"列与 STD_Supplier §1 同步。

---

## 9. 更新历史

| 日期 | 版本 | 变更内容 |
|------|------|---------|
| 2026-06-06 | V1.7 | 新增 [[COOLING/Suppliers/PRD-STULZ-CeilAir]] (候选 Candidate 状态): 基于 STULZ《CeilAir Engineering Manual》2018 版 85 页 PDF 提取 OHS-084-DG-FC 全部参数; §3.2 STULZ 行添加"UL/CETL 已认证(60Hz 专用), CE / 50Hz 缺席"警示; STULZ 状态由"待 STULZ 回复"细化为"Q1 50Hz/CE 待 STULZ 回复"。 |
| 2026-06-06 | V1.6 | TICA 评审文档重命名: `TICA_Hybrid_Chiller_Configuration_Review` → `TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review`(含产品型号); 新增 `TICA风冷磁浮冷水机组技术参数表&配置表.xlsx` 厂家更新版主源;CSVs 标记为历史投标资料。 |
| 2026-06-06 | V1.5 | 重组:建立 DESIGN/ + Suppliers/ 二级分类;新增 [[STD_Supplier]] 统一供应商管理体系入口;2 个冷却 CSV 移至 COOLING/Suppliers/;状态列与 STD_Supplier §1 同步;NETWORK 段迁至 FOG A Series/Design/ |
| 2026-05-22 | V1.4 | 新增 STULZ CeilAir、Vertiv RDHx、Hybrid Chiller 规格需求书;补充冷却 Zone DESIGN/ 子目录;完善制造供应商说明;修复 UPS 电池表空行格式 |
| 2026-04-09 | V1.3 | 新增独立 Guideline 体系;冷却系统拆分为 Guideline(架构选型)+ 产品文档;网络系统拆分为 Guideline(IB/ROCE/带内/带外)+ 产品文档;Buildin 重命名为 UPS |
| 2026-04-01 | V1.2 | 新增 Guideline 体系;BESS 目录独立,添加 Tesla Megapack 2 XL 和国轩产品文档 |
| 2026-03-29 | V1.1 | 统一命名结构;添加 UPS 型号(9395XR-600/1500);增加冷却 Zone 标准配置说明 |
| 初始版本 | V1.0 | 初始第三方产品清单 |

---

*Document Version: v1.7 | Last Updated: 2026-06-06*
