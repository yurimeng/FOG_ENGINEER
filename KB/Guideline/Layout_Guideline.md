---
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/layout
  - #MDC
---
# Layout Guideline / 布局规划技术指南

> **执行摘要**:本 Guideline 定义 Layout Planner 在容器与机架布局、维护通道净空、线缆敷设、维护可达性、扩展规划及浸没/DLC 专项布局上的设计原则与约束。总体设计原则与跨 Agent 工作流详见 [[PRINCIPLE_Guideline]]。

## 文档导航

| 块 | 主题 | 包含章节 |
|----|------|---------|
| [[_blocks/Layout_Guideline/01_L1_L2_Principles_Clearance]] | L-1/L-2 核心布局原则与维护通道净空 | L-1, L-2 |
| [[_blocks/Layout_Guideline/02_L3_L4_Cables_Access]] | L-3/L-4 线缆敷设与维护可达性 | L-3, L-4 |
| [[_blocks/Layout_Guideline/03_L5_Expansion]] | L-5 扩展规划 | L-5 |
| [[_blocks/Layout_Guideline/04_L6_Container_Rack]] | L-6 容器与机架布局 | L-6 |
| [[_blocks/Layout_Guideline/05_L7_Workflow]] | L-7 工作流集成 | L-7 |

---

## 1. 核心布局原则与维护通道净空
![[_blocks/Layout_Guideline/01_L1_L2_Principles_Clearance]]

## 2. 线缆敷设与维护可达性
![[_blocks/Layout_Guideline/02_L3_L4_Cables_Access]]

## 3. 扩展规划
![[_blocks/Layout_Guideline/03_L5_Expansion]]

## 4. 容器与机架布局
![[_blocks/Layout_Guideline/04_L6_Container_Rack]]

## 5. 工作流集成
![[_blocks/Layout_Guideline/05_L7_Workflow]]

---

## Changelog

### v1.3 — 2026-06-17
- 结构拆分。原 7 个 H2 章节拆分为 5 个独立块文件,存放于 `_blocks/Layout_Guideline/`。保留全部 L-1 ~ L-7 章节 ID 与交叉引用。frontmatter 不变。

### v1.2 — 2026-06-05
- 章节 ID 与 [[PRINCIPLE_Guideline#§8 章节 ID 一致性表]] 对齐:所有章节增加 L-1 ~ L-7 前缀。
- 新增「速查 / Quick Reference」与「章节速查 / Section Index」表。
- 将原「Container Infrastructure Layout」「Rack Layout Strategy」「Immersion Tank Placement」「DLC Rack Layout」四节合并为 §L-6《容器与机架布局》,保留全部原始表格与内容。
- 章节标题统一为「§L-X 中文标题 / English Title」格式。
- 新增跨 Guideline 引用:Compliance §C-5、NETWORK §N-2、Risk §R-5/§R-7、COOLING §G-8、POWER §P-2。
- 文件末尾新增 Changelog 区块(按 CLAUDE.md §6 规则)。

### v1.1 — 2026-04-12
- 初版结构调整。

### v1.0 — 2026-03-10
- 初稿,源自 `Works_Public/AGENTS/Layout Planner.md`。
