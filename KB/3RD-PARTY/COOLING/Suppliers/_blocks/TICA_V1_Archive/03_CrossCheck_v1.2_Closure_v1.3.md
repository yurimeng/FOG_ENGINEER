---
title: "TICA V1 — 交叉验证 + v1.2 闭环 + v1.3 新闭环"
parent: "[[.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review]]"
order: 3
tags:
  - #workspace/engineer
  - #type/review-archive
  - #product/Hybrid-Chiller
  - #vendor/TICA
  - #cooling
  - #archive
  - #MDC
created: 2026-06-18
source_file: "KB/3RD-PARTY/COOLING/Suppliers/.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review.md"
source_anchors: []
---

## 2.3 v1.2 新增 — 关键参数交叉验证（CSV 1 ↔ CSV 2 自洽性确认）

| 关键参数 | CSV 1（系统参数）| CSV 2（配置）| 自洽性 |
|----------|------------------|--------------|--------|
| 机组型号 | TAMFV430.3ALF5 | TAMFV430.3ALF5 | ✅ 同款（v1.3 厂家配置表统一）|
| 独立工质 / 压缩机数量 | 3 套独立工质系统 | 3 台 TT450 | ✅ |
| 制冷剂 | R513A | （未在 CSV 2 标注）| ✅ V1.5 §5.4 允许 R513A（Kemi 站点建议优先 R1234ze）|
| 风机数量 | 22 台 EC | 22 台 Ziehl-Abegg | ✅ |
| 旁通阀管径 | DN200 | DN200 三通阀 | ✅ |
| 蒸发器类型 | 高效满液壳管式 | 满液式换热器 | ✅ |
| 板换进水温度 | 22/32°C（FWS 一次侧）| （CSV 2 未涉及水路）| ✅ |

### 2.4 v1.2 新增 — CSV 2 闭环项

> 以下问题因 CSV 2 提供数据而**已闭环**：

| # | 闭环项 | CSV 2 答复 | V1.5 §14 接受品牌 |
|---|--------|-----------|------------------|
| ~~Q23~~ | **磁悬浮压缩机品牌** | **Danfoss Turbocor TT450-E-1-ST-SL** × 3 台 | ✅ Turbocor 在 §5.3 接受品牌清单 |
| ~~Q26-1~~ | 风机品牌 | Ziehl-Abegg 施乐百 ZN091-ZIQ.GL.V5P1 × 22 | ✅ Ziehl-Abegg 在 §9 接受品牌清单 |
| ~~Q26-2 (v1.2 初始)~~ | PLC 品牌(初始版)| Schneider 施耐德 HMIGXO3512 触摸屏 + TC180A 主控板 | ✅ Schneider 在 §14 接受品牌清单(v1.3 进一步升级为 Siemens, 见 §2.6)|
| ~~Q26-3~~ | 旁通阀品牌 / 规格 | Bray DN200 三通阀（70E201-113DB536/K）| 🟧 Bray 不在 §14 接受品牌清单（Belimo / Siemens / Honeywell），但**规格匹配 V1.5 §7.1 DN200 要求**——须 Q33 书面说明替代理由或换品牌 |

> [!info] v1.2 旁通阀说明
> Bray 不在 V1.5 §14 接受品牌清单（Belimo / Siemens / Honeywell）。CSV 2 所列 DN200 规格与 V1.5 §7.1 锁定值匹配，但品牌须 Q33 确认。

### 2.5 v1.2 新增 — CSV 2 暴露的新缺口

> CSV 2 同时暴露两项原本未发现的问题：

| # | 新缺口 | 影响 | v1.3 状态 |
|---|--------|------|-----------|
| ~~Q34~~ | **压缩机变频器品牌不达标**(v1.2 暴露, v1.3 厂家已解决) | V1.5 §14 接受 ABB / Danfoss / Siemens 之一；CSV 2 列"新时达 AS 系列"非 §14 接受品牌。须书面说明 OEM 来源 / 是否提供 §14 接受品牌的替代方案 | ✅ **已闭环 (v1.3)**: Danfoss Turbocor TT450 磁悬浮压缩机内置 VFD, 厂家已从配置表电气清单中**整项移除**独立外配变频器(参见 §2.6 + §2.2 末行) |
| **Q35** | **干冷器 V 型自制（11 台）规格未明** | V1.5 §6 锁定翅片/管材/涂层/盐雾测试报告。CSV 2 仅标"V 型换热器（自制）"，翅片（铝翅片铜管 / 全铝微通道）未明 → 与 Q29 合并跟进 | ⏳ 仍待厂家澄清(v1.3 xlsx 未提供该项) |

### 2.6 v1.3 新增 — xlsx 厂家电气配件更新闭环项

> 厂家 2026-06-06 提供更新版 xlsx 后, 以下问题**已闭环**:

| # | 闭环项 | xlsx 答复 | V1.5 §14 接受品牌 |
|---|--------|----------|------------------|
| ~~Q34~~ | **压缩机变频器品牌** | **整项移除**: Danfoss Turbocor TT450 磁悬浮压缩机内置 VFD, 无须独立外配 | ✅ 不再适用 — 闭环 |
| **Q36 (升级)** | **PLC 品牌升级** | Schneider HMIGXO3512 → **Siemens MTP700 Unified 触摸屏 + Siemens 1200 G2 控制器**(同时移除华联 TC180A + 天加 TC282 国产板卡) | ✅ **§14 接受品牌度提升**: 从 Schneider 升级为 Siemens, 同时减少 2 块国产板卡 |
| **Q37 (升级)** | **EEV 控制器升级** | 三花 VSD1001 × 2 → **Danfoss EKF 2A × 4** | ✅ Danfoss 在 §14 接受品牌清单 |
| **Q38 (新增审计)** | **电源指示灯** | 施耐德 XB2BVM × 3 | ✅ Schneider 在 §14 接受品牌清单 |
| **Q39 (新增审计)** | **急停按钮** | 施耐德 ZB2BS54C + ZB2BZ104C 红色(自带 2NC)× 1 | ✅ Schneider 在 §14 接受品牌清单 |
| **Q40 (新增审计)** | **中间继电器** | 施耐德 RXM4LB2P7 × 2 | ✅ Schneider 在 §14 接受品牌清单 |
| — | **温度传感器细化** | 久茂 902150/10-378-1001-1-6-50-999-12000/000(12m)× 12 | 🟧 Jumo 久茂非 §14 接受品牌清单(§14 待补德系传感器品牌) |
| — | **压力传感器拆分** | 丹佛斯 AKS 3000 高压 (0~30 bar) × 2 + 低压 (-1~12 bar) × 2 | ✅ Danfoss 在 §14 接受品牌清单 |
