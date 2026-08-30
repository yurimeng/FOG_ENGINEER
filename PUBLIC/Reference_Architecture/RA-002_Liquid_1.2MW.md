---
tags:
  - #workspace/engineer
  - #type/reference
  - #product/l1240c45
  - #MDC
---
# Reference Architecture — 1.2MW DLC AI Inference Unit
1.2MW 直冷液冷 AI 推理算力单元标准参考架构

Reference Architecture Version: v1.3
Last Updated: 2026-08-30

> **数据源 / Source of truth：** 本文全部产品参数以 [[PRODUCT_SPEC_BASELINE]]（六 SKU 规格基准表 v2.0）为准 —— **本文任一数值与基准表冲突时，以基准表为准**。本 RA 对应 SKU：**L1240C45**。
>
> **置信度标注规则见 [[UNCONFIRMED_Convention]] §2：** ✅ 已确认 · 🔶 derived 我方推导 · ⏳ #unconfirmed 待证实 · ⛔ conflict 源冲突。带 ⏳ / ⛔ 的行**不得对客外发**（[[UNCONFIRMED_Convention]] §5）。

---

## 1. 架构概述

本参考架构为基于直冷液冷（DLC）的 AI 推理算力单元，适用于中大型边缘推理集群。

| 项目 | 内容 |
|------|------|
| IT 容量 | **1.2MW（1240kW）** |
| 产品形态 | 1× DC45 集装箱 |
| 冷却技术 | Direct Liquid Cooling（直冷液冷 DLC）|
| 散热方式 | **Hybrid Cooling System**（干冷器+DX一体化）+ FCU |
| 交期 | **首批 120 天 EXW · Scale（扩容批次）90 天 EXW**，自下单起算；另有**假负载运行期 5–30 天**（不含在 EXW 承诺内）；商务 / 运输 / 安装**一律不予承诺**。见 [[PRODUCT_SPEC_BASELINE]] §3.1 |

---

## 2. IT负载 vs 整体电力负荷

| 项目 | 数值 | 说明 |
|------|------|------|
| **IT 负载 / IT Load** | **1240kW** | 服务器、GPU 实际消耗，**不含**冷却与配电损耗 |
| **整体电力负荷 / Total Facility Load** | **随 PUE 变化，逐站点计算** | IT Load ＋ 冷却 ＋ 配电损耗 ＋ 辅助负荷。计算入口 <https://mdcx.org>（TCO / Designer）|
| PUE | **`1.0x`** | **不给固定值、不给区间、不给"典型值"**，逐站点按场地气候计算，入口 <https://mdcx.org> |

> **这两个数不是一回事，谈容量前必须先对齐口径。** 站点侧的变电申请、进线容量与开关柜选型必须按 **Total Facility Load** 计算，不能按 IT Load 计算；客户口中的「X MW」须先澄清指的是哪一个（[[PRODUCT_SPEC_BASELINE]] §3.4 · [[CLAUDE.md]] Hard Rule 5）。
>
> **PUE 一律写 `1.0x`**（2026-08-30 Yuri 裁定 · 关闭 C-2；基准表中 L1240C45 原载的 PUE 区间一并作废）。定性可说：可全年自然冷却的气候落在低端，更热的站点 DX / 机械制冷介入、PUE 相应上移 —— **但不给具体数**。原「按环境温度给 PUE 区间」与「整体电力负荷给 kW 区间」两种写法**均已作废**（作废的具体数值见文末 Changelog）。

---

## 3. 计算架构

| 项目 | 参数 |
|------|------|
| 服务器类型 | GPU 服务器（如 NVIDIA B300 等 DLC 兼容服务器）|
| PSU 类型 | 单相 200–240V |
| 冷却方式 | 冷板式直冷液冷（Cold Plate DLC）|
| 服务器进口温度 | 26–28°C |
| 负载特性 | 高动态（AI 负载）|

---

## 4. 产品配置

本方案使用 **1× DC45**：

| 项目 | DC45 参数 |
|------|-----------|
| IT 容量 | 1240kW（8×150kW DLC Racks + 1×40kW 风冷）|
| 风冷辅助 | 40kW × 1 |
| UPS | EATON 9395XR-1500（10 UPM × 150kW）|
| 电池 | 3× EATON 93LiG2（8 分钟后备）|
| 主 CDU | 1.2MW Rack CDU × 1 |
| 备用 CDU | 150kW In-Rack CDU（可选）|
| FCU | **12×40kW**（根据环境温度动态调整），18–25°C |
| 冷却 | 干冷器 + DX（每台 DC45 独立配置）|
| Busbar | SIEMENS 2500A |

---

## 5. 电力架构

| 项目 | 参数 |
|------|------|
| 输入电压 | 415V AC / 3P + N + PE |
| 频率 | 50/60Hz |
| UPS | EATON 9395XR-1500（10 UPM，1500kW），内置于 DC45 |
| UPS 电池 | 3× EATON 93LiG2，内置于 DC45，约 8 分钟后备（**UPS 电池**，与 BESS 电池完全不同）|
| BESS（推荐）| Grid → BESS → DC45 |
| 母线 | SIEMENS 2500A 封闭式母线 |
| 分支方式 | Tap-off 插接，每机柜 250A |

### 5.1 配电路径

Grid / BESS → PDC → UPS（9395XR-1500）→ PDC → Busbar（2500A）
    → Tap-off Unit（TOU，含 MCCB）→ DLC Racks → PDU → Server PSU

详细电力分配和热力分析参见：https://dc45-cooling-calc.pages.dev/

---

## 6. 液冷系统架构

Hybrid Cooling System
        ↓
Primary CDU（1.2MW）← DC45 内置
        ↓
Rack CDU（150kW）← 可选，每柜一台
        ↓
GPU Server（冷板）

---

## 7. FCU 散热架构

| 项目 | 参数 |
|------|------|
| FCU 模组数量 | **12 台**（根据环境温度动态调整）|
| 单台能力 | 40kW |
| 总能力 | **480kW** |
| 工作模式 | 低温区（<28°C）：部分 FCU 运行；高温区（≥28°C）：全载运行 |
| 出风温度 | 18–25°C（压缩机可加热/制冷）|
| 排风方式 | 负压排风（百叶窗 + EC 风机）|
| 总风量 | 60,000–80,000 CMH |
| 压差控制 | ΔP 5–15Pa（机柜前微正压，后侧负压）|

> **注：** FCU 数量根据环境温度动态调整。低温环境可减少运行数量以节省能耗；高温环境需全载运行。详细电力分配和热力分析参见冷却计算工具：https://dc45-cooling-calc.pages.dev/

---

## 7.1 原厂 OEM 机柜适配

DC45 支持**不预装 DLC 机柜**，客户可后续自行安装原厂 OEM 机柜。

| 项目 | 参数 |
|------|------|
| 最大机柜宽度 | 800mm |
| 最大机柜深度 | 1200mm |
| 最大机柜高度 | 2300mm |
| 兼容品牌 | SMCI（超微）、HPE（慧与）、DELL（戴尔）、Lenovo（联想）等标准 19 英寸机柜 |
| 适配方式 | 预留液冷歧管（Manifold）接口和配电接口，支持后装 |

> **注意：** 原厂 OEM 机柜需自行确认与 DC45 液冷管路的兼容性。

---

## 8. 冷却 Zone 配置

| 项目 | 配置 |
|------|------|
| 散热方式 | **Hybrid Cooling System**（必须）|
| 主 CDU | 1.2MW Rack CDU |
| 环境 >28°C | DX 强制启动 |
| 禁止 | 纯干冷器 |

参考：[[COOLING_SYSTEM_Guideline]]

---

## 9. 冗余说明

| 层级 | 冗余描述 |
|------|---------|
| **UPS 模块** | 9395XR-1500 内置 10 个功率模块，内部 N+1（单模块故障不影响运行）|
| **CDU** | 主 CDU + 可选 In-Rack CDU（可选 1+1 配置）|
| **FCU** | 12 台中根据环境温度调整运行数量（部分 FCU 故障不影响整体）|
| **IT Zone（DC45）** | **无内部冗余** — 单台 DC45 独立运行 |
| **MDC 系统级** | 多台 DC45 并联 → 系统级冗余（由集装箱数量决定）|
| **Power Zone** | 可选 N+1/2N | 需要额外 Switchgear |

---

## 10. PUE 参考

| 环境条件 | 运行模式 | PUE |
|----------|---------|-----|
| 环境 <28°C | Hybrid Cooling（干冷优先）| **`1.0x`** —— 落在本产品 PUE 带的**低端** |
| 环境 28–35°C | Hybrid Cooling（DX介入）+ FCU | **`1.0x`** —— DX 介入，较低端**上移** |
| 环境 >35°C | Hybrid Cooling（DX主导）+ FCU | **`1.0x`** —— DX 主导，落在本产品 PUE 带的**高端** |

> **PUE 一律写 `1.0x`，不给固定值、不给区间**（2026-08-30 Yuri 裁定 · 关闭 C-2）。上表只保留"环境温度 → 运行模式 → PUE 高低端"的**定性**对应关系，原三档 PUE 数值已作废（作废的具体数值见文末 Changelog）。
> 具体数值请用 <https://mdcx.org> 的 TCO / Designer 按站点气候条件逐站点计算 —— 对客时给这个链接，不给数字。

---

## 11. 标准输出格式（团队引用模板）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reference Architecture — 1.2MW DLC AI Inference Unit
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

IT Load:       1240kW（1×DC45）
Total Load:    随 PUE 变化，逐站点用 https://mdcx.org 计算（不给区间）
PUE:           1.0x（逐站点计算，不给固定值）
Product:       DC45（DLC Container，45ft）
Cooling:       DLC + Hybrid Cooling System + FCU（12×40kW 动态调整）
Power:         Grid + UPS（9395XR-1500）+ BESS（可选）
OEM Rack:      支持 SMCI/HPE/DELL/Lenovo（宽800×深1200×高2300mm）
Redundancy:    UPS 模块 N+1 / FCU 动态配置（**IT Zone 本身无内部冗余**）
Delivery:      首批 **120 天 EXW** / Scale **90 天 EXW**（自下单起算）
               假负载运行期 5–30 天（Supermicro 建议，**不含在 EXW 承诺内**）
               商务 / 运输 / 安装：**一律不予承诺**
Warranty:      核心部件自 EXW 起 1 年 + 后续按年服务费
               ONSITE / NBD / 24×7 等响应级别**以 Invoice 为准**，本文不承诺

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

---

## 12. 参考文档

- DC45 完整规格：[[PRODUCTS_L1240C45|KB/PRODUCTS_L1240C45]]
- MDC 组合标准：[[_COMMON/PRODUCTS_MDC|KB/_COMMON/_COMMON/PRODUCTS_MDC]]
- 冷却方案：[[COOLING_SYSTEM_Guideline]]
- UPS 规格：[[UPS_EATON_9395XR|Eaton 9395XR]]
- 冷却计算工具：https://dc45-cooling-calc.pages.dev/

---

*Document Version: v1.3 | Last Updated: 2026-08-30*

## Changelog

> v1.3 变更（2026-08-30）：**按 [[PRODUCT_SPEC_BASELINE]] v2.0 传导 2026-08-30 Yuri 四条裁定。** ① **双环路温位（C-1）—— 不适用本 SKU**：该裁定（外冷源 32–36 °C → CDU +4 °C → GPU 36–40 °C）只覆盖 L1800C45 / L450C20 两个双环路 SKU；L1240C45 为**单环路** TCS 26–28 °C 暖水口径，§3「服务器进口温度 26–28°C」与基准表 §1.2 一致，本次未作温位改动。 ② **PUE（C-2）**：§2 与 §10 的 `~1.07–1.15` / `~1.15–1.25` / `~1.25–1.35` / `~1.07–1.35` 全部作废，一律改写为 **`1.0x`**，逐站点用 <https://mdcx.org> 计算；Total Facility Load 的 `~1325–1675kW` 区间同步作废，改为"随 PUE 变化，逐站点计算"，**IT Load vs Total Facility Load 的口径区分予以保留并强化**（Hard Rule 5）。 ③ **交期（C-8）**：§1 与 §11 的 `~185–230 天` 及其五阶段拆解（勘测 / 商务 / 制造 / 运输 / 安装）**全部删除**，改为首批 **120 天 EXW** · Scale **90 天 EXW**（自下单起算），新增**假负载运行期 5–30 天**（Supermicro 建议，不含在 EXW 承诺内），商务 / 运输 / 安装**一律不予承诺**。 ④ **质保（C-9）**：§11 新增 Warranty 行 —— 核心部件自 EXW 起一年 + 后续按年服务费，ONSITE / NBD / 24×7 等响应级别以 Invoice 为准，本文不承诺（全文原无 `9×5 NBD`，无需删除）。 另：本文无 A32 槽体口径（浸没线专有），无需 A32→I50TS 迁移；顶部新增数据源指针（以 [[PRODUCT_SPEC_BASELINE]] 为准 + [[UNCONFIRMED_Convention]] 标注规则）；本文首次建立 `## Changelog` 节。全文不含价格数字。冷却与电力的工程计算过程（FCU 12×40kW 热平衡、配电路径、水力口径）**未作删改**。
