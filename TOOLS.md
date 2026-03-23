# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.


# Tools Dispatcher

Engineer 不直接生成最终结构化文档。

必须：

1. 识别任务类型
2. 调用对应 PROCESS
3. 再调用对应 TOOLS
4. 最终统一输出结构

优先级：

KNOWLEDGE_BASE > PROCESS > TOOLS > Memory


## 1. 工具读取规则

当需要结构化输出时，必须读取对应工具文件：

- 报价生成 → ./TOOLS/QUOTE_ENGINE.md
- CAD逻辑 → ./TOOLS/CAD_GUIDELINES.md
- 客户管理 → ./TOOLS/NOTION_WORKFLOW.md
- 跟进规则 → ./TOOLS/FOLLOWUP_RULES.md

---

## 2. 报价输出规范

调用：

./TOOLS/QUOTE_ENGINE.md

输出必须包括：

- 项目名称
- 地点
- 配置
- 冗余结构
- 冷却方案
- 交付周期
- EXW
- FOB
- CIF

---

## 3. CAD输出规范

调用：

./TOOLS/CAD_GUIDELINES.md

输出必须包括：

- 布局逻辑说明
- 设备相对位置
- 维护通道说明
- 冷却路径说明
- 电力路径说明

---

## 4. 客户管理规范

调用：

./TOOLS/NOTION_WORKFLOW.md

创建：

- 客户编号
- 项目编号
- 技术需求摘要
- 报价版本
- 风险标记
- 下次跟进时间

---

## 5. 自动提醒规则

调用：

./TOOLS/FOLLOWUP_RULES.md

逻辑：

if last_contact > 14 days:
    提醒 Yuri

---

## 6. 知识冲突处理

若知识库冲突：

优先级：

1. KNOWLEDGE_BASE
2. PROCESS
3. TOOLS
4. Memory记录

---

## 7. Memory写入规则

必须写入：

./memory/

- 客户创建
- 新报价
- 新设计决策
- 重大风险