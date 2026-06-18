---
title: "01_Overview_Agent_Reference — §1 §2"
parent: "[[../3rd Party List]]"
order: 1
tags:
  - "#workspace/engineer"
  - "#type/3rd-party-list"
  - "#product/general"
  - "#architecture"
  - #MDC
created: 2026-06-18
source_file: "KB/3RD-PARTY/3rd Party List.md"
source_anchors:
  - "§1"
  - "§2"
---

# §1. 分类体系说明

在 MDC 体系中，**IT Zone**（A32 / AC40 / AC45 / DC45）是公司自主产品。
**Cooling Zone**、**Power Zone** 和 **Network Zone** 主要采用第三方成熟产品。

## 1.1 二级目录结构（V1.5 新增）

```
3RD-PARTY/
├── STD_Supplier.md             ← ★ 统一供应商管理体系入口
├── BESS/{DESIGN,Suppliers}/
├── Busbar/{DESIGN,Suppliers}/
├── UPS/{DESIGN,Suppliers}/
└── COOLING/{DESIGN,Suppliers}/
```

- **DESIGN/**  — R&D 设计准则/需求书(受众:工程师 + AI)
- **Suppliers/**  — 供应商产品 PRD / 选型记录(受众:人)

---

# §2. Agent 引用规则（重要）

> **Agent 在读取第三方产品时的标准顺序：**
> 1. 查询 [[../3rd Party List|3rd Party List]] ← 本文件
> 2. 查询 [[../STD_Supplier|STD_Supplier]] ← **V1.5 新增**:跨类别供应商管理体系
> 3. 查询对应类别的 **Guideline**（设计原则）
> 4. 在子文件夹中查找合适的产品文档，匹配解决方案
