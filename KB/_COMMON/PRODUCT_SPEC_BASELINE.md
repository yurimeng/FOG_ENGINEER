---
tags:
  - "#workspace/engineer"
  - "#type/reference"
  - "#type/design-spec"
  - "#product/general"
  - "#unconfirmed"
  - "#MDC"
doc_version: v2.1
updated: 2026-08-30
audience: 全体 Agent + 人（工程 / 售前 / ATS / AM）
status: 现行基准
source_of_truth:
  - "MDC 站点仓库 docs/PRODUCT-MATRIX.md（Locked · D-13 · §5 change log 2026-08-27）"
  - "MDC 站点仓库 docs/rules/NAMING.md（Locked · D-11）"
  - "MDC 站点仓库 llms-full.txt（对客页面全文，2026-08-28 生成）"
  - "MDC 站点仓库 DLC/src/data/profiles/*.json 与 Immer/src/data/containers/*.json（Designer 数据层，2026-08-30 审计）"
  - "MDC 站点仓库 TCO/public/tco-power.js（计算引擎口径，2026-08-30 审计）"
---

# 六 SKU 规格基准表

> **这份文档的角色：** vault 内所有产品文档（Tech Spec CN/EN/External、Quick Ref、PRODUCTS_MDC、Reference Architecture、Guideline 产品速查）的**唯一上游数据源**。任何一处产品数值与本表不符，以本表为准；本表与站点仓库不符，以站点仓库为准。
>
> **本表不定义 SKU。** SKU 码与状态由站点 `docs/PRODUCT-MATRIX.md` 拥有，KB 侧在 [[NAMING_MAP]] 做映射。见 [[CLAUDE.md]] Hard Rule 2。
>
> **置信度标记含义见 [[UNCONFIRMED_Convention]] §2**：✅ 已确认 · 🔶 derived 我方推导 · ⏳ #unconfirmed 待证实 · ⛔ conflict 源冲突。本表带文档级 `#unconfirmed`。
>
> **裁定状态：** 2026-08-30 Yuri 裁定关闭 5 条（KC-1 / KC-2 / KC-8 / KC-9 + CW330 归属），**剩余 5 条未裁定**（KC-3 / KC-4 / KC-5 / KC-6 / KC-7），见 [[#6. 冲突登记簿|§6]]。对客前必查该节。

## 0. 六 SKU 一览

| 短别名 | 全 SKU ID | 线 | IT kW | 尺寸 | 环路 | UPS | 密度 | 状态 |
|---|---|---|---|---|---|---|---|---|
| **L1240C45** | `L1240C45SUR150` | Liquid | 1240 | 45ft HC | S | 内置 | R150 | shipped ✅ |
| **L1800C45** | `L1800C45DR220` | Liquid | 1800 | 45ft HC | D | 外置 | R220 | shipped ✅ |
| **L450C20** | `L450C20DR150` | Liquid | 450 | 20ft | D | 外置 | R150 | shipped ✅ |
| **I400C45** | `I400C45SUT50` | Immersion | 400 | 45ft | S | 内置 | T50 | shipped ✅ |
| **I400C40** | `I400C40ST50` | Immersion | 400 | 40ft | S | 外置 | T50 | shipped ✅ |
| **I200C20** | `I200C20ST50` | Immersion | 200 | 20ft | S | 外置 | T50 | shipped ✅ |

> **六个 SKU 全部 `shipped`。** 站点 2026-08-27 D-19 gate 一次性放行 I200C20 / L1800C45 / L450C20 三个原 draft SKU。
>
> [[I50TS]]（`I50TS`，旧称 A32）是浸没槽体**组件**，不是 SKU，不进本表。它是 I400C45 / I400C40 的 8× 与 I200C20 的 4× 构成单元。**该码为 KB 侧按 Tank 正则推导** ⏳ **#unconfirmed** —— 等站点侧写入 `PRODUCT-MATRIX.md` Alias registry，预期 TBD。见 [[#9. 未裁定冲突登记簿|§6 · KC-7]]。

^baseline-overview

## 1. Liquid Cooling 线

### 1.1 容量与密度

| 字段 | L1240C45 | L1800C45 | L450C20 | 置信度 |
|---|---|---|---|---|
| IT 容量 | 1240 kW | 1800 kW | 450 kW | ✅ 站点 |
| 机柜构成 | 8× 150 kW 液冷 + 1× 40 kW 风冷 = 9 柜 | **8× 220 kW 液冷 + 1× 40 kW 风冷 = 9 柜** | **3× 150 kW 液冷，无风冷柜 = 3 柜** | ✅ 站点 Designer profile |
| 单柜密度 | 150 kW（R150） | 220 kW（R220） | 150 kW（R150） | ✅ 站点 |
| GPU 平台 | GB300 NVL72 · B300 HGX（SXM / NVLink） | GB300 NVL72 · B300 HGX | ⏳ **#unconfirmed** | ✅ 站点（仅 L1240/L1800 披露） |

> ✅ **2026-08-30 站点审计已取到确定值**，来源 `DLC/src/data/profiles/l1800.json` · `l450.json` 与 `packages/scene/src/tables.ts`。原 ⏳ 关闭。
> **注意 L450C20 没有风冷柜** —— 与两个 45ft 液冷 SKU 不同，站点 `TCO/public/tco-power.js` 的风冷柜常量对它是 0。
>
> ⚠️ **不要把项目文档里的柜位数当产品规格。** `Projects/` 下按项目容积规划的"柜位/仓"数与产品机柜数不是同一量纲，两者只隔一个 wikilink，极易误引。

### 1.2 冷却架构

| 字段 | L1240C45 | L1800C45 | L450C20 | 置信度 |
|---|---|---|---|---|
| 环路数 | 单环路 | 双环路 | 双环路 | ✅ 站点 |
| GPU 侧进水温位 | TCS 26 °C 暖水单点（KB 工程口径 26–28 °C） | **36–40 °C** ✅ 裁定 | **36–40 °C** ✅ 裁定 | ✅ |
| 外冷源一次侧出水（FWS 进 CDU） | 站点 EG · 22 °C | **32–36 °C** ✅ 裁定 | **32–36 °C** ✅ 裁定 | ✅ |
| CDU 温升（approach） | ≥4 °C（[[CDU_Requirement V5]]） | **+4 °C** ✅ 裁定 | **+4 °C** ✅ 裁定 | ✅ |
| CRAH 侧温位 | 无独立 CRAH 环路（Branch 3 走 TCS 冷凝） | **10 / 16 °C 冷冻水** | **10 / 16 °C 冷冻水** | ✅ 站点 |
| 二次侧介质 | **PG25**（25% 丙二醇） | **纯水 0%** | ⏳ **#unconfirmed** —— 等 L450C20 DESIGN 或 CW330 选型书，预期 TBD | ✅ KB / ✅ 选型书 / ⏳ |
| 末端构成 | 冷板 + 9× RDHX + 9× 顶置 DX | 冷板 + CW 型 CRAH | ⏳ **#unconfirmed** —— 等 L450C20 DESIGN，预期 TBD | ✅ KB / ✅ 选型书 / ⏳ |
| CDU 选型 | ≥1500 kW（[[CDU_Requirement V5]]，**未定型号**，状态见 §4）⛔ 见 KC-10 | **STULZ SCR 14103 W** ✅ ATS approved | **STULZ SCR 14103 W** ✅ 站点 profile | ⛔ / ✅ / ✅ |
| CRAH 选型 | 9× STULZ OHS-084-DG-FC（**⏳ 正在 review**，CE / 50 Hz 阻塞）⛔ 见 KC-10 | **STULZ CRS 560 CW**（CW560）✅ ATS approved | **STULZ CRS 330 CW**（CW330）✅ 归属已定 · ⏳ 规格待厂家（2026-08-31），见 [[PRD-STULZ-CW330]] | ⛔ / ✅ / ✅ |
| **CDU / CRAH 台数与冗余** | CDU 1 台（≥1500 kW）· CRAH 9 台（N，无 N+1） | **CDU 2× SCR 14103 W · CRAH 4× CRS 560 CW** | **CDU 1× SCR 14103 W · CRAH 2× CRS 330 CW（N+1）** | ✅ 站点 Designer profile |
| 室外侧排热基线 | ≥1700 kW | ⏳ **#unconfirmed** —— 等 L1800C45 DESIGN，预期 TBD | ⏳ **#unconfirmed** —— 等 L450C20 DESIGN，预期 TBD | ✅ KB / ⏳ / ⏳ |
| PUE | **1.0x** —— 不给固定值，随场地环境计算（[[#^baseline-pue\|见 §2.2 裁定]]） | **1.0x** | **1.0x** | ✅ 裁定 |

> ## 双环路 GPU 侧温位链（2026-08-30 Yuri 裁定 · 关闭 KC-1）
>
> ```
> 外冷源（干冷器）出水  32–36 °C
>         ↓  进 CDU 一次侧（FWS）
>      CDU 板换 approach  +4 °C
>         ↓  出 CDU 二次侧（TCS）
>   GPU 冷板进水  36–40 °C
> ```
>
> **这条链同时适用 L1800C45 与 L450C20**（两者均为双环路、无 UPS 的 DLC 解决方案）。
>
> **与已批 STULZ SCR 14103 W 选型书的对应关系：** 选型书取该带的**热端设计点** —— FWS 36 °C 进 / 46 °C 出，TCS 40 °C 供 / 50 °C 回，approach 恰为 4 °C，与本裁定完全一致。选型书不是另一套温位，是同一条链在最不利工况下的取值。
>
> ⚠️ **站点对客页目前写「GPU 36–45 °C」，与本裁定不符。** 上限 45 应为 40。这是工程参数（Yuri 所有），不是 SKU 码（站点所有），故以本表为准；**需回站点仓库修正三处液冷页面文案**，见 §5 反向同步。

> **L1240C45 与另两个 SKU 的冷却基线不可互换。** [[CDU_Requirement V5]]（FWS 22/32 · TCS 26/36 · PG25 · DN100 法兰）与 [[CRAH_Requirement V5]]（自含式 DX · PG25 冷凝）的 scope **只覆盖 L1240C45**。L1800C45 温位整体高约 14 K、介质为纯水、接口为 Tri-Clamp。详见 [[PRD-STULZ-SCR14103W]] §4 与 [[PRD-STULZ-CRS560CW]] §4。
>
> ✅ **CDU / CRAH 台数与冗余于 2026-08-30 站点审计取到确定值**（`DLC/src/data/profiles/l1800.json:25-28` · `l450.json:25-28`）。[[PRD-STULZ-SCR14103W]] Q1 与 [[PRD-STULZ-CW330]] Q5 据此关闭。
>
> **L1800C45 / L450C20 仍没有专属 CRAH / CDU Requirement。** 两个 SKU 的冷却侧只有 PRD 与站点 profile，**没有需求书基线**。这是当前最大的工程文档缺口 —— 两者共用同一条温位链与同一 CRAH 侧 10/16 °C 回路，可以合并成一份覆盖「无 UPS 的 DLC 解决方案」的 `CRAH_Requirement V6` + `CDU_Requirement V6`。

^baseline-liquid-cooling

### 1.3 电力

| 字段 | L1240C45 | L1800C45 | L450C20 | 置信度 |
|---|---|---|---|---|
| UPS 边界 | **箱内**（UPS + 电池） | **箱外**（UPS / 电池 / PDC 由场站提供） | **箱外** | ✅ 站点 |
| UPS 型号 | EATON 9395XR-1500（1500 kW） | 不适用 | 不适用 | ✅ KB |
| 电池后备 | ~8 min（3× 93LiG2） | 不适用 | 不适用 | ✅ KB |
| 母线 | SIEMENS 2500A 封闭插接式 | ⏳ **#unconfirmed** —— 等 DESIGN/BOM，预期 TBD | ⏳ **#unconfirmed** —— 同左 | ✅ KB / ⏳ / ⏳ |
| 供电制式 | 380 / 400 / 415 / 480 V AC | 同左 | 同左 | ✅ 站点 |

> **800 V HVDC 今日不供货。** 站点 FAQ 明确：380/400/415/480 V AC 为在售制式，800 V HVDC 属 Roadmap Q3 2026。**不得对客承诺。**
>
> **Roadmap：** 独立 MDCX 电源模块（UPS / 电池 / PDC）在研，面向边界必须在箱外的场站。站点三个液冷产品页均已披露。
>
> **箱外 UPS 是配置，不是降级。** 站点原话：*"the boundary moves outside the box — and that's a configuration, not a downgrade."* 触发条件通常是场地能否许可锂电池进入算力箱体，属地方主管部门判定，不是技术判定。

### 1.4 结构

| 字段 | L1240C45 | L1800C45 | L450C20 | 置信度 |
|---|---|---|---|---|
| 箱型 | 45ft High Cube | 45ft High Cube | 20ft ⏳ **标准箱还是 High Cube 未确认** | ✅ / ✅ / ⏳ |
| 外形尺寸 | 13,716 × 2,438 × 2,992 mm | ⏳ **#unconfirmed** —— 见下注 | ⏳ **#unconfirmed** —— 见下注 | ✅ KB / ⏳ / ⏳ |
| 空箱重 | ~16 T | ⏳ **#unconfirmed** —— 等 DESIGN，预期 TBD | ⏳ **#unconfirmed** —— 同左 | ✅ KB / ⏳ / ⏳ |
| 满载重 | ~20–25 T | ⏳ **#unconfirmed** —— 同左 | ⏳ **#unconfirmed** —— 同左 | ✅ KB / ⏳ / ⏳ |

> ⏳ **L1800C45 外形不可简单套用 L1240C45。** 虽同为 45ft HC，但 [[KB/LIQUID/L1800C45/index|L1800C45 index]] 记载**上部模块已由 600 抬高至 900 mm**（一次侧互联总管内收）。该 900 mm 是箱内净高还是影响外廓，文档未说明。在澄清前**不得**引用 13,716 × 2,438 × 2,992 mm 作为 L1800C45 规格。等 Layout Planner 确认，预期 TBD。
>
> ⏳ **L450C20 的 20ft 标准箱 vs High Cube 是本表最具决策价值的缺口。** 该 SKU 的全部价值主张就是"45ft 进不去的舱位它能进"，而标准箱与 HC 的高度差 305 mm（2,591 vs 2,896 mm）直接决定能否进场。**不得**引用 ISO 名义值 6,058 × 2,438 × 2,591 mm。等站点 Designer profile 或 DESIGN 文档，预期 TBD。

## 2. Immersion Cooling 线

### 2.1 容量与密度

| 字段 | I400C45 | I400C40 | I200C20 | 置信度 |
|---|---|---|---|---|
| IT 容量 | 400 kW（**推荐 360 kW** / 上限 400 kW） | 400 kW（**推荐 360 kW** / 上限 400 kW） | 200 kW（**推荐 180 kW** / 上限 200 kW） | ✅ 站点 Designer |
| 槽体 | 8× [[I50TS]] + 1× 10 kW 风冷柜 | 8× [[I50TS]] + 1× 10 kW 风冷柜 | 4× [[I50TS]] + 1× **5 kW** 风冷柜 | ✅ 站点 Designer |
| 单槽密度 | 50 kW（T50） | 50 kW（T50） | 50 kW（T50） | ✅ 站点 |
| GPU 数上限 | 512 张 PCIe | 512 张 PCIe | **256 张 PCIe** ⛔ 见 KC-6（站点已对客发布，KB 原禁止外发） | ✅ / ✅ / ⛔ |
| GPU 平台 | 4090 · 5090 · RTX PRO 6000 Blackwell SE · H100 · H200（PCIe 4U 8-GPU） | 同左 | 4090 · 5090 · RTX PRO 6000 · H100 · H200（PCIe） | ✅ 站点 |

> ✅ **风冷柜不计入 IT 容量**（2026-08-30 站点审计关闭原 KC-3）。站点计算引擎 `TCO/public/tco-power.js:24-25` 明写：*"Immersion air racks are facility, not IT (itCapacity_kW.max == tanks × 50)"* —— 风冷柜算设施负荷，IT 容量 = 槽数 × 50 kW。
> 即：I400C45 / I400C40 = 8 × 50 = 400 kW IT，另有 10 kW 风冷柜计入设施侧；I200C20 = 4 × 50 = 200 kW IT，另有 5 kW 风冷柜。**进线容量申请须按 IT + 设施合计，不能只报 IT。**

### 2.2 冷却架构

| 字段 | I400C45 | I400C40 | I200C20 | 置信度 |
|---|---|---|---|---|
| 方式 | 单相浸没 | 单相浸没 | 单相浸没 | ✅ 站点 |
| 槽内 CDU | 双 CDU · 2N | 双 CDU · 2N | 双 CDU · 2N | ✅ 站点 |
| 设施水温位 | 32 / 37 °C 暖水 | ⏳ **#unconfirmed** —— 核心相同，推同温位属 🔶 derived；等 Cooling Engineer 确认，预期 TBD | ⏳ **#unconfirmed** —— 同左 | ✅（仅 I400C45 披露）/ ⏳ / ⏳ |
| 油侧 ΔT | 8 K | 8 K | 8 K | ✅ 站点 |
| 单槽油流量 | ≈11–12 m³/h | ≈11–12 m³/h | ≈11–12 m³/h | ✅ 站点 |
| 整箱二次侧流量 | ≈88–96 m³/h 🔶 derived（11–12 × 8 槽，**设计值**） | ≈88–96 m³/h 🔶 derived | ≈44–48 m³/h 🔶 derived（11–12 × 4 槽） | 🔶 |
| PUE | **1.0x** —— 不给固定值，随场地环境计算 | 同左 | 同左 | ✅ 裁定 |
| 冷源 | 干冷器为主；峰值站点加 Hybrid Chiller | 同左 | 同左 | ✅ 站点 |

> ## PUE 一律写 `1.0x`（2026-08-30 Yuri 裁定 · 关闭 KC-2）
>
> **浸没线 PUE 不存在统一数值。** 最终值由场地环境决定，**必须逐站点计算**。
>
> - **对内 / 对客一律写 `1.0x`**，不写 1.05、不写区间、不写"典型值"。
> - **计算入口：** <https://mdcx.org> 的 TCO / Designer —— 输入站点气候条件后得出该站点的 PUE。对客时给这个链接，不给数字。
> - 定性可说：干冷器可全年排热的气候落在低端；更热的站点需加混合冷机，PUE 相应上移。**但不给具体数。**
>
> **任何一处写死 PUE 数值都是错的**，等同违反 [[CLAUDE.md]] Hard Rule 5（IT vs Facility 口径混淆）。液冷线同理 —— L1240C45 现载的 1.15–1.20 亦按 `1.0x` 口径处理，见 §1.2。

^baseline-pue

^baseline-immersion-cooling

### 2.3 电力

| 字段 | I400C45 | I400C40 | I200C20 | 置信度 |
|---|---|---|---|---|
| UPS 边界 | **箱内**（45ft 专用电力舱） | **箱外**（客户自备） | **箱外** | ✅ 站点 |
| UPS 容量 | 600 kW · EATON | 600 kW（**客户自备**） | 不适用 | ✅ 站点 |
| 电池后备 | ~20 min（内置，2× 93LiG2） | ~10 min（客户自备） | ⏳ **#unconfirmed** —— 等 DESIGN，预期 TBD | ✅ / ✅ / ⏳ |
| UL 合规 | ✅ UL compliant（站点 `ulCompliant: true`） | **❌ 不提供**（站点 `ac40.json:22` `ulCompliant: false`，明确否定而非未披露） | **❌ 不提供**（站点 `ac20.json` 同为 false） | ✅ 站点 Designer |
| **供电制式** | ⏳ **#unconfirmed** | ⏳ **#unconfirmed** | ⏳ **#unconfirmed** | ⏳ |

> ⏳ **浸没线三个 SKU 没有任何已确认的进线电压。** §1.3 那行 380/400/415/480 V AC 的站点依据只覆盖液冷线。这是客户第一页就会问的问题。等 Power Engineer 或站点补充，预期 TBD。
>
> ⛔ **注意 UPS 归属易错点：** 600 kW 箱内 UPS 属 **I400C45**。I400C40 的 UPS 在箱外、由客户自备。vault 内曾有文档把箱内 600 kW 记到 I400C40 名下（已在 `AGENTS/Power Engineer.md` 修正并留标记）。

### 2.4 结构

| 字段 | I400C45 | I400C40 | I200C20 | 置信度 |
|---|---|---|---|---|
| 箱型 | 45ft（含专用电力舱） | 40ft | 20ft 算力舱 | ✅ 站点 |
| 外形尺寸 | ⏳ **#unconfirmed** | ⏳ **#unconfirmed** —— 既有 Tech Spec 载 12,192 × 2,438 × 2,896 mm，来自 AC40 V1.4 旧基线，未经本表确认 | ⏳ **#unconfirmed** | ⏳ |
| 空箱重 / 满载重 | ⏳ **#unconfirmed** | ⏳ **#unconfirmed** —— 既有 Tech Spec 载 12–16 T / 22–30 T，同上 | ⏳ **#unconfirmed** | ⏳ |

> **I400C45 与 I400C40 的差别只有两项：** 电力边界，以及那五英尺（= 电力舱体积）。八槽核心、油回路、冷却规则完全相同。站点原话：*"They share the same 400 kW, eight-tank core."*
>
> **I200C20 不是 I400 的减半版。** 同 T50 密度、一半槽数（4×），为进不了 40/45ft 的场地而造。**不要用"缩小版""半配置""半价"这类表述对客。**

## 3. 跨 SKU 共用条款

### 3.1 交付（2026-08-30 Yuri 裁定 · 关闭 KC-8）

**只承诺 EXW，其余一律不承诺。**

| 字段 | 值 | 承诺性质 | 置信度 |
|---|---|---|---|
| **首批交期** | **下单后 120 天 EXW** | ✅ **承诺** | ✅ 裁定 |
| **Scale（扩容批次）交期** | **90 天 EXW** | ✅ **承诺** | ✅ 裁定 |
| **假负载运行期** | **5–30 天** —— 以假负载验证供电与冷却链后再上真实算力。来源：**Supermicro 建议** | ⚠️ 不含在 EXW 承诺内 | ✅ 裁定 |
| 商务周期（合同 / 付款 / 采购） | **不予承诺** | ❌ 不承诺 | ✅ 裁定 |
| 运输与清关 | **不予承诺**，买方自理 | ❌ 不承诺 | ✅ 裁定 |
| 现场安装与调试 | **不予承诺** | ❌ 不承诺 | ✅ 裁定 |
| 预制率 | 99% 出厂前完成 | 陈述 | ✅ 站点 |

> ## 交期表述规则
>
> 1. **唯一可承诺的是 EXW 天数**：首批 120 天、Scale 90 天，均自**下单**起算。
> 2. **商务、运输、安装三段一律不承诺**，不给天数、不给区间、不做估算。客户追问按 [[CLAUDE.md]] §5 转商务团队。
> 3. **假负载运行期 5–30 天单独列出**，明确不在 EXW 承诺内。这是 Supermicro 的实践建议：先用假负载跑通供电与冷却链，再装真实 GPU，避免拿客户的算力资产做首次联调。
> 4. **旧口径全部作废**：站点的「90 天 EXW / 满负荷 120 天」、KB Tech Spec 的「185–230 天含物流」、站点四阶段（勘察→制造→海运→安装）均不再引用。
>
> ⚠️ **站点对客页仍写「90 days ex-works, up to 120 when the line is full」与四阶段时间轴**，与本裁定不符 —— 需回站点仓库修正，见 §5 反向同步。
>
> ⏳ 假负载运行期发生在**工厂端还是现场端**未明确 —— 等 ATS 补充，预期 TBD。（不影响承诺口径，两种情形都在 EXW 承诺之外。）

### 3.2 软件与运营

| 字段 | 值 | 置信度 |
|---|---|---|
| CIOS | 每台 MDCX 均含。路径寻址遥测、告警转工单、运维工作流、用量计量；开源核心 Apache-2.0（Roadmap） | ✅ 站点 |
| 数字孪生 | NVIDIA Omniverse，实时状态投射到 3D 模型 | ✅ 站点 |
| DCM | 算力交易市场，**Roadmap · MVP 开发中**。不得作为已交付能力对客承诺 | ✅ 站点 |

### 3.3 可用性、冗余与质保

| 字段 | 值 | 置信度 |
|---|---|---|
| 设计目标 | Tier II 投资，经差异化冗余达到 Tier III 级可用性 | ✅ 站点 |
| 冗余原则 | 失效代价高的地方 2N，其余 N+1 —— **不做全局 2N** | ✅ 站点 |
| 浸没线冗余模型 | 集装箱是最小冗余单元：槽内冷却 2N，单箱不设 IT 冗余，系统级 N / N+1 / 2N 靠增加箱数 | ✅ 站点 |
| 质保背书 | 浸没线由 OEM 背书；Intel DataCenter Certified | ✅ 站点 |
| **质保范围与年限** | **核心部件，自 EXW 起一年** | ✅ 裁定 |
| **后续年份** | **按年收取服务费** | ✅ 裁定 |
| **支持 SLA（ONSITE / NBD / 24×7 等）** | **以 Invoice 为准**，KB 不定义、不承诺 | ✅ 裁定 |

> ## 质保表述规则（2026-08-30 Yuri 裁定 · 关闭 KC-9）
>
> - **可写：** 核心部件 EXW 起一年质保；后续年份按年服务费。
> - **不可写：** 任何具体的响应级别。ONSITE / NBD / 9×5 / 24×7 这类条款**以 Invoice 为准** —— KB 与 Tech Spec 一律不承诺，客户问就转商务。
> - **旧口径作废：** 既有 Tech Spec §12 载的「1 年 / 9×5 NBD」中，**9×5 NBD 部分不再出现**在任何文档里。

### 3.4 IT Load vs Total Facility Load

**这是 [[CLAUDE.md]] Hard Rule 5 的执行口径，任何「X MW」需求必须先澄清指的是哪一个。**

| SKU | IT Load | Total Facility Load | 置信度 |
|---|---|---|---|
| L1240C45 | 1240 kW | 随 PUE 变化，**逐站点用 <https://mdcx.org> 计算** | ✅ 裁定 |
| L1800C45 | 1800 kW | 随 PUE 变化，**逐站点用 <https://mdcx.org> 计算** | ✅ 裁定 |
| L450C20 | 450 kW | 随 PUE 变化，**逐站点用 <https://mdcx.org> 计算** | ✅ 裁定 |
| I400C45 | 400 kW | 随 PUE 变化，**逐站点用 <https://mdcx.org> 计算** | ✅ 裁定 |
| I400C40 | 400 kW | 随 PUE 变化，**逐站点用 <https://mdcx.org> 计算** | ✅ 裁定 |
| I200C20 | 200 kW | 随 PUE 变化，**逐站点用 <https://mdcx.org> 计算** | ✅ 裁定 |

^baseline-it-vs-facility

## 4. 已批第三方冷却设备索引

| SKU | 环路 | 设备 | 型号 | 状态 | 文档 |
|---|---|---|---|---|---|
| **L1800C45** | GPU 侧 | CDU | STULZ SCR 14103 W | ✅ **ATS approved** 2026-08-30 | [[PRD-STULZ-SCR14103W]] |
| **L1800C45** | CRAH 侧 | CW 精密空调 | STULZ CRS 560 CW | ✅ **ATS approved** 2026-08-30 | [[PRD-STULZ-CRS560CW]] |
| **L450C20** | CRAH 侧 | CW 精密空调 | STULZ **CW330** | ✅ **归属已定** 2026-08-30 · ⏳ 规格参数待厂家提供（预期 2026-08-31） | [[PRD-STULZ-CW330]] |
| L1240C45 | Branch 2 | RDHX | VERTIV CoolLoop DCD35 | ⏳ 正在 review（Q1 待 VERTIV） | [[PRD-Vertiv-RDHx]] |
| L1240C45 | Branch 3 | 顶置 DX | STULZ OHS-084-DG-FC | ⏳ 正在 review（**CE / 50 Hz 市场准入阻塞**） | [[PRD-STULZ-CeilAir]] |
| L1240C45 | Branch 3 替代 | 卧式自含水冷 DX | 未定（Vertiv / HiRef / 国产 CE 线） | ⏳ RFQ 阶段 | [[CRAH_Replacement_RFQ_Spec V1]] |
| L1240C45 | 室外侧 | Hybrid Chiller | TICA TAMFV430.3ALF5 | ✅ **ATS Full Pass** 2026-06-11 | [[TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.3]] |

> ## CW 型 CRAH 的产品族归属（2026-08-30 Yuri 裁定）
>
> **CW330 与 CW560（CRS 560 CW）同属「无 UPS 的 DLC 解决方案」族** —— 即 **L1800C45 + L450C20** 这两个双环路、UPS 在箱外的液冷 SKU。CW560 已定 L1800C45，**CW330 归 L450C20**。
>
> 两者共用同一条 GPU 侧温位链（外冷源 32–36 °C → CDU +4 °C → GPU 36–40 °C）与同一 CRAH 侧 10/16 °C 冷冻水回路，差别只在容量档。这也意味着两个 SKU 的 CRAH 侧可以共用一份需求书基线 —— 见 §1.2 末的文档缺口说明。

> **「已批」与「正在 review」不是同一状态，本节是这两个词的唯一裁判。** §1.2 的选型行若与本节冲突，以本节为准。完整准入清单见 [[3rd Party List]] → [[02_Cooling_Zone]]。

## 5. 下游同步清单

修改本表任一数值后，**必须**同步下列文档：

| 文档 | 同步内容 |
|---|---|
| [[CLAUDE.md]] §2 | SKU 列表与状态（**易漏：该文件本身携带产品状态**） |
| [[MDC_Product_Quick_Ref]] | 六 SKU 对比表 |
| [[PRODUCTS_MDC]] | §3 IT Zone 产品对照 · §4 最小节点 · §6 冷却 Zone |
| `PUBLIC/Tech_Spec/<SKU>_Tech_Spec_CN.md` / `_EN.md` | §3 容量 · §5 冷却 · §6 电力 · §12 服务 · §14 汇总 |
| `PUBLIC/Tech_Spec/<SKU>_Tech_Spec_External.md` | 对外输出版（**只含 ✅ 与 🔶**，⏳ 与 ⛔ 整行删除） |
| `PUBLIC/Tech_Spec/_blocks/<SKU>_Tech_Spec_{CN,EN}/*.md` | 块文件与父文件同步（**易漏：L1240C45 与 I400C40 各有 14 个块**） |
| [[KB/LIQUID/index]] · [[KB/IMMERSION/index]] · 各 SKU `index.md` | 状态表与冷却选型节 |
| [[COOLING_SYSTEM_Guideline]] | 产品速查块的 IT Zone 匹配规则 |
| `PUBLIC/Reference_Architecture/RA-*.md` | 参考架构的容量 / PUE / 交期 / 质保（**2026-08-30 曾整组漏更，务必带上**） |
| `PUBLIC/Products/_blocks/PRODUCTS_*/01_*.md` | 产品 PRD 的参数表 |
| [[FOG_Workspace_Summary]] · [[_navigation]] · [[hot]] | 产品线口径 |
| [[NAMING_MAP]] | 仅当 SKU 码或状态变化 |
| 站点仓库 `docs/PRODUCT-MATRIX.md` | **本表永远跟随站点，不反推**（SKU 码与状态由站点拥有） |

### ⚠️ 需回站点仓库修正的三项（本表反向输出）

工程参数由 Yuri 拥有，站点对客文案目前与 2026-08-30 裁定不符，需回 `~/Documents/Fog/Dev.nosync/MDC` 修正：

| # | 站点现状 | 应改为 | 涉及页面 |
|---|---|---|---|
| 1 | 液冷双环路写「GPU 36–45 °C」 | **GPU 36–40 °C** | `liquid-l1800.html` · `liquid-l450.html` · `solutions/liquid` 概览 · `llms-full.txt` |
| 2 | 浸没线写「PUE ≈ 1.05 @ peak dry-bulb ≤ 24 °C」 | **PUE `1.0x`，逐站点用 TCO/Designer 计算** | 三个浸没产品页 + 首页 FAQ |
| 3 | 交期写「90 days EXW, up to 120 when line is full」+ 四阶段时间轴 | **首批 120 天 EXW / Scale 90 天 EXW；商务·运输·安装不承诺；增假负载期 5–30 天** | 首页 Delivery 段 + 全部六个产品页 |

## 6. 冲突登记簿

> ## ⚠️ 编号不要和站点 Claims 台账搞混
>
> - **KB 冲突登记簿用 `KC-n`**（本节）—— 记录"哪些事没定"
> - **站点 Claims 台账用 `Cn`**（`docs/CLAIMS.md`，C1–C46，无连字符）—— 记录"哪些对客数字被授权说、能出现在哪些页面"
>
> 两者编号空间完全独立且含义相反。站点的 `C9` 是液冷 PUE 声明，KB 的 `KC-9` 是质保来源缺失 —— **引用时务必带前缀**。

> 每条都是**不能靠查资料解决、必须由人拍板**的问题。**2026-08-30 Yuri 裁定关闭 4 条（KC-1 / KC-2 / KC-8 / KC-9）**，另关闭 CW330 归属（原 [[PRD-STULZ-CW330]] Q1）。**剩余 5 条待裁。**

### 已裁定

| # | 冲突 | 裁定（2026-08-30 Yuri） |
|---|---|---|
| **KC-1** ✅ | L1800C45 GPU 侧温位：站点 36–45 °C vs 已批 CDU 工况 | **GPU 进水 36–40 °C；外冷源一次侧出水 32–36 °C；CDU approach +4 °C。** STULZ 选型书取该带热端设计点，与裁定一致。站点页 45 应改 40 |
| **KC-2** ✅ | I400C45 的 PUE 与设施负荷不自洽 | **PUE 一律写 `1.0x`**，不给固定值。逐站点用 <https://mdcx.org> 计算。适用全部六 SKU，L1240C45 的 1.15–1.20 亦作废 |
| **KC-8** ✅ | 交期三种并存口径 | **首批 120 天 EXW、Scale 90 天 EXW，自下单起算；商务/运输/安装一律不承诺。** 另增假负载运行期 5–30 天（Supermicro 建议），不含在 EXW 内 |
| **KC-9** ✅ | 质保年限与 SLA 无来源 | **核心部件 EXW 起一年，后续按年服务费。ONSITE / NBD / 24×7 等条款以 Invoice 为准**，KB 不定义 |
| **CW330 归属** ✅ | CW330 属哪个 SKU | **CW330 与 CW560（CRS560CW）同属「无 UPS 的 DLC 解决方案」族** = L1800C45 + L450C20。CW560 已定 L1800C45，**CW330 归 L450C20** |

### 待裁定

| # | 冲突 | 影响面 | 谁来裁 |
|---|---|---|---|
| **KC-6** | **I200C20 GPU 上限 256 已经对客发布，但 KB 原本禁止外发。** 站点 `Immer/src/data/containers/ac20.json:14` 定义 256，`rd-i200c20.html:247` 与 Designer 容器选择器**均已渲染给客户**。KB 此前按从严处理禁止外发。**已发布的数字收不回来 —— 要么 KB 追认，要么站点撤下**，不能两边并存 | 所有 External 版 · 站点 RD 页 | ATS |
| **KC-10** | **站点 L1240C45 profile 的冷却选型与 KB 已批清单打架。** 站点 `DLC/src/data/profiles/dc45.json:21-27` 给 L1240C45 配 `scr14103w`×1 + `crs560cw`×2；KB §4 明确这两台是 **L1800C45 专属已批设备**，L1240C45 的 CDU 是"≥1500 kW 未定型号"、CRAH 是 9× OHS-084-DG-FC（正在 review、CE/50Hz 阻塞）。且站点 `crah/` 目录**根本没有 OHS-084-DG-FC**，而 `packages/scene/src/tables.ts:61` 又写 `CRAH_COUNT_L1240 = 9` | L1240C45 全部冷却文档 + 站点 Designer 出数 | ATS + Cooling Engineer |
| **KC-11** | **L1800C45 二次侧介质两说。** KB §1.2 与已批 STULZ 选型书写**纯水 0%**；站点 `l1800.json:23` provenance 写 **PG45**（ρ 1031, cp 3.67）。介质决定防冻策略与换热计算，不能并存 | L1800C45 冷却计算 · 寒冷站点方案 | Cooling Engineer |
| **KC-12** | **「I200C20 是什么」两套产品定义。** 站点（`ac20.json` + 已发布 RD 页 + 本表 §2.1）= 满配 4 槽 200 kW 出售；KB [[RA-003_Immersion_0.2MW_All-in-One]] = 标配 2 槽 100 kW + 预留 2 位可扩容。**这不是数值差异，是产品定义差异** | I200C20 全部对客材料 · 报价单位 | ATS |
| **KC-13** | **交期起算点两说。** 站点 Claims C3/C4 写 *"from receipt of down payment"*（自收到首付款）；2026-08-30 裁定写"自**下单**起算"。差一个付款动作，直接影响合同违约认定 | 六 SKU §12 · 合同条款 | 商务 + 法务 |
| **KC-14** | **浸没线设施水温位至少四套并存。** 本表 §2.2（I400C45）32/37 °C · [[RA-001_Immersion_0.4MW]] 32–35 / 35–38 °C · [[RA-003_Immersion_0.2MW_All-in-One]] §5.1 FWS 31–33 / 38–40 °C（油侧 35 / 42–45 °C）· 站点 Designer 另有算法 | 三个浸没 SKU 的冷却节 | Cooling Engineer |
| **KC-15** | **L1240C45 冷却末端构成两套。** 本表 §1.2 与 Tech Spec 写「冷板 + 9× RDHX + 9× 顶置 DX」；[[RA-002_Liquid_1.2MW]] §4/§8 写「FCU 12× 40 kW = 480 kW」，且主 CDU 写 1.2 MW 而非 ≥1500 kW（差 300 kW，影响 TOU 整定） | L1240C45 冷却与配电 | ATS + Cooling Engineer |
| **KC-7** | **`I50TS` 码本身是 ⏳，却是三个 ✅ shipped SKU 的构成单元。** 一个不能引用的组件码，让任何浸没 Tech Spec 的槽体规格节都无法写成干净的 ✅ | 三个浸没 SKU 的槽体节 | 站点侧（写入 Alias registry） |

^baseline-conflicts

---

## Changelog

| 版本 | 日期 | 变更 |
|---|---|---|
| **v2.1** | **2026-08-30** | **吸收 MDCX 站点仓库审计结果。** 站点 Designer 数据层已有确定值，按"本表永远跟随站点"规则从 ⏳ 转 ✅：L1800C45 = 8×220 kW 液冷 + 1×40 kW 风冷、CDU 2× SCR 14103 W、CRAH 4× CRS 560 CW；L450C20 = 3×150 kW 无风冷柜、CDU 1× SCR 14103 W、CRAH 2× **CRS 330 CW（N+1）**；I200C20 有 5 kW 风冷柜、推荐 180 kW。关闭 KC-3（风冷柜算设施不算 IT，站点 `tco-power.js` 口径）与 KC-4（I200C20 确有风冷柜）；KC-5 前提更正（站点 `ulCompliant: false` 是明确否定，非未披露）；KC-6 重写（256 已对客发布，须裁定追认或撤下）。新增 KC-10…KC-15 六条站点↔KB 冲突。冲突编号加 `KC-` 前缀，与站点 Claims 台账 `Cn` 分离。§5 同步清单补 Reference_Architecture 与 Products/_blocks 两项（本次漏更根因） |
| **v2.0** | **2026-08-30** | **Yuri 裁定关闭 5 条冲突。** KC-1 双环路 GPU 侧温位链落定（外冷源 32–36 °C → CDU +4 °C → GPU 36–40 °C，STULZ 选型书为该带热端设计点；站点 45 应改 40）；KC-2 PUE 全线改写 `1.0x` 并指向 <https://mdcx.org> 计算，L1240C45 的 1.15–1.20 与浸没线的 1.05 一并作废；KC-8 交期统一为首批 120 天 EXW / Scale 90 天 EXW，商务·运输·安装一律不承诺，新增假负载运行期 5–30 天（Supermicro 建议）；KC-9 质保统一为核心部件 EXW 起一年 + 按年服务费，ONSITE/NBD/24×7 以 Invoice 为准；CW330 归属落定 L450C20（与 CW560 同属无 UPS 的 DLC 族）。§5 新增「需回站点仓库修正的三项」反向同步清单。剩余待裁 KC-3…KC-7 |
| v1.1 | 2026-08-30 | 按两轮 Tech Spec 编写中发现的问题回填：新增 §6 未裁定冲突登记簿（KC-1…KC-9）；§1.2 "已批"改"选型"并与 §4 状态对齐（L1240C45 的 RDHX / CeilAir 实为正在 review）；新增 CDU/CRAH 台数与冗余行；L1800C45 外形由 🔶 降为 ⏳（上部模块 900 mm 抬升未澄清）；L450C20 补标准箱 vs High Cube 缺口；补浸没线供电制式缺口、10 kW 风冷柜归属、I200C20 交换机位置、I400C40 UL 状态、质保与 SLA 来源缺失；补整箱二次侧流量 🔶；A32 全部改 [[I50TS]]；补齐全部空白置信度格；§5 同步清单补 CLAUDE.md、块文件、Guideline、External 版 |
| v1.0 | 2026-08-30 | 首版。从站点 `PRODUCT-MATRIX.md` 与 `llms-full.txt` 提取六 SKU 全字段；按 [[UNCONFIRMED_Convention]] 四级置信度逐字段标注；建立下游同步清单 |
