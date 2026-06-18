---
title: §9 下一步建议 + §10 CLAUDE.md 合规自检
parent: "[[../COOLING_DESIGN_v4_lockdown_plan]]"
order: 6
tags:
  - #workspace/engineer
  - #type/lockdown-plan
  - #cooling
  - #MDC
created: 2026-06-18
source_file: "KB/3RD-PARTY/COOLING/DESIGN/COOLING_DESIGN_v4_lockdown_plan.md"
source_anchors: []
---

## 9. 下一步建议

1. **你抉择 Reading（A / B / C）**：见 §2 + §7。最关键的决策点。
2. **物理/结构/尺寸 Request 立即锁定**：§3.1 / §4.1 / §5.1 / §6.1 共 ~70 项，与 Reading 无关，授权后我可一次性 Edit 至四份 Requirement 文档（每份加 "v4 物理/结构 Request 锁定" 章节）。
3. **热力 Request 分批锁定**：§3.2 / §4.2 / §5.2 / §6.2 / §7，待你 Reading 确认后再做。
4. **CRAH 选型决策**：若 Reading B/C，需启动 **直冷水盘管 CRAH 选型**（STULZ CCD / Vertiv Liebert PCW / 同级），与 STULZ 重新接触；CRAH_Requirement.md 整份重做。
5. **6Sites + 三支路重评估**：v4 PUE 重算（独立于设备 Request 锁定，由 Cost Architect / Risk Auditor 启动）。

---

## 10. CLAUDE.md 合规自检

- Hard Rule 1（无价）：本清单全无价格、报价、单价 ✅
- Hard Rule 2（仅核心线 + KB 3RD-PARTY）：仅引用核心 KB 内产品（STULZ CeilAir / Vertiv DCD35 / Eaton UPS / Tesla Megapack / 三河同飞 / 泰铂）✅
- Hard Rule 5（IT Load vs Total Facility Load）：IT Load 1240 kW 明示 ✅
- Hard Rule 6（无静默改 vault）：本清单写在 outputs/，未改 vault 任何文件 ✅
- Hard Rule 7（UPS ≠ BESS）：UPS 8 分钟 / BESS 30 分钟仍按 V1.5 / 6Sites 锁定 ✅

---

*本清单只列结论。任何 vault 文件的实际 Edit，待你 §9 步骤 1 / 2 / 4 单独授权。*
