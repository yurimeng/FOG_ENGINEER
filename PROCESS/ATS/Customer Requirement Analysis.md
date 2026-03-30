---
tags:
  - #workspace/engineer
  - #type/process
  - #process/ats
---

# Customer Requirement Analysis Process
客户需求分析流程

Document Version: v1.0
Last Updated: 2026-03-10

---

## 1 Purpose / 目的

EN  
Transform customer requests into engineering parameters that can be used for solution design.

CN  
将客户需求转化为可用于工程设计的技术参数。

---

## 2 Scope / 适用范围

EN

This process applies to all presales infrastructure projects including:

- Edge datacenters
- AI training clusters
- AI inference clusters
- HPC deployments

CN

该流程适用于所有预售基础设施项目，包括：

- 边缘数据中心
- AI训练集群
- AI推理节点
- HPC部署

---

## 3 Inputs / 输入

Customer business requirements  
Target compute scale  
Deployment timeline  
Budget expectations  
Location information

客户业务需求  
目标算力规模  
部署时间  
预算范围  
部署地点

---

## 4 Process Steps / 流程步骤

Step 1  
Collect customer objectives.

Step 2  
Identify required compute capacity.

Step 3
**⚠️ CRITICAL: Estimate expected power demand. Clarify whether client means IT load or total facility load. Always output both.**

Step 4  
Identify deployment model.

Step 5  
Determine timeline and budget constraints.

---

## 5 Outputs / 输出

Estimated compute scale  
Estimated power requirement  
Deployment model  
Preliminary architecture direction

预计算力规模
**IT 负载**（计算设备实际消耗）
**整体电力负荷**（IT 负载 ÷ PUE，场地电力接入容量）
部署模式
初步架构方向

---

## 6 Key Decisions / 关键决策

Edge vs centralized deployment  
Container vs building  
Immersion vs DLC cooling

边缘部署还是集中部署  
容器式还是机房式  
浸没式还是DLC

---

## 7 Risks / 风险提示

Incomplete customer information
Unrealistic timeline expectations
Underestimated compute requirements
**Confusion between IT load and total facility load (must be clarified before proceeding)**

客户需求不完整  
时间要求不现实  
算力需求被低估