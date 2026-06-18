---
title: §5–§6 RDHx + CRAH 物理/结构/尺寸锁定矩阵
parent: "[[../COOLING_DESIGN_v4_lockdown_plan]]"
order: 4
tags:
  - #workspace/engineer
  - #type/lockdown-plan
  - #cooling
  - #MDC
created: 2026-06-18
source_file: "KB/3RD-PARTY/COOLING/DESIGN/COOLING_DESIGN_v4_lockdown_plan.md"
source_anchors: []
---

## 5. RDHX Requirement — 物理/结构/尺寸锁定矩阵

### 5.1 ✅ 已可锁定（架构无关）

| Request # | 项 | 锁定值 | 来源 |
|---|---|---|---|
| RDHX-P-01 | 后门总宽 / 高 / 深 | 600 × 2230 × 160–180 mm | v1.0 §2 |
| RDHX-P-02 | 模块数 | 4 模块（纵向堆叠，10U 单模块）| v1.0 §2 |
| RDHX-P-03 | 后门开角度 | ≥ 120° | v1.0 §2 |
| RDHX-P-04 | 单门重量 | 70–90 kg | v1.0 §2 |
| RDHX-P-05 | 水侧接口位置 | 顶部歧管 | v1.0 §4 |
| RDHX-P-06 | 接口规格 | **DN25（1"）**，快插 | v1.0 §4 |
| RDHX-P-07 | 最大工作压力 | 10 bar | v1.0 §4 |
| RDHX-P-08 | 翅片材质 | 铝 3003/1100，厚度 0.25 mm，间距 6 mm | v1.0 §5 |
| RDHX-P-09 | 集管 / 歧管 | 铝 / 不锈钢（PG25 兼容证明）| v1.0 §6 |
| RDHX-P-10 | 框架 | 粉末涂层钢 | v1.0 §6 |
| RDHX-P-11 | 密封 | EPDM（PG25 兼容）| v1.0 §6 |
| RDHX-P-12 | 设计寿命 | ≥ 10 年 | v1.0 §7 |
| RDHX-P-13 | 泄漏率 | ≤ 10⁻⁶ mbar·L/s | v1.0 §7 |
| RDHX-P-14 | 运行环境温度 | 5–45°C；进风 5–60°C | v1.0 §7 |
| RDHX-P-15 | 最大面速度 / ΔP | 8 m/s / 200 Pa 单门 | v1.0 §9 |
| RDHX-P-16 | 水侧流速限制 | 1–3 m/s | v1.0 §9 |
| RDHX-P-17 | 数量 | 9（8 DLC + 1 风冷柜）| v1.0 §12 |

### 5.2 ⏸ 等 Reading 决定后再锁

| Request # | 项 | 影响 |
|---|---|---|
| RDHX-T-01 | TCS 进水温度 | A: 28°C · B/C: 22°C |
| RDHX-T-02 | 单门吸热（ε-NTU 实算）| 进水 22°C 时，ε=0.55 下 DLC 43.3°C 排气吸热从 21 kW（27°C 水）→ 约 **29 kW**，**吸热比例从 52% → ~71%** |
| RDHX-T-03 | 设计水 ΔT | 维持 8°C 或上调（取决于水温与 GPU 排气温度差）|
| RDHX-T-04 | 单门设计流量 | A: ~2.4 m³/h · B/C: ~3.2 m³/h（按 29 kW / ΔT 8°C / PG25）|
| RDHX-T-05 | 9 门合计流量 | A: ~21 m³/h · B/C: ~29 m³/h |
| RDHX-T-06 | 进风温度上限 | 仍存在 datasheet 40°C vs 实际 43.3°C 的 Q1 — **不受 Reading 影响，独立解决** |
| RDHX-T-07 | 介质 | 跟 CDU-T-04/05 |

---

## 6. CRAH Requirement — 物理/结构/尺寸锁定矩阵 + 选型存疑

> **CRAH 是 v4 最大的风险点**。当前 v1.1 锁定 STULZ OHS-084-DG-FC（自含式 DX，PG25 在冷凝侧），其能力受 TCS 温度强相关。若选 Reading B（22°C 直送），DX 路线可能被直冷水盘管（true CRAH）路线取代。

### 6.1 ✅ 已可锁定（架构无关，假设仍是 9 台顶置）

| Request # | 项 | 锁定值 | 来源 |
|---|---|---|---|
| CRAH-P-01 | 数量 | 9（顶置均匀分布）| v1.1 §2 |
| CRAH-P-02 | 冗余 | N（无 N+1，顶部空间饱和）| v1.1 §2 |
| CRAH-P-03 | 单台净重（CeilAir）| 250 kg | v1.1 §9 |
| CRAH-P-04 | 9 台顶置总载荷 | 2250 kg | v1.1 §9 / §11 Q5 |
| CRAH-P-05 | 安装方式 | 吊顶（4 点吊装）| v1.1 §9 |
| CRAH-P-06 | 维护通道 | 底面 ≥ 600 mm（开盖/抽芯）| v1.1 §9 |
| CRAH-P-07 | 振动隔离 | 弹簧/橡胶减震，传递率 ≤ 5% | v1.1 §9 |
| CRAH-P-08 | 防护等级 | IP41 / IP44（室内安装）| v1.1 §9 |
| CRAH-P-09 | 排水 | 蒸发器底盘 → 集装箱地面排水沟 | v1.1 §9 / §11 Q4 |
| CRAH-P-10 | 通信 | Modbus RTU/TCP；BACnet/IP 优先 | v1.1 §8 |
| CRAH-P-11 | 群控 | 9 台主从（轮询 / 负荷均分 / 故障切换）| v1.1 §8 |
| CRAH-P-12 | 不配 | 电再热 / 加湿器 / 蒸汽 / 热气 | v1.1 §7 |
| CRAH-P-13 | 风量（单台标称）| ≥ 5,690 m³/h @ 0.5 inH₂O ESP | v1.1 §4 |
| CRAH-P-14 | 9 台合计风量 | ≥ 51,200 m³/h | v1.1 §4 |
| CRAH-P-15 | 机柜进风目标 | 25–27°C（出风混合后）| v1.1 §4 |

### 6.2 ⏸ 选型大方向 — 等 Reading 决定

| Reading | CRAH 类型 | 候选产品 | 决策影响 |
|---|---|---|---|
| **A**（TCS 28°C）| 自含式 DX + EG/PG 冷凝（CeilAir 类）| 现状 STULZ OHS-084-DG-FC | 沿用 v1.1，存在 S-Max × 28°C 缺口 −7%，靠 GPU 降载兜底 |
| **B**（TCS 22°C 直送）| **直冷水盘管 CRAH（CW Coil only）** | STULZ CCD 系列 / Vertiv Liebert PCW / Schneider 同级 | **整份 CRAH_Requirement.md 重做**；取消压缩机、制冷剂、FC 阀组；增加水盘管面积 + 凝水排放 |
| **C**（TCS ≈ 23°C）| 同 B（CW Coil） | 同 B | 同 B，但盘管在 23°C 工况下显冷略低于 22°C |

### 6.3 Reading B/C 下 CRAH 估算（直冷水盘管）

若改为直冷水盘管 CRAH（22°C 进水，机房回风 32°C / 35% RH）：
- 显冷量典型 30–40 kW / 单台（4 排盘管，5690 m³/h）
- 9 台合计显冷 **270–360 kW** → 覆盖 S-Max @ 230 kW 余量 **+17–57%** ✅
- 单台冷凝液流量 **3.5–4.5 m³/h**（ΔT 8°C，PG25/EG）
- 9 台合计 **31–40 m³/h**（比 v1.1 的 48.7 m³/h 低 ~20%）
- 单台 ΔP 估算 25–40 kPa（无 DX 旁通，全部走盘管）
- 重量预估 180–220 kg / 台（无压缩机，比 CeilAir 轻 30+ kg）
- **CRAH-P-04 总载荷可下修至 ~1800 kg**

### 6.4 Reading B/C 触发的下游变化

| 项 | 影响 |
|---|---|
| 制冷剂 R-407C | **取消**（无压缩机）|
| Free Cooling 阀组 | **取消**（直冷水本身就是 FC）|
| UL/CE R-407C 充注合规 | **简化** |
| 压缩机功耗 ~58 kW | **取消** → 全年 PUE 改善 0.04–0.05 |
| Branch 3 PICV 量程 | 从 0–55 m³/h → 0–45 m³/h |
| 出风温度可达性 | 直冷水盘管出风 ~14–16°C（vs CeilAir DX 12–18°C）— 仍能保机柜进风 25–27°C |
