# FOG Workspace 工作区总结
**Fog Computing — Edge Datacenter Infrastructure Engineering System**
**用于：工作区迁移 / AI交接 / 对比评估**

> 📅 生成时间：2026-05-19
> 📅 最后更新：2026-05-20（v1.1 — 修正 §5 目录结构：移除 3RD-PARTY/BESS 下不存在的 Guideline 旧路径，补全 COOLING/NETWORK 实际文件）
> 📂 文档库路径：YurimengKB > FOG/
> 🔖 版本：v1.1

---

## 1. 工作区概述

**FOG Workspace** 是 Fog Computing 的模块化边缘数据中心工程知识库，由 Obsidian Vault（YurimengKB）驱动。

### 核心定位
- 专注：Modular Datacenter / Immersion Cooling / Edge AI Deployment
- 方法：Engineering Agent 协作系统（FEIS 架构）
- 原则：No pricing output（严禁输出任何价格数字）

### 关键约束（硬边界）
| 禁止行为 | 说明 |
|---------|------|
| 提供任何价格数字 | 严禁成本估算、报价或单价 |
| 推荐 KB 之外的产品 | 所有配置必须使用 KB 中定义的产品 |
| 向客户介绍竞品 | 不解释其他方案的优缺点 |
| 超出边缘数据中心范围 | 专注 MDC/边缘数据中心领域 |
| 提供金融或投资建议 | 严格限定在技术范围内 |

> 当客户询问价格时：
> *"配置方案由我提供，价格由我们的商务团队根据您确认的配置单独核算。请联系您的客户经理获取正式报价。"*

---

## 2. 产品体系

### 2.1 核心产品线

| 产品 | 类型 | IT 容量 | 冷却方式 | UPS | UL认证 | 定位 |
|------|------|---------|---------|-----|--------|------|
| **A32** | 单柜浸没槽 | 45–50kW | 单相浸没式 | 外置（客户自备） | ❌ | 最小单元 |
| **AC40** | 40ft 集装箱 | 400kW | 单相浸没式 | 外置（客户自备） | ❌ | 通用 AI 推理 |
| **AC45** | 45ft 集装箱 | 400kW | 单相浸没式 | 内置（专用电力舱） | ✅ | 北美合规 |
| **DC45** | 45ft 集装箱 | 1240kW（8×150kW DLC） | 直冷液冷 DLC | 内置 | ✅ | 超大算力集群 |

### 2.2 MDC（Modular Datacenter Cluster）架构

MDC 由三个 Zone 组成：

```
Transformer → Switchgear → [Power Zone: BESS / Generator]
                          ↓
                    [IT Zone: AC40 / AC45 / DC45]
                      ├── PDC → UPS → CDU → Tanks/Racks
                      ↓
              [Cooling Zone: Hybrid Cooling System（干冷器+DX一体化）]
```

| Zone | 名称 | 描述 |
|------|------|------|
| **IT Zone** | 算力单元区 | 服务器容纳和 UPS，由 AC40/AC45/DC45 组成 |
| **Cooling Zone** | 冷却单元区 | 外制冷，为 IT Zone 提供散热 |
| **Power Zone** | 电力单元区 | 后备电源，由 BESS 或柴发提供 |

### 2.3 PUE 设计参考

> ⚠️ 不写固定数字，根据环境温度浮动

| 产品 | 低温区（干冷优先）| 高温区（DX辅助）|
|------|----------------|----------------|
| AC40 | ~1.02–1.08 | ~1.15–1.20 |
| AC45 | ~1.02–1.08 | ~1.15–1.20 |
| DC45 | ~1.07–1.15 | ~1.25–1.35 |

### 2.4 IT Load vs Total Facility Load（重要区分）

**客户说"X MW 功率"时，必须澄清：**
- **IT Load**：服务器、GPU 实际消耗（客户通常指这个）
- **Total Facility Load**：IT Load + 冷却 + UPS损耗 + 照明 + 辅助系统

示例：DC45 IT Load 1240kW → Total Facility Load ~1390–1670kW（取决于 PUE）

---

## 3. 第三方产品生态

### 引用规则（必须按顺序）
1. 查询 `3rd Party List.md`
2. 查询对应类别的 **Guideline**（设计原则）
3. 在子文件夹中查找合适的产品文档

### 3.1 Cooling Zone — 冷却系统

| 产品 | 供应商 | 适用 |
|------|--------|------|
| 干冷器 + DX 双冷源机组 | 泰铂 | AC40/DC45 标准配置 |
| 600kW 集成冷站 | 三河同飞 | 螺杆式，一体化热泵冷源 |

**架构类型速查：**

| 架构 | 压缩机 | 适用制冷量 |
|------|--------|-----------|
| DX 方案 | 涡旋式 | <300kW |
| 螺杆压缩机 | 螺杆式 | 300–600kW |
| 磁悬浮压缩机 | 磁悬浮 | 能效优先 |
| 热泵方案 | 热泵机组 | 极寒/精确温控 |

### 3.2 Power Zone — 电力系统

**UPS（IT Zone 标配）：**

| IT Zone | UPS型号 | 总功率 | UPS放置 | 电池后备 |
|---------|---------|--------|---------|----------|
| AC40 | EATON 9395XR-600 | 600kW | 外置（客户自备）| ~10分钟 |
| AC45 | EATON 9395XR-600 | 600kW | 内置，UL合规 | ~20分钟 |
| DC45 | EATON 9395XR-1500 | 1500kW | 内置，UL合规 | ~8分钟 |

> ⚠️ UPS型号数字 = 总功率（kW），非 kVA
> ⚠️ UPS电池（93LiG2）≠ BESS：UPS电池是分钟级，BESS是小时级

**BESS 储能：**

| 品牌/型号 | 类型 | 适用场景 |
|----------|------|----------|
| TESLA Megapack 2 XL | 大型储能集装箱级 | 城市边缘 / 高ESG |
| 国轩 ESC480-125P261-UL | 工商业储能一体机 | 成本优化 / 国产方案 |

### 3.3 网络产品

| 类别 | 供应商 | 说明 |
|------|--------|------|
| 布线系统 | 引澜 | 结构化布线，商用成熟产品 |
| AC40 网络配置 | 参考配置 | 端口定义及布线规范 |

### 3.4 制造与组装

| 供应商 | 能力 | 备注 |
|--------|------|------|
| 三河同飞 | 冷却设备制造 | 参考供应商 |
| DSBJ（东山精密）| 制造 | 参考供应商 |
| 广东惠集 | 集装箱箱体制造 | 只做箱体，其他件客供，不做总集成 |
| 惟远能源 | 标准件供应 | 只做标准件，不定制 |

> ⚠️ 广东惠集和惟远能源有明确业务边界，方案设计时不得超出其能力范围

---

## 4. Agent 组织架构

### 4.1 协作流程

```
Client
  │
  ▼
AM（客户经理） ──需求结构化──▶ ATS（架构技术销售）
                                    │
                          Specialist Delegation
                                    │
                         ┌──────────┼──────────┐
                         ▼          ▼          ▼
               Power Engineer  Cooling   Layout Planner
               Cost Architect  Engineer
                         │          │          │
               Compliance Officer     Risk Auditor
                         │          │
                         └────┬─────┘
                              ▼
                        ATS（整合输出）
                              │
                              ▼
                           Client
```

### 4.2 核心角色

| Agent | 职责 | 硬边界 |
|-------|------|--------|
| **AM** | 客户关系、需求发现、项目跟踪 | 不设计技术系统 |
| **ATS** | 技术架构、专家协调、方案整合 | 不输出价格 |
| **Power Engineer** | 电力与储能系统设计 | — |
| **Cooling Engineer** | 热管理系统设计 | — |
| **Layout Planner** | 物理基础设施布局 | — |
| **Cost Architect** | CAPEX 评估 | 不输出价格 |
| **Compliance Officer** | 监管合规、认证审查 | 可否决不合规设计 |
| **Risk Auditor** | 风险分析、SPOF 检测 | 可建议重新设计 |
| **Market Researcher** | 市场情报、内容输出 | — |

---

## 5. 文档目录结构

```
FOG/
├── AGENTS.md                    # Agent 组织架构定义
├── VERSION.md                   # 版本历史
│
├── KB/                          # 知识库（产品+第三方+指南）
│   ├── index.md                 # KB 总索引
│   │
│   ├── FOG A Series/            # AC40/AC45/A32 产品文档
│   │   ├── PRODUCTS_AC40.md
│   │   ├── PRODUCTS_AC45.md
│   │   └── PRODUCTS_A32.md
│   │
│   ├── FOG D Series/            # DC45 产品文档
│   │   ├── PRODUCTS_DC45.md
│   │   ├── DC45 Tech Spec CN.md
│   │   ├── DC45 Tech Spec EN.md
│   │   ├── DC45 Quick Tech Spec.md
│   │   └── DC45 Layout/         # 布局图（SVG）
│   │
│   ├── BOM/                     # 物料清单
│   │   └── DC45_MDC_BOM.md
│   │
│   ├── Guideline/               # 设计原则（Guideline）
│   │   ├── COOLING_SYSTEM_Guideline.md
│   │   ├── POWER_SYSTEMS_Guideline.md
│   │   ├── Layout_Guideline.md
│   │   ├── Risk_Guideline.md
│   │   ├── Compliance_Guideline.md
│   │   ├── Cost_Guideline.md
│   │   └── Marketing_Guideline.md
│   │
│   ├── 3RD-PARTY/              # 第三方产品
│   │   ├── 3rd Party List.md    # ⚠️ 必须首先查阅
│   │   ├── BESS/
│   │   │   ├── TESLA MEGAPACK 2 XL.md
│   │   │   └── Gotion ESC480-125P261-UL.md
│   │   ├── UPS/
│   │   │   └── Eaton/
│   │   │       └── UPS_EATON_9395XR.md
│   │   ├── COOLING/
│   │   │   ├── Hybrid Cooler 600kW - 同飞.md
│   │   │   ├── DRYCOOL_with_DX.md
│   │   │   └── Hybrid Chiller Requirement 技术规格需求书.md
│   │   ├── Busbar/
│   │   │   └── Siemens/
│   │   └── NETWORK/
│   │       ├── PRODUCTS_NETWORK.md
│   │       └── AC40_NETWORK_CONF.md
│   │
│   ├── attachments/             # 附件（图片等）
│   ├── MDC Power Flow.png
│   ├── DC45 Racks.png
│   └── KB_Relation.canvas
│
├── PROCESS/                     # 工作流程
│   ├── index.md
│   ├── AM/                      # AM 流程
│   │   ├── Customer Discovery Process.md
│   │   ├── Lead Qualification Process.md
│   │   ├── Requirement Brief Process.md
│   │   └── ATS Handoff Process.md
│   └── ATS/                     # ATS 流程
│       ├── Proposal Generation Process.md
│       ├── Requirement Analysis.md
│       ├── Collaboration Process.md
│       └── index.md
│
├── Projects/                    # 项目目录
│   ├── project_list.md          # ⚠️ 项目总览（唯一数据源）
│   ├── 外发资料_最新/            # 外发文档（MSA草稿等）
│   │   ├── MSA Draft CN.md
│   │   ├── MSA Draft EN.md
│   │   ├── DC45 Tech Spec CN.md
│   │   └── DC45 Tech Spec EN.md
│   └── [客户项目]/
│       ├── Project_Record.md    # 项目主记录
│       └── Site Info/           # 现场信息
│
└── Reference Architecture/       # 参考架构
    ├── Proposal_Canvas_Template.canvas
    ├── EDGE_INFERENCE_DLC_1.2MW.md
    └── EDGE_INFERENCE_IMMERSION_0.4MW.md
```

---

## 6. 关键工作流程

### 6.1 项目阶段流转

```
Lead → Qualification → Technical Discussion → NDA → TS → QUOTE → Contract → Pay → Closed-Won/Lost
```

### 6.2 提案生成前置条件

| 输入 | 来源 | 状态检查 |
|------|------|---------|
| 客户需求（RFI）| AM | 必须完整 |
| 架构选型 | ATS | 已确定 |
| 容量规划 | ATS + Power Engineer | IT 负载和总负荷已澄清 |
| 冷却设计 | Cooling Engineer | Hybrid Cooling System 已确定 |
| 布局设计 | Layout Planner | 物理布置已确定 |
| 合规清单 | Compliance Officer | UL/CE 等认证路径已确认 |
| 风险清单 | Risk Auditor | SPOF 已识别 |

### 6.3 关键澄清项（提案前必须澄清）

- IT 负载 vs 整体电力负荷
- UL 合规要求（影响选型：AC40 vs AC45）
- 目标交付时间（参考周期 185-230 天）
- Grid 稳定性（影响 BESS 配置）

### 6.4 付款条件（参考）

| 里程碑 | 比例 |
|--------|------|
| 合同签署 | 60% 预付款 |
| 交付（FOB）| 30% |
| 安装调测 | 10% |

---

## 7. 项目总览

### 活跃项目（截至 2026-05-12）

| 项目 | 客户 | 阶段 | 产品 | IT Load | 地点 |
|------|------|------|------|---------|------|
| BILT_Finland_70MW | BILT | Technical Discussion | DC45 / 模块化 | 20MW Q4 + 50MW Q1 | 芬兰 |
| Phoenix_Global | Phoenix Global | Qualification | DC45 | 267MW | Abu Dhabi / Oman |
| Logy_Computer | Logy Computer | Lead | DC45 | TBD | 哈萨克斯坦 |
| 8th_Power | 8th Power | 募资中 | AC40 + RTX PRO 6000S | 500kW | 美国 |
| PQTech | PQTech | Technical Discussion | AC40 | ~1.6MW | 上海浦东 |
| Simple_Mining | Simple Mining | Technical Discussion | DC45 Pair | TBD | Iowa, USA |

### 待跟进项目

| 项目 | 状态 |
|------|------|
| Clutch_40MW | 项目记录缺失 |
| RiCloud | 项目记录缺失 |
| BTCT | 项目记录缺失 |
| 自建算力项目 | 项目记录缺失 |

> 📌 Lark Projects Token: `NwVqf0ozvlZ7lTdI9wmc1bJnnje`

---

## 8. 外发资料规范

| 规范 | 说明 |
|------|------|
| 命名 | `DC45 Tech Spec EN.md` / `DC45 Tech Spec CN.md`（中英文成对） |
| 路径 | `FOG/Projects/外发资料_最新/` |
| 版本管理 | 每次修改同步中英文，递增版本号 |
| INDEX | `外发资料_最新/index.md` 是唯一数据源 |

---

## 9. 常用工具与访问方式

### Obsidian Vault 访问
- **Vault 名**：YurimengKB
- **路径**：`~/Library/Mobile Documents/iCloud~md~obsidian/Documents/YurimengKB`
- **访问方式**：obsidian-cli（必须用 `obsidian` 命令，非 `obsidian-cli`）

### Lark 访问
- **Token**：`lark-cli --token EuezfrGInlXZwcd21ZZcomnHnJd`
- **Docs Token**：`QgFdddyXmoNIU7xLAOycXH4insc`（项目总览）

### 部署周期参考
- 现场勘测：~15天
- 商务准备：~15天
- 生产制造：~90-120天
- 运输：~45-60天
- 部署安装：~10-20天
- **参考总周期：~185–230天**

---

## 10. 迁移交接检查清单

### 新 AI 必须了解
- [ ] No pricing rule（绝对规则，无例外）
- [ ] IT Load vs Total Facility Load 区分
- [ ] 所有产品文档在 KB 中的位置
- [ ] 第三方产品引用顺序（3rd Party List → Guideline → 产品）
- [ ] Agent 协作流程（AM → ATS → Specialists → ATS整合）
- [ ] 项目总览在 Lark 和本地同步方式
- [ ] 外发资料的命名和版本规范

### 禁止事项
- [ ] 不得输出任何价格数字（区间、估算均禁止）
- [ ] 不得引入 3rd Party List 以外的产品
- [ ] 不得在未经确认情况下修改 Obsidian 文件

---

*Summary generated: 2026-05-19 | Last updated: 2026-05-20 (v1.1)*
*For AI handover and comparison purposes*
