---
title: "I400C40 第三节：IT 容量"
parent: "[[I400C40_Tech_Spec_CN]]"
order: 3
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/i400c40"
  - "#MDC"
created: 2026-07-28
source_file: "PUBLIC/Tech_Spec/I400C40_Tech_Spec_CN.md"
source_anchors:
  - "^sec-3-it-capacity"
---

## 3. IT 容量 ^sec-3-it-capacity

| 项目 | 参数 |
|------|------|
| **IT 总容量（推荐）** | **360kW**（8 × I50TS × 45kW） ^mdc-7db5bf0c0e |
| **IT 总容量（最大）** | **400kW**（8 × I50TS × 50kW） ^mdc-2e262d049b |
| 浸没槽 | 8 × I50TS（每柜推荐 45kW / 最大 50kW，2N CDU 散热冗余） ^mdc-0b25089fdb |
| 风冷机柜 | 1 × **10kW**（独立风冷，不计入浸没 IT 主容量时可单独列项） |
| 机架空间 | **256RU / 232OU**（8 × 32RU） ⏳ **#unconfirmed** —— 取自旧基线 AC40 V1.4，[[PRODUCT_SPEC_BASELINE]] 未覆盖；等 I400C40 DESIGN/ 工程文档（出厂图纸 / 称重报告 / 结构计算书）产出并回写基准表，预期 TBD ^mdc-6760e79a51 |
| 二次侧进/出油温 | **进油 ≤35°C / 出油 ≈43°C，ΔT=8K** |
| 一次侧进/出水温 | **≤32 / 37°C（ΔT=5K）** ⛔ **conflict** —— [[PRODUCT_SPEC_BASELINE]] §2.2 仅对 I400C45 有站点依据，I400C40 同温位属推导；等 Cooling Engineer 确认 I400C40 是否同温位并回写基准表，预期 TBD ^mdc-53355b21ea |
| 设计环境湿球温度 | **28°C** ⏳ **#unconfirmed** —— 取自旧基线 AC40 V1.4，[[PRODUCT_SPEC_BASELINE]] 未覆盖；等 I400C40 DESIGN/ 工程文档（出厂图纸 / 称重报告 / 结构计算书）产出并回写基准表，预期 TBD ^mdc-66c3c4f7fc |
| 功率因数（UPS 输出侧） | **0.9**（外置 UPS 按此选型） |

### IT 负载 vs 整体电力负荷

| 项目 | 数值 | 说明 |
|------|------|------|
| **IT 负载** | 推荐 360kW / 最大 400kW | 服务器、GPU 实际消耗（浸没 Tank） |
| **整体电力负荷（Total Facility Load）** | 随 PUE 变化，**逐站点用 <https://mdcx.org> 计算** | ✅ 2026-08-30 裁定（关闭 C-2）。原「~400–480kW」区间作废 |
| **PUE** | **`1.0x`** | ✅ 2026-08-30 裁定。**不给固定值、不给区间、不给「典型值」**，逐站点计算，入口 <https://mdcx.org>（TCO / Designer）。原「~1.05–1.10 / ~1.15–1.20」全部作废 |

> **IT Load ≠ Total Facility Load。** 客户口头「400kW」须澄清是 IT 还是站端总用电。整体负荷 = IT + 冷却电耗 + 配电损耗 + 辅机。UPS 外置时，UPS 损耗与电池柜散热**不在 I400C40 本体内**，但须计入站端总容量。**这个区分是硬规则（[[CLAUDE.md]] Hard Rule 5），必须保留；但设施负荷不给数字。** ^mdc-42629c1144
>
> 定性可说：干冷器可全年排热的气候落在低端；更热的站点需加混合冷机，PUE 相应上移。**但不给具体数。** 见 [[PRODUCT_SPEC_BASELINE#^baseline-pue]]。

### 与电气计算书的关系

舱内 415VAC 电气负荷分项见 §6（源：[[I400C40 工作负荷]]）。IT-PDC1 / IT-PDC2 各按约 381kW 配置，为 **双路 A/B 馈电能力**（每 Tank 双 PDU），**不是**同时 762kW IT 有功。同时 IT 有功仍以 **360–400kW** 为准。 ^mdc-0198389948

---

## Changelog

| 日期 | 变更 |
|---|---|
| 2026-09-20 | 🧭 unconfirmed-062 改为 ⛔ conflict，未裁定赢家 |
