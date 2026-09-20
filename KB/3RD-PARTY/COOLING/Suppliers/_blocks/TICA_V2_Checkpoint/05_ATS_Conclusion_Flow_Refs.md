---
title: "TICA V2.0 Checkpoint — ATS 评审 + 3rd Party 流程 + 引用 + Changelog"
parent: "[[.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2]]"
order: 5
tags:
  - #workspace/engineer
  - #type/review-archive
  - #product/Hybrid-Chiller
  - #vendor/TICA
  - #cooling
  - #archive
  - #MDC
created: 2026-06-18
source_file: "KB/3RD-PARTY/COOLING/Suppliers/.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.md"
source_anchors: []
---

## 5. ATS 综合评审

### 5.1 ATS 评审意见

**ATS 维度评审结论：有条件通过（Conditional Pass）**

- ✅ **技术规格符合 V5 基线主体要求**（性能 / 流体边界 / 压缩机 / 电气品牌 / 环境标定 / 流量 + 扬程余量）
- ✅ **关键品牌 V5 §3 / §14 合规度高**（Danfoss Turbocor + Ziehl-Abegg + Wilo + Siemens + Danfoss EEV + Schneider 配件）
- ✅ **冗余架构**（3 套独立工质 N+1 + Wilo 泵流量富余 +21.6%）
- ✅ **V5 锁定参数全数验证可达**（额定容量 +6.3% / 流量 +10.6% / 扬程 +33% / EER +86%）
- 🟥 **2 项 P0 阻塞**（Q24 UAE 极热 COP / Q31 完整认证文件）
- 🟧 **11 项 P1 关注**（V5 §6 2N 拓扑 / V5 §9 漂移联动 / V5 §11 出厂测试 / V5 §6.1 保温回执 / 旁通阀品牌 / 干冷器规格 / 加热模块 / 抗震 / 维护 / 全年能耗 / R513A 法规清单）
- 🟧 **3rd Party List 不在清单**（须 ATS / Risk / Compliance 三方评审 + Yuri 签字入库）

### 5.2 入库条件（Conditions for ATS Approval to Source）

> [!important] ATS Approve-to-Source 条件清单
> 满足以下条件后，ATS 维度可签发"Approve-to-Source"：

| 条件 | 状态 | 备注 |
|------|------|------|
| C1. Q24 UAE 46°C 极热 COP 数据提供（COP ≥ 2.8 + 四档曲线）| 🟥 待厂家回复 | P0 阻塞 |
| C2. Q31 CE + PED + UL + EN 378 / ASHRAE 15 完整认证文件 | 🟥 待厂家回复 | P0 阻塞 |
| C3. Q41 FWS 主泵 2N 拓扑确认 + 附件清单 | 🟧 待厂家回复 | V5 §6 |
| C4. Q42 ±2°C 漂移 4 层联动响应表 + 控制器迟滞 + Lead-Lag 时延 | 🟧 待厂家回复 | V5 §9 |
| C5. Q43 出厂测试矩阵 + 第三方验证报告（FWS ±0.5°C / 漂移恢复 ≤ 5 min / FC 切换 ≤ 3 min）| 🟧 待厂家回复 | V5 §11 |
| C6. Q44 一次侧管路保温前提书面回执（集成商边界声明）| 🟧 待厂家回复 | V5 §6.1 |
| C7. Q33 Bray 旁通阀替代说明 或 切换 Belimo / Siemens / Honeywell | 🟧 待厂家回复 | V5 §5 |
| C8. Q35 V 型干冷器规格（翅片 / 管材 / 涂层）+ ISO 9227 盐雾 ≥ 1000h 报告 | 🟧 待厂家回复 | V5 §5 + §8 |
| C9. R513A 6 站点（Astana 移出后 5 站点）法规适用清单 | 🟧 待厂家回复 | V5 §4 口径对齐（非阻塞）|
| C10. IPLV ≥ 5.0 实测 / 噪声 ≤ 75 dB(A) / IP54 / 寿命 ≥ 15 年补全文件 | 🟧 待厂家回复 | V5 §2 / §8 |

### 5.3 3rd Party List 增补流程

> [!warning] CLAUDE.md Hard Rule #2 — TICA 不在 3rd Party List
> 引入决策须串行经过以下流程，本评审仅完成 **ATS 部分**：

1. **ATS 评审**（本文档）— 技术规格 / 性能 / 适配性 → 🟧 有条件通过（条件 C1–C10）
2. **Risk 评审**（待 ATS 闭环后启动）— SPOF / 财务风险 / 供应链稳定性 / 售后响应能力（欧洲 + Kemi 区域）
3. **Compliance 评审**（待 Q31 闭环后启动）— CE / UL / PED 完整性 + EN 378 / ASHRAE 15 验证
4. **3rd Party List 增补决议** — Yuri 签字入库
5. **入库后**：在 `KB/3RD-PARTY/COOLING/TICA/` 下创建独立产品文档 + 同步更新 `KB/3RD-PARTY/3rd Party List.md`

### 5.4 当前状态总结

> **🟧 ATS Conditional Pass — Pending P0 Closure**
>
> - 技术维度无原则性 blocker；P0 阻塞为数据 / 认证文件缺失，非设计缺陷
> - 主流站点（UAE / TX / TH / Kemi）有条件通过；Astana 不适配（已移出考核）
> - 下一里程碑：等待厂家 Q24 / Q31 回复 → 启动 Risk + Compliance 评审 → 3rd Party List 入库

---

## 6. 引用

- 厂家原始文件（主源）：`[[TICA风冷磁浮冷水机组技术参数表&配置表]]`（xlsx · 2026-06-06 厂家更新版）
- 厂家历史投标资料：`[[风冷磁浮冷水机组技术参数表&配置表]]`（CSV 1 · 系统参数）· `[[自然冷却风冷螺杆式冷水机组]]`（CSV 2 · 配置 BOM）
- **技术规格基线**：`[[Hybrid Chiller Requirement V5]]` Checkpoint（2026-06-06）
- 归档基线（详尽法规对比 / 17 项澄清问题保留）：`.Hybrid Chiller Requirement V1.6.md`（点前缀归档）
- 治理基线：`[[../../LIQUID/L1240C45/DESIGN/L1240C45 Hydronic & Thermal Design Criteria|Rev.C]]` §9.2 ^mdc-208c23e8b6
- 上游 CDU：`[[CDU_Requirement V5]]`
- 配套邮件草稿：`[[TICA_Clarification_Email_Drafts]]`
- 3rd Party 清单：`KB/3RD-PARTY/3rd Party List.md`（当前不含 TICA）
- **本评审历史归档**：`.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review.md`（v1.0–v1.4 演化推导）

---

> **遵循 CLAUDE.md**：本文档不含价格 / 报价 / 单价信息（Hard Rule #1）。TICA 不在 3rd Party List（Hard Rule #2），不构成采购推荐。

---

## Changelog

| 版本 | 日期 | 变更摘要 |
|------|------|---------|
| **V2.0** | **2026-06-06** | **Checkpoint 抽取版**：按 5 段式重组（合并配置出处 / 合并澄清内容 / 待澄清汇总 / 综合建议 / ATS 评审）。§1 整合 CSV 1 + CSV 2 + xlsx + V5 章节对照为 9 张统一对照表（§1.1–§1.9，按 V5 §2 / §3 / §4 / §5 / §6 / §7 / §8 / §9 / §11 + BOM 品牌）。§2 合并 Q22–Q44 + V5 §10 Q 编号为统一总表（含状态 / 优先级 / V5 映射 / 闭环依据四列）。§3 拆分 P0 / P1 + 行动项 — A8 / A9 V5 补充澄清行动项保留。§4 综合建议：技术结论 / 关键亮点 / 关键缺口与风险矩阵 / 商务建议。§5 ATS 评审：意见 + C1–C10 入库条件清单 + 3rd Party List 增补流程 + 当前状态。**结论不变**：🟧 ATS Conditional Pass — Pending P0 Closure。v1.0–v1.4 详尽演化推导归档至 `.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review.md`。|
| v1.4（归档）| 2026-06-06 | 评审基线切换 V1.5/V1.6 → V5 Checkpoint。新增 Q41（FWS 2N 拓扑）/ Q42（漂移联动）/ Q43（出厂测试加项）/ Q44（保温回执）；R513A 制冷剂在 V5 §4 主表口径调整。详见归档版。|
| v1.0–v1.3（归档）| 2026-06-01 至 2026-06-06 | 初始评审 → Astana 移出 → CSV→xlsx 数据源切换 → 电气配件升级（PLC / EEV / VFD / Schneider 配件）。详见归档版。|

---

*Document Version: V2.0 Checkpoint | Last Updated: 2026-06-06 | Baseline: Hybrid Chiller Requirement V5 Checkpoint*
