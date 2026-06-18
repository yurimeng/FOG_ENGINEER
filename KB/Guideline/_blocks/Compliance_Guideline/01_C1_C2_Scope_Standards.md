---
title: "C-1/C-2 适用范围与关键标准"
parent: "[[Compliance_Guideline]]"
order: 1
tags:
  - #workspace/engineer
  - #type/guideline
  - #product/compliance
  - #compliance
  - #MDC
created: 2026-06-17
source_file: "KB/Guideline/Compliance_Guideline.md"
source_anchors:
  - "C-1 适用范围"
  - "C-2 关键标准"
---

## C-1 适用范围 / Applicable Scope

Compliance Officer evaluates compliance across the following domains:

| Domain / 领域 | Content / 内容 |
|---|---|
| Electrical safety / 电气安全 | UL, CSA, IEC, local codes |
| Cooling system safety / 冷却系统安全 | Thermal management, equipment safety |
| BESS / Energy storage / 储能系统 | Battery safety, thermal management, electrical isolation, fire suppression |
| Container datacenter / 容器数据中心 | Structural integrity, electrical integration, emergency access |
| Fire protection / 消防系统 | NFPA standards, fire suppression integration |
| Operational safety / 运维安全 | Safety procedures, certification requirements |

> Compliance Officer 拥有对合规结论的 **veto 权力**（详见 `AGENTS/Compliance Officer.md`）。当 [[#C-6 合规风险识别]] 中的任一红旗被触发时，结论即为 FAIL，必须上报 ATS。

---

## C-2 关键标准 / Key Standards

Compliance Officer must be aware of and reference the following major industry standards:

### Electrical Safety / 电气安全

- **UL Standards** — Underwriters Laboratories safety requirements
- **CSA Standards** — Canadian Standards Association requirements
- **IEC Standards** — International Electrotechnical Commission standards
- **Local electrical codes** — Regional jurisdictional requirements

### Fire Protection / 消防

- **NFPA Fire Protection Standards** — National Fire Protection Association codes
  - NFPA 855 (Standard for the Installation of Stationary Energy Storage Systems)
  - Applicable fire suppression requirements for BESS and datacenter environments

> 制冷剂选型与 IP 防护等级涉及 [[COOLING_SYSTEM_Guideline#§G-9 环境设计]]；电气隔离细节涉及 [[POWER_SYSTEMS_Guideline#§P-5 UPS 选型]]。跨域冲突时按 [[PRINCIPLE_Guideline#§6 跨 Guideline 冲突处理]] 处理：涉及安全/合规 → 合规侧优先。
