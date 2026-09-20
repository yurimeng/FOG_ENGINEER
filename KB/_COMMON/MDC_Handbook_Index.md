---
ttags:
  - #MDC
---
# MDC Engineering Handbook — Index

> **Audience:** 工程师 + AI。
>
> 本文档是 [[MDC Engineering Handbook]] 的主题索引。
> 原 Handbook 是一篇完整的叙事性论证文档（WHY → HOW → WHAT），包含所有细节内容。
> 本索引用于快速定位和交叉导航，不替代原文档阅读。

---

## Handbook 导航

### §1 行业问题与驱动力（Industry Problem）

分析为什么传统数据中心无法满足 AI Factory 时代的算力需求。

| 章节 | 主题 | 核心结论 |
|------|------|---------|
| §1.1 | 算力产业从矿场转向 AI Factory | GPU 功率密度 80–150kW/rack，远超空气冷却能力 |
| §1.2 | AI Factory 对基础设施的要求 | 高速网络、高可靠性供电、高效率冷却 |
| §1.3 | 传统 Hyperscale 建设周期过长 | 12–24 个月，建设速度 < 算力需求增长速度 |
| §1.4 | 大量矿场基础设施寻求转型 | 矿场 → AI 需要重构冷却/电力/网络 |
| §1.5 | 需要新的部署模式 | 高密度 + 快速部署 + 灵活扩展 + 降低资本风险 |
| §1.6 | 从数据中心到算力工厂 | 算力基础设施必须可工业化复制 |
| §1.7 | MDC 作为 AI Factory 基础设施 | 模块化设计 → 可快速复制的工业化算力模块 |

**结论：** 传统模式不行，需要新的基础设施范式。

---

### §2 MDC 设计理念（Philosophy）

阐述 MDC 的六个核心设计原则。

| 章节 | 主题 | 核心结论 |
|------|------|---------|
| §2.1 | 产品化（Infrastructure as Product）| 标准化生产 + 工厂预集成 + 75–90 天部署 |
| §2.2 | 模块化架构（Modular Architecture）| 计算/冷却/电力/网络解耦，线性扩展 |
| §2.3 | 快速部署（Rapid Deployment）| 工厂完成集成，现场仅做接入 |
| §2.4 | 高密度算力支持（High Density Compute）| 原生支持 80–150kW/rack，液冷优先 |
| §2.5 | 最小化场地依赖（Site Agnostic）| 只需电力/冷却/网络三个外部接入条件 |
| §2.6 | 按需扩展（Demand Driven Scaling）| 模块化扩展 vs 预建设模式，降低资本风险 |
| §2.7 | 面向 AI Factory 的算力基础设施 | 算力模块 = 工业生产线上的生产单元 |

**结论：** MDC 是产品化基础设施，而非工程项目。

---

### §3 系统设计原则（System Design Principles）

定义架构设计的基本工程原则。

| 章节 | 主题 | 核心结论 |
|------|------|---------|
| §3.1 | 全球环境适应性 | 统一高温水架构（28–35°C）+ 混合制冷策略（Free Cooling / Hybrid / Mechanical）|
| §3.2 | 能源效率优先 | Immersion PUE ~1.04 / DLC PUE ~1.15–1.22 |
| §3.2.1 | 最大化液冷比例 | φ_air 控制在 8–27% |
| §3.2.2 | 提高水温运行 | 26–32°C 冷却水，Dry Cooler 可直接散热 |
| §3.3 | 面向 AI 工作负载的可靠性 | 按工作负载类型（Training/Inference）差异化设计 |
| §3.4 | 标准化交付 | 工厂预集成 + 标准接口 + 模块化运维 |
| §3.5 | 计算平台选型 | PCIe+Immersion vs SXM+DLC 对比及选型建议 |
| §3.6 | 混合算力架构 | AC40 + DC45 同园区混合部署 ^mdc-9d3bd10c74 |

**结论：** 设计原则必须适配 AI 工作负载特征和全球气候环境。

**关联文档：**
- [[COOLING_SYSTEM_Guideline|KB/Guideline/COOLING_SYSTEM_Guideline]]
- [[RA-001_Immersion_0.4MW|Reference Architecture/EDGE_INFERENCE_IMMERSION_0.4MW]]

---

### §4 系统架构（System Architecture）

三大域（Compute / Cooling / Power）的工程实现细节。

| 章节 | 主题 | 核心结论 |
|------|------|---------|
| §4.1 | 总体架构原则 | 算力独立 / 分层容错 / 能量缓冲优先 |
| §4.2 | 计算系统架构 | AC40（PCIe+Immersion）/ DC45（SXM+DLC）详细设计 ^mdc-dc33e84e04 |
| §4.3 | 冷却系统架构 | 冷却冗余分层模型 / 分层控制逻辑 / 热路径设计原则 |
| §4.4 | 电力系统架构 | 单路 / 双路 / Tier III 实现 / 电力调度优先级 |
| §4.5 | 认证与标准体系 | UL / CE / IEC / NFPA / Uptime Tier III 适用场景 |
| §4.6 | 架构总结 | 三大域独立演化，通过标准接口解耦 |

**结论：** 三域架构 + 分层容错实现整体可靠性。

**关联文档：**
- [[L1240C45 Power System Criteria|KB/LIQUID/L1240C45/DESIGN/L1240C45 Power System Criteria]] ^mdc-48b50a5c23
- [[L1240C45 Hydronic & Thermal Design Criteria|KB/LIQUID/L1240C45/DESIGN/L1240C45 Hydronic & Thermal Design Criteria]] ^mdc-15b3e17a79
- [[L1240C45 Compliance Checklist UL CE Fire|KB/LIQUID/L1240C45/DESIGN/L1240C45 Compliance Checklist UL CE Fire]] ^mdc-d7fac48938
- [[RA-002_Liquid_1.2MW|Reference Architecture/EDGE_INFERENCE_DLC_1.2MW]]

---

### §5 部署架构（Deployment Architecture）

从单模块到 AI Factory 园区的扩展路径。

| 章节 | 主题 | 核心结论 |
|------|------|---------|
| §5.1 | 部署层级 | Infrastructure → Module → ACC → AI Factory Campus |
| §5.2 | 单模块部署 | 最小可部署单元，三个外部接入条件即可运行 |
| §5.3 | ACC 园区部署 | 共享冷却/电力，模块级 UPS 不共享 |
| §5.4 | 扩展路径 | 线性增量扩展，电力主接入按最终规模预留 |
| §5.5 | 混合算力园区 | AC40 + DC45 同园区，共享冷却站 ^mdc-681f41e13c |
| §5.6 | 运维控制架构 | BMS → DCIM → 算力调度三层分离 |

**结论：** 以模块为原子单元，以 ACC 为标准园区单元，线性扩展。

**关联文档：**
- [[L1240C45_Thermal_Assessment_6Sites|KB/LIQUID/L1240C45/DESIGN/L1240C45_Thermal_Assessment_6Sites]] ^mdc-c96dde96d9

---

### §6 工程设计原则（Doctrine）

用"为什么选择 X 而不是 Y"的格式，解释 MDC 的核心工程决策逻辑。

| 章节 | 决策 | 核心理由 |
|------|------|---------|
| §6.1 | 产品化 vs 项目化 | GPU 供应链数周 vs 数据中心建设 12–24 个月；算力无法上线 = 沉没资本 |
| §6.2 | 模块解耦 vs 整体集成 | GPU 每 1–2 年换代，解耦使 Compute 域独立演化不影响 Cooling/Power |
| §6.3 | 差异化冗余 vs 全系统 2N | AI 训练可重启，成本高；冗余目的是支持维护，不是掩盖低可靠性 |
| §6.4 | 高温水冷 vs 低温冷冻水 | 28–35°C 即可满足 DLC/Immersion，Dry Cooler 大多数气候下无需机械制冷 |
| §6.5 | BESS vs 柴油发电机 | BESS 运维成本低 + 可削峰填谷平滑 GPU 波动 + 与 UPS 协同形成完整电力防线 |
| §6.6 | 75–90 天部署周期 | 工厂预集成 + 标准化接口 + 最小化现场施工 |
| §6.7 | Doctrine 执行机制 | 判断标准 → 工程约束 → 执行检查表 |

**结论：** 每个决策都有明确的因果链和工程约束，不可随意变更。

---

### §7 产品快速参考（Product Quick Reference）

三大产品平台对比。

**关联文档：**
- [[MDC_Product_Quick_Ref|KB/LIQUID/L1240C45/DESIGN/MDC_Product_Quick_Ref]]（详细对比表） ^mdc-bd22c1a9b8
- [[I400C40|KB/IMMERSION/PRODUCTS_I400C40]] ^mdc-1f765e899a
- [[I400C45|KB/IMMERSION/PRODUCTS_I400C45]] ^mdc-528f4cfbf5
- [[L1240C45_Tech_Spec_EN|KB/LIQUID/L1240C45/PRODUCTS/L1240C45 Tech Spec EN]] ^mdc-513608c422

---

### §8 研发标准条款（Engineering Standards）

**关联文档：**
- [[MDC_Standards_Compilation|KB/_COMMON/MDC_Standards_Compilation]]（完整标准条款）

---

## 文档关系图

```
MDC Engineering Handbook（索引入口）
├── [[MDC Engineering Handbook|原文档完整阅读]]（叙事性论证）
│
├── §1–6 核心内容（不分拆，保持 WHY→HOW→WHAT 论证链）
│
├── §7 产品快速参考 → [[MDC_Product_Quick_Ref]]
│     ├── [[I400C40]] ^mdc-6af340ffa5
│     ├── [[I400C45]] ^mdc-4420b0a90c
│     └── [[L1240C45_Tech_Spec_EN]]
│
└── §8 研发标准 → [[MDC_Standards_Compilation]]
      ├── [[L1240C45 Power System Criteria]] ^mdc-8efe0fa200
      ├── [[L1240C45 Hydronic & Thermal Design Criteria]] ^mdc-a1d5656bd2
      ├── [[L1240C45 Compliance Checklist UL CE Fire]] ^mdc-11761269f3
      └── [[L1240C45_Thermal_Assessment_6Sites]]

三大 Reference Architecture（案例验证）：
├── [[RA-002_Liquid_1.2MW]]
├── [[RA-001_Immersion_0.4MW]]
└── [[Site_Reference_Climate_Standard]]
```

---

## 阅读建议

| 目的 | 推荐路径 |
|------|---------|
| 快速选型判断 | §7 → [[MDC_Product_Quick_Ref]] |
| 理解 MDC 决策逻辑 | §6 Doctrine → §2 Philosophy → §1 Problem |
| 了解系统架构细节 | §4 Architecture + 关联专项设计文档 |
| 查询设计标准 | §8 → [[MDC_Standards_Compilation]] |
| 查询全球环境适配 | §3.1 + [[MDC/Reference Architecture/Site_Reference_Climate_Standard]] |

---

*Document Version: v1.0 | Last Updated: 2026-05-31*

---

## Update Log

| 日期 | 变更内容 |
|------|---------|
| 2026-05-31 | 创建索引文档，原 Handbook 保留不变 |