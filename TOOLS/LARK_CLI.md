---
tags:
  - #workspace/engineer
  - #type/tool
  - #system/feis
  - #external/lark-cli
  - #MDC
---
# LARK_CLI.md — 飞书 CLI 工具注册

## 基本信息

| 项目 | 值 |
|------|-----|
| 名称 | lark (飞书 CLI) |
| 版本 | v1.0.12 |
| 安装路径 | `/usr/local/bin/lark` |
| 平台 | macOS ARM64 (Apple Silicon) |
| 官方仓库 | github.com/larksuite/cli |

## 用途

- 飞书/ Lark 平台管理（消息、文档、表格、日历、邮件、任务等）
- 支持 200+ 命令和 20+ AI Agent Skills
- 支持 AI Agent 集成

## 常用命令

```bash
# 认证登录
lark auth login

# 查看版本
lark --version

# 获取帮助
lark --help

# 查看支持的模块
lark list
```

## 认证状态

- **未认证** — 首次使用需要 `lark auth login`

## 注册信息

- 注册时间：2026-04-16
- 安装方式：GitHub Releases 直接下载 (`lark-cli-1.0.12-darwin-arm64.tar.gz`)