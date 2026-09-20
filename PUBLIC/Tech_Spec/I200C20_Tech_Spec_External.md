---
tags:
  - "#MDC"
  - "#type/design-spec"
  - "#product/i200c20"
doc_version: v1.1
updated: 2026-08-30
audience: 客户（对外输出版 · 可直接发送）/ Customer-facing (releasable)
sku_id: I200C20ST50
---

# I200C20 — Technical Specification（对外输出版 · External Release） ^mdc-cf07e6d6f4
**20ft 单相浸没式液冷算力舱 · 20ft single-phase immersion compute bay**

> **受众 Audience：** 客户。本版为**唯一允许直接发给客户**的 I200C20 技术规格文件。 ^mdc-8ee1edf65a
> *Customers. This is the only I200C20 specification document approved for direct release.* ^mdc-beed6411e8
>
> **配套版本 Companion versions：** 中文内部版 [[I200C20_Tech_Spec_CN]] · 英文内部版 [[I200C20_Tech_Spec_EN]]
>
> **数据源 Data source：** 全部参数取自 [[PRODUCT_SPEC_BASELINE]]（六 SKU 规格基准表 v1.0 / 2026-08-30）。**本版仅收录已确认（✅）与我方推导（🔶 设计值）参数**；尚未确认的参数不在本版出现，将在技术澄清阶段以书面形式提供。
> *All parameters are taken from the MDCX six-SKU baseline. This edition carries only confirmed values and clearly labelled design values; parameters still under engineering confirmation do not appear here and will be issued in writing during technical clarification.*
>
> **参数争议以基准表为准 / The baseline table settles parameter disputes.**

---

## 文档导航 · Document Navigation

> **本版为单文件，块拆分待需要时再做。** 章节锚点（`^sec-1-layout` … `^sec-14-summary`）与内部版一致，编号保持对齐，因此本版章节号不连续。
> *This edition is a single file; block splitting will be done if and when it is needed. Section anchors and numbering are kept aligned with the internal editions, so the section numbers in this edition are not consecutive.*

| § | 章节 · Section | 锚点 · Anchor | 状态 · Status |
|---|----------------|---------------|---------------|
| 1 | 布局 · Layout | `^sec-1-layout` | **本版未收录** —— 布置图将在技术澄清阶段以图纸形式提供；舱段构成见 §2 · *Not in this edition; the general arrangement is issued as drawings during technical clarification — bay composition is in §2* |
| 2 | 产品定位 · Product Positioning | `^sec-2-positioning` | 收录 · Included |
| 3 | IT 容量与设施总负荷 · IT Capacity and Total Facility Load | `^sec-3-it-capacity` | 收录 · Included |
| 4 | 浸没槽规格 · Immersion Tank Specification | `^sec-4-rack-spec` | 收录 · Included |
| 5 | 冷却系统 · Cooling System | `^sec-5-cooling` | 收录 · Included |
| 6 | 配电规格 · Power Distribution | `^sec-6-power` | 收录 · Included |
| 7 | 结构规格 · Structural | `^sec-7-structural` | **本版未收录** —— 尺寸与重量将在技术澄清阶段以书面图纸提供 · *Not in this edition; dimensions and weights are issued as drawings during technical clarification* |
| 8 | 网络与线缆管理 · Network & Cabling | `^sec-8-network` | **本版未收录** —— 属项目级设计 · *Not in this edition; project-level design* |
| 9 | 环境与合规 · Environmental & Compliance | `^sec-9-environment` | 收录 · Included |
| 10 | 监控与管理 · Monitoring & Management | `^sec-10-monitoring` | 收录 · Included |
| 11 | 消防与安全 · Fire Protection & Safety | `^sec-11-fire` | **本版未收录** —— 按部署地消防规范做项目级设计 · *Not in this edition; designed per the fire code of the deployment jurisdiction* |
| 12 | 服务与交付 · Service & Delivery | `^sec-12-service` | 收录 · Included |
| 13 | 选址与安装 · Site & Installation | `^sec-13-site` | 收录 · Included |
| 14 | 主要参数汇总 · Key Specifications Summary | `^sec-14-summary` | 收录 · Included |

---

## 2. 产品定位 · Product Positioning ^sec-2-positioning

**I200C20 是 45 英尺进不去时的推理密度。** ^mdc-0333e8a331

它面向的场地条件很具体：城市既有厂房内的一块空地、屋顶、地下空间、旧机房改造、道路转弯半径吃不下 40/45 英尺箱的园区 —— **场地本身决定了只能放 20 英尺，而算力需求并没有因此降低**。I200C20 的回答不是把密度降下来迁就箱型，而是在 20 英尺里保持与 400 kW 产品**完全相同的单槽密度**：4 台浸没槽，每槽 50 kW，200 kW IT。 ^mdc-68988590c1

**同密度、一半槽数、为不同的场地约束而造。** 选择 I200C20 的通常原因不是预算，而是场地进不去。 ^mdc-ee31054b18

***I200C20 is inference density for when 45 feet will not fit.*** ^mdc-c8094998a5

*The site conditions it addresses are specific: a clear patch inside an existing urban plant building, a rooftop, an underground space, a legacy machine room being converted, a campus whose turning radii cannot take a 40 or 45ft box — **the site itself dictates 20 feet, and the compute requirement has not shrunk to match**. The I200C20 answer is not to lower density to suit the form factor, but to hold inside 20 feet exactly the **same per-tank density** as the 400 kW products: four immersion tanks, 50 kW each, 200 kW of IT.* ^mdc-12b54cec90

***The same density, half the tank count, built for a different site constraint.*** *The reason to choose I200C20 is usually not budget — it is that the site will not take a bigger box.* ^mdc-7508ffe173

| 维度 · Dimension | 定位 · Positioning |
|------------------|--------------------|
| 产品线 · Product line | Immersion Cooling（单相浸没）· Single-phase immersion |
| SKU | `I200C20ST50` ^mdc-bf4cd1797e |
| IT 容量 · IT capacity | 200 kW |
| 构成单元 · Building blocks | 4× 浸没槽 · 4 immersion tanks |
| 单槽密度 · Per-tank density | **50 kW —— 与 400 kW 产品相同** · 50 kW, identical to the 400 kW products |
| 电力边界 · Power boundary | **箱外**（客户 / 场站侧提供 UPS、电池与配电）· **Outside the box** (customer / site supplies UPS, batteries, distribution) |
| 箱型 · Container | 20ft 算力舱 · 20ft compute bay |
| 舱段构成 · Bay composition | 单一算力舱（4× 浸没槽 + 运维通道），电力设备在箱外 · A single compute bay (4 tanks + service aisle); electrical plant outside |
| 状态 · Status | 已量产交付 · Shipped |

### 2.1 浸没线三个产品的关系 · How the three immersion products relate

| 产品 · Product | SKU | 箱型 · Container | IT | 槽数 · Tanks | 单槽密度 · Per-tank | UPS 边界 · UPS boundary |
|----------------|-----|------------------|-----|--------------|---------------------|-------------------------|
| I400C45 | `I400C45SUT50` | 45ft（含电力舱）· with power bay | 400 kW | 8 | 50 kW | 箱内 · Inside ^mdc-07256bf469 |
| I400C40 | `I400C40ST50` | 40ft | 400 kW | 8 | 50 kW | 箱外 · Outside ^mdc-590813dccc |
| **I200C20** | `I200C20ST50` | **20ft** | **200 kW** | **4** | **50 kW** | **箱外 · Outside** ^mdc-1119454142 |

> 三者同密度不同规模。选型的第一问不是「要多少 kW」，而是**场地能放下多长的箱子、以及电力边界在哪一侧**。
> *The three are the same density at different scale. The first selection question is not "how many kW" but **how long a box the site can take, and which side the power boundary sits on**.*

---

## 3. IT 容量与设施总负荷 · IT Capacity and Total Facility Load ^sec-3-it-capacity

200 kW 是**槽内 IT 有功**，不是站端进线容量。这两个口径服务于两个不同的决策：IT Load 决定买到多少算力，Total Facility Load 决定变电容量申请与电费测算。

*200 kW is **IT real power inside the tanks**, not the site service capacity. The two measures serve two different decisions: IT Load determines how much compute is purchased; Total Facility Load determines the substation capacity applied for and the electricity cost model.*

| 项目 · Item | 参数 · Specification |
|-------------|----------------------|
| **IT Load** | **200 kW** —— 4 个浸没槽内服务器 / GPU 的实际有功 · Real power of the servers / GPUs inside the four tanks |
| 浸没槽 · Immersion tanks | 4 台，每槽 50 kW · 4 tanks at 50 kW each |
| GPU 平台 · GPU platforms | 4090 · 5090 · RTX PRO 6000 · H100 · H200（PCIe） |

> **Total Facility Load 与 IT Load 是两个不同的数。** 设施总负荷 = IT + 槽内 CDU 泵功 + 室外排热电耗 + 配电损耗 + 辅机。I200C20 的 UPS 在箱外，其损耗计入站端而非本箱。**站端总用电取决于站点气候与冷源选型，须逐站核算**，MDCX 将在技术澄清阶段以书面形式提供该项计算结果。 ^mdc-57b8b16a97
> ***Total Facility Load and IT Load are two different numbers.*** *Facility load = IT + in-tank CDU pump power + outdoor rejection energy + distribution losses + auxiliaries. On I200C20 the UPS sits outside the box, so its losses land in site capacity rather than in this container. **Total site power depends on site climate and heat-rejection selection and is calculated per site**; MDCX issues that calculation in writing during technical clarification.* ^mdc-b5fcfa18f5

---

## 4. 浸没槽规格 · Immersion Tank Specification ^sec-4-rack-spec

I200C20 使用的浸没槽**与 400 kW 产品是同一款槽体**，槽数不同而已 —— 运维方式、备件与操作规程通用。 ^mdc-64166810c5

*I200C20 uses **the same tank** as the 400 kW products, only fewer of them — O&M practice, spares and operating procedures are common.* ^mdc-4d68c1cbc3

| 项目 · Item | 参数 · Specification |
|-------------|----------------------|
| 数量（整箱）· Quantity per container | 4 |
| 单槽 IT 容量 · IT capacity per tank | 50 kW |
| 冷却方式 · Cooling method | 单相浸没 · Single-phase immersion |
| 槽内 CDU · In-tank CDU | 双 CDU · **2N 完全冗余** · Dual CDU, fully redundant 2N |
| 油侧 ΔT · Oil-side ΔT | 8 K |
| 单槽油流量 · Oil flow per tank | ≈11–12 m³/h |
| 支持 GPU 平台 · Supported GPU platforms | 4090 · 5090 · RTX PRO 6000 · H100 · H200（PCIe） |

---

## 5. 冷却系统 · Cooling System ^sec-5-cooling

服务器整机浸入介电液，热量由槽内 CDU 的板式换热器交给设施水，再由室外冷源排入大气。没有服务器风扇，没有冷热通道 —— **这套架构在 I200C20 上与 400 kW 产品完全一致，只是槽数从 8 变成 4**，这也是 20 英尺箱能承载 200 kW 而不需要降密度的原因。 ^mdc-5c046bd3da

*Whole servers sit in dielectric fluid; the in-tank CDU plate heat exchangers hand that heat to facility water, and the outdoor plant rejects it to atmosphere. There are no server fans and no hot and cold aisles — **on I200C20 this architecture is identical to the 400 kW products, only with four tanks instead of eight**, which is why a 20ft box carries 200 kW without derating density.* ^mdc-928008d33a

```
IT Load → 介电液 Dielectric fluid (4×) → 双 CDU 板换 Dual CDU plate HX (2N) → 设施水 Facility water
                                                                                        ↓
                    干冷器为主 Dry coolers primarily; 峰值站点加混合冷机 Hybrid Chiller at peak-climate sites
```

### 5.1 设计工况 · Design conditions

| 项目 · Item | 参数 · Specification | 备注 · Notes |
|-------------|----------------------|--------------|
| 冷却方式 · Cooling method | 单相浸没 · Single-phase immersion | — |
| 槽内 CDU 配置 · In-tank CDU | 每槽双 CDU · **2N** · Dual CDU per tank, 2N | — |
| 油侧 ΔT · Oil-side ΔT | **8 K** | — |
| 单槽油流量 · Oil flow per tank | **≈11–12 m³/h** | — |
| 整箱二次侧流量 · Container secondary flow | **≈44–48 m³/h** | **设计值**，由单槽流量 × 4 推出，以最终选型为准 · **Design value**, derived from per-tank flow × 4, subject to final selection |
| 室外冷源 · Outdoor heat source | 干冷器为主；峰值站点加混合冷机 · Dry coolers primarily; Hybrid Chiller at peak-climate sites | — |

> 设施水温位按站点冷源选型确定，将在技术澄清阶段以书面形式提供。
> *Facility water temperatures follow the site's heat-rejection selection and are issued in writing during technical clarification.*

### 5.2 PUE · PUE ^sec-5-pue

| 项目 · Item | 参数 · Specification |
|-------------|----------------------|
| PUE | **`1.0x`** —— 不给固定值、不给区间。最终值由场地环境决定，**逐站点计算**，入口 <https://mdcx.org>（TCO / Designer）· **`1.0x`** — no fixed value and no range. The final figure is set by site conditions and is **computed per site** with the TCO / Designer at <https://mdcx.org> |

> 干冷器可全年排热的气候落在低端；更热的站点需加装混合冷机，PUE 相应上移。请用 <https://mdcx.org> 按贵站点气候条件计算具体数值。
> *Climates where dry coolers reject heat year-round sit at the low end; hotter sites require a hybrid chiller and PUE moves up accordingly. Run your site's climate through <https://mdcx.org> for the figure.*

### 5.3 故障模式 · Failure modes

**设计值 · Design values** —— 由 2N 冗余架构推出的运行影响，以最终设计为准。
*Operational consequences derived from the 2N redundancy architecture; subject to final design.*

| 故障 · Failure | 影响 · Impact |
|----------------|---------------|
| 单 CDU 故障 · Single CDU failure | 无影响，另一台 CDU 承担全槽负荷 · None; the other CDU carries the whole tank |
| 双 CDU 同时故障 · Both CDUs fail | 该槽停机，其余 3 槽不受影响 · That tank shuts down; the other three are unaffected |
| 室外冷源失效 · Outdoor plant failure | 设施水温上升，需降载或停机 · Facility water temperature rises; derate or shut down |
| 板换 / 过滤器堵塞 · Fouled plate HX or filter | 换热效率下降，油温抬升 · Reduced heat transfer, rising oil temperature |

> 4 槽箱的单槽停机影响为 25% 算力（8 槽箱为 12.5%）。冗余单位仍是整箱，见 §6.1。
> *A tank outage on a four-tank box is 25% of compute (12.5% on an eight-tank box). The unit of redundancy remains the container — see §6.1.*

### 5.4 冷源配置原则 · Heat-rejection configuration rule

每台 I200C20 与其室外冷源**一对一**配置，不跨箱共享冷源。系统级可用性靠增加箱数实现。 ^mdc-79aa905e37
*Each I200C20 is paired **one-to-one** with its outdoor plant; plant is not shared across containers. System-level availability is achieved by adding containers.* ^mdc-5ad1b31747

---

## 6. 配电规格 · Power Distribution ^sec-6-power

I200C20 的电力边界在**箱外**：UPS、电池与配电由场站或客户提供，箱体只接受进线。20 英尺箱内不预留电力舱空间 —— 这正是它能把 200 kW 密度装进 20 英尺的原因之一。 ^mdc-5b7743b09e

*The I200C20 power boundary is **outside the box**: UPS, batteries and distribution are supplied by the site or the customer, and the container only receives an incoming feed. No power-bay volume is reserved inside the 20ft envelope — one of the reasons 200 kW of density fits inside 20 feet at all.* ^mdc-164450e59d

| 项目 · Item | 参数 · Specification |
|-------------|----------------------|
| UPS 边界 · UPS boundary | **箱外**（场站 / 客户提供 UPS、电池、PDC）· **Outside the box** (site / customer supplies UPS, batteries, PDC) |
| UPS 容量 · UPS capacity | **不适用** —— MDCX 不为本产品定义 UPS 容量，由客户按其电力架构选型 · **Not applicable** — MDCX does not define a UPS capacity for this product; it is selected by the customer to suit their electrical architecture |

> **UPS 与 BESS 是两回事：** UPS 是分钟级切换后备，BESS 是小时级储能。二者在 I200C20 上都在箱外，属于不同的设备和不同的采购项。 ^mdc-ca8827d712
> ***UPS and BESS are not the same thing:*** *UPS is minutes-scale ride-through, BESS is hours-scale storage. On I200C20 both sit outside the box, and they are different equipment and different procurement items.* ^mdc-dd771a6d16

### 6.1 冗余模型 · Redundancy model ^sec-6-redundancy

> **集装箱是最小冗余单元。** *The container is the smallest unit of redundancy.*

| 层级 · Layer | 冗余 · Redundancy |
|--------------|-------------------|
| 槽内冷却（每槽双 CDU）· In-tank cooling (dual CDU per tank) | **2N** |
| 单箱 IT · Single-container IT | **不设 IT 冗余** —— 单箱是一个整体 · **No IT redundancy**; a container is one whole |
| 系统级 · System level | **N / N+1 / 2N 靠增加箱数实现** · N / N+1 / 2N achieved by adding containers |
| 设计目标 · Design objective | Tier II 投资，经差异化冗余达到 Tier III 级可用性 · Tier II investment reaching Tier III-class availability through differentiated redundancy |
| 冗余原则 · Redundancy principle | 失效代价高的地方 2N，其余 N+1 —— 不做全局 2N · 2N where failure is expensive, N+1 elsewhere; never global 2N |

> **20 英尺箱型让「增加箱数」这条冗余路径在受限场地上成为现实选项** —— 两台 I200C20 组成 N+1，占地与吊装限界仍小于一台 40 英尺箱。对场地受限但要求可用性的客户，这是 I200C20 的实际价值。 ^mdc-a285881060
> ***The 20ft form factor makes "add another container" a realistic redundancy path on a constrained site*** *— two I200C20 units forming N+1 still sit inside a smaller footprint and lifting envelope than one 40ft box. For a space-constrained customer who nonetheless needs availability, that is the real value of I200C20.* ^mdc-79f785f755

---

## 9. 环境与合规 · Environmental & Compliance ^sec-9-environment

| 项目 · Item | 参数 · Specification |
|-------------|----------------------|
| 散热选型气候判据 · Heat-rejection climate gate | 历史极端干球 **≤ 24 °C** → 干冷器为主；**> 24 °C** → 加装混合冷机 · Historical extreme dry-bulb ≤ 24 °C → dry coolers primarily; > 24 °C → add a hybrid chiller |
| 质保背书 · Warranty backing | 浸没线由 OEM 背书；**Intel DataCenter Certified** · Immersion line backed by the OEM; Intel DataCenter Certified |
| 可用性等级目标 · Availability target | Tier II 投资 → Tier III 级可用性（差异化冗余）· Tier II investment → Tier III-class availability |

---

## 10. 监控与管理 · Monitoring & Management ^sec-10-monitoring

| 项目 · Item | 参数 · Specification |
|-------------|----------------------|
| **CIOS** | 每台 MDCX 均含。路径寻址遥测、告警转工单、运维工作流、用量计量 · Included with every MDCX: path-addressed telemetry, alarm-to-ticket, O&M workflows, usage metering |
| 数字孪生 · Digital twin | **NVIDIA Omniverse** —— 实时状态投射到 3D 模型 · Live state projected onto a 3D model |

---

## 12. 服务与交付 · Service & Delivery ^sec-12-service

### 12.1 价格 · Pricing

> **配置方案由 MDCX 工程团队提供，价格由商务团队核算，请联系客户经理获取正式报价。**
> *The configuration is provided by the MDCX engineering team; pricing is calculated by the commercial team. Please contact your account manager for a formal quotation.*

### 12.2 交期 · Lead time

**只承诺 EXW，其余一律不承诺。** *EXW is the only commitment; nothing else is committed.*

| 项目 · Item | 参数 · Specification |
|-------------|----------------------|
| **首批交期 · First-batch lead time** | **下单后 120 天 EXW** · 120 days EXW from order placement |
| **Scale 扩容批次交期 · Scale (expansion batch) lead time** | **90 天 EXW** · 90 days EXW |
| **假负载运行期 · Dummy-load burn-in period** | **5–30 天**，先以假负载验证供电与冷却链，再上真实算力；**不含在 EXW 承诺内**（来源：Supermicro 建议）· **5–30 days** of dummy-load burn-in to prove the power and cooling chain before real compute goes in; **not covered by the EXW commitment** (source: Supermicro recommendation) |
| 商务周期 · Commercial cycle | 合同、付款与采购周期**不予承诺** · Contract, payment and procurement cycles are **not committed** |
| 运输与清关 · Freight and customs | 买方自理，**不予承诺周期** · Buyer's responsibility; **no duration is committed** |
| 现场安装与调试 · On-site installation and commissioning | **不予承诺** · **Not committed** |

> 商务、运输、安装三段不给天数、不给区间、不做估算。
> *No day count, range or estimate is given for the commercial, freight or installation segments.*

### 12.3 质保与支持 · Warranty and support

| 项目 · Item | 参数 · Specification |
|-------------|----------------------|
| 质保范围与年限 · Warranty scope and term | **核心部件，自 EXW 起一年** · **Core components, one year from EXW** |
| 后续年份 · Subsequent years | **按年收取服务费** · **Annual service fee** |
| 支持响应等级 · Support response level | ONSITE / NBD / 9×5 / 24×7 等条款**以 Invoice 为准**，本文档不定义 · Terms such as ONSITE / NBD / 9×5 / 24×7 are **governed by the Invoice** and are not defined in this document |
| 质保背书 · Warranty backing | 浸没线由 OEM 背书；**Intel DataCenter Certified** · Immersion line backed by the OEM; Intel DataCenter Certified |

### 12.4 交付与服务 · Delivery and service

| 项目 · Item | 参数 · Specification |
|-------------|----------------------|
| 预制率 · Prefabrication rate | **99% 出厂前完成** · 99% completed before leaving the factory |

### 12.5 扩展逻辑 · Expansion logic

| 方向 · Direction | 说明 · Notes |
|------------------|--------------|
| 横向扩展 · Scale-out | 增加 I200C20 台数 —— 20 英尺箱型让多箱扩展在受限场地上成为现实选项；系统级 N / N+1 / 2N 由箱数决定 · Add I200C20 units; the 20ft form factor makes multi-container growth realistic on constrained sites, and system-level redundancy is set by container count ^mdc-50a68ac456 |
| 混合部署 · Mixed deployment | 与 I400C45 / I400C40 混合组集群 —— 同款浸没槽，运维口径与备件通用 · Cluster with I400C45 / I400C40; the same tank means common O&M practice and common spares ^mdc-d8827e4bd0 |

---

## 13. 选址与安装 · Site & Installation ^sec-13-site

I200C20 的选址判据与 400 kW 产品不同：后者的第一约束通常是电力与冷源，I200C20 的第一约束往往是**结构与进场路径** —— 楼板承重、净空高度、吊装半径、坡道或电梯限界。**这些必须在方案阶段完成结构复核**，由双方在技术澄清阶段共同确认，不留到部署期。 ^mdc-32c8d6f313

*I200C20's siting criteria differ from the 400 kW products. For those the first constraint is usually power and heat rejection; for I200C20 it is usually **structure and the access route** — floor loading, clear height, lifting radius, ramp or lift envelope. **A structural review must be completed at proposal stage**, jointly confirmed during technical clarification rather than left to deployment.* ^mdc-8c781bc8bb

| 项目 · Item | 要求 · Requirement |
|-------------|--------------------|
| 室外冷源 · Outdoor plant | 每箱一对一配置：干冷器为主，峰值站点加混合冷机；不跨箱共享 · One-to-one per container; dry coolers primarily, hybrid chiller at peak-climate sites; not shared |
| 气候前置判据 · Climate gate | 历史极端干球 ≤ 24 °C 可按自然冷却路线；> 24 °C 须核算混合冷机 DX 电耗并计入设施负荷 · ≤ 24 °C permits the free-cooling route; above 24 °C the hybrid chiller's DX energy must be calculated into facility load |
| 电力接入 · Power connection | 客户侧提供 UPS、电池与配电；箱体只接受进线 · The customer supplies UPS, batteries and distribution; the container only receives an incoming feed |
| 结构复核 · Structural review | 楼板 / 地面承重、净空、进场路径与吊装方案，双方在技术澄清阶段确认 · Slab or ground loading, clear height, access route and lift plan, jointly confirmed during technical clarification |
| 当地审批 · Local permits | 规划、用电、消防、环保 —— 项目级确认；室内部署另需建筑与消防报建 · Planning, utility, fire, environmental — confirmed per project; indoor deployment additionally requires building and fire approvals |

### 13.1 Zone 边界 · Zone boundaries

| Zone | 与 I200C20 的关系 · Relation to I200C20 ^mdc-dca461b781 |
|------|------------------------------------------|
| IT Zone | **I200C20 本体**（4× 浸没槽）· I200C20 itself (4 tanks) ^mdc-83707af5a3 |
| Power Zone | UPS、电池、配电全部在箱外，属客户 / 场站范围 · UPS, batteries and distribution all outside, on the customer / site side |
| Cooling Zone | 室外冷源一对一，不在箱体内集成 · Outdoor plant one-to-one, not integrated inside the container |

---

## 14. 主要参数汇总 · Key Specifications Summary ^sec-14-summary

| 项目 · Item | 参数 · Specification |
|-------------|----------------------|
| SKU | `I200C20ST50` ^mdc-28e4534e01 |
| 箱型 · Container | 20ft 算力舱 · 20ft compute bay |
| IT Load | **200 kW** |
| 浸没槽 · Immersion tanks | 4 台，每槽 50 kW · 4 tanks at 50 kW each |
| 单槽密度 · Per-tank density | **50 kW —— 与 400 kW 产品相同** · identical to the 400 kW products |
| GPU 平台 · GPU platforms | 4090 · 5090 · RTX PRO 6000 · H100 · H200（PCIe） |
| 冷却方式 · Cooling method | 单相浸没；每槽双 CDU **2N** · Single-phase immersion; dual CDU per tank, 2N |
| 油侧 ΔT · Oil-side ΔT | 8 K |
| 单槽油流量 · Oil flow per tank | ≈11–12 m³/h |
| 整箱二次侧流量 · Container secondary flow | ≈44–48 m³/h（**设计值** · **design value**） |
| PUE | **`1.0x`** —— 逐站点用 <https://mdcx.org>（TCO / Designer）计算，不给固定值与区间 · **`1.0x`** — computed per site with the TCO / Designer at <https://mdcx.org>; no fixed value and no range |
| 室外冷源 · Outdoor heat source | 干冷器为主；峰值站点加混合冷机 · Dry coolers primarily; hybrid chiller at peak-climate sites |
| UPS 边界 · UPS boundary | 箱外（客户 / 场站提供）· Outside the box (customer / site supplied) |
| 冗余模型 · Redundancy model | 槽内 2N；单箱无 IT 冗余；系统级靠增箱 · 2N in-tank; no IT redundancy in a single box; system level by adding boxes |
| 软件 · Software | CIOS（标配）+ NVIDIA Omniverse 数字孪生 · CIOS (standard) + NVIDIA Omniverse digital twin |
| 预制率 · Prefabrication rate | 99% 出厂前完成 · 99% completed before leaving the factory |
| 交期 · Lead time | 首批 120 天 EXW · Scale 90 天 EXW；假负载运行期 5–30 天（不含在 EXW 承诺内）；商务 / 运输 / 安装不予承诺 · 120 days EXW first batch, 90 days EXW for Scale; dummy-load burn-in 5–30 days (not covered by the EXW commitment); commercial, freight and installation are not committed |
| 质保 · Warranty | 核心部件自 EXW 起 1 年；后续年份按年收取服务费；响应级别以 Invoice 为准 · Core components one year from EXW; annual service fee thereafter; response level governed by the Invoice |

> Total Facility Load、设施水温位、外形尺寸与重量按站点条件逐项核算，在技术澄清阶段以书面形式提供。
> *Total Facility Load, facility water temperatures, external dimensions and weights are calculated against site conditions and issued in writing during technical clarification.*

---

## Changelog

| 版本 · Version | 日期 · Date | 变更摘要 · Summary |
|----------------|-------------|--------------------|
| v1.1 | 2026-08-30 | **按 2026-08-30 Yuri 四条裁定更新（[[PRODUCT_SPEC_BASELINE]] v2.0）。** ① 双环路 GPU 侧温位裁定不适用浸没线，本版未作温位改动。 ② **PUE 一律写 `1.0x`** —— 不给固定值、不给区间、不给「典型值」，逐站点用 <https://mdcx.org>（TCO / Designer）计算；原「≈1.05 + 历史极端干球 ≤ 24 °C」表述与 Total Facility Load 的具体区间一并作废，改为「随 PUE 变化，逐站点计算」，但 IT Load vs Total Facility Load 的口径区分保留。 ③ **交期**写入正式承诺：首批 **120 天 EXW**、Scale **90 天 EXW**（自下单起算），假负载运行期 **5–30 天**（Supermicro 建议，**不含在 EXW 承诺内**）；商务 / 运输 / 安装**一律不予承诺**；删除「交期以商务合同为准」的占位写法。 ④ **质保**写入正式承诺：核心部件**自 EXW 起一年**，后续年份**按年收取服务费**；ONSITE / NBD / 9×5 / 24×7 等响应级别条款**以 Invoice 为准**，本版不定义。§12 重排为 12.1 价格 / 12.2 交期 / 12.3 质保与支持 / 12.4 交付与服务 / 12.5 扩展逻辑。 本版仍不含任何价格数字，也不含任何未确认或源冲突标记。 · Updated to Yuri's four rulings of 2026-08-30: PUE stated as `1.0x` and computed per site at <https://mdcx.org> (the former ≈1.05 wording and all facility-load ranges are void); lead time committed as 120 days EXW first batch / 90 days EXW Scale with a 5–30 day dummy-load burn-in outside the EXW commitment and no commitment on the commercial, freight or installation segments; warranty committed as core components for one year from EXW plus an annual service fee, with response levels governed by the Invoice. No pricing and no unconfirmed-or-conflicted markers anywhere. |
| v1.0 | 2026-08-30 | 首版对外输出版。参数取自 [[PRODUCT_SPEC_BASELINE]] v1.1，仅收录 ✅ 已确认与 🔶 推导（标注为「设计值」）字段；§1 布局、§7 结构、§8 网络、§11 消防因全节参数尚未确认而未收录，已在导航表标注；§2 正面写明「为 40/45 英尺进不去的场地而造」的定位，未使用「减半 / 缩小版」表述；§3 保留 IT Load 与 Total Facility Load 的区分但不给设施负荷数字；交期按源冲突处理，只写「以商务合同为准」；全文无价格数字、无竞品对比。本版为单文件，块拆分待需要时再做。 · First external release. Only confirmed and clearly labelled design values are carried; sections 1, 7, 8 and 11 are not included and are flagged in the navigation table; §2 states the positioning positively without "halved" or "shrunken" wording; §3 keeps the IT Load / Total Facility Load distinction without quoting a facility figure; lead time is stated as governed by the commercial contract; no price figures and no competitor comparison appear anywhere. |
