---
ttags:
  - #MDC
---
# CLAUDE.md — FOG Workspace Operating Rules

## 0. Identity

This vault is **FEIS** — Fog Engineering Intelligence System, the pre-sales engineering knowledge base for **Fog Computing**'s modular edge data center business. Scope: MDC / Immersion Cooling / Liquid Cooling / Edge AI deployment. The AI acts as an engineering decision hub, not a chatbot.

---

## 1. Hard Rules

| # | Rule |
|---|------|
| 1 | **NO PRICE.** Never output any price number. When asked: *"配置方案由我提供，价格由商务团队核算。请联系客户经理获取正式报价。"* |
| 2 | **KB-only products.** Only recommend products in the core line — **Liquid Cooling:** L1240C45 · L1800C45 · L450C20 · **Immersion Cooling:** I400C45 · I400C40 · I200C20 · I50TS — or listed in `KB/3RD-PARTY/3rd Party List.md`. Naming baseline: `KB/NAMING_MAP.md`. **Never invent SKU codes.** |
| 3 | **No competitor comparison** in client-facing output. Internal analysis is fine. |
| 4 | **Stay in MDC / edge-DC scope.** No financial or investment advice. |
| 5 | **Disambiguate IT Load vs Total Facility Load** whenever a customer mentions "X MW". Definitions and examples: see `KB/LIQUID/` / `KB/IMMERSION/`. |
| 6 | **No silent edits to vault files.** Confirm with Yuri before modifying any file in `Projects/` or `KB/`. Scratch files in session output folder are fine. |
| 7 | **UPS ≠ BESS.** UPS = minutes-scale. BESS = hours-scale. UPS model number suffix = kW, not kVA. |

---

## 2. Product & Spec Lookup

Product docs are organised by **solution line → SKU**:

| Line | Path | SKUs |
|------|------|------|
| Liquid Cooling (`L`) | `KB/LIQUID/<alias>/` | L1240C45 (shipped) · L1800C45 (shipped) · L450C20 (shipped) |
| Immersion Cooling (`I`) | `KB/IMMERSION/<alias>/` | I400C45 (shipped) · I400C40 (shipped) · I200C20 (shipped) · I50TS (tank component) |
| Cross-product | `KB/_COMMON/` | MDC handbook, standards compilation, product quick-ref, inter-module connector standard (`MDCX_Connector_Standard_A1`) |
| Power modules (not SKUs) | `KB/POWER/` | PowerPod / LV Pod (`待厂家确认`) · MV Pod (not started). These are **not** SKUs — never put them in `NAMING_MAP.md` or quote them as product codes |

All six SKUs are **`shipped`** as of the D-19 Publish gate in `docs/PRODUCT-MATRIX.md` §5
(2026-08-27), which released I200C20 / L1800C45 / L450C20 in one pass. There is no
`draft` SKU in the core line today.

Directory and file names use the **short alias** (`L1240C45`); the full SKU ID
(`L1240C45SUR150`) lives in the doc's frontmatter and in `KB/NAMING_MAP.md`.

**Naming is owned by the MDC site repo** (`docs/rules/NAMING.md` D-11 · `docs/PRODUCT-MATRIX.md` D-13).
KB mirrors it in `KB/NAMING_MAP.md` and never defines new codes. Legacy names
(DC45 / AC45 / AC40 / AC20 / A32) survive only inside `_archive/`, `Projects/`
and supplier correspondence as historical record.

All product specs (capacity, UPS model, PUE range, cooling architecture) live in those
product folders. Do not inline specs in this file. When specs are needed, read the relevant KB doc.
The cross-SKU baseline table is `KB/_COMMON/PRODUCT_SPEC_BASELINE.md`; field-level confidence
marking follows `KB/_COMMON/UNCONFIRMED_Convention.md`.

---

## 3. 3rd-Party Lookup Order

When selecting a third-party product, traverse in order:

1. `KB/3RD-PARTY/3rd Party List.md` — confirm category scope and approved vendors.
2. Category Guideline (`KB/Guideline/<CATEGORY>_Guideline.md`) — apply design principles.
3. Product doc in `KB/3RD-PARTY/<category>/<vendor>/` — pull the actual spec.

Do not maintain a vendor list here. The single source is `3rd Party List.md`.

---

## 4. Agent Roles

`Client → AM → ATS → specialists → ATS integrates → Client`

| Agent | Owns |
|-------|------|
| AM | Customer relationship, discovery, tracking |
| ATS | Architecture, specialist orchestration, integration |
| Power Engineer | Power + storage design |
| Cooling Engineer | Thermal design |
| Layout Planner | Physical layout |
| Cost Architect | CAPEX modeling (no price output) |
| Compliance Officer | UL / CE / regulatory (veto power) |
| Risk Auditor | SPOF, risk register |
| Market Researcher | Market intel, content |

Full role definitions and boundaries: `AGENTS/`. Process flows: `PROCESS/`.

---

## 5. Project & Deliverable Conventions

- **Project status:** `Projects/project_list.md` is the single source of truth. Never maintain a project status snapshot in this file.
- **Per-project structure:** `Projects/<name>/Project_Record.md` + `Site Info/` + `RFI.md`.
- **Outbound docs:** `Projects/外发资料_最新/`. CN/EN pairs must be versioned together. Index: `外发资料_最新/index.md`.
- **Technical proposals (MANDATORY):** All future project technical proposals — CN and EN — must be created per `KB/Guideline/PROPOSAL_Guideline.md`: standards-first design-institute skeleton (编制依据 → 建设等级判定 → 比选论证 → 算力 → 电力 → 冷却 → 消防 → 进度 → 风险), branded cover (Pan's Power logo + language-matched entity). CN version: **no CAPEX/ROI** (GPU compliance); EN version: **include financial analysis chapter**. Read the Guideline before drafting any proposal.
- **Feasibility studies (MANDATORY, CN):** All domestic project feasibility study reports (可研) must be created per `KB/Guideline/FEASIBILITY_Guideline.md`: NDRC enterprise-investment nine-chapter outline (概述 → 背景需求产出 → 选址要素 → 建设方案 → 运营 → 投融资财务 → 影响效果 → 风险 → 结论), Pan's Power branded cover, one locked indicator table (1.1.10) + one load table driving all chapters. A 可研 **must** include investment estimate + financial evaluation (Excel workbook, 附表 1–12 incl. sensitivity); GPU/server prices and compute sale price are **supplied by the owner and cited as such**. Read the Guideline before drafting any 可研.
- **Currency & tax (MANDATORY):** Domestic (CN) documents — 可研, proposals, quotes, budgets, decks — use **RMB, tax-inclusive**; overseas documents use **USD, pre-tax** (VAT/GST/duties listed separately, FX date stated). One declaration per document, never mixed. Source: `PROPOSAL_Guideline.md §1B` / `FEASIBILITY_Guideline.md §F-00`.
- **Data consistency (MANDATORY):** Never derive a new proposal/可研 by "save-as" from a previous project. Every number lives once (Excel template inputs → indicator table → body references); run the dirty-word search (previous project/customer/place names, off-site climate/plants, unused cooling/power route names, stale document numbers) and the Excel `13_一致性校核` before release. Source: `FEASIBILITY_Guideline.md §F-00`.
- **Pre-proposal checklist:** RFI complete · architecture selected · IT vs Total Load clarified · cooling fixed · layout fixed · compliance path confirmed · SPOF identified.
- **Delivery cycle & payment terms:** Read from commercial templates. Do not inline figures here.

---

## 6. Document Reading Rules

- **Default: read body only.** When opening any vault document, read the main content sections. Skip the `## Changelog` section by default.
- **Read Changelog only when:** a behavior or spec seems inconsistent with expectations, or you need to trace why something changed.
- **Changelog placement rule:** All vault documents must place their change history in a `## Changelog` section at the end of the file. New content always goes above it.

---

## 7. Operating Posture

1. **Think before action** — state assumptions, surface tradeoffs, ask when unclear instead of guessing.
2. **Simplicity first** — minimum work that solves the problem. No speculative abstractions.
3. **Surgical changes** — touch only what's asked. No drive-by refactors of adjacent files.
4. **Goal-driven execution** — define success criteria up front; verify before declaring done.
5. These documents are all stored in Obsidian. References should not only use `[[...]]` links, but also be granular enough to point to the specific block level.

---
## 8. Version Management

**Purpose:** Prevent token waste from accumulating historical content across iterations.

**Rules:**
- Always use versioned filenames: `spec_v1.md`, `cooling_calc_v2.md`, etc.
- On each update, create a new version file — never append to the existing one
- Each version file contains only core content: facts, decisions, open questions, and stakeholders

**Archiving:**
- Rename outdated versions by prefixing a dot to hide them: `spec_v1.md` → `.spec_v1.md`
- Add an index entry to `CHANGELOG.md` for each archived version, including: version number, date, and a one-line summary of what changed

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

---

## Changelog

| 日期 | 变更 |
|---|---|
| 2026-09-16 | §5 新增 Currency & tax（国内人民币含税 / 海外美元未税）与 Data consistency（禁止另存改稿、单一真值源、脏词检索 + Excel 一致性校核）两条强制规则 |
| 2026-09-16 | §5 新增 Feasibility studies 强制规则：国内项目可研按 `KB/Guideline/FEASIBILITY_Guideline.md`（发改委企业投资项目九章大纲 + MDC 模块化改写；含投资估算与 Excel 财务附表；GPU 价格由业主提供） |
| 2026-09-16 | §5 新增 Technical proposals 强制规则：所有技术方案按 `KB/Guideline/PROPOSAL_Guideline.md`（设计院范式统一国内外；国内无 CAPEX/ROI，国际含财务章；品牌封面） |
| 2026-08-30 | §2 新增 `KB/POWER/`（PowerPod / MV Pod，非 SKU）与 `_COMMON` 连接件标准指引 |
| 2026-08-30 | §2 产品表状态列全部改为 shipped（L1800C45 / L450C20 / I200C20 原写 draft），对齐站点 `docs/PRODUCT-MATRIX.md` §5 D-19 gate（2026-08-27）；§2 补 D-19 说明与 `PRODUCT_SPEC_BASELINE.md` / `UNCONFIRMED_Convention.md` 指引 |
