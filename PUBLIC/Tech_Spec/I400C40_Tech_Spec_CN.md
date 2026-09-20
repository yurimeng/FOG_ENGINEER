---
tags:
  - "#MDC"
  - "#type/design-spec"
  - "#product/i400c40"
  - "#unconfirmed"
doc_version: v1.6
updated: 2026-08-30
sku_id: I400C40ST50
---
# I400C40 — Tech Spec ^mdc-10012107d0
**All-In-One Immersion Container（40ft 浸没式液冷集装箱）**

> **SKU 标识：** 短别名 **I400C40** · 全 SKU ID `I400C40ST50` · 产品线 **Immersion Cooling（I）** · 状态 **shipped**。命名基准见 [[NAMING_MAP]]。 ^mdc-5ed0f9cb04
>
> **受众说明：** 本文档为销售 / 售前交付物，目标读者：客户、客户经理、方案架构师。参数为准绳值；如与工程设计冲突，以 [[PUBLIC/Products/I400C40|I400C40 产品 PRD]] 与 [[PUBLIC/Products/I50TS|I50TS]] 统一参数表为准。参数基准：**V1.0（2026-07-28）**，源产品文档 AC40 V1.4 / A32 V1.4。 ^mdc-6d94b551c1
>
> **数据源：** 产品参数以 [[PRODUCT_SPEC_BASELINE]]（六 SKU 规格基准表）为准，**与本文冲突时以基准表为准**。本文若干数值来自旧基线 AC40 / A32 V1.4，基准表尚未覆盖，已按 [[UNCONFIRMED_Convention]] 逐项标注。 ^mdc-a0ae79d8fa
>
> **三版互链：** 中文内部版（本文） · 英文内部版 [[I400C40_Tech_Spec_EN]] · 对外输出版 [[I400C40_Tech_Spec_External]]
>
> ✅ **2026-08-30 Yuri 裁定已传导（[[PRODUCT_SPEC_BASELINE]] v2.0）：** §3 / §14 PUE 与整体电力负荷改为 `1.0x` / 逐站点用 <https://mdcx.org> 计算（原 ⛔ PUE 冲突关闭）；§12 交期改为首批 120 天 EXW、Scale 90 天 EXW、假负载运行期 5–30 天，商务 / 运输 / 安装不予承诺（原 ⛔ 交期冲突关闭）；§12 / §14 质保改为核心部件自 EXW 起一年 + 按年服务费，响应级别以 Invoice 为准。
>
> ⏳ **本文档仍带文档级 `#unconfirmed`：** 结构尺寸 / 重量、设施水温位、整箱流量、设计湿球、机架空间为 ⏳ 待证实。逐项的等谁 / 等什么 / 预期时点见对应章节表格备注。**整份不外发**，对客请用对外输出版。
>
> **内部工程详档：** [[PUBLIC/Products/I400C40]] · [[PUBLIC/Products/I50TS]] · [[KB/IMMERSION/I400C40/I400C40 工作负荷]] · [[COOLING_SYSTEM_Guideline]] ^mdc-745a2f39a7

版本：V1.6 | 日期：2026-08-30 | 参数基准：V1.0（2026-07-28）

> **V1.0 首版要点（对齐 AC40/A32 V1.4）：** ^mdc-6c18c3fa48
> 1. IT 容量锁定：**推荐 360kW / 最大 400kW**（8×I50TS（旧称 A32）：推荐 45kW / 最大 50kW）+ 1×10kW 风冷机柜 ^mdc-6cd3457f4e
> 2. 冷却：单相浸没 + Tank 内置 Dual CDU（1+1）；二次侧 **进油 ≤35°C / 出油 ≈43°C / ΔT=8K**；一次侧 ≤32/37°C（ΔT=5K）
> 3. 散热选型：站点历史最高干球 **≤24°C → 纯干冷器**；**>24°C → Hybrid Chiller**（干冷+DX 一体化）
> 4. UPS：**外置（客户自备）** EATON 9395XR-600 + 2×93LiG2（约 10 分钟）— 本体不含 UPS
> 5. 整机 **非 UL 整机认证**（需 UL 时选型 [[PUBLIC/Products/I400C45|I400C45]]） ^mdc-edf40e7ceb

---

## 文档导航

| § | 章节 | 块文件 |
|---|------|--------|
| 1 | Layout / 布局图 | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/01_Sec1_Layout\|01_Sec1_Layout]] |
| 2 | 产品定位 | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/02_Sec2_Positioning\|02_Sec2_Positioning]] |
| 3 | IT 容量 | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/03_Sec3_IT_Capacity\|03_Sec3_IT_Capacity]] |
| 4 | 浸没槽 / 机柜规格 | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/04_Sec4_Rack_Spec\|04_Sec4_Rack_Spec]] |
| 5 | 冷却系统（浸没 + Hybrid 热排放） | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/05_Sec5_Cooling\|05_Sec5_Cooling]] |
| 6 | 配电规格 | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/06_Sec6_Power\|06_Sec6_Power]] |
| 7 | 结构规格 | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/07_Sec7_Structural\|07_Sec7_Structural]] |
| 8 | 网络与线缆管理 | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/08_Sec8_Network\|08_Sec8_Network]] |
| 9 | 环境与合规 | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/09_Sec9_Environment\|09_Sec9_Environment]] |
| 10 | 监控与管理系统 | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/10_Sec10_Monitoring\|10_Sec10_Monitoring]] |
| 11 | 消防与安全 | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/11_Sec11_Fire\|11_Sec11_Fire]] |
| 12 | 服务与支持 | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/12_Sec12_Service\|12_Sec12_Service]] |
| 13 | 选址与安装要求 | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/13_Sec13_Site\|13_Sec13_Site]] |
| 14 | I400C40 主要参数汇总 | [[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/14_Sec14_Summary\|14_Sec14_Summary]] ^mdc-8eb3cc606b |

---

## 1. Layout / 布局图 ^sec-1-layout
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/01_Sec1_Layout]]

## 2. 产品定位 ^sec-2-positioning
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/02_Sec2_Positioning]]

## 3. IT 容量 ^sec-3-it-capacity
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/03_Sec3_IT_Capacity]]

## 4. 浸没槽 / 机柜规格 ^sec-4-rack-spec
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/04_Sec4_Rack_Spec]]

## 5. 冷却系统（浸没 + Hybrid 热排放） ^sec-5-cooling
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/05_Sec5_Cooling]]

## 6. 配电规格 ^sec-6-power
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/06_Sec6_Power]]

## 7. 结构规格 ^sec-7-structural
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/07_Sec7_Structural]]

## 8. 网络与线缆管理 ^sec-8-network
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/08_Sec8_Network]]

## 9. 环境与合规 ^sec-9-environment
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/09_Sec9_Environment]]

## 10. 监控与管理系统 ^sec-10-monitoring
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/10_Sec10_Monitoring]]

## 11. 消防与安全 ^sec-11-fire
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/11_Sec11_Fire]]

## 12. 服务与支持 ^sec-12-service
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/12_Sec12_Service]]

## 13. 选址与安装要求 ^sec-13-site
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/13_Sec13_Site]]

## 14. I400C40 主要参数汇总 ^sec-14-summary
![[PUBLIC/Tech_Spec/_blocks/I400C40_Tech_Spec_CN/14_Sec14_Summary]]

---

## 变更记录

| 版本 | 日期 | 变更摘要 |
|------|------|---------|
| V1.6 | 2026-08-30 | **传导 2026-08-30 Yuri 四条裁定（[[PRODUCT_SPEC_BASELINE]] v2.0）。** ① **PUE 一律写 `1.0x`** —— §3 与 §14 的「低温 ~1.05–1.10 / 高温 ~1.15–1.20」及整体电力负荷 ~400–480 kW 全部作废，改为「随 PUE 变化，逐站点用 <https://mdcx.org>（TCO / Designer）计算」；原 ⛔ PUE 冲突关闭；§3 的 IT Load vs Total Facility Load 概念区分按硬规则保留。② **交期统一为首批 120 天 EXW / Scale 90 天 EXW（自下单起算）**，新增假负载运行期 5–30 天（Supermicro 建议，不含在 EXW 承诺内），商务 / 运输 / 安装一律不予承诺；**删除** §12 的 ~185–230 天与部署 SOP 四阶段表、§14 的部署周期行，上一轮的 ⛔ 提示块一并替换为裁定后的正式表述。③ **质保统一为核心部件自 EXW 起一年 + 后续年份按年收取服务费**；**删除** §12 与 §14 的「9×5 NBD」及其 ⏳ 标记，响应级别一律以 Invoice 为准。④ 双环路 GPU 侧温位裁定不适用浸没线，未作改动。块文件 03 / 12 / 14 同步。 ^mdc-7fb99e33d1 |
| V1.5 | 2026-08-30 | 按 2026-08-30 新命名与新数据基线刷新。① 命名对齐 [[NAMING_MAP]]：AC40 → **I400C40**、A32 → **I50TS**、AC45 → **I400C45**、DC45 → **L1240C45**（标题、正文、块文件 frontmatter `title` 全量替换；槽体首次出现处保留「旧称 A32」一次性说明；Changelog 历史描述与「AC40 V1.4 / A32 V1.4」旧基线版本引用按 [[NAMING_MAP]] §4 保留原样）。② 顶部补 SKU 标识行：全 SKU ID `I400C40ST50` · 产品线 Immersion Cooling · 状态 shipped。③ 建立 CN / EN / External 三版互链。④ 顶部补数据源指针：参数以 [[PRODUCT_SPEC_BASELINE]] 为准，冲突时以基准表为准。⑤ §12 交期在表格上方加 ⛔ conflict 提示块（EXW vs 到场总周期两套口径，**原数字保留**）。⑥ 按 [[UNCONFIRMED_Convention]] 重标置信度，**数值一律保留、只加标记**：设施水 ≤32/37 °C（ΔT=5K）⏳；外形 12,192×2,438×2,896 mm、空箱 12–16 T / 运行 22–30 T、256RU/232OU、整箱流量 87.8 / 97.6 m³/h、设计湿球 28 °C 均 ⏳（旧基线 AC40 V1.4，基准表未覆盖）；**PUE ⛔ conflict** 并在数字同行补上「历史极端干球 ≤ 24 °C」适用边界；质保 1 年 / 9×5 NBD ⏳（基准表 §3.3 无来源）。⑦ frontmatter 加 `#unconfirmed` / `doc_version` / `updated` / `sku_id`。 ^mdc-f892dc063c |
| V1.0 | 2026-07-28 | 首版。按 DC45 Tech Spec 14 节结构建立 AC40 售前 Tech Spec；参数对齐 AC40/A32 V1.4（ΔT=8K、干球 ≤24°C 纯干冷判据、UPS 外置 9395XR-600、电气负荷 PDC 表）。 ^mdc-c7ed511c43 |

---

*文档版本：V1.6 | 最后更新：2026-08-30*
