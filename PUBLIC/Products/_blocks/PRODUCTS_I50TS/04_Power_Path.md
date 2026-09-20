---
title: 电力路径
parent: "[[../I50TS]]"
order: 4
tags:
  - #workspace/engineer
  - #type/product
  - #product/i50ts
  - #power
  - #MDC
created: 2026-06-18
source_file: "PUBLIC/Products/I50TS.md"
source_anchors: []
---

## 6. 电力路径

```
INPUT → PDC → UPS（可选，外置） → A32 Tank → IT Servers ^mdc-90a181b795
```

说明：
- A32 本体**不包含 UPS**（UPS 需外置或由 AC40/DC45 提供） ^mdc-808a380345
- 支持外部 PDC 接入
- 可对接 BESS 或发电机系统
