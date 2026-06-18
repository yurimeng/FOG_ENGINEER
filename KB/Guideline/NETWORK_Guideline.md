---
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/network
  - #MDC
---
# NETWORK SYSTEM Guideline / 网络系统设计 Guideline

> **执行摘要**:本文档为网络系统设计原则(Network System Design Guideline),定义网络架构选型、IB/ROCE 策略、带内/带外管理原则和产品匹配规则。适用于 MDC 模块化数据中心集群(Network Zone)的设计选型。统一执行准则与章节 ID 体系见 [[PRINCIPLE_Guideline]]。

## 文档导航

| 块 | 主题 | 包含章节 |
|----|------|---------|
| [[_blocks/NETWORK_Guideline/01_N1_N2_Foundation]] | N-1/N-2 文件定位与核心设计原则 | N-1, N-2 |
| [[_blocks/NETWORK_Guideline/02_N3_Architecture]] | N-3 网络架构选型 | N-3 |
| [[_blocks/NETWORK_Guideline/03_N4_IB]] | N-4 IB 设计原则 | N-4 |
| [[_blocks/NETWORK_Guideline/04_N5_ROCE]] | N-5 ROCE 设计原则 | N-5 |
| [[_blocks/NETWORK_Guideline/05_N6_N7_N8_Management]] | N-6/N-7/N-8 管理网络(带内+带外+对比) | N-6, N-7, N-8 |
| [[_blocks/NETWORK_Guideline/06_N9_N10_Zone_Security]] | N-9/N-10 网络与 IT Zone 匹配与安全设计 | N-9, N-10 |
| [[_blocks/NETWORK_Guideline/07_N11_N12_Prohibitions_Refs]] | N-11/N-12 禁止事项与参考文档 | N-11, N-12 |

---

## 1. 文件定位与核心设计原则
![[_blocks/NETWORK_Guideline/01_N1_N2_Foundation]]

## 2. 网络架构选型
![[_blocks/NETWORK_Guideline/02_N3_Architecture]]

## 3. IB 设计原则
![[_blocks/NETWORK_Guideline/03_N4_IB]]

## 4. ROCE 设计原则
![[_blocks/NETWORK_Guideline/04_N5_ROCE]]

## 5. 管理网络(带内+带外+对比)
![[_blocks/NETWORK_Guideline/05_N6_N7_N8_Management]]

## 6. 网络与 IT Zone 匹配与安全设计
![[_blocks/NETWORK_Guideline/06_N9_N10_Zone_Security]]

## 7. 禁止事项与参考文档
![[_blocks/NETWORK_Guideline/07_N11_N12_Prohibitions_Refs]]

---

## Changelog

> v1.4 变更(2026-06-17):结构拆分。原 12 个 H2 章节拆分为 7 个独立块文件,存放于 `_blocks/NETWORK_Guideline/`。保留全部 N-1 ~ N-12 章节 ID 与交叉引用。frontmatter 不变。

> v1.3 变更:章节 ID 归位与结构标准化(2026-06-05)。具体变更:
> - **章节 ID 归位**: 12 个一级章节按 [[PRINCIPLE_Guideline#§8 章节 ID 一致性表]] 分配 N-1 ~ N-12 短码。
> - **结构标准化**: 新增 H1 标题、元数据(Version / Last Updated / Source)、速查(Quiqk Reference)、章节速查(Section Index)表;`## Changelog` 统一放置于文件末尾。
> - **交叉链接**: 章节内新增 `[[#§ID 标题]]` 内联锚点;跨文件引用统一使用 `[[PRINCIPLE_Guideline#§X ...]]` 等 § 前缀短码格式。
> - **内容**: 所有技术规则、表格、参数、禁令保持原样,未做删改。

> v1.2 变更(2026-05-19):从 `KB/3RD-PARTY/NETWORK/NETWORK_Guideline.md` 迁移至 `KB/Guideline/NETWORK_Guideline.md`,与其他 Guideline 统一归位;引用路径同步更新。
