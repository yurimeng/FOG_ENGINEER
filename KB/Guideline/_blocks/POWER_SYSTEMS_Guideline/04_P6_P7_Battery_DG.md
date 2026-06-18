---
title: §P-6 UPS 电池技术 + §P-7 柴油发电机选型
parent: "[[../POWER_SYSTEMS_Guideline]]"
order: 4
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/power
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/POWER_SYSTEMS_Guideline.md"
source_anchors: []
---

## P-6 UPS 电池技术对比 (UPS Battery Technology)

| 技术 | 特点 | 适用 |
|------|------|------|
| VRLA（阀控式铅酸）| 成本低、寿命短 | 极少使用 |
| **Li-ion（磷酸铁锂，LiFePO4）** | 高循环寿命、安全、能量密度高 | **标配（EATON 93LiG2）** |
| 超级电容 | 响应 / 切换时间 <1ms，容量极小 | 特殊场景，不作为主备电 |

> 储能合规要求见 [[Compliance_Guideline#C-3 储能系统合规]]。

---

## P-7 柴油发电机选型 (Diesel Generator Selection)

### 柴油发电机（DG）的核心优势

| 特性 | 说明 |
|------|------|
| 启动时间 | 10–15 秒 |
| 技术成熟度 | 100 年以上 |
| 功率密度 | 非常高 |
| 成本 | 最低的单位 kW 成本 |
| 适用性 | 长时间断电（>6 小时）的场景 |

### 柴油发电机（DG）的常见顾虑

客户对柴油发电机通常有 4 类顾虑：

| 顾虑 | 具体问题 |
|------|---------|
| **环保与许可** | EPA Tier 4 排放标准、NOx、颗粒物；Air Permit 审批复杂 |
| **燃料供应** | 需维持 24–72 小时燃料储备；极端天气（暴风雪、洪水）下供应链中断风险 |
| **维护成本** | 定期测试运行；燃料长期储存变质；启动失败风险 |
| **ESG / 碳排放** | 高碳排设备；与 AI 公司 Net Zero 和 ESG 指标冲突 |

### DG 选型规则

- **Standby rating**：备用工况额定（短期用）
- **Prime rating**：连续工况额定（长期用）
- **NFPA 110 Level 1**：关键负载的合规等级，必须满足
