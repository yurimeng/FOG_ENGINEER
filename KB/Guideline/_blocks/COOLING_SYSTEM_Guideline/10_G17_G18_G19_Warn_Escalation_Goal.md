---
title: §G-17 警告 + §G-18 上报 + §G-19 最终目标
parent: "[[../COOLING_SYSTEM_Guideline]]"
order: 10
tags:
  - #workspace/engineer
  - #type/guideline
  - #domain/cooling
  - #MDC
created: 2026-06-18
source_file: "KB/Guideline/COOLING_SYSTEM_Guideline.md"
source_anchors: []
---

## §G-17 工程警告条件 (Engineering Warning Conditions)

Cooling Engineer must raise warnings when:

- Cooling capacity is insufficient for peak heat load
- Ambient temperatures exceed cooling system design limits
- Heat rejection systems are undersized
- Cooling architecture introduces single points of failure
- Customer requests pure dry cooler at a site with historical max dry-bulb >24°C (out of criterion — must escalate)
- Customer requests N+1 or 2N cooling redundancy (not offered — must escalate)

警告触发后按 [[#§G-18 上报规则]] 处理。

---

## §G-18 上报规则 (Escalation Rules)

Cooling Engineer **MUST** escalate to ATS when:
- Project requires cooling capacity outside standard Hybrid Cooling System range
- Site ambient temperature exceeds all listed product specifications
- Customer requests pure dry cooler at a site with historical max dry-bulb >24°C
- Customer requests N+1 or 2N cooling redundancy
- Water-constrained site requires cooling tower not in KB
- IT Zone to Cooling Zone 1:1 pairing cannot be maintained
- No product in `KB/3RD-PARTY/COOLING/` meets project requirements

**This Guideline is authoritative. If a proposed configuration contradicts it, flag and escalate — do not proceed independently.**

上报路径同步在 [[PRINCIPLE_Guideline#§4 Key Matrix]] S12 场景登记；冷却层 SPOF 评估方法见 [[Risk_Guideline#§R-2 单点故障识别]]。

---

## §G-19 最终目标 (Final Objective)

Deliver thermal management systems that enable reliable high-density computing while minimizing infrastructure complexity.
