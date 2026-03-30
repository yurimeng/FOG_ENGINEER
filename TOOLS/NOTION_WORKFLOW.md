---
tags:
  - #workspace/engineer
  - #type/tool
  - #process/am
---

# Notion Client Management Workflow

## 1. 目标

为每个客户建立结构化档案。

---

## 2. 必须创建字段

Client Database 字段：

- Client Name（客户名称）
- Project ID（项目编号）
- Location（部署地点）
- IT Load（IT 负载，kW）
- Total Facility Load（整体电力负荷，kW）
- PUE（参考值）
- Cooling Type（冷却类型）
- Power Structure（电力架构）
- Redundancy Level（冗余等级）
- Configuration Version（配置版本）
- Status（状态）
- Risk Level（风险等级）
- Last Contact Date（最近联系日期）
- Next Action Date（下次跟进日期）

---

## 3. 状态定义

- Lead（潜在客户）
- Technical Discussion（技术交流中）
- **Solution Delivered（方案已交付）** ← 注：Engineering Agent 输出配置，AM 负责报价
- Negotiation（商务谈判中）
- Closed-Won（成交）
- Closed-Lost（未成交）

---

## 4. 配置版本规则

格式：

```
C-YYYY-ProjectCode-V1
C-YYYY-ProjectCode-V2
```

> 注："C" = Configuration（配置）。Engineering Agent 只负责配置版本管理，报价版本由 AM 在商务流程中管理。

---

## 5. 风险等级

Low
Medium
High

高风险条件：

- 客户无明确需求
- IT 负载 vs 整体电力负荷 未澄清
- 负载接近系统上限
- 场地未确认
- 合规未明确

---

## 6. 自动整理规则

每次：

- **新配置版本**交付（Engineering Agent）
- 重大设计变更
- 风险升级

必须更新 Notion。

---

## 7. AM vs Engineering Agent 分工

| 流程 | 负责方 |
|------|--------|
| 技术需求发现 | AM + ATS |
| 配置方案设计 | ATS + Engineering Specialists |
| **配置版本管理** | ATS |
| 商业报价生成 | AM（使用 QUOTE_ENGINE.md）|
| 报价版本管理 | AM |
| 项目跟进 | AM |
