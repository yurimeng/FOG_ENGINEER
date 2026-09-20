---
title: "L1240C45 第四节：机架规格"
parent: "[[L1240C45_Tech_Spec_CN]]"
order: 4
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/l1240c45"
  - "#thermal"
  - "#MDC"
created: 2026-06-18
source_file: "PUBLIC/Tech_Spec/L1240C45_Tech_Spec_CN.md"
source_anchors:
  - "^sec-4-rack-spec"
---

## 4. 机架规格 ^sec-4-rack-spec

| 项目 | 参数 |
|------|------|
| 机柜类型 | 48U 标准机柜 |
| 机柜深度 | 1200mm |
| 机柜宽度 | 800mm |
| 机柜数量 | 9 台（8 DLC + 1 风冷） |
| 液冷方式 | 侧置 Manifold（液冷歧管） |
| PDU 位置 | 后置 |
| 机柜后门离集装箱墙距离 | 350mm |
| 底部管路空间 | 350–400mm（配电区域无地板架高） |

### 4.1 冷板 Manifold 配置

| 项目 | 参数 |
|------|------|
| 每 rack manifold 数量 | **2 个**（冷板 ≤ 100）/ **3 个**（冷板 > 100，NVL72-class） |
| 每 manifold 分支数 | 20–50 |
| 每分支设计流量 | **1.6–2.1 L/min**（在 1–3 L/min 规格内 30%+ 余量） |
| 每 manifold 入口 | **PICV（压差独立流量阀）+ 流量计**（防双 manifold 间不平衡） |
| 总 manifold 数量 (L1240C45 整机) | **16–24 个**（8 rack × 2–3 manifold/rack） ^mdc-0bbd25e4b2 |
| 不平衡率 | ≤ 10%（单 manifold 内）/ ≤ 15%（含 manifold 间） |

---
