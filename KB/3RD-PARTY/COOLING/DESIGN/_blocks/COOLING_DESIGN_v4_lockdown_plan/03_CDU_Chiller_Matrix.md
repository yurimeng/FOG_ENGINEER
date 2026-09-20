---
title: §3–§4 CDU + Chiller 物理/结构/尺寸锁定矩阵
parent: "[[../COOLING_DESIGN_v4_lockdown_plan]]"
order: 3
tags:
  - #workspace/engineer
  - #type/lockdown-plan
  - #cooling
  - #MDC
created: 2026-06-18
source_file: "KB/3RD-PARTY/COOLING/DESIGN/COOLING_DESIGN_v4_lockdown_plan.md"
source_anchors: []
---

## 3. CDU Requirement — 物理/结构/尺寸锁定矩阵

> 当前版本 v3.0（本会话刚完）。下表标注哪些 Request 现状已锁、哪些需 Reading 决定。

### 3.1 ✅ 已可锁定（架构无关）

| Request # | 项 | 锁定值 | 来源 |
|---|---|---|---|
| CDU-P-01 | 接口数量 | 仅 4 个：P-IN / P-OUT / S-OUT / S-IN | v3.0 §3.1 |
| CDU-P-02 | P-IN/P-OUT 公称管径 | **DN100**（PN16 / Class 150）| v3.0 §3.2 |
| CDU-P-03 | S-OUT/S-IN 公称管径 | **DN100**（PN16 / Class 150）| v3.0 §3.2 |
| CDU-P-04 | 接口距地面高度 | 500–1200 mm | v3.0 §3.3 |
| CDU-P-05 | 进出水水平间距 | ≥ 400 mm 同侧 | v3.0 §3.3 |
| CDU-P-06 | 接口正前方维护空间 | ≥ 600 mm | v3.0 §3.3 |
| CDU-P-07 | CDU 占地 | ≤ 2.5 m (L) × ≤ 1.2 m (W)（DC45 IT zone 内）| v3.0 §10 ^mdc-d73c907692 |
| CDU-P-08 | CDU 维护通道 | 正面 ≥ 800 / 侧面 ≥ 600 / 顶部 ≥ 500 mm | v3.0 §10 |
| CDU-P-09 | 吊耳载荷 | 顶部 4 角，单点 ≥ 1500 kg | v3.0 §10 |
| CDU-P-10 | 安装方式 | DC45 集装箱内落地 + 减震支脚（隔振率 ≥ 90%）| v3.0 §10 ^mdc-1a47ffff50 |
| CDU-P-11 | 防腐等级 | 室内 C3 / 户外延伸接口段 C4-M | v3.0 §8 |
| CDU-P-12 | 噪音 | ≤ 75 dB(A) @ 1 m | v3.0 §8 |
| CDU-P-13 | 运行温度范围 | 5–45°C | v3.0 §8 |
| CDU-P-14 | 二次泵冗余 | 2N 或 N+1 | v3.0 §2.1 |
| CDU-P-15 | 二次泵驱动 | VFD（70%–100% 流量调节）| v3.0 §2.1 |
| CDU-P-16 | 设计寿命 | ≥ 10 年；MTBF ≥ 50,000 h | v3.0 §7 |
| CDU-P-17 | 控制器 | PLC + ≥ 7" 触屏（中英文）| v3.0 §6 |
| CDU-P-18 | 通信 | Modbus TCP / BACnet + 干接点告警 | v3.0 §6 |
| CDU-P-19 | 泄漏检测 | 盘底电导率传感器 + 排水 | v3.0 §10 |

### 3.2 ⏸ 等 Reading 决定后再锁

| Request # | 项 | 取决于 Reading |
|---|---|---|
| CDU-T-01 | 板换 LMTD / UA | A: ≥6°C / ≥250 kW/K · B: 取消板换 · C: ≤1°C / ≥1500 kW/K |
| CDU-T-02 | FWS 供回水温度 | A: 22/32°C · B: n/a（无 FWS）· C: 22/32°C |
| CDU-T-03 | TCS 供回水温度 | A: 28/38°C · B: 22/32°C（直接 = FWS）· C: 23/33°C |
| CDU-T-04 | 一次侧介质 | A/C: 站点 EG（25/40/55/60%）· B: 单一流体（待定）|
| CDU-T-05 | 二次侧介质 | A/C: PG25 · B: 单一流体（待定）|
| CDU-T-06 | 一次侧流量 | 依 Q / cp / ΔT 重算（Reading A/C 大致 ≥160 m³/h）|
| CDU-T-07 | 二次侧流量 | A/C: ≥175 m³/h · B: 同总流量 |
| CDU-T-08 | 二次侧扬程 | A/C: ≥220 kPa · B: 单泵需覆盖全环路 TDH（可能 ≥35 m H₂O）|

---

## 4. Hybrid Chiller Requirement — 物理/结构/尺寸锁定矩阵

### 4.1 ✅ 已可锁定（架构无关）

| Request # | 项 | 锁定值 | 来源 |
|---|---|---|---|
| CHILLER-P-01 | 整机重量（运行）| ≤ 15,000 kg | V1.5 §3 |
| CHILLER-P-02 | 外形 | 40/45ft ISO 集装箱框架 UH | V1.5 §3 |
| CHILLER-P-03 | 防护等级 | IP54（室外）| V1.5 §3 |
| CHILLER-P-04 | 噪音 | ≤ 75 dB(A) @ 1 m | V1.5 §3 |
| CHILLER-P-05 | 工作压力 | ≥ 10 bar | V1.5 §3 |
| CHILLER-P-06 | 设计寿命 | ≥ 15 年 | V1.5 §3 |
| CHILLER-P-07 | 压缩机冗余 | N+1，≤ 30 s 自动切换 | V1.5 §5.2 |
| CHILLER-P-08 | 压缩机品牌 | Copeland / Bitzer / Danfoss / Smardt / Turbocor / 同级一线 | V1.5 §5.3 |
| CHILLER-P-09 | 制冷剂 | R454B 优先；R32 可接受；R1234ze(E) for EU；禁 R22/R404A/R410A | V1.5 §5.4 |
| CHILLER-P-10 | 运行环境温度（全球基线）| −40°C ~ +50°C；Astana 扩展 −55°C | V1.5 §3 / 附录 A |
| CHILLER-P-11 | FWS 主泵冗余 | 2N + VFD | V1.5 §10 |
| CHILLER-P-12 | 干冷器 | 必配 | V1.5 §2 |
| CHILLER-P-13 | 旁通阀 | 必配（极寒兜底）| V1.5 §2 |
| CHILLER-P-14 | 湿膜 | 可选；UAE/Thailand 强烈推荐 | V1.5 §2 |
| CHILLER-P-15 | 加热模块 | Astana 强制 ≥60 kW；TX/Kemi 推荐 30 kW | V1.5 §3 / 附录 A |
| CHILLER-P-16 | 通信 | Modbus / BACnet + 干接点 | V1.5 §11 |
| CHILLER-P-17 | 各站点防腐 | Kemi/UAE C5-M；其余 C3；详 V1.5 附录 A | V1.5 |
| CHILLER-P-18 | 维护频次 | UAE/Thailand ≤6 个月 / 其余 ≤12 个月 | V1.5 §3 |

### 4.2 ⏸ 等 Reading 决定后再锁

| Request # | 项 | 影响 |
|---|---|---|
| CHILLER-T-01 | 额定制冷量 | A/C: ≥1600 kW（基本不动）· B: 重算（可能 ≥1700 kW 含支路损耗）|
| CHILLER-T-02 | CHW 供水温度 | A/C: **22°C**（v1.5 旧值 26–28 弃用）· B: **22°C**（同）|
| CHILLER-T-03 | CHW 回水温度 | A/C: 32°C · B: 32–38°C（按 ΔT 与支路决定）|
| CHILLER-T-04 | CHW 流量 | A/C: ≥160 m³/h（保持）· B: 全环路单泵流量 ≥175 m³/h |
| CHILLER-T-05 | 干冷器散热基线 | ≥1700 kW（全 Reading 不变）但**自由冷却阈值显著下移**（22°C 出水 → free-cool 限制 T_amb ≤ ~17°C 而非 ~23°C）|
| CHILLER-T-06 | 全年 PUE / COP | 全部 6 站点重算（free-cool 小时数下降 + L2/L3 小时数上升）|
| CHILLER-T-07 | 介质 | A/C: 站点 EG · B: 单一介质（含机房） |
| CHILLER-T-08 | UAE 46°C COP | ≥2.8 → 重算（出水 22°C 比 26°C 更难达成，COP 可能跌至 2.3）|
