---
tags:
  - #workspace/engineer
  - #type/product
  - #product/mdc
  - #MDC
---
# MDC – Modular Datacenter Cluster
模块化数据中心集群标准组合参考
版本：V2.0（2026-08-30 六 SKU 对齐版）

> **参数基准：** [[PRODUCT_SPEC_BASELINE]]。本文档讲的是 **MDC 集群怎么组**（Zone 划分、配置组合、冗余规则），单 SKU 规格一律回基准表查。
> **命名基准：** [[NAMING_MAP]]。置信度标记见 [[UNCONFIRMED_Convention]]。

---

## 1. MDC 定义

MDC（Modular Datacenter Cluster）是由多个模块组成的模块化数据中心。
每个 MDC 由三个 Zone 组成：

| Zone | 中文名 | 描述 |
|------|--------|------|
| **IT Zone** | 算力单元区 | 提供服务器容纳，部分 SKU 含 UPS。六个 SKU 任选：L1240C45 / L1800C45 / L450C20（液冷线）· I400C45 / I400C40 / I200C20（浸没线） |
| **Cooling Zone** | 冷却单元区 | 外制冷，为 IT Zone 内服务器提供散热能力 |
| **Power Zone** | 电力单元区 | 后备电源系统，由 BESS 或柴油发电机提供 |

---

## 2. 架构图

```
Transformer → Switchgear → [Power Zone: BESS / Generator]
                          ↓
        [IT Zone: L1240C45 / L1800C45 / L450C20 / I400C45 / I400C40 / I200C20]
                      ├── PDC → UPS → CDU → Tanks/Racks
                      ↓
              [Cooling Zone: Hybrid Cooling System（干冷器+DX一体化）]
```

---

## 3. IT Zone 产品对照

**六个 SKU 全部 `shipped`**（站点 `PRODUCT-MATRIX.md` 2026-08-27 D-19 gate 放行）。

| 产品 | 全 SKU | 旧名 | 规格 | IT 容量 | 冷却类型 | UPS 放置 | UPS 电池后备 | UL |
|------|--------|------|------|---------|----------|---------|-----------|-----|
| **L1240C45** | `L1240C45SUR150` | DC45 | 45ft HC | 1240kW | Liquid Cooling · 单环路 | **内置** | 3×93LiG2（~8min）| ✅ |
| **L1800C45** | `L1800C45DR220` | — | 45ft HC | 1800kW | Liquid Cooling · 双环路 | 外置 | 不适用 | ⏳ |
| **L450C20** | `L450C20DR150` | — | 20ft ⏳ | 450kW | Liquid Cooling · 双环路 | 外置 | 不适用 | ⏳ |
| **I400C45** | `I400C45SUT50` | AC45 | 45ft（含电力舱）| 400kW | 浸没式 | **内置**（600kW）| 2×93LiG2（~20min）| ✅ |
| **I400C40** | `I400C40ST50` | AC40 | 40ft | 400kW（推荐 360kW）| 浸没式 | 外置（客户自备）| 2×93LiG2（~10min，客户自备）| ⏳ ⛔ |
| **I200C20** | `I200C20ST50` | AC20 | 20ft 算力舱 | 200kW | 浸没式 | 外置 | ⏳ | ⏳ |
| **I50TS**（组件）| `I50TS` ⚠️ | A32 | 单槽 | 45–50kW | 浸没式 | 外置（客户自备）| 外置 | — |

> ⚠️ `I50TS` 为 KB 侧按 Tank 正则推导，⏳ 待站点 Alias registry 确认（[[PRODUCT_SPEC_BASELINE#^baseline-conflicts|基准表 C-7]]）。它是 I400C45/I400C40 的 8× 与 I200C20 的 4× 构成单元，不是独立 SKU。
> ⛔ I400C40 的 UL 状态未定义（站点该格为空白），见[[PRODUCT_SPEC_BASELINE#^baseline-conflicts|基准表 C-5]]。**受管制市场投标前须经 Compliance Officer 确认。**
> 各 SKU 完整规格见 [[PRODUCT_SPEC_BASELINE]]；选型判断见 [[MDC_Product_Quick_Ref]]。

> ⚠️ **UPS 电池 vs BESS 电池：** 上表中"UPS电池后备"指 UPS 配套的 93LiG2 磷酸铁锂电池柜（分钟级瞬时切换后备）。BESS（如 Tesla Megapack / 国轩）是独立大型储能系统（小时级供电），两者完全不同。

参考（每个 SKU 三版：CN / EN / 对外版）：
- L1240C45：[[L1240C45_Tech_Spec_CN|CN]] · [[L1240C45_Tech_Spec_EN|EN]] · [[L1240C45_Tech_Spec_External|对外版]]
- L1800C45：[[L1800C45_Tech_Spec_CN|CN]] · [[L1800C45_Tech_Spec_EN|EN]] · [[L1800C45_Tech_Spec_External|对外版]]
- L450C20：[[L450C20_Tech_Spec_CN|CN]] · [[L450C20_Tech_Spec_EN|EN]] · [[L450C20_Tech_Spec_External|对外版]]
- I400C45：[[I400C45_Tech_Spec_CN|CN]] · [[I400C45_Tech_Spec_EN|EN]] · [[I400C45_Tech_Spec_External|对外版]] · [[PUBLIC/Products/I400C45|PRD]]
- I400C40：[[I400C40_Tech_Spec_CN|CN]] · [[I400C40_Tech_Spec_EN|EN]] · [[I400C40_Tech_Spec_External|对外版]] · [[PUBLIC/Products/I400C40|PRD]]
- I200C20：[[I200C20_Tech_Spec_CN|CN]] · [[I200C20_Tech_Spec_EN|EN]] · [[I200C20_Tech_Spec_External|对外版]]
- I50TS：[[PUBLIC/Products/I50TS|I50TS]]

> **只有对外版可直接发客户。** CN/EN 版含 ⏳ 待证实字段，见 [[UNCONFIRMED_Convention#^unconfirmed-external|标注规范 §5]]。

---

## 4. 最小节点规格

| 等级 | IT 容量 | 典型配置 | 冷却方式 | 使用场景 |
|------|---------|---------|----------|----------|
| **Single** | 0.5MW | 1–2× I400C40/I400C45，或 2–3× I200C20 | 浸没式 | 边缘推理 |
| **Small** | 1.2MW | 1× L1240C45，或 3× I400C40/I400C45，或 2–3× L450C20 | Liquid / 浸没式 | 边缘推理 / 模型再训练 |
| **Medium** | 2–3MW | 2× L1240C45，或 1–2× L1800C45，或液冷+浸没混合 | 混合 | 区域级边缘节点 |
| **Large** | 5MW+ | 多个 MDC 并联（L1800C45 单箱密度最高） | 按需组合 | 数据中心级部署 |

> **I400C45 vs I400C40 选型提示：** 两者 IT 容量与八槽核心完全相同，差别只有电力边界和那五英尺（= 电力舱体积）。场地已有配电、或锂电不许进箱 → I400C40；场地没有配电、且允许锂电进箱 → I400C45（另具 UL 与 ~20min 后备）。
>
> **液冷线选型提示：** 空地起步选 L1240C45（UPS 在箱内）；缺地不缺电选 L1800C45（220 kW/柜）；45ft 进不去选 L450C20。详见 [[MDC_Product_Quick_Ref]] §2。

---

## 5. 标准配置参考（团队引用标准）

> ⚠️ 以下为标准组合推荐。实际配置根据客户需求由 ATS 确认。

### 5.1 小规模边缘推理（0.5–1MW）

| 项目 | 配置 |
|------|------|
| 推荐产品 | I400C40（场地已有配电）/ I400C45（需整体交付）|
| 数量 | 1–2 台 |
| IT 容量 | 400–800kW |
| 冷却 | 浸没式（干冷 + DX）|
| 电力 | Grid + UPS + BESS（推荐）/ 柴油发电机 |
| 冗余 | IT Zone 独立运行；Power Zone 可选 N+1 |

### 5.2 中等规模推理/训练（1–3MW）

| 项目 | 配置 |
|------|------|
| 推荐产品 | L1240C45，或 L1240C45 + I400C40 混合 |
| 数量 | 1–3 台 L1240C45，或混合组合 |
| IT 容量 | 1240–3720kW |
| 冷却 | Liquid Cooling（Hybrid Chiller ≥1600kW）|
| 电力 | Grid + UPS + BESS（推荐）|
| 冗余 | N+1（Power Zone 可升级 2N）|

### 5.3 大规模集群（3MW+）

| 项目 | 配置 |
|------|------|
| 推荐产品 | 多台 L1240C45 / L1800C45 + I400C40 组合 |
| 扩展方式 | 横向并联（增加集装箱数量）|
| IT 容量 | 3MW+ |
| 冷却 | 按集装箱类型独立配置 |
| 电力 | Grid + UPS + BESS（Power Zone N+1/2N）|

---

## 6. 冷却 Zone 配置标准

> 冷却 Zone 与 IT Zone **一对一配置**，每个 IT Zone 集装箱配置一套独立冷却设备。

| IT Zone | 冷却 Zone 配置 | 散热方式 |
|---------|---------------|----------|
| I400C45 / I400C40 / I200C20（浸没式）| **Hybrid Cooling System**（干冷器+DX一体化）| 每台独立配置 |
| L1240C45（液冷·单环路）| **Hybrid Chiller** ≥1600 kW（TICA TAMFV430.3ALF5 已 ATS Full Pass）+ 三支路 TCS PG25 | 每台独立配置 |
| L1800C45（液冷·双环路）| GPU 侧 **STULZ SCR 14103 W** CDU + 列间侧 **STULZ CRS 560 CW**（均 ✅ ATS approved）· 室外侧 ⏳ | ⏳ 台数与冗余未定 |
| L450C20（液冷·双环路）| ⏳ **#unconfirmed** —— 列间空调 疑为 [[PRD-STULZ-CW330\|CW330]]，等厂家参数（2026-08-31）与 ATS 指定归属 | ⏳ |

> ⚠️ **规则：不允许纯干冷器方案。** 浸没线必须配置 Hybrid Cooling System（干冷器+DX一体化），确保环境温度 >28°C 时的散热能力。**唯一例外是 [[I50TS]] 单槽的纯干冷场景**，见 [[COOLING_SYSTEM_Guideline]]。
>
> ⚠️ **600kW 集成冷站不适用液冷线。** L1240C45（IT 1240kW）需 ≥1600kW Hybrid Chiller。容量匹配规则见 [[02_Cooling_Zone]]。
>
> ⚠️ **L1800C45 / L450C20 尚无专属 列间空调 / CDU Requirement**，冷却侧目前只有 PRD、没有需求书基线。这是当前最大的工程文档缺口。

参考：[[COOLING_SYSTEM_Guideline]]

---

## 7. 电力 Zone 配置标准

| 架构 | 适用场景 | 特点 |
|------|---------|------|
| **Grid + UPS + BESS**（推荐）| 城市边缘 / 高 ESG 要求 / 电网不稳定 | 毫秒切换、稳压、模块化 |
| **Grid + UPS + 柴油发电机** | 偏远地区 / 长时备电需求（>8h）| 机械发电、长时间运行 |
| **Grid + UPS + BESS + 小型柴油** | 极端高可靠性需求 | BESS 覆盖瞬态 + 柴油兜底 |

> 参考：[[POWER_SYSTEMS_Guideline]]

---

## 8. 冗余设计规则

| Zone | 可选冗余 | 说明 |
|------|---------|------|
| **IT Zone** | **无内部冗余** | 每个容器独立运行；多容器之间可提供系统级 N+1/2N |
| **Cooling Zone** | **无内部冗余** | 每台冷却设备一对一服务对应 IT Zone；多套冷却设备之间无冗余共享 |
| **Power Zone** | **N+1 / 2N 可选** | 需要额外的 Switchgear 配置（成本增加）|

> ⚠️ **重要：** IT Zone 和 Cooling Zone 不提供 N+1 或 2N 冗余。每个容器/设备独立工作。如客户需要更高冗余，通过增加整个集装箱数量实现。
>
> **UPS 模块内部 N+1：** I400C45（9395XR-600）与 L1240C45（9395XR-1500）内置 UPS 模块支持单模块故障不影响运行；I400C40 / I200C20 / L1800C45 / L450C20 的 UPS 外置，客户按此原则选型。但这都不是 IT Zone 级别的冗余设计。
>
> **浸没槽内是 2N。** 每个 [[I50TS]] 槽配双 CDU 2N —— 泵或 CDU 可不排液更换，单点失效不停机。但这是槽级冷却冗余，**不是 IT 冗余**。

参考：[[ATS|AGENTS/ATS]]（Architecture Workflow, Step 3）

---

## 9. 交付周期

| 项 | 值 | 承诺性质 |
|------|------|---------|
| **首批交期** | **下单后 120 天 EXW** | ✅ 承诺 |
| **Scale（扩容批次）** | **90 天 EXW** | ✅ 承诺 |
| **假负载运行期** | **5–30 天** —— 先以假负载跑通供电与冷却链，再上真实算力（Supermicro 建议） | ⚠️ 不含在 EXW 承诺内 |
| 商务 / 运输 / 安装 | **不予承诺** | ❌ |

> **只承诺 EXW。** 商务周期、运输清关、现场安装三段一律不给天数、不给区间、不做估算，客户追问按 [[CLAUDE.md]] §5 转商务团队。
> 旧口径「185–230 天含物流」与「制造 90–120 天」等阶段拆解已于 2026-08-30 作废。

> ⚠️ **以上为单个集装箱单元参考周期。** MDC 集群（多台集装箱）因可并行制造，实际总周期与单台接近。详细周期需根据具体项目规模确认。

---

## 10. 网络 Zone 配置

网络设备由外部集成商提供（如"引澜"等），MDC 提供标准机柜空间和电源接口。

参考：[[PRODUCTS_NETWORK|KB/PRODUCTS_NETWORK]]

---

## 11. 设计原则

- **模块独立**：每个集装箱独立配置、独立运行
- **并联扩展**：通过增加集装箱数量实现容量扩展
- **分区消防**：每个集装箱独立消防系统
- **冗余供电**：I400C45 / L1240C45 的 UPS 及电池内置；I400C40 / I200C20 / L1800C45 / L450C20 的 UPS 及电池外置（客户自备）；BESS / 发电机属 Power Zone

---

## 12. Power Flow

```
Grid Utility
    ↓
Transformer
    ↓
Switchgear / Breaker
    ↓
[BESS] ← 可选，Grid 不稳定或需要削峰时配置
    ↓
IT Zone（L1240C45 / L1800C45 / L450C20 / I400C45 / I400C40 / I200C20）
    ├── PDC
    ├── UPS (EATON 9395XR) ← 仅箱内 UPS 的 SKU；其余在箱外
    ├── CDU / 冷板 Manifold / 浸没槽
    └── 服务器负载
    ↓
Cooling Zone (Hybrid Cooling System)
```

---

## Changelog

| 版本 | 日期 | 变更 |
|---|---|---|
| V2.0 | 2026-08-30 | 六 SKU 对齐。§1 Zone 定义、§2/§12 架构图、§3 IT Zone 产品对照（补 L1800C45/L450C20/I200C20 三行 + 三版 Tech Spec 入口）、§4 最小节点配置、§6 冷却 Zone（按线区分冷源并挂入已批机型）、§8 冗余（补槽内 2N）、§9 交期（⛔ 标记）、§11 设计原则 全部换新码；接入 [[PRODUCT_SPEC_BASELINE]] 与 [[UNCONFIRMED_Convention]] |
| V1.1 | 2026-03-29 | 统一结构版 |

---

*Document Version: V2.0 | Last Updated: 2026-08-30*
