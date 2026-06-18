---
title: "TICA V2.0 Checkpoint — 待澄清点 + 综合建议"
parent: "[[.TICA_TAMFV430.3ALF5_Hybrid_Chiller_Configuration_Review_V2]]"
order: 4
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

## 3. 待澄清点汇总

### 3.1 🟥 P0 阻塞项（入 BOM 必须澄清）

1. **Q24 — 极热 COP（UAE 46°C 满载）**：缺 46°C DB / 30°C WB 工况下整机制冷量 ≥ 1,200 kW + COP ≥ 2.8 数据；缺四档 COP 曲线（15 / 25 / 35 / 48°C 含湿膜启停边界）。**影响**：V5 §2 强制 / UAE 站点选型 BOM 闭环。
2. **Q31 — CE / UL / PED 认证**：缺 CE 证书（含 PED 2014/68/EU）+ UL 1995 等效 + EN 378 / ASHRAE 15 制冷剂泄漏证明。**影响**：V5 §7 入库硬约束 / Compliance 评审硬条件。

### 3.2 🟧 P1 关注项（入 BOM 候选前补全）

**新增（v1.4 → V2.0）**
- **Q41** — FWS 主泵 2N 拓扑（双泵 / 切换逻辑 / IP55 / 附件清单）
- **Q42** — ±2°C 漂移 4 层联动响应表 + 控制器迟滞 + Lead-Lag 轮换 + BMS 信号清单
- **Q43** — 出厂测试加项（FWS ±0.5°C / 漂移恢复 ≤ 5 min / FC 切换 ≤ 3 min）
- **Q44** — 一次侧管路保温集成商边界书面回执

**已有澄清项**
- Q28（H-Q + 水侧 ΔP 曲线）/ Q29（干冷器 4 档环温散热）/ Q30（湿膜选配）/ Q32（旁通 PID 阈值）/ Q33（Bray 旁通阀品牌替代）/ Q35（V 型干冷器规格 + 盐雾）
- V5 §10 Q5（加热模块）/ Q13（全年能耗）/ Q18（泰国抗震）/ Q19（维护频次）/ Q20d（FC 阈值新校核）

**补全数据项**
- IPLV ≥ 5.0 实测 / 噪声 ≤ 75 dB(A) / IP54 / 寿命 ≥ 15 年证书
- UAE 盐雾 ≥ 1000h 报告（ISO 9227）/ TX −23°C 冷启动
- R513A 法规适用站点清单（V5 §4 主表口径对齐 — 非阻塞）

### 3.3 行动项

| # | 行动 | 责任 | 状态 |
|---|------|------|------|
| A1 | 起草厂家澄清邮件（Q24 / Q31 P0 + Q28–Q30 / Q32–Q35 P1）| ATS | ✅ 已发送（2026-06-03）参见 [[TICA_Clarification_Email_Drafts]] |
| A3 | 启动 TICA 3rd Party List 增补流程 | ATS / Risk / Compliance | 🟧 待 Yuri 拍板 |
| A4 | 厂家回复 Q24 / Q31 后更新本评审 V2.x 节点 | ATS | 🟧 待 Q24 / Q31 闭环 |
| A5 | 主流站点（UAE / TX / TH / Kemi）选型报告 | Cooling Engineer | 🟧 待 P0 闭环 |
| **A8（v1.4 → V2.0）** | 起草 V5 补充澄清邮件（Q41 / Q42 / Q43 / Q44 + R513A 法规适用清单 + Q33 / Q35 跟进）| ATS | 🟧 待启动 — 建议合并入下一轮厂家联络 |
| **A9（v1.4 → V2.0）** | V5 §10 Q 编号映射回写至 [[TICA_Clarification_Email_Drafts]]（防止下次邮件编号错位）| ATS | 🟧 待启动 |

---

## 4. 综合建议

### 4.1 技术结论

**V5 基线下 TICA TAMFV430.3ALF5 主体技术符合**。核心性能（额定 1,700 kW、EER 6.50、FWS 22/32°C 直接吻合、Wilo 33.24m 扬程对 V5 ≥ 25m 富余 +33%、−45°C 最低环温覆盖 Kemi）+ 关键品牌（Danfoss Turbocor 压缩机 / Ziehl-Abegg 风机 / Wilo 泵 / Siemens PLC / Danfoss EKF EEV）均达 V5 §2 / §3 / §6 / §14 要求；3 套独立工质满足 N+1 冗余；磁悬浮 + R513A 组合达成无油 + 低 GWP。

### 4.2 关键亮点

1. **V5 §6 扬程下调带来的裕度释放**：V1.6 33m → V5 25m 锁定下，Wilo 33.24m 由"刚好匹配"升级为"富余 +33%"。机内 13m + 机外 20m 总扬程 33m 设计余量在 V5 锁定下进一步释放，100m FWS 管路 + CDU 一次侧损失即便偏保守估算也充分覆盖。
2. **FWS 22/32°C 一次侧标定直接吻合 V5 §2 锁定**（V1.5 26°C 已废止 — Q22 闭环结论延续有效）。
3. **磁悬浮 + 无油 + 内置 VFD**：v1.3 厂家移除独立外配变频器（新时达 AS）整项电气清单 → V5 §3 / §14 品牌合规度显著提升。
4. **电气系统 100% Siemens / Danfoss / Schneider 接受品牌**：v1.3 升级链条（Schneider PLC → Siemens；三花 EEV → Danfoss；压力传感器 AKS 3000 高/低压拆分）完成 §14 整体合规。
5. **R513A 制冷剂**：A1 类 / GWP ~573（远低于 R134a 1430 / R407C 1774 / R410A 2088）/ EU / US / UAE / TH 法规允许，环保性能良好。

### 4.3 关键缺口与风险

| 风险 | 严重性 | 影响 | 缓解方向 |
|------|------|------|--------|
| Q24 UAE 46°C COP 缺数据 | 🟥 P0 | UAE 站点选型阻塞 | 厂家提供实测或仿真 COP + 四档曲线 |
| Q31 CE / UL / PED 认证缺失 | 🟥 P0 | 入库硬约束 + Compliance 评审硬条件 | 厂家提供完整证书复印件 + 覆盖型号声明 |
| Q41 FWS 主泵 2N 拓扑未明 | 🟧 P1 | 单点故障风险 / 系统可用性指标受影响 | 厂家书面确认是否内置 2 台 + 切换逻辑 + 附件 |
| Q42 漂移联动响应缺数据 | 🟧 P1 | V5 §9 锁定的 ±2°C 漂移 4 层联动 → CDU 漂移 → GPU 降载链路无法闭环验证 | 厂家提供控制器响应表 + 5 min 漂移曲线 + BMS 信号清单 |
| Q43 出厂测试缺报告 | 🟧 P1 | FWS ±0.5°C / 漂移恢复 ≤ 5 min / FC 切换 ≤ 3 min 无法工厂验收 | 厂家在 FAT 中追加该 3 项 + 第三方报告 |
| Q33 Bray 旁通阀品牌非 V5 §5 接受 | 🟧 P1 | 品牌合规但规格匹配（DN200）| 书面说明替代理由 或 切换 Belimo / Siemens / Honeywell |
| Q35 V 型干冷器规格未明（翅片 / 涂层）| 🟧 P1 | UAE 盐雾环境长期可靠性风险 | 厂家提供翅片 / 管材 / 涂层规格 + ISO 9227 盐雾 ≥ 1000h 报告 |
| R513A 未列于 V5 §4 主表 | 🟧 文件口径 | 不构成阻塞 — A1 类合规延续 V1.6 §5.4 归档版 | 厂家在交付文件中明示 6 站点（Astana 移出后 5 站点）法规适用清单 |
| Astana 已移出 | ✅ Closed | TICA 不适配 −55°C；改用替代方案（仅适用 Kemi −43°C 主流站点）| — |

### 4.4 商务建议（非定价）

1. **不建议在 Q24 / Q31 闭环前进入正式报价阶段**（Hard Rule #1：FOG 不输出价格；本建议针对评估流程时序）。
2. 建议在下一轮厂家联络中合并 A8 / A9 行动项（Q41–Q44 + R513A 法规清单 + Q33 / Q35 跟进），减少邮件来回次数。
3. 3rd Party List 增补流程可在 P0 闭环后并行启动（Risk 评审 / Compliance 评审可在等待厂家回复期间提前展开 Risk 维度评估）。
4. 6 站点全年能耗模型（Q13）建议在 P0 闭环后立即跟进 — 是 BD 比价 / TCO 测算的关键输入。
