---
tags:
  - #workspace/engineer
  - #type/general
  - #product/general
---

# KB_ACCESS.md — Obsidian CLI 操作规范

> 本文件定义 FEIS 系统访问 Obsidian Vault 的标准命令集。
> 所有 Agent 必须通过 `obsidian-cli` 访问 Vault，禁止直接文件读写。

---

## 强制规则

| 规则 | 说明 |
|------|------|
| **命令唯一性** | 必须使用 `obsidian-cli`，禁止 `obsidian`、`obsidianmd` 等 |
| **路径基准** | 所有路径为 **相对路径**，以工作空间根目录为基准 |
| **禁止直接读写** | 禁止使用 `open()`、`write()`、`cat` 等直接访问 vault 文件 |

---

## 命令速查

| 操作 | 命令 | 示例 |
|------|------|------|
| 浏览目录 | `obsidian-cli list <相对路径>` | `obsidian-cli list Works_Public/KB` |
| 读取文件 | `obsidian-cli print "相对路径/文件名"` | `obsidian-cli print "Works_Public/KB/PRODUCTS_A32.md"` |
| 模糊搜索 | `obsidian-cli search "关键词"` | `obsidian-cli search "AC45"` |
| 内容搜索 | `obsidian-cli search-content "关键词"` | `obsidian-cli search-content "BESS"` |
| 打开笔记 | `obsidian-cli open "相对路径/文件名"` | `obsidian-cli open "Works_Public/AGENTS.md"` |
| 创建笔记 | `obsidian-cli create -c "内容"` | `obsidian-cli create -c "# Title"` |
| 每日笔记 | `obsidian-cli daily` | `obsidian-cli daily` |

---

## 路径规范

```
正确：相对路径，以工作空间根目录为基准
   Works_Public/KB/PRODUCTS_A32.md
   Works_Confidential/ResourcePool/备件清单.md

错误：以 vault 根目录为基准
   YurimengKB/Works_Public/KB/PRODUCTS_A32.md

错误：绝对路径
   /Users/yuri/YurimengKB/Works_Public/KB/PRODUCTS_A32.md
```

---

## 工作空间速查

| 工作空间 | 路径 | 敏感级别 |
|---------|------|---------|
| 公开 | `Works_Public/` | 公开 |
| 机密 | `Works_Confidential/` | 机密 |
| 日记 | `Diaries/` | 私人 |
| 个人信息 | `Personal/` | 私人 |
| 模板 | `Template/` | 通用 |

---

## 已知限制

- `obsidian-cli list` 对空目录返回空字符串，无法区分"目录不存在"和"目录为空"
- 读取超过约 100K 字符的文件会被截断
- `obsidian-cli create -c` 参数为字符串，不接受管道输入

---

## 典型工作流

**问答流程（必须严格执行）：**

1. 定位 — 读取「知识库索引.md」，确定知识领域
2. 搜索 — `obsidian-cli search` / `obsidian-cli search-content` 匹配笔记
3. 阅读 — `obsidian-cli print` 读取 1-3 篇相关笔记
4. 整合 — 结合私有知识与通用能力，给出精准回答
5. 引用 — 回答末尾注明参考了哪些笔记

**创建新笔记：**

```
obsidian-cli create -c "# 笔记标题"
```

**搜索关键词：**

```
obsidian-cli search "关键词"           # 文件名搜索
obsidian-cli search-content "关键词"   # 文件内容搜索
```

---

---

*Document Version: v1.1 | Last Updated: 2026-04-12*
