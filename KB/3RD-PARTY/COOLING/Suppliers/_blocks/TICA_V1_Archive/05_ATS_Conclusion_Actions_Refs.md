---
title: "TICA V1 — ATS 综合建议 + 行动项 + 引用 + Changelog"
parent: "[[.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review]]"
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
source_file: "KB/3RD-PARTY/COOLING/Suppliers/.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review.md"
source_anchors: []
---

## 5. ATS 综合建议

### 5.1 TICA TAMFV430.3ALF5（磁悬浮）— 推荐候选（条件性，V5 基线）

**主流站点（UAE / TX / TH / Kemi）有条件通过**，须 2 项 P0（Q24 / Q31） + 12 项 P1（含 v1.4 新增 Q41 / Q42 / Q43 / Q44）全部澄清后入 BOM 候选。
**Astana 哈萨克斯坦站点已移出厂家考核**（2026-06-02 决策；V5 附录 A 同步注明）。

**核心亮点（V5 基线下）**：
- EER 6.50 远超 V5 §2 综合 COP 3.5（+86%）
- **v1.4 新亮点**：内置 Wilo 33.24m 泵在 V5 §6 锁定（≥ 25m）下**富余 +33%**（由 V1.6 33m 的"刚好匹配"升级为"裕度释放"）
- 3 套独立工质系统（N+1 冗余）
- FWS 22 / 32°C 标定**直接吻合 V5 §2 锁定**（V1.5 26°C 已废止）
- R513A 制冷剂（A1 类 / GWP ~573 / EU/US/UAE/TH 允许；🟧 V5 §4 主表未直接列，须交叉 V1.6 §5.4 归档版）
- 流量 / 容量 / 防护 / 重量均达标
- −45°C 最低环温满足 V5 §8 标准版 −40°C，覆盖 Kemi −43°C（+2°C 裕度）
- **v1.2 闭环**: 磁悬浮压缩机品牌（Danfoss Turbocor TT450）、风机品牌（Ziehl-Abegg）、PLC 品牌（Schneider）
- **v1.3 闭环 / 升级**: 机组型号统一为 **TAMFV430.3ALF5**; PLC **升级**为 Siemens (MTP700 Unified + 1200 G2); EEV 控制器**升级**为 Danfoss EKF 2A; Q34 变频器闭环（磁悬浮内置 VFD）；3 项 Schneider 配件均 §14 合规

**关键缺口（v1.4 更新 — V5 基线）**：
- ~~磁悬浮压缩机 / 风机 / PLC / 变频器 / EEV 品牌~~ → **v1.2-v1.3 闭环**
- **UAE 极热 COP 缺数据**（Q24 ↔ V5 §10 Q24, **P0 阻塞**）
- **CE / UL / PED 认证文件未提供**（Q31 ↔ V5 §10 Q31, **P0 阻塞**）
- **干冷器 V 型换热器规格 + 散热曲线未明**（Q35 ↔ V5 §10 Q17, P1）
- **旁通阀品牌非 V5 §5 接受**（Q33, P1: Bray → 须换 Belimo / Siemens / Honeywell）
- **🆕 V5 §6 FWS 主泵 2N 拓扑未明**（Q41, P1: 单台 / 2N 配置 / 切换逻辑 / IP55 / 附件）
- **🆕 V5 §9 ±2°C 漂移 4 层联动响应未提供**（Q42, P1: 控制器响应表 / 迟滞 / 备机切换时延 / BMS 联动信号）
- **🆕 V5 §11 出厂测试加项未提供**（Q43, P1: FWS ±0.5°C / 漂移恢复 ≤ 5 min / FC 切换 ≤ 3 min）
- **🆕 V5 §6.1 一次侧管路保温前提书面回执**（Q44, P1: 集成商边界声明）
- **R513A 制冷剂**：V5 §4 主表未直接列，建议厂家在交付文件中明示法规适用站点清单（不构成阻塞，但 §4 口径需对齐）

### 5.2 入库决策前置

> [!warning] 3rd Party List 增补流程
> TICA 不在当前 3rd Party List。引入须经以下流程：
> 1. **ATS 评审**：技术规格 / 性能 / 适配性（**本评估文档输出**）
> 2. **Risk 评审**：SPOF / 财务风险 / 供应链稳定性
> 3. **Compliance 评审**：CE / UL / PED 认证完整性（**待 Q31 闭环**）
> 4. **3rd Party List 增补决议**：经 Yuri 签字后入库
> 5. **入库后**：在 `KB/3RD-PARTY/COOLING/TICA/` 下创建独立产品文档 + 同步更新 `3rd Party List.md`

---

## 6. 行动项

| # | 行动 | 责任 | 状态 |
|---|------|------|------|
| A1 | 起草厂家澄清邮件（Q24 / Q31 P0 + Q28-Q30 / Q32-Q35 P1）| ATS | ✅ **已发送**（2026-06-03，详见 [[TICA_Clarification_Email_Drafts]] 发送记录）|
| ~~A2~~ | ~~起草 R1–R5 螺杆方案退回邮件~~ | **v1.2 删除**：CSV 2 与 CSV 1 为同款产品，无须单独退回邮件 | ✅ Closed |
| A3 | 启动 TICA 3rd Party List 增补流程 | ATS / Risk / Compliance | 待 Yuri 拍板 |
| A4 | 厂家回复后更新本评审文档 | ATS | 待 Q24 / Q31 + Q28-Q30 / Q32-Q35 回复 |
| A5 | 主流站点（UAE / TX / TH / Kemi）选型报告 | Cooling Engineer | 待 Q24 / Q31 闭环 |
| ~~A6~~ | ~~极寒站点（Astana）选型报告~~ | **Astana 已移出厂家考核，行动项关闭** | ✅ Closed |
| ~~A7~~ | ~~V1.5 §3 措辞修正（"CHW Supply" → "TCS 二次侧"）~~ | **V5 §2 已直接锁定 FWS 22/32°C 一次侧 — 措辞歧义自动消解** | ✅ Closed by V5 |
| **A8（v1.4 新增）** | 起草 V5 基线补充澄清邮件（Q41 2N 拓扑 / Q42 漂移联动 / Q43 出厂测试 / Q44 一次侧保温回执 + 制冷剂法规适用清单）| ATS | 🟧 待启动 — 建议合并入下一轮厂家联络 |
| **A9（v1.4 新增）** | V5 §10 Q 编号映射回写至 `[[TICA_Clarification_Email_Drafts]]`（防止下次邮件编号错位）| ATS | 🟧 待启动 |

---

## 7. 引用

- 厂家原始文件（v1.3 主源）：`[[TICA风冷磁浮冷水机组技术参数表&配置表]]`（xlsx · 2026-06-06 厂家更新版, 含 Catalog + 配置表更新电气部分 两个 sheet）
- 厂家历史投标资料：`[[风冷磁浮冷水机组技术参数表&配置表]]`（CSV 1 · 系统参数）· `[[自然冷却风冷螺杆式冷水机组]]`（CSV 2 · 配置, 2026-06-03 厂家书面确认与 CSV 1 同款）
- **技术规格基线（v1.4 切换）**：`[[Hybrid Chiller Requirement V5]]` Checkpoint（2026-06-06）
- 归档基线（详尽法规对比 / 17 项澄清问题保留）：`.Hybrid Chiller Requirement V1.6.md`（点前缀归档版）
- 治理基线：`[[../../LIQUID/L1240C45/DESIGN/L1240C45 Hydronic & Thermal Design Criteria|Rev.C]]` §9.2
- 三支路评估：`[[../../LIQUID/L1240C45/DESIGN/L1240C45 三支路冷却重评估 2026-05-21|Rev 11]]` §4.4
- 上游 CDU：`[[CDU_Requirement V5]]`
- 配套邮件草稿：`[[TICA_Clarification_Email_Drafts]]`
- 3rd Party 清单：`KB/3RD-PARTY/3rd Party List.md`（当前不含 TICA）

---

> **遵循 CLAUDE.md**：本文档不含价格、报价或单价信息（Hard Rule #1）。TICA 当前不在 3rd Party List（Hard Rule #2），不构成采购推荐。

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| **v1.4** | **2026-06-06** | **评审基线切换至 V5 Checkpoint**（[[Hybrid Chiller Requirement V5]]）。主体结论不变（TICA 主流站点仍为有条件推荐候选），同步以下 V5 锁定变更：(1) **扬程下调 V1.6 33m → V5 §6 ≥ 25m** — TICA 33.24m 由"刚好吻合"升级为"富余 +33%"；(2) **新增 Q41**（V5 §6 2N 泵拓扑锁定 — TICA CSV 仅披露单台，须澄清 2N 配置 / 切换逻辑 / IP55 / 附件）；(3) **新增 Q42**（V5 §9 ±2°C 漂移 4 层联动 — TICA 未提供控制器响应曲线 / 迟滞 / Lead-Lag）；(4) **新增 Q43**（V5 §11 出厂测试加项 — FWS 控制精度 ±0.5°C / 漂移恢复 ≤ 5 min / FC 切换 ≤ 3 min 报告未提供）；(5) **新增 Q44**（V5 §6.1 一次侧管路保温集成商边界书面回执）；(6) **R513A 制冷剂口径**：V5 §4 主表未直接列，建议厂家明示法规适用清单（合规性保留，须交叉 V1.6 §5.4 归档版）；(7) **§3 综合对照表全面重排**至 V5 §2 / §3 / §4 / §5 / §6 / §7 / §8 / §9 / §11 章节体系；(8) **§4.0 V5 §10 ↔ TICA Q 编号映射**新增（V5 §10 Q20a/c/d / Q21 / Q24 / Q31 / Q5 / Q13 / Q17 / Q18 / Q19 → TICA Q24/Q28/Q29/Q31/Q35 等显式对照）；(9) **§1.2 内置泵表**升级标注 V5 §6 拓扑 / 防护 / 附件须澄清项；(10) Q22 闭环结论延续有效（V5 §2 直接锁定 FWS 22/32°C，V1.5 26°C 措辞歧义自动消解 → A7 行动项关闭）；(11) **新增 A8 / A9 行动项**（V5 基线补充澄清邮件 + Q 编号回写邮件草稿）。**P0 阻塞（Q24 / Q31）+ Q33 / Q35 仍待厂家回复，未变。** |
| v1.3 | 2026-06-06 | 厂家提供 xlsx 电气配件更新: (1) 型号统一为 **TAMFV430.3ALF5**(原 CSV 1 写作 "TAMFV-ALF5 430.3"); (2) §2.2 电气部件清单全表更新,新增 BLOB `^tica-v13-electrical`;(3) **Q34 闭环**: 磁悬浮压缩机内置 VFD, 厂家已整项移除独立外配变频器;(4) **Q36 升级**: PLC 从 Schneider HMIGXO3512 升级为 **Siemens MTP700 Unified + 1200 G2 控制器**(同时移除华联 + 天加国产板卡);(5) **Q37 升级**: EEV 控制器从三花 VSD1001 升级为 **Danfoss EKF 2A × 4**;(6) 新增 3 项 Schneider 配件(电源指示灯/急停按钮/中间继电器),均 §14 合规;(7) §3 综合对照表 / §4.1 已闭环项 / §4.3 P1 重要项 / §5.1 关键缺口 同步刷新;(8) §2.6 v1.3 新增段——xlsx 厂家电气配件更新闭环项;(9) 数据源从 CSV 切换至 xlsx,CSVs 保留为历史投标资料;(10) 文件**重命名**: `TICA_Hybrid_Chiller_Configuration_Review.md` → `TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review.md`(含产品型号)。P0 项(Q24/Q31)/ Q33 旁通阀 / Q35 干冷器规格 仍未闭环,仍待厂家回复。 |
| v1.2 | 2026-06-03 | 同款产品确认: 两个 CSV 对应同一款产品 TAMFV-ALF5 430.3。删除螺杆方案退回段。Q23(磁悬浮品牌) / 风机 / PLC / 旁通阀规格已闭环。 |
| v1.1 | 2026-06-02 | Astana 站点移出厂家考核;V1.6 扬程锁定 33m(机内 13m + 机外 20m)。 |
| v1.0 | 2026-06-01 | 初始评审版本。 |

---

*Document Version: v1.4 | Last Updated: 2026-06-06 | Baseline: Hybrid Chiller Requirement V5 Checkpoint*
