
Obsidian CLI — 项目管理强制规则

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
- [[AGENTS/AM|AGENTS/AM]] — AM 负责项目文档创建和进度更新
- [[AGENTS/ATS|AGENTS/ATS]] — ATS 负责方案设计和选型结果记录