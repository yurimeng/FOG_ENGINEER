---
title: "CDU v3.2 — 附录 A/B + 下游联动 + ±2°C 漂移"
parent: "[[CDU_Requirement v3.2]]"
order: 7
tags:
  - #workspace/engineer
  - #type/design-spec
  - #product/CDU
  - #cooling
  - #MDC
created: 2026-06-17
source_file: "KB/3RD-PARTY/COOLING/DESIGN/.CDU_Requirement v3.2.md"
source_anchors: []
---


## §14 下游文档联动清单（v3.0 新增，CLAUDE.md Hard Rule 6 合规）

本节列出 v3.0 温度堆栈修正所**触发的下游文档变更**。本 CDU 文档不静默修改下列文件，由 Yuri 逐份确认后单独 Edit：

| # | 文档 | 路径 | 需改的具体行 | 改成什么 | 触发原因 |
|---|---|---|---|---|---|
| 1 | L1240C45 Tech Spec CN | `KB/LIQUID/L1240C45/L1240C45 Tech Spec CN.md` | L48 "TCS 进水温度 26–28°C" | **TCS 供水 26°C 单点**（v3.2）；FWS 供水 22°C / 回水 32°C；CDU 板换 approach 4°C 显式补充 | CDU v3.2 TCS / FWS 温度 + approach 锁定 |
| 2 | L1240C45 Tech Spec EN | `KB/LIQUID/L1240C45/L1240C45 Tech Spec EN.md` | L48 "TCS Inlet Temperature 26–28°C" | 与 CN 版同步英文化（TCS supply 26°C single point；FWS 22/32°C；4°C approach）| 出厂规格 CN/EN 配对 |
| 3 | L1240C45 Quick Tech Spec | `KB/LIQUID/L1240C45/L1240C45 Quick Tech Spec.md` | L33 "服务器进口温度 26–28°C" | **服务器进口（TCS 供水）26°C 单点** | Quick Spec 对外口径同步 |
| 4 | PRODUCTS_L1240C45 | `KB/LIQUID/L1240C45/PRODUCTS_L1240C45.md` | L30 + L95 重复 "服务器进口温度 26–28°C" | 同 #3 | 产品主页面同步 |
| 5 | Hybrid Chiller Requirement | `KB/3RD-PARTY/COOLING/DESIGN/Hybrid Chiller Requirement 技术规格需求书.md` | 一次/CHW 供水温度 26–28°C → **22°C**；回水 36–38°C → **32°C**；全年能耗模型 / PUE 区段图 / 干冷器自然冷却占比图 | ✅ **v1.6 已发布**（2026-06-05，本次会话同步完成；§3 / §4.2 / §11 Q20 已改完；6Sites PUE 重算待后续）| FWS 由 free-cooling 主导 → 制冷机主导，能效模型须重算 |
| 6 | L1240C45 三支路冷却重评估 V4 | `KB/LIQUID/L1240C45/DESIGN/L1240C45 三支路冷却重评估 V4.md` | §1.5 一致性核查 / §1.6 板换温度堆栈 / §8 一次侧管路保温 | ✅ **V4 已发布**（2026-06-06，本文档 v3.2 的设计基准）| 评估文档锁定 4°C approach + TCS 26°C 单点 + 100m 管路保温 |
| 7 | RDHX Requirement | `KB/3RD-PARTY/COOLING/DESIGN/RDHX_Requirement.md` | TCS 进水 28°C → 26°C；单门吸热 / 流量改为 V4 ε-NTU 实算 22.3 kW / 2.49 m³/h；9 门合计 9 → 22.4 m³/h | ✅ **v1.2 已发布**（2026-06-06）| 三支路 TCS 输入条件统一 |
| 7-A | CRAH Requirement | `KB/3RD-PARTY/COOLING/DESIGN/CRAH_Requirement.md` | TCS 进水 28°C → 26°C；S-Max 缺口 −7% → +11.6%；GPU 降载常态保障退回故障预案 | ✅ **v1.3 已发布**（2026-06-06）| S-Max 缺口翻转，客户外发文件移除算力上限披露 |
| 8 | L1240C45 Hydronic & Thermal Design Criteria Rev.C | `KB/LIQUID/L1240C45/DESIGN/L1240C45 Hydronic & Thermal Design Criteria.md` | §9.0 TCS/FWS 温度数值（如有）| 补充 v3.2 数值（TCS 26/36°C，板换 4°C approach）| Rev.C 与 v3.2 数值对齐 |
| **9（v3.2 新增）** | **L1240C45 三支路冷却重评估 V4 §8 / Hybrid Chiller V1.6 §10.1**（一次侧管路联动）| `KB/LIQUID/L1240C45/DESIGN/L1240C45 三支路冷却重评估 V4.md` §8 + `KB/3RD-PARTY/COOLING/DESIGN/Hybrid Chiller Requirement 技术规格需求书.md` §10.1 | 100m FWS 管路保温要求（DN200 主干 95m + DN100 CDU 接入 5m，≥50mm 岩棉）| ✅ **V4 §8 + Chiller V1.6 §10.1 + 本 CDU v3.2 §10.5 三处已同步**（2026-06-06）| 一次侧管路若不保温，无保温下 30% 负载 CDU 进水漂移 4.4K，吃光 4°C approach 预算 |
| 5 | Hybrid Chiller Requirement | `KB/3RD-PARTY/COOLING/DESIGN/Hybrid Chiller Requirement 技术规格需求书.md` | §1.1 S-Max 1352→1350 kW；§10.1 新增一次侧管路联动条款 | ✅ **V1.6 微调已发布**（2026-06-06）| 数据对齐 V4 + 管路联动声明 |

> **CLAUDE.md Hard Rule 6 合规说明**：本 v3.2 仅修改 `CDU_Requirement.md` 本身。上述 #1–#4 / #8（L1240C45 Tech Spec CN/EN / Quick Tech Spec / PRODUCTS_L1240C45 / Hydronic Criteria）任何一份文档的实际修改均待 Yuri 单独授权后逐份 Edit。#5 / #6 / #7 / #7-A / #9 已在本会话内全部同步完成（V4 / Chiller V1.6 / RDHX v1.2 / CRAH v1.3 / CDU v3.2）。

> ⚠️ **跨文档不一致期窗口**：v3.2 发布日 (2026-06-06) → 上述 #1–#4 / #8 全部同步完成日之间，DC45 主规格 / Quick Spec / PRODUCTS_L1240C45 / Hydronic Criteria 仍可能写 TCS 28°C 旧值。对外供应商沟通以本 CDU v3.2 为准；对客户外发资料须暂缓更新 TCS / FWS 数值，直至全部联动到位。

---

---

## §15 极端工况应对：CDU 进水 ±2°C 漂移（v3.2 新增） ^cdu-15-drift-response

> **场景**：CDU 一次侧进水（FWS）从 22°C 标称漂移到 **20–24°C**（±2°C），假设 CDU 板换 approach 4°C 不变。详见 [[../../LIQUID/L1240C45/DESIGN/L1240C45 三支路冷却重评估 V4|V4]] §9 完整评估。

### 15.1 触发条件
- Chiller 控制器故障 / VFD 失稳（V1.6 §3 标称精度 ±0.5°C，±2°C 是 4× 故障带）
- 一次侧管路保温损坏（V4 §8 计算：极端工况下无保温漂移可达 4K）
- Chiller 干冷器堵塞 + 极热 / free-cooling 阀失效

### 15.2 CDU 本体工作状态

| 漂移 | FWS 进/出 | TCS 供/回 | 板换 LMTD | UA 需求 | 状态 |
|------|---------|---------|---------|---------|------|
| 冷端 −2°C | 20°C / 30°C | 24°C / 34°C | **4°C 不变** | ≥ 375 kW/K **不变** | ✅ |
| 标称 | 22°C / 32°C | 26°C / 36°C | 4°C | ≥ 375 kW/K | ✅ |
| 热端 +2°C | 24°C / 34°C | 28°C / 38°C | **4°C 不变** | ≥ 375 kW/K **不变** | ✅ |

> **关键结论**：approach 4°C 假设保持时，**CDU 板换换热能力完全不受 ±2°C 漂移影响**（LMTD 与 UA 需求均不变，Q ≥ 1500 kW 仍兑现）。下游温度跟随漂移，但 CDU 本体 BOM 无需任何变更。

### 15.3 CDU 二次泵流量校核

| 漂移 | B1 | B2 | B3 | 总流量 | 占设计容量 ≥175 m³/h |
|------|-----|-----|-----|------|----------------------|
| 冷端 −2°C | 78.3 | 25.0 | 48.7 | 152.0 m³/h | 87% ✅ |
| 标称 | 78.3 | 22.4 | 48.7 | 149.3 m³/h | 85% ✅ |
| 热端 +2°C | 78.3 | 19.7 | 48.7 | 146.7 m³/h | 84% ✅ |

> Branch 2 流量随 TCS 漂移在 19.7–25.0 m³/h 区间变化（吸热比例 48.6–61.4%），PICV 量程 0–30 m³/h 全覆盖。二次泵 VFD 流量调节范围 70–100% (122.5–175 m³/h) 全工况覆盖。

### 15.4 CDU 控制器（PLC）应对动作

CDU 控制器须在 §6 控制策略基础上增加漂移响应逻辑：

| 漂移条件 | CDU 自主动作 | BMS 联动信号 |
|---------|------------|------------|
| 冷端 −1°C 以下持续 30s | 二次泵 VFD 降频至 70%（节能）| 上报 Chiller free-cooling 优先 |
| 冷端 −2°C 以下持续 30s | 同上 + 预警告警 | 上报"FWS 过冷" |
| **热端 +1°C 以上持续 30s** | 二次泵 VFD 升频至 95% | 上报 Chiller 提升压缩机负荷 |
| **热端 +1.5°C 以上 + S-Max 工况** | 同上 + 输出 GPU 降载至 95% 信号 | 主动缓解 CeilAir 负荷 |
| **热端 +2°C 持续 > 5 分钟** | 同上 + 输出 GPU 降载至 93% 信号（V4 §9.5 兜底） | 故障告警 |
| 漂移 > ±3°C | 紧急停机或 N+1 切换 | Chiller 严重故障告警 + GPU 降载至 60% |

### 15.5 监测传感器要求（新增到 §6 控制规格）

| 传感器 | 位置 | 精度 | 用途 |
|--------|------|------|------|
| **PT100** | CDU P-IN 进水侧 | ±0.2°C | 一次侧温度监测 + 漂移检测 |
| PT100 | CDU P-OUT 出水侧 | ±0.2°C | 一次侧 ΔT 校验 |
| PT100 | CDU S-OUT 二次侧供水 | ±0.2°C | 二次侧温度监测 |
| PT100 | CDU S-IN 二次侧回水 | ±0.2°C | 二次侧 ΔT 校验 + 冷板 ΔT 校核 |

### 15.6 与下游组件的协同

| 组件 | 状态 | 详见 |
|------|------|------|
| Branch 1（GPU 冷板）| ✅ 冷板入水 24–28°C 全在 GPU 平台设计范围 | V4 §9.3.1 |
| Branch 2（RDHx）| ✅ 单门 19.7–24.85 kW，PICV 全覆盖 | [[RDHX_Requirement]] §13 / V4 §9.3.2 |
| Branch 3（CeilAir）| ⚠️ 热端 +2°C × S-Max 余量 **−3.1%** | [[CRAH_Requirement]] §15 / V4 §9.3.3 |
| Chiller（一次侧）| ⚠️ 热端漂移恶化 PUE；冷端利好 | [[Hybrid Chiller Requirement 技术规格需求书]] §16 / V4 §9.3.5 |

---

*文档维护说明：本文档为 v3.2 技术需求，**对齐 V4 4°C approach 抉择**（详 §1.4）。**§15 新增 ±2°C 漂移应对**（V4 §9 同步）。待供应商书面回复 Q1（v3.2 重发）/ Q1-A（UA ≥ 375 kW/K）/ Q1-B / Q2–Q9 后升级为正式规格书 v3.3。任何架构调整须回溯到 [[../../LIQUID/L1240C45/DESIGN/L1240C45 三支路冷却重评估 V4|V4]] 校核闭环。*

> **遵循 CLAUDE.md**：本文档不含价格、报价或单价信息（Hard Rule 1）。CDU 选型与采购由 ATS 整合输出技术规格，价格由商务团队按确认配置单独核算。本次 v3.2 修订严格遵循 Hard Rule 6（无静默改），所有触发的下游文档变更均在 §14 列明，#1–#4 / #8 待 Yuri 单独授权。
