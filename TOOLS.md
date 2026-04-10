---
tags:
  - #workspace/engineer
  - #type/tool
  - #system/feis
---

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

- 配置生成 → [[Proposal Generation Process|PROCESS/Proposal Generation Process]]
- CAD逻辑 → [[CAD_GUIDELINES|TOOLS/CAD_GUIDELINES]]
- 客户管理 → [[NOTION_WORKFLOW|TOOLS/NOTION_WORKFLOW]]
- ⚠️ 报价生成 → **仅供 AM（商务团队）使用，Engineering Agent 禁止访问 [[QUOTE_ENGINE|TOOLS/QUOTE_ENGINE]]**

---

## 2. 配置输出规范（Engineering Agent 使用）

调用：

[[Proposal Generation Process|PROCESS/Proposal Generation Process]]

**⚠️ Engineering Agent 禁止访问 [[QUOTE_ENGINE|TOOLS/QUOTE_ENGINE]]（仅供商务团队）。**

输出必须包括：

- 项目名称
- 地点
- **产品型号与数量**（A32 / AC40 / AC45 / DC45）
- **IT 负载（kW）**
- **整体电力负荷（kW）**
- PUE 参考范围
- 冗余结构（N / N+1 / 2N）
- 冷却方案（Immersion / DLC + **Hybrid Cooling System**）
- 交付周期

**禁止输出：价格、成本、报价。**


---

## 3. CAD输出规范

调用：

[[CAD_GUIDELINES|TOOLS/CAD_GUIDELINES]]

输出必须包括：

- 布局逻辑说明
- 设备相对位置
- 维护通道说明
- 冷却路径说明
- 电力路径说明

---

## 4. 客户管理规范

调用：

[[NOTION_WORKFLOW|TOOLS/NOTION_WORKFLOW]]

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

[[AM|AGENTS/AM]]（Section 3.6 Project Follow-up Monitoring）


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

[[Projects/[项目名]/Project_Record.md|Projects/Project_Record]]

- 客户创建
- **新配置版本**（不是报价）
- 新设计决策
- 重大风险

---

## 8. Obsidian CLI — 项目管理强制规则

**⚠️ 所有项目文档操作必须通过 Obsidian CLI 执行。禁止直接读写文件。**

### 项目文档路径

```
Works_Public/Projects/
└── [项目名称]/
    └── Project_Record.md        ← 项目主文档
Works_Public/Projects/INDEX.md   ← 项目索引
```

### 必须使用 Obsidian CLI
- **读取**：获取项目状态、查看必填字段
- **写入**：更新进度、添加沟通记录、设计方案

### 禁止直接访问
```
❌ Read/Write/Edit 工具直接访问项目文档
❌ 项目文档存放在 Works_Public/Projects/ 以外的任何位置
```

### Obsidian CLI 命令
```bash
# 读取
obsidian-cli run --task read --note "Works_Public/Projects/[项目名]/Project_Record.md"
obsidian-cli run --task read --note "Works_Public/Projects/INDEX.md"

# 写入
obsidian-cli run --task update --note "Works_Public/Projects/[项目名]/Project_Record.md"
obsidian-cli run --task update --note "Works_Public/Projects/INDEX.md"
```

### 同步规则
每次更新项目文档后，**必须**同步更新 [[Projects/INDEX.md]]

### 相关 Agent
- [[AGENTS/AM]] — AM 负责项目文档创建和进度更新
- [[AGENTS/ATS]] — ATS 负责方案设计和选型结果记录
