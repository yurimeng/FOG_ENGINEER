---
tags:
  - "#MDC"
  - "#type/design-spec"
  - "#product/l450c20"
doc_version: v1.1
updated: 2026-08-30
audience: 客户 / Customer（对外输出版）
sku_id: L450C20DR150
---

# L450C20 — Technical Specification（对外输出版 / External Edition）
**双环路直接液冷集装箱数据中心 · Dual-Loop Direct Liquid Cooled Container Data Center**
**20ft · 450 kW IT · 单柜 150 kW / 150 kW per rack**

> **受众 / Audience：** 客户。**本版是本 SKU 唯一允许直接发给客户的版本。**
> This edition is written for customers and is the only edition of this SKU cleared for direct release.
>
> **配套版本 / Companion editions：** [[L450C20_Tech_Spec_CN|中文内部版 / CN internal]] · [[L450C20_Tech_Spec_EN|English internal]]
>
> **数据源 / Source of truth：** 全部参数取自 [[PRODUCT_SPEC_BASELINE]]（六 SKU 规格基准表）。**参数争议以基准表为准。**
> All parameters are taken from [[PRODUCT_SPEC_BASELINE]]. **Where parameters disagree, the baseline table governs.**
>
> **本版收录范围 / Scope of this edition：** 仅收录已确认参数与标注为「设计值」的推导参数。本产品的设备选型与结构参数正在工程定型中，将在技术澄清阶段随图纸与计算书一并提供。
> This edition carries confirmed parameters plus derived parameters explicitly labelled as design values. Equipment selection and structural parameters for this product are in engineering definition and will be provided with drawings and calculations during technical clarification.
>
> **本版为单文件，块拆分待需要时再做 / This edition is a single file; block splitting is deferred until needed.** 锚点 `^sec-2-positioning` … `^sec-14-summary` 已保留 / anchors are preserved.

版本 / Version: v1.1 | 日期 / Date: 2026-08-30 | SKU: `L450C20DR150`

---

## 文档导航 / Document Navigation

| § | 章节 / Section | 本版 / This edition |
|---|---|---|
| 2 | 产品定位 / Product Positioning | ✅ |
| 3 | IT 容量 / IT Capacity | ✅ |
| 4 | 机架规格 / Rack Specifications | ✅ |
| 5 | 冷却系统 / Cooling System | ✅ 架构 / architecture |
| 6 | 配电规格 / Power Distribution | ✅ |
| 7 | 结构规格 / Structural Specifications | ✅ 箱型 / container type |
| 10 | 监控与管理 / Monitoring & Management | ✅ |
| 12 | 服务与支持 / Service & Support | ✅ |
| 13 | 选址与安装 / Site & Installation | ✅ |
| 14 | 参数汇总 / Key Specifications Summary | ✅ |
| 1 · 8 · 9 · 11 | 布局图 / 网络 / 环境与合规 / 消防与安全 —— Layout / Network / Environmental & Compliance / Fire Protection | **本版未收录；相关参数在技术澄清阶段提供 / Not included in this edition; these parameters are provided during technical clarification** |

---

## 2. 产品定位 / Product Positioning ^sec-2-positioning

**中文：** L450C20 是 20ft 双环路直接液冷集装箱数据中心，单柜最大 150 kW，整箱 IT 容量 450 kW。

**这个产品的存在理由，是一扇门。** 45ft High Cube 是 13.7 米长、近 3 米高的钢箱，它进不去很多地方：层高三米出头的老厂房、只有货梯的屋顶机房、限高涵洞之后的园区、乡道拐角转不过来的山地站点、吊车站位摆不开的密集城区。这些场地不缺电、也不缺需求，缺的是一条 45ft 箱能通过的物理路径。L450C20 用 20ft 标准箱型，把运输、吊装与通过性全部拉回最普通的一档。

**代价我们直说：单位算力成本高于 45ft 机型。** 双环路的 CDU、CRAH、两套管路、控制、消防与监控是固定投入，摊在 450 kW 上必然高于摊在 1240 kW 或 1800 kW 上。**这不是缺陷，这是为「塞得进那个舱位」付的钱。** 如果贵方场地能进 45ft 箱，我们会建议选 45ft 机型；选择 L450C20 的正当理由只有一个 —— 45ft 进不去。

同时请注意：**L450C20 不是大箱的减配版。** 它与 [[L1800C45_Tech_Spec_External|L1800C45]] 同为双环路架构、同样的 GPU 侧暖水 + CRAH 侧冷冻水温位体系，密度码 `R150` 与 [[L1240C45_Tech_Spec_External|L1240C45]] 相同。它是换了箱型重新排的产品。

**English:** L450C20 is a 20ft dual-loop direct-liquid-cooled containerized data center — up to 150 kW per rack and 450 kW IT per container.

**The reason this product exists is a doorway.** A 45ft High Cube is a steel box 13.7 m long and nearly 3 m tall, and there are many places it cannot enter: legacy buildings with barely three metres of clear height, rooftop plant rooms served only by a goods lift, campuses behind a height-restricted underpass, hill sites where a rural bend cannot be negotiated, dense urban plots where a crane has nowhere to stand. Those sites are short of neither power nor demand — they are short of a physical route a 45ft box can travel. L450C20 uses a 20ft standard shell to put transport, lifting and access back into the most ordinary category there is.

**We will say the cost plainly: cost per unit of compute is higher than on the 45ft machines.** A dual-loop CDU, CRAH, two pipework systems, controls, fire protection and monitoring are fixed investments; amortised over 450 kW they are necessarily higher than over 1240 kW or 1800 kW. **That is not a defect; it is the price of fitting through the opening.** If your site can take a 45ft container we will recommend a 45ft machine. There is exactly one legitimate reason to choose L450C20: a 45ft container cannot get in.

Note also that **L450C20 is not a stripped-down large container.** It shares the dual-loop architecture and the GPU warm-water / CRAH chilled-water scheme with [[L1800C45_Tech_Spec_External|L1800C45]], and shares the `R150` density code with [[L1240C45_Tech_Spec_External|L1240C45]]. It is a different shell, laid out from scratch.

---

## 3. IT 容量 / IT Capacity ^sec-3-it-capacity

| 项目 / Item | 参数 / Parameter |
|---|---|
| 整箱 IT 容量 / Total IT capacity | **450 kW** |
| 单柜最大密度 / Maximum rack density | **150 kW**（密度码 / density code `R150`） |
| 环路 / Loops | 双环路 / Dual loop（`D`） |

### 3.1 IT Load 与 Total Facility Load 的区别 / IT Load vs Total Facility Load ^sec-3-it-vs-facility

**中文：** 这两个数不是一回事，谈容量前必须先对齐口径。

- **IT Load（IT 负荷）＝ 450 kW** —— 服务器与 GPU 实际消耗的电功率，不含任何冷却与配电损耗。本文档中所有「450 kW」均指 IT Load。
- **Total Facility Load（设施总负荷）＝ IT Load ＋ 冷却系统（CDU 泵、CRAH 风机、室外冷源）＋ 配电损耗 ＋ 辅助负荷。** 该数值随 **PUE** 变化，取决于站点气候与室外冷源方案，**必须逐站点计算** —— 入口为 <https://mdcx.org> 的 TCO / Designer。
- **PUE = `1.0x`** —— 不给固定值、不给区间。干冷器可全年排热的气候落在低端，更热的站点需加混合冷机、PUE 相应上移；具体数值请用 <https://mdcx.org> 按贵站点气候条件计算。

站点侧的变电申请、进线容量与开关柜选型必须按 Total Facility Load 计算，不能按 IT Load 计算。若贵方的「X MW」指的是电网侧可用容量，请在方案对齐会上明确说明，我方据此反算可支持的 IT 容量。

**English:** These are two different numbers and the basis must be aligned before any capacity discussion.

- **IT Load = 450 kW** — the electrical power actually consumed by servers and GPUs, excluding all cooling and distribution losses. Every "450 kW" in this document refers to IT Load.
- **Total Facility Load = IT Load + cooling (CDU pumps, CRAH fans, outdoor heat rejection) + distribution losses + auxiliaries.** The figure varies with **PUE** and depends on site climate and the outdoor heat-rejection scheme, so it **must be computed per site** — use the TCO / Designer at <https://mdcx.org>.
- **PUE = `1.0x`** — no fixed value and no range. Climates where dry coolers reject heat year-round sit at the low end; hotter sites need a hybrid chiller and PUE moves up accordingly. For a figure, run your site's climate through <https://mdcx.org>.

Utility applications, incoming feeder capacity and switchgear selection on the site side must be sized on Total Facility Load, not on IT Load. If your "X MW" refers to available grid capacity, please say so at the solution alignment meeting and we will work backwards to the supportable IT capacity.

---

## 4. 机架规格 / Rack Specifications ^sec-4-rack-spec

| 项目 / Item | 参数 / Parameter |
|---|---|
| 单柜最大功率 / Maximum rack power | **150 kW** |
| 冷却方式 / Cooling method | 冷板直接液冷（DLC），二次侧接 CDU 回路 / Direct liquid cooling (cold plate), secondary side served by the CDU loop |

| 机柜构成 / Rack build | **3× 150 kW 液冷机柜，无风冷机柜**<br>3× 150 kW liquid-cooled racks, no air-cooled rack |

> 机柜外形、Manifold 配置与适配 GPU 平台随项目算力配置确定，在技术澄清阶段随布置图一并提供。
> Rack form factor, manifold configuration and supported GPU platforms follow the project's compute configuration and are provided with the layout drawings during technical clarification.

---

## 5. 冷却系统（双环路） / Cooling System (Dual Loop) ^sec-5-cooling

### 5.1 架构 / Architecture ^sec-5-dual-loop

**中文：** L450C20 箱内并行运行两条在介质、温位、水力上完全独立的回路。

| 回路 / Loop | 承担负荷 / Load carried | 温位 / Temperatures |
|---|---|---|
| **回路 A —— GPU 侧暖水 / Loop A — GPU-side warm water** | GPU / CPU 冷板液冷负荷（绝大部分 IT 热量）/ Cold-plate liquid load (the great majority of IT heat) | **GPU 冷板进水 36–40 °C**；外冷源出水 32–36 °C；CDU approach +4 °C · **GPU cold-plate inlet 36–40 °C**; outdoor-plant supply 32–36 °C; CDU approach +4 °C |
| **回路 B —— CRAH 侧冷冻水 / Loop B — CRAH-side chilled water** | 机房残余风冷负荷 / Residual room air load | **10 / 16 °C 冷冻水 / chilled water** |

**为什么分成两条：** 冷板可以吃 40 °C 量级的水，风冷末端不行 —— 要把机房回风降到可用的送风温度，盘管进水必须在 10 °C 量级。并在同一条回路上，要么冷板侧被迫用冷水、浪费自然冷却时数并拉高 PUE，要么 CRAH 侧冷量不足。解耦之后，回路 A 的 36–40 °C 暖水在绝大多数气候下可由干冷器直接排掉，机械制冷只作补充；回路 B 的冷冻水负荷则小得多。

**在 20ft 箱体里实现双环路，是本产品的核心工程工作：** 两套泵组、两套管路、两组外部接口、两套定压补水，全部要排进约六米长的箱内。这也是本产品的设备选型必须针对 20ft 单独完成、不能从 45ft 机型平移的原因。

**Why two loops:** cold plates will take water in the 40 °C class; air-side terminals will not — bringing room return air down to a usable supply temperature requires coil water in the 10 °C class. On a single loop, either the cold-plate side is forced onto cold water — throwing away free-cooling hours and raising PUE — or the CRAH side runs short of capacity. Decoupled, Loop A's 36–40 °C warm water can be rejected on dry coolers alone in most climates with mechanical cooling only as a topper, while Loop B carries a far smaller chilled-water load.
> **GPU 侧温位链：** 外冷源（干冷器）出水 **32–36 °C** → 进 CDU 一次侧 → CDU 板换 approach **+4 °C** → **GPU 冷板进水 36–40 °C**。
> ***GPU-side temperature chain:*** *outdoor plant (dry cooler) supply **32–36 °C** → CDU primary side → plate-HX approach **+4 °C** → **GPU cold-plate inlet 36–40 °C**.*


**Realising a dual loop inside a 20ft shell is this product's central engineering task:** two pump sets, two pipework systems, two sets of external connections and two pressurisation / make-up arrangements all have to be routed inside roughly six metres. That is also why the equipment selection for this product is carried out specifically for the 20ft shell rather than transplanted from the 45ft machines.

### 5.2 室外侧 / Outdoor side

| 项目 / Item | 参数 / Parameter |
|---|---|
| 回路 A 室外冷源 / Loop A heat rejection | 干冷器为主（出水 32–36 °C，自然冷却时数长），峰值站点加机械补冷 —— **设计值，以最终选型为准** / Dry-cooler-led (long free-cooling hours at a 32–36 °C supply), mechanical topping at peak-climate sites — **design value, subject to final selection** |
| PUE | **`1.0x`** —— 不给固定值、不给区间，逐站点用 <https://mdcx.org>（TCO / Designer）计算 · **`1.0x`** — no fixed value and no range; computed per site with the TCO / Designer at <https://mdcx.org> |
| 回路 B 室外冷源 / Loop B heat rejection | 冷水机组（10/16 °C 冷冻水）—— **设计值，以最终选型为准** / Chiller plant (10/16 °C chilled water) — **design value, subject to final selection** |

| CDU | **1× STULZ SCR 14103 W** |
| CRAH | **2× STULZ CRS 330 CW，N+1 冗余 / 2× STULZ CRS 330 CW, N+1** |

> CDU 与 CRAH 的单台容量参数，以及室外侧排热基线，在技术澄清阶段随热力计算与选型书一并提供。站点 PUE 请用 <https://mdcx.org> 的 TCO / Designer 按贵站点气候条件计算。
> CDU and CRAH models, capacities, quantities and redundancy models, together with the outdoor heat-rejection baseline, are provided with the thermal calculations and selection sheets during technical clarification. For the site PUE, run your site's climate through the TCO / Designer at <https://mdcx.org>.

^sec-5-crah

---

## 6. 配电规格 / Power Distribution ^sec-6-power

### 6.1 电力边界：UPS 在箱外 / Power boundary: the UPS sits outside

**中文：** L450C20 的 UPS、电池与 PDC 置于集装箱之外，由场站提供。**这是一次刻意的边界设计，不是配置削减。**

在 20ft 箱型上，这个选择尤其直接：一个 20ft 箱的内部长度约为 45ft High Cube 的 44%。要同时容纳算力机柜、双环路的两套泵组与管路、配电、消防与监控，再切出能装下 UPS 与电池组的电力舱，450 kW 的 IT 容量就无从谈起。把电力边界放在箱外，换回来的是：

1. **箱内空间全部让给算力与双环路管路** —— 这是 450 kW 能在 20ft 里成立的前提。
2. **后备时间不受箱体容积封顶**，由贵方按自身可用性目标确定，可与柴发方案统筹。
3. **电力侧可独立扩容与检修**，UPS 扩容与电池更换不需要动集装箱。

若贵方希望电力边界在箱外但不自建电力设施，MDCX 的独立电源模块（UPS / 电池 / PDC）在研，可在方案沟通中一并讨论。

**English:** On L450C20 the UPS, batteries and PDC sit outside the container and are supplied by the site. **This is a deliberate boundary design, not a reduction in configuration.**

On a 20ft shell the choice is particularly direct: a 20ft container's internal length is about 44% of a 45ft High Cube's. Fit compute racks, two dual-loop pump sets and pipework systems, distribution, fire protection and monitoring inside it, then carve out an electrical bay large enough for a UPS and a battery string, and 450 kW of IT capacity stops being achievable. Putting the boundary outside buys back:

1. **All of the interior goes to compute and dual-loop pipework** — the precondition for 450 kW existing in a 20ft shell at all.
2. **Backup time is not capped by the shell**; you set it against your own availability target and can coordinate it with a genset scheme.
3. **The electrical side is expanded and maintained independently** — UPS expansion and battery replacement never touch the container.

If you want the boundary outside but do not intend to build the electrical infrastructure, MDCX's standalone power module (UPS / battery / PDC) is in development and can be discussed as part of the solution.

### 6.2 配电参数 / Distribution parameters

| 项目 / Item | 参数 / Parameter |
|---|---|
| UPS 边界 / UPS boundary | **箱外，由场站提供 UPS / 电池 / PDC** · **Outside the container; UPS / batteries / PDC supplied by the site** |
| 供电制式 / Supply voltages | **380 / 400 / 415 / 480 V AC** |
| 800 V HVDC | Roadmap Q3 2026，今日不供货 / roadmap Q3 2026, not shipping today |

---

## 7. 结构规格 / Structural Specifications ^sec-7-structural

| 项目 / Item | 参数 / Parameter |
|---|---|
| 箱型 / Container type | **20ft** |

> **外形尺寸、空箱重与满载重以最终图纸为准，将在技术澄清阶段提供。**
> **Exterior dimensions, empty weight and loaded weight follow the final drawings and will be provided during technical clarification.**
>
> 由于本产品的核心应用场景正是「45ft 进不去」的受限场地，我方建议在项目启动阶段即由贵方提供以下现场条件，作为方案输入：**运输路径的限高与限宽、转弯半径、桥涵与地磅承载、吊装作业面与吊车站位、机房门洞与楼板荷载。** 我方将据此确认可行性并出具落位方案。
> Because this product exists precisely for sites a 45ft container cannot enter, we recommend that the following site conditions be supplied at project kick-off as design inputs: **clearance height and width along the haul route, turning radii, bridge/culvert and weighbridge capacity, the lifting working face and crane positions, door openings and floor loading.** We will confirm feasibility and issue a placement scheme on that basis.

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
| 场站须提供的冷却接口 / Cooling interfaces to be provided by the site | **两路独立**：回路 A 暖水（外冷源出水 32–36 °C，GPU 冷板进水 36–40 °C）+ 回路 B 冷冻水（10/16 °C）。两路不可合并 · **Two independent services**: Loop A warm water (outdoor-plant supply 32–36 °C, GPU cold-plate inlet 36–40 °C) and Loop B chilled water (10/16 °C). They cannot be combined |
| 现场安装与调试 / On-site installation & commissioning | 不予承诺 / Not committed |
| 运费与清关 / Freight & customs | 买方自理，不予承诺周期 / Buyer's responsibility; no duration committed |
| **运输与通过性条件 / Transport and access conditions** | 本产品的关键项目输入，见 §7 清单 · The key project input for this product; see the list in §7 |

> 冷却接口形式与尺寸、地基承载、地面平整度与维护净距随最终设备选型与布置确定，在技术澄清阶段提供。
> Cooling connection types and sizes, foundation loading, ground levelness and maintenance clearances follow the final equipment selection and layout, and are provided during technical clarification.

---

## 14. 参数汇总 / Key Specifications Summary ^sec-14-summary

| 项目 / Item | 参数 / Parameter |
|---|---|
| SKU | `L450C20DR150` |
| 箱型 / Container type | **20ft** |
| **IT 容量 / IT capacity** | **450 kW**（IT Load，非设施总负荷 · IT Load, not Total Facility Load） |
| 单柜最大密度 / Maximum rack density | **150 kW**（`R150`） |
| 环路 / Loops | 双环路 / Dual loop（`D`） |
| 回路 A / Loop A | GPU 冷板进水 36–40 °C；外冷源出水 32–36 °C；CDU approach +4 °C · GPU cold-plate inlet 36–40 °C; outdoor-plant supply 32–36 °C; CDU approach +4 °C |
| PUE | **`1.0x`** —— 逐站点用 <https://mdcx.org> 计算 · computed per site at <https://mdcx.org> |
| 回路 B / Loop B | CRAH 侧 10 / 16 °C 冷冻水 · CRAH-side 10 / 16 °C chilled water |
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
| v1.0 | 2026-08-30 | 首版对外输出版（中英双语单文件）。本版收录已定型的产品参数（IT 容量、单柜密度、双环路温位、电力边界）与标注为「设计值」的工程推导值；设备选型、外形尺寸与结构参数正在工程定型中，不在本版收录范围，将在技术澄清阶段随图纸与选型书提供。布局图、网络、环境与合规、消防与安全四节同理，已在导航表标注。§3 显式区分 IT Load 与 Total Facility Load；§6 说明 UPS 置于箱外的边界设计；§7 就受限场地的运输通过性条件列出项目输入清单。交期以商务合同为准，全文不含交期数字与价格数字。锚点 `^sec-2-positioning` … `^sec-14-summary` 保留；本版为单文件，块拆分待需要时再做。 · First external edition (bilingual, single file). It carries the fixed product parameters (IT capacity, rack density, dual-loop temperatures, power boundary) plus engineering values explicitly labelled as design values; equipment selection, exterior dimensions and structural parameters are in engineering definition, outside its scope, and provided with drawings and selection sheets during technical clarification, as are the Layout, Network, Environmental & Compliance and Fire Protection sections flagged in the navigation table. §3 separates IT Load from Total Facility Load; §6 explains the external UPS boundary; §7 lists the transport-access inputs needed for restricted sites. Lead time is governed by the commercial contract; no lead-time figures and no pricing appear anywhere. |
