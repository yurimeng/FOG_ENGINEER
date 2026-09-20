---
title: "DC45 三支路 Rev 11 — 冷板 Manifold 校核 + 附录 + Changelog"
parent: "[[../L1240C45 三支路冷却重评估 2026-05-21]]"
order: 8
tags:
  - #workspace/engineer
  - #type/engineering-summary
  - #product/DC45
  - #cooling
  - #thermal
  - #archive
  - #MDC
created: 2026-06-18
source_file: "KB/LIQUID/L1240C45/_archive/L1240C45 三支路冷却重评估 2026-05-21.md"
source_anchors: []
---

## 7. Cold Plate Manifold 选型校核（Rev 10）

> **校核任务**：用户给定的冷板分配 manifold 规格是否满足 DC45 单 rack 的 163–206 L/min 流量需求。 ^mdc-bc6d3b145b

### 7.1 用户给定 Manifold 参数

| 参数 | 数值 |
|------|------|
| 分支数 / 单 manifold | **20–50** |
| 单分支流量 | **1–3 L/min** |
| 不平衡率 | **≤ 10%** |
| 假设用途 | rack 内冷板分配（CDU 二次 → rack manifold → 各 GPU/CPU 冷板） |

**单 manifold 流量容量包络**：
- 下限：20 × 1 = 20 L/min
- **上限：50 × 3 = 150 L/min**

### 7.2 DC45 单 rack 流量需求 (PG25, ΔT 10K) ^mdc-2a1f40e38c

来自 §6.6 φ_air 全场景扫描：

| φ_air | 单 rack 液冷负荷 | 单 rack 流量需求 |
|-------|----------------|-----------------|
| 8% (CDU 护栏) | 138 kW | **206 L/min** ← 最高 |
| 10% | 135 kW | 201 L/min |
| 15% | 127.5 kW | 190 L/min |
| 20% | 120 kW | 179 L/min |
| 27% (S-Max) | 109.5 kW | **163 L/min** |

### 7.3 Manifold 数量推导 — 单台 manifold/rack 不够

**单 manifold 上限 150 L/min** vs **单 rack 需求 163–206 L/min**：

| 场景 | 需求 | 单 manifold (50/3) | 利用率 | 结论 |
|------|------|-------------------|--------|------|
| S-Max (φ_air=27%) | 163 L/min | 150 L/min | **109%** | ❌ 略不足 |
| 设计上限 (φ_air=8%) | 206 L/min | 150 L/min | **137%** | ❌ 显著不足 |

**结论：每 rack 必须 ≥ 2 个 manifold**。

### 7.4 双 manifold/rack 配置校核

每 rack 2 个 manifold 总容量 = 2 × 150 = **300 L/min**

| 场景 | 需求 | 双 manifold 容量 | 利用率 | 每分支实际流量 (假设 2×50=100 分支) | 结论 |
|------|------|-----------------|--------|----------------------------------|------|
| S-Max (φ_air=27%) | 163 L/min | 300 L/min | 54% | **1.63 L/min** ✅ 在 1–3 范围 | ✅ |
| φ_air=15% | 190 L/min | 300 L/min | 63% | 1.90 L/min ✅ | ✅ |
| φ_air=10% | 201 L/min | 300 L/min | 67% | 2.01 L/min ✅ | ✅ |
| **φ_air=8% (上限)** | 206 L/min | 300 L/min | 69% | **2.06 L/min** ✅ | ✅ |
| RDHX 单台失效 | 206 L/min | 300 L/min | 69% | 2.06 L/min ✅ | ✅ |

✅ **双 manifold 配置覆盖 φ_air ∈ [8%, 27%] 全场景**，每分支流量稳定在 **1.6–2.1 L/min**（1–3 区间中位）。

### 7.5 三 manifold/rack 配置（如 GPU 数量 > 100/rack）

如 rack 内冷板数量 > 100（如 NVL72 + 完整 CPU + NIC 冷板 ~ 108+ 个），单 manifold 50 分支不足，需 **3 manifold × ~36 分支** 每 rack：

| 场景 | 需求 | 三 manifold 容量 (450 L/min) | 每分支实际 (108 分支) |
|------|------|---------------------------|---------------------|
| S-Max | 163 L/min | 36% | 1.51 L/min |
| **φ_air=8%** | 206 L/min | 46% | **1.91 L/min** |

✅ 也满足要求；分支数留更多余量。

### 7.6 ≤ 10% 不平衡率影响评估

#### 7.6.1 单 manifold 内 ≤ 10% 不平衡

不平衡率 ≤ 10% 意味单分支流量可在标称值 ± 5% 范围波动（典型定义）：
- 标称 2.0 L/min → 实际 1.9–2.1 L/min（±5%）
- 标称 1.6 L/min → 实际 1.52–1.68 L/min（±5%）

**对 GPU 冷板热影响**：
- 流量 ±5% → 冷板 ΔT 反向变化 ~ ±5%（Q = m·cp·ΔT，Q 固定下 m 与 ΔT 反向）
- GPU 设计 ΔT 通常 10–15K，± 5% = ± 0.5–0.75K → **可接受**
- 不会触发 GPU 温度保护（典型阈值 +10K vs 设计点）

✅ ≤ 10% 不平衡率 **对 DLC 系统是工程可接受值**。

#### 7.6.2 双 manifold 之间的平衡

两个 manifold 在 rack 入口的 ΔP 需匹配，否则一台抢流量、另一台流量不足：
- 推荐**主动平衡**：每 manifold 入口装 PICV（压差独立流量阀），各设定 1/2 总流量
- 或**对称布置**：双 manifold 走相同长度/路径的 supply / return 管，自然平衡

**风险**：如双 manifold 简单并联无控制，长度不一时流量分配可能偏差 10–20%（实际 manifold 间不平衡可能超 ≤ 10% 单 manifold 内规格）。建议加入分支流量计 + 报警。

### 7.7 综合校核结论

| 校核项 | 结果 |
|--------|------|
| Manifold 选型容量（单台 150 L/min）| ✅ 数学合理（每 rack 2–3 台） |
| 分支数 20–50 | ✅ 兼容典型 GPU 平台（NVL72-class ~ 108 冷板）|
| 单分支流量 1–3 L/min | ✅ 落在 1.5–2.1 L/min 实际工作点（与 GPU 冷板典型 1–2 L/min 设计一致）|
| ≤ 10% 不平衡 | ✅ DLC 系统工程可接受 |

**Rev 10 锁定建议**：

| 项 | 建议 |
|----|------|
| **manifold 数量/rack** | **2 个**（若 rack 内冷板 ≤ 100）/ **3 个**（若冷板 > 100）|
| **每 rack 总分支数** | **80–150**（取决于服务器平台）|
| **每分支设计流量** | **1.6–2.1 L/min**（在 1–3 L/min 规格内有 30%+ 余量）|
| **双 manifold 间平衡** | 每 manifold 入口装 **PICV** + 流量计；推荐对称布置主管 |
| **manifold 间最大允差** | 总不平衡（含 manifold 间 + manifold 内）≤ **15%**（含 ≤ 10% 单 manifold + ≤ 5% 间隙）|
| **总 manifold 数量 (DC45 整机)** | **16–24 个**（8 rack × 2-3 manifold/rack） ^mdc-b4056370ad |

### 7.8 与上游 CDU 二次侧的接口

CDU 二次侧 → 8 rack 的总管 → 每 rack 进入 2-3 个 manifold：

- CDU 二次主管：DN50–DN65（PG25, 175 m³/h 总流量）
- rack 入口分支管：DN25–DN32（25 m³/h/rack ≈ 200 L/min @ PG25）
- 双 manifold 间分配：rack 入口分流到两个 DN20 → manifold 主管
- manifold 出口分支：每分支 ~ 1/4"–3/8" 软管 + 快接

---

## 附录 A — 计算依据

### A.1 RDHX 吸热模型

设单柜后门风量 V (m³/h)、风热 Q_air (kW)：

```
m_air·cp_air = V / 3600 × 1.2 × 1.005  (kW/K)
ΔT_rack = Q_air / (m_air·cp_air)          ← 服务器进出温差
T_rear = T_intake + ΔT_rack                ← RDHX 入风温度
```

RDHX 80% 吸热目标下：
```
Q_RDHX = 0.80 × Q_air
ΔT_RDHX = 0.80 × ΔT_rack
T_RDHX_out = 0.20 × T_rear + 0.80 × T_intake
```

DLC 柜 (φ_air=27%, V≈5500 m³/h, Q_air=40.5 kW, T_intake=26°C)：
- ΔT_rack ≈ 21.8°C ⇒ T_rear ≈ 47.8°C
- T_RDHX_out = 0.2×47.8 + 0.8×26 = **30.4°C** (回机房)

风冷柜 (Q_air=40 kW, V≈6000 m³/h)：
- ΔT_rack ≈ 19.9°C ⇒ T_rear ≈ 45.9°C
- T_RDHX_out = **30.0°C**

两类柜 RDHX 出风 ≈ **30°C**，混入机房后由 CeilAir 处理。

### A.2 CeilAir DX 工作原理（Rev 4 更正）

⚠️ Rev 1–3 的 LMTD 受限分析**仅适用于 CW coil**，对 OHS-084-DW 自含式 DX **不成立**。Rev 4 撤回该分析路径。

DX 单元工作原理（OHS-084-DW）：

```
房间空气 (~ 32–35°C, 50% RH)
        ↓
DX 蒸发器 (制冷剂蒸发温度 ~ 5–10°C)
        ↓ (空气被冷却 + 部分除湿)
出风 (~ 15–18°C, 标准 CRAC 出风)
        ↓
        ↓ 与机房空气混合
        ↓
机柜前进风 (~ 25–27°C，目标可保)

制冷剂回路 (高压侧):
压缩机出口 → 水冷冷凝器 (冷凝温度 ~ 35–38°C @ TCS 26–28°C)
                ↓
        冷凝水 (TCS 进水 27°C → 出水 32°C，ΔT_w ≈ 5°C)
```

**关键差异**：
- DX 蒸发温度 (~ 7°C) 决定空气侧能力，**与 TCS 水温无关**
- TCS 水温只影响冷凝侧 — 越冷越好（COP 上扬），越热则压缩机功耗上升
- 因此 25–27°C 进风目标在任何 TCS 水温下都可达

### A.3 OHS-084-DW datasheet 数值校核

实际工况下单台能力反推：

```
单台总排热 (datasheet) = 20.7 kW
压缩机输入功 = 3.4 kW
⇒ 单台冷却能力 (制冷量) = 20.7 − 3.4 = 17.3 kW
```

这与 datasheet 中"总冷量 47.9 kW @ 72/60"差异较大 — 印证 §3.2 中 ⚠️ 单位复核请求。**取保守值 17.3 kW/台为 BOM 兜底**：

- 8 台 × 17.3 = 138.4 kW > S-Max 127 kW ✅ 余量 9%
- 9 台 × 17.3 = 155.7 kW > S-Max 127 kW ✅ 余量 23%

**保守结论**：即使 datasheet 中 kW 数值有笔误、实际单台只有 17.3 kW，8 台仍能覆盖 S-Max（余量 9%），9 台 N+1 余量 23%。**8 台 N 仍是合理 BOM，9 台 N+1 提供 SPOF 防御**。

冷凝水流量校核：
```
Q_rej = ρ · cp · Q_water · ΔT_water
20.7 kW = 1000 × 4.186 × (1.88/3600) × ΔT
⇒ ΔT_water ≈ 9.5 K
```

实际 ΔT_water 9.5 K 比预设 5 K 大，意味 datasheet 默认水侧流量偏小（紧凑配置）。如客户需要降低 ΔT 改善 COP，可加大冷凝水流量至 ~ 3.6 m³/h/台（ΔT 5 K），8 台总 ~ 29 m³/h，但需 STULZ 确认水盘管阻力是否允许此流量上调。

### A.4 修订记录

- 2026-05-21 (Rev 1) — 初版（按 v1 基线：8 RDHX、DCD50 推荐、DG 模式推荐）。
- 2026-05-21 (Rev 2) — v2 修正后重做：
  - 9 × RDHX（含风冷柜）
  - RDHX 80% 吸热（视为上限）
  - CeilAir 纯 TCS 水冷（不带 DX）
  - 机柜进风 25–27°C 目标 → 标识 LMTD 物理边界
  - 推荐变更：**DCD35**（不再 DCD50）+ **OHS-084-DW**（不再 DG）
- 2026-05-21 (Rev 3) — 落实用户两项决策：
  - **Route A 锁定**：进风目标改至 ASHRAE A2 envelope (≤30°C)
  - **RDHX 80% 重定义**：稳态运行目标
  - §3.3–§3.4 重写为决策记录
  - §4 / §5 按 9× N+1 CeilAir 重算
- 2026-05-21 (Rev 4) — 接入 OHS-084-DW datasheet：
  - **重大澄清**：OHS-084-DW 是 **自含式 DX**（双 Scroll 压缩机 + 水冷冷凝器）
  - 撤回 Route A，进风目标恢复 25–27°C
  - §3.2–§3.4 / §4.3 / §4.4 / §5 全面重写
  - 临时结论：**8× DCD35 + 8× OHS-084-DW**（仅在 80% 吸热假设下闭环）
- 2026-05-21 (Rev 5) — 接入 DCD35/50 datasheet：
  - ε-NTU 物理校核显示 80% 吸热目标在 TCS 暖水 + 被动型条件下**物理不可达**（要求 ε ≥ 0.86）
  - 给出三条路线 X/Y/Z 供决策
  - **当前状态：BLOCKED 等 Yuri 决策**
- 2026-05-21 (Rev 6) — Yuri 给出四项关键 update：
  - 撤回 80% 硬约束 → ε-NTU 实算
  - 服务器排气 41–48°C 允许计算
  - CeilAir 改 OHS-084-DG，TCS 改 PG25
  - CeilAir 上限 9 台
  - **遗留问题**：STULZ datasheet 中 kW vs MBH 不自洽
- 2026-05-21 (Rev 7) — STULZ datasheet 确认；BOM 临界闭环
- 2026-05-21 (Rev 8) — 单 CDU 三支路架构校核，给定 1350/120/150 不闭环，给出三选一方案
- 2026-05-21 (Rev 9) — 方案 A φ_air 全场景扫描完成；CDU 上修至 1500/175/220
- 2026-05-21 (Rev 10) — 校核冷板 manifold：每 rack ≥ 2 个,每分支 1.6–2.1 L/min,PICV 防双 manifold 不平衡
- **2026-05-21 (Rev 11)** — 终版整理：新增 §0.5 执行摘要，对 Yuri 三个核心问题做直接回答：
  - **Q1 (φ_air 全场景能否工作)**：当前 CDU ❌；方案 A 升级后 ✅
  - **Q2 (是否流量不平衡)**：✅ 必然不平衡，三支路 K 差 1 个数量级 + 工况漂移
  - **Q3 (解决方案)**：四层联动 — CDU 升级 + PICV + 流量监测联动 GPU 降载 + 冷板 manifold 配置

---

> **遵循 CLAUDE.md**：本文档不含任何价格、报价或单价信息（Hard Rule #1）。所有引用产品 (VERTIV DCD35, STULZ OHS-084-DW, EATON 9395XR-1500) 均在 KB 或 3rd Party List 范围 (Hard Rule #2)。配置由 ATS 整合输出，价格由商务团队按确认配置单独核算。
