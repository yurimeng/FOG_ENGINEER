---
tags:
  - #MDC
---
# MDC Product Quick Reference

> **Audience:** 销售 / 方案架构师 / 客户经理。用于在 AC40 / AC45 / DC45 三个产品平台之间快速选型判断。
> **配套产品文档:** [[DC45 Tech Spec EN]] / [[DC45 Tech Spec CN]] · [[../../FOG A Series/PRODUCTS_AC40]] · [[../../FOG A Series/PRODUCTS_AC45]]
> **注意:** DC45 IT 容量以 V1.4 (2026-05-21) 为准 (8×150kW + 1×40kW = 1240kW);本表"8×155kW"为 V1.2 旧值,已识别为冲突,详见 [[../DESIGN/STD_DC45#^std-2-1-it|STD §3 冲突 C2]]。

---

## 产品平台快速对比

| 维度 | AC40 | AC45 | DC45 |
|------|------|------|------|
| **冷却方式** | 单相浸没式液冷 | 单相浸没式液冷 | 冷板式直冷液冷（DLC）|
| **GPU 平台** | PCIe（H100/H200/H400/4090/5090）| PCIe（可定制混合）| SXM / B系列 / GB系列 |
| **IT 容量** | 400kW | 400kW | 1240kW（8×155kW DLC + 40kW 风冷）⚠️ 见上方备注 |
| **功率密度** | 40–80kW/rack | 40–80kW/rack | 100–150kW/rack（及以上）|
| **UPS 放置** | 外置（客户）| 内置（电力舱）| 内置 |
| **UL 合规** | ❌ | ✅ | ✅ |
| **典型场景** | AI 推理 / 分布式训练 / 边缘算力 | AI 推理 / 分布式训练（UL 认证）| 大规模 AI 训练 / 高性能推理集群 |
| **网络** | Ethernet | Ethernet | InfiniBand / NVLink |
| **选型建议** | 推理优先 + 成本敏感 | 推理优先 + 需要 UL | 训练优先 + 高密度 |

---

详见各产品文档：

- [[../../FOG A Series/PRODUCTS_AC40|KB/FOG A Series/PRODUCTS_AC40]]
- [[../../FOG A Series/PRODUCTS_AC45|KB/FOG A Series/PRODUCTS_AC45]]
- [[DC45 Tech Spec EN|KB/FOG D Series/PRODUCTS/DC45 Tech Spec EN]]

---

*Document Version: v1.0 | Last Updated: 2026-05-31*