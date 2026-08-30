---
title: "04_Manufacturing_Prohibitions_Network — §5 §6 §7 §8"
parent: "[[../3rd Party List]]"
order: 4
tags:
  - "#workspace/engineer"
  - "#type/3rd-party-list"
  - "#product/general"
  - "#architecture"
  - #MDC
created: 2026-06-18
source_file: "KB/3RD-PARTY/3rd Party List.md"
source_anchors:
  - "§5"
  - "§6"
  - "§7"
  - "§8"
---

# §5. Network Zone — 网络系统

> **V1.5 状态:** 网络类文档整体迁移至 [[KB/IMMERSION/_line/index|IMMERSION/_line/]],此处不再列出(参见 `[[KB/IMMERSION/index]]`)。
> 网络 Zone 选型原则:见 Guideline(已删除)→ 当前由各 IT Zone 设计文档自带。

---

# §6. Manufacturing & Assembly — 制造与组装

| 供应商 | 能力 | 备注 |
|--------|------|------|
| ~~三河同飞~~ | ~~冷却设备制造~~ | ⛔ **已移出** (2026-06-16, 创建规则时入库) |
| DSBJ(东山精密)| 制造 | 参考供应商 |
| 广东惠集 | 集装箱箱体制造 | **只做箱体**,其他所有件为客供,**不做总集成** |
| 惟远能源 | 标准件供应 | **只做标准件,不定制**;定制需另签研发合同;未做过 UPS 和算力机柜一体 |

> ⚠️ 注意：广东惠集(箱体)和惟远能源(标准件)有明确的业务边界,方案设计时须注意不要超出其能力范围。DSBJ 专注制造。

---

# §7. 禁止事项

- ❌ 禁止引入清单以外的第三方产品(须经 ATS 确认并更新本文件后方可使用)
- ❌ 禁止冷却 Zone 与 IT Zone 容量不匹配
- ❌ AC40/DC45 禁止纯干冷器作为唯一散热方式
- ❌ 带外管理网络不得与带内管理网络共用物理链路

---

# §8. 统一供应商管理体系入口(NEW V1.5)

> 跨类别查询供应商评审状态时,使用 [[../STD_Supplier|STD_Supplier]]。
> 本文件 §3 / §4 中的"状态"列与 STD_Supplier §1 同步。
