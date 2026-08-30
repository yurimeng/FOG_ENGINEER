---
tags:
  - #workspace/engineer
  - #type/reference
  - #product/i400c40
  - #MDC
---
# Reference Architecture — 0.4MW Immersion AI Inference Unit
0.4MW 浸没式 AI 推理算力单元标准参考架构

Reference Architecture Version: v1.3
Last Updated: 2026-08-30

> **数据源 / Source of truth：** 本文全部产品参数以 [[PRODUCT_SPEC_BASELINE]]（六 SKU 规格基准表 v2.0）为准 —— **本文任一数值与基准表冲突时，以基准表为准**。本 RA 对应 SKU：**I400C40**。
>
> **置信度标注规则见 [[UNCONFIRMED_Convention]] §2：** ✅ 已确认 · 🔶 derived 我方推导 · ⏳ #unconfirmed 待证实 · ⛔ conflict 源冲突。带 ⏳ / ⛔ 的行**不得对客外发**（[[UNCONFIRMED_Convention]] §5）。



---

## 1. 架构概述

本参考架构为基于浸没式液冷的 AI 推理算力单元，适用于边缘推理部署。

| 项目 | 内容 |
|------|------|
| IT 容量 | **0.4MW（400kW）** |
| 产品形态 | 1× AC40 集装箱 |
| 冷却技术 | 浸没式液冷（Immersion Cooling）|
| 散热方式 | **Hybrid Cooling System**（干冷器+DX一体化）|
| 交期 | **首批 120 天 EXW · Scale（扩容批次）90 天 EXW**，自下单起算；另有**假负载运行期 5–30 天**（不含在 EXW 承诺内）；商务 / 运输 / 安装**一律不予承诺**。见 [[PRODUCT_SPEC_BASELINE]] §3.1 |

---

## 2. IT负载 vs 整体电力负荷

| 项目 | 数值 | 说明 |
|------|------|------|
| **IT 负载 / IT Load** | **400kW** | 服务器、GPU 实际消耗，**不含**冷却与配电损耗 |
| **整体电力负荷 / Total Facility Load** | **随 PUE 变化，逐站点计算** | IT Load ＋ 冷却 ＋ 配电损耗 ＋ 辅助负荷。计算入口 <https://mdcx.org>（TCO / Designer）|
| PUE | **`1.0x`** | **不给固定值、不给区间、不给"典型值"**，逐站点按场地气候计算，入口 <https://mdcx.org> |

> **这两个数不是一回事，谈容量前必须先对齐口径。** 站点侧的变电申请、进线容量与开关柜选型必须按 **Total Facility Load** 计算，不能按 IT Load 计算；客户口中的「X MW」须先澄清指的是哪一个（[[PRODUCT_SPEC_BASELINE]] §3.4 · [[CLAUDE.md]] Hard Rule 5）。
>
> **PUE 一律写 `1.0x`**（2026-08-30 Yuri 裁定 · 关闭 C-2）。定性可说：干冷器可全年排热的气候落在低端，更热的站点需加混合冷机、PUE 相应上移 —— **但不给具体数**。原「按环境温度给 PUE 区间」与「整体电力负荷给 kW 区间」两种写法**均已作废**（作废的具体数值见文末 Changelog）。

---

## 3. 计算架构

| 项目 | 参数 |
|------|------|
| 服务器规格 | 双路 CPU，1.5TB RAM |
| GPU | 8 × NVIDIA RTX PRO 6000 Blackwell Server Edition |
| 服务器数量 | 按 400kW IT 包络配置（典型 ~50 台，视 GPU TDP）|
| GPU 总数 | ~400（按典型配置）|
| 单服务器 GPU | 8 × |
| 网络 | NVIDIA BlueField-3 DPU，OCP 25G × 1 |
| 服务器形态 | 4U |
| 主要用途 | AI 推理 |

> ⚠️ 服务器与 GPU 数量取决于实际 GPU TDP 与功耗包络。若客户配置 GPU TDP 较高致 IT 负载逼近 400kW 上限，需评估是否升级至多台 AC40 并联。

---

## 4. 产品配置

本方案使用 **1× AC40**：

| 项目 | AC40 参数 |
|------|-----------|
| IT 容量 | 400kW（8×50kW **I50TS（原 A32）** Tank）|
| 风冷辅助 | 10kW × 1 |
| UPS | EATON 9395XR-600（4 UPM × 150kW）|
| UPS 电池 | 2× EATON 93LiG2（10 分钟后备）|
| CDU | 内阻 Dual CDU（1+1 冗余）|
| 冷却 | **Hybrid Cooling System** |

> 如客户算力需求大于 400kW，请参考 RA-002（1.2MW DLC，DC45）或采用多台 AC40 并联。

---

## 5. 冷却架构

| 项目 | 参数 |
|------|------|
| 冷却技术 | 浸没式液冷（Immersion）|
| Tank 型号 | **I50TS**，50kW/柜（密度码 `T50`）|
| Tank 数量 | 8 台（组成 AC40）|
| 热交换器 | CDU（内置于 Tank），1+1 冗余 |
| 散热方式 | **Hybrid Cooling System**（必须）|
| 进液温度 | 32–35°C ⏳ **#unconfirmed** —— 见下注 |
| 出液温度 | 35–38°C ⏳ **#unconfirmed** —— 见下注 |

> ⏳ **#unconfirmed —— 设施水温位与基准表不一致，本次不自行统一。** [[PRODUCT_SPEC_BASELINE]] §2.2 只披露了 **I400C45 的 32 / 37 °C**，**I400C40 一栏本身即为 ⏳**（"核心相同，推同温位属 🔶 derived"）。本文的 **32–35 / 35–38 °C** 是第三套数值，来源为本 RA v1.2 既有工程口径，未经基准表确认。三套数并存、未经裁定，**本次只标注、不合并**。等 Cooling Engineer 确认 I400C40 设施水温位，预期 TBD。
>
> 注：2026-08-30 裁定 1（外冷源 32–36 °C → CDU +4 °C → GPU 36–40 °C）**只适用 L1800C45 / L450C20 两个双环路液冷 SKU**，不适用本浸没 SKU，故本节未按该链改写。

---

## 6. 电力架构

| 项目 | 参数 |
|------|------|
| 电网连接 | Grid Utility |
| UPS | EATON 9395XR-600（4 UPM，600kW），**外置（客户自备）**，AC40 本体不含 UPS |
| UPS 电池 | 2× EATON 93LiG2，**外置（客户自备）**，约 10 分钟后备 |
| 储能（BESS）| ~500kW BESS（可选，Grid 不稳定地区推荐）|
| 功率路径 | Grid → BESS → Switchgear → AC40 |

---

## 7. 冗余策略

| 系统 | 冗余级别 | 说明 |
|------|---------|------|
| **UPS 模块** | 内部 N+1（4 模块）| 单模块故障不影响运行 |
| **CDU** | Dual CDU，1+1 | 完全冗余 |
| **IT Zone（AC40）** | **无内部冗余** | 单台 AC40 独立运行 |
| BESS（可选）| 可配置 N+1 | 按客户可靠性要求 |

---

## 8. PUE 参考

| 环境条件 | 运行模式 | PUE |
|----------|---------|-----|
| 环境 <28°C | Hybrid Cooling（干冷优先）| **`1.0x`** —— 落在本产品 PUE 带的**低端** |
| 环境 28–35°C | Hybrid Cooling（DX 介入）| **`1.0x`** —— DX 介入，较低端**上移** |
| 环境 >35°C | Hybrid Cooling（DX 主导）| **`1.0x`** —— DX 主导，落在本产品 PUE 带的**高端** |

> **PUE 一律写 `1.0x`，不给固定值、不给区间**（2026-08-30 Yuri 裁定 · 关闭 C-2）。上表只保留"环境温度 → 运行模式 → PUE 高低端"的**定性**对应关系，原三档 PUE 数值已作废（作废的具体数值见文末 Changelog）。
> 具体数值请用 <https://mdcx.org> 的 TCO / Designer 按站点气候条件逐站点计算 —— 对客时给这个链接，不给数字。

---

## 9. 标准输出格式（团队引用模板）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reference Architecture — 0.4MW Immersion AI Inference Unit
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

IT Load:       400kW（1×AC40）
Total Load:    随 PUE 变化，逐站点用 https://mdcx.org 计算（不给区间）
PUE:           1.0x（逐站点计算，不给固定值）
Product:       AC40（Immersion Container，40ft）
Cooling:       Immersion + **Hybrid Cooling System**
Power:         Grid + UPS（9395XR-600）+ BESS（可选）
Redundancy:    UPS 模块 N+1 / CDU 1+1（**IT Zone 本身无内部冗余**）
Delivery:      首批 **120 天 EXW** / Scale **90 天 EXW**（自下单起算）
               假负载运行期 5–30 天（Supermicro 建议，**不含在 EXW 承诺内**）
               商务 / 运输 / 安装：**一律不予承诺**
Warranty:      核心部件自 EXW 起 1 年 + 后续按年服务费
               ONSITE / NBD / 24×7 等响应级别**以 Invoice 为准**，本文不承诺

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

---

## 10. 参考文档

- AC40 完整规格：[[I400C40|KB/PRODUCTS_I400C40]]
- I50TS 完整规格：[[I50TS|KB/PRODUCTS_I50TS]]
- MDC 组合标准：[[_COMMON/PRODUCTS_MDC|KB/_COMMON/_COMMON/PRODUCTS_MDC]]
- 冷却方案：[[COOLING_SYSTEM_Guideline]]
- UPS 规格：[[UPS_EATON_9395XR|KB/3RD-PARTY/UPS/Eaton/UPS_EATON_9395XR]]
- 上一级容量参考架构：[[RA-002_Liquid_1.2MW|RA-002 / 1.2MW DLC]]

---

*Document Version: v1.3 | Last Updated: 2026-08-30*

## Changelog

> v1.2 变更：原命名 "0.5MW" 与实际配置（1×AC40 = 400kW IT）不符。按"RA 命名 = IT 容量"原则，重命名为 0.4MW；同步修正所有 IT 负载 / Total Load 数字；删除原 §4 中混淆 RA 边界的"1.2MW 方案需 3×AC40"误导注释（1.2MW 场景应走 RA-002 / DC45）。

> v1.3 变更（2026-08-30）：**按 [[PRODUCT_SPEC_BASELINE]] v2.0 传导 2026-08-30 Yuri 四条裁定。** ① **双环路温位（C-1）—— 不适用本 SKU**：该裁定只覆盖 L1800C45 / L450C20 两个双环路液冷 SKU，本浸没 SKU 未作温位改写；§5 的 32–35 / 35–38 °C 与基准表 §2.2 不一致，已按 [[UNCONFIRMED_Convention]] 标 ⏳ #unconfirmed，**未自行统一**。 ② **PUE（C-2）**：§2 与 §8 的 `~1.02–1.08` / `~1.08–1.15` / `~1.15–1.20` / `~1.02–1.20` 全部作废，一律改写为 **`1.0x`**，逐站点用 <https://mdcx.org> 计算；Total Facility Load 的 `~408–480kW` 区间同步作废，改为"随 PUE 变化，逐站点计算"，**IT Load vs Total Facility Load 的口径区分予以保留并强化**（Hard Rule 5）。 ③ **交期（C-8）**：§1 与 §9 的 `~185–230 天` 及其五阶段拆解（勘测 / 商务 / 制造 / 运输 / 安装）**全部删除**，改为首批 **120 天 EXW** · Scale **90 天 EXW**（自下单起算），新增**假负载运行期 5–30 天**（Supermicro 建议，不含在 EXW 承诺内），商务 / 运输 / 安装**一律不予承诺**。 ④ **质保（C-9）**：§9 新增 Warranty 行 —— 核心部件自 EXW 起一年 + 后续按年服务费，ONSITE / NBD / 24×7 等响应级别以 Invoice 为准，本文不承诺（全文原无 `9×5 NBD`，无需删除）。 另：**槽体旧名 A32 全部改为 I50TS**（§4 / §5 / §10 共 3 处，§4 首次出现处保留 `I50TS（原 A32）` 对照；§10 的 wikilink 原已指向 `[[I50TS]]`、正文仍写 A32 的半迁移状态一并修复）；顶部新增数据源指针（以 [[PRODUCT_SPEC_BASELINE]] 为准 + [[UNCONFIRMED_Convention]] 标注规则）。全文不含价格数字。
