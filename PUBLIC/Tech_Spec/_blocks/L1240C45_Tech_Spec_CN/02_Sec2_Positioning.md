---
title: "L1240C45 第二节：产品定位"
parent: "[[L1240C45_Tech_Spec_CN]]"
order: 2
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/l1240c45"
  - "#thermal"
  - "#MDC"
created: 2026-06-18
source_file: "PUBLIC/Tech_Spec/L1240C45_Tech_Spec_CN.md"
source_anchors:
  - "^sec-2-positioning"
---

## 2. 产品定位 ^sec-2-positioning

L1240C45 是 **45ft 集装箱规格的直冷液冷（DLC）模块化数据中心**，采用冷板式液冷技术（Direct Liquid Cooling），适用于超大算力 AI 集群高密度部署。 ^mdc-3d5765f5f4

![[PDC_SLD_EN_light.svg|SuOCbROt9ozRtAxyvDrcBiXnnqc.png]]

> **冷却架构**：L1240C45 采用 **TCS PG25 三支路并联** 冷却架构，所有热量统一通过 TCS 二次环路送至室外侧（混合干冷器 + DX）： ^mdc-f2cbb30faa
> - **Branch 1 — 主 CDU 冷板回路**：8 × DLC 机柜 73% 液冷热量
> - **Branch 2 — 9× 被动 RDHX**：吸收机柜后门 47–55% 排风热
> - **Branch 3 — 9× 顶置 STULZ OHS-084-DG-FC**：处理机房残余空气热 + UPS/辅助热

---
