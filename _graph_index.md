---
type: meta
title: "FOG Graph Index — Communities 速查"
updated: 2026-08-30T00:00:00Z
tags:
  - #workspace/engineer
  - #type/graph-index
  - #system/feis
  - #MDC
source: graphify-out/graph.json + GRAPH_REPORT.md
---

# FOG — Graph Index (Community 速查)

> **这一页只是 graph.json 的目录，不存事实。** 事实见各 KB 文档本身。本页让你快速定位"我要找的东西在哪个 community"。
>
> **数据源：** `graphify-out/graph.json`（2995 节点 / 2815 links / 379 community / 41 hyperedges，AST-only 生成，0 token cost）
>
> **重生成：** `graphify update .` 然后 `python3 .tools/gen_graph_index.py graphify-out`
>
> **权威源：** 见各 community 标题后的 `C##` —— 读 `GRAPH_REPORT.md` 查详情

---

## 怎么用

| 我想找… | 看哪组 |
|---------|--------|
| FEIS 身份 / 原则 / 工程哲学 | A_FEIS_Identity |
| 产品手册（Liquid Cooling：L1240C45/L1800C45/L450C20 · Immersion Cooling：I400C45/I400C40/I200C20 · I50TS 槽体组件 · MDC）| B_Product |
| 冷却架构（浸没/DLC/CDU/RDHX/TriBranch/PUE）| C_Cooling |
| 电力（BESS/UPS/Busbar/柴发）| D_Power |
| 网络与安全（TLS/802.1X/水印）| E_Network_Security |
| 合规/风险/消防/认证 | F_Compliance_Risk |
| 成本（CAPEX/TCO/Cost Methodology）| G_Cost |
| Agent 角色/工作流/治理 | H_Workflow_Agents |
| 供应商（TICA/Siemens/EATON/Gotion/Stulz/Vertiv）| I_Vendors |
| 项目交付物（EXT-001/PQTech/客户访谈）| J_Project |
| 布局（机柜/线缆/托盘）| K_Layout |
| Guideline 命名规范 / 文档树 | L_Guidelines_Meta |
| 市场情报 / 内容输出 | M_Marketing |

---

## 全量 Community 表（按节点数降序）

> **怎么读：** 名字来自 `graphify-out/.graphify_labels.json`（权威）；节点数和类型分布来自 `graphify-out/graph.json`。本表**不是**手工分组 —— 直接按节点数排，主题自现。
>
> ⚠️ **旧名说明（2026-08-30）：** 下表 community 名称（如 `C19 AC40 Pipeline Layout`、`C05 DC45 Power Distribution`、`C00 Product Architecture (DC45/AC45/AC40/A32)`）由 `graphify label` 从 `.graphify_labels.json` 机器生成，**本页不手工改** —— 手改会在下次 `gen_graph_index.py` 重生成时被覆盖，且与 labels.json 失配。这些标签中的旧名 **DC45 / AC45 / AC40 / AC20 / A32** 分别对应 **L1240C45 / I400C45 / I400C40 / I200C20 / I50TS**（见 [[NAMING_MAP]]），要消除需先 `graphify update .` + `graphify label .` 重新打标，再重生成本表。
>
> **自动重生成：** `python3 .tools/gen_graph_index.py graphify-out`（输出本节表格），再用 Write 工具覆盖本节。脚本读取 labels.json 和 graph.json，不写启发式。

| C# | 名称 | 节点 | 类型 |
|----|------|------|------|
| C02 | Compliance & Risk | 49 | concept:32/document:15/paper:2 |
| C13 | Vendor Scope Changes (Astana removed) | 47 | document:47 |
| C19 | AC40 Pipeline Layout | 43 | document:43 |
| C63 | Watermark / TLS / 802.1X Security | 41 | document:40/rationale:1 |
| C87 | Community 87 | 39 | document:39 |
| C88 | Community 88 | 36 | document:36 |
| C89 | Community 89 | 34 | document:34 |
| C90 | Community 90 | 34 | document:34 |
| C11 | Container Cooling & Compliance | 34 | concept:22/document:10/image:2 |
| C91 | Community 91 | 31 | document:31 |
| C92 | Community 92 | 29 | document:29 |
| C94 | Community 94 | 28 | document:28 |
| C93 | Community 93 | 28 | document:28 |
| C05 | DC45 Power Distribution | 28 | concept:15/document:11/image:1/paper:1 |
| C95 | Community 95 | 26 | document:26 |
| C96 | Community 96 | 26 | document:26 |
| C97 | Community 97 | 25 | document:25 |
| C98 | Community 98 | 25 | document:25 |
| C99 | Community 99 | 25 | document:25 |
| C06 | Product Comparison & Heat Rejection | 25 | concept:16/document:9 |
| C100 | Community 100 | 24 | document:24 |
| C101 | Community 101 | 24 | document:24 |
| C17 | DC45 Site & Version History | 23 | document:14/concept:6/paper:2/image:1 |
| C102 | Community 102 | 23 | document:23 |
| C103 | Community 103 | 23 | document:23 |
| C104 | Community 104 | 23 | document:23 |
| C105 | Community 105 | 22 | document:22 |
| C08 | DC45 DLC Rack Performance | 22 | concept:17/document:4/image:1 |
| C00 | Product Architecture (DC45/AC45/AC40/A32) | 21 | document:15/concept:3/rationale:2/image:1 |
| C106 | Community 106 | 21 | document:21 |
| C107 | Community 107 | 20 | document:20 |
| C108 | Community 108 | 19 | document:19 |
| C09 | Power Zone (BESS & UPS Suppliers) | 18 | document:10/concept:7/paper:1 |
| C18 | Site Climate & 3-Branch Cooling | 18 | concept:12/document:6 |
| C109 | Community 109 | 18 | document:18 |
| C110 | Community 110 | 17 | document:16/rationale:1 |
| C111 | Community 111 | 17 | document:17 |
| C112 | Community 112 | 17 | document:17 |
| C113 | Community 113 | 17 | document:17 |
| C114 | Community 114 | 17 | document:17 |
| C16 | Agent Organization (AM/ATS/Specialists) | 17 | concept:7/document:6/rationale:4 |
| C15 | A32 Immersion Cabinet | 17 | concept:10/document:6/paper:1 |
| C115 | Community 115 | 16 | document:16 |
| C117 | Community 117 | 16 | document:16 |
| C118 | Community 118 | 16 | document:16 |
| C116 | Community 116 | 16 | document:16 |
| C12 | Agent I/O Matrix & Onboarding | 15 | concept:9/document:5/image:1 |
| C119 | Community 119 | 15 | document:15 |
| C120 | Community 120 | 14 | document:14 |
| C121 | Community 121 | 14 | document:14 |
| C123 | Community 123 | 14 | document:14 |
| C122 | Community 122 | 14 | document:14 |
| C124 | Community 124 | 14 | document:14 |
| C14 | FEIS Identity & Engineering Access | 14 | concept:10/document:4 |
| C125 | Community 125 | 13 | document:8/rationale:5 |
| C127 | Community 127 | 13 | document:13 |
| C126 | Community 126 | 13 | document:6/concept:6/image:1 |
| C128 | Community 128 | 13 | document:13 |
| C04 | Network & Cooling Selection | 13 | document:6/concept:5/image:1/code:1 |
| C03 | MDC Product Hierarchy | 13 | document:6/concept:6/paper:1 |
| C131 | Community 131 | 12 | document:12 |
| C132 | Community 132 | 12 | document:12 |
| C133 | Community 133 | 12 | document:12 |
| C129 | Community 129 | 12 | document:9/rationale:3 |
| C130 | Community 130 | 12 | document:10/rationale:2 |
| C134 | Community 134 | 12 | document:12 |
| C01 | ATS Workflow & Governance | 12 | concept:8/document:3/rationale:1 |
| C21 | Cooling Capacity & Dual Source Design | 12 | concept:8/document:4 |
| C136 | Community 136 | 11 | document:11 |
| C137 | Community 137 | 11 | document:11 |
| C139 | Community 139 | 11 | document:11 |
| C141 | Community 141 | 11 | document:11 |
| C50 | MDC Engineering Doctrine | 11 | document:9/rationale:2 |
| C138 | Community 138 | 11 | document:11 |
| C135 | Community 135 | 11 | document:8/rationale:3 |
| C10 | DC45 Tech Spec Sections | 11 | document:5/concept:5/rationale:1 |
| C140 | Community 140 | 11 | document:11 |
| C07 | Agent Roles & Compliance Standards | 11 | concept:9/document:2 |
| C145 | Community 145 | 10 | document:10 |
| C151 | Community 151 | 10 | document:10 |
| C152 | Community 152 | 10 | document:10 |
| C153 | Community 153 | 10 | document:10 |
| C144 | Community 144 | 10 | document:10 |
| C146 | Community 146 | 10 | document:10 |
| C147 | Community 147 | 10 | document:10 |
| C148 | Community 148 | 10 | document:10 |
| C150 | Community 150 | 10 | document:10 |
| C149 | Community 149 | 10 | document:10 |
| C142 | Community 142 | 10 | concept:7/document:3 |
| C143 | Community 143 | 10 | concept:5/document:4/paper:1 |
| C156 | Community 156 | 9 | document:9 |
| C159 | Community 159 | 9 | document:9 |
| C168 | Community 168 | 9 | document:9 |
| C154 | Community 154 | 9 | document:9 |
| C155 | Community 155 | 9 | document:9 |
| C161 | Community 161 | 9 | document:9 |
| C162 | Community 162 | 9 | document:9 |
| C158 | Community 158 | 9 | document:9 |
| C160 | Community 160 | 9 | document:9 |
| C164 | Community 164 | 9 | document:9 |
| C165 | Community 165 | 9 | document:9 |
| C166 | Community 166 | 9 | document:9 |
| C167 | Community 167 | 9 | document:9 |
| C157 | Community 157 | 9 | document:8/concept:1 |
| C169 | Community 169 | 9 | document:9 |
| C170 | Community 170 | 9 | document:9 |
| C163 | Community 163 | 9 | document:9 |
| C22 | Immersion Cooling Architecture | 9 | document:4/concept:4/image:1 |
| C23 | Cost Architect Rules | 9 | concept:5/document:4 |
| C182 | Community 182 | 8 | code:6/rationale:2 |
| C171 | Community 171 | 8 | document:8 |
| C172 | Community 172 | 8 | document:8 |
| C177 | Community 177 | 8 | document:8 |
| C178 | Community 178 | 8 | document:8 |
| C186 | Community 186 | 8 | document:8 |
| C176 | Community 176 | 8 | document:8 |
| C179 | Community 179 | 8 | document:8 |
| C180 | Community 180 | 8 | document:8 |
| C173 | Community 173 | 8 | document:8 |
| C185 | Community 185 | 8 | document:8 |
| C183 | Community 183 | 8 | document:8 |
| C184 | Community 184 | 8 | document:8 |
| C174 | Community 174 | 8 | document:8 |
| C175 | Community 175 | 8 | document:8 |
| C187 | Community 187 | 8 | document:8 |
| C181 | Community 181 | 8 | document:8 |
| C25 | AC40 Power & Tank CDU Redundancy | 8 | concept:4/document:2/rationale:2 |
| C26 | DC45 Rack Topology (48U) | 8 | concept:4/document:2/image:2 |
| C28 | DC45 Side View Layout | 8 | concept:6/image:2 |
| C20 | I400C40 Layout & Cooling Redundancy | 8 | concept:5/image:2/document:1 |
| C27 | DC45 Cable & Tray Engineering | 8 | concept:5/document:3 |
| C24 | Fire Protection & Safety | 8 | concept:6/document:2 |
| C193 | Community 193 | 7 | document:7 |
| C194 | Community 194 | 7 | document:7 |
| C197 | Community 197 | 7 | document:7 |
| C195 | Community 195 | 7 | document:7 |
| C199 | Community 199 | 7 | document:7 |
| C200 | Community 200 | 7 | document:7 |
| C206 | Community 206 | 7 | document:7 |
| C207 | Community 207 | 7 | document:7 |
| C208 | Community 208 | 7 | document:7 |
| C209 | Community 209 | 7 | document:7 |
| C192 | Community 192 | 7 | document:5/concept:2 |
| C203 | Community 203 | 7 | document:7 |
| C204 | Community 204 | 7 | document:7 |
| C196 | Community 196 | 7 | document:7 |
| C191 | Community 191 | 7 | document:7 |
| C198 | Community 198 | 7 | document:7 |
| C205 | Community 205 | 7 | document:7 |
| C201 | Community 201 | 7 | document:7 |
| C189 | Community 189 | 7 | document:6/concept:1 |
| C202 | Community 202 | 7 | document:7 |
| C210 | Community 210 | 7 | document:7 |
| C211 | Community 211 | 7 | document:7 |
| C190 | Community 190 | 7 | concept:5/document:2 |
| C29 | CAPEX Categories (K-1/K-2) | 7 | concept:4/document:2/paper:1 |
| C188 | Community 188 | 7 | concept:6/document:1 |
| C212 | Community 212 | 6 | document:6 |
| C221 | Community 221 | 6 | document:6 |
| C222 | Community 222 | 6 | document:6 |
| C223 | Community 223 | 6 | document:6 |
| C224 | Community 224 | 6 | document:6 |
| C229 | Community 229 | 6 | document:6 |
| C230 | Community 230 | 6 | document:6 |
| C234 | Community 234 | 6 | document:6 |
| C218 | Community 218 | 6 | document:6 |
| C219 | Community 219 | 6 | document:6 |
| C214 | Community 214 | 6 | document:6 |
| C226 | Community 226 | 6 | document:6 |
| C227 | Community 227 | 6 | document:6 |
| C228 | Community 228 | 6 | document:6 |
| C231 | Community 231 | 6 | document:6 |
| C232 | Community 232 | 6 | document:6 |
| C233 | Community 233 | 6 | document:6 |
| C225 | Community 225 | 6 | document:6 |
| C217 | Community 217 | 6 | document:4/rationale:1/image:1 |
| C213 | Community 213 | 6 | concept:3/document:2/rationale:1 |
| C33 | DC45 TriBranch Air-Cooled RDHX | 6 | concept:4/document:2 |
| C32 | DC45 TCS PG25 3-Branch Cooling | 6 | document:3/concept:3 |
| C220 | Community 220 | 6 | concept:5/document:1 |
| C215 | Community 215 | 6 | concept:4/document:2 |
| C31 | CDU Spec (1350kW TriBranch) | 6 | concept:5/document:1 |
| C30 | AC40 Network Configuration | 6 | concept:5/image:1 |
| C216 | Community 216 | 6 | concept:6 |
| C236 | Community 236 | 5 | document:5 |
| C244 | Community 244 | 5 | document:5 |
| C246 | Community 246 | 5 | document:5 |
| C248 | Community 248 | 5 | document:5 |
| C249 | Community 249 | 5 | document:5 |
| C250 | Community 250 | 5 | document:5 |
| C247 | Community 247 | 5 | document:5 |
| C259 | Community 259 | 5 | document:5 |
| C269 | Community 269 | 5 | document:5 |
| C270 | Community 270 | 5 | document:5 |
| C75 | EATON 93Li-G2 BESS Brochure | 5 | document:4/concept:1 |
| C271 | Community 271 | 5 | document:5 |
| C235 | Community 235 | 5 | document:5 |
| C254 | Community 254 | 5 | document:5 |
| C239 | Community 239 | 5 | document:5 |
| C238 | Community 238 | 5 | document:5 |
| C240 | Community 240 | 5 | document:5 |
| C251 | Community 251 | 5 | document:5 |
| C252 | Community 252 | 5 | document:5 |
| C255 | Community 255 | 5 | document:5 |
| C256 | Community 256 | 5 | document:5 |
| C257 | Community 257 | 5 | document:5 |
| C260 | Community 260 | 5 | document:5 |
| C258 | Community 258 | 5 | document:5 |
| C261 | Community 261 | 5 | document:5 |
| C262 | Community 262 | 5 | document:5 |
| C263 | Community 263 | 5 | document:5 |
| C264 | Community 264 | 5 | document:5 |
| C265 | Community 265 | 5 | document:5 |
| C242 | Community 242 | 5 | document:5 |
| C243 | Community 243 | 5 | document:5 |
| C267 | Community 267 | 5 | document:5 |
| C268 | Community 268 | 5 | document:5 |
| C266 | Community 266 | 5 | document:5 |
| C35 | TCO Baseline Assumptions | 5 | concept:4/document:1 |
| C34 | DC45 CeilAir & Manifold Design | 5 | concept:4/document:1 |
| C253 | Community 253 | 5 | document:4/concept:1 |
| C241 | Community 241 | 5 | document:3/concept:2 |
| C245 | Community 245 | 5 | concept:3/document:2 |
| C237 | Community 237 | 5 | concept:4/document:1 |
| C274 | Community 274 | 4 | document:4 |
| C275 | Community 275 | 4 | document:4 |
| C281 | Community 281 | 4 | document:4 |
| C280 | Community 280 | 4 | document:4 |
| C283 | Community 283 | 4 | document:4 |
| C272 | Community 272 | 4 | document:4 |
| C282 | Community 282 | 4 | document:4 |
| C287 | Community 287 | 4 | document:4 |
| C305 | Community 305 | 4 | document:4 |
| C273 | Community 273 | 4 | document:4 |
| C296 | Community 296 | 4 | document:4 |
| C297 | Community 297 | 4 | document:4 |
| C276 | Community 276 | 4 | document:4 |
| C288 | Community 288 | 4 | document:4 |
| C289 | Community 289 | 4 | document:4 |
| C304 | Community 304 | 4 | document:4 |
| C290 | Community 290 | 4 | document:4 |
| C284 | Community 284 | 4 | document:4 |
| C285 | Community 285 | 4 | document:4 |
| C291 | Community 291 | 4 | document:4 |
| C292 | Community 292 | 4 | document:4 |
| C293 | Community 293 | 4 | document:4 |
| C294 | Community 294 | 4 | document:4 |
| C295 | Community 295 | 4 | document:4 |
| C278 | Community 278 | 4 | document:4 |
| C279 | Community 279 | 4 | document:4 |
| C303 | Community 303 | 4 | document:4 |
| C302 | Community 302 | 4 | document:4 |
| C300 | Community 300 | 4 | document:4 |
| C301 | Community 301 | 4 | document:4 |
| C298 | Community 298 | 4 | document:4 |
| C299 | Community 299 | 4 | document:4 |
| C38 | Vendor Changelog (TICA/cooling) | 4 | document:2/concept:2 |
| C40 | Vault Identity & Document Tree | 4 | concept:3/document:1 |
| C42 | Guideline ID Schema (G/P/N/C/K/L/R/M) | 4 | concept:2/document:1/rationale:1 |
| C44 | Risk Red Flags & Load Risk | 4 | concept:3/document:1 |
| C36 | I50TS Flow Diagram Components | 4 | concept:2/image:1/document:1 |
| C39 | DC45 Branch 1+2 (CDU + CoolLoop) | 4 | document:3/concept:1 |
| C41 | FEIS Core Capabilities | 4 | document:2/concept:2 |
| C43 | PRINCIPLE Escalation & Cross-Reference | 4 | concept:4 |
| C37 | PUE Reference & Thermal Load | 4 | concept:4 |
| C286 | Community 286 | 4 | concept:3/document:1 |
| C277 | Community 277 | 4 | concept:3/paper:1 |
| C306 | Community 306 | 3 | document:3 |
| C307 | Community 307 | 3 | document:3 |
| C338 | Community 338 | 3 | document:3 |
| C321 | Community 321 | 3 | document:3 |
| C330 | Community 330 | 3 | document:3 |
| C331 | Community 331 | 3 | document:3 |
| C339 | Community 339 | 3 | document:3 |
| C334 | Community 334 | 3 | document:3 |
| C310 | Community 310 | 3 | document:3 |
| C311 | Community 311 | 3 | document:3 |
| C312 | Community 312 | 3 | document:3 |
| C308 | Community 308 | 3 | document:3 |
| C309 | Community 309 | 3 | document:3 |
| C313 | Community 313 | 3 | document:3 |
| C314 | Community 314 | 3 | document:3 |
| C322 | Community 322 | 3 | document:3 |
| C323 | Community 323 | 3 | document:3 |
| C324 | Community 324 | 3 | document:3 |
| C325 | Community 325 | 3 | document:3 |
| C327 | Community 327 | 3 | document:3 |
| C328 | Community 328 | 3 | document:3 |
| C329 | Community 329 | 3 | document:3 |
| C336 | Community 336 | 3 | document:3 |
| C337 | Community 337 | 3 | document:3 |
| C332 | Community 332 | 3 | document:3 |
| C333 | Community 333 | 3 | document:3 |
| C326 | Community 326 | 3 | document:3 |
| C315 | Community 315 | 3 | document:3 |
| C316 | Community 316 | 3 | document:3 |
| C317 | Community 317 | 3 | document:3 |
| C318 | Community 318 | 3 | document:3 |
| C319 | Community 319 | 3 | document:3 |
| C320 | Community 320 | 3 | document:3 |
| C335 | Community 335 | 3 | document:3 |
| C46 | Pricing & Compliance Reasoning | 3 | concept:2/document:1 |
| C49 | Cost Guideline & Workflow | 3 | concept:2/document:1 |
| C51 | TICA Kemi Scope Decision | 3 | document:3 |
| C45 | TICA V2 Vendor Review Chain | 3 | concept:2/document:1 |
| C48 | TICA Vendor Evaluation Checkpoints | 3 | document:2/concept:1 |
| C53 | Marketing Prohibitions & M-Series | 3 | concept:2/document:1 |
| C47 | Layout Workflow L-1/L-7 | 3 | document:2/concept:1 |
| C52 | Compliance & Risk Guidelines | 3 | concept:2/document:1 |
| C355 | Community 355 | 2 | code:2 |
| C360 | Community 360 | 2 | document:2 |
| C361 | Community 361 | 2 | document:2 |
| C362 | Community 362 | 2 | document:2 |
| C363 | Community 363 | 2 | document:2 |
| C364 | Community 364 | 2 | document:2 |
| C365 | Community 365 | 2 | document:2 |
| C373 | Community 373 | 2 | document:2 |
| C374 | Community 374 | 2 | document:2 |
| C375 | Community 375 | 2 | document:2 |
| C376 | Community 376 | 2 | document:2 |
| C377 | Community 377 | 2 | document:2 |
| C378 | Community 378 | 2 | document:2 |
| C340 | Community 340 | 2 | document:2 |
| C359 | Community 359 | 2 | document:2 |
| C343 | Community 343 | 2 | document:2 |
| C341 | Community 341 | 2 | document:2 |
| C342 | Community 342 | 2 | document:2 |
| C344 | Community 344 | 2 | document:2 |
| C356 | Community 356 | 2 | document:2 |
| C357 | Community 357 | 2 | document:2 |
| C358 | Community 358 | 2 | document:2 |
| C366 | Community 366 | 2 | document:2 |
| C367 | Community 367 | 2 | document:2 |
| C372 | Community 372 | 2 | document:2 |
| C368 | Community 368 | 2 | document:2 |
| C345 | Community 345 | 2 | document:2 |
| C346 | Community 346 | 2 | document:2 |
| C347 | Community 347 | 2 | document:2 |
| C348 | Community 348 | 2 | document:2 |
| C349 | Community 349 | 2 | document:2 |
| C350 | Community 350 | 2 | document:2 |
| C351 | Community 351 | 2 | document:2 |
| C352 | Community 352 | 2 | document:2 |
| C353 | Community 353 | 2 | document:2 |
| C354 | Community 354 | 2 | document:2 |
| C369 | Community 369 | 2 | document:2 |
| C370 | Community 370 | 2 | document:2 |
| C371 | Community 371 | 2 | document:2 |
| C68 | Siemens Busbar Selection | 2 | document:1/concept:1 |
| C65 | Cooling Network Reference Architecture | 2 | code:1/concept:1 |
| C79 | Power Engineer & Power Zone | 2 | document:1/concept:1 |
| C67 | EXT-001 T2/T3 Deliverables | 2 | document:1/concept:1 |
| C69 | Risk R-3/R-4 Red Flags | 2 | document:1/concept:1 |
| C70 | BESS vs DG Selection (P-8) | 2 | document:1/concept:1 |
| C72 | Doc Tree / Process / Architecture | 2 | document:1/concept:1 |
| C66 | AI/Training & Compliance Agents | 2 | document:1/concept:1 |
| C76 | Gotion ESC480 BESS | 2 | document:1/concept:1 |
| C61 | Cost Methodology K-3 to K-6 | 2 | document:2 |
| C58 | Networking Concepts (N-Series) | 2 | document:1/concept:1 |
| C55 | TICA TAMFV430.3ALF5 Hybrid Chiller | 2 | document:1/concept:1 |
| C57 | 3rd Party List Cross-Reference | 2 | document:1/concept:1 |
| C56 | TriBranch Architecture Manifold | 2 | image:1/concept:1 |
| C64 | Cooling & Network Vendor Warnings | 2 | document:2 |
| C74 | TICA Hybrid Chiller PRD | 2 | concept:1/document:1 |
| C54 | PQTech Interview Content | 2 | document:1/concept:1 |
| C77 | Thermal Model & e-NTU RDHX | 2 | document:1/concept:1 |
| C60 | Compliance Officer Veto Power | 2 | document:1/concept:1 |
| C71 | Marketing Guidelines & Workflow | 2 | document:1/concept:1 |
| C78 | Risk R-7 Scalability | 2 | document:1/concept:1 |
| C73 | Layout Guideline Workflow | 2 | document:1/concept:1 |
| C62 | COOLING G-16 Checklist | 2 | document:1/concept:1 |
| C59 | DC45 Container Structural | 2 | document:1/concept:1 |
| C379 | Community 379 | 1 | code:1 |
| C80 | Document References & Citations | 1 | document:1 |
| C81 | Certifications & Reference Docs | 1 | document:1 |
| C86 | Layout L-7 Workflow | 1 | concept:1 |
| C84 | COOLING G-17/18/19 Warnings | 1 | document:1 |
| C85 | Marketing Workflow | 1 | concept:1 |
| C83 | Power Path FOG A/D Series | 1 | document:1 |
| C82 | Compliance C-3 BESS | 1 | document:1 |

---

## 维护

```bash
graphify update .                                    # AST-only 重建 graph
python3 .tools/gen_graph_index.py graphify-out       # 重新生成本表内容
```

- `graph.json` 变化时（添加/删除 KB 文档）→ 重生成 `graphify-out` → **重写本表**
- 新 community 若显示 `Community N` 占位名，可运行 `graphify label .`（需 LLM）命名

*Created: 2026-06-24 | Source: graphify-out/graph.json | Last Updated: 2026-08-30*

> **2026-08-30 更新：** 「怎么用」表的产品手册一行改为两条产品线 + 六 SKU 新码（六 SKU 全部 `shipped`，站点 `docs/PRODUCT-MATRIX.md` §5 D-19 gate · 2026-08-27）；全量 Community 表为机器生成，其中 18 处旧名标签**未手改**，已在表头加旧名↔新名对照说明，待重新打标后消除。
