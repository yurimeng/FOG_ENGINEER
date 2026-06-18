---
tags:
  - "#MDC"
  - "#type/design-spec"
  - "#product/dc45"

---
# DC45 — Quick Tech Spec
**PowerPod with Direct Liquid Cooling (45ft Container)**

> **受众说明：** 本文档为销售 / 售前交付物,目标读者:客户、客户经理、方案架构师。参数为准绳值;如与工程设计冲突,以 [[KB/FOG D Series/DESIGN/STD_DC45|STD_DC45]] 统一参数表为准。参数基准:V1.4 (2026-05-21)。
>
> **English version:** [[DC45_Tech_Spec_EN]]

版本：V1.4 | 日期：2026-05-21

> **V1.4 更新（基于 [[KB/FOG D Series/DESIGN/DC45 三支路冷却重评估 V4|DC45 三支路冷却重评估 V4]]）：**
> 1. CDU 选型上修：换热 ≥ 1500 kW / 二次侧流量 ≥ 175 m³/h / 二次侧扬程 ≥ 220 kPa / 二次泵变频 / 2N 或 N+1 冗余
> 2. TCS 循环液锁定为 **PG25**（25% 丙二醇水溶液），TCS 进水 26–28°C
> 3. 三支路冷却架构明确：主 CDU 冷板 / 9× VERTIV DCD35 被动 RDHX / 9× STULZ OHS-084-DG-FC 顶置空调
> 4. 室外侧总散热基线 ≥ 1700 kW
> 5. 冷板 manifold 配置锁定：每 rack 2 个（冷板 ≤ 100）或 3 个（冷板 > 100），每分支 1.6–2.1 L/min，PICV + 流量计

---

## 文档导航

| § | 章节 | 块文件 |
|---|------|--------|
| 1 | Layout / 布局图 | [[_blocks/DC45_Tech_Spec_CN/01_Sec1_Layout\|01_Sec1_Layout]] |
| 2 | 产品定位 | [[_blocks/DC45_Tech_Spec_CN/02_Sec2_Positioning\|02_Sec2_Positioning]] |
| 3 | IT 容量 | [[_blocks/DC45_Tech_Spec_CN/03_Sec3_IT_Capacity\|03_Sec3_IT_Capacity]] |
| 4 | 机架规格 | [[_blocks/DC45_Tech_Spec_CN/04_Sec4_Rack_Spec\|04_Sec4_Rack_Spec]] |
| 5 | 冷却系统（三支路 TCS PG25 架构） | [[_blocks/DC45_Tech_Spec_CN/05_Sec5_Cooling\|05_Sec5_Cooling]] |
| 6 | 配电规格 | [[_blocks/DC45_Tech_Spec_CN/06_Sec6_Power\|06_Sec6_Power]] |
| 7 | 结构规格 | [[_blocks/DC45_Tech_Spec_CN/07_Sec7_Structural\|07_Sec7_Structural]] |
| 8 | 网络与线缆管理 | [[_blocks/DC45_Tech_Spec_CN/08_Sec8_Network\|08_Sec8_Network]] |
| 9 | 环境与合规 | [[_blocks/DC45_Tech_Spec_CN/09_Sec9_Environment\|09_Sec9_Environment]] |
| 10 | 监控与管理系统 | [[_blocks/DC45_Tech_Spec_CN/10_Sec10_Monitoring\|10_Sec10_Monitoring]] |
| 11 | 消防与安全 | [[_blocks/DC45_Tech_Spec_CN/11_Sec11_Fire\|11_Sec11_Fire]] |
| 12 | 服务与支持 | [[_blocks/DC45_Tech_Spec_CN/12_Sec12_Service\|12_Sec12_Service]] |
| 13 | 选址与安装要求 | [[_blocks/DC45_Tech_Spec_CN/13_Sec13_Site\|13_Sec13_Site]] |
| 14 | DC45 主要参数汇总 | [[_blocks/DC45_Tech_Spec_CN/14_Sec14_Summary\|14_Sec14_Summary]] |

---

## 1. Layout / 布局图 ^sec-1-layout
![[_blocks/DC45_Tech_Spec_CN/01_Sec1_Layout]]

## 2. 产品定位 ^sec-2-positioning
![[_blocks/DC45_Tech_Spec_CN/02_Sec2_Positioning]]

## 3. IT 容量 ^sec-3-it-capacity
![[_blocks/DC45_Tech_Spec_CN/03_Sec3_IT_Capacity]]

## 4. 机架规格 ^sec-4-rack-spec
![[_blocks/DC45_Tech_Spec_CN/04_Sec4_Rack_Spec]]

## 5. 冷却系统（三支路 TCS PG25 架构） ^sec-5-cooling
![[_blocks/DC45_Tech_Spec_CN/05_Sec5_Cooling]]

## 6. 配电规格 ^sec-6-power
![[_blocks/DC45_Tech_Spec_CN/06_Sec6_Power]]

## 7. 结构规格 ^sec-7-structural
![[_blocks/DC45_Tech_Spec_CN/07_Sec7_Structural]]

## 8. 网络与线缆管理 ^sec-8-network
![[_blocks/DC45_Tech_Spec_CN/08_Sec8_Network]]

## 9. 环境与合规 ^sec-9-environment
![[_blocks/DC45_Tech_Spec_CN/09_Sec9_Environment]]

## 10. 监控与管理系统 ^sec-10-monitoring
![[_blocks/DC45_Tech_Spec_CN/10_Sec10_Monitoring]]

## 11. 消防与安全 ^sec-11-fire
![[_blocks/DC45_Tech_Spec_CN/11_Sec11_Fire]]

## 12. 服务与支持 ^sec-12-service
![[_blocks/DC45_Tech_Spec_CN/12_Sec12_Service]]

## 13. 选址与安装要求 ^sec-13-site
![[_blocks/DC45_Tech_Spec_CN/13_Sec13_Site]]

## 14. DC45 主要参数汇总 ^sec-14-summary
![[_blocks/DC45_Tech_Spec_CN/14_Sec14_Summary]]

---

## 变更记录

| 版本 | 日期 | 变更摘要 |
|------|------|---------|
| V1.4 | 2026-05-21 | 同步 [[DESIGN/DC45 三支路冷却重评估 2026-05-21\|Rev 11 三支路冷却重评估]]：CDU 上修至 ≥1500 kW / ≥175 m³/h / ≥220 kPa（VFD + 2N/N+1）；TCS 介质锁定 PG25；锁定 9× DCD35 RDHX + 9× STULZ OHS-084-DG-FC；新增 §5 冷却系统、§4.1 冷板 manifold；室外侧基线 ≥1700 kW |
| V1.3 | 2026-05-09 | 服务器进水温度由 24°C 修订为 26–28°C（TCS 范围） |

---

*文档版本：V1.4 | 最后更新：2026-05-21*
