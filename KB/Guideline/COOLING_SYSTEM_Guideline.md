---
tags:
  - #type/guideline
  - #domain/cooling
---

# COOLING SYSTEM Guideline / 冷却系统技术 Guideline

Document Version: v1.0
Last Updated: 2026-04-11
Owner: Cooling Engineer
Reference: [[Works_Public/AGENTS/Cooling Engineer]]

---

# G-1 ⚠️ MANDATORY WORKFLOW / 强制工作流程

> Cooling Engineer is a **domain specialist**. Focus exclusively on thermal management. Do not attempt to perform work outside your domain.

## Step 1 — Read This Guideline First (MANDATORY)

Before starting any technical work, Cooling Engineer **MUST** read this file.

This Guideline defines:
- Permitted cooling architectures (dry cooler + DX mandatory; pure dry cooler prohibited)
- DX activation threshold (≥28°C ambient)
- IT Zone to Cooling Zone matching rules (AC40, DC45, A32 each have specific capacity requirements)
- Hybrid Cooling System design principles
- Environmental operating ranges

**This Guideline is authoritative. If project requirements conflict with it, flag and escalate to ATS before proceeding.**

## Step 2 — Review Product Catalog

Reference `./KB/COOLING/` to select compatible cooling equipment.

## Step 3 — Perform Technical Analysis

Within your domain, perform:
- Heat load evaluation
- Cooling capacity planning
- Cooling redundancy design
- Environmental adaptability analysis

## Step 4 — Output to ATS

**Output results to ATS only** (do not output directly to AM or clients).

Output must include:
- Recommended cooling architecture
- Capacity calculations
- IT Zone to Cooling Zone pairing
- Product model and quantity
- Redundancy level
- Any Guideline conflicts or escalations

---

# G-2 Thermal Engineering Scope / 热工工程范围

Cooling Engineer is responsible for:

- Cooling architecture selection
- Heat load evaluation
- Cooling capacity planning
- Cooling redundancy design
- Environmental adaptability

The engineer must ensure that thermal management systems remain stable across varying environmental conditions.

---

# G-3 Supported Cooling Technologies / 支持的冷却技术

Cooling Engineer has expertise in:

- **Immersion Cooling** — preferred for high-density compute
- **Direct Liquid Cooling (DLC)** — for hardware that cannot be immersed
- **Rear Door Heat Exchangers**
- **Air Cooling Systems** — legacy deployments only
- **Hybrid Cooling System**（干冷器+DX一体化）
- **DX Systems**（DX 是 Hybrid Cooling 的组成部分）
- **Hybrid Cooling Architectures**

Each technology has specific advantages and deployment conditions.

---

# G-4 Cooling Architecture Priority / 冷却架构优先级

Evaluate cooling technologies in this order:

| Priority | Technology | Applicable Scenario |
|---------|-----------|-------------------|
| 1 | Immersion Cooling | High-density compute, AI training clusters, GPU-dense workloads |
| 2 | Direct Liquid Cooling (DLC) | Hardware cannot be immersed, standard rack infrastructure required |
| 3 | Air Cooling | Low density, legacy deployments only |

Higher thermal efficiency solutions should be preferred when compatible with workload and infrastructure constraints.

---

# G-5 Immersion Cooling / 浸没式冷却

Immersion cooling is the preferred cooling method for high-density computing workloads.

**Advantages:**
- High thermal efficiency
- Uniform heat removal
- Reduced mechanical complexity
- Elimination of large air handling systems

**Particularly suitable for:**
- AI training clusters
- GPU dense compute
- High power density racks

---

# G-6 Direct Liquid Cooling (DLC) / 直冷液冷

DLC is appropriate when:
- Hardware cannot be immersed
- Standard rack infrastructure must be preserved
- Cooling must be integrated with existing datacenter environments

DLC systems typically require:
- Cold plate loops
- Coolant distribution units (CDU)
- External heat rejection systems

---

# G-7 Heat Rejection Systems / 热排放系统

## Permitted Configurations

| Method | Status | Notes |
|--------|--------|-------|
| **Hybrid Cooling System**（干冷器+DX一体化） | ✅ REQUIRED for all AC40/DC45 | Standard configuration |
| 冷却塔 | ✅ Permitted | Requires adequate water supply |
| Pure Dry Cooler | ❌ **PROHIBITED** | Not allowed for any IT Zone deployment |

## DX Activation Rule

**DX (Direct Expansion) is automatically activated when ambient temperature ≥ 28°C.**

- DX is a mandatory component of the Hybrid Cooling System
- Pure dry cooler mode is prohibited regardless of ambient temperature

## Selection Factors

- Climate conditions
- Water availability
- Power efficiency goals
- Operational complexity

---

# G-8 IT Zone to Cooling Zone Matching / IT Zone 与冷却区匹配

## 8.1 Mandatory 1:1 Pairing

**Each IT Zone container must have its own dedicated Cooling Zone unit. N+1 and 2N redundancy are NOT offered for the Cooling Zone.**

| IT Zone Type | Cooling Zone Requirement | Cooling Capacity |
|-------------|------------------------|-----------------|
| AC40 | 1× Hybrid Cooling System | ~600kW class |
| DC45 | 1× Hybrid Cooling System | ~1200kW class |
| A32 | 1× Hybrid Cooling System | ~320kW class |

> Each cooling device is matched to one specific IT Zone device. Do not size one cooling unit to serve multiple IT Zone containers.

## 8.2 Redundancy Constraints

| Zone | N+1 | 2N | Notes |
|------|-----|-----|-------|
| IT Zone | ❌ Not offered | ❌ Not offered | Each container independent |
| **Cooling Zone** | **❌ Not offered** | **❌ Not offered** | 1:1 pairing with IT Zone |
| Power Zone | ✅ Allowed (needs extra switchgear) | ✅ Allowed (needs extra switchgear) | — |

---

# G-9 Environmental Design / 环境设计

Cooling systems must consider local environmental conditions.

Key factors:
- Ambient temperature
- Seasonal temperature variation
- Humidity
- Dust or environmental contamination
- Water availability

Cooling systems must operate reliably under extreme weather conditions.

---

# G-10 Thermal Load Calculation / 热负荷计算

Cooling Engineer must evaluate total thermal load.

**Components:**
- IT heat load
- Pump systems
- Auxiliary equipment
- Electrical conversion losses

**Sizing rule:** Cooling capacity ≥ Peak IT heat load × 1.1 (minimum 10% margin)

**PUE reference:**
- ≤28°C ambient: PUE ~1.1–1.2 (DX off)
- ≥28°C ambient: PUE ~1.2–1.4 (DX activated)

---

# G-11 Redundancy Strategy / 冗余策略

Cooling redundancy follows practical engineering principles:

- N+1 for critical pumps (where applicable within the container)
- Redundant circulation loops where necessary
- Independent cooling modules for container deployments
- Full duplication of cooling plants should be **avoided** unless operational requirements justify the complexity

**⚠️ Cooling Zone does NOT offer N+1 or 2N.** Each cooling device works with one IT Zone device.

---

# G-12 Containerized Cooling / 容器冷却

Containerized datacenters require specialized cooling strategies.

Typical approaches:
- Integrated immersion tanks
- Rack-level DLC systems
- External Hybrid Cooling Systems
- Self-contained cooling loops

The objective is to **minimize external infrastructure dependencies**.

---

# G-13 Extreme Condition Operation / 极端条件运行

Cooling Engineer must ensure systems remain operational during:
- Heat waves
- Cold climates
- Dust-heavy environments
- Remote deployments

Cooling architecture should remain stable across these conditions.

---

# G-14 Product Selection / 产品选择

Only products listed in `./KB/COOLING/` may be selected.

| Product | Supplier | Key Specs | Reference |
|---------|---------|-----------|----------|
| DRYCOOL_with_DX | 泰铂 | 600kW class; IP55; C3防腐; 涡旋压缩机 | [[DRYCOOL_with_DX\|KB/COOLING/DRYCOOL_with_DX]] |
| Hybrid Cooler 600kW | 三河同飞 | 600kW; 螺杆压缩机; -15°C~45°C; IP54 | [[Hybrid Cooler 600kW - 同飞\|KB/Hybrid Cooler 同飞]] |

**If no product in `./KB/COOLING/` meets project requirements, escalate to ATS before proceeding.**

---

# G-15 KB Lookup & Verify / 知识库查阅

## Two-Step Lookup Process

> **Step 1 → Guideline:** Read this file (`COOLING_SYSTEM_Guideline`) first — it defines mandatory architecture rules, IT Zone matching requirements, and prohibited configurations.
> **Step 2 → Products:** Traverse `./KB/COOLING/` to verify individual product parameters match the project requirements.

## Step 1 — This Guideline (Authoritative)

This file is the authoritative source for:
- Permitted cooling architectures (dry cooler + DX mandatory; pure dry cooler prohibited)
- DX activation threshold (≥28°C ambient)
- IT Zone to Cooling Zone matching rules
- Hybrid Cooling System design principles
- Environmental operating ranges

**If a proposed product or configuration contradicts this Guideline, flag and escalate to ATS before proceeding.**

## Step 2 — Product Verification

Check `./KB/COOLING/` subfolder for product specs.

---

# G-16 Verification Checklist / 验证清单

Before finalizing any Cooling Zone design, confirm:

- [ ] Cooling capacity ≥ IT Zone heat load with ≥10% margin
- [ ] DX system present (pure dry cooler = prohibited)
- [ ] Supplier and model documented from `./KB/COOLING/`
- [ ] IT Zone to Cooling Zone 1:1 pairing maintained
- [ ] Environmental temperature range covers site conditions
- [ ] Protection class suitable for deployment environment (IP55 min recommended)
- [ ] No conflicts with mandatory rules in this Guideline
- [ ] Escalation raised if required

---

# G-17 Engineering Warning Conditions / 工程警告条件

Cooling Engineer must raise warnings when:

- Cooling capacity is insufficient for peak heat load
- Ambient temperatures exceed cooling system design limits
- Heat rejection systems are undersized
- Cooling architecture introduces single points of failure
- Customer requests pure dry cooler (prohibited — must escalate)
- Customer requests N+1 or 2N cooling redundancy (not offered — must escalate)

---

# G-18 Escalation Rules / 上报规则

Cooling Engineer **MUST** escalate to ATS when:
- Project requires cooling capacity outside standard Hybrid Cooling System range
- Site ambient temperature exceeds all listed product specifications
- Customer requests pure dry cooler
- Customer requests N+1 or 2N cooling redundancy
- Water-constrained site requires cooling tower not in KB
- IT Zone to Cooling Zone 1:1 pairing cannot be maintained
- No product in `./KB/COOLING/` meets project requirements

**This Guideline is authoritative. If a proposed configuration contradicts it, flag and escalate — do not proceed independently.**

---

# G-19 Final Objective / 最终目标

Deliver thermal management systems that enable reliable high-density computing while minimizing infrastructure complexity.
