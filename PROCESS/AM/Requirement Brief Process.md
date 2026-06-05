---
tags:
  - #workspace/engineer
  - #type/process
  - #process/am
  - #MDC
---
# Requirement Brief Process (需求摘要生成流程)

## 1. Purpose / 目的
将碎片化的【客户需求记录】提炼为标准化的结构化文档，作为 ATS (方案设计) 的唯一输入源。

## 2. Trigger / 触发条件
- `Customer Discovery Process` 完成并输出 **Customer Requirement Notes**。

## 3. Inputs / 输入
- 先检查./Projects下有没有对应的项目, 没有则创建项目文件夹.
- 如果有的话检查是否有RFI, 有的话则利用, 否则则询问
- 客户需求记录 (Customer Discovery Notes)

## 4. Processing Logic / 处理逻辑
*AI 在生成 Brief 时应遵循以下转换原则：*
- **去噪**：删除会议记录中的寒暄和无关信息。
- **结构化**：将散落在笔记各处的碎片信息归类到对应的模板项下。
- **补全**：检查是否有缺失项（如缺失电力需求），并在输出中标记为 `[待确认]`。

## 5. Standard Output Template / 标准输出模板
*请严格按照以下格式输出：*

### 📋 Customer Profile
- **Customer Name:** [客户名称]
- **Industry:** [所属行业]
- **Location:** [部署地点]

### 🚀 Compute Requirements
- **GPU Type:** [具体型号/要求]
- **Cluster Size:** [集群规模/节点数]
- **Interconnect:** [互联要求，如 InfiniBand/RoCE]

### ⚡ Infrastructure
- **Power Availability:** [可用电力/单机柜功率]
- **Cooling:** [散热方式/要求]
- **Deployment Mode:** [物理机 / 容器 / 混合]

### 📅 Project Timeline
- **Target Go-Live:** [预计上线日期]
- **Key Milestones:** [关键节点]

### 💰 Budget Range
- **Estimated Budget:** [预算区间]
- **Budget Status:** [已审批 / 申请中 / 待定]

## 6. Outputs / 输出
- **Final Customer Requirement Brief (标准需求摘要)** $\rightarrow$ 交付给 $\rightarrow$ 方案设计团队 (ATS)。

---

*Document Version: v1.1 | Last Updated: 2026-04-12*
