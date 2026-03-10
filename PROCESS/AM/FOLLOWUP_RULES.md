# Client Follow-Up Rules

## 1. 目标

避免客户丢失。
建立自动跟进机制。

---

## 2. 跟进逻辑

if days_since_last_contact > 14:
    标记 Follow-Up Required

if days_since_last_contact > 30:
    标记 Risk of Loss

if days_since_last_contact > 45:
    标记 Dormant Client

---

## 3. 优先级规则

优先跟进：

- 大于 500kW 项目
- 已发报价项目
- 进入技术评估阶段项目

---

## 4. 提醒输出格式

必须输出：

- 客户名称
- 项目编号
- 上次联系时间
- 当前状态
- 建议跟进方式

---

## 5. 写入Memory

写入：

/memory/client_followup_log.md

记录：

- 日期
- 客户
- 状态
- 建议行动