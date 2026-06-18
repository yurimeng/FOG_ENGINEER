---
title: "TICA V2.2 — ATS Full Pass 评审 + 引用 + Changelog"
parent: "[[.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.2]]"
order: 4
tags:
  - #workspace/engineer
  - #type/review-archive
  - #product/Hybrid-Chiller
  - #vendor/TICA
  - #cooling
  - #archive
  - #MDC
  - #ats-full-pass
created: 2026-06-18
source_file: "KB/3RD-PARTY/COOLING/Suppliers/.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.2.md"
source_anchors: []
---

## 5. ATS 综合评审

### 5.1 ATS 评审意见

**ATS 维度评审结论：完全通过（Full Pass）— Kemi 单站点口径（2026-06-11 ATS 决议, P0 阻塞 Q31 认证时序 + 噪声 87 dB(A) 同意接受）**

- ✅ 极寒适配链条主体闭环（−45°C / 55% EG / 防冻逻辑 / Bray −45°C 阀 / 2N 主泵）
- ✅ 品牌合规度高（Danfoss Turbocor + Ziehl-Abegg + Wilo + Siemens + Schneider；Bray 偏差理由成立待签）
- ✅ P0 阻塞闭环（原 2 项 P0「Q31 认证时序 / 噪声 87 dB(A)」经 ATS 决议接受, 转入 P1 关注内容; 2026-06-11 ATS Full Pass, 可入 BOM）
- 🟧 缺附件 ×7 + 我方重发说明 ×2（Q42 / Q44）— 已降 P1
- ✅ 3rd Party List 增补: STD_Supplier V1.3 / 3rd Party List V1.8 已同步刷新状态 ⏳ → ✅

### 5.2 入库条件（C1–C10 修订版）

| 条件 | 状态 | 备注 |
|------|------|------|
| C1.（修订）CE + PED 证书编号 + 型号覆盖声明前置提供；正本下单后补 | 🟧 待厂家 | P1（原 P0, 2026-06-11 ATS 接受; 正本下单后补）|
| C2.（新增）噪声 87 dB(A) 处置方案确定（消声包 / 布局 / 基线）| 🟧 待决策 + 厂家 | P1（原 P0, 2026-06-11 ATS 接受 87 dB(A) 基线; 消声包选配待 TICA 提供）|
| C3. Q41(b)(d) 切换逻辑 + 附件清单 → 合同技术附件 | 🟧 下单交付 | V5 §6 |
| C4. Q42 响应表（我方模板重发后回填）| 🟧 待双方 | V5 §9 |
| C5. Q43 FAT 测试矩阵 + 第三方报告 → 合同技术附件 | 🟧 下单交付 | V5 §11 |
| C6. Q44 保温边界声明（我方范本重发后签回）| 🟧 待双方 | V5 §6.1 |
| C7. Q33 Bray 偏差 ATS 签字 | 🟧 待 ATS | 理由已成立 |
| C8. 缺附件 ×7 补齐 | 🟧 待厂家 | 含 R513A EU F-Gas / 芬兰清单 |
| C9. Q28 水泵定型书面确认（品牌 + 扬程不漂移）| 🟧 待厂家 | V5 §6 |
| C10. EN 378 户外豁免论证 + 电伴热带 −45°C 认证 + IP54 设计声明 | 🟧 待厂家 | Compliance 输入 |

### 5.3 当前状态总结

> **✅ ATS Full Pass — Kemi 单站点 / 2026-06-11 P0 阻塞闭环**
>
> - ✅ 极寒技术维度闭环（−45°C / 55% EG / Bray −45°C 阀 / 2N 主泵 / 噪声 87 dB(A) 基线接受）
> - 🟧 **P1 关注内容**: A10 第二轮澄清（10 项打包）/ A11 消声包选配决策 / A12 IPLV→全年 COP 基线修订 / Q33 Bray 签字 / 附件 ×7 补齐 / Q42 响应表回填 / Q44 保温边界声明签回 / Q28 水泵定型 / EN 378 户外豁免论证 / 电伴热带 −45°C 认证 / 涂层厚度
> - 📦 **下一步**: A10 第二轮澄清邮件起草 + Risk 评审（已可启动, 不再阻塞 P0）+ Compliance 持续收 C1/C8/C10 闭环材料 → 3rd Party List 已入库（STD_Supplier V1.3 / 3rd Party List V1.8）

---

## 6. 引用

- **本版主源**：`[[TICA技术澄清应答汇总V1]]`（厂家应答 xlsx · 2026-06-11 收到 · 已存本目录）
- 厂家配置主源：`[[TICA风冷磁浮冷水机组技术参数表&配置表]]`（xlsx · 2026-06-06）
- 技术规格基线：`[[Hybrid Chiller Requirement V5]]` Checkpoint（2026-06-06）
- 治理基线：`[[../../FOG D Series/DESIGN/DC45 Hydronic & Thermal Design Criteria|Rev.C]]` §9.2
- 上游 CDU：`[[CDU_Requirement V5]]`
- 第一轮澄清邮件：`[[TICA_Clarification_Email_Drafts]]`
- 3rd Party 清单：`KB/3RD-PARTY/3rd Party List.md`（**V1.8 已含 TICA Hybrid Chiller, 状态 ✅**）
- 供应商管理体系：`KB/3RD-PARTY/STD_Supplier.md` §1.1 行 4（**V1.3 已升级 ⏳ → ✅, 2026-06-11 ATS Full Pass**）
- **归档版**：`.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.1.md`（V2.1 Conditional Pass, Pending P0 Closure）· `.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.md`（V2.0 四站点九张对照表）· `.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review.md`（v1.0–v1.4）

---

> **遵循 CLAUDE.md**：本文档不含价格 / 报价 / 单价信息（Hard Rule #1）。TICA 不在 3rd Party List（Hard Rule #2），不构成采购推荐。

---

## Changelog

| 版本 | 日期 | 变更摘要 |
|------|------|---------|
| **V2.2** | **2026-06-11** | **ATS 决议: Conditional Pass → Full Pass (P0 阻塞 Q31 认证时序 + 噪声 87 dB(A) 同意接受, 可入 BOM).** §0 / §5.1 / §5.2 (C1/C2 P0→P1) / §5.3 (状态总结 + P1 关注内容展开) / §3 行动项 A3 同步刷新; frontmatter status / archived_versions / related 引用 3rd Party List V1.8 与 STD_Supplier V1.3。P1 关注内容（A10 第二轮澄清 / A11 消声包 / A12 IPLV→COP / Q33 Bray / 附件 ×7 / Q42 / Q44 / Q28 / EN 378 / 电伴热带 / 涂层）跟进中，待 TICA 提供产品后再处理。V2.1 重命名为 `.…_Review_V2.1.md` 归档（保留 Conditional Pass 表述 + Pending P0 Closure 状态）。|
| V2.1 | 2026-06-11 | 核对厂家《TICA技术澄清应答汇总V1.xlsx》全部应答（§1 逐项核对表）。**考核口径收窄为 Kemi 单站点**（2026-06-11 Yuri 决策，§2 影响清单）。P0 重构：Q24 降级 N/A；Q31 转为认证时序问题；**新增噪声 87 dB(A) P0 红旗**。新闭环：Q33（待签）/ Q34 / Q41 主体 / Q30 防冻 / 调速 / 寿命。新增行动项 A10（第二轮澄清邮件 10 项打包）/ A11（噪声决策）/ A12（IPLV→全年 COP 基线修订）。入库条件 C1–C10 全面修订。V2.0 四站点对照表归档至 `.…_Review_V2.md`。|
| V2.0（归档）| 2026-06-06 | Checkpoint 抽取版：5 段式重组 + 9 张 V5 对照表 + Q22–Q44 总表。详见归档版。|
| v1.0–v1.4（归档）| 2026-06-01 至 06-06 | 初始评审 → Astana 移出 → 数据源切换 → 电气升级 → V5 基线迁移。详见归档版。|

---

*Document Version: V2.2 | Last Updated: 2026-06-11 | Baseline: Hybrid Chiller Requirement V5 Checkpoint | Scope: Kemi 单站点 | Status: ✅ ATS Full Pass (Kemi 单站点, 可入 BOM)*
