---
title: "06_Escalation_Conflict_Maintenance — §5 §6 §7"
parent: "[[PRINCIPLE_Guideline]]"
order: 6
tags:
  - #workspace/engineer
  - #type/principle
  - #product/general
  - #architecture
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/PRINCIPLE_Guideline.md"
source_anchors:
  - "§5"
  - "§6"
  - "§7"
---

# §5 上报决策树 / Escalation Decision Tree

```
客户需求进入
   │
   ▼
[是否触及 §1.6 触发条件?]
   │                        │
   YES                       NO
   │                        │
   ▼                        ▼
[立即上报 ATS]      [进入 Key Matrix 场景匹配]
                            │
                            ▼
                  [按场景完成必读章节阅读]
                            │
                            ▼
                  [按章节规则进行设计/分析]
                            │
                            ▼
                  [是否产生与 Guideline 冲突?]
                            │            │
                            YES           NO
                            │            │
                            ▼            ▼
                      [上报 ATS]   [按规范输出给 ATS/AM]
```

> 上报 = 留痕。自行决定 = 责任。

---

# §6 跨 Guideline 冲突处理 / Cross-Guideline Conflict Resolution

| 冲突类型 | 处理规则 |
|---------|---------|
| **本 Principle vs 具体 Guideline** | 具体 Guideline 优先（本 Principle 提供索引与执行规则，不重复技术约束） |
| **Guideline A vs Guideline B** | 涉及安全/合规 → 合规侧优先；涉及可靠性 → 工程现实优先；不确定 → 上报 ATS |
| **Guideline vs KB 产品文档** | Guideline 优先（详见 [[COOLING_SYSTEM_Guideline#§G-15 KB 查询与验证\|§G-15]]、`AGENTS/ATS.md` §4.3） |
| **Guideline vs SOUL/PRINCIPLES.md** | SOUL/PRINCIPLES.md 优先 |
| **Guideline vs 客户需求** | Guideline 是硬约束，需求冲突时**必须上报**而非自行调整 Guideline |
| **同一 Guideline 内旧版本 vs 新版本** | 以文件头部 "Last Updated" 字段标注的版本为准 |

---

# §7 维护规则 / Maintenance Rules

| 规则 | 说明 |
|------|------|
| **新增章节 ID** | 必须按现有前缀（G-/P-/N-/C-/K-/L-/R-/M-）继续编号 |
| **章节重命名** | 必须同步更新本文件 §2 章节范围与 §4 Key Matrix 中所有引用 |
| **章节删除** | 必须在本文件 Changelog 留痕；Key Matrix 中所有引用该章节的单元格必须清除或迁移 |
| **新增 Guideline 文件** | 必须在 §2 文件清单新增一行；在 §4 Key Matrix 中按需新增 Agent × 场景列项 |
| **本 Principle 变更** | 必须更新 Changelog 并在内部 broadcast；不修改本文件则 Key Matrix 视为权威 |
