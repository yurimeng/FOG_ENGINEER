---
tags:
  - "#MDC"
  - "#type/reference"
  - "#product/general"
  - "#unconfirmed"
doc_version: v2.0
updated: 2026-08-30
audience: 销售 / 方案架构师 / 客户经理 / AM
---
# MDC 产品速查

> **用途：** 在六个 SKU 之间快速做选型判断。**这是导航表，不是规格表** —— 任何参数以 [[PRODUCT_SPEC_BASELINE]] 为准，与本表冲突时以基准表为准。
>
> **命名基准：** [[NAMING_MAP]]。旧名 DC45 / AC45 / AC40 / AC20 / A32 已全部退役，仅在历史档案、项目记录与供应商往来中保留。 ^mdc-cb4e3429a0
>
> **置信度标记：** ✅ 已确认 · 🔶 derived · ⏳ [[UNCONFIRMED_Convention|#unconfirmed]] · ⛔ conflict

---

## 1. 第一个岔路口：GPU 形态决定产品线

**这是唯一不能搞错的一步。**

| GPU 形态 | 产品线 | 为什么 |
|---|---|---|
| **PCIe** 推理卡（4090 / 5090 / RTX PRO 6000 / H100 / H200 PCIe） | **Immersion Cooling** | PCIe 板卡的热量摊在整张卡上 —— VRM、NIC 和 GPU 一样烫。把整台服务器泡进去，才不用为每个上架的 SKU 单独设计冷板 |
| **SXM / OAM / NVLink** 训练卡（GB300 NVL72 · B300 HGX） | **Liquid Cooling** | 热量集中在 GPU 封装上，其余板载器件次要。冷板是从封装到水最短的路径 |

> 站点原话：*"PCIe runs immersion; SXM and OAM run liquid."*
> **如果客户的机队是 SXM / NVLink，浸没线到此为止，直接转液冷。** 反之亦然。

---

## 2. Liquid Cooling 线（`L`）—— 三个 SKU

| 维度 | **L1240C45** | **L1800C45** | **L450C20** ^mdc-bbef1d38ea |
|---|---|---|---|
| 全 SKU ID | `L1240C45SUR150` | `L1800C45DR220` | `L450C20DR150` ^mdc-f10a6a5acf |
| IT 容量 | **1240 kW** | **1800 kW** | **450 kW** |
| 箱型 | 45ft High Cube | 45ft High Cube | 20ft ⏳ 标准箱/HC 未确认 |
| 单柜密度 | 150 kW（R150） | **220 kW（R220）** ← 全线天花板 | 150 kW（R150） |
| 环路 | 单环路 · TCS 26 °C 暖水 | 双环路 · GPU 进水 **36–40 °C** + 列间 10/15 °C | 双环路 · GPU 进水 **36–40 °C** + 列间 10/15 °C |
| 末端 | **CRAH 吊顶** 9× OHS-084-DG-FC | **列间** 2× CRS 560 CW + 6× CRS 320 CW<br>净 296.0 kW · 风机 34.8 kW · 62,600 m³/h | **列间** 4× CRS 320 CW<br>净 116.4 kW · 风机 18.0 kW · 24,400 m³/h |
| UPS | **箱内**（UPS + 电池） | 箱外 | 箱外 |
| 机柜 | 8× 150 kW 液冷 + 1× 40 kW 风冷 | 8× 220 kW 液冷 + 1× 40 kW 风冷 | 3× 150 kW 液冷，无风冷柜 |
| PUE | `1.0x` —— 逐站点用 <https://mdcx.org> 计算 | `1.0x` | `1.0x` |
| 状态 | shipped | shipped | shipped |

### 怎么选

| 场地情况 | 选 | 理由 |
|---|---|---|
| **一块空地，只有一路进线** | **L1240C45** | 全线唯一把 UPS 和电池装进算力箱的型号。你接的是市电、水和网，不是一套配电工程 ^mdc-ed2fe35ce2 |
| **地不够了，电够** | **L1800C45** | 同样 45ft 壳子多装 560 kW IT、每柜多 70 kW。不含 UPS 不是缺件 —— 场站已经为电付过一次 ^mdc-2c27424576 |
| **45ft 进不去** | **L450C20** | 20ft 那扇还能进得去的门。每 kW 比 45ft 贵，这是为塞进舱位付的价钱，不是产品降级 ^mdc-23795a4d0c |

> **一个前置问题：场地能否许可锂电池置于算力箱体内？** 不能的地方边界就划到箱外（L1800C45 / L450C20）。**这是地方主管部门判定，不是技术判定，也不是降级。** ^mdc-e34573345b

---

## 3. Immersion Cooling 线（`I`）—— 三个 SKU

| 维度 | **I400C45** | **I400C40** | **I200C20** ^mdc-323898124b |
|---|---|---|---|
| 全 SKU ID | `I400C45SUT50` | `I400C40ST50` | `I200C20ST50` ^mdc-44de42f68d |
| IT 容量 | **400 kW**（推荐 360 kW） | **400 kW**（推荐 360 kW） | **200 kW**（推荐 180 kW） |
| 箱型 | 45ft（含专用电力舱） | 40ft | 20ft 算力舱 |
| 槽体 | 8× [[I50TS]] + 1× 10 kW 风冷柜 | 8× [[I50TS]] + 1× 10 kW 风冷柜 | 4× [[I50TS]] + 1× 5 kW 风冷柜 ^mdc-97bcb001c6 |
| 单槽密度 | 50 kW（T50） | 50 kW（T50） | 50 kW（T50） |
| GPU 数上限 | 512 张 PCIe | 512 张 PCIe | 256 张 PCIe ⛔ 见基准表 KC-6 |
| UPS | **箱内** 600 kW · ~20 min | 箱外（客户自备）· ~10 min | 箱外 |
| UL | ✅ compliant | ❌ 不提供 | ❌ 不提供 |
| PUE | `1.0x` —— 逐站点用 <https://mdcx.org> 计算 | 同左 | 同左 |
| 状态 | shipped | shipped | shipped |

### 怎么选

| 场地情况 | 选 | 理由 |
|---|---|---|
| **场地没有配电，且允许锂电进箱** | **I400C45** | 完整推理包：八槽 + UPS + 电池一起落地，一个 SKU 而不是"算力箱 + 一个院子里的配电工程" ^mdc-c17f52f9da |
| **场地已有配电，或锂电不许进箱** | **I400C40** | 同样八槽核心，短五英尺 —— 那五英尺就是电力舱。场站已经为电付过一次，箱子不再收第二次 ^mdc-b33c5494cb |
| **40/45ft 都进不去** | **I200C20** | 20ft 四槽边缘推理舱 ^mdc-7f90d7ba7c |

> ⚠️ **I400C45 与 I400C40 的差别只有电力边界和那五英尺。** 八槽核心、油回路、冷却规则完全相同。 ^mdc-fe0e9a9485
>
> ⚠️ **I200C20 不是 I400 的减半版。** 同 T50 密度、一半槽数，为进不了 40/45ft 的场地而造。**不要用"缩小版""半配置""半价"对客描述。** ^mdc-8f6bfd6e1c

---

## 4. 六 SKU 横向速查

| SKU | 线 | IT kW | 尺寸 | 密度 | UPS | 一句话定位 |
|---|---|---|---|---|---|---|
| L1240C45 | Liquid | 1240 | 45ft | 150 kW/柜 | 内置 | 空地起步，电也一起给你 ^mdc-b9c988286e |
| L1800C45 | Liquid | 1800 | 45ft | **220 kW/柜** | 外置 | 缺地不缺电时的密度天花板 ^mdc-30cc7bb676 |
| L450C20 | Liquid | 450 | 20ft | 150 kW/柜 | 外置 | 还能进得去的那扇门 ^mdc-9a4d0201e2 |
| I400C45 | Immersion | 400 | 45ft | 50 kW/槽 | 内置 | 完整推理包 ^mdc-f54e772dfa |
| I400C40 | Immersion | 400 | 40ft | 50 kW/槽 | 外置 | 你自己的电力架构 ^mdc-92d493cdef |
| I200C20 | Immersion | 200 | 20ft | 50 kW/槽 | 外置 | 边缘推理舱 ^mdc-48e0e02649 |

---

## 5. 对客时最容易出错的四件事

**1. IT Load ≠ Total Facility Load。**
客户说「我要 X MW」时**必须先问是哪一个**（[[CLAUDE.md]] Hard Rule 5）。表里的 kW 都是 IT 负荷 —— 服务器实际用电。计入冷却与辅助后设施总负荷更高，差值由 PUE 决定，而 PUE 取决于站点气候。区间见 [[PRODUCT_SPEC_BASELINE#^baseline-it-vs-facility|基准表 §3.4]]。

**2. PUE 一律写 `1.0x`，不给数。**
六个 SKU 都不存在统一 PUE 值 —— 由场地气候决定，必须逐站点算。对客给计算入口 <https://mdcx.org>，**不给数字**。定性可以说：干冷器能全年排热的气候落在低端，更热站点加混合冷机后上移。**写死任何 PUE 数值都是错的。**

**3. 冗余靠加箱数，不靠箱内。**
集装箱是最小冗余单元。浸没槽内冷却是 2N，但**单箱不设 IT 冗余**；系统级 N / N+1 / 2N 通过增加集装箱实现。

**4. 交期口径未统一。** ⛔
站点 90 天 EXW（运费买方自理）与 KB 的 185–230 天（含物流到场）不是同一量纲，尚未裁定（[[PRODUCT_SPEC_BASELINE#^baseline-conflicts|基准表 C-8]]）。**裁定前不要单独报任一数字**，按 [[CLAUDE.md]] §5 从商务模板读取。

> **价格：** 配置方案由 MDCX 工程团队提供，价格由商务团队核算。请联系客户经理获取正式报价。

---

## 6. 产品文档入口

| SKU | KB 工程入口 | 对外 Tech Spec |
|---|---|---|
| L1240C45 | [[KB/LIQUID/L1240C45/index\|LIQUID/L1240C45/]] | [[L1240C45_Tech_Spec_CN\|CN]] · [[L1240C45_Tech_Spec_EN\|EN]] · [[L1240C45_Tech_Spec_External\|对外版]] ^mdc-c7155cfe6b |
| L1800C45 | [[KB/LIQUID/L1800C45/index\|LIQUID/L1800C45/]] | [[L1800C45_Tech_Spec_CN\|CN]] · [[L1800C45_Tech_Spec_EN\|EN]] · [[L1800C45_Tech_Spec_External\|对外版]] ^mdc-b8e20705e1 |
| L450C20 | [[KB/LIQUID/L450C20/index\|LIQUID/L450C20/]] | [[L450C20_Tech_Spec_CN\|CN]] · [[L450C20_Tech_Spec_EN\|EN]] · [[L450C20_Tech_Spec_External\|对外版]] ^mdc-0712820d82 |
| I400C45 | [[KB/IMMERSION/I400C45/index\|IMMERSION/I400C45/]] | [[I400C45_Tech_Spec_CN\|CN]] · [[I400C45_Tech_Spec_EN\|EN]] · [[I400C45_Tech_Spec_External\|对外版]] ^mdc-6e891f2c03 |
| I400C40 | [[KB/IMMERSION/I400C40/index\|IMMERSION/I400C40/]] | [[I400C40_Tech_Spec_CN\|CN]] · [[I400C40_Tech_Spec_EN\|EN]] · [[I400C40_Tech_Spec_External\|对外版]] ^mdc-fcb8573434 |
| I200C20 | [[KB/IMMERSION/I200C20/index\|IMMERSION/I200C20/]] | [[I200C20_Tech_Spec_CN\|CN]] · [[I200C20_Tech_Spec_EN\|EN]] · [[I200C20_Tech_Spec_External\|对外版]] ^mdc-d243f8b563 |
| I50TS（槽体组件） | [[KB/IMMERSION/I50TS/index\|IMMERSION/I50TS/]] | [[PUBLIC/Products/I50TS\|I50TS]] ^mdc-c7cb121549 |

> **对外版是唯一可直接发给客户的版本** —— 只保留 ✅ 与 🔶 字段，⏳ 与 ⛔ 整行删除。CN / EN 版含待证实字段，**不得整份外发**。见 [[UNCONFIRMED_Convention#^unconfirmed-external|标注规范 §5]]。

---

## Changelog

| 版本 | 日期 | 变更 |
|---|---|---|
| v2.1 | 2026-08-30 | 传导四条裁定（温位 36–40 / PUE `1.0x` / 交期 120·90 EXW + 假负载期 / 质保一年）并吸收站点 Designer 确定值（机柜构成、风冷柜、UL、推荐容量、GPU 上限） |
| v2.0 | 2026-08-30 | 全量重写。原表只覆盖 AC40 / AC45 / DC45 三个旧名平台并自带 8×155 vs 8×150 的 IT 容量冲突 —— 该冲突随旧表一并废止，现表统一取基准表的 8×150 + 1×40。改为六 SKU 两线结构；新增 §1 GPU 形态决策岔路、§5 对客四大易错点、§6 三版文档入口；全表接入置信度标记并指向 [[PRODUCT_SPEC_BASELINE]] |
| v1.0 | 2026-05-31 | 初版（AC40 / AC45 / DC45 三平台对比） |
