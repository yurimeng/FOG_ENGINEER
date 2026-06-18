---
title: "TICA V2.1 — 补全项 + Kemi 决策影响清单"
parent: "[[.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.1]]"
order: 3
tags:
  - #workspace/engineer
  - #type/review-archive
  - #product/Hybrid-Chiller
  - #vendor/TICA
  - #cooling
  - #archive
  - #MDC
created: 2026-06-18
source_file: "KB/3RD-PARTY/COOLING/Suppliers/.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2.1.md"
source_anchors: []
---

## 1.3 补全项

| 项 | 厂家答复要点 | V2.1 判定 |
|---|---|---|
| IPLV ≥5.0 | 本项目用 high SST 磁悬浮机组，适配高蒸发温度数据中心工况，**无法响应空调工况，无法计算 IPLV** | 🟧 理由成立 — 建议 V5 基线修订：对高 SST 机型以**全年加权 COP**（−20~35°C 曲线 + Q13 能耗模型）替代 IPLV 条款 → **A12** |
| 噪声 ≤75 dB(A) | 满载 87 dB(A) @ 1m | 🟥 见 §1.1 P0 |
| IP54 | 电控柜按 IP54 设计，**无证书** | 🟧 部分 — 要求设计声明书面化；证书项列入 Compliance 评审裁量 |
| 寿命 ≥15 年 | 满足 | ✅ 闭环（交付文件保留书面声明） |
| TT450 调速范围 | 10–100% | ✅ 闭环 |
| 100% 自然冷散热量曲线 | 可提供 | ⏳ 缺附件 |
| 外形图 + 接口高程图 | 可提供 | ⏳ 缺附件 |
| 海拔 ≥2000m 降额 | 不提供（芬兰项目） | ⛔ N/A（Kemi 海拔 <50m，口径一致） |
| TX Uri −20°C 冷启动 | 不明白报告含义，要求指明内容 | ⛔ N/A（TX 移出）。若未来重启多站点：须先提供冷启动报告定义 |
| 泰国抗震 PGA 0.08g | 不提供（芬兰项目） | ⛔ N/A（TH 移出） |
| 加热模块 | **含电伴热带**；磁浮自然冷机组进出水温高 + 无油系统，增加电加热无意义 | 🟧 工程理由可接受（Kemi −43°C 下 55% EG + 电伴热 + 两级防冻逻辑构成防冻链）；**电伴热带 ≥−45°C 认证未确认** → A10 补问 |

---

## 2. Kemi 单站点口径决策影响清单

> 决策：2026-06-11 Yuri 拍板，TICA 考核口径收窄为 Kemi（芬兰）单站点。依据：厂家应答三处明确按芬兰项目应标；TICA −45°C 最低环温 / 55% EG / Wilo −45°C 认证对 Kemi −43°C 适配度本就最高。

| 原条款 | 原优先级 | 收窄后 |
|--------|---------|---------|
| Q24 UAE 46°C 极热 COP | 🟥 P0 | ⛔ N/A（保留 −20~35°C 曲线索取，转 Q13 输入） |
| UL 1995 等效 | 🟥 P0（Q31 子项） | ⛔ N/A |
| Q30 湿膜（UAE / TH） | 🟧 P1 | ⛔ N/A（防冻逻辑子项已闭环） |
| UAE 盐雾 ≥1000h（ISO 9227） | 🟧 P1 | ⛔ 降级（热交 1000h 报告仍索取作通用佐证） |
| Q18 泰国抗震 PGA 0.08g | 🟧 P1 | ⛔ N/A |
| Q19 UAE / TH 维护频次 | 🟧 P1 | ⛔ N/A |
| TX −20/−23°C 冷启动 | 🟧 P1 | ⛔ N/A |
| 海拔 ≥2000m 降额 | 🟧 | ⛔ N/A |
| Q13 全年能耗模型 | 🟧 P1（6 站点） | 🟧 保留，**仅 Kemi 气候数据** |
| Q5 加热模块 | 🟧 P1 | 🟧 保留（Kemi 适用；电伴热带 −45°C 认证待补） |
| R513A 法规清单 | 🟧 P1 | 🟧 保留，聚焦 EU F-Gas + 芬兰 |

> ⚠️ 若未来 BD 需要 TICA 覆盖 UAE / TX / TH，须厂家**书面确认愿意扩展应标范围**后，以 V2.0 归档版四站点对照表为基线重启考核。
