---
title: "05_Changelog — §9 更新历史"
parent: "[[../3rd Party List]]"
order: 5
tags:
  - "#workspace/engineer"
  - "#type/3rd-party-list"
  - "#product/general"
  - "#architecture"
  - #MDC
created: 2026-06-18
source_file: "KB/3RD-PARTY/3rd Party List.md"
source_anchors:
  - "§9"
---

# §9. 更新历史

| 日期 | 版本 | 变更内容 |
|------|------|---------|
| 2026-08-30 | V2.1 | 新增 [[PRD-STULZ-CW320]] CW320 参数已固化（PRD v2.0 / 2026-09-08 选型书，净 29.1 kW / 风机 4.5 kW；归属 L1800C45 × 6 + L450C20 × 4，已入 BOM）。同批: [[02_Supplier_Table_Cooling_Power\|STD_Supplier §1.1]] 补 12/13/14 三行(SCR14103W / CRS560CW / CW330)并将 AC40/AC45/DC45 旧名换为新码; [[08_G14_G15_Product_Lookup\|COOLING Guideline §G-14]] 产品速查表重建为含适配 SKU 与状态的 8 行视图, §G-15 增 Step 3 置信度核查。标注规则见 [[UNCONFIRMED_Convention]]。 | ^mdc-473ef8fc22 ✅
| 2026-08-30 | V2.0 | **新增 L1800C45 冷却选型两项 ATS approved 机型**: [[PRD-STULZ-CRS560CW]](房间级 CW 精密空调 · CRAH 侧 10/16 °C · 57.3 kW/台)与 [[PRD-STULZ-SCR14103W]](CDU · 1200 kW · FWS 36/46 · TCS 40/50 · Tri-Clamp 4")。§3.1.2 / §3.2 / §3.4 三处入表; §3.2 容量匹配规则补 L1800C45 一条。两机型与现行 [[CRAH_Requirement V5]] / [[CDU_Requirement V5]](scope = L1240C45)属不同 SKU 与不同架构,差异对照见各 PRD §4; **L1800C45 专属需求书尚未建立**。同批修复 §3.1.2 / §3.2 指向已点前缀归档旧版(v3.2 / v1.3 / 无版本号)的失效链接,统一指向 V5;并修正 TICA 评审链接指向 V2.3、将已归档的 `.计算公式.md` 标注为非现行基线。 ^mdc-8c529a4dae |
| 2026-06-16 | V1.9 | **移出泰铂(干冷器+DX) · 三河同飞(600kW 集成冷站)** — 创建规则时入库, 未走正式 ATS 评审, 不构成采购推荐. §3.2 / §3.4 / §6 状态由 ✅ → ⛔ 已移出; PRD 文档保留为历史归档 (不删除); 新增 §3.5 移出原因记录 + 重新引入流程. V1.8 TICA Full Pass 维持. |
| 2026-06-11 | V1.8 | TICA Hybrid Chiller ATS Full Pass: §3.2 / §3.4 状态由 ⏳ 正在review → ✅ 已经review完成 (P0 阻塞 Q31 认证时序 + 噪声 87 dB(A) 同意接受, 可入 BOM); P1 关注内容 (消声包选配 / Q33 Bray 签字 / 附件补齐 / 噪声频谱 / IPLV→COP 基线修订) 待 TICA 提供产品后再处理。详见 [[TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.3\|TICA V2.3]]。|
| 2026-06-06 | V1.7 | 新增 [[PRD-STULZ-CeilAir]] (候选 Candidate 状态): 基于 STULZ《CeilAir Engineering Manual》2018 版 85 页 PDF 提取 OHS-084-DG-FC 全部参数; §3.2 STULZ 行添加"UL/CETL 已认证(60Hz 专用), CE / 50Hz 缺席"警示; STULZ 状态由"待 STULZ 回复"细化为"Q1 50Hz/CE 待 STULZ 回复"。 |
| 2026-06-06 | V1.6 | TICA 评审文档重命名: `TICA_Hybrid_Chiller_Configuration_Review` → `TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review`(含产品型号); 新增 `TICA风冷磁浮冷水机组技术参数表&配置表.xlsx` 厂家更新版主源;CSVs 标记为历史投标资料。 |
| 2026-06-06 | V1.5 | 重组:建立 DESIGN/ + Suppliers/ 二级分类;新增 [[../STD_Supplier]] 统一供应商管理体系入口;2 个冷却 CSV 移至 COOLING/Suppliers/;状态列与 STD_Supplier §1 同步;NETWORK 段迁至 IMMERSION/_line/ |
| 2026-05-22 | V1.4 | 新增 STULZ CeilAir、Vertiv RDHx、Hybrid Chiller 规格需求书;补充冷却 Zone DESIGN/ 子目录;完善制造供应商说明;修复 UPS 电池表空行格式 |
| 2026-04-09 | V1.3 | 新增独立 Guideline 体系;冷却系统拆分为 Guideline(架构选型)+ 产品文档;网络系统拆分为 Guideline(IB/ROCE/带内/带外)+ 产品文档;Buildin 重命名为 UPS |
| 2026-04-01 | V1.2 | 新增 Guideline 体系;BESS 目录独立,添加 Tesla Megapack 2 XL 和国轩产品文档 |
| 2026-03-29 | V1.1 | 统一命名结构;添加 UPS 型号(9395XR-600/1500);增加冷却 Zone 标准配置说明 |
| 初始版本 | V1.0 | 初始第三方产品清单 |

## Changelog

| 日期 | 变更 |
|---|---|
| 2026-09-20 | 🧭 unconfirmed-175 已可关闭，已回写来源值（已可关闭） |
