# Workspace Version

Workspace: Engineer Workspace
Product: Fog Computing Engineering AI
Version: v1.1.0
Release Date: 2026-03-29
Status: Active Development

Reference backup: ../KB_backup_20260329_200742

---

# Version History

## v1.1.0 — Team Refactor (2026-03-29)

Core principle updates:
- Principle 7: NO PRICE — absolute prohibition on any price, cost estimate, or quotation
- Principle 8: IT Load vs Total Facility Load — mandatory clarification and dual-output rule
- New file: ./KB/POWER_LOAD.md (IT负载与整体电力负荷定义)

Agent updates:
- AGENTS.md: KB-only product portfolio rule added (A32/AC40/DC45/MDC only)
- AGENTS.md: "Do NOT educate clients" rule added
- AGENTS.md: Hard Boundaries section added (what we do NOT do)
- ATS.md: Configuration output format specified (no price figures)
- ATS.md: IT Load / Total Load clarification required in all outputs
- Cost Architect.md: Refocused from cost estimation to configuration specification
- Risk Auditor.md: Load definition risk added as risk category
- BOOTSTRAP.md: CONFIGURATION mode for pricing inquiries (redirects to AM)
- BOOTSTRAP.md: Price interception rule added

Process updates:
- Proposal Generation Process: Cost estimation removed, configuration spec added
- Capacity Planning Process: IT load and total facility load outputs separated
- Customer Requirement Analysis: Power demand clarification added
- Cooling Architecture Process: IT load vs total facility load reference added
- WORKFLOW.md: Proposal Stage renamed to "Configuration only — NO price"
- DECISION_TREE.md: KB-only portfolio constraint noted

## v1.0.0 — Initial Release
First structured release of the Engineering Workspace.

Includes:

Core System Files
- IDENTITY
- SOUL
- PRINCIPLES
- BOOTSTRAP
- HEARTBEAT

Agent Structure
- AM
- ATS
- Cooling Engineer
- Power Engineer
- Layout Planner
- Cost Architect
- Compliance Officer
- Risk Auditor

Knowledge Base
- A32
- AC40
- DC45
- MDC

Third Party Knowledge
- Cooling Systems
- Power Systems
- Networking
- UPS Eaton 9395XR

Process Libraries
- Pre-sales flow
- Client management
- Certification standards

Tools
- CAD Guidelines
- Notion Workflow
- Quote Engine

---

# Versioning Rules

Versioning follows Semantic Versioning.

Format:

MAJOR.MINOR.PATCH

MAJOR
Breaking architecture changes.

MINOR
New capabilities or modules added.

PATCH
Small improvements, bug fixes, documentation updates.

---

# Compatibility

This workspace is designed for:

OpenClaw Agent Framework

Recommended model capability:

- reasoning LLM
- tool calling
- document retrieval