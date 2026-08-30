---
tags:
  - #workspace/engineer
  - #type/reference
  - #product/ac20
  - #MDC
---
# Reference Architecture — 0.2MW Immersion All-in-One Unit
0.2MW 浸没式一体化（All-in-One）算力单元标准参考架构

Reference Architecture Version: v1.1
Last Updated: 2026-08-30

> **数据源 / Source of truth：** 本文全部产品参数以 [[PRODUCT_SPEC_BASELINE]]（六 SKU 规格基准表 v2.0）为准 —— **本文任一数值与基准表冲突时，以基准表为准**。本 RA 对应 SKU：**I200C20**。
>
> **置信度标注规则见 [[UNCONFIRMED_Convention]] §2：** ✅ 已确认 · 🔶 derived 我方推导 · ⏳ #unconfirmed 待证实 · ⛔ conflict 源冲突。带 ⏳ / ⛔ 的行**不得对客外发**（[[UNCONFIRMED_Convention]] §5）。

---

## ⛔ CONFLICT · 未裁定 —— 「I200C20 这个产品是什么」两套口径并存

> **这不是数值差异，是产品定义级差异。在 ATS 裁定前，本文任何一节都不得单独作为对客口径引用。**
> 本块按 [[UNCONFIRMED_Convention]] §2 第四级（⛔ conflict）登记，**本次修订不选边、不合并**。

| 口径 | 内容 | 来源 |
|---|---|---|
| **口径 A —— 本 RA 现载（标配 2 槽 + 预留 2 位）** | **标配交付 2×I50TS = 100 kW**，箱内预留 2 个扩展位（B 排，预留管路走位与配电支管），现场吊装扩容至满配 4 槽 200 kW | 本文 §1 / §2 / §4 / §5.1 / §5.3 / §9（RA-003 v1.0，2026-07-12） |
| **口径 B —— 站点侧与基准表现载（满配 4 槽出售）** | **4× [[I50TS]] = 200 kW 满配**，无"标配 2 槽"一说；无风冷柜 | 站点 Designer `Immer/src/data/containers/ac20.json` · 站点已发布的 Reference Design 页（**已对客发布**）· [[PRODUCT_SPEC_BASELINE]] §2.1 |

**两套口径的实际后果不同，必须裁定：**

- **报价与交付范围**：客户拿到的是 2 槽还是 4 槽 —— 直接决定 BOM、进线容量申请与冷量匹配（本文 §5.3 的 ~160% / ~31% 两档裕度即建立在口径 A 之上）。
- **对客一致性风险**：**口径 B 已经通过站点 Reference Design 页对客发布**；本文口径 A 仅存在于 KB 内部。若销售同时引用两处，客户会看到同一 SKU 的两种产品定义。
- **扩容路径是否成立**：口径 B 若为准，本文 §9「扩展路径」（2 槽 → 4 槽现场吊装）整节的前提不成立。

**状态：** ⛔ **等 ATS 裁定，预期 TBD。** 裁定落定前：本文两处口径**同时保留**、均不删除；对客材料按 [[UNCONFIRMED_Convention]] §5 处理（⛔ 行不外发）。裁定后须同步 [[PRODUCT_SPEC_BASELINE]] §2.1 与站点 `docs/PRODUCT-MATRIX.md`。

> 相关但**不是同一条**：基准表 §2.1 记 I200C20 **无风冷柜**、并已就"交换机装在哪里"开出未裁定冲突 **C-4**（Layout Planner 裁）；而本文 §4 载「48U 风冷机柜 × 1（网络/管理设备）」、§3 载「机内 2× QM9700 交换机（Tank 间隙立式安装）」—— 本文内部亦不自洽。一并提交 C-4 处理，本次不改。

---

## 1. 架构概述

本参考架构为基于浸没式液冷的一体化（All-in-One）算力单元：20ft IT 集装箱 + 20ft 冷源框架（内置 Hybrid Chiller），整线交付、现场仅需接电接网，适用于小型边缘推理部署。

| 项目 | 内容 |
|------|------|
| IT 容量 | **0.2MW（200kW，满配 4× I50TS（原 A32））** ⛔ **产品定义未裁定，见文首 CONFLICT 块** |
| 标配交付 | **2×I50TS = 100kW**，预留 2 个扩展位 ⛔ **产品定义未裁定，见文首 CONFLICT 块**（站点侧按满配 4 槽 200 kW 出售，无「标配 2 槽」一说）|
| 产品形态 | 1× AC20（20ft IT 集装箱）+ 1× 20ft 冷源框架 |
| 冷却技术 | 浸没式液冷（Immersion Cooling）|
| 散热方式 | **Hybrid Chiller**（TASFV-080.1AAF1，自然冷却+机械制冷一体）|
| 交期 | **首批 120 天 EXW · Scale（扩容批次）90 天 EXW**，自下单起算；另有**假负载运行期 5–30 天**（不含在 EXW 承诺内）；商务 / 运输 / 安装**一律不予承诺**。见 [[PRODUCT_SPEC_BASELINE]] §3.1 |

> 命名说明：按 "RA 命名 = IT 容量" 原则（见 RA-001 v1.2 Changelog），本 RA 以满配 IT 容量 0.2MW 命名。冷源（262–283kW ≈ 0.3MW）为冷却包络，不作为命名依据。

---

## 2. IT负载 vs 整体电力负荷

| 项目 | 标配（2×I50TS）| 满配（4×I50TS）| 说明 |
|------|------------|------------|------|
| **IT 负载 / IT Load** | **100kW** | **200kW** | 服务器、GPU 实际消耗，**不含**冷却与配电损耗（I50TS 单柜 50kW Max / 45kW 推荐）。⛔ 标配 / 满配两栏本身即上方产品定义冲突的一部分 |
| **整体电力负荷 / Total Facility Load** | **随 PUE 变化，逐站点计算** | **随 PUE 变化，逐站点计算** | IT Load ＋ 冷却 ＋ 配电损耗 ＋ 辅助负荷。计算入口 <https://mdcx.org>（TCO / Designer）|
| PUE | **`1.0x`** | **`1.0x`** | **不给固定值、不给区间、不给"典型值"**，逐站点按场地气候计算，入口 <https://mdcx.org> |

> **这两个数不是一回事，谈容量前必须先对齐口径。** 站点侧的变电申请、进线容量与开关柜选型必须按 **Total Facility Load** 计算，不能按 IT Load 计算；客户口中的「X MW」须先澄清指的是哪一个（[[PRODUCT_SPEC_BASELINE]] §3.4 · [[CLAUDE.md]] Hard Rule 5）。
>
> **PUE 一律写 `1.0x`**（2026-08-30 Yuri 裁定 · **C-2 已关闭**）。原 PUE 区间、原「PUE 下限仅在某干球温度门槛以下成立」的附条件写法、以及标配 / 满配两个 Total Facility Load kW 区间**全部作废**（作废的具体数值见文末 Changelog）。定性可说：可全年自然冷却的气候落在低端，更热的站点机械制冷介入、PUE 相应上移 —— **但不给具体数**。

---

## 3. 计算架构

| 项目 | 参数 |
|------|------|
| 服务器规格 | 双路 CPU，1.5TB RAM（同 RA-001 基准配置）|
| GPU | 8 × NVIDIA RTX PRO 6000 Blackwell Server Edition |
| 服务器数量 | 标配 ~12 台 / 满配 ~25 台（按 GPU TDP 与功耗包络）|
| 单服务器 GPU | 8 × |
| 网络 | NVIDIA BlueField-3 DPU，OCP 25G × 1；机内 2× QM9700 交换机（Tank 间隙立式安装）|
| 服务器形态 | 4U（浸没竖插）|
| 主要用途 | AI 推理 |

> ⚠️ 服务器与 GPU 数量取决于实际 GPU TDP。若客户 IT 需求 >200kW，请升级至 RA-001（0.4MW，AC40）。

---

## 4. 产品配置

本方案使用 **1× AC20 + 1× 20ft 冷源框架**（端对端拼接，整线长度 ≈ 2×6.058m）：

| 项目 | AC20 参数 |
|------|-----------|
| IT 容量 | 200kW 满配（4×50kW I50TS Tank 槽位）|
| 标配 Tank | 2×I50TS（T 排），2 个扩展位（B 排，预留管路走位）|
| 风冷辅助 | 48U 风冷机柜 × 1（网络/管理设备）|
| 配电 | PDC1 × 1（直供，**无内置 UPS**）|
| UPS | 无内置；可选外置（客户自备）|
| CDU | Tank 内置 Dual CDU（1+1 冗余）|
| 冷源 | 20ft 框架内置 **TASFV-080.1AAF1 Hybrid Chiller** |
| 管路 | 底部 DN100 环管，与 Chiller 水侧（DN125）直连 |

> All-in-One 边界：与 RA-001（AC40 需现场配套 Hybrid Cooling System）不同，本方案冷源随整线出厂、管路预连，现场无冷却侧施工。

---

## 5. 冷却架构

### 5.1 浸没侧（IT Zone）

| 项目 | 参数 |
|------|------|
| 冷却技术 | 浸没式液冷（Immersion）|
| Tank 型号 | I50TS，50kW Max / 45kW 推荐 |
| Tank 数量 | 标配 2 台，满配 4 台 |
| 热交换器 | CDU（内置于 Tank），1+1 冗余 |
| Tank 进液/出液 | 35°C / 42–45°C（ΔT ≈ 10K）⏳ **#unconfirmed** —— 见下注 |
| FWS 供/回水 | 31–33°C / 38–40°C ⏳ **#unconfirmed** —— 见下注 |

> ⏳ **#unconfirmed —— 设施水温位与基准表不一致，本次不自行统一。** [[PRODUCT_SPEC_BASELINE]] §2.2 只披露了 **I400C45 的 32 / 37 °C**，**I200C20 一栏本身即为 ⏳**；[[RA-001_Immersion_0.4MW|RA-001]] 另载 32–35 / 35–38 °C。加上本文的 **35 / 42–45 °C（油侧）与 31–33 / 38–40 °C（FWS）**，vault 内浸没线设施水温位目前**至少四套并存**且未经裁定，**本次只标注、不合并**。等 Cooling Engineer 确认 I200C20 油侧与 FWS 温位，预期 TBD。
>
> 注：2026-08-30 裁定 1（外冷源 32–36 °C → CDU +4 °C → GPU 36–40 °C）**只适用 L1800C45 / L450C20 两个双环路液冷 SKU**，不适用本浸没 SKU，故本节未按该链改写。§5.2 的 Chiller 选型计算与 §5.3 冷量匹配计算过程均未改动。

### 5.2 冷源侧（Hybrid Chiller，TASFV-080.1AAF1）

| 项目 | 参数 |
|------|------|
| 制冷量 | IDC① 262kW / IDC② 283kW / GB 232kW |
| 制冷输入功率 | 77.7kW（IDC①），EER 3.37 |
| 100% 自然冷却温度 | 5°C（IDC①）/ 7.7°C（IDC②）（表列 IDC 工况）|
| 压缩机 | 半封闭螺杆，变频启动，能量调节 25–100% |
| 制冷剂 | R134a，单回路 |
| 风机 | 6 台，总风量 135,000 m³/h |
| 蒸发器 | 高效满液式壳管（Flooded Shell-and-Tube）|
| 水流量 / 压降 | 44.6 m³/h / 78 kPa，接口 DN125，设计压力 1.0MPa |
| 尺寸 / 重量 | 4220×2250×2560mm / 运输 4822kg，运行 5123kg |
| 供电 | 380V 3N~50Hz，最大运行电流 196A |

> **暖水工况说明：** 表列 100% 自然冷却温度为 IDC 低温水工况。浸没方案 FWS 供水 31–33°C（暖水），实际 100% 自然冷却窗口大幅上移：环境 ≤25°C 可全自然冷却，>28°C 机械制冷介入（对齐 I50TS Working Scenario）。

### 5.3 冷量匹配

| 配置 | IT 负载 | 冷源能力 | 裕度 |
|------|--------|---------|------|
| 标配 2×I50TS | 100kW | 262kW（IDC①）| ~160% |
| 满配 4×I50TS | 200kW | 262kW（IDC①）| ~31%（含风冷辅助与损耗后仍 >20%）|

---

## 6. 电力架构

| 项目 | 参数 |
|------|------|
| 电网连接 | Grid Utility，380V 3N~50Hz |
| 功率路径 | Grid → (BESS 可选) → Switchgear → PDC1 → I50TS Tanks / 风冷机柜 |
| 冷源供电 | Chiller 独立回路（最大 196A），与 IT 配电分开 |
| UPS | **无内置**（AC20 设计取消 UPS/UPS BESS）；如需后备，外置客户自备 |
| 储能（BESS）| 可选，Grid 不稳定地区推荐 |

> ⚠️ 与 RA-001/RA-002 的关键差异：本方案无任何内置后备电源，断电即停机。对可用性有要求的客户必须外置 UPS 或 BESS。

---

## 7. 冗余策略

| 系统 | 冗余级别 | 说明 |
|------|---------|------|
| **CDU** | Dual CDU，1+1 | 每 Tank 完全冗余 |
| **冷源（Chiller）** | **N（单机无冗余）** | 依赖冷量裕度（满配 ~31%）；压缩机故障时自然冷却窗口内可维持运行 |
| **UPS** | 无 | 见 §6 |
| **IT Zone（AC20）** | **无内部冗余** | 单台 AC20 独立运行 |
| BESS（可选）| 可配置 | 按客户可靠性要求 |

> 冷源单点是本架构与 RA-001（干冷器阵列多风扇冗余）的主要可靠性差异，选型时须向客户明示。

---

## 8. PUE 参考

| 环境条件 | 运行模式 | PUE |
|----------|---------|-----|
| 环境 <25°C | 100% 自然冷却（风机运行）| **`1.0x`** —— 落在本产品 PUE 带的**低端** |
| 环境 25–35°C | Hybrid（自然冷却+压缩机部分负载）| **`1.0x`** —— 压缩机部分负载介入，较低端**上移** |
| 环境 >35°C | 机械制冷主导（EER 3.37 → 满配约 +59kW 制冷输入）| **`1.0x`** —— 机械制冷主导，落在本产品 PUE 带的**高端** |

> **PUE 一律写 `1.0x`，不给固定值、不给区间**（2026-08-30 Yuri 裁定 · 关闭 C-2）。上表只保留"环境温度 → 运行模式 → PUE 高低端"的**定性**对应关系，原三档 PUE 数值已作废（作废的具体数值见文末 Changelog）；**EER 3.37 与满配约 +59kW 制冷输入功率属工程计算结论，予以保留**（见 §5.2）。
> 具体数值请用 <https://mdcx.org> 的 TCO / Designer 按站点气候条件逐站点计算 —— 对客时给这个链接，不给数字。

场地气候校验对照：[[PUBLIC/Reference_Architecture/Site_Reference_Climate_Standard]]

---

## 9. 扩展路径

| 阶段 | 配置 | IT 容量 | 动作 |
|------|------|--------|------|
| 标配交付 | 2×I50TS（T 排）| 100kW | — |
| 扩容 | +2×I50TS（B 排预留位）| 200kW | 现场吊装（内置 KBK 行车），接入预留支管/配电 |
| 超出 0.2MW | — | — | 升级 RA-001（AC40，0.4MW）或 RA-002（DC45，1.2MW）|

---

## 10. 标准输出格式（团队引用模板）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reference Architecture — 0.2MW Immersion All-in-One Unit
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

IT Load:       200kW 满配（标配 2×I50TS = 100kW）⛔ 产品定义未裁定，见文首 CONFLICT 块
Total Load:    随 PUE 变化，逐站点用 https://mdcx.org 计算（不给区间）
PUE:           1.0x（逐站点计算，不给固定值）
Product:       AC20（Immersion Container，20ft）+ 20ft Chiller Frame
Cooling:       Immersion + **Hybrid Chiller**（TASFV-080.1AAF1，262kW）
Power:         Grid → PDC1 直供（**无内置 UPS**；UPS/BESS 可选外置）
Redundancy:    CDU 1+1 / 冷源 N（**IT Zone 与冷源均无内部冗余**）
Delivery:      首批 **120 天 EXW** / Scale **90 天 EXW**（自下单起算）
               假负载运行期 5–30 天（Supermicro 建议，**不含在 EXW 承诺内**）
               商务 / 运输 / 安装：**一律不予承诺**
Warranty:      核心部件自 EXW 起 1 年 + 后续按年服务费
               ONSITE / NBD / 24×7 等响应级别**以 Invoice 为准**，本文不承诺

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

---

## 11. 参考文档

- I50TS 技术要求：[[I50TS Technical Requirement|KB/IMMERSION/I50TS/I50TS Technical Requirement]]
- 产品规格基准：[[PRODUCT_SPEC_BASELINE]] §2.1 / §2.2 / §3.1 / §3.3 · 标注规范：[[UNCONFIRMED_Convention]]
- MDC 组合标准：[[_COMMON/PRODUCTS_MDC|KB/_COMMON/_COMMON/PRODUCTS_MDC]]
- 冷却方案：[[COOLING_SYSTEM_Guideline]]
- 场地气候标准：[[PUBLIC/Reference_Architecture/Site_Reference_Climate_Standard]]
- 同系列（更大容量）：[[RA-001_Immersion_0.4MW|RA-001 / 0.4MW Immersion（AC40）]]、[[RA-002_Liquid_1.2MW|RA-002 / 1.2MW DLC（DC45）]]
- Chiller 规格：TICA TASFV-AAF1 系列选型表（080.1，本文 §5.2 摘录）
- 3D 模型：`MDC/AC_3D/AC20.blend`（20ft + Chiller Frame 布局）

---

*Document Version: v1.1 | Last Updated: 2026-08-30*

## Changelog

> v1.0 初版。立项工作名为 "0.3MW All-in-One"，其中 0.3MW 实为冷源包络（TASFV-080.1 制冷量 262–283kW）。按 "RA 命名 = IT 容量" 原则（RA-001 v1.2 Changelog）定名为 0.2MW（满配 4×I50TS × 50kW）；标配交付 2×I50TS = 100kW。

> v1.1 变更（2026-08-30）：**按 [[PRODUCT_SPEC_BASELINE]] v2.0 传导 2026-08-30 Yuri 四条裁定。** ① **双环路温位（C-1）—— 不适用本 SKU**：该裁定只覆盖 L1800C45 / L450C20 两个双环路液冷 SKU，本浸没 SKU 未作温位改写；§5.1 的 35 / 42–45 °C（油侧）与 31–33 / 38–40 °C（FWS）与基准表 §2.2 不一致，已按 [[UNCONFIRMED_Convention]] 标 ⏳ #unconfirmed，**未自行统一**。 ② **PUE（C-2）**：§2 与 §8 的 `~1.05–1.12` / `~1.12–1.25` / `~1.25–1.33` / `~1.05–1.33` 全部作废，一律改写为 **`1.0x`**，逐站点用 <https://mdcx.org> 计算；§2 原「下限 1.05 仅在历史极端干球温度 ≤ 24 °C 成立」的附条件 ⛔ 写法随 C-2 关闭一并撤除；Total Facility Load 的 `~105–133kW` / `~210–266kW` 区间同步作废，改为"随 PUE 变化，逐站点计算"，**IT Load vs Total Facility Load 的口径区分予以保留并强化**（Hard Rule 5）。 ③ **交期（C-8）**：§1 与 §10 的 `~185–230 天` 及其五阶段拆解（勘测 / 商务 / 制造 / 运输 / 安装）**全部删除**，改为首批 **120 天 EXW** · Scale **90 天 EXW**（自下单起算），新增**假负载运行期 5–30 天**（Supermicro 建议，不含在 EXW 承诺内），商务 / 运输 / 安装**一律不予承诺**。 ④ **质保（C-9）**：§10 新增 Warranty 行 —— 核心部件自 EXW 起一年 + 后续按年服务费，ONSITE / NBD / 24×7 等响应级别以 Invoice 为准，本文不承诺（全文原无 `9×5 NBD`，无需删除）。 另：**槽体旧名 A32 全文 18 处改为 I50TS**（含本 Changelog v1.0 条目内 2 处，§1 首次出现处保留 `I50TS（原 A32）` 对照）；顶部新增数据源指针；**文首新增 ⛔ CONFLICT 块**，登记「标配 2 槽 100 kW + 预留 2 位」（本 RA）与「满配 4 槽 200 kW」（站点 Designer `ac20.json` + 已对客发布的 Reference Design 页 + 基准表 §2.1）两套**产品定义级**口径，两种口径并列保留、**本次不选边**，等 ATS 裁定。全文不含价格数字；§5.2 Chiller 选型参数、§5.3 冷量匹配与 §7 冗余的工程计算过程与结论**未作删改**。
