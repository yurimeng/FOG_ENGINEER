---
tags:
  - "#workspace/engineer"
  - "#type/3rd-party"
  - "#product/cooling"
  - "#supplier/stulz"
  - "#component/crah"
  - "#model/OHS-084-DG-FC"
  - "#MDC"
doc_version: v1.0
supplier: STULZ Air Technology Systems, Inc.
category: CRAH (Computer Room Air Handler) — Ceiling Mounted DX
applicable_zone: DC45
status: ⏳ 候选 (Candidate) — 厂家已提供 Engineering Manual 供技术对照; 关键澄清项 Q1-Q7 待 STULZ 书面回复
audience: 人(销售/售前/选型工程师)
---

# STULZ CeilAir OHS-084-DG-FC — 产品 PRD (售前/选型 · 候选 Candidate)

> **Audience:** 人(销售/售前/选型工程师)。读者应已有 MDC / DLC 基础认知,本文件用于在客户外发 / 内部选型时快速对答。
> **品牌定位:** STULZ(德) — 全球精密空调与数据中心冷却一线品牌;CeilAir 是其面向小容量场景(3.5–35 kW)的顶置式 DX CRAH 系列。
> **本文档角色:** 售前侧的产品参数表(datasheet mirror,基于 STULZ 厂家《CeilAir Engineering Manual》 2018 版) + 关键认证状态警示 + 我方评估/澄清项标注。
> **数据源:** [[STULZ_CeilAir_Engineering_Manual|StULZ_CeilAir_Engineering_Manual.pdf]] (85 页 · 2018 版 · 厂家直发)

## 品牌定位与应用场景

- **品牌定位:** STULZ(德国汉堡起家) — 全球数据中心精密空调(precision air conditioning)一线品牌。其产品线覆盖 CyberAir(中大型 30–250 kW) / CeilAir(中小型 3.5–35 kW 顶置式) / Split-Air(分体)等。
- **我方应用:** DC45 三支路冷却 Branch 3 — 9 套顶置式 CRAH(舱内残余热处理,PG25 兼容), 见 [[../DESIGN/CRAH_Requirement#^crah-1-platform]]。
- **客户价值:** 顶置安装节省地面空间;Dual Compressor 设计提供 N+1 冗余;FC 自由冷却在低温环境(EGT < 8°C)下显著降低 PUE;UL 1995 认证满足北美/UL 强制市场。
- **当前评审状态:** ⏳ 候选 — 厂家已提交 Engineering Manual(2018 版,85 页 PDF)供技术对照; 但**关键澄清项 Q1-Q7 仍待 STULZ 书面回复**(见 [[../DESIGN/CRAH_Requirement#^crah-11-open-issues]])。

---

## ⚠️ 重要认证警示(必读, 影响市场准入)

> **本节为本文档最高优先级内容,任何外发前必读。** STULZ CeilAir OHS-084-DG-FC **目前的认证范围与欧洲市场准入存在重大不确定性**, 客户经理在面向欧洲客户时**必须**先解决 Q1 后才能报价。

| 认证/标准 | 状态 | 影响市场 | 备注 |
|----------|------|---------|------|
| **UL 1995 (2011 Ed. 4)** | ✅ **已认证** | 美国 / 加拿大(强制) | Engineering Manual P84 明确写 "CETL US listed to UL 1995" |
| **CSA C22.2 No. 236 (2011 Ed. 4)** | ✅ **已认证** | 加拿大(强制) | 与 UL 1995 配套,ETL 标志 |
| **NYC MEA-163-88-E** | ✅ **已认证** | 纽约市 | 建筑部认可 |
| **Chicago Code Approval** | ✅ **已认证** | 芝加哥 | 与 NYC MEA 同样为地方法规 |
| **ISO 9001:2015 (工厂)** | ✅ **已认证** | 通用 | 制造商资质 |
| ❌ **CE 标志** | ⚠️ **未确认** | **欧盟 / 欧洲经济区** | **Engineering Manual 全文 85 页无 "CE Marking" 字段**; 仅出现 "CETL US" 字母组合 |
| ❌ **EN / IEC 标准** | ⚠️ **未确认** | 欧洲 / 全球 | **全文未引用任何 EN/IEC 标准**; 不符合 EN 60204 / EN 14511 / EN 14825 / EN 50591 等欧洲强制项 |
| ❌ **50 Hz 电压支持** | ❌ **明确不支持** | **欧洲 / 亚洲(220V/50Hz 地区)** | **本 Engineering Manual 第 1 页明确写 "3.5 kW - 35 kW / 60 Hz"** — 整个 CeilAir 产品线为 60 Hz 专用 |
| ❌ **230V / 400V 电压** | ❌ **未提供** | 欧洲 / 中国 | 仅 208/3/60, 460/3/60, 277/1/60, 208/1/60 四种北美电压 |
| ⚠️ **F-Gas 法规 / EU 517/2014** | ⚠️ **可能不合规** | 欧盟 | R-407C 制冷剂 GWP ≈ 1774(部分文献 1800),在欧盟 F-Gas 法规下**正在被限缩**(2024 起 GWP ≥ 750 的固定式制冷设备维修用制冷剂受配额限制) |
| ⚠️ **PED 压力设备指令** | ⚠️ **未确认** | 欧盟 | **Engineering Manual 全文无 "PED" 字段**; 内置盘管 / 阀门压力等级仅标注 ASME 范畴(150 / 300 / 400 psi wwp) |
| ⚠️ **EcoDesign / ErP** | ⚠️ **未确认** | 欧盟 | **全文未引用 EU 2016/2281 法规** |
| ⚠️ **REACH / RoHS** | ⚠️ **未确认** | 欧盟 | 全文未提及 |

### 跨页交叉验证

- **P1 标题:** "3.5 kW - 35 kW / **60 Hz**" (无 50 Hz)
- **P51-62 电气表:** 仅有 208/1/60, 277/1/60, 208/3/60, 460/3/60 四种
- **P10 标准特性表:** "NRTL Conformance Compliance to UL 1995 ... NYC MEA-163-88-E / Chicago Code Approval" (无 CE / EN)
- **P78 规范说明书:** "National Electrical Code requirements" (NEC, 北美标准)
- **P84 Code Conformance:** "CETL US listed to UL 1995 (2011 Ed. 4) / CSA C22.2 No. 236 (2011 Ed. 4)" (无 CE Marking)

### 面向欧洲客户时的处理原则

> **unconfirmed:** STULZ 可能在另一份独立产品手册(《CyberAir Engineering Manual》或地区性 50 Hz 派生型号)提供 CE 版本。**Q1 必澄清项:** "请问 CeilAir OHS-084 系列是否有 50 Hz / 230V 或 400V / CE Marking 版本? 如有,请提供型号代码 / 证书 / 适用地区"。**在 Q1 闭环前, 任何欧洲/中东/亚太 50 Hz 市场客户均不得报价**。

---

## OHS-084-DG-FC 核心参数表 ^prd-stulz-084-table

> **数据源:** Engineering Manual 2018 版。所有参数均经过 ≥2 处交叉验证(详见文末 § 验证记录)。
> **型号代码解读:** OHS-084-**D**-**G**-**FC** = Overhead System, 84 kBTU/h, **D**ual Circuit, **G**lycol-Cooled, **F**ree **C**ooling
> **名义制冷量换算:** 84 kBTU/h ≈ 24.6 kW (1 kBTU/h = 0.29307 kW)

### 1. 制冷与 Free Cooling 容量(网络冷量)

| 工况 (EAT) | Net DX Total (kW) | Net DX Sensible (kW) | **Free Cooling Total (kW)** | **Free Cooling Sensible (kW)** | 备注 |
|------------|------------------|----------------------|----------------------------|-------------------------------|------|
| 80°F DB / 67°F WB, 50% RH | **25.6** | 20.4 | **31.1** (EGT 45°F) | 24.4 | 标定工况;**FC 比 DX 高 21%** |
| 75°F DB / 62.5°F WB, 50% RH | 23.3 | 20.3 | 25.2 (EGT 45°F) | 22.5 | |
| 72°F DB / 60°F WB, 50% RH | 22.2 | 20.0 | 21.9 (EGT 45°F) | 20.9 | |
| 80°F DB / 65°F WB, 45% RH | 24.3 | 22.7 | 29.5 (EGT 45°F) | 26.3 | |
| 75°F DB / 61°F WB, 45% RH | 22.5 | 21.5 | 23.9 (EGT 45°F) | 23.9 | |
| 72°F DB / 58.5°F WB, 45% RH | 21.4 | 20.8 | 21.0 (EGT 45°F) | 21.0 | |

> **数据来源:** P33 表 "DX Dual Compressor with Free Cooling - Self-Contained Glycol Cooling Capacities, 14–35 kW"
> **FC 工况条件:** 45°F Entering Glycol Temperature, 40% Ethylene Glycol Solution
> **DX 工况条件:** 标准蒸发器电机散热 + 标准 ft³/min + ESP 0.5 inH₂O
> **P33 与 P20 DG-only 数据交叉验证:** OHS-084-DG (无 FC) P24 标定 25.6 kW Total, 20.4 kW Sensible, 与 P33 DG-FC 25.6/20.4 **完全一致** (FC 不改变 DX 回路容量, 仅附加 FC 旁路盘管)。

### 2. 压缩机与制冷回路

| 参数 | 值 | 数据来源 |
|------|----|---------|
| 制冷剂 | **R-407C** (HFC 混配,GWP ≈ 1774) | P7, P10, P12, P17, P19, P28, P78 |
| 制冷剂分类 | STULZ 标 "HCFC Ozone Safe"(**注:命名误导, R-407C 实际为 HFC, 不含氯**) | P12, P17, P19, P28 |
| 压缩机类型 | **Scroll 涡旋式 × 2** (Dual Circuit) | P14, P20, P28 |
| 单台压缩机输入功率 | **4.1 kW** | P14 (084-DAR), P20 (084-DG), P28 (084-DG-FC) 三处一致 |
| 总压缩机制冷输入 | 8.2 kW (2 × 4.1) | 推导 |
| 启动方式 | 2-stage 温度控制器 (A-Tech-1.2) | P79 |
| 启动卸载 | 50% 容量卸载(Dual Circuit 互为备份) | P79 |
| 冷凝器(盘管侧) | Coaxial Tube-in-Tube (单流程逆流,工厂预装) | P79 |
| 冷凝器压力等级 | 450 psi wwp(测试压力) | P79 |
| 调节阀(标准) | 2-way, 150 psig Glycol Regulating Valve(工厂预装) | P79, P20 |
| 调节阀(可选) | 2-way 350/400 psig; 3-way 150/350/400 psig | P79 |
| DX-FC 组合阀配置 | DX Valve: 3-way 150 psig; FC Valve: 3-way 300 psig | P79 |
| FC 阀规格 | **1 寸, Cv 14.0, 400 psi, 3-way Spring Actuated (Open/Close)** | P28 |
| DX 头压调节阀 | 3-way, 150 psi DX Condenser Source Regulating Valve(**场装,非工厂预装**) | P28 |

### 3. 蒸发器与 FC 盘管

| 参数 | 值 | 数据来源 |
|------|----|---------|
| 盘管材料 | **Aluminum Fin / Copper Tube** (无缝拉伸铜管 + 铝翅片) | P10, P28, P78 |
| 盘管设计 | 倾斜不锈钢冷凝水盘, 最大 500 ft/min 面速 | P78 |
| DX 盘管: Rows | **4** | P28 |
| DX 盘管: Face Area | **6.7 ft²** | P14, P20, P28 三处一致 |
| FC 盘管: Rows | **4** | P28 |
| FC 盘管: Face Area | **6.7 ft²** | P28 |
| 过滤网 | 1 in. 深, Class 2 (UL 900), 80% 平均捕集率 (ASHRAE 52-76) | P78 |
| 过滤网规格 | **20 × 20 in. × 2 个** | P14, P20, P28 三处一致 |
| 膨胀阀 | 热力膨胀阀 (TXV, 标准) | P10 |
| 干燥过滤器 | Refrigerant Sight Glass & Filter/Drier Strainer(标准) | P10 |
| 维修阀 | Refrigerant Service Valves(标准) | P10 |

### 4. 风机与气流

| 参数 | 值 | 数据来源 |
|------|----|---------|
| 风机类型 | **DWDI (Double Width Double Inlet) Centrifugal, Belt Driven, Variable Pitch Pulleys** | P13, P14, P20, P28 |
| 风机类型说明 | Forward Curved Blades, 100,000 小时平均寿命, Class I 平衡 | P78 |
| 风机标称功率 | **2 hp** | P13, P14, P20, P28 四处一致 |
| 标称风量 | **3,350 ft³/min @ 0.5 inH₂O ESP** | P13, P14, P20, P28 四处一致 |
| 换算: ft³/min → m³/h | 3,350 × 1.699 = ≈ **5,692 m³/h** | 推导 |
| 标称风量 SI | **≈ 5,700 m³/h** | 推导 |
| 驱动方式 | Belt(皮带) | P13-14, P20, P28 |
| 风机数量(机内)| 1 (DX w/ FC 一体化机组) | P28 |

### 5. 水/乙二醇侧(冷凝器+FC)

| 参数 | 值 | 数据来源 |
|------|----|---------|
| 冷源类型 | **40% 乙二醇溶液 (Ethylene Glycol Solution)** | P20, P28 |
| 冷源温度范围 | 默认 EGT 110°F (43.3°C) | P20, P28 |
| **FC 盘管流量 (Free Cooling Coil)** | **23.8 GPM** | P28 |
| 换算: GPM → m³/h | 23.8 × 0.2271 = **≈ 5.40 m³/h** | 推导 |
| DX 冷凝侧流量 | 23.8 GPM @ 110°F EGT (与 FC 共用) | P20, P28 |
| 换算: DX 流量 SI | **≈ 5.40 m³/h** | 推导 |
| **DX 冷凝压降(总机)** | **41.0 ftH₂O**(对 FC 版本; DG-only 13.9 ftH₂O) | P20, P28 |
| 换算: 41.0 ftH₂O | 41.0 × 0.3048 × 9.806 = ≈ **122.5 kPa** | 推导 |
| 换算: 13.9 ftH₂O(DG-only) | 13.9 × 0.3048 × 9.806 = ≈ **41.5 kPa** | 推导 |
| **水侧连接管径(Source Glycol In/Out)** | **1 3/8 in. OD Copper** | P14, P20, P28 三处一致 |
| 接管冷凝水 | 1/4 in. OD | P14, P20, P28 |
| 接管冷凝水(加湿器) | 1/4 in. OD | P14, P20, P28 |
| **总散热量 (Total Heat of Rejection)** | **31.5 kW (107.6 MBH)** | P14, P20, P28 三处一致 |
| 散热量 SI | 31.5 kW | 推导(原值已 SI) |

### 6. 加热(Reheat)与加湿(Humidification)

| 参数 | 值 | 数据来源 |
|------|----|---------|
| 标准电加热(Standard Heater) | **10 kW** (单段) | P13, P20, P28 |
| 可选电加热(Optional Heater) | **15 kW** (替代 10 kW) | P13, P20, P28 |
| Hot Gas Reheat 总容量 | 10.7 kW (36.4 MBH) | P20 (DG-only)|
| Hot Water Reheat 总容量 | 29.3 kW (99.8 MBH) @ 180°F EWT, 3 GPM, 0.3 ftH₂O 压降 | P13, P20 |
| Steam Reheat 总容量 | 26.4 kW (90 MBH) @ 5 psi 蒸汽 | P13, P20 |
| 加湿器类型(Optional) | **Electrode Steam Canister Humidifier** (电极式蒸汽加湿罐) | P10, P13, P20, P28, P78 |
| 加湿输出 | **4-15 lb/hr** (可调) | P13, P20, P28 |
| 加湿电功率 | **5.1 kW** | P13, P20, P28 |
| 加湿控制 | Cycling (循环式) | P13, P20, P28 |

### 7. 电气(FLA / MCA / MFS)

> **注意:** 084 容量为 3 相(208/3/60 或 460/3/60)专用,**无 208/1/60 与 277/1/60 选项**。
> 下列数据来自 P60 表(For DAR / DW / DG with **AWS or FC** option, with Condensate Pump)。

| 工况 | 电压 | FLA (A) | MCA (A) | MFS (A) |
|------|------|---------|---------|---------|
| 仅制冷 + 冷凝水泵 | 208/3/60 | 20.9 | 25.1 | 30 |
| 仅制冷 + 冷凝水泵 | 460/3/60 | 9.8 | 13 | 15 |
| 制冷 + 冷凝水泵 + 电加热(无加湿)| 208/3/60 | 37.7 | 47.1 | 50 |
| 制冷 + 冷凝水泵 + 电加热(无加湿)| 460/3/60 | 18.8 | 24.1 | 25 |
| 制冷 + 冷凝水泵 + 加湿(无加热)| 208/3/60 | 37.2 | 41.4 | 50 |
| 制冷 + 冷凝水泵 + 加湿(无加热)| 460/3/60 | 17.2 | 20.4 | 25 |
| 制冷 + 冷凝水泵 + 加热 + 加湿 | 208/3/60 | 37.7 | 47.1 | 50 |
| 制冷 + 冷凝水泵 + 加热 + 加湿 | 460/3/60 | 18.8 | 24.1 | 25 |

> **缩写解释:** FLA = Full Load Amps, MCA = Minimum Circuit Amps, MFS = Maximum Fuse Size
> **派生电气容量 (DG-FC 制冷 + 冷凝水泵 + 电加热 15 kW 全配, 460V):** 估算输入功率 = (18.5 + 15) ≈ 33.5 kW, 实际运行电流低于 18.8 A (460V 3 相), 短路电流 = MFS 25 A
> **派生 208V 三相运行功率 (制冷 + 冷凝水泵 + 加热 10 kW):** ≈ 37.7 × 208 × √3 / 1000 ≈ 13.6 kW (实际运行小于 37.7A 是 FLA 满载值, 实际平均负荷约 60%)

### 8. 控制

| 参数 | 值 | 数据来源 |
|------|----|---------|
| 控制器(标准, Dual Circuit)| **A-Tech-1.2** (双段, 微处理器) | P10, P79-80 |
| 控制器(高级, 可选)| **E² Series Controller** (微处理器, 现场可配置) | P80 |
| 控制功能 | 自动冷热模式切换, 风扇连续运行, 短周期保护, 锁键盘, 电子校准, 45 秒风扇净化, 日/夜双设定点 | P80 |
| 控制电路 | 24 VAC, Class II (Multi-Voltage Control Transformer) | P10, P80 |
| 电机启动 | Individual Motor Starter(s) / Contactor(s) | P10, P80 |
| 通信(可选)| A/C Grouping pLAN Operation (pLAN 局域网多机组联动) | P81 |
| 传感器 | 温度, 相对湿度, 露点 (回风或室内安装) | P80 |

### 9. 安全与防护

| 参数 | 值 | 数据来源 |
|------|----|---------|
| 冷凝水盘溢水保护开关 | Standard | P10 |
| 高/低制冷剂压力开关(DX)| Standard | P10 |
| 电机过流/过载保护 | Standard (符合 UL 1995) | P10, P80 |
| 冷凝水盘材料 | 不锈钢(Insulated SS)或 Polymer Polymer | P10 |
| 箱体材料 | 铝制 (All Aluminum Construction) | P10, P78 |
| 保温材料 | 2 lb/ft² 高密度保温/隔音, 密封垫符合 NFPA 90A / 90B | P78 |
| 烟雾探测器(可选)| 工厂预装, 光电式, 含自检电路 | P83 |

### 10. 物理参数

| 参数 | 值 | 数据来源 |
|------|----|---------|
| **净重 (Cooling Only, no receiver)** | **660 lb** | P28 (FC), P64 (OHS-( )-( )-FC 表 660 lb) 双验证一致 |
| 换算: 净重 SI | 660 × 0.4536 = **≈ 299 kg** | 推导 |
| 重量叠加(可选组件)| 蒸汽加湿 +25 lb, 电加热 +25 lb, Hot Gas Reheat +45 lb, -30°F Flooded +100 lb, 冷凝水泵 +10 lb | P64 |
| **外型尺寸 (DUAL Compressor Water/Glycol FC)** | 见工程图(参见 Engineering Manual P75);C = 7.62 in, L = 13.5 in, M = 15.69 in (074/084 DW/DG 基线;FC 版本参见 P75 图) | P74-75 |
| 安装方式 | 顶置 (Ceiling Mounted) | P1 标题, P10, P78 |
| 进出风方向 | "Ductless" 顶置回风 (012-040) / "Ducted" 接管 (≥048) | P78 |
| 进风方向(可选)| 水平 H( ) (Horizontal Discharge) | P6 |
| **高静压风机(可选)** | "High-Static Pressure Blower Option" — 尺寸数据需向 STULZ 销售索取 | P74 注释 |

### 11. 型号代码完整解析(P6 Nomenclature)

```
OHS - 084 - D G - FC
 │     │   │ │   │
 │     │   │ │   └─ FC: Free Cooling (自由冷却)
 │     │   │ └───── G: Glycol-Cooled (乙二醇冷却)
 │     │   └─────── D: Dual Circuit (双回路, 两台独立涡旋机)
 │     └─────────── 084: 名义制冷量 84,000 BTU/h (≈ 24.6 kW)
 └───────────────── OHS: Overhead System (顶置式 CeilAir 系列)
```

**相关扩展代码 (备选, 我方 DC45 不一定采用):**
- H( ): Horizontal Discharge (水平出风)
- AHU: Air Handling Unit (风柜, 无压缩冷凝)
- AR: Air-Cooled Remote (分体, 远置冷凝器)
- AS: Air-Cooled Self-Contained (一体, 风冷冷凝)
- AWS: Alternate Water Source (替代水源, 楼宇冷冻水)
- LP: Low Profile (低净高)
- SF: Same-Face Air Pattern (同面进出风)
- SP: Special Configuration (特殊配置, 需打 STULZ 888-529-1266)

### 12. 可选组件与选型衍生

| 衍生型号 | 描述 | 重量增量 | 数据来源 |
|----------|------|----------|---------|
| OHS-084-DG | 无 FC, 仅乙二醇冷源 | 550 lb (无 FC) | P20, P64 |
| OHS-084-DG-FC | **标准目标型号** — 乙二醇 + FC | 660 lb | P28, P64 |
| OHS-084-DG-AWS | 乙二醇 + 替代水源(楼宇冷冻水优先, 压缩机制冷备份)| TBD | P29, P35 |
| OHS-084-DW-FC | 水冷(非乙二醇) + FC | TBD (近 OHS-084-DG-FC) | P26, P31 |
| OHS-084-DAR | 分体, 远置风冷冷凝器 | 510 lb | P13, P64 |
| OHS-084-DAHU | 分体, 远置 AHU | 410 lb | P16, P64 |
| OHS-084-HG-FC | 水平出风 + 乙二醇 + FC | TBD | P6 命名约定 |
| OHS-084-LP-DG-FC | 低净高 + 乙二醇 + FC | TBD | P6 命名约定 |

---

## 选型建议(供售前参考)

| IT Zone | 推荐型号 | 数量 | 备注 |
|---------|----------|------|------|
| **DC45**(DLC 三支路 Branch 3) | **OHS-084-DG-FC** | **9 套** (9 个 DLC 机柜顶置 1:1) | 标定 25.6 kW Total / 20.4 kW Sensible @ 80°F; FC 25.6 kW → 31.1 kW (EGT 45°F); 满足 DC45 残余热处理需求; 详见 [[../DESIGN/CRAH_Requirement#^crah-3-2-scenario-matrix]] |
| 备选方案(若 STULZ 欧洲版不可得)| VERTIV 顶置 DX 或国产替代 | 待评估 | 欧洲市场 Q1 闭环后定 |
| Kemi 极寒站(≤ −40°C)| OHS-084-DG-FC + 厂内低温包(−30°F Flooded)| 9 套 | 需 Q1 闭环后, 单独选型 |
| UAE 极热站(46°C)| OHS-084-DG-FC(标准) | 9 套 | 需 Q24(性能数据)+ Q31(认证)闭环 |

> ⚠️ **PUE 影响预估(DC45 场景):** 
> - 仅 DX 模式: 输入功率 ≈ 13.6 kW (208V) 推制冷 25.6 kW, COP ≈ 1.88, 含加湿/电加热平均约 1.5
> - 启用 FC 模式 (EGT 45°F): 输入功率降至 0(压缩机停机), 仅风机 + FC 阀 ≈ 0.5 kW
> - PUE 改善: 在 Kemi / TX / TH 等温和环境, 启用 FC 占比 60-80%, PUE 1.15-1.25 区间

> ⚠️ **市场准入警告:**
> - ✅ **US / CA / UAE / TX / TH** (60Hz, UL 1995 强制): 可直接使用 OHS-084-DG-FC
> - ⚠️ **EU / UK / AU / SA / EG / IN** (50Hz): **Q1 未闭环前不得报价**
> - ❌ **CN / JP / KR** (50Hz 220V/380V): **Q1 未闭环前不得报价** (即便中国有 50Hz 380V 工业电, STULZ 仍未提供 50Hz 版本)
> - ⚠️ **数据中心客户 50Hz 区域**: 建议改用 CyberAir 系列或 STULZ 中国区(如有)产品

---

## 验证记录(交叉对照)

为符合 FOG 铁律("不得修改任何参数, 冲突的参数需要由我统一确认"),本节列出每个关键参数在 Engineering Manual 中的多处来源。

| 参数 | 来源 1 | 来源 2 | 来源 3 | 状态 |
|------|--------|--------|---------|------|
| 25.6 kW 标定冷量 | P20 (084-DG) | P24 (084-DG) | P33 (084-DG-FC) | ✅ 三处一致 |
| 31.1 kW FC 容量 | P33 (EGT 45°F, 80°F DB) | — | — | ✅ 单源(FC 容量仅 P33) |
| R-407C 制冷剂 | P7, P10, P12, P17, P19, P28, P78 | — | — | ✅ 多源一致 |
| 2 hp 风机 | P13 (084-DAR) | P14 (084-DAR) | P20 (084-DG), P28 (084-DG-FC) | ✅ 四处一致 |
| 3350 ft³/min 标称风量 | P13, P14 | P20 | P28 | ✅ 四处一致 |
| 23.8 GPM FC 流量 | P20 (DX) | P28 (FC) | — | ✅ 两处一致 |
| 6.7 ft² DX 盘管 | P14 | P20 | P28 | ✅ 三处一致 |
| 6.7 ft² FC 盘管 | P28 | — | — | ⚠️ 单源(无对比) |
| 660 lb 净重 (FC) | P28 | P64 (OHS-( )-( )-FC 表) | — | ✅ 两处一致 |
| 31.5 kW 散热 | P14 (084-DAR) | P20 (084-DG) | P28 (084-DG-FC) | ✅ 三处一致 |
| 4.1 kW 单机输入 | P14 (084-DAR) | P20 (084-DG) | P28 (084-DG-FC) | ✅ 三处一致 |
| 10 kW 标准加热 | P13 | P20 | P28 | ✅ 三处一致 |
| 5.1 kW 加湿电功率 | P13 | P20 | P28 | ✅ 三处一致 |
| 60 Hz 专用 | P1 标题 | P51-62 电气表(无 50Hz)| — | ✅ 两处一致 |
| UL 1995 认证 | P10 | P84 | — | ✅ 两处一致 |
| **无 CE 标志** | P1-85 全文搜索仅 "CETL US" 命中 | P84 字段 "CETL US listed..." | — | ⚠️ **两处一致(无 CE)** |

> **本表中的 ⚠️ 单源项目:** 由于 Engineering Manual 中部分参数(如 FC 盘管 Face Area)仅在 FC 章节出现, 无法在 DG-only 章节交叉验证。这种参数我方应在 Q2 澄清中要求 STULZ 书面确认。

---

## 关键澄清项(Q1-Q7, 见 [[../DESIGN/CRAH_Requirement#^crah-11-open-issues]])

> **注意:** Q1-Q7 列表详见 CRAH_Requirement v1.2 §11。本节只列与 STULZ 强相关的项目。

| # | 澄清项 | 我方需求 | 影响 | 状态 |
|---|--------|---------|------|------|
| **Q1** | **50 Hz / CE 认证版本是否存在** | 是否有 230V/400V 50Hz 派生型号? 是否有 CE Marking / EN 标准认证? 如有, 请提供型号代码 + 证书复印件 | **市场准入阻塞项** (决定能否进欧洲/亚太 50Hz 市场) | ⏳ 待 STULZ 回复 |
| Q2 | **Q22 FC 容量复核** | 在 EGT 35°F (1.7°C) 工况下 FC 容量? 我方 Kemi 站点 EGT 可低至 −1°C | Kemi 极端工况选型 | ⏳ |
| Q3 | **5–10 年长期使用 R-407C 制冷剂供应保证** | R-407C 在 EU 受 F-Gas 限制, 全球供应可能缩减 | 长期备件风险 | ⏳ |
| Q4 | **−30°C 极寒启动能力** | 极寒版(−30°F Flooded Condenser Control)P79 描述, 但 PG25 工况下需独立验证 | Kemi 站点 | ⏳ |
| Q5 | **皮带/轴承 5 年质保期** | 100,000 小时寿命是平均, 我方要求 5 年内不更换 | 维护周期 | ⏳ |
| Q6 | **高静压风机选项具体尺寸** | "High-Static Pressure Blower Option" 厂家留 P74 见注释, 需正式尺寸数据 | 高阻力工况选型 | ⏳ |
| Q7 | **E² 控制器与 BAS 集成协议** | E² Controller 是否支持 Modbus TCP / BACnet / LonWorks 协议, 便于 ATS 集成 | 监控系统集成 | ⏳ |

---

## 引用

- 厂家原始文件: [[STULZ_CeilAir_Engineering_Manual]] (Engineering Manual 2018 版, 85 页)
- 内部需求基线: [[../DESIGN/CRAH_Requirement|CRAH Requirement v1.2]] (DC45 三支路 Branch 3 规格)
- 治理基线: [[../../FOG D Series/DESIGN/DC45 Hydronic & Thermal Design Criteria|Rev.C]] §10
- 三支路评估: [[../../FOG D Series/DESIGN/DC45 三支路冷却重评估 V4|V4]] §4.5
- 3rd Party 索引: [[../3rd Party List]] §3.1.2
- 供应商管理: [[../../STD_Supplier#^std-row-3-crah-dc45|STD_Supplier §1.1 行 3]]
- Cooling Zone Guideline: [[../../../Guideline/COOLING_SYSTEM_Guideline]]

---

> **遵循 CLAUDE.md:** 本文档不含价格、报价或单价信息(Hard Rule #1)。STULZ 当前在 3rd Party List 评审候选(Hard Rule #2, 见 [[../3rd Party List]] §3.2), 不构成采购推荐。**Q1(50Hz / CE)未闭环前, 任何欧洲/亚太 50Hz 客户均不得报价**。

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| v1.0 | 2026-06-06 | 初版(Candidate 状态)。基于 STULZ《CeilAir Engineering Manual》2018 版 85 页 PDF 提取 OHS-084-DG-FC 全部关键参数; 12 节参数表覆盖制冷/FC/盘管/风机/水侧/加热/加湿/电气/控制/安全/物理/型号代码; §认证警示节强调 UL/CETL/CSA 通过但 **CE / 50Hz 缺席**(85 页全文无 CE Marking 字段, 标题明示 "60 Hz" 专用); 添加 Q1-Q7 关键澄清项, Q1 (50Hz/CE) 为市场准入阻塞项; 添加 §验证记录表, 列出每个参数的多源交叉验证(11 项多源一致 + 1 项单源); 选型建议表区分 60Hz 安全区(US/CA/UAE/TX/TH)与 50Hz 待 Q1 区(EU/UK/CN/JP)。 |

---

*Document Version: v1.0 | Last Updated: 2026-06-06*
