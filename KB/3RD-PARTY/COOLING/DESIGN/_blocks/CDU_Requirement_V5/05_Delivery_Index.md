---
title: "CDU V5 — 交付要求 + 上下游对齐索引"
parent: "[[CDU_Requirement V5]]"
order: 5
tags:
  - #workspace/engineer
  - #type/design-spec
  - #product/CDU
  - #cooling
  - #MDC
created: 2026-06-17
source_file: "KB/3RD-PARTY/COOLING/DESIGN/CDU_Requirement V5.md"
source_anchors: []
---

## 9. 交付要求

| 项 | 要求 |
|---|---|
| 交付物 | CDU 本体（板换 / 二次泵 ×2 / VFD ×2 / 膨胀罐 / 控制柜 / 内部管路 / 保温）|
| 数量 | 1 台 / DC45 ^mdc-c0ac38d069 |
| **不在交付范围** | 外部分配 manifold / 三支路 PICV / 隔离阀 / 平衡阀 / 止回阀 / 过滤器 / 流量计 / 温度计 / 压力表（由 ATS 单独打包采购）|
| 附件文档 | 安装手册（CN/EN）/ 接口尺寸图 / PG25 兼容证明 / ΔP 曲线 / 出厂测试报告 |
| 出厂测试 | **两组温度堆栈**（详 §2 板换 Q 闭环行）|
| 质保 | ≥ 2 年（关键件 ≥ 5 年）|

---

## 10. 与 V5 主文件 / 上下游对齐索引

| 参数 | 本文档 | V5 主文件 | 上下游 |
|---|---|---|---|
| FWS 22/32°C | §1 / §3 | §1 架构基线 | [[Hybrid Chiller Requirement V5]] §3 |
| Approach 4°C / LMTD 4°C / UA ≥ 375 kW/K | §1 / §2 | §1 架构基线 / §3.1 | — |
| TCS 26/36°C | §1 / §3 | §1 架构基线 | [[RDHX_Requirement V5]] §3 / [[CRAH_Requirement V5]] §3 |
| 二次侧 ≥ 175 m³/h / ≥ 220 kPa / VFD / 2N | §2 | §3.1 | — |
| PICV B1/B2/B3 量程 | §4 | §3.2 | RDHx §4 / CRAH §6 |
| 一次侧管路保温 ≥ 50mm 岩棉 | §6 | §6 | [[Hybrid Chiller Requirement V5]] §10.1 |
| ±2°C 漂移 4 层联动 | §7 | §5 | RDHx §6 / CRAH §6 |
