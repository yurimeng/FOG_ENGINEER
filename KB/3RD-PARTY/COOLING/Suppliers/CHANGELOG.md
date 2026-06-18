---
title: COOLING/Suppliers — 版本归档索引
date: 2026-06-06
tags:
  - "#workspace/engineer"
  - "#type/changelog"
  - "#domain/cooling"
audience: 工程师 / AI 评审追溯
---

# COOLING/Suppliers — 版本归档索引

> 本目录下文档的版本归档清单。每次版本升级时新版另存为带版本号文件，旧版以点前缀（`.filename.md`）归档；本表登记每次归档动作。

## 归档清单

| 归档文件 | 归档日期 | 上游版本 → 新版本 | 内含主要内容（保留在归档版） | 上游链路 |
|----------|---------|------------------|--------------------------|---------|
| `.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.md` | 2026-06-11 | V2.0 Checkpoint → V2.1 | (1) 四站点（UAE / TX / TH / Kemi）口径下的 §1 九张 V5 配置对照表（§1.1–§1.9）全量；(2) Q22–Q44 + V5 §10 双向映射总表原版；(3) 四站点口径 C1–C10 入库条件原版。V2.1 起考核口径收窄为 Kemi 单站点（2026-06-11 决策），四站点基线若重启以本归档版为准 | TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.1.md（当前活跃版）|
| `.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.2.md` | 2026-06-15 | V2.1 → V2.2（Full Pass, 5 类附件未入库版）→ V2.3 | (1) 2026-06-11 ATS Full Pass 决议（P0 阻塞 Q31 认证时序 + 噪声 87 dB(A) 同意接受）；(2) 3rd Party List V1.8 / STD_Supplier V1.3 入库同步；(3) V2.3 起 5 类附件（全年能效 / Wilo H-Q / 盘管选型 / SGS 盐雾 / Bray 阀 / 外形图）全部入库，本归档版作为附件未入库的 Full Pass 决策版本保留 | TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.3.md（当前活跃版）|
| `.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review.md` | 2026-06-06 | v1.0–v1.4 → V2.0 Checkpoint | (1) v1.0 初始评审；(2) v1.1 Astana 移出决策推导；(3) v1.2 CSV 1 ↔ CSV 2 同款产品识别（"螺杆"命名差异书面确认）+ Q23 闭环；(4) v1.3 xlsx 数据源切换 + 电气配件升级链条（PLC Schneider→Siemens / EEV 三花→Danfoss / Q34 内置 VFD 闭环 / 3 项 Schneider 配件 + 传感器细化）；(5) v1.4 评审基线 V1.5/V1.6 → V5 切换 + Q41–Q44 新增 + R513A 在 V5 §4 主表口径调整 | TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.md（V2.0 Checkpoint 当前活跃版）|

## 当前活跃文档

| 主题 | 当前活跃版本 | 链接 |
|------|------------|------|
| TICA TAMFV430.3ALF5 Hybrid Chiller 评审 | **V2.3**（Kemi 单站点口径 + 5 类附件数据落地 + 1 P0 EG 浓度冲突）| [[TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.3]] |
| TICA 厂家澄清应答（源文件）| V1（2026-06-11 收到）| `TICA技术澄清应答汇总V1.xlsx` |
| TICA 投标澄清邮件（存档）| — | [[TICA_Clarification_Email_Drafts]] |
| STULZ CeilAir OHS-084-DG-FC PRD | — | [[PRD-STULZ-CeilAir]] |
| Vertiv RDHx PRD | — | [[PRD-Vertiv-RDHx]] |
| 三河同飞 600 kW Chiller PRD | — | [[PRD-同飞-Chiller-600KW]] |
| 泰铂 Chiller PRD | — | [[PRD-泰铂-Chiller]] |

## 归档约定

- 版本升级到 Checkpoint（如 V2.0）时：新版另存为带版本号文件名（`_V2.md`），旧版以点前缀归档。
- 小版本迭代（如 v1.3 → v1.4）：在原文件内部 Changelog 表追加行，不另存归档版本。
- 归档原因记录在本文件，便于未来追溯演化逻辑。
- 归档文件保留全部历史推导细节；活跃版只保留 Checkpoint 结论与最新基线对照。

---

## Changelog of CHANGELOG

| 版本 | 日期 | 摘要 |
|------|------|------|
| v1.0 | 2026-06-06 | 创建 — 首次登记 TICA 评审 v1.0–v1.4 → V2.0 Checkpoint 归档动作。|
| v1.1 | 2026-06-11 | 登记 V2.0 → V2.1 归档（厂家澄清应答 V1 核对 + Kemi 单站点口径收窄）；澄清应答 xlsx 入库本目录。|
| v1.2 | 2026-06-15 | 登记 V2.1 → V2.2 → V2.3 归档（V2.2 Full Pass 决策版 → V2.3 5 类附件数据入库 + 1 项 P0 EG 浓度冲突识别）；5 类附件（Excel + PDF + DWG）入库 `TICA Response file/` 子目录。|
