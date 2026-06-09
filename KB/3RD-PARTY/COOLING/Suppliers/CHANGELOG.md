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
| `.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review.md` | 2026-06-06 | v1.0–v1.4 → V2.0 Checkpoint | (1) v1.0 初始评审；(2) v1.1 Astana 移出决策推导；(3) v1.2 CSV 1 ↔ CSV 2 同款产品识别（"螺杆"命名差异书面确认）+ Q23 闭环；(4) v1.3 xlsx 数据源切换 + 电气配件升级链条（PLC Schneider→Siemens / EEV 三花→Danfoss / Q34 内置 VFD 闭环 / 3 项 Schneider 配件 + 传感器细化）；(5) v1.4 评审基线 V1.5/V1.6 → V5 切换 + Q41–Q44 新增 + R513A 在 V5 §4 主表口径调整 | TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.md（V2.0 Checkpoint 当前活跃版）|

## 当前活跃文档

| 主题 | 当前活跃版本 | 链接 |
|------|------------|------|
| TICA TAMFV430.3ALF5 Hybrid Chiller 评审 | **V2.0 Checkpoint** | [[TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2]] |
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
