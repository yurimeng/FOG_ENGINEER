---
tags:
  - #workspace/engineer
  - #type/process
  - #process/am
---
---
tags:
  - #workspace/engineer
  - #type/process
  - #process/am
---

# Customer Discovery Process (客户需求发现流程)

## 1. Purpose / 目的
深度挖掘客户的真实痛点、技术约束和业务期望，为生成 `Requirement Brief` 提供完整数据支持。

## 2. Trigger / 触发条件
- `Lead Qualification Process` 输出为 **Qualified Opportunity**。

## 3. Inputs / 输入
- 已筛选的项目机会 (Qualified Opportunity)
- 客户初次会议笔记 (Initial Meeting Notes)

## 4. Execution Steps / 执行步骤
- **Step 1: 业务目标深挖** $\rightarrow$ 通过访谈确认客户希望通过该项目解决的具体业务问题。
- **Step 2: 算力需求量化** $\rightarrow$ 确认 GPU 类型、数量、显存需求、互联要求。
- **Step 3: 部署环境勘察** $\rightarrow$ 确认机房位置、电力供应、散热条件、网络带宽。
- **Step 4: 时间轴对齐** $\rightarrow$ 确认关键里程碑（如：招标日期 $\rightarrow$ 到货日期 $\rightarrow$ 上线日期）。
- **Step 5: 预算范围确认** $\rightarrow$ 确认预算上限或预期的成本区间。

## 5. AI-Guided Key Questions / AI 引导问题 (访谈话术)
*当 AI 辅助调研时，请使用以下逻辑提问：*
- **关于算力：** "为了确保方案匹配，您目前预计需要的总算力规模是多少？是否有特定的 GPU 型号要求？"
- **关于部署：** "在部署地点方面，机房目前的电力承载能力能否满足高性能计算的需求？是否接受容器化部署？"
- **关于时间：** "该项目理想的上线时间点是什么时候？是否有不可逾越的截止日期？"
- **关于预算：** "对于本项目，贵司是否有预设的预算区间，以便我们提供最匹配的配置方案？"

## 6. Outputs / 输出
- **Customer Requirement Notes (客户需求详细记录)** $\rightarrow$ 触发 $\rightarrow$ `Requirement Brief Process`

---

*Document Version: v1.1 | Last Updated: 2026-04-12*
