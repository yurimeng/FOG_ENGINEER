---
title: "冗余设计 + IT Zone 匹配"
parent: "[[PRD-泰铂-Chiller]]"
order: 3
tags:
  - #workspace/engineer
  - #type/prd
  - #product/dry-cooler-dx
  - #supplier/泰铂
  - #cooling
  - #MDC
created: 2026-06-17
source_file: "KB/3RD-PARTY/COOLING/Suppliers/PRD-泰铂-Chiller.md"
source_anchors: []
---

## 3. 冗余设计 + IT Zone 匹配

### 3.1 压缩机冗余(DX 部分)

- N+1 配置(通常 3 用 1 备或更多)
- 支持单台故障不停机
- 满负载时可在线切换

### 3.2 水泵冗余

- 2+1 配置(2 用 1 备)
- 变频控制
- 支持自动切换

### 3.3 干冷器冗余

- 按项目需求配置
- 低温地区可减少干冷器配置

### 3.4 与 IT Zone 的匹配

| IT Zone | 冷却 Zone 配置 |
|---------|---------------|
| AC40(400kW IT) | 干冷器 + DX(AC40 专用) ^mdc-fa55997d2d |
| DC45(1240kW IT) | 干冷器 + DX + 风墙(DC45 专用) ^mdc-c03be771b4 |

参考:
- AC40 完整规格:[[I400C40|I400C40]] ^mdc-1d0932a80d
- DC45 完整规格:[[L1240C45_Tech_Spec_EN|L1240C45]] ^mdc-fbff3467f7
- MDC 标准组合:[[_COMMON/PRODUCTS_MDC]]
- 冷却系统设计原则:[[COOLING_SYSTEM_Guideline]]
