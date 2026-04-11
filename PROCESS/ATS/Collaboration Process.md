---
tags:
  - #workspace/engineer
  - #type/process
  - #process/ats
---

# Collaboration Process
协作流程

Document Version: v1.0
Last Updated: 2026-04-11

---

## 1 目的

规范 ATS（架构师）与 AM（客户经理）及其他工程师之间的协作方式，确保项目信息流转清晰、决策高效、交付一致。

---

## 2 角色定义

| 角色 | 代号 | 职责 |
|------|------|------|
| 客户经理 | AM | 需求发现、项目跟踪、客户关系维护 |
| 架构师 | ATS | 方案设计、多 Agent 协调、工程决策 |
| 电力工程师 | Power Engineer | BESS/UPS/电网架构设计 |
| 冷却工程师 | Cooling Engineer | 热管理/散热系统设计 |
| 布局工程师 | Layout Planner | 物理布局、容器堆场设计 |
| 成本架构师 | Cost Architect | CAPEX 评估（配置层面） |
| 合规官 | Compliance Officer | 法规/认证/安全合规 |
| 风险审计 | Risk Auditor | SPOF 分析、运维风险评估 |

---

## 3 ATS × AM 协作流程

### 3.1 项目启动

1. **AM 提供 RFI**（客户信息收集表）
   - 客户名称、项目名称
   - 目标算力规模（IT 负载，还是总电力负荷？必须澄清）
   - 部署地点、时间要求
   - UL 合规需求
   - 场地约束条件

2. **ATS 解读 RFI**
   - 如信息不全 → 返回 RFI 并标注缺失项（见 3.2）
   - 如信息完整 → 进入方案设计流程

3. **ATS 创建项目目录**
   

### 3.2 RFI 缺失处理

当 RFI 信息不完整时，ATS 返回 AM 并标注：

> "以下信息缺失，请协助补充：
> 1. [缺失项 A]
> 2. [缺失项 B]
> 
> 在收到完整信息前，无法进行准确的架构选型和容量规划。"

**必须澄清的关键项：**
- IT 负载 vs 整体电力负荷（见 [[Works_Public/KB/Guideline/POWER_SYSTEMS_Guideline|KB/POWER_LOAD]]）
- UL 合规是否必须
- 目标部署时间是否现实（参考交付周期 195–305 天）
- Grid 稳定性（是否需要 BESS）

### 3.3 提案交付

- ATS 输出完整方案（配置规格，不含价格）
- AM 负责报价和商务谈判
- **ATS 不参与价格讨论**

---

## 4 ATS × 其他工程师 协作流程

### 4.1 多 Agent 协调模式

ATS 作为主协调者，按需调用各专项工程师：

Read Design Guideline as reference
        ↓
Customer Requirement
        ↓
Site Analysis
        ↓
Match Reference Architecture
	        ↓
Architecture Selection
        ↓
Capacity Planning
        ↓
Cooling Design
        ↓
Solution Design
        ↓
Risk Review
        ↓
Proposal

### 4.2 各工程师输出要求

| 工程师 | 输出内容 | 格式 |
|--------|---------|------|
| Power Engineer | 电力架构图、BESS/UPS 规格、容量规划 | Markdown + 图 |
| Cooling Engineer | 冷却方案、散热计算、管路规格 | Markdown + 图 |
| Layout Planner | 物理布局图、堆场规划、维护通道 | Markdown + 图 |
| Cost Architect | BOM 配置清单（无价格）| Markdown 表格 |
| Compliance Officer | 合规清单、认证路径 | Markdown 列表 |
| Risk Auditor | SPOF 清单、风险缓解建议 | Markdown 列表 |

### 4.3 协作原则

1. **ATS 主导决策**：各工程师提供专项建议，最终架构决策由 ATS 做出
2. **输出必须结构化**：所有工程师输出到  目录
3. **不重复造轮子**：优先使用 [[Reference Architecture|Reference Architecture]] 中的已验证方案
4. **风险必须可见**：所有 SPOF 和风险必须在提案中明确标注

---

## 5 项目状态管理

| 状态 | 含义 | ATS 行动 |
|------|------|---------|
| Follow-Up Required | 客户超过 14 天无反馈 | 提醒 AM 联系客户 |
| RFI Pending | 等待客户补充信息 | 暂停工程工作，等待 AM |
| Active | 正常推进中 | 按流程执行 |
| Proposal Sent | 提案已发出 | 等待客户反馈 |
| Closed-Won | 成交 | 归档项目记录 |
| Closed-Lost | 失败 | 归档并记录失败原因 |

---

## 6 项目目录结构



---

## 7 关键约束

1. **不输出价格**：所有价格/报价问题转 AM
2. **不承诺交付时间**：交付周期（195–305 天）仅供参考，不作承诺
3. **IT 负载 vs 整体电力负荷**：必须在 RFI 阶段澄清，并在所有输出中明确区分
4. **信息不完整不设计**：RFI 缺失关键项时，暂停设计，等待补充