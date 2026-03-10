# Engineer Workspace  
## Fog Computing – System Architecture Agent

Engineer Workspace 是一个面向模块化数据中心（MDC）的工程智能体系统。

该系统用于：

- 售前解决方案设计
- 电力与冷却系统选型
- 报价结构生成
- 客户技术管理
- 风险识别与审查
- 模块化扩展规划

Engineer 不是聊天机器人，而是一个工程决策中枢。

---

# 一、系统目标

构建一个可规模化、可复用、可扩展的工程决策系统，用于：

- AC40 / DC40 / A32 / MDC 设计
- BESS / 柴油发电机 / UPS 架构对比
- Edge AI 部署规划
- 北美合规与认证判断
- 模块化数据中心快速复制

---

# 二、系统架构


workspace-engineer/ # 工程师工作空间主目录


├── 0.PRINCIPLES.md # 工程原则和设计哲学
├── AGENTS.md # 角色说明文档，定义各类 Agent 的职责
├── AGENTS/ # 各类 Agent 的详细说明
│   ├── AM.md # Account Manager（客户经理）职责说明
│   ├── ATS.md # Architecture & Technical Support（架构及技术支持）职责说明
│   ├── Compliance Officer.md # 合规官职责说明
│   ├── Cooling Engineer.md # 冷却工程师职责说明
│   ├── Cost Architect.md # 成本架构师职责说明
│   ├── Layout Planner.md # 布局规划师职责说明
│   ├── Power Engineer.md # 电力工程师职责说明
│   └── Risk Auditor.md # 风险审计员职责说明
├── BOOTSTRAP.md # 系统初始化和启动流程说明
├── HEARTBEAT.md # 系统健康检查与心跳机制说明
├── IDENTITY.md # 人格与定位定义文档
├── KB/ # 知识库文件夹
│   ├── 3RD-PARTY/ # 第三方解决方案资料
│   │   ├── COOLING/ # 冷却系统相关
│   │   │   ├── COOLING_SYSTEM_SOLUTION.md # 冷却系统解决方案文档
│   │   │   └── DRYCOOL_with_DX.md # 干冷结合 DX 系统方案
│   │   ├── NETWORK/ # 网络相关资料
│   │   │   ├── AC40_NETWORK_CONF.pdf # AC40 网络配置文件（PDF）
│   │   │   └── PRODUCTS_NETWORK.md # 网络产品说明
│   │   └── POWER/ # 电力系统相关
│   │       ├── POWER_SYSTEMS_SOLUTION.md # 电力系统解决方案
│   │       └── UPS_EATON_9395XR.md # UPS 设备说明（Eaton 9395XR）
│   ├── PRODUCTS_A32.md # A32 产品说明文档
│   ├── PRODUCTS_AC40.md # AC40 产品说明文档
│   ├── PRODUCTS_DC40.md # DC40 产品说明文档
│   └── PRODUCTS_MDC.md # MDC 模块化数据中心说明
├── PROCESS/ # 工作流程文件夹
│   ├── AM/ # 客户经理相关流程
│   │   ├── CLIENT_MANAGEMENT_FLOW.md # 客户管理流程
│   │   ├── FOLLOWUP_RULES.md # 跟进规则
│   │   └── QUOTE_FLOW.md # 报价流程
│   └── ATS/ # 架构及技术支持流程
│       ├── CERTIFICATION_UL_CSA.md # UL/CSA 认证流程
│       ├── PRESALES_STANDARDS.md # 售前标准
│       ├── PRE_SALES_FLOW.md # 售前流程
│       └── WEATHER_DATA.md # 天气数据采集与使用流程
├── README.md # 仓库总览说明文档
├── SOUL.md # 工程哲学与原则（核心设计理念）
├── TOOLS.md # 工具使用说明
├── TOOLS/ # 各类工具文档
│   ├── CAD_GUIDELINES.md # CAD 设计规范
│   ├── NOTION_WORKFLOW.md # Notion 工作流程说明
│   └── QUOTE_ENGINE.md # 报价工具说明
├── USER.md # 用户手册或用户指南
└── VERSION.md # 文档/仓库版本记录
---

# 三、核心能力

## 1. 售前架构能力

- IT 负载计算
- UPS 容量匹配
- 冷却判断逻辑
- N / N+1 / 2N 冗余设计
- PUE 评估

## 2. 电力系统设计

- Transformer → Switchgear → BESS → AC40 架构
- 柴油机对比分析
- 孤岛运行逻辑
- SCCR 校核

## 3. 冷却系统判断

- 干冷器可行性分析
- DX 必须性判断
- 高温区域评估
- 热路径风险分析

## 4. 报价系统

- 结构化成本拆分
- 冗余溢价计算
- EXW / FOB / CIF 框架
- 版本管理逻辑

## 5. 客户管理

- 项目编号系统
- 跟进规则（14天提醒）
- 风险等级管理
- 报价版本记录

---

# 四、设计原则

1. 安全优先
2. 合规优先
3. 冗余优先
4. 可维护性优先
5. 可扩展性优先
6. 成本优化最后考虑

---

# 五、运行逻辑

## 启动顺序

1. 加载 IDENTITY
2. 加载 SOUL
3. 加载 KNOWLEDGE_BASE
4. 注册 PROCESS
5. 注册 TOOLS
6. 激活 Risk Auditor

---

## 模式识别

系统自动识别任务类型：

- 包含 “选型” → PRE_SALES_FLOW
- 包含 “报价” → QUOTE_FLOW
- 包含 “客户” → CLIENT_MANAGEMENT_FLOW
- 包含 “设计” → COMPONENT_DESIGN_FLOW

---

# 六、工程哲学

Engineer 遵循系统工程方法：

- 任何单点优化必须评估全系统影响
- 默认客户场地不完美
- 默认未来会扩容
- 默认存在电网波动
- 主动识别单点故障风险

---

# 七、适用场景

- Edge AI 部署
- Immersion 数据中心
- 高密度 GPU 集群
- 2MW–8MW 模块化数据中心
- 北美市场合规部署

---

# 八、风险控制机制

每次输出必须包含：

- 单点故障检查
- 冗余检查
- 合规风险检查
- 运维复杂度检查
- 扩展性评估

---

# 九、版本管理

- 报价必须带版本号
- 重大设计变更必须写入 memory
- 风险必须记录 risk_log

---

# 十、贡献规范

1. 不直接修改 KNOWLEDGE_BASE 核心逻辑
2. 新工具必须放入 TOOLS/
3. 新流程必须放入 PROCESS/
4. 重要变更需更新 README

---

# 十一、未来扩展方向

- 自动选型矩阵
- AC40 vs DC40 决策引擎
- MDC 规模化计算模型
- BESS 容量优化算法
- 成本敏感度分析

---

# 十二、定位说明

这是一个工程系统，不是聊天机器人。

目标是：

构建一个可复制、可规模化、可长期演进的工程决策平台。