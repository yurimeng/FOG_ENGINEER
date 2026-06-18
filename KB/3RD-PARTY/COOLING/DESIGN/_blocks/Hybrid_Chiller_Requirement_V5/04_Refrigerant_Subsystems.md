---
title: "Hybrid Chiller V5 — 制冷剂选型 + 干冷器/旁通/加热/湿膜"
parent: "[[Hybrid Chiller Requirement V5]]"
order: 4
tags:
  - #workspace/engineer
  - #type/design-spec
  - #product/Hybrid-Chiller
  - #cooling
  - #MDC
created: 2026-06-17
source_file: "KB/3RD-PARTY/COOLING/DESIGN/Hybrid Chiller Requirement V5.md"
source_anchors: []
---

## 4. 制冷剂选型（各站点法规适用）

| 候选 | 安全 | GWP | 站点适用性 |
|---|---|---|---|
| **R-1234ze（HFO）** | A2L（弱可燃）| 7 | 全部 — 推荐 |
| R-32（HFC） | A2L | 675 | EU 接受；UAE / 泰国接受；TX 接受 |
| R-454B（HFO/HFC 混合）| A2L | 466 | 全部 — 推荐 |
| R-407C（HFC） | A1 | 1774 | EU 2025+ 限制；其他站点过渡接受 |
| R-410A（HFC）| A1 | 2088 | **EU 新设备禁用**；其他站点过渡 |

> A2L 制冷剂在 EU 站点须配制冷剂泄漏检测（EN 378 / ASHRAE 15）+ 充注口专用接头。
> 详细各站点法规适用与推荐选型请回 .Hybrid Chiller Requirement V1.6 §5.4。

---

## 5. 干冷器 / 旁通 / 加热 / 风机 / 湿膜

| 项 | 锁定 |
|---|---|
| **干冷器** | ≥ 1700 kW @ 10°C 环境；变频 EC 风机；翅片亲水铝箔 / 环氧涂层；金属壳热浸镀锌 + 聚酯粉末喷涂 |
| **旁通阀（必配）** | 电动三通调节阀（Belimo / Siemens / Honeywell），与风机转速联动；FWS < 24°C 优先降风机转速，< 22°C 旁通介入 |
| **加热模块（极寒可选；Astana 强制）** | ≤ −8°C 自动启动，达 0°C 关闭；冷启动 FWS < −5°C 时禁止启动水泵；电伴热带配套；品牌 Watlow / Chromalox / Vulcanic |
| **风机** | 一线品牌 EC 变频（ebm-papst / Ziehl-Abegg / Rosenberg）；N+1 冗余 |
| **湿膜（UAE / 泰国强烈建议）** | DN50 / PN10 预留接口；无机纤维或高分子蒸发材料 ≥ 3 年寿命；TDS ≤ 500 ppm；环境 > 25°C 且湿球温差 > 5°C 启动；UAE 高湿（RH > 80%）按实时湿球判断 |
