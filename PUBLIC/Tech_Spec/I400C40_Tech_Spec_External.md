---
tags:
  - "#MDC"
  - "#type/design-spec"
  - "#product/i400c40"
doc_version: v1.1
updated: 2026-08-30
audience: 客户（对外输出版 · 可直接发送）/ Customer-facing (releasable)
sku_id: I400C40ST50
---

# I400C40 — Technical Specification（对外输出版 · External Release） ^mdc-e515064dcf
**All-In-One Immersion Container · 40ft 单相浸没式液冷集装箱**
**40ft single-phase immersion container**

> **受众 Audience：** 客户。本版为**唯一允许直接发给客户**的 I400C40 技术规格文件。 ^mdc-d8c71c19bc
> *Customers. This is the only I400C40 specification document approved for direct release.* ^mdc-c987a0d83c
>
> **配套版本 Companion versions：** 中文内部版 [[I400C40_Tech_Spec_CN]] · 英文内部版 [[I400C40_Tech_Spec_EN]]
>
> **数据源 Data source：** 全部参数取自 [[PRODUCT_SPEC_BASELINE]]（六 SKU 规格基准表 v1.0 / 2026-08-30）。**本版仅收录已确认（✅）与我方推导（🔶 设计值）参数**；尚未确认的参数不在本版出现，将在技术澄清阶段以书面形式提供。
> *All parameters are taken from the MDCX six-SKU baseline. This edition carries only confirmed values and clearly labelled design values; parameters still under engineering confirmation do not appear here and will be issued in writing during technical clarification.*
>
> **参数争议以基准表为准 / The baseline table settles parameter disputes.**
>
> ⚠️ **本版与既有内部版 [[I400C40_Tech_Spec_CN]] / [[I400C40_Tech_Spec_EN]]（V1.0 · 2026-07-28）不是同一套数据。** 既有内部版的参数基线为旧产品文档 AC40 / A32 V1.4，其中若干数值尚未进入 [[PRODUCT_SPEC_BASELINE]]，因此**未收录于本对外版**。两者冲突时以基准表为准。 ^mdc-fd473331c2
> *This edition is not built from the same data set as the existing internal editions (V1.0, 2026-07-28), whose parameter baseline is the legacy AC40 / A32 V1.4 product documents. Figures from those documents that have not yet entered the baseline table are not carried here. Where the two disagree, the baseline table governs.* ^mdc-6bc9a23838

---

## 文档导航 · Document Navigation

> **本版为单文件，块拆分待需要时再做。** 章节锚点（`^sec-1-layout` … `^sec-14-summary`）与内部版一致，编号保持对齐，因此本版章节号不连续。
> *This edition is a single file; block splitting will be done if and when it is needed. Section anchors and numbering are kept aligned with the internal editions, so the section numbers in this edition are not consecutive.*

| § | 章节 · Section | 锚点 · Anchor | 状态 · Status |
|---|----------------|---------------|---------------|
| 1 | 布局 · Layout | `^sec-1-layout` | 收录 · Included |
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

## 1. 布局 · Layout ^sec-1-layout

40 英尺箱体为单一算力舱：8 台浸没槽沿两侧箱壁双排布置、每侧 4 台，中间为运维通道；另设 1 台 10 kW 风冷机柜。箱内不设电力舱 —— UPS 与电池在箱外。

*The 40ft container is a single compute bay: eight immersion tanks in two rows against the side walls, four per side, with a central service aisle, plus one 10 kW air-cooled rack. There is no power bay inside the box — the UPS and batteries sit outside.*

![[KB/IMMERSION/I400C40/I400C40 Layout_v1.svg]] ^mdc-2376e532fe
*布局示意 · Layout schematic*

| 项目 · Item | 参数 · Specification |
|-------------|----------------------|
| 舱段划分 · Bay division | 单一算力舱（8× 浸没槽 + 1× 10 kW 风冷柜），电力设备在箱外 · A single compute bay (8 tanks + 1× 10 kW air rack); electrical plant outside the box |
| 浸没槽排布 · Tank arrangement | 双排靠箱壁，中央运维通道 · Two rows against the walls, central service aisle |

---

## 2. 产品定位 · Product Positioning ^sec-2-positioning

**同样的八槽核心，你自己的电力架构。**

I400C40 与 I400C45 共享**完全相同的 400 kW 八槽浸没核心** —— 同样的槽体、同样的油回路、同样的 2N 槽内冷却、同样的冷却规则。差别只有一处：**电力边界在箱外**。UPS、电池与配电由场站提供。 ^mdc-5e185edaa3

对于已经建成配电与后备体系的场站，这不是减配，而是**不重复付费**：场站已经为电付过一次，箱子不再收第二次。既有的 UPS 容量、既有的运维体系、既有的电气标准继续使用；箱体只承担它真正擅长的那部分 —— 把 400 kW 的算力密度和浸没冷却封装好，交到进线端。

***The same eight-tank core, your own electrical architecture.***

*I400C40 shares an **identical 400 kW eight-tank immersion core** with I400C45 — the same tanks, the same oil loop, the same 2N in-tank cooling, the same cooling rules. There is exactly one difference: **the power boundary is outside the box**. UPS, batteries and distribution are provided by the site.* ^mdc-d9d72588aa

*For a site that has already built its distribution and ride-through, this is not a reduced configuration — it is **not paying twice**: the site has already paid for power once, and the container does not charge for it again. Existing UPS capacity, existing operations practice and existing electrical standards stay in use, and the container carries only the part it is genuinely good at — packaging 400 kW of compute density and immersion cooling up to the incoming terminals.*

| 维度 · Dimension | 定位 · Positioning |
|------------------|--------------------|
| 产品线 · Product line | Immersion Cooling（单相浸没）· Single-phase immersion |
| SKU | `I400C40ST50` ^mdc-e2f1711ff9 |
| IT 容量 · IT capacity | 400 kW（推荐 360 kW / 上限 400 kW）· 400 kW (360 kW recommended / 400 kW maximum) |
| 构成单元 · Building blocks | 8× 浸没槽 + 1× 10 kW 风冷机柜 · 8 immersion tanks + 1× 10 kW air-cooled rack |
| 单槽密度 · Per-tank density | 50 kW |
| 电力边界 · Power boundary | **箱外**（客户自备 UPS 与电池）· **Outside the box** (customer-supplied UPS and batteries) |
| 箱型 · Container | 40ft |
| 状态 · Status | 已量产交付 · Shipped |

### 2.1 I400C40 与 I400C45 —— 同一个八槽核心 · The same eight-tank core ^mdc-587bd35a12

差别**只有电力边界，以及那五英尺（即电力舱的体积）**。八槽浸没核心、油回路与冷却规则完全相同。

*The difference is **only the power boundary and those five feet — the volume of the power bay**. The eight-tank immersion core, the oil loop and the cooling rules are identical.*

| 项 · Item | I400C40 | I400C45 ^mdc-e947953355 |
|-----------|---------|---------|
| 八槽浸没核心 · Eight-tank core | 相同 · Identical | 相同 · Identical |
| 油回路与冷却规则 · Oil loop and cooling rules | 相同 · Identical | 相同 · Identical |
| 箱型 · Container | 40ft | 45ft（含电力舱）· with power bay |
| UPS 边界 · UPS boundary | 箱外，客户自备 600 kW，~10 min 后备 · Outside, customer-supplied 600 kW, ~10 min | 箱内 600 kW，~20 min 后备 · Inside, 600 kW, ~20 min |
| 整机 UL · Full-system UL | 非本产品交付项 · Not a deliverable of this product | ✅ UL compliant |

**选型判据 · Selection rule：** 场站已有既成的电力架构、UPS 与电池已在别处付过一次 → I400C40。场站尚未为这 400 kW 建过配电与后备，或市场强制整机 UL → I400C45。 ^mdc-f4fcfe71bb
*If the site already has an established electrical architecture and has paid for UPS and batteries elsewhere, choose I400C40. If the site has not yet built distribution and ride-through for this 400 kW, or the market mandates full-system UL, choose I400C45.* ^mdc-e445c66499

---

## 3. IT 容量与设施总负荷 · IT Capacity and Total Facility Load ^sec-3-it-capacity

400 kW 是**槽内 IT 有功**，不是站端进线容量。两个口径服务于两个不同的决策：IT Load 决定买到多少算力，Total Facility Load 决定变电容量申请与电费测算。

*400 kW is **IT real power inside the tanks**, not the site service capacity. The two measures serve two different decisions: IT Load determines how much compute is purchased; Total Facility Load determines the substation capacity applied for and the electricity cost model.*

| 项目 · Item | 参数 · Specification | 备注 · Notes |
|-------------|----------------------|--------------|
| **IT Load** | **推荐 360 kW / 上限 400 kW** —— 8 个浸没槽内服务器 / GPU 的实际有功 · 360 kW recommended / 400 kW maximum — real power of the servers / GPUs inside the eight tanks | — |
| **Total Facility Load** | **随 PUE 变化，逐站点计算** —— IT + 槽内 CDU 泵功 + 室外排热 + 配电损耗 + 舱内辅机；入口 <https://mdcx.org>（TCO / Designer）· Varies with PUE and is computed per site — IT + in-tank CDU pump power + outdoor rejection + distribution losses + auxiliaries; use the TCO / Designer at <https://mdcx.org> | PUE 一律写 `1.0x`，不给固定值与区间 · PUE is stated as `1.0x`; no fixed value and no range |
| 浸没槽 · Immersion tanks | 8 台，每槽 50 kW · 8 tanks at 50 kW each | — |
| 风冷机柜 · Air-cooled rack | 1× 10 kW | — |
| GPU 数上限 · Maximum GPU count | 512 张 PCIe · 512 PCIe GPUs | — |
| GPU 平台 · GPU platforms | 4090 · 5090 · RTX PRO 6000 Blackwell SE · H100 · H200（PCIe 4U 8-GPU） | — |

> **I400C40 的 UPS 在箱外，因此 UPS 损耗与电池柜散热不在本箱之内，但必须计入站端总容量。** ^mdc-4da6ac30ad
> ***Because the I400C40 UPS sits outside the container, UPS losses and battery-cabinet heat are not inside this box — but they must still be counted in site capacity.*** ^mdc-91dbcc8af0

---

## 4. 浸没槽规格 · Immersion Tank Specification ^sec-4-rack-spec

| 项目 · Item | 参数 · Specification |
|-------------|----------------------|
| 数量（整箱）· Quantity per container | 8 |
| 单槽 IT 容量 · IT capacity per tank | 50 kW |
| 冷却方式 · Cooling method | 单相浸没 · Single-phase immersion |
| 槽内 CDU · In-tank CDU | 双 CDU · **2N 完全冗余** · Dual CDU, fully redundant 2N |
| 油侧 ΔT · Oil-side ΔT | 8 K |
| 单槽油流量 · Oil flow per tank | ≈11–12 m³/h |
| 支持 GPU 平台 · Supported GPU platforms | 4090 · 5090 · RTX PRO 6000 Blackwell SE · H100 · H200（PCIe 4U 8-GPU） |

---

## 5. 冷却系统 · Cooling System ^sec-5-cooling

服务器整机浸入介电液，热量由槽内 CDU 的板式换热器交给设施水，再由室外冷源排入大气。没有服务器风扇，没有冷热通道，箱内不存在需要靠风量维持的热平衡 —— 这是浸没架构能在低干球站点做到极低 PUE 的物理前提（**具体 PUE 逐站点计算，见 §5.2**）。**这套冷却架构与 I400C45 完全相同。** ^mdc-23a08a8a9d

*Whole servers sit in dielectric fluid; the in-tank CDU plate heat exchangers hand that heat to facility water, and the outdoor plant rejects it to atmosphere. There are no server fans, no hot and cold aisles, and no in-container heat balance that depends on airflow — this is the physical premise for the very low PUE the immersion architecture reaches at low dry-bulb sites. **This cooling architecture is identical to I400C45.*** ^mdc-e4f87ee9a9

```
IT Load → 介电液 Dielectric fluid (8×) → 双 CDU 板换 Dual CDU plate HX (2N) → 设施水 Facility water
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
| 整箱二次侧流量 · Container secondary flow | **≈88–96 m³/h** | **设计值**，由单槽流量 × 8 推出，以最终选型为准 · **Design value**, derived from per-tank flow × 8, subject to final selection |
| 风冷支路 · Air branch | 1× 10 kW 风冷机柜，独立配置，不与浸没回路共用换热路径 · 1× 10 kW air-cooled rack, independent; does not share a heat path with the immersion loops | — |
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
| 双 CDU 同时故障 · Both CDUs fail | 该槽停机，其余 7 槽不受影响 · That tank shuts down; the other seven are unaffected |
| 室外冷源失效 · Outdoor plant failure | 设施水温上升，需降载或停机 · Facility water temperature rises; derate or shut down |
| 板换 / 过滤器堵塞 · Fouled plate HX or filter | 换热效率下降，油温抬升 · Reduced heat transfer, rising oil temperature |

### 5.4 冷源配置原则 · Heat-rejection configuration rule

每台 I400C40 与其室外冷源**一对一**配置，不跨箱共享冷源。系统级可用性靠增加箱数实现。 ^mdc-b9cb698c4e
*Each I400C40 is paired **one-to-one** with its outdoor plant; plant is not shared across containers. System-level availability is achieved by adding containers.* ^mdc-6f9e7623d1

---

## 6. 配电规格 · Power Distribution ^sec-6-power

I400C40 的电力边界在**箱外**：UPS、电池与配电由场站或客户提供，箱体只接受进线。40 英尺箱内不设电力舱 —— 全部内部容积用于算力与运维。 ^mdc-804815a24a

*The I400C40 power boundary is **outside the box**: UPS, batteries and distribution are provided by the site or the customer, and the container only receives an incoming feed. There is no power bay inside the 40ft envelope — the whole internal volume serves compute and service access.* ^mdc-85598e33fd

```
Grid / BESS / Generator → 客户侧 UPS 与配电（箱外）· Customer-side UPS and distribution (outside)
                                        ↓
                        I400C40 进线 · incomer → 8× 浸没槽 tanks + 10 kW 风冷柜 air rack ^mdc-5760e5c197
```

| 项目 · Item | 参数 · Specification |
|-------------|----------------------|
| UPS 边界 · UPS boundary | **箱外**（客户自备）· **Outside the box** (customer-supplied) |
| UPS 容量 · UPS capacity | **600 kW**（客户自备）· 600 kW (customer-supplied) |
| 电池后备 · Battery ride-through | **~10 min**（客户自备）· ~10 min (customer-supplied) |

> **UPS 与 BESS 是两回事：** UPS 是分钟级切换后备，BESS 是小时级储能。二者在 I400C40 上都在箱外，属于不同的设备和不同的采购项。客户侧设备的合规责任按合同约定。 ^mdc-2083fc4ffb
> ***UPS and BESS are not the same thing:*** *UPS is minutes-scale ride-through, BESS is hours-scale storage. On I400C40 both sit outside the box, and they are different equipment and different procurement items. Compliance responsibility for customer-side equipment is set by contract.* ^mdc-52f4493970

### 6.1 冗余模型 · Redundancy model ^sec-6-redundancy

> **集装箱是最小冗余单元。** *The container is the smallest unit of redundancy.*

| 层级 · Layer | 冗余 · Redundancy |
|--------------|-------------------|
| 槽内冷却（每槽双 CDU）· In-tank cooling (dual CDU per tank) | **2N** |
| 单箱 IT · Single-container IT | **不设 IT 冗余** —— 单箱是一个整体 · **No IT redundancy**; a container is one whole |
| 系统级 · System level | **N / N+1 / 2N 靠增加箱数实现** · N / N+1 / 2N achieved by adding containers |
| 设计目标 · Design objective | Tier II 投资，经差异化冗余达到 Tier III 级可用性 · Tier II investment reaching Tier III-class availability through differentiated redundancy |
| 冗余原则 · Redundancy principle | 失效代价高的地方 2N，其余 N+1 —— 不做全局 2N · 2N where failure is expensive, N+1 elsewhere; never global 2N |

> 冗余的问题不是「是不是 2N」，而是「哪一层」。槽内冷却是 2N；IT 层面的冗余单位是箱 —— 需要 N+1 就配 N+1 台箱。这样为冗余付出的成本买到的是可用算力，而不是闲置的箱内设备。
> *The question is not "is it 2N" but "at which layer". In-tank cooling is 2N; at the IT layer the unit of redundancy is the container — N+1 means N+1 containers. What redundancy spending buys is then usable compute rather than idle equipment inside a box.*

---

## 9. 环境与合规 · Environmental & Compliance ^sec-9-environment

| 项目 · Item | 参数 · Specification |
|-------------|----------------------|
| 散热选型气候判据 · Heat-rejection climate gate | 历史极端干球 **≤ 24 °C** → 干冷器为主；**> 24 °C** → 加装混合冷机 · Historical extreme dry-bulb ≤ 24 °C → dry coolers primarily; > 24 °C → add a hybrid chiller |
| 整机 UL · Full-system UL | **不作为 I400C40 的交付项** —— 需要整机 UL 认证的市场请选型 [[I400C45_Tech_Spec_External\|I400C45]] · **Not a deliverable of I400C40** — where full-system UL is mandatory, select I400C45 ^mdc-a104fdf033 |
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
| 横向扩展 · Scale-out | 增加 I400C40 台数；系统级 N / N+1 / 2N 由箱数决定 · Add I400C40 units; system-level redundancy is set by container count ^mdc-ec0f3636a1 |
| 混合部署 · Mixed deployment | 与 I400C45 / I200C20 混合组集群 —— 同款浸没槽，运维口径与备件通用 · Cluster with I400C45 / I200C20; the same tank means common O&M practice and common spares ^mdc-7fd1a947e1 |

---

## 13. 选址与安装 · Site & Installation ^sec-13-site

| 项目 · Item | 要求 · Requirement |
|-------------|--------------------|
| 室外冷源 · Outdoor plant | 每箱一对一配置：干冷器为主，峰值站点加混合冷机；不跨箱共享 · One-to-one per container; dry coolers primarily, hybrid chiller at peak-climate sites; not shared |
| 气候前置判据 · Climate gate | 历史极端干球 ≤ 24 °C 可按自然冷却路线；> 24 °C 须核算混合冷机 DX 电耗并计入设施负荷 · ≤ 24 °C permits the free-cooling route; above 24 °C the hybrid chiller's DX energy must be calculated into facility load |
| 电力接入 · Power connection | 客户侧提供 UPS、电池与配电，并预留其占地、散热与维护通道；箱体只接受进线 · The customer supplies UPS, batteries and distribution and reserves their footprint, cooling and access; the container only receives an incoming feed |
| 当地审批 · Local permits | 规划、用电、消防、环保 —— 项目级确认 · Planning, utility, fire, environmental — confirmed per project |

### 13.1 Zone 边界 · Zone boundaries

| Zone | 与 I400C40 的关系 · Relation to I400C40 ^mdc-62b5aee9dd |
|------|------------------------------------------|
| IT Zone | **I400C40 本体**（8× 浸没槽 + 10 kW 风冷柜）· I400C40 itself (8 tanks + 10 kW air rack) ^mdc-ad403812aa |
| Power Zone | UPS、电池、配电全部在箱外，属客户 / 场站范围 · UPS, batteries and distribution all outside, on the customer / site side |
| Cooling Zone | 室外冷源一对一，不在箱体内完整集成 · Outdoor plant one-to-one, not fully integrated inside the container |

---

## 14. 主要参数汇总 · Key Specifications Summary ^sec-14-summary

| 项目 · Item | 参数 · Specification |
|-------------|----------------------|
| SKU | `I400C40ST50` ^mdc-eef71ac363 |
| 箱型 · Container | 40ft |
| IT Load | **推荐 360 kW / 上限 400 kW** · 360 kW recommended / 400 kW maximum |
| Total Facility Load | **随 PUE 变化，逐站点用 <https://mdcx.org> 计算** · varies with PUE, computed per site at <https://mdcx.org> |
| 浸没槽 · Immersion tanks | 8 台，每槽 50 kW · 8 tanks at 50 kW each |
| 风冷机柜 · Air-cooled rack | 1× 10 kW |
| GPU 数上限 · Maximum GPU count | 512 张 PCIe · 512 PCIe GPUs |
| GPU 平台 · GPU platforms | 4090 · 5090 · RTX PRO 6000 Blackwell SE · H100 · H200 |
| 冷却方式 · Cooling method | 单相浸没；每槽双 CDU **2N** · Single-phase immersion; dual CDU per tank, 2N |
| 油侧 ΔT · Oil-side ΔT | 8 K |
| 单槽油流量 · Oil flow per tank | ≈11–12 m³/h |
| 整箱二次侧流量 · Container secondary flow | ≈88–96 m³/h（**设计值** · **design value**） |
| PUE | **`1.0x`** —— 逐站点用 <https://mdcx.org>（TCO / Designer）计算，不给固定值与区间 · **`1.0x`** — computed per site with the TCO / Designer at <https://mdcx.org>; no fixed value and no range |
| 室外冷源 · Outdoor heat source | 干冷器为主；峰值站点加混合冷机 · Dry coolers primarily; hybrid chiller at peak-climate sites |
| UPS 边界 · UPS boundary | 箱外，客户自备 · Outside the box, customer-supplied |
| UPS 容量 · UPS capacity | 600 kW（客户自备）· 600 kW (customer-supplied) |
| 电池后备 · Battery ride-through | ~10 min（客户自备）· ~10 min (customer-supplied) |
| 整机 UL · Full-system UL | 非本产品交付项；需要时选型 I400C45 · Not a deliverable of this product; select I400C45 where required ^mdc-f52475c090 |
| 冗余模型 · Redundancy model | 槽内 2N；单箱无 IT 冗余；系统级靠增箱 · 2N in-tank; no IT redundancy in a single box; system level by adding boxes |
| 软件 · Software | CIOS（标配）+ NVIDIA Omniverse 数字孪生 · CIOS (standard) + NVIDIA Omniverse digital twin |
| 预制率 · Prefabrication rate | 99% 出厂前完成 · 99% completed before leaving the factory |
| 交期 · Lead time | 首批 120 天 EXW · Scale 90 天 EXW；假负载运行期 5–30 天（不含在 EXW 承诺内）；商务 / 运输 / 安装不予承诺 · 120 days EXW first batch, 90 days EXW for Scale; dummy-load burn-in 5–30 days (not covered by the EXW commitment); commercial, freight and installation are not committed |
| 质保 · Warranty | 核心部件自 EXW 起 1 年；后续年份按年收取服务费；响应级别以 Invoice 为准 · Core components one year from EXW; annual service fee thereafter; response level governed by the Invoice |

> 设施水温位、外形尺寸与重量按站点条件逐项核算，在技术澄清阶段以书面形式提供。
> *Facility water temperatures, external dimensions and weights are calculated against site conditions and issued in writing during technical clarification.*

---

## Changelog

| 版本 · Version | 日期 · Date | 变更摘要 · Summary |
|----------------|-------------|--------------------|
| v1.1 | 2026-08-30 | **按 2026-08-30 Yuri 四条裁定更新（[[PRODUCT_SPEC_BASELINE]] v2.0）。** ① 双环路 GPU 侧温位裁定不适用浸没线，本版未作温位改动。 ② **PUE 一律写 `1.0x`** —— 不给固定值、不给区间、不给「典型值」，逐站点用 <https://mdcx.org>（TCO / Designer）计算；原「≈1.05 + 历史极端干球 ≤ 24 °C」表述与 Total Facility Load 的具体区间一并作废，改为「随 PUE 变化，逐站点计算」，但 IT Load vs Total Facility Load 的口径区分保留。 ③ **交期**写入正式承诺：首批 **120 天 EXW**、Scale **90 天 EXW**（自下单起算），假负载运行期 **5–30 天**（Supermicro 建议，**不含在 EXW 承诺内**）；商务 / 运输 / 安装**一律不予承诺**；删除「交期以商务合同为准」的占位写法。 ④ **质保**写入正式承诺：核心部件**自 EXW 起一年**，后续年份**按年收取服务费**；ONSITE / NBD / 9×5 / 24×7 等响应级别条款**以 Invoice 为准**，本版不定义。§12 重排为 12.1 价格 / 12.2 交期 / 12.3 质保与支持 / 12.4 交付与服务 / 12.5 扩展逻辑。 本版仍不含任何价格数字，也不含任何未确认或源冲突标记。 · Updated to Yuri's four rulings of 2026-08-30: PUE stated as `1.0x` and computed per site at <https://mdcx.org> (the former ≈1.05 wording and all facility-load ranges are void); lead time committed as 120 days EXW first batch / 90 days EXW Scale with a 5–30 day dummy-load burn-in outside the EXW commitment and no commitment on the commercial, freight or installation segments; warranty committed as core components for one year from EXW plus an annual service fee, with response levels governed by the Invoice. No pricing and no unconfirmed-or-conflicted markers anywhere. |
| v1.0 | 2026-08-30 | 首版对外输出版。参数取自 [[PRODUCT_SPEC_BASELINE]] v1.1，仅收录 ✅ 已确认与 🔶 推导（标注为「设计值」）字段；§7 结构、§8 网络、§11 消防因全节参数尚未确认而未收录，已在导航表标注；设施水温位一行因基准表对 I400C40 尚无确认来源而整行删除；§2 定位写明「同样八槽核心、你自己的电力架构」；交期按源冲突处理，只写「以商务合同为准」，不给天数；全文无价格数字、无竞品对比。**注意本版与既有内部版（基线为 AC40/A32 V1.4）不是同一套数据，冲突时以基准表为准。** 本版为单文件，块拆分待需要时再做。 · First external release. Only confirmed and clearly labelled design values are carried; sections 7, 8 and 11 are not included and are flagged in the navigation table; the facility water temperature row is removed because the baseline carries no confirmed source for it on I400C40; lead time is stated as governed by the commercial contract, with no day count; no price figures and no competitor comparison appear anywhere. Note that this edition is not built from the same data set as the existing internal editions. |
