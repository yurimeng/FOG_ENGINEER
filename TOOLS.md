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

- 配置生成 → ./PROCESS/ATS/Proposal Generation Process.md
- CAD逻辑 → ./TOOLS/CAD_GUIDELINES.md
- 客户管理 → ./TOOLS/NOTION_WORKFLOW.md
- ⚠️ 报价生成 → **仅供 AM（商务团队）使用，Engineering Agent 禁止访问 ./TOOLS/QUOTE_ENGINE.md**

---

## 2. 配置输出规范（Engineering Agent 使用）

调用：

./PROCESS/ATS/Proposal Generation Process.md

**⚠️ Engineering Agent 禁止访问 ./TOOLS/QUOTE_ENGINE.md（仅供商务团队）。**

输出必须包括：

- 项目名称
- 地点
- **产品型号与数量**（A32 / AC40 / DC45）
- **IT 负载（kW）**
- **整体电力负荷（kW）**
- PUE 参考范围
- 冗余结构（N / N+1 / 2N）
- 冷却方案（Immersion / DLC + Dry Cooler + DX）
- 交付周期

**禁止输出：价格、成本、报价。**


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
- **配置版本**（不是报价版本）
- 风险标记
- 下次跟进时间

---

## 5. 自动提醒规则

跟进提醒规则由 AM 负责，具体逻辑参见：

./AGENTS/AM.md（Section 3.6 Project Follow-up Monitoring）


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

./Projects/[项目名]/Project_Record.md

- 客户创建
- **新配置版本**（不是报价）
- 新设计决策
- 重大风险
