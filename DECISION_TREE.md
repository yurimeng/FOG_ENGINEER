# Engineering Architecture Decision Tree
工程架构决策树

Document Version: v1.0
Last Updated: 2026-03-10

---

**⚠️ 所有决策必须在 KB 定义的产品组合内（A32 / AC40 / DC45 / MDC）。不推荐 KB 外的产品。**

---

# 1 Purpose / 目的

EN

This document defines architectural decision rules for datacenter infrastructure design.

The decision tree helps ATS select appropriate technologies based on customer requirements, deployment constraints, and operational considerations.

CN

本文档定义数据中心基础设施架构的决策规则。

该决策树帮助 ATS 根据客户需求、部署环境和运维条件选择合适的技术方案。

---

# 2 Decision Hierarchy / 决策层级

Architecture decisions follow a hierarchical order:

架构决策遵循以下层级顺序：

1 Deployment Model
2 Compute Cooling Architecture
3 Power Architecture
4 Heat Rejection Strategy
5 Infrastructure Form Factor

---

# 3 Deployment Model Decision
部署模式决策

Decision Factors:

- Project scale
- Latency requirements
- Site availability

决策因素：

- 项目规模
- 延迟需求
- 场地条件

Decision Rules:

IF deployment is near users  
→ Edge deployment

IF deployment requires centralized training  
→ Centralized datacenter

IF site infrastructure is limited  
→ Containerized deployment

---

# 4 Compute Cooling Architecture
计算冷却架构决策

Primary Options:

Immersion Cooling  
Direct Liquid Cooling (DLC)

主要选项：

浸没式冷却  
直冷液冷

Decision Rules:

IF compute density > 80 kW per rack  
→ Prefer immersion cooling

IF GPU cluster uses OEM DLC servers  
→ Use DLC cooling

IF customer prioritizes lowest PUE  
→ Prefer immersion cooling

IF customer requires compatibility with standard servers  
→ Prefer DLC

---

# 5 Power Architecture Decision
电力架构决策

Primary Options:

Grid + UPS  
Grid + UPS + Generator  
Grid + UPS + BESS

主要选项：

电网 + UPS  
电网 + UPS + 柴油发电机  
电网 + UPS + 储能系统

Decision Rules:

IF site has unstable grid  
→ Add BESS

IF diesel generator is restricted  
→ Use BESS

IF project prioritizes fast deployment  
→ Prefer BESS over generator

IF long backup time required (>1 hour)  
→ Consider generator

Default Edge Strategy:

Grid + UPS + BESS

默认边缘架构：

电网 + UPS + 储能

---

# 6 Heat Rejection Strategy
散热方式决策

Primary Options:

Dry Cooler  
Cooling Tower  
DX Cooling  
Hybrid Cooling

主要选项：

干冷器  
冷却塔  
DX制冷  
混合方案

Decision Rules:

IF ambient temperature < 28°C  
→ Dry cooler preferred

IF water availability is high  
→ Cooling tower viable

IF ambient temperature extremely high  
→ Add DX support

IF noise restrictions exist  
→ Avoid large cooling towers

---

# 7 Infrastructure Form Factor
基础设施形式决策

Primary Options:

Traditional building  
Containerized datacenter  
Hybrid deployment

主要选项：

传统机房  
集装箱数据中心  
混合部署

Decision Rules:

IF deployment timeline < 90 days  
→ Containerized deployment

IF site infrastructure limited  
→ Containerized deployment

IF large-scale hyperscale campus  
→ Building datacenter

---

# 8 Energy Storage Strategy
储能策略

Primary Options:

No energy storage  
BESS for fault tolerance  
BESS for energy optimization

主要选项：

无储能  
储能用于容错  
储能用于能源优化

Decision Rules:

IF single grid connection  
→ Add BESS

IF grid curtailment exists  
→ Add BESS

IF diesel generator undesirable  
→ Replace with BESS

---

# 9 Redundancy Strategy
冗余策略

Primary Options:

N  
N+1  
2N

主要选项：

N  
N+1  
2N

Decision Rules:

IF mission critical compute  
→ N+1 minimum

IF hyperscale environment  
→ N+1

IF financial or trading systems  
→ 2N

Edge default:

N+1

---

# 10 Edge Datacenter Default Architecture
边缘数据中心默认架构

Compute

Immersion or DLC depending on server type

Power

Grid + UPS + BESS

Cooling

Dry cooler with optional DX

Infrastructure

Containerized modules

---

# 11 Engineering Philosophy Alignment
工程哲学

All decisions must align with the following principles:

所有架构决策必须符合以下原则：

- Modular design
- Minimal complexity
- Fast deployment
- Operational simplicity
- Scalable architecture

模块化设计  
避免过度复杂  
快速部署  
运维简单  
可扩展架构