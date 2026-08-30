---
tags:
  - "#MDC"
  - "#type/design-spec"
  - "#product/l1240c45"
  - "#unconfirmed"
doc_version: v1.6
updated: 2026-08-30
sku_id: L1240C45SUR150
---
# L1240C45 — Tech Spec
**PowerPod with Direct Liquid Cooling (45ft Container)**

> **SKU 标识：** 短别名 **L1240C45** · 全 SKU ID `L1240C45SUR150` · 产品线 **Liquid Cooling（L）** · 状态 **shipped**。命名基准见 [[NAMING_MAP]]。
>
> **受众说明：** 本文档为销售 / 售前交付物,目标读者:客户、客户经理、方案架构师。参数为准绳值;如与工程设计冲突,以 [[STD_L1240C45|STD_L1240C45]] 统一参数表为准。参数基准:V1.4 (2026-05-21)。
>
> **数据源：** 产品参数以 [[PRODUCT_SPEC_BASELINE]]（六 SKU 规格基准表）为准，**与本文冲突时以基准表为准**；L1240C45 的既有工程参数争议仍走 [[STD_L1240C45]] 裁定入口。
>
> **三版互链：** 中文内部版（本文） · 英文内部版 [[L1240C45_Tech_Spec_EN]] · 对外输出版 [[L1240C45_Tech_Spec_External]]
>
> ✅ **2026-08-30 Yuri 裁定已传导（[[PRODUCT_SPEC_BASELINE]] v2.0）：** §3 PUE 与设施总负荷改为 `1.0x` / 逐站点用 <https://mdcx.org> 计算；§12 交期改为首批 120 天 EXW、Scale 90 天 EXW、假负载运行期 5–30 天，商务 / 运输 / 安装不予承诺；§12 与 §14 质保改为核心部件自 EXW 起一年 + 按年服务费，响应级别以 Invoice 为准。原 ⛔ 交期冲突已关闭。
>
> ⏳ **本文档仍带文档级 `#unconfirmed`：** 尚有若干「待确认」行（§9.1 运行海拔、§13 现场调试与当地审批）。逐项的等谁 / 等什么 / 预期时点见对应章节。标记含义见 [[UNCONFIRMED_Convention]] §2；**整份不外发**，对客请用对外输出版。

版本：V1.6 | 日期：2026-08-30 | 参数基准：V1.4（2026-05-21）

> **V1.4 更新（基于当时的三支路冷却重评估 V4；V4 现已点前缀归档，现行版本为 [[KB/LIQUID/L1240C45/DESIGN/L1240C45 三支路冷却重评估 V5|三支路冷却重评估 V5]]）：**
> 1. CDU 选型上修：换热 ≥ 1500 kW / 二次侧流量 ≥ 175 m³/h / 二次侧扬程 ≥ 220 kPa / 二次泵变频 / 2N 或 N+1 冗余
> 2. TCS 循环液锁定为 **PG25**（25% 丙二醇水溶液），TCS 进水 26–28°C
> 3. 三支路冷却架构明确：主 CDU 冷板 / 9× VERTIV DCD35 被动 RDHX / 9× STULZ OHS-084-DG-FC 顶置空调
> 4. 室外侧总散热基线 ≥ 1700 kW
> 5. 冷板 manifold 配置锁定：每 rack 2 个（冷板 ≤ 100）或 3 个（冷板 > 100），每分支 1.6–2.1 L/min，PICV + 流量计

---

## 文档导航

| § | 章节 | 块文件 |
|---|------|--------|
| 1 | Layout / 布局图 | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/01_Sec1_Layout\|01_Sec1_Layout]] |
| 2 | 产品定位 | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/02_Sec2_Positioning\|02_Sec2_Positioning]] |
| 3 | IT 容量 | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/03_Sec3_IT_Capacity\|03_Sec3_IT_Capacity]] |
| 4 | 机架规格 | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/04_Sec4_Rack_Spec\|04_Sec4_Rack_Spec]] |
| 5 | 冷却系统（三支路 TCS PG25 架构） | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/05_Sec5_Cooling\|05_Sec5_Cooling]] |
| 6 | 配电规格 | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/06_Sec6_Power\|06_Sec6_Power]] |
| 7 | 结构规格 | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/07_Sec7_Structural\|07_Sec7_Structural]] |
| 8 | 网络与线缆管理 | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/08_Sec8_Network\|08_Sec8_Network]] |
| 9 | 环境与合规 | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/09_Sec9_Environment\|09_Sec9_Environment]] |
| 10 | 监控与管理系统 | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/10_Sec10_Monitoring\|10_Sec10_Monitoring]] |
| 11 | 消防与安全 | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/11_Sec11_Fire\|11_Sec11_Fire]] |
| 12 | 服务与支持 | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/12_Sec12_Service\|12_Sec12_Service]] |
| 13 | 选址与安装要求 | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/13_Sec13_Site\|13_Sec13_Site]] |
| 14 | L1240C45 主要参数汇总 | [[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/14_Sec14_Summary\|14_Sec14_Summary]] |

---

## 1. Layout / 布局图 ^sec-1-layout
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/01_Sec1_Layout]]

## 2. 产品定位 ^sec-2-positioning
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/02_Sec2_Positioning]]

## 3. IT 容量 ^sec-3-it-capacity
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/03_Sec3_IT_Capacity]]

## 4. 机架规格 ^sec-4-rack-spec
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/04_Sec4_Rack_Spec]]

## 5. 冷却系统（三支路 TCS PG25 架构） ^sec-5-cooling
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/05_Sec5_Cooling]]

## 6. 配电规格 ^sec-6-power
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/06_Sec6_Power]]

## 7. 结构规格 ^sec-7-structural
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/07_Sec7_Structural]]

## 8. 网络与线缆管理 ^sec-8-network
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/08_Sec8_Network]]

## 9. 环境与合规 ^sec-9-environment
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/09_Sec9_Environment]]

## 10. 监控与管理系统 ^sec-10-monitoring
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/10_Sec10_Monitoring]]

## 11. 消防与安全 ^sec-11-fire
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/11_Sec11_Fire]]

## 12. 服务与支持 ^sec-12-service
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/12_Sec12_Service]]

## 13. 选址与安装要求 ^sec-13-site
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/13_Sec13_Site]]

## 14. L1240C45 主要参数汇总 ^sec-14-summary
![[PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/14_Sec14_Summary]]

---

## 变更记录

| 版本 | 日期 | 变更摘要 |
|------|------|---------|
| V1.6 | 2026-08-30 | **传导 2026-08-30 Yuri 四条裁定（[[PRODUCT_SPEC_BASELINE]] v2.0）。** ① **PUE 一律写 `1.0x`** —— §3 的 ~1.07–1.15 / ~1.25–1.35 与 Total Facility Load 区间 ~1325–1675 kW 全部作废，改为「随 PUE 变化，逐站点用 <https://mdcx.org>（TCO / Designer）计算」；§3 的 IT Load vs Total Facility Load 概念区分按硬规则保留。② **交期统一为首批 120 天 EXW / Scale 90 天 EXW（自下单起算）**，新增假负载运行期 5–30 天（Supermicro 建议，不含在 EXW 承诺内），商务 / 运输 / 安装一律不予承诺；**删除** §12 的 ~185–230 天与部署 SOP 四阶段表，上一轮的 ⛔ 提示块一并替换为裁定后的正式表述。③ **质保统一为核心部件自 EXW 起一年 + 后续年份按年收取服务费**；**删除** §12 与 §14 的「9×5 NBD」「1 年 / 9×5 NBD」，响应级别一律以 Invoice 为准。④ 双环路 GPU 侧温位裁定（GPU 36–40 °C）不适用本 SKU（单环路 TCS 26–28 °C），未作改动。块文件 03 / 12 / 14 同步。 |
| V1.5 | 2026-08-30 | 按 2026-08-30 新命名与新数据基线刷新。① 命名对齐 [[NAMING_MAP]]：DC45 → **L1240C45**（标题、正文、块文件 frontmatter `title` 全量替换；Changelog 历史描述与旧文档版本引用按 [[NAMING_MAP]] §4 保留原样）。② 顶部补 SKU 标识行：全 SKU ID `L1240C45SUR150` · 产品线 Liquid Cooling · 状态 shipped。③ 建立 CN / EN / External 三版互链。④ 顶部补数据源指针：参数以 [[PRODUCT_SPEC_BASELINE]] 为准，冲突时以基准表为准，工程参数争议仍走 [[STD_L1240C45]]。⑤ **删除 §6.3「PDU 型号对比」竞品表**（该表将本产品与一款竞品 PDU 并列，而本文受众写明为客户，违反 [[CLAUDE.md]] Hard Rule 3），替换为一行说明。⑥ §12 交期在表格上方加 ⛔ conflict 提示块：「~185–230 天」（到场总周期）与基准表 §3.1「90 天 EXW + 运费买方自理」为两套口径，未裁定前不得单独对客引用；**原数字全部保留**。⑦ frontmatter 加 `#unconfirmed` / `doc_version` / `updated` / `sku_id`。 |
| V1.4 | 2026-05-21 | 同步 [[DESIGN/L1240C45 三支路冷却重评估 2026-05-21\|Rev 11 三支路冷却重评估]]：CDU 上修至 ≥1500 kW / ≥175 m³/h / ≥220 kPa（VFD + 2N/N+1）；TCS 介质锁定 PG25；锁定 9× DCD35 RDHX + 9× STULZ OHS-084-DG-FC；新增 §5 冷却系统、§4.1 冷板 manifold；室外侧基线 ≥1700 kW |
| V1.3 | 2026-05-09 | 服务器进水温度由 24°C 修订为 26–28°C（TCS 范围） |

---

*文档版本：V1.6 | 最后更新：2026-08-30*
