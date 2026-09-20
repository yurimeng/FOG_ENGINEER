---
tags:
  - "#workspace/engineer"
  - "#type/reference"
  - "#type/design-spec"
  - "#product/general"
  - "#unconfirmed"
  - "#MDC"
doc_version: v2.6
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
> **裁定状态：** 2026-08-30 Yuri 裁定关闭 5 条（KC-1 / KC-2 / KC-8 / KC-9 + CW320 归属），**剩余 5 条未裁定**（KC-3 / KC-4 / KC-5 / KC-6 / KC-7），见 [[#6. 冲突登记簿|§6]]。对客前必查该节。

## 0. 六 SKU 一览

| 短别名 | 全 SKU ID | 线 | IT kW | 尺寸 | 环路 | UPS | 密度 | 状态 |
|---|---|---|---|---|---|---|---|---|
| **L1240C45** | `L1240C45SUR150` | Liquid | 1240 | 45ft HC | S | 内置 | R150 | shipped ✅ ^mdc-7c365b5ae3 |
| **L1800C45** | `L1800C45DR220` | Liquid | 1800 | 45ft HC | D | 外置 | R220 | shipped ✅ ^mdc-5a27079d6e |
| **L450C20** | `L450C20DR150` | Liquid | 450 | 20ft | D | 外置 | R150 | shipped ✅ ^mdc-c08b454a8c |
| **I400C45** | `I400C45SUT50` | Immersion | 400 | 45ft | S | 内置 | T50 | shipped ✅ ^mdc-d41f68b310 |
| **I400C40** | `I400C40ST50` | Immersion | 400 | 40ft | S | 外置 | T50 | shipped ✅ ^mdc-045d12c6d1 |
| **I200C20** | `I200C20ST50` | Immersion | 200 | 20ft | S | 外置 | T50 | shipped ✅ ^mdc-a9d16a90b1 |

> **六个 SKU 全部 `shipped`。** 站点 2026-08-27 D-19 gate 一次性放行 I200C20 / L1800C45 / L450C20 三个原 draft SKU。 ^mdc-eb3f7d710a
>
> [[I50TS]]（`I50TS`，旧称 A32）是浸没槽体**组件**，不是 SKU，不进本表。它是 I400C45 / I400C40 的 8× 与 I200C20 的 4× 构成单元。**该码为 KB 侧按 Tank 正则推导** ⏳ **#unconfirmed** —— 等站点侧写入 `PRODUCT-MATRIX.md` Alias registry，预期 TBD。见 [[#9. 未裁定冲突登记簿|§6 · KC-7]]。 ^mdc-f1b8164411

^baseline-overview

## 0.1 冷却末端术语（规范，不得混用）

液冷线有**两种完全不同的末端机型**，此前 vault 与站点都把它们混称「CRAH」，2026-08-30 起按下表严格区分：

| 术语 | 指什么 | 用在哪个 SKU | 机型 | 送风方式 | 冷源 |
|---|---|---|---|---|---|
| **CRAH（吊顶机型）** | 顶置自含式 DX 精密空调 | **仅 L1240C45** | STULZ CeilAir **OHS-084-DG-FC** | 顶置下送 | 机内压缩机 + PG25 水冷冷凝 ^mdc-b520b75539 |
| **CyberRow CW（列间冷冻水空调）** | 列间式全水盘管机组 | **L1800C45 · L450C20** | STULZ **CRS 560 CW**（CW560）· **CRS 320 CW**（CW320） | 嵌入机柜列，左/右侧向送风 | 无压缩机，直接接 10/15 °C 冷冻水 ^mdc-6cc64b46de |

**三条硬规则：**

1. **「CRAH」只指 L1240C45 的吊顶机型。** 写 L1800C45 / L450C20 的末端时用「列间空调」或「CyberRow CW」，中英文均不得用 CRAH。 ^mdc-0e62a07a28
2. **两者不可互相替代。** [[CRAH_Requirement V5]] 的 scope 只覆盖吊顶 DX 机型；[[CRAH_Replacement_RFQ_Spec V1]] 已论证列间/房间级 CW 型在 L1240C45 的 TCS 26 °C 单点工况下**物理不可行**（换热温差仅 6 K）。反向同理：吊顶 DX 机型不进双环路 SKU。 ^mdc-9b2383c402
3. **文件名 `CRAH_Requirement V5` 保留原名**（它确实是吊顶机型的需求书），但其正文 scope 须写明「仅 L1240C45 吊顶机型」。 ^mdc-e3246359d3

> ✅ **站点分类词已改正（2026-09-02，Yuri 指示）：** `docs/CLAIMS.md` C33、`liquid-l1800.html` / `liquid-l450.html` / `solutions/liquid.html`、`llms.txt`、`packages/solution-matrix`、`functions/lib/seed.ts` 与两份 `content/docs/claims.*.md` 的英文 `CRAH` 全部改为 **in-row CW**，中文统一为 **CW 列间空调**。规则同时写进站点 `docs/rules/NAMING.md` §1.2（含"L1240C45 = CRAH / 吊顶"一行），CLAIMS C33 备注里也带了同一条。 ^mdc-6c51a55271
>
> **字段名 `crahId` / `crahCount` / `crahBranchLPM` / `totalHeatByCRAH` 明确保留不改** —— 它们是单环路时代的引擎字段名，改名要重录全部快照且不带来任何工程收益；站点 NAMING.md §1.2 与 `dc45-spec.ts` 的 schema 注释都写明了"不是产品术语，不得在文案中沿用"。KC-16 的 ① 已关闭，② ③ 仍开。

^baseline-terminology

## 1. Liquid Cooling 线

### 1.1 容量与密度

| 字段 | L1240C45 | L1800C45 | L450C20 | 置信度 ^mdc-17e97f5584 |
|---|---|---|---|---|
| IT 容量 | 1240 kW | 1800 kW | 450 kW | ✅ 站点 |
| 机柜构成 | 8× 150 kW 液冷 + 1× 40 kW 风冷 = 9 柜 | **8× 220 kW 液冷 + 1× 40 kW 风冷 = 9 柜** | **3× 150 kW 液冷，无风冷柜 = 3 柜** | ✅ 站点 Designer profile |
| 单柜密度 | 150 kW（R150） | 220 kW（R220） | 150 kW（R150） | ✅ 站点 |
| GPU 平台 | GB300 NVL72 · B300 HGX（SXM / NVLink） | GB300 NVL72 · B300 HGX | ⏳ **#unconfirmed** | ✅ 站点（仅 L1240/L1800 披露） |

> ✅ **2026-08-30 站点审计已取到确定值**，来源 `DLC/src/data/profiles/l1800.json` · `l450.json` 与 `packages/scene/src/tables.ts`。原 ⏳ 关闭。
> **注意 L450C20 没有风冷柜** —— 与两个 45ft 液冷 SKU 不同，站点 `TCO/public/tco-power.js` 的风冷柜常量对它是 0。 ^mdc-a48d54f35d
>
> ⚠️ **不要把项目文档里的柜位数当产品规格。** `Projects/` 下按项目容积规划的"柜位/仓"数与产品机柜数不是同一量纲，两者只隔一个 wikilink，极易误引。

### 1.2 冷却架构

| 字段 | L1240C45 | L1800C45 | L450C20 | 置信度 ^mdc-b4469ae6d7 |
|---|---|---|---|---|
| 环路数 | 单环路 | 双环路 | 双环路 | ✅ 站点 |
| GPU 侧进水温位 | TCS 26 °C 暖水单点（KB 工程口径 26–28 °C） | **36–40 °C** ✅ 裁定 | **36–40 °C** ✅ 裁定 | ✅ |
| 外冷源一次侧出水（FWS 进 CDU） | 站点 EG · 22 °C | **32–36 °C** ✅ 裁定 | **32–36 °C** ✅ 裁定 | ✅ |
| CDU 温升（approach） | ≥4 °C（[[CDU_Requirement V5]]） | **+4 °C** ✅ 裁定 | **+4 °C** ✅ 裁定 | ✅ |
| CRAH 侧温位 | 无独立 CRAH 环路（Branch 3 走 TCS 冷凝） | **10 / 15 °C 冷冻水（ΔT 5 K）** | **10 / 15 °C 冷冻水（ΔT 5 K）** | ✅ 站点（2026-08-31 由 10/15 改） |
| 二次侧介质 | **PG25**（25% 丙二醇） | **纯水 0%** | ⏳ **#unconfirmed** —— 等 L450C20 DESIGN 或 CW320 选型书，预期 TBD | ✅ KB / ✅ 选型书 / ⏳ ^mdc-77035531f0 |
| 末端构成 | 冷板 + 9× RDHX + 9× 顶置 DX **CRAH** | 冷板 + **CyberRow CW 列间空调** | **冷板 + 4× CRS 320 CW** ✅ 站点 profile / PRD v2.0 | ✅ KB / ✅ 选型书 / ✅ ^mdc-311342bcd7 |
| CDU 选型 | ≥1500 kW（[[CDU_Requirement V5]]，**未定型号**，状态见 §4）⛔ 见 KC-10 | **STULZ SCR 14103 W** ✅ ATS approved | **STULZ SCR 14103 W** ✅ 站点 profile | ⛔ / ✅ / ✅ |
| CRAH 选型 | 9× STULZ OHS-084-DG-FC（**⏳ 正在 review**，CE / 50 Hz 阻塞）⛔ 见 KC-10 | **STULZ CRS 560 CW**（CW560）✅ ATS approved · **参数已固化 2026-09-08（设计点 13,000 m³/h）** | **STULZ CRS 320 CW**（CW320）✅ **参数已固化 2026-09-08**（选型书到位，风机 4.5 kW 满转），见 [[PRD-STULZ-CW320]] v2.0 | ⛔ / ✅ / ✅ ^mdc-a4afbb7563 |
| **CDU / 列间空调台数与冗余** | CDU 1 台（≥1500 kW）· CRAH 9 台吊顶（N，无 N+1） | **CDU 2× SCR 14103 W · 列间空调 **2× STULZ CRS 560 CW + 6× STULZ CRS 320 CW**（混配，共 8 台）** | **CDU 1× SCR 14103 W · 列间空调 4× CRS 320 CW**（2026-09-02 由 2 台改；N+1 风量余量 1.4%） | ✅ 站点 Designer profile |
| 室外侧排热基线 | ≥1700 kW | ⏳ **#unconfirmed** —— 等 L1800C45 DESIGN，预期 TBD | ⏳ **#unconfirmed** —— 等 L450C20 DESIGN，预期 TBD | ✅ KB / ⏳ / ⏳ ^mdc-e9712a9802 |
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
> **这条链同时适用 L1800C45 与 L450C20**（两者均为双环路、无 UPS 的 DLC 解决方案）。 ^mdc-a016730b26
>
> **与已批 STULZ SCR 14103 W 选型书的对应关系：** 选型书取该带的**热端设计点** —— FWS 36 °C 进 / 46 °C 出，TCS 40 °C 供 / 50 °C 回，approach 恰为 4 °C，与本裁定完全一致。选型书不是另一套温位，是同一条链在最不利工况下的取值。
>
> ⚠️ **站点对客页目前写「GPU 36–45 °C」，与本裁定不符。** 上限 45 应为 40。这是工程参数（Yuri 所有），不是 SKU 码（站点所有），故以本表为准；**需回站点仓库修正三处液冷页面文案**，见 §5 反向同步。

> **L1240C45 与另两个 SKU 的冷却基线不可互换。** [[CDU_Requirement V5]]（FWS 22/32 · TCS 26/36 · PG25 · DN100 法兰）与 [[CRAH_Requirement V5]]（自含式 DX · PG25 冷凝）的 scope **只覆盖 L1240C45**。L1800C45 温位整体高约 14 K、介质为纯水、接口为 Tri-Clamp。详见 [[PRD-STULZ-SCR14103W]] §4 与 [[PRD-STULZ-CRS560CW]] §4。 ^mdc-b1c5dbf59c
>
> ## 🔴 2026-09-08：CW 参数按 StulzSelect 选型书固化 —— 厂家样本表作废
>
> **定案（Yuri 2026-09-08）：CRS 560 CW 冻结在「风量提高」运行点 13,000 m³/h**（与「标准机」是同一台硬件、同一风机型号，只是满转，**采购不分型号**）；**配置维持 2×560 + 6×320，4×560 的替代方案另开评审。** 选型书工况：回风 37 °C · RH **27%** · 冷冻水 10/15 °C · 0% 乙二醇 · ESP 0 Pa。
>
> | | 2026-08-31（样本表，作废） | **2026-09-08（选型书，现行）** |
> |---|---|---|
> | CRS 560 CW 单台 | 毛 64.2 / 风机 2.6 / 净 61.6 kW · 11,200 m³/h · 11.04 m³/h | **毛 64.6 / 风机 3.9 / 净 60.7 kW · 13,000 m³/h · 11.1 m³/h · 140 kPa · DN32 阀** |
> | CRS 320 CW 单台 | 毛 35.8 / 风机 1.49 ✅ / 净 29.1 kW · 6,400 m³/h · 6.16 m³/h | **毛 33.6 / 风机 4.5 / 净 29.1 kW · 6,100 m³/h · 5.8 m³/h · 119 kPa · DN25 阀** | ^mdc-4630409bd8
> | L1800C45 列间侧合计 | 毛 343.2 / 风机 14.1 / 净 329.1 kW · 60,800 m³/h · 59.0 m³/h | **毛 330.8 / 风机 34.8 / 净 296.0 kW · 62,600 m³/h · 57.0 m³/h** | ^mdc-072f50599f
> | L450C20 列间侧合计（4 台） | 毛 143.2 / 风机 5.96 / 净 137.2 kW · 25,600 m³/h · 24.64 m³/h | **毛 134.4 / 风机 18.0 / 净 116.4 kW · 24,400 m³/h · 23.2 m³/h** | ^mdc-e427cd5c60
> | 外形 W×H×D · 重量 | 600×2000×1375 / 254 kg · 400×2000×1375 ⏳ | **600×1950×1375 / 254 kg · 400×1950×1375 / 190 kg** |
>
> 🔴 **三条硬结论：**
> 1. **CRS 320 CW 的风机功率是 4.5 kW，不是推导的 1.49 kW，而且它已在 3,850/3,850 rpm 满转 —— 该机型零风量余量。** 「320 转速余量待确认」关闭。
> 2. **厂家样本表偏乐观，一律改引选型书。** 样本工况 4 给 560 在 11,200 风量下 64.2 kW，选型书同风量只有 58.8；320 给 35.8 @6,400，选型书 33.6 @6,100。
> 3. **单机总水阻是厂家值 140 kPa（560）/ 119 kPa（320），不是此前按平方律估的 ≈94 kPa —— LT 侧循环泵扬程必须按 140 kPa 重选。**「向 STULZ 询 DN40 两通阀」关闭：厂家在 DN32 上给 48 kPa。
>
> ✅ **口径公式被厂家数据逐台反证：** 净 = 毛 − 风机；水流量 = 毛/(1.163×ΔT)（5.78→5.8 · 10.11→10.1 · 11.11→11.1）。
>
> ⚠️ **两条往下游传：** ① 列间风机负荷 14.1 → **34.8 kW**（@1800 kW IT 约 +0.012 PUE），进箱体辅助负载表；② **L450C20 的 N+1 风量余量由 6.4% 收到 1.4%**（掉一台剩 18,300 对最不利 18,043 m³/h）—— 该 SKU 今后任何风量增量都会击穿 N+1。 ^mdc-5e18d0cfe2
>
> ⏳ **唯一新增未决项：声学。** 选型书不含声功率/声压；CON-001 §5 支路流噪判据原引的 67.6 dB(A) 是 2,393 rpm 旧值，设计点改满转后不适用，须向 STULZ 索取。
>
> 详见站点 `docs/CONNECTOR-STANDARD-MDCX-CON-001.md` **A4** · [[PRD-STULZ-CW320]] v2.0 · [[PRD-STULZ-CRS560CW]] v2.0。

> ## ⛔ 2026-08-31（已被上方 2026-09-08 取代）：CRS 330 CW 停用改 CRS 320 CW · 冷冻水口径改 10/15
>
> **1. 机型。** STULZ 反馈 **CRS 330 CW 不可用**，替代机型 **CRS 320 CW**；非标宽度**只能定制到 400 mm，不是 300 mm**。L1800C45 6 台 + L450C20 2 台全部改配。站点组件目录已改名 `crs330cw.json` → `crs320cw.json`。 ^mdc-88cf6efcd5
>
> **2. 工况口径统一。** 两种 CyberRow CW 机型改为同一条厂家样本工况：**回风 37 °C · RH 25% · 冷冻水 10/15 °C · 0% 乙二醇**（样本工况 4）。此前 560 用其选型书的 36 °C / 10-16 °C，320 用推导值。
>
> | | 旧（作废） | **现行** |
> |---|---|---|
> | CRS 560 CW 单台 | 毛 57.3 / 净 54.7 kW · 8.2 m³/h | **毛 64.2 / 净 61.6 kW · 11.04 m³/h** |
> | CRS 320 CW 单台 | （CRS 330 CW）毛 36 / 净 33 kW · 5.16 m³/h | **毛 35.8 / 净 29.1 kW ✅ · 6.16 m³/h** | ^mdc-579317d6a9
> | L1800C45 列间侧合计 | 毛 330.6 / 净 307.4 kW · 47.4 m³/h | **毛 343.2 / 净 329.1 kW · 59.0 m³/h** | ^mdc-c1480d9f35
>
> **冷量几乎没变，流量涨 24%** —— 因为 ΔT 由 6 K 降到 5 K。站点 `CLAIMS.md` C33 已由 10/16 改 **10/15**，六个产品页与 12 张 RD 页已重出。
>
> ✅ **未决项 ① 已定案（Yuri 2026-08-31）：保持 DN40。** CW 单机支路判据由 v≤2.5 放宽到 **v≤3.1 m/s**（3.01 m/s 通过），其余回路判据不变；前提是纯水闭式除氧与型式试验补测支路流噪。**连带：560 单机水侧压降 52 → ≈94 kPa（估算），LT 侧泵扬程须重选，DN32 两通阀内 3.7 m/s，建议询 DN40 阀。**
>
> ⚠️ **未决项 ② 仍未决：** 6 台列间机由 300 变 400，**算力仓柜列加长 600 mm**，两端余量 467→167 mm，3D 未联动。
>
> ✅ CRS 320 CW 的**风机功率 1.49 kW 与净冷量 29.1 kW 仍是推导值**（按风量比缩放 560 的 2.6 kW），外形 2000×400×1375 中的高与深为暂定。等 StulzSelect 选型书与外形图。 ^mdc-e0894a4390

> ## L1800C45 列间空调是混配（2026-08-30 Yuri 确认） ^mdc-fac07530e0
>
> **2× CRS 560 CW + 6× CRS 320 CW，共 8 台（2026-09-08 复核维持不变）。** 净冷量合计 = 毛 **330.8** − 风机合计 **34.8** = **296.0 kW**（单台净 60.7 / 29.1）。
>
> 8 台列间机对应 9 个机柜位（8 液冷 + 1 风冷）—— 列间机嵌在机柜之间，台数由**排布**决定，不是单纯按热负荷除单机容量得出。
>
> ✅ **站点已改（2026-09-02）：`plant.crah` 由单一 `crahId` + `crahCount` 改成列表 `[{id, count}]`，L1800C45 直接写实配的 `2× crs560cw + 6× crs320cw`。** KC-16 ② 关闭。 ^mdc-39e83dfa02
> 引擎仍只吃「单台器件 + 台数」，所以 `packages/solve/src/crahFleet.ts` 喂给它**按台数加权的平均机**——这样 `单台 × 台数` 形式的每一项聚合都精确：8 台 · 净 **296.0 kW** · 风机 **34.80 kW** · 风量 **62,600 m³/h** · 冷冻水 **57.00 m³/h**，与本节和 CON-001 **A4** 逐位吻合。
>
> ⚠️ **平均机唯一算不准的是 N+1** —— 掉一台平均机比掉一台 560 轻。真实最不利是**净 235.3 kW / 风量 49,600 m³/h**（一台 CRS 560 CW 停机）。解析器另给 `capacityWithLargestDownKW` / `airflowWithLargestDownM3h`，冗余校核必须用这两个，**不得用 `单台 × (台数−1)`**。
>
> ✅ **L450C20 的列间由 2× 改 4× CRS 320 CW（Yuri 2026-09-02 定案）。** 🔴 **2026-09-08 参数固化后重算：四台为净 116.4 kW / 24,400 m³/h / 风机 18.0 kW；N+1 剩 87.3 kW / 18,300 m³/h，对最不利 18,043 m³/h 只余 1.4%（原 6.4%）。N+1 仍成立但已无余量。** 以下为 2026-09-02 的原始论证（数字为旧口径）： 两台不是冷量不够而是**风量不够**：3× GB300 需 9,175 m³/h、排热 54 kW，单台幸存机两项都不满足；3 柜 × 8 台 B300 需 14,435 m³/h，**两台全开 12,800 也不够**。四台后 137.2 kW / 25,600 m³/h，N+1 剩 102.9 kW / 19,200 m³/h，覆盖最不利的 37.5 kW / 18,043 m³/h（3 柜 × 10 台 B300）。备选 3× CRS 560 CW（22,400 m³/h）同样可行，未选。**这个 SKU 的判据是风量不是冷量，复核时按风量来。** ^mdc-352ebbacab
>
> ✅ **CDU 运行方式（Yuri 2026-09-02）：两台 CDU 可 A/B 分别运行，也可同时运行 —— 两种都是正常模式，不是故障工况。** 两个连带后果见 [[Supermicro_GB300_B300_Thermal_Verification_v1]] §2.2 / §2.3：单台运行时二次侧全流量走 DN125 干管的**一端**（厂家流量下 1.38–1.65 m/s ✅，但 **R220 铭牌 1,760 kW @ΔT14 = 2.67 m/s ❌**，DN125 单端载热上限 ΔT14 1,646 / ΔT15 1,764 / ΔT20 2,352 kW）；反过来，一用一备正好解决泵的调节下限问题（单台 70 % = 72.7 m³/h 对需求 56.4，1.29 倍；两台同时则 145.3 m³/h，2.6 倍）。
>
> CDU 台数（L1800C45 2 台 / L450C20 1 台）取站点 profile。[[PRD-STULZ-SCR14103W]] Q1 与 [[PRD-STULZ-CW320]] Q5 据此关闭。 ^mdc-1b3478bb3a
>
> **L1800C45 / L450C20 仍没有专属 列间空调 / CDU Requirement。** 两个 SKU 的冷却侧只有 PRD 与站点 profile，**没有需求书基线**。这是当前最大的工程文档缺口 —— 两者共用同一条温位链与同一 列间侧 10/15 °C 回路，可以合并成一份覆盖「无 UPS 的 DLC 解决方案」的 `CRAH_Requirement V6` + `CDU_Requirement V6`。 ^mdc-1069a1d139

^baseline-liquid-cooling

### 1.3 电力

| 字段 | L1240C45 | L1800C45 | L450C20 | 置信度 ^mdc-5bf3b942d4 |
|---|---|---|---|---|
| UPS 边界 | **箱内**（UPS + 电池） | **箱外**（UPS / 电池 / PDC 由场站提供） | **箱外** | ✅ 站点 |
| UPS 型号 | EATON 9395XR-1500（1500 kW） | 不适用 | 不适用 | ✅ KB |
| 电池后备 | ~8 min（3× 93LiG2） | 不适用 | 不适用 | ✅ KB |
| 母线 | SIEMENS 2500A 封闭插接式 | **2 × 2000 A 封闭插接式（A / B 双路分流，132 × 215，五线制）** —— 见 [[L1800C45_Busway_TOU_Design_v1]] | ⏳ **#unconfirmed** —— 等 DESIGN/BOM，预期 TBD | ✅ KB / 🔶 设计定案 / ⏳ |
| 单柜配电（TOU） | 每机柜 Tap-off 插接 | **400 A 插接箱 × 2 / 柜**（A / B 各 1，共 16 只）· 出线 **4 × 63 A**（箱体按 6 路位预留）· 出线端 **IEC 60309 60 A** | ⏳ **#unconfirmed** | ✅ KB / 🔶 设计定案 / ⏳ |
| 供电制式 | 380 / 400 / 415 / 480 V AC | 同左 | 同左 | ✅ 站点 |

> 🔶 **L1800C45 的箱内母线由「1 × 4000 A」改为「2 × 2000 A 分流」（Yuri 2026-09-03 定案）。** 两条母线**只分流、不互为备用**，干线铜排为承认的单点；冗余在插接开关及其下游。取消了原方案的 16 组 T 型分接头、16 只转角弯头与 16 段支路直段，系统纵深由 1,412 mm 降到 714 mm。机柜插接开关由 630 A 改 **400 A**，出线由 1 路改 **4 路 63 A / IEC 60309 60 A**（箱体按 6 路位预留，因 4 路带不到本 SKU 的 225 kW/柜上限）。 ^mdc-c5a2f440e3
> **状态为「设计定案 · 待厂家确认」** —— 对外文件 BW-TC-001 Rev.B / BW-TC-002 Rev.B 已发 Siemens，两条阻塞项已发 Supermicro。全部参数、坐标与待确认清单见 [[L1800C45_Busway_TOU_Design_v1]]。
>
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
> ✅ **L450C20 的 20ft 标准箱 vs High Cube 是本表最具决策价值的缺口。** 该 SKU 的全部价值主张就是"45ft 进不去的舱位它能进"，而标准箱与 HC 的高度差 305 mm（2,591 vs 2,896 mm）直接决定能否进场。**不得**引用 ISO 名义值 6,058 × 2,438 × 2,591 mm。等站点 Designer profile 或 DESIGN 文档，预期 TBD。

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
| **L1800C45** | 列间侧 | CyberRow CW | STULZ **CRS 560 CW × 2**（与 CRS 320 CW × 6 混配） | ✅ **ATS approved** 2026-08-30 | [[PRD-STULZ-CRS560CW]] |
| **L1800C45** | 列间侧 | CyberRow CW | STULZ **CRS 320 CW × 6**（与 CRS 560 CW × 2 混配） | ✅ 归属已定 2026-08-30 · ⏳ 规格待厂家 | [[PRD-STULZ-CW320]] |
| **L450C20** | 列间侧 | CyberRow CW | STULZ **CRS 320 CW × 4**（N+1） | ✅ **归属已定** 2026-08-30 · ✅ 规格 ✅ PRD v2.0 2026-09-08 | [[PRD-STULZ-CW320]] | ^mdc-cw320-l450-idx
| L1240C45 | Branch 2 | RDHX | VERTIV CoolLoop DCD35 | ⏳ 正在 review（Q1 待 VERTIV） | [[PRD-Vertiv-RDHx]] |
| L1240C45 | Branch 3 | 顶置 DX | STULZ OHS-084-DG-FC | ⏳ 正在 review（**CE / 50 Hz 市场准入阻塞**） | [[PRD-STULZ-CeilAir]] |
| L1240C45 | Branch 3 替代 | 卧式自含水冷 DX | 未定（Vertiv / HiRef / 国产 CE 线） | ⏳ RFQ 阶段 | [[CRAH_Replacement_RFQ_Spec V1]] |
| L1240C45 | 室外侧 | Hybrid Chiller | TICA TAMFV430.3ALF5 | ✅ **ATS Full Pass** 2026-06-11 | [[TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.3]] |

> ## CyberRow CW 列间空调 的产品族归属（2026-08-30 Yuri 裁定）
>
> **CW320 与 CW560（CRS 560 CW）同属「无 UPS 的 DLC 解决方案」族** —— 即 **L1800C45 + L450C20** 这两个双环路、UPS 在箱外的液冷 SKU。CW560 已定 L1800C45，**CW320 归 L450C20**。
>
> 两者共用同一条 GPU 侧温位链（外冷源 32–36 °C → CDU +4 °C → GPU 36–40 °C）与同一 列间侧 10/15 °C 冷冻水回路，差别只在容量档。这也意味着两个 SKU 的 列间侧可以共用一份需求书基线 —— 见 §1.2 末的文档缺口说明。

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

> 每条都是**不能靠查资料解决、必须由人拍板**的问题。**2026-08-30 Yuri 裁定关闭 4 条（KC-1 / KC-2 / KC-8 / KC-9）**，另关闭 CW320 归属（原 [[PRD-STULZ-CW320]] Q1）。**剩余 5 条待裁。**

### 已裁定

| # | 冲突 | 裁定（2026-08-30 Yuri） |
|---|---|---|
| **KC-1** ✅ | L1800C45 GPU 侧温位：站点 36–45 °C vs 已批 CDU 工况 | **GPU 进水 36–40 °C；外冷源一次侧出水 32–36 °C；CDU approach +4 °C。** STULZ 选型书取该带热端设计点，与裁定一致。站点页 45 应改 40 |
| **KC-2** ✅ | I400C45 的 PUE 与设施负荷不自洽 | **PUE 一律写 `1.0x`**，不给固定值。逐站点用 <https://mdcx.org> 计算。适用全部六 SKU，L1240C45 的 1.15–1.20 亦作废 |
| **KC-8** ✅ | 交期三种并存口径 | **首批 120 天 EXW、Scale 90 天 EXW，自下单起算；商务/运输/安装一律不承诺。** 另增假负载运行期 5–30 天（Supermicro 建议），不含在 EXW 内 |
| **KC-9** ✅ | 质保年限与 SLA 无来源 | **核心部件 EXW 起一年，后续按年服务费。ONSITE / NBD / 24×7 等条款以 Invoice 为准**，KB 不定义 |
| **CW320 归属** ✅ | CW320 属哪个 SKU | **CW320 与 CW560（CRS560CW）同属「无 UPS 的 DLC 解决方案」族** = L1800C45 + L450C20。CW560 已定 L1800C45，**CW320 归 L450C20** |

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
| **KC-16** | **站点把两种末端机型混称 CRAH，且 L1240C45 的末端配错。** ①【2026-09-02 已关闭，见 §0.1】分类词：`crahId`/`crahCount` 字段名、`CLAIMS.md` C33 的 *"in-row CRAH"*、产品页英文 `CRAH` —— 全部把 CyberRow CW 列间机归到 CRAH 名下（见 §0.1）。②【2026-09-02 已关闭】站点写 `crs560cw × 4`，实配为 **2× CRS 560 CW + 6× CRS 320 CW**（Yuri 2026-08-30 确认）；`plant.crah` 已改为列表结构，实配已入库，聚合值与本文件逐位一致。③ ④ **`DLC/src/data/profiles/dc45.json` 的 plant 块给 **L1240C45** 配了 `crs560cw` × 2，但 L1240C45 用的是吊顶 DX（OHS-084-DG-FC），**列间 CW 机型在该 SKU 工况下物理不可行**（[[CRAH_Replacement_RFQ_Spec V1]]）。站点 Designer 据此出的 L1240C45 冷却数是错的 | 站点 Designer 出数 · 12 张 RD 页 · L1240C45 全部冷却口径 | ATS + 站点侧 |
| **KC-7** | **`I50TS` 码本身是 ⏳，却是三个 ✅ shipped SKU 的构成单元。** 一个不能引用的组件码，让任何浸没 Tech Spec 的槽体规格节都无法写成干净的 ✅ | 三个浸没 SKU 的槽体节 | 站点侧（写入 Alias registry） |

^baseline-conflicts

---

## Changelog

| 版本 | 日期 | 变更 |
|---|---|---|
| 2026-09-20 | 🧭 unconfirmed-178 已可关闭，已回写来源值（已可关闭） |
| 2026-09-20 | 🧭 unconfirmed-168 改为 ⛔ conflict，未裁定赢家 |
| 2026-09-20 | 🧭 unconfirmed-177 已可关闭（已可关闭） |
| 2026-09-20 | 🧭 unconfirmed-218 已可关闭（已可关闭） |
| 2026-09-20 | 🧭 unconfirmed-219 已可关闭（已可关闭） |
| 2026-09-20 | 🧭 unconfirmed-220 已可关闭（已可关闭） |
| **v2.5** | **2026-09-03** | **§1.3 电力：L1800C45 的母线由 ⏳ #unconfirmed 落为「2 × 2000 A 封闭插接式（A / B 双路分流，132 × 215，五线制）」**，并新增「单柜配电（TOU）」行（400 A 插接箱 × 2 / 柜，出线 4 × 63 A / IEC 60309 60 A，箱体按 6 路位预留）。两条母线**只分流、不互为备用**，干线铜排为承认的单点。取消原方案的 16 T 头 / 16 弯头 / 16 支路，系统纵深 1,412 → 714 mm。状态为 🔶 **设计定案 · 待厂家确认**（BW-TC-001 Rev.B / BW-TC-002 Rev.B 已发 Siemens）。全部参数见 [[L1800C45_Busway_TOU_Design_v1]]。下游已同步：[[L1800C45_Tech_Spec_CN]] §6.2 与 §14、[[L1800C45_Tech_Spec_EN]] 同位、[[KB/LIQUID/L1800C45/index\|L1800C45 index]]、[[MDC/KB/3RD-PARTY/Busbar/index\|Busbar index]] |
| **v2.4** | **2026-08-31** | **CRS 330 CW 停用 → CRS 320 CW**（厂家反馈；非标宽度下限 400 mm）。**两种 CyberRow CW 的工况口径统一到样本工况 4**（回风 37 °C · 冷冻水 10/15 °C · 0% 乙二醇）：560 单台净 54.7→**61.6 kW**、流量 8.2→**11.04 m³/h**；320 单台净 **29.1 kW** ✅、流量 **6.16 m³/h**；L1800C45 列间侧合计净 307.4→**329.1 kW**、47.4→**59.0 m³/h**。全 vault 的 10/16 改 **10/15**。原 `PRD-STULZ-CW330.md` 更名并重写为 [[PRD-STULZ-CW320]]（v1.0）。站点侧同步：`crs320cw.json`、`l450.json` 的 `crahId`、`CLAIMS.md` C33、CON-001 A3、六个产品页与 12 张 RD 页。**定案：560 支路保持 DN40，CW 单机支路判据放宽到 v≤3.1 m/s**（连带：单机压降 52→≈94 kPa，LT 泵扬程须重选；DN32 两通阀 3.7 m/s 建议询 DN40 阀）。**仍未决：柜列 +600 mm** |
| **v2.3** | **2026-08-30** | **L1800C45 列间空调实配确认（Yuri）：2× CRS 560 CW + 6× CRS 330 CW，共 8 台、净冷量 307.4 kW。** 站点 `crahCount: 4` 单一机型写法作废；CW330 的适用范围由「仅 L450C20」扩为「L1800C45 6 台 + L450C20 2 台」。KC-16 补记站点台数错误与 `plant` schema 无法表达混配 |
| **v2.2** | **2026-08-30** | **末端术语规范化（Yuri 澄清）。** 新增 §0.1：CRAH（吊顶 DX，仅 L1240C45）与 CyberRow CW（列间冷冻水，L1800C45 / L450C20）严格区分，中英文均不得混用。全 vault 18 份文件的错标已改。新增 KC-16 记录站点侧两处问题：分类词混用，以及 `dc45.json` 给 L1240C45 错配 CRS 560 CW（列间机在该 SKU 工况物理不可行） |
| **v2.1** | **2026-08-30** | **吸收 MDCX 站点仓库审计结果。** 站点 Designer 数据层已有确定值，按"本表永远跟随站点"规则从 ✅ 转 ✅：L1800C45 = 8×220 kW 液冷 + 1×40 kW 风冷、CDU 2× SCR 14103 W、列间空调 4× CRS 560 CW；L450C20 = 3×150 kW 无风冷柜、CDU 1× SCR 14103 W、列间空调 2× **CRS 330 CW（N+1）**；I200C20 有 5 kW 风冷柜、推荐 180 kW。关闭 KC-3（风冷柜算设施不算 IT，站点 `tco-power.js` 口径）与 KC-4（I200C20 确有风冷柜）；KC-5 前提更正（站点 `ulCompliant: false` 是明确否定，非未披露）；KC-6 重写（256 已对客发布，须裁定追认或撤下）。新增 KC-10…KC-15 六条站点↔KB 冲突。冲突编号加 `KC-` 前缀，与站点 Claims 台账 `Cn` 分离。§5 同步清单补 Reference_Architecture 与 Products/_blocks 两项（本次漏更根因） |
| **v2.0** | **2026-08-30** | **Yuri 裁定关闭 5 条冲突。** KC-1 双环路 GPU 侧温位链落定（外冷源 32–36 °C → CDU +4 °C → GPU 36–40 °C，STULZ 选型书为该带热端设计点；站点 45 应改 40）；KC-2 PUE 全线改写 `1.0x` 并指向 <https://mdcx.org> 计算，L1240C45 的 1.15–1.20 与浸没线的 1.05 一并作废；KC-8 交期统一为首批 120 天 EXW / Scale 90 天 EXW，商务·运输·安装一律不承诺，新增假负载运行期 5–30 天（Supermicro 建议）；KC-9 质保统一为核心部件 EXW 起一年 + 按年服务费，ONSITE/NBD/24×7 以 Invoice 为准；CW330 归属落定 L450C20（与 CW560 同属无 UPS 的 DLC 族）。§5 新增「需回站点仓库修正的三项」反向同步清单。剩余待裁 KC-3…KC-7 |
| v1.1 | 2026-08-30 | 按两轮 Tech Spec 编写中发现的问题回填：新增 §6 未裁定冲突登记簿（KC-1…KC-9）；§1.2 "已批"改"选型"并与 §4 状态对齐（L1240C45 的 RDHX / CeilAir 实为正在 review）；新增 CDU/CRAH 台数与冗余行；L1800C45 外形由 🔶 降为 ⏳（上部模块 900 mm 抬升未澄清）；L450C20 补标准箱 vs High Cube 缺口；补浸没线供电制式缺口、10 kW 风冷柜归属、I200C20 交换机位置、I400C40 UL 状态、质保与 SLA 来源缺失；补整箱二次侧流量 🔶；A32 全部改 [[I50TS]]；补齐全部空白置信度格；§5 同步清单补 CLAUDE.md、块文件、Guideline、External 版 |
| v1.0 | 2026-08-30 | 首版。从站点 `PRODUCT-MATRIX.md` 与 `llms-full.txt` 提取六 SKU 全字段；按 [[UNCONFIRMED_Convention]] 四级置信度逐字段标注；建立下游同步清单 |
