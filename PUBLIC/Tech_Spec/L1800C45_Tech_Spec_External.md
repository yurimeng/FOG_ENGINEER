---
tags:
  - "#MDC"
  - "#type/design-spec"
  - "#product/l1800c45"
doc_version: v1.1
updated: 2026-08-30
audience: 客户 / Customer（对外输出版）
sku_id: L1800C45DR220
---

# L1800C45 — Technical Specification（对外输出版 / External Edition）
**双环路直接液冷集装箱数据中心 · Dual-Loop Direct Liquid Cooled Container Data Center**
**45ft High Cube · 1800 kW IT · 单柜 220 kW / 220 kW per rack**

> **受众 / Audience：** 客户。**本版是本 SKU 唯一允许直接发给客户的版本。**
> This edition is written for customers and is the only edition of this SKU cleared for direct release.
>
> **配套版本 / Companion editions：** [[L1800C45_Tech_Spec_CN|中文内部版 / CN internal]] · [[L1800C45_Tech_Spec_EN|English internal]]
>
> **数据源 / Source of truth：** 全部参数取自 [[PRODUCT_SPEC_BASELINE]]（六 SKU 规格基准表）。**参数争议以基准表为准。**
> All parameters are taken from [[PRODUCT_SPEC_BASELINE]]. **Where parameters disagree, the baseline table governs.**
>
> **本版收录范围 / Scope of this edition：** 仅收录已确认参数与标注为「设计值」的推导参数。尚未定型的参数将在技术澄清阶段提供。
> This edition carries confirmed parameters plus derived parameters explicitly labelled as design values. Parameters not yet fixed will be provided during technical clarification.
>
> **本版为单文件，块拆分待需要时再做 / This edition is a single file; block splitting is deferred until needed.** 锚点 `^sec-2-positioning` … `^sec-14-summary` 已保留 / anchors are preserved.

版本 / Version: v1.1 | 日期 / Date: 2026-08-30 | SKU: `L1800C45DR220`

---

## 文档导航 / Document Navigation

| § | 章节 / Section | 本版 / This edition |
|---|---|---|
| 2 | 产品定位 / Product Positioning | ✅ |
| 3 | IT 容量 / IT Capacity | ✅ |
| 4 | 机架规格 / Rack Specifications | ✅ |
| 5 | 冷却系统 / Cooling System | ✅ |
| 6 | 配电规格 / Power Distribution | ✅ |
| 7 | 结构规格 / Structural Specifications | ✅ |
| 10 | 监控与管理 / Monitoring & Management | ✅ |
| 12 | 服务与支持 / Service & Support | ✅ |
| 13 | 选址与安装 / Site & Installation | ✅ |
| 14 | 参数汇总 / Key Specifications Summary | ✅ |
| 1 · 8 · 9 · 11 | 布局图 / 网络 / 环境与合规 / 消防与安全 —— Layout / Network / Environmental & Compliance / Fire Protection | **本版未收录；相关参数在技术澄清阶段提供 / Not included in this edition; these parameters are provided during technical clarification** |

---

## 2. 产品定位 / Product Positioning ^sec-2-positioning

**中文：** L1800C45 是 45ft High Cube 双环路直接液冷集装箱数据中心，单柜最大 220 kW，整箱 IT 容量 1800 kW，面向 GB300 NVL72 与 B300 HGX 这类 SXM / NVLink 机架级 GPU 系统。

这个产品服务的是一类很具体的场地条件：**电有了，地不够（out of floor, not power）。** 园区已经拿到变电容量、已有 MV 进线与变压器余量，甚至已经建好电力室，缺的是足够的、够高的、承重够的机房面积去摊开一片百千瓦级机柜。L1800C45 用单柜 220 kW 把同样的算力压进同一个 45ft 占地：一个集装箱占位换回 1800 kW IT。当场地按面积计价、或厂房层高与楼板荷载卡死扩容时，这个密度差就是决策依据。

同产品线内的分工：需要 UPS 与电池随箱到场、场站没有独立电力室时，选 [[L1240C45_Tech_Spec_External|L1240C45]]（单柜 150 kW，UPS 箱内）；45ft 箱体进不去的场地，选 [[L450C20_Tech_Spec_External|L450C20]]（20ft，450 kW）。

**English:** L1800C45 is a 45ft High Cube dual-loop direct-liquid-cooled containerized data center — up to 220 kW per rack and 1800 kW IT per container — built for rack-scale SXM / NVLink GPU systems such as GB300 NVL72 and B300 HGX.

It serves a very specific site condition: **you are out of floor, not out of power.** The campus already holds the substation capacity — an MV feed, spare transformer headroom, often a finished electrical room — but lacks the floor area, ceiling height and slab capacity to spread out a field of 100 kW-class racks. L1800C45 uses 220 kW per rack to compress the same compute into the same 45ft footprint: one container slot returns 1800 kW of IT. Where the site is charged by area, or where building height and floor loading cap expansion, that density delta is the decision basis.

Within the product line: choose [[L1240C45_Tech_Spec_External|L1240C45]] (150 kW per rack, UPS inside) when the site has no separate electrical room and wants UPS and batteries delivered with the container; choose [[L450C20_Tech_Spec_External|L450C20]] (20ft, 450 kW) where a 45ft container cannot physically enter.

---

## 3. IT 容量 / IT Capacity ^sec-3-it-capacity

| 项目 / Item | 参数 / Parameter |
|---|---|
| 整箱 IT 容量 / Total IT capacity | **1800 kW** |
| 单柜最大密度 / Maximum rack density | **220 kW**（密度码 / density code `R220`） |
| GPU 平台 / GPU platforms | **GB300 NVL72 · B300 HGX**（SXM / NVLink） |
| 环路 / Loops | 双环路 / Dual loop（`D`） |

### 3.1 IT Load 与 Total Facility Load 的区别 / IT Load vs Total Facility Load ^sec-3-it-vs-facility

**中文：** 这两个数不是一回事，谈容量前必须先对齐口径。

- **IT Load（IT 负荷）＝ 1800 kW** —— 服务器与 GPU 实际消耗的电功率，不含任何冷却与配电损耗。本文档中所有「1800 kW」均指 IT Load。
- **Total Facility Load（设施总负荷）＝ IT Load ＋ 冷却系统（CDU 泵、列间空调 风机、室外冷源）＋ 配电损耗 ＋ 辅助负荷。** 该数值随 **PUE** 变化，取决于站点气候与室外冷源方案，**必须逐站点计算** —— 入口为 <https://mdcx.org> 的 TCO / Designer。
- **PUE = `1.0x`** —— 不给固定值、不给区间。干冷器可全年排热的气候落在低端，更热的站点需加混合冷机、PUE 相应上移；具体数值请用 <https://mdcx.org> 按贵站点气候条件计算。

站点侧的变电申请、进线容量与开关柜选型必须按 Total Facility Load 计算，不能按 IT Load 计算。若贵方的「X MW」指的是电网侧可用容量，请在方案对齐会上明确说明，我方据此反算可支持的 IT 容量。

**English:** These are two different numbers and the basis must be aligned before any capacity discussion.

- **IT Load = 1800 kW** — the electrical power actually consumed by servers and GPUs, excluding all cooling and distribution losses. Every "1800 kW" in this document refers to IT Load.
- **Total Facility Load = IT Load + cooling (CDU pumps, 列间空调 fans, outdoor heat rejection) + distribution losses + auxiliaries.** The figure varies with **PUE** and depends on site climate and the outdoor heat-rejection scheme, so it **must be computed per site** — use the TCO / Designer at <https://mdcx.org>.
- **PUE = `1.0x`** — no fixed value and no range. Climates where dry coolers reject heat year-round sit at the low end; hotter sites need a hybrid chiller and PUE moves up accordingly. For a figure, run your site's climate through <https://mdcx.org>.

Utility applications, incoming feeder capacity and switchgear selection on the site side must be sized on Total Facility Load, not on IT Load. If your "X MW" refers to available grid capacity, please say so at the solution alignment meeting and we will work backwards to the supportable IT capacity.

---

## 4. 机架规格 / Rack Specifications ^sec-4-rack-spec

| 项目 / Item | 参数 / Parameter |
|---|---|
| 单柜最大功率 / Maximum rack power | **220 kW** |
| 冷却方式 / Cooling method | 冷板直接液冷（DLC），二次侧接 CDU TCS 回路 / Direct liquid cooling (cold plate), secondary side served by the CDU TCS loop |
| 适配 GPU 平台 / Supported GPU platforms | GB300 NVL72 · B300 HGX（SXM / NVLink） |

| 机柜构成 / Rack build | **8× 220 kW 液冷机柜 + 1× 40 kW 风冷机柜 = 9 柜**<br>8× 220 kW liquid-cooled racks + 1× 40 kW air-cooled rack = 9 racks |

> 机柜外形与 Manifold 配置随项目算力配置确定，在技术澄清阶段随布置图一并提供。
> Rack form factor and manifold configuration follow the project's compute configuration and are provided with the layout drawings during technical clarification.

---

## 5. 冷却系统（双环路） / Cooling System (Dual Loop) ^sec-5-cooling

### 5.1 架构 / Architecture ^sec-5-dual-loop

**中文：** L1800C45 箱内并行运行两条在介质、温位、水力上完全独立的回路。

| 回路 / Loop | 承担负荷 / Load carried | 温位 / Temperatures | 介质 / Fluid |
|---|---|---|---|
| **回路 A —— GPU 侧暖水 / Loop A — GPU-side warm water** | GPU / CPU 冷板液冷负荷（绝大部分 IT 热量）/ Cold-plate liquid load (the great majority of IT heat) | **GPU 冷板进水 36–40 °C**；外冷源出水 32–36 °C；CDU approach +4 °C · **GPU cold-plate inlet 36–40 °C**; outdoor-plant supply 32–36 °C; CDU approach +4 °C | 纯水，0% 乙二醇 / Pure water, 0% glycol |
| **回路 B —— 列间侧冷冻水 / Loop B — In-row CW chilled water** | 机房残余风冷负荷 / Residual room air load | **10 / 16 °C 冷冻水 / chilled water** | 纯水，0% 乙二醇 / Pure water, 0% glycol |

**为什么分成两条：** 冷板可以吃 40 °C 量级的水，风冷末端不行 —— 要把机房回风从 36 °C 降到 21 °C 送风，盘管进水必须在 10 °C 量级。并在同一条回路上，要么冷板侧被迫用冷水、浪费自然冷却时数并拉高 PUE，要么 列间侧冷量不足、送风温度失控。解耦之后，回路 A 的 36–40 °C 暖水在绝大多数气候下可由干冷器直接排掉，机械制冷只作补充；回路 B 的冷冻水负荷则小得多，冷机容量随之下降。这是把单柜密度做到 220 kW 的必要条件，也是能耗上的回报。

**Why two loops:** cold plates will take water in the 40 °C class; air-side terminals will not — dropping a 36 °C return to a 21 °C supply requires coil water in the 10 °C class. On a single loop, either the cold-plate side is forced onto cold water — throwing away free-cooling hours and raising PUE — or the in-row CW side runs short of capacity and supply temperature goes out of control. Decoupled, Loop A's 36–40 °C warm water can be rejected on dry coolers alone in most climates with mechanical cooling only as a topper, while Loop B carries a far smaller chilled-water load and a correspondingly smaller chiller. This is the precondition for a 220 kW rack, and it is where the energy return comes from.
> **GPU 侧温位链：** 外冷源（干冷器）出水 **32–36 °C** → 进 CDU 一次侧 → CDU 板换 approach **+4 °C** → **GPU 冷板进水 36–40 °C**。
> ***GPU-side temperature chain:*** *outdoor plant (dry cooler) supply **32–36 °C** → CDU primary side → plate-HX approach **+4 °C** → **GPU cold-plate inlet 36–40 °C**.*

> 已批 CDU 选型点 FWS 36/46 °C · TCS 40/50 °C 是这条链的**热端设计点**，approach 恰为 4 °C。
> *The approved CDU duty point of FWS 36/46 °C · TCS 40/50 °C is the **hot-end design point** of this chain, with an approach of exactly 4 °C.*

### 5.2 回路 A —— CDU / Loop A — CDU ^sec-5-cdu

板式换热器隔离一次侧 FWS（场站 / 干冷器侧）与二次侧 TCS（冷板侧），场站水质不进入冷板。
Plate heat exchangers isolate the primary FWS (site / dry-cooler side) from the secondary TCS (cold-plate side): site water quality never reaches the cold plates.

| 项目 / Item | 参数 / Parameter |
|---|---|
| 型号 / Model | **STULZ SCR 14103 W**（接口顶出 / connections up） |
| 单机换热容量 / Capacity per unit | **1200 kW** |
| FWS 进 / 出温度 / FWS inlet / outlet | **36 / 46 °C** |
| TCS 进 / 出温度 / TCS inlet / outlet | **40 / 50 °C** |
| 介质 / Fluid（一次 / 二次侧 · primary / secondary） | 纯水 / 纯水，乙二醇 0 / 0 % · Pure water / pure water, glycol 0 / 0 % |
| 板式换热器 / Plate heat exchangers | 2 台 / units · 逼近温差 / approach **4 °C** · 换热余量 / margin **41 %** |
| FWS / TCS 总流量 / total flow | **103.8 / 103.8 m³/h**（1.44 LPM/kW） |
| FWS / TCS 总压降 / total pressure drop | **140 / 195 kPa** |
| 泵组 / Pump set | 3 × CM 25-2 · 单泵 / each 6.7 kW · 总功率 / total **20.0 kW** |
| 干重 / 运行重量 · Dry / operating weight | **950 kg / 1,175 kg** |
| 外形（高 × 宽 × 深）/ Dimensions (H × W × D) | **2,090 × 900 × 1,200 mm** |
| 接口 / Connections | 4 × DN100（130 mm）**Tri-Clamp** · DIN 32676-B（ISO 1127），顶部出线 / top exit |
| 管路材质 / Pipework material | 不锈钢 / Stainless steel |
| 供电 / Electrical supply | 3Ph / N / PE / 380 V / 50 Hz |

| CDU 台数 / CDU units | **2× STULZ SCR 14103 W** |

> 冗余模型按项目可用性目标确定，在技术澄清阶段提供。
> Unit count and redundancy model (N+1 / 2N) follow the project's IT capacity and availability target, and are provided during technical clarification.

### 5.3 回路 B —— 列间空调 / Loop B — 列间空调 ^sec-5-crah

房间级下送风冷冻水型精密空调：全水盘管 + 两通调节阀，机内无压缩机、无制冷剂充注。
Room-level downflow chilled-water precision air conditioner: all-water coil plus a two-way control valve, no compressor and no refrigerant charge inside the unit.

| 项目 / Item | 参数 / Parameter |
|---|---|
| 型号 / Model | **STULZ CRS 560 CW** |
| 单机总冷量 / 显冷量 · Total / sensible capacity per unit | **57.3 / 57.3 kW**（全显冷 / fully sensible） |
| 净总冷量 / 净显冷量 · Net total / net sensible | 54.7 / 54.7 kW |
| 回风温度 / 湿度 · Return-air temperature / humidity | 36 °C / 25 % rel. |
| 送风温度 / Supply-air temperature | **21 °C**（ΔT = 15 K） |
| 风量 / 迎面风速 · Airflow / face velocity | **11,200 m³/h** / 2.7 m/s |
| 进 / 出水温度 · Water inlet / outlet | **10.0 / 16.0 °C** |
| 水侧流量 / Water flow | **8.2 m³/h** |
| 介质 / Fluid | 纯水，0% 乙二醇 / Pure water, 0% glycol |
| 水侧总压降 / Total water-side pressure drop | **52 kPa**（盘管 / coil 12 + 两通阀 / DN32 two-way valve 26 + 管路 / pipework 14） |
| 风机 / Fans | 3 × VBS0355STRHZ · 空气侧总压降 / total air-side drop 320 Pa |
| 总功耗 / EER · Total input / EER | **2.6 kW** / **21.04 kW/kW** |
| 声功率级 / 2 m 声压级 · Sound power / sound pressure at 2 m | 87.8 / 67.6 dB(A) |
| 外形（高 × 宽 × 深）/ 重量 · Dimensions (H × W × D) / weight | **2,000 × 600 × 1,375 mm** / **254 kg** |
| 供电 / Electrical supply | 400 V / 50 Hz / 3Ph / N / PE |
| 水管接口 / Water connections | 进 / 出各 1 只 1.5" 外螺纹 · 1 inlet + 1 outlet, 1.5" male thread |
| 选型海拔基准 / Altitude basis of selection | 0 m —— 非 0 海拔站点重新选型 / non-zero altitude sites are re-selected |

| 列间空调台数 / in-row CW units | **4× STULZ CRS 560 CW** |

> 冗余模型按项目 列间侧热负荷确定，在技术澄清阶段提供。
> Unit count and redundancy model follow the project's in-row CW heat load and are provided during technical clarification.

### 5.4 室外侧 / Outdoor side

| 项目 / Item | 参数 / Parameter |
|---|---|
| 回路 A 室外冷源 / Loop A heat rejection | 干冷器为主（36/46 °C 暖水，自然冷却时数长），峰值站点加机械补冷 —— **设计值，以最终选型为准** / Dry-cooler-led (long free-cooling hours on 36/46 °C warm water), mechanical topping at peak-climate sites — **design value, subject to final selection** |
| 回路 B 室外冷源 / Loop B heat rejection | 冷水机组（10/16 °C 冷冻水）—— **设计值，以最终选型为准** / Chiller plant (10/16 °C chilled water) — **design value, subject to final selection** |

> 室外侧排热基线与站点 PUE 取决于当地气候数据与室外冷源方案，在技术澄清阶段随热力计算提供。
> The outdoor heat-rejection baseline and site PUE depend on local climate data and the outdoor plant scheme, and are provided with the thermal calculations during technical clarification.

---

## 6. 配电规格 / Power Distribution ^sec-6-power

### 6.1 电力边界：UPS 在箱外 / Power boundary: the UPS sits outside

**中文：** L1800C45 的 UPS、电池与 PDC 置于集装箱之外，由场站提供。**这是一次刻意的边界设计，不是配置削减。** 它面向已有电力室、或愿意自建电力室的场站，换回三项收益：

1. **箱内空间全部让给算力。** 45ft 箱内不切电力舱，同样的占地容纳 1800 kW IT。
2. **后备时间不受箱体容积封顶。** UPS 在箱外时，电池规模与后备时长由贵方按自身可用性目标确定，可与柴发方案统筹。
3. **电力侧可独立扩容与检修。** UPS 扩容、电池更换、PDC 改造不需要动集装箱。

若贵方希望电力边界在箱外但不自建电力设施，MDCX 的独立电源模块（UPS / 电池 / PDC）在研，可在方案沟通中一并讨论。

**English:** On L1800C45 the UPS, batteries and PDC sit outside the container and are supplied by the site. **This is a deliberate boundary design, not a reduction in configuration.** It targets sites that already have — or are willing to build — an electrical room, and it buys back three things:

1. **All of the interior goes to compute.** No electrical bay is carved out of the 45ft shell, so the same footprint holds 1800 kW of IT.
2. **Backup time is not capped by the shell.** With the UPS outside, battery size and autonomy are set by you against your own availability target and can be coordinated with a genset scheme.
3. **The electrical side is expanded and maintained independently.** UPS expansion, battery replacement and PDC rework never touch the container.

If you want the boundary outside but do not intend to build the electrical infrastructure, MDCX's standalone power module (UPS / battery / PDC) is in development and can be discussed as part of the solution.

### 6.2 配电参数 / Distribution parameters

| 项目 / Item              | 参数 / Parameter                                                                                      |
| ---------------------- | --------------------------------------------------------------------------------------------------- |
| UPS 边界 / UPS boundary  | **箱外，由场站提供 UPS / 电池 / PDC** · **Outside the container; UPS / batteries / PDC supplied by the site** |
| 供电制式 / Supply voltages | **380 / 400 / 415 / 480 V AC**                                                                      |
| 800 V HVDC             | Roadmap Q3 2026，今日不供货 / roadmap Q3 2026, not shipping today                                         |
| CDU 供电 / CDU supply    | 3Ph / N / PE / 380 V / 50 Hz（泵组 20.0 kW/台 · pump set 20.0 kW per unit）                              |
| 列间空调 供电 / 列间空调 supply  | 400 V / 50 Hz / 3Ph / N / PE（2.6 kW/台 · per unit）                                                   |

---

## 7. 结构规格 / Structural Specifications ^sec-7-structural

| 项目 / Item | 参数 / Parameter |
|---|---|
| 箱型 / Container type | **45ft High Cube** |
| 外形尺寸（L × W × H）/ Exterior dimensions | **13,716 × 2,438 × 2,992 mm** —— **设计值，以最终图纸为准 / design value, subject to final drawings** |
| 上部模块高度 / Upper module height | 900 mm（一次侧互联总管内收 / primary-side interconnect headers pulled inboard） |
| CDU 运行重量 / CDU operating weight | 1,175 kg / 台 · per unit |
| 列间空调 干重 / 列间空调 dry weight | 254 kg / 台 · per unit |

> 空箱重、满载重与地基荷载要求随最终配置确定，在技术澄清阶段随结构荷载计算提供。
> Empty weight, loaded weight and foundation loading requirements follow the final configuration and are provided with the structural load calculations during technical clarification.

---

## 10. 监控与管理 / Monitoring & Management ^sec-10-monitoring

| 项目 / Item | 参数 / Parameter |
|---|---|
| **CIOS** | 每台 MDCX 均含：路径寻址遥测、告警转工单、运维工作流、用量计量 · Included with every MDCX: path-addressed telemetry, alarm-to-ticket, operations workflows, usage metering |
| 数字孪生 / Digital twin | **NVIDIA Omniverse** —— 实时状态投射到 3D 模型 · live state projected onto the 3D model |

---

## 12. 服务与支持 / Service & Support ^sec-12-service

### 12.1 价格 / Pricing

> **配置方案由 MDCX 工程团队提供，价格由商务团队核算，请联系客户经理获取正式报价。**
>
> **The configuration is produced by the MDCX engineering team; pricing is calculated by the commercial team. Please contact your account manager for a formal quotation.**

### 12.2 交付与服务 / Delivery and service

| 项目 / Item | 参数 / Parameter |
|---|---|
| **首批交期 / First-batch lead time** | **下单后 120 天 EXW · 120 days EXW from order placement** |
| **Scale 扩容批次交期 / Scale (expansion batch) lead time** | **90 天 EXW · 90 days EXW** |
| **假负载运行期 / Dummy-load burn-in period** | **5–30 天**，先以假负载验证供电与冷却链，再上真实算力；**不含在 EXW 承诺内**（来源：Supermicro 建议）· **5–30 days** of dummy-load burn-in to prove the power and cooling chain before real compute goes in; **not covered by the EXW commitment** (source: Supermicro recommendation) |
| 商务周期 / Commercial cycle | 合同、付款与采购周期**不予承诺** · Contract, payment and procurement cycles are **not committed** |
| 运输与清关 / Freight & customs | 买方自理，**不予承诺周期** · Buyer's responsibility; **no duration is committed** |
| 现场安装与调试 / On-site installation & commissioning | **不予承诺** · **Not committed** |
| 预制率 / Prefabrication ratio | **99% 出厂前完成 / completed before leaving the factory** |
| 质保期 / Warranty period | **核心部件，自 EXW 起一年** · **Core components, one year from EXW** |
| 后续年份 / Subsequent years | **按年收取服务费** · **Annual service fee** |
| 支持响应等级 / Support response level | **以 Invoice 为准** · **Governed by the Invoice** |
| 可用性设计目标 / Availability design target | **Tier II 投资，经差异化冗余达到 Tier III 级可用性 · Tier II investment reaching Tier III-class availability through differentiated redundancy** |
| 冗余原则 / Redundancy principle | 失效代价高处 2N，其余 N+1 —— 不做全局 2N · 2N where failure is expensive, N+1 elsewhere — no blanket 2N |

> **只承诺 EXW。** 商务、运输、安装三段不给天数、不给区间、不做估算。假负载运行期 5–30 天单独列出，明确不在 EXW 承诺内。ONSITE / NBD / 9×5 / 24×7 等响应级别条款以 Invoice 为准，本文档不定义。
> **EXW is the only commitment.** No day count, range or estimate is given for the commercial, freight or installation segments. The 5–30 day dummy-load burn-in is listed separately and is explicitly outside the EXW commitment. Response-level terms such as ONSITE / NBD / 9×5 / 24×7 are governed by the Invoice and are not defined in this document.

---

## 13. 选址与安装 / Site & Installation ^sec-13-site

| 项目 / Item | 要求 / Requirement |
|---|---|
| 场站须提供的电力设施 / Electrical infrastructure to be provided by the site | **UPS / 电池 / PDC**（见 §6.1）· **UPS / batteries / PDC** (see §6.1) |
| 场站须提供的冷却接口 / Cooling interfaces to be provided by the site | **两路独立**：回路 A 暖水（外冷源出水 32–36 °C，GPU 冷板进水 36–40 °C；选型点 FWS 36/46 °C）+ 回路 B 冷冻水（10/16 °C）。两路不可合并 · **Two independent services**: Loop A warm water (outdoor-plant supply 32–36 °C, GPU cold-plate inlet 36–40 °C; duty point FWS 36/46 °C) and Loop B chilled water (10/16 °C). They cannot be combined |
| CDU 接口形式 / CDU connection type | 4 × DN100 **Tri-Clamp**（DIN 32676-B），顶部出线；场站侧按卫生级卡箍配对，非法兰 · 4 × DN100 **Tri-Clamp** (DIN 32676-B), top exit; site pipework matched with sanitary clamps, not flanges |
| 列间空调 接口形式 / 列间空调 connection type | 进 / 出各 1 只 1.5" 外螺纹 · 1 inlet + 1 outlet, 1.5" male thread |
| 现场安装与调试 / On-site installation & commissioning | 不予承诺 / Not committed |
| 运费与清关 / Freight & customs | 买方自理，不予承诺周期 / Buyer's responsibility; no duration committed |
| 噪声（列间空调 单台）/ Noise (per in-row CW unit) | 声功率 87.8 dB(A) · 2 m 声压 67.6 dB(A) · Sound power 87.8 dB(A) · 67.6 dB(A) at 2 m |

> 地基承载、地面平整度、维护净距与多机噪声叠加随最终配置与布置确定，在技术澄清阶段提供。
> Foundation loading, ground levelness, maintenance clearances and multi-unit noise superposition follow the final configuration and layout, and are provided during technical clarification.

---

## 14. 参数汇总 / Key Specifications Summary ^sec-14-summary

| 项目 / Item | 参数 / Parameter |
|---|---|
| SKU | `L1800C45DR220` |
| 箱型 / Container type | 45ft High Cube |
| 外形尺寸 / Exterior dimensions | 13,716 × 2,438 × 2,992 mm（设计值 / design value） |
| **IT 容量 / IT capacity** | **1800 kW**（IT Load，非设施总负荷 · IT Load, not Total Facility Load） |
| 单柜最大密度 / Maximum rack density | **220 kW**（`R220`） |
| GPU 平台 / GPU platforms | GB300 NVL72 · B300 HGX（SXM / NVLink） |
| 环路 / Loops | 双环路 / Dual loop（`D`） |
| 回路 A / Loop A | GPU 冷板进水 36–40 °C；外冷源出水 32–36 °C；CDU approach +4 °C；选型点 FWS 36/46 · TCS 40/50 °C（热端设计点）· GPU cold-plate inlet 36–40 °C; outdoor-plant supply 32–36 °C; CDU approach +4 °C; duty point FWS 36/46 · TCS 40/50 °C (hot-end design point) |
| PUE | **`1.0x`** —— 逐站点用 <https://mdcx.org> 计算 · computed per site at <https://mdcx.org> |
| 回路 B / Loop B | 列间侧 10 / 16 °C 冷冻水 · in-row CW 10 / 16 °C chilled water |
| 介质 / Fluid | 纯水，0% 乙二醇 · Pure water, 0% glycol |
| CDU | STULZ SCR 14103 W · 1200 kW/台 · 103.8 m³/h · Tri-Clamp DN100 顶出 · 泵组 20.0 kW · per unit / top exit / 20.0 kW pump set |
| 列间空调 | STULZ CRS 560 CW · 57.3 kW/台（净 54.7）· 11,200 m³/h · 8.2 m³/h · 52 kPa · 400 V/50 Hz |
| UPS 边界 / UPS boundary | **箱外，由场站提供 · Outside the container, supplied by the site** |
| 供电制式 / Supply voltages | 380 / 400 / 415 / 480 V AC（800 V HVDC 为 Roadmap Q3 2026 · roadmap Q3 2026） |
| 软件 / Software | CIOS（含 / included）· NVIDIA Omniverse 数字孪生（含 / included） |
| 可用性 / Availability | Tier II 投资 → Tier III 级可用性 · Tier II investment → Tier III-class availability |
| 交期 / Lead time | 首批 120 天 EXW · Scale 90 天 EXW；假负载运行期 5–30 天（不含在 EXW 承诺内）；商务 / 运输 / 安装不予承诺 · 120 days EXW first batch, 90 days EXW for Scale; dummy-load burn-in 5–30 days (not covered by the EXW commitment); commercial, freight and installation are not committed |
| 质保 / Warranty | 核心部件自 EXW 起 1 年；后续年份按年收取服务费；响应级别以 Invoice 为准 · Core components one year from EXW; annual service fee thereafter; response level governed by the Invoice |
| 价格 / Price | 配置方案由 MDCX 工程团队提供，价格由商务团队核算，请联系客户经理获取正式报价 · Configuration by the MDCX engineering team; pricing by the commercial team — contact your account manager for a formal quotation |

---

## Changelog

| 版本 / Version | 日期 / Date | 变更摘要 / Summary |
|---|---|---|
| v1.1 | 2026-08-30 | **按 2026-08-30 Yuri 四条裁定更新（[[PRODUCT_SPEC_BASELINE]] v2.0）。** ① **双环路 GPU 侧温位链**：外冷源出水 32–36 °C → CDU approach +4 °C → GPU 冷板进水 **36–40 °C**（原「36–45 °C」上限 45 改 40，§5 / §13 / §14）。 ② **PUE 一律写 `1.0x`** —— 不给固定值、不给区间、不给「典型值」，逐站点用 <https://mdcx.org>（TCO / Designer）计算；Total Facility Load 的具体区间一并作废，改为「随 PUE 变化，逐站点计算」，但 IT Load vs Total Facility Load 的口径区分保留。 ③ **交期**写入正式承诺：首批 **120 天 EXW**、Scale **90 天 EXW**（自下单起算），假负载运行期 **5–30 天**（Supermicro 建议，**不含在 EXW 承诺内**）；商务 / 运输 / 安装**一律不予承诺**；删除「以商务合同为准」的占位写法与四阶段时间轴、「现场安装与调试 3–4 周」。 ④ **质保**写入正式承诺：核心部件**自 EXW 起一年**，后续年份**按年收取服务费**；ONSITE / NBD / 9×5 / 24×7 等响应级别条款**以 Invoice 为准**，本版不定义（原「1 年 / 9×5 NBD」已删除）。 本版仍不含任何价格数字，也不含任何未确认或源冲突标记。 · Updated to Yuri's four rulings of 2026-08-30: adjudicated GPU-side temperatures where applicable; PUE stated as `1.0x` and computed per site at <https://mdcx.org>; lead time committed as 120 days EXW first batch / 90 days EXW Scale with a 5–30 day dummy-load burn-in outside the EXW commitment and no commitment on the commercial, freight or installation segments; warranty committed as core components for one year from EXW plus an annual service fee, with response levels governed by the Invoice. No pricing and no unconfirmed-or-conflicted markers anywhere. |
| v1.0 | 2026-08-30 | 首版对外输出版（中英双语单文件）。本版收录已定型的产品参数、已批准的双环路 CDU / 列间空调选型参数，以及标注为「设计值」的工程推导值；仍在工程定型中的布局图、网络、环境与合规、消防与安全四节不在本版收录范围，已在导航表标注，相关参数在技术澄清阶段提供。§3 显式区分 IT Load 与 Total Facility Load；§6 说明 UPS 置于箱外的边界设计。交期以商务合同为准，全文不含交期数字与价格数字。锚点 `^sec-2-positioning` … `^sec-14-summary` 保留；本版为单文件，块拆分待需要时再做。 · First external edition (bilingual, single file). It carries the fixed product parameters, the approved dual-loop CDU / in-row CW selection data, and engineering values explicitly labelled as design values; Layout, Network, Environmental & Compliance and Fire Protection are outside its scope, flagged in the navigation table, and provided during technical clarification. §3 separates IT Load from Total Facility Load; §6 explains the external UPS boundary. Lead time is governed by the commercial contract; no lead-time figures and no pricing appear anywhere. |
