---
tags:
  - "#MDC"
  - "#type/design-spec"
  - "#product/l1240c45"
doc_version: v1.1
updated: 2026-08-30
audience: 客户 / Customer（对外输出版）
sku_id: L1240C45SUR150
---

# L1240C45 — Technical Specification（对外输出版 / External Edition）
**单环路直接液冷集装箱数据中心 · Single-Loop Direct Liquid Cooled Container Data Center**
**45ft High Cube · 1240 kW IT · 单柜 150 kW / 150 kW per rack · UPS 箱内 / UPS inside**

> **受众 / Audience：** 客户。**本版是本 SKU 唯一允许直接发给客户的版本。**
> This edition is written for customers and is the only edition of this SKU cleared for direct release.
>
> **配套版本 / Companion editions：** [[L1240C45_Tech_Spec_CN|中文内部版 / CN internal]] · [[L1240C45_Tech_Spec_EN|English internal]]
>
> **数据源 / Source of truth：** 全部产品参数取自 [[PRODUCT_SPEC_BASELINE]]（六 SKU 规格基准表）；工程参数取自 [[L1240C45_Tech_Spec_EN]] V1.4（三支路冷却重评估 V4）。**参数争议以基准表为准。**
> Product parameters are taken from [[PRODUCT_SPEC_BASELINE]]; engineering parameters from [[L1240C45_Tech_Spec_EN]] V1.4. **Where parameters disagree, the baseline table governs.**
>
> **本版收录范围 / Scope of this edition：** 仅收录已确认参数与标注为「设计值」的推导参数。尚在选型评审中的第三方设备型号不在本版收录范围，将在技术澄清阶段随选型书提供。
> This edition carries confirmed parameters plus derived parameters explicitly labelled as design values. Third-party equipment models still under selection review are not included here and will be provided with the selection sheets during technical clarification.
>
> **本版为单文件，块拆分待需要时再做 / This edition is a single file; block splitting is deferred until needed.** 锚点 `^sec-1-layout` … `^sec-14-summary` 已保留 / anchors are preserved.

版本 / Version: v1.1 | 日期 / Date: 2026-08-30 | SKU: `L1240C45SUR150`

---

## 文档导航 / Document Navigation

| § | 章节 / Section | 本版 / This edition |
|---|---|---|
| 1 | 布局图 / Layout | ✅ |
| 2 | 产品定位 / Product Positioning | ✅ |
| 3 | IT 容量 / IT Capacity | ✅ |
| 4 | 机架规格 / Rack Specifications | ✅ |
| 5 | 冷却系统 / Cooling System | ✅ |
| 6 | 配电规格 / Power Distribution | ✅ |
| 7 | 结构规格 / Structural Specifications | ✅ |
| 8 | 网络与线缆管理 / Network & Cable Management | ✅ |
| 9 | 环境与合规 / Environmental & Compliance | ✅ |
| 10 | 监控与管理 / Monitoring & Management | ✅ |
| 11 | 消防与安全 / Fire Protection & Safety | ✅ |
| 12 | 服务与支持 / Service & Support | ✅ |
| 13 | 选址与安装 / Site & Installation | ✅ |
| 14 | 参数汇总 / Key Specifications Summary | ✅ |

> 本版 14 节齐全；节内个别尚未定型的行已按 [[UNCONFIRMED_Convention]] §5 移除。
> All fourteen sections are present; individual rows not yet fixed have been removed per [[UNCONFIRMED_Convention]] §5.

---

## 1. 布局图 / Layout ^sec-1-layout

![[TOP.svg|TOP.svg]]
*俯视图 / TOP view*

![[FRONT.jpg]]
*正视图 / FRONT view*

![[SIDE.jpg]]
*侧视图 / SIDE view*

---

## 2. 产品定位 / Product Positioning ^sec-2-positioning

**中文：** L1240C45 是 45ft High Cube 单环路直接液冷集装箱数据中心，采用冷板液冷，单柜 150 kW，整箱 IT 容量 1240 kW，面向高密度 AI / HPC 集群部署。

这个产品的分界线在**电力边界**：**UPS、电池与母线全部在箱内。** 场站只需要把市电送到箱边，箱内的不间断电源、电池后备、母线与配电一次交付到位。它面向的是没有独立电力室、也不打算为一次部署新建电力设施的场站 —— 一个集装箱到场，算力与电力同时闭环。

同产品线内的分工：场站已有电力室、缺的是机房面积时，选 [[L1800C45_Tech_Spec_External|L1800C45]]（单柜 220 kW，1800 kW，UPS 箱外）；45ft 箱体进不去的受限场地，选 [[L450C20_Tech_Spec_External|L450C20]]（20ft，450 kW）。

**冷却架构：** L1240C45 采用**三支路并联 TCS 回路（PG25）**，全部热量经 TCS 二次侧送至室外侧（混合干冷器 + DX）：

- **支路 1 —— 主 CDU 冷板回路：** 承担 8 台液冷机柜 73% 的液冷热量
- **支路 2 —— 9 台被动式后门换热器（RDHX）：** 吸收 47–55% 的后门排风热量
- **支路 3 —— 9 台顶置空调：** 处理机房残余风冷热量与 UPS / 辅助热量

**English:** L1240C45 is a 45ft High Cube single-loop direct-liquid-cooled containerized data center using cold-plate liquid cooling — 150 kW per rack, 1240 kW IT per container — for high-density AI / HPC cluster deployment.

Its dividing line is the **power boundary**: **UPS, batteries and busbar are all inside the container.** The site only has to bring utility power to the container edge; uninterruptible power, battery autonomy, busbar and distribution are delivered inside it in one pass. It targets sites with no separate electrical room that do not intend to build electrical infrastructure for a first deployment — one container arrives and both compute and power are closed out.

Within the product line: choose [[L1800C45_Tech_Spec_External|L1800C45]] (220 kW per rack, 1800 kW, UPS outside) where the site already has an electrical room and is short of floor area; choose [[L450C20_Tech_Spec_External|L450C20]] (20ft, 450 kW) for restricted sites a 45ft container cannot enter.

**Cooling architecture:** L1240C45 runs a **three-branch parallel TCS loop on PG25**, with all heat carried to the outdoor side (hybrid dry cooler + DX) via the TCS secondary loop:

- **Branch 1 — primary CDU cold-plate loop:** 73% of the liquid-cooled heat from the eight DLC racks
- **Branch 2 — 9 × passive rear-door heat exchangers (RDHX):** absorbs 47–55% of rear-door exhaust air heat
- **Branch 3 — 9 × ceiling-mounted units:** handles residual room air heat plus UPS and auxiliary heat

---

## 3. IT 容量 / IT Capacity ^sec-3-it-capacity

| 项目 / Item | 参数 / Parameter |
|---|---|
| 整箱 IT 容量 / Total IT capacity | **1240 kW** |
| 液冷机柜 / DLC racks | 8 × 150 kW（73% 液冷 / 27% 风冷 · 73% liquid / 27% air） |
| 风冷机柜 / Air-cooled rack | 1 × 40 kW |
| 单柜密度 / Rack density | **150 kW**（密度码 / density code `R150`） |
| GPU 平台 / GPU platforms | GB300 NVL72 · B300 HGX（SXM / NVLink） |
| TCS 进水温度 / TCS inlet temperature | **26–28 °C**（CDU 二次侧供至冷板 / RDHX / 顶置机组冷凝侧 · CDU secondary supply to cold plates / RDHX / ceiling-unit condensers） |
| 机柜前进风温度 / Rack front intake temperature | **25–27 °C**（顶置 DX 蒸发器出风 12–18 °C，与 TCS 水温解耦 · ceiling DX evaporator output 12–18 °C, decoupled from TCS water temperature） |
| 液冷风冷比上限 / DLC air-cool ratio (φ_air) | 设计上限 / design ceiling **27%**，CDU 下限护栏 / CDU guardrail ≥ **8%** |
| 功率因数（UPS 输出侧）/ Power factor (UPS output side) | 0.9 |

### 3.1 IT Load 与 Total Facility Load 的区别 / IT Load vs Total Facility Load ^sec-3-it-vs-facility

**中文：** 这两个数不是一回事，谈容量前必须先对齐口径。

| 口径 / Metric | 定义 / Definition | 取值 / Value |
|---|---|---|
| **IT Load（IT 负荷）** | 服务器与 GPU 实际消耗的电功率，不含冷却与配电损耗 · Power actually consumed by servers and GPUs, excluding cooling and distribution losses | **1240 kW** |
| **Total Facility Load（设施总负荷）** | IT Load ＋ 冷却 ＋ 配电损耗 ＋ 辅助负荷 · IT Load + cooling + distribution losses + auxiliaries | **随 PUE 变化，逐站点计算** · varies with PUE, calculated per site |
| **PUE** | 由站点气候与冷源方案决定 · set by site climate and the heat-rejection scheme | **`1.0x`** —— 逐站点计算，入口 <https://mdcx.org>（TCO / Designer）· computed per site with the TCO / Designer at <https://mdcx.org> |

站点侧的变电申请、进线容量与开关柜选型必须按 Total Facility Load 计算，不能按 IT Load 计算。若贵方的「X MW」指的是电网侧可用容量，请在方案对齐会上明确说明。
Utility applications, incoming feeder capacity and switchgear selection must be sized on Total Facility Load, not IT Load. If your "X MW" refers to available grid capacity, please say so at the solution alignment meeting.

> **PUE 不给固定值、不给区间。** 干冷器可全年排热的气候落在低端，更热的站点需加混合冷机、PUE 相应上移 —— 具体数值请用 <https://mdcx.org> 的 TCO / Designer 按贵站点气候条件计算。
> **No fixed PUE value and no range are given.** Climates where dry coolers reject heat year-round sit at the low end; hotter sites need a hybrid chiller and PUE moves up accordingly. For a figure, run your site's climate through the TCO / Designer at <https://mdcx.org>.

---

## 4. 机架规格 / Rack Specifications ^sec-4-rack-spec

| 项目 / Item | 参数 / Parameter |
|---|---|
| 机柜类型 / Rack type | 48U 标准机柜 / 48U standard rack |
| 机柜深度 / Rack depth | 1200 mm |
| 机柜宽度 / Rack width | 800 mm |
| 机柜数量 / Rack quantity | 9（8 液冷 + 1 风冷 · 8 DLC + 1 air-cooled） |
| 液冷接入 / Liquid cooling | 侧置 Manifold / Side-mounted manifold |
| PDU 位置 / PDU position | 后置 / Rear-mounted |
| 机柜后门至箱壁间距 / Rack rear door to container wall gap | 350 mm |
| 底部线缆 / 管路空间 / Bottom cable & pipe space | 350–400 mm（配电区不设架空地板 · no raised floor in the distribution zone） |

### 4.1 冷板 Manifold 配置 / Cold-Plate Manifold Configuration

| 项目 / Item | 参数 / Parameter |
|---|---|
| 每柜 Manifold 数 / Manifolds per rack | **2**（冷板 ≤ 100 · cold plates ≤ 100）/ **3**（冷板 > 100，NVL72 级 · cold plates > 100, NVL72 class） |
| 每 Manifold 分支数 / Branches per manifold | 20–50 |
| 每分支设计流量 / Design flow per branch | **1.6–2.1 L/min**（在 1–3 L/min 规格内留 30%+ 余量 · 30%+ margin inside the 1–3 L/min spec） |
| Manifold 进口配件 / Manifold inlet fitting | **PICV 压力无关型控制阀 + 流量计 · PICV + flow meter**（防止 Manifold 间失衡 · prevents inter-manifold imbalance） |
| 整箱 Manifold 总数 / Total manifolds | **16–24**（8 柜 × 2–3 · 8 racks × 2–3） |
| 失衡容差 / Imbalance tolerance | ≤ 10%（Manifold 内 · within a manifold）/ ≤ 15%（含 Manifold 间 · including inter-manifold） |

---

## 5. 冷却系统（三支路 TCS PG25） / Cooling System (Three-Branch TCS PG25) ^sec-5-cooling

### 5.1 TCS 总述 / TCS Overview

| 项目 / Item | 参数 / Parameter |
|---|---|
| 循环介质 / Circulating fluid | **PG25**（25% 丙二醇水溶液；所有湿部件须 PG 兼容 · 25% propylene-glycol/water; all wetted equipment must be PG-compatible） |
| TCS 进水温度 / TCS inlet temperature | **26–28 °C** |
| TCS 设计温差 / TCS design ΔT | 10 °C（CDU 二次侧 · CDU secondary）/ 8 °C（RDHX 支路 · RDHX branch） |
| 总循环流量（S-Max）/ Total circulating flow (S-Max) | ≈ **148 m³/h** |
| 总循环流量（φ_air = 8%）/ Total circulating flow (φ_air = 8%) | ≈ **154 m³/h** —— 设计上限 / design ceiling |
| 总排热量（S-Max）/ Total heat rejected (S-Max) | ≈ **1352 kW** |
| 总扬程 / Total TDH | 19–25 m H₂O |
| TCS 主泵 / TCS main pump | 铭牌 200 m³/h @ 25 m H₂O，PG 兼容叶轮与密封，变频，2N 或 N+1 · Nameplate 200 m³/h @ 25 m H₂O, PG-compatible impeller and seals, VFD, 2N or N+1 |
| 室外侧排热基线 / Outdoor heat-rejection baseline | **≥ 1700 kW**（混合干冷器 + DX 板换组合 · hybrid dry cooler + DX plate-HX combination） |

### 5.2 支路 1 —— 主 CDU / Branch 1 — Primary CDU

| 项目 / Item | 参数 / Parameter |
|---|---|
| 换热容量 / Heat-rejection capacity | **≥ 1500 kW** |
| 二次侧流量 / Secondary-side flow | **≥ 175 m³/h** |
| 二次侧扬程 / Secondary-side head | **≥ 220 kPa（≈ 22 m H₂O）** |
| 二次泵 / Secondary pump | 变频驱动 / VFD-driven |
| 冗余 / Redundancy | **2N 或 N+1** 二次泵 · 2N or N+1 secondary pumps |
| 支路 1 设计流量（S-Max）/ Branch 1 design flow (S-Max) | 78 m³/h |
| 支路 1 设计流量（φ_air = 8% 上限）/ Branch 1 design flow (φ_air = 8% ceiling) | 98.6 m³/h |
| 支路 1 压降 / Branch 1 ΔP | 47–128 kPa（随 φ_air 变化 · varies with φ_air） |
| 承担负荷 / Served load | 8 台液冷机柜冷板（每柜液冷负荷 109.5 kW）· cold plates of 8 DLC racks (109.5 kW liquid load per rack) |

### 5.3 支路 2 —— 后门换热器（RDHX） / Branch 2 — Rear-Door Heat Exchangers

| 项目 / Item | 参数 / Parameter |
|---|---|
| 数量与形式 / Quantity & type | **9 × 被动式后门换热器 · 9 × passive RDHX**（8 台装于液冷柜后门 + 1 台装于风冷柜后门 · 8 on DLC rack rear doors + 1 on the air-cooled rack rear door） |
| 实际风侧吸热率（TCS 26–28 °C）/ Actual air-heat absorption (TCS 26–28 °C) | 47–55%（ε ≈ 0.55 为被动式 RDHX 物理上限 · ε ≈ 0.55 is the passive-RDHX physical ceiling） |
| 支路 2 设计流量（PG25）/ Branch 2 design flow (PG25) | ≈ 21 m³/h |
| 支路 2 压降 / Branch 2 ΔP | 36–62 kPa |
| 支路 2 回收热量 / Branch 2 heat recovered | ≈ 189 kW |

> 设备型号与铭牌参数以最终选型为准，将在技术澄清阶段随选型书提供。
> Equipment models and nameplate data follow the final selection and will be provided with the selection sheets during technical clarification.

### 5.4 支路 3 —— 顶置机组 / Branch 3 — Ceiling-Mounted Units

| 项目 / Item | 参数 / Parameter |
|---|---|
| 数量与形式 / Quantity & type | **9 × 顶置自含式 DX 机组（带自然冷却回路，EG / PG 兼容）· 9 × self-contained ceiling DX units with a free-cooling loop, EG/PG compatible** |
| 9 台合计显冷量 / Nine-unit total sensible capacity | ≈ **234 kW** —— **设计值 / design value** |
| 支路 3 设计流量 / Branch 3 design flow | **48.7 m³/h** |
| 支路 3 压降 / Branch 3 ΔP | 63–73 kPa |
| 支路 3 回收热量 / Branch 3 heat recovered | ≈ 287 kW（含压缩机输入约 58 kW · including ~58 kW compressor input） |
| 安装 / Installation | 沿箱顶 13.7 m 长度均布 · evenly distributed along the 13.7 m container roof |

> 设备型号与铭牌参数以最终选型为准，将在技术澄清阶段随选型书提供。
> Equipment models and nameplate data follow the final selection and will be provided with the selection sheets during technical clarification.

### 5.5 三支路水力汇总（PG25 · S-Max） / Three-Branch Hydraulic Summary (PG25 · S-Max)

| 支路 / Branch | 设计流量 / Design flow | 峰值流量 / Peak-case flow | 压降 / ΔP | TCS 回收热量 / TCS heat recovered |
|---|---|---|---|---|
| 支路 1 —— 主 CDU 冷板 / Branch 1 — primary CDU cold plates | 78 m³/h | 98.6 m³/h @ φ_air = 8% | 47–128 kPa | 876 kW |
| 支路 2 —— 9× RDHX / Branch 2 — 9 × RDHX | 21 m³/h | 21 m³/h | 36–62 kPa | ≈ 189 kW |
| 支路 3 —— 9× 顶置机组 / Branch 3 — 9 × ceiling units | 48.7 m³/h | 48.7 m³/h | 63–73 kPa | ≈ 287 kW |
| **TCS 合计 / TCS total** | **≈ 148 m³/h** | **≈ 154 m³/h** | TDH 19–25 m H₂O | **≈ 1352 kW** |

### 5.6 控制策略 / Control Strategy

| 控制层 / Control layer | 逻辑 / Logic |
|---|---|
| 流量分配 / Flow distribution | 每条支路配 **PICV 压力无关型控制阀**，上游压差波动时仍保持设定流量 · every branch has a **PICV** holding setpoint flow regardless of upstream ΔP swings |
| 冷板支路 → GPU 联锁 / Cold-plate branch → GPU interlock | 支路 1 流量 < 70 m³/h → GPU 降至 80%；< 60 m³/h → GPU 降至 60% · Branch 1 flow < 70 m³/h → GPU throttle to 80%; < 60 m³/h → throttle to 60% |
| RDHX 支路 / RDHX branch | 单台 RDHX < 1.5 m³/h → 该柜 GPU 降频并告警 · any single RDHX < 1.5 m³/h → that rack's GPUs throttle plus alarm |
| 顶置支路 / Ceiling branch | 支路 3 < 40 m³/h → 告警并跟踪顶送风温度 · Branch 3 < 40 m³/h → alarm plus roof-supply temperature trending |

### 5.7 室外侧冷源 / Outdoor Heat Rejection

| 项目 / Item | 参数 / Parameter |
|---|---|
| 室外侧排热基线 / Outdoor heat-rejection baseline | **≥ 1700 kW**（混合干冷器 + DX 板换组合 · hybrid dry cooler + DX plate-HX combination） |
| 混合冷机 / Hybrid chiller | **TICA TAMFV430.3ALF5** |

---

## 6. 配电规格 / Power Distribution ^sec-6-power

### 6.1 主配电 / Main Distribution

**电力边界：UPS、电池与母线全部在箱内。** 场站只需将市电送至箱边。
**Power boundary: UPS, batteries and busbar are all inside the container.** The site only brings utility power to the container edge.

| 设备 / Device | 数量 / Qty | 说明 / Notes |
|---|---|---|
| 进线柜 / Incoming switchgear | 1 面 / panel | 主断路器 / CT / 计量 · main breaker / CT / metering |
| UPS 主柜 / UPS main cabinet | 1 面 / panel | **EATON 9395XR-1500（1500 kW）**，在线双变换，含静态旁路切换逻辑 · online double conversion, includes static bypass transfer logic |
| 电池组 / Battery bank | 独立配置 / standalone | **3 × 93LiG2 · 后备约 8 分钟 / ~8 min autonomy** |
| 旁路柜 / Bypass panel | 1 面 / panel | 含 MCCB + 机械联锁（防止两路同时闭合）· MCCB + mechanical interlock preventing both paths closing simultaneously |
| 母线系统 / Busbar system | 1 套 / set | **SIEMENS 2500A** 封闭插接式母线，含始端箱 · enclosed plug-in busbar, includes end feed box |

**插接箱（TOU）配置 / Tap-off Unit (TOU) configuration** —— 电流与断路器整定为**设计值，以最终 BOM 为准** / currents and breaker ratings are **design values, subject to the final BOM**:

| 负荷类型 / Load type | 数量 / Qty | 单台电流 / Current per unit | 断路器 / MCB |
|---|---|---|---|
| 液冷机柜 / DLC racks | 8 | ~200 A | 250 A |
| 风冷机柜 / Air-cooled rack | 1 | ~80 A | 100 A |
| 主 CDU（≥1500 kW，变频二次泵）/ Primary CDU (≥1500 kW, VFD secondary pump) | 1 | ~35 A | 50 A |
| 顶置机组 / Ceiling units | 9 | ~15 A | 20 A |
| TCS 主循环泵 + RDHX 控制器 / TCS main pump + RDHX controllers | 1 组 / group | ~20 A | 32 A |

> 9 台顶置机组压缩机输入合计约 58 kW，含风机与控制约 70 kW。
> Nine ceiling units draw roughly 58 kW of compressor input in total, or about 70 kW including fans and controls.

### 6.2 机柜 PDU / Rack PDU

| 项目 / Item | 参数 / Parameter |
|---|---|
| 输入规格 / Input rating | **60 A 415 V** |
| 输出接口 / Output interface | **24 位 C19 · 24-position C19** |
| 保护 / Protection | **磁液压断路器 · magnetic hydraulic circuit breaker** |
| 电源线 / Power cable | 1.5 m AWG 线缆（出厂预装 · factory pre-installed） |
| 安装位置 / Installation position | 后置 / rear-mounted |
| 监测 / Monitoring | 电流监测（PDU 面板显示）· current monitoring, PDU panel display |

---

## 7. 结构规格 / Structural Specifications ^sec-7-structural

| 项目 / Item | 参数 / Parameter |
|---|---|
| 箱型 / Container type | **45ft High Cube** |
| 外形尺寸（L × W × H）/ Exterior dimensions | **13,716 × 2,438 × 2,992 mm** |
| 内部净高 / Interior clear height | 随安装与冷却配置变化，以实际图纸为准 · varies by installation and cooling configuration; refer to the actual drawings |
| 内部可用净宽 / Interior usable width | 随安装与冷却配置变化，以实际图纸为准 · varies by installation and cooling configuration; refer to the actual drawings |
| 防护等级 / Enclosure rating | 按需定制 / custom per requirement |
| 空箱重 / Empty weight | **~16 T**（不含 IT 负载 · without IT load） |
| 满载重（含 IT）/ Loaded weight (with IT) | **~20–25 T**（随配置变化 · depends on configuration） |
| 地基要求 / Foundation requirement | 承载 ~20–25 T，地面平整度 ±0.5° · ~20–25 T load capacity, ground levelness ±0.5° |

---

## 8. 网络与线缆管理 / Network & Cable Management ^sec-8-network

| 项目 / Item | 参数 / Parameter |
|---|---|
| 线缆穿舱 / Cable penetration | **支持顶进与底进**（线缆或母线）· supports top and bottom entry (cable or busbar) |
| 桥架 / Cable tray | **位于机柜上方（顶置）** · located above the racks (top-mounted) |
| 光纤 / 网络进线 / Fibre & network entry | **箱体侧面进线** · container side entry |

---

## 9. 环境与合规 / Environmental & Compliance ^sec-9-environment

### 9.1 运行环境 / Operating Environment

| 项目 / Item | 参数 / Parameter |
|---|---|
| 工作温度 / Operating temperature | **-45 °C ~ +45 °C** |
| 工作湿度 / Operating humidity | 按标准数据中心（典型 40%–60% RH，无冷凝）· per standard data center practice (typically 40%–60% RH, non-condensing) |

### 9.2 认证 / Certifications

| 认证 / Certification | 状态 / Status |
|---|---|
| UL | **组件已取得 UL 认证；整机需现场 TUV 认证** · components UL certified; the complete unit requires on-site TUV field certification |
| TUV 现场认证 / TUV field certification | **必需 —— 在部署阶段安排** · required, arranged during deployment |

> 运行海拔与整机认证的站点适配项在技术澄清阶段确认。
> Operating altitude and site-specific certification items are confirmed during technical clarification.

---

## 10. 监控与管理 / Monitoring & Management ^sec-10-monitoring

| 项目 / Item | 参数 / Parameter |
|---|---|
| 监控系统 / Monitoring system | **PLC + MODBUS** |
| 通信协议 / Communication protocols | MODBUS / TCP/IP |
| 监测参数 / Monitored parameters | 电压、电流、功率、温度、湿度、UPS 状态、EPO 回路 · voltage, current, power, temperature, humidity, UPS status, EPO circuits |
| 远程访问 / Remote access | **SNMP / Web** |
| BMS 集成 / BMS integration | 支持（MODBUS）· supported (MODBUS) |
| **CIOS** | 每台 MDCX 均含：路径寻址遥测、告警转工单、运维工作流、用量计量 · Included with every MDCX: path-addressed telemetry, alarm-to-ticket, operations workflows, usage metering |
| 数字孪生 / Digital twin | **NVIDIA Omniverse** —— 实时状态投射到 3D 模型 · live state projected onto the 3D model |

---

## 11. 消防与安全 / Fire Protection & Safety ^sec-11-fire

| 项目 / Item | 参数 / Parameter |
|---|---|
| 灭火剂 / Extinguishing agent | **FM-200（HFC-227ea）** |
| 探测系统 / Detection system | **ASSD 吸气式感烟探测 / VESDA · air-sampling smoke detection / VESDA** |
| 火警主机 / Fire alarm panel | **含 / included** |
| 手动报警按钮 / Manual pull station | **含 / included** |
| 声光报警 / Horn-strobe alarm | **含 / included** |
| 门禁 / Access control | **支持读卡 / 人脸识别 · card reader / facial recognition supported** |

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
| 地基承载 / Ground load capacity | ~20–25 T（需专业工程评估 · requires professional engineering assessment） |
| 地面平整度 / Ground levelness | **±0.5°** |
| 维护净距 / Clearance requirements | 箱体四周须留足维护净距 · sufficient maintenance clearance on all four sides |
| 冷却系统接口 / Cooling system connection | 干冷器或冷却塔接口（依排热方案确定）· dry cooler or cooling tower interface, per the heat-rejection scheme |
| 场站须提供的电力 / Electrical supply to be provided by the site | 市电送至箱边即可；UPS / 电池 / 母线在箱内 · utility power to the container edge; UPS / batteries / busbar are inside |
| 运费与清关 / Freight & customs | 买方自理 / Buyer's responsibility |

> **选址建议：** 优先考虑寒冷干燥气候站点（降低 DX 依赖、改善 PUE）。TCS 进水温度越接近 26 °C，顶置机组压缩机耗电越低。
> **Site recommendation:** prioritise cold, dry climates (less DX dependence, better PUE). The closer TCS inlet sits to 26 °C, the lower the ceiling units' compressor draw.

---

## 14. 参数汇总 / Key Specifications Summary ^sec-14-summary

| 项目 / Item | 参数 / Parameter |
|---|---|
| SKU | `L1240C45SUR150` |
| 箱型 / Container type | 45ft High Cube（13,716 × 2,438 × 2,992 mm） |
| **IT 容量 / IT capacity** | **1240 kW**（8 × 150 kW 液冷 + 1 × 40 kW 风冷 · 8 × 150 kW DLC + 1 × 40 kW air-cooled）—— IT Load，非设施总负荷 · IT Load, not Total Facility Load |
| Total Facility Load | 随 PUE 变化，逐站点用 <https://mdcx.org> 计算 · varies with PUE, computed per site at <https://mdcx.org> |
| PUE | **`1.0x`** —— 逐站点计算 · computed per site |
| 单柜密度 / Rack density | **150 kW**（`R150`） |
| 机柜数量 / Rack quantity | 9（8 液冷 + 1 风冷 · 8 DLC + 1 air-cooled） |
| GPU 平台 / GPU platforms | GB300 NVL72 · B300 HGX（SXM / NVLink） |
| 冷却方式 / Cooling method | 三支路并联 TCS PG25：冷板 + RDHX + 顶置机组 · three-branch parallel TCS PG25: cold plates + RDHX + ceiling units |
| TCS 介质 / TCS fluid | **PG25**（25% 丙二醇水溶液 · 25% propylene-glycol/water） |
| TCS 进水温度 / TCS inlet temperature | **26–28 °C** |
| TCS 总循环流量 / TCS total circulating flow | ≈ **148–154 m³/h** |
| CDU | 换热 ≥ 1500 kW / 二次侧 ≥ 175 m³/h / ≥ 220 kPa，变频，2N 或 N+1 · ≥ 1500 kW / ≥ 175 m³/h / ≥ 220 kPa, VFD, 2N or N+1 |
| 室外侧排热基线 / Outdoor heat-rejection baseline | **≥ 1700 kW**（混合干冷器 + DX 板换 · hybrid dry cooler + DX plate-HX） |
| 混合冷机 / Hybrid chiller | TICA TAMFV430.3ALF5 |
| 机柜前进风温度 / Rack front intake temperature | 25–27 °C |
| **UPS** | **EATON 9395XR-1500（1500 kW），箱内 · inside the container** |
| 电池后备 / Battery autonomy | **~8 分钟 / ~8 min**（3 × 93LiG2） |
| 母线 / Busbar | **SIEMENS 2500A** |
| PDU | 输入 60 A 415 V，输出 24 位 C19，磁液压断路器 · input 60 A 415 V, 24-position C19 output, magnetic hydraulic breaker |
| 空箱重 / Empty weight | ~16 T |
| 工作温度 / Operating temperature | -45 °C ~ +45 °C |
| 灭火剂 / Extinguishing agent | FM-200 |
| 探测 / Detection | ASSD / VESDA |
| 门禁 / Access control | 读卡 / 人脸识别 · card reader / facial recognition |
| 监控 / Monitoring | PLC MODBUS / SNMP / Web · CIOS · NVIDIA Omniverse 数字孪生 / digital twin |
| 认证 / Certification | 组件 UL 认证；整机需现场 TUV 认证 · components UL certified; whole unit requires on-site TUV field certification |
| 质保 / Warranty | 核心部件自 EXW 起 1 年；后续年份按年收取服务费；响应级别以 Invoice 为准 · Core components one year from EXW; annual service fee thereafter; response level governed by the Invoice |
| 可用性 / Availability | Tier II 投资 → Tier III 级可用性 · Tier II investment → Tier III-class availability |
| 交期 / Lead time | 首批 120 天 EXW · Scale 90 天 EXW；假负载运行期 5–30 天（不含在 EXW 承诺内）；商务 / 运输 / 安装不予承诺 · 120 days EXW first batch, 90 days EXW for Scale; dummy-load burn-in 5–30 days (not covered by the EXW commitment); commercial, freight and installation are not committed |
| 价格 / Price | 配置方案由 MDCX 工程团队提供，价格由商务团队核算，请联系客户经理获取正式报价 · Configuration by the MDCX engineering team; pricing by the commercial team — contact your account manager for a formal quotation |

---

## Changelog

| 版本 / Version | 日期 / Date | 变更摘要 / Summary |
|---|---|---|
| v1.1 | 2026-08-30 | **按 2026-08-30 Yuri 四条裁定更新（[[PRODUCT_SPEC_BASELINE]] v2.0）。** ① 双环路 GPU 侧温位裁定不适用本 SKU（单环路 TCS 26–28 °C），本版未作温位改动。 ② **PUE 一律写 `1.0x`** —— 不给固定值、不给区间、不给「典型值」，逐站点用 <https://mdcx.org>（TCO / Designer）计算；Total Facility Load 的具体区间一并作废，改为「随 PUE 变化，逐站点计算」，但 IT Load vs Total Facility Load 的口径区分保留。 ③ **交期**写入正式承诺：首批 **120 天 EXW**、Scale **90 天 EXW**（自下单起算），假负载运行期 **5–30 天**（Supermicro 建议，**不含在 EXW 承诺内**）；商务 / 运输 / 安装**一律不予承诺**；删除「以商务合同为准」的占位写法与四阶段时间轴、「现场安装与调试 3–4 周」。 ④ **质保**写入正式承诺：核心部件**自 EXW 起一年**，后续年份**按年收取服务费**；ONSITE / NBD / 9×5 / 24×7 等响应级别条款**以 Invoice 为准**，本版不定义（原「1 年 / 9×5 NBD」已删除）。 本版仍不含任何价格数字，也不含任何未确认或源冲突标记。 · Updated to Yuri's four rulings of 2026-08-30: adjudicated GPU-side temperatures where applicable; PUE stated as `1.0x` and computed per site at <https://mdcx.org>; lead time committed as 120 days EXW first batch / 90 days EXW Scale with a 5–30 day dummy-load burn-in outside the EXW commitment and no commitment on the commercial, freight or installation segments; warranty committed as core components for one year from EXW plus an annual service fee, with response levels governed by the Invoice. No pricing and no unconfirmed-or-conflicted markers anywhere. |
| v1.0 | 2026-08-30 | 首版对外输出版（中英双语单文件），自 L1240C45 Tech Spec V1.4 摘录。本版收录已定型的产品参数与标注为「设计值」的工程推导值；仍在工程定型或选型评审中的参数不在本版收录范围，将在技术澄清阶段随图纸与选型书提供。交期以商务合同为准，全文不含交期数字与价格数字。锚点 `^sec-1-layout` … `^sec-14-summary` 保留；本版为单文件，块拆分待需要时再做。 · First external edition (bilingual, single file), extracted from L1240C45 Tech Spec V1.4. It carries the product parameters that are fixed plus engineering values explicitly labelled as design values; parameters still in engineering definition or selection review are outside its scope and are provided with drawings and selection sheets during technical clarification. Lead time is governed by the commercial contract; no lead-time figures and no pricing appear anywhere. |
