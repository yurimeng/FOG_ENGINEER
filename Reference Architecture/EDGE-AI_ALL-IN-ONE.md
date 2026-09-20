---
tags:
  - "#workspace/engineer"
  - "#type/reference"
  - "#product/ac20"
  - "#product/i50ts"
  - "#MDC"
  - "#scenario/edge-ai"
  - "#cooling/immersion"
  - "#cooling/hybrid-chiller"
  - "#power/bess"
  - "#deploy/cn"
  - "#all-in-one"
---
# Reference Architecture — EDGE-AI ALL-IN-ONE (AC20 + Hybrid Chiller,国内部署) ^mdc-ce66352b2f

> 基于 [[RA-003_Immersion_0.2MW_All-in-One|RA-003]] AC20 浸没式 All-in-One 平台,套用 EDGE_AI A32x2 方案的国内部署模板 — 2×A32 + 沐曦 GPU 推理集群,Hybrid Chiller (TASFV-080.1AAF1, 262kW) 集成于 20ft 冷源框架,集装箱 + 框架整线交付,外部 BESS 供电,无 UPS,标准 PDC,沐曦 GPU + RoCE v2。 ^mdc-8b752d99d9

Reference Architecture Version: v1.0
Last Updated: 2026-07-12

变更摘要:初版。基于 RA-003 AC20 平台 (0.2MW IT 满配, 标配 100kW), 复用 EDGE_AI A32x2 v1.3 的 8×H3C R5500 G6 沐曦 GPU 算力配置, 切换冷源为 All-in-One 框架内置 Hybrid Chiller (无现场冷却施工), 国内 380V/220V 部署 + 外部 BESS + CCC 认证 + GB 消防规范。 ^mdc-fef6129084

---

## 1. 架构概述

| 项目 | 内容 |
|------|------|
| 部署地区 | 中国大陆 |
| 场景 | 边缘 AI 推理,中密度沐曦 GPU 集群,All-in-One 整线交付 |
| IT 容量 | **56kW**(8 × H3C R5500 G6,单台 ~7kW,OAM 8-GPU 模组) |
| 整体电力负荷 | ~76kW(IT 56kW + 辅助 20kW);冷源 77.7kW (Hybrid Chiller 满载,见 §5.2) |
| PUE | ~1.36(76kW IT Zone / 210kW Facility,含冷源满载;极端工况见 §8) |
| 产品形态 | **1 × AC20(20ft IT 集装箱)+ 1 × 20ft Hybrid Chiller Frame**(整线 ≈ 2 × 6.058m 拼接) ^mdc-34f8c2c5e1 |
| IT 主体 | **2 × A32 浸没机柜**(标配,T 排 2 槽),2 个 B 排扩展位预留 ^mdc-1239946d06 |
| 计算节点 | 8 × H3C UniServer R5500 G6 沐曦 GPU (8U,OAM 8-GPU 模组,液冷版) |
| 电源入口 | 外部 BESS → AC 380V / 50Hz,无 UPS |
| 二次配电 | PDC 配电箱 → 母线 → A32 内置 PSU → 服务器 PSU → rPDU 直连 ^mdc-f93a4ab519 |
| 网络 | 1 × 网络交换机柜(ToR ×2 + OOB ×1) |
| 散热 | **A32 内置 2N CDU(1+1 冗余)+ 20ft 框架内置 Hybrid Chiller(TASFV-080.1AAF1, 262kW)**;Hybrid 自然冷却 + 机械制冷一体, 环境 ≤25°C 全自然冷却 ^mdc-1ba076a865 |
| 残热 | A32 CDU 二次侧散热走 Hybrid Chiller;无独立壁挂(整线封闭) ^mdc-d4f7394d04 |
| 认证 | 分部件 CCC;整机无 UL/TUV 认证要求 |

> A32 来源见 [[MDC/PUBLIC/Products/_blocks/PRODUCTS_I50TS/01_Product_Position_And_Params|A32 Product Position + Core Params]]。AC20 平台见 [[RA-003_Immersion_0.2MW_All-in-One|RA-003 §4 产品配置]]。Hybrid Chiller 规格见 [[RA-003_Immersion_0.2MW_All-in-One#5.2 冷源侧(冷源框架)|RA-003 §5.2]] (TASFV-080.1AAF1, 262kW)。容器冷却见 [[COOLING_SYSTEM_Guideline#§G-12 容器冷却|§G-12]]。IT 负荷定义见 [[POWER_SYSTEMS_Guideline#§P-1 IT 负载定义|§P-1]]。 ^mdc-7c2cf884a2

---

## 1A. A32 浸没机柜简介 ^mdc-fe2e6e17c2

A32 是面向边缘 AI 与高密度 GPU 部署的单相浸没式液冷单机柜,标品 IT 容量推荐 45kW、最大 50kW,内部集成 2N 冗余 CDU(2 × 50kW),32RU / 29OU 容量,兼容 OCP 3.0 服务器。本方案采用 2 台 A32,提供总计 64RU 部署空间(2 × 32RU)。每台 H3C R5500 G6 为 8U 机型,单 A32 部署 4 台 8U 服务器,2 台 A32 共 8 台(满配,无富余空间;扩展需扩到 4 × A32)。 ^mdc-f10878c2fd

A32 详细参数见 [[MDC/PUBLIC/Products/_blocks/PRODUCTS_I50TS/01_Product_Position_And_Params|A32 Product Position + Core Params]]、[[02_Cabinet_Details|A32 Cabinet Details]]、[[04_Power_Path|A32 Power Path]]。 ^mdc-3b2a83a5d1

> **RFI 项:本方案按 R5500 G6 8U 机型(OAM 8-GPU 模组,液冷版)计算;若客户实际采购 6U 液冷副型,32RU 仍只放 4 台(32/6=5 槽,实际 4 台),部署结论不变。**

主要特性:

- 单相矿物油浸没(DC20 / S5LV,闪点 >170°C,非易燃)
- 二次侧(油):进油 ≤35°C,出油 ≈43°C,ΔT=8K
- 一次侧(水):进水 ≤32°C,出水 37°C,ΔT=5K
- 2N 冗余 CDU,各 Tank 内置,故障不中断运行
- 兼容 EIA 19″ / 21″ / OCP,最大服务器深度 1000mm
- 支持 Immersion-ready 服务器与改造风冷服务器
- A32 本体不含 UPS,需外部 PDC / BESS 接入(本方案采用外部 BESS) ^mdc-3e8fd6b913

![[透视图.702.png]]

![A32 浸没液冷机柜示意图(渲染图)](A32%20Flow.png) ^mdc-dc9a026be3

![A32 冷却流路原理图 v1(SVG 矢量)](A32%20Flow_v1.svg) ^mdc-3387db52be

---

## 1B. AC20 All-in-One 平台简介(预留图位) ^mdc-2a53d32c37

AC20 是 FOG 标品的 0.2MW 浸没式 All-in-One 单元:1 × 20ft IT 集装箱 + 1 × 20ft 冷源框架(内置 Hybrid Chiller),端对端拼接,整线交付。现场仅需接电接网,无冷却侧施工。 ^mdc-e144e5ade9

![[AC20_LAYOUT.PNG.png]]

**AC20 平台完整参数**(摘自 [[RA-003_Immersion_0.2MW_All-in-One|RA-003 §4 / §5]]): ^mdc-80e694655c

| 项目 | 参数 |
|------|------|
| IT 容量 | 200kW 满配(4 × 50kW A32 Tank 槽位) ^mdc-364e9a5331 |
| 标配 Tank | 2 × A32(T 排,各 50kW),2 个 B 排扩展位预留 ^mdc-e159436771 |
| 风冷辅助 | 48U 风冷机柜 × 1(网络/管理设备)|
| 配电 | PDC1 × 1(直供,**无内置 UPS**)|
| UPS | 无内置;可选外置(客户自备)|
| CDU | Tank 内置 Dual CDU(1+1 冗余)|
| 冷源 | 20ft 框架内置 **TASFV-080.1AAF1 Hybrid Chiller** |
| 管路 | 底部 DN100 环管,与 Chiller 水侧(DN125)直连 |
| 整线长度 | ≈ 2 × 6.058m(端对端拼接)|
| 整线重量 | ~12-13T(IT 集装箱 7-8T + Chiller Frame 5T)|
| 交付周期 | 首批 120 天 EXW / Scale 90 天 EXW；商务·运输·安装不承诺；假负载运行期 5–30 天|

**Hybrid Chiller (TASFV-080.1AAF1) 关键参数**(摘自 [[RA-003_Immersion_0.2MW_All-in-One#5.2 冷源侧(Hybrid Chiller,TASFV-080.1AAF1)|RA-003 §5.2]]):

| 项目 | 参数 |
|------|------|
| 制冷量 | IDC① 262kW / IDC② 283kW / GB 232kW |
| 制冷输入功率 | 77.7kW(IDC①),EER 3.37 |
| 100% 自然冷却温度 | 5°C(IDC①)/ 7.7°C(IDC②)(表列 IDC 低温水工况)|
| 压缩机 | 半封闭螺杆,变频启动,能量调节 25–100% |
| 制冷剂 | R134a,单回路 |
| 风机 | 6 台,总风量 135,000 m³/h |
| 蒸发器 | 高效满液式壳管(Flooded Shell-and-Tube)|
| 水流量 / 压降 | 44.6 m³/h / 78 kPa,接口 DN125,设计压力 1.0MPa |
| 尺寸 / 重量 | 4,220 × 2,250 × 2,560mm / 运输 4,822kg,运行 5,123kg |
| 供电 | **380V 3N~50Hz**,最大运行电流 **196A** |

> **暖水工况修正:** 表列 100% 自然冷却温度为 IDC 低温水工况。本方案 FWS 供水 31–33°C(暖水),实际 100% 自然冷却窗口大幅上移 — **环境 ≤25°C 全自然冷却, >28°C 机械制冷介入**(对齐 A32 Working Scenario)。 ^mdc-7150b20f4e

AC20 完整规格见 [[RA-003_Immersion_0.2MW_All-in-One|RA-003]]。 ^mdc-7731f91d4d

---

## 2. IT 负载 vs 整体电力负荷

| 项目 | 标配(2×A32)| 满配(4×A32)| 说明 ^mdc-4482f92062 |
|------|------------|------------|------|
| **IT 负载** | **56kW** | **112kW** | 8 / 16 × H3C R5500 G6(8U,OAM 8-GPU 模组,液冷版),单台 ~7kW |
| **IT Zone 辅助** | ~10kW | ~20kW | A32 CDU 一次侧循环泵 2N × 5kW ^mdc-277af1ea14 |
| **Hybrid Chiller 输入** | ~78kW(满载)| ~120kW(满载) | TASFV-080.1AAF1 IDC① 工况 EER 3.37,极端高温 35°C+ 时接近满载 |
| 残热(壁挂 / 维护)| 0kW | 0kW | 整线封闭,无独立壁挂 |
| 配电损耗 | 3–5kW | 5–8kW | PDC 主开关、母线压降 |
| 辅助(照明/监控/门禁)| 2kW | 2kW | — |
| **整体电力负荷** | ~149kW | ~259kW | IT Zone + 冷源 + 辅助 |
| PUE | ~1.36 | ~1.31 | 见 §8 PUE 参考 |

> **注 1:** 冷源输入功率随环境温度变化显著, §8 工况表给出 PUE 区间 (~1.05 全自然冷却 / ~1.36 满载机械制冷)。
> **注 2:** 与 EDGE_AI A32x2 单箱方案关键差异:本方案整线含 Hybrid Chiller,Facility 总负荷 = IT Zone + Chiller 输入, 而非仅 IT Zone;Chiller 输入受环境温度调节, 冬季低负载冬季 PUE 可达 ~1.05。

---

## 3. 计算架构

| 项目 | 参数 |
|------|------|
| 服务器 | H3C UniServer R5500 G6(**8U** 双路,支持 OAM 8-GPU 模组,液冷版) |
| GPU | 沐曦 C500 / C550(OAM 8-GPU 模组形式),以客户 RFI 为准 |
| 数量 | 标配 8 台(2 × A32 × 4 台/A32);满配 16 台(4 × A32 × 4 台/A32) ^mdc-0ab547d045 |
| 单服务器功耗 | ~7kW(8 × 沐曦 GPU ~600W + 双路 CPU + 内存 + NVMe + 风扇假设) |
| 机位空间 | A32 提供 32RU / 29OU,**8U × 4 = 32RU, 2 柜满配无富余**;扩展至 4 × A32 时启用 B 排预留位 ^mdc-6d2aef86a2 |
| 兼容性 | R5500 G6 液冷版自带冷板 + 漏液检测,入浸没仍需 OEM 改造(去风扇、换浸没 PSU 接头、PCB 三防涂覆),改造量小于风冷版 |
| 网络 | 每台 1 × 25G/100G NIC(业务 + 互联)+ 1 × 1G BMC(HDM 专用,RJ45,缺省 IP 192.168.1.2/24) |
| PCIe | 4 或 8 个 PCIe 5.0 x16 槽位(网卡转接模块),每槽 75W |
| OCP | OCP 3.0 网卡槽位 × 1 |
| 内存 | DDR5,32 DIMM,最多 12TB |
| BMC | 新华三 HDM(Redfish / IPMI / SNMP) |
| 散热 | N+1 风扇冗余;CPU/GPU 液冷模块带进水/出水/漏液检测快接头 |

H3C R5500 G6 出厂有风冷和液冷两个版本,本方案需采购**液冷版**(8U 液冷机型),入 A32 浸没前再走 OEM 改造。RFI 必须先回:客户是否已采购液冷版、是否接受浸没改造、改造责任在谁。 ^mdc-18740caece

> **数据来源:** H3C UniServer R5500 G6 技术白皮书 v1.0(2025 新华三技术有限公司)。R5500 G6 为 8U 旗舰 AI 服务器,机箱高度支持 8U 和 6U;8U 机型支持风冷和液冷,6U 机型仅支持液冷;OAM 8-GPU 模组是标准 GPU 配置形式。

---

## 4. 箱体布局

```
┌──────── 20ft IT 集装箱 (6,058 × 2,438 × 2,896mm) ────────┐    ┌── 20ft Hybrid Chiller Frame (6,058 × 2,438 × 2,896mm) ──┐
│                                                          │    │                                                            │
│  ┌── A32 #1 ──┐    ┌── A32 #2 ──┐    ┌─ 风冷辅助 ─┐    │    │  ┌── TASFV-080.1AAF1 Hybrid Chiller ──┐  ┌─ 膨胀罐/阀门 ─┐ │ ^mdc-8aa0591c53
│  │  32RU/29OU │    │  32RU/29OU │    │  48U 风冷  │    │    │  │  半封闭螺杆变频,R134a,262kW      │  │  200L + 蝶阀  │ │
│  │  4×H3C     │    │  4×H3C     │    │  机柜 ×1   │    │    │  │  6 × EC 轴流风机,135,000 m³/h  │  │  DN125 水侧    │ │
│  │  R5500 G6  │    │  R5500 G6  │    │  (网络/    │    │    │  │  DN125 / 1.0 MPa / 380V/196A    │  │                │ │
│  │  沐曦 GPU  │    │  沐曦 GPU  │    │   管理设备)│    │    │  │  4,220 × 2,250 × 2,560mm        │  │                │ │
│  │  ↑2N CDU   │    │  ↑2N CDU   │    │            │    │    │  │  4822kg 运输 / 5123kg 运行     │  │                │ │
│  │  DC20/S5LV │    │  DC20/S5LV │    │            │    │    │  └──────────────────────────────────┘  └────────────────┘ │
│  └────────────┘    └────────────┘    └────────────┘    │    │                                                            │
│                                                          │    │  维护通道(单侧 600mm) + 控制柜 + 接电接网接口              │
│  ┌─ PDC 主柜 ────────────────────────────────────────┐   │    │                                                            │
│  │  ACB 400A + 4×100A + 32A + 16A + 10A MCCB + SPD  │   │    │                                                            │
│  └────────────────────────────────────────────────────┘   │    │                                                            │
│                                                          │    │                                                            │
└──────────────────────────────────────────────────────────┘    └────────────────────────────────────────────────────────────┘
```

| 区域 | 内容 | 备注 |
|------|------|------|
| **前 20ft IT 集装箱** | 2 × A32(标配,T 排)+ 1 × 48U 风冷机柜(网络/管理设备)+ 1 × PDC 主柜 | 整机重 ~7-8T;前后舱之间无隔板(整舱统一) ^mdc-e52af03c93 |
| **后 20ft Hybrid Chiller Frame** | TASFV-080.1AAF1 Hybrid Chiller + 200L 膨胀罐 + DN150 蝶阀组 + 控制柜 | 重 ~5T;一次侧水力预连,DN125 进出水法兰外接客户管网 |
| 端门 | 前后各 1 端门 | 双出口,符合国内消防规范 |
| 维护通道 | IT 集装箱单侧 600mm / Chiller Frame 单侧 600mm | — |
| 总重 | 整机 ~12-13T(含 IT 集装箱 7-8T + Chiller Frame 5T) | 远低于 40ft 16T 上限 |

> **与 EDGE_AI A32x2 v1.3 关键差异:** ① 单 20ft IT + 单 20ft Chiller Frame 替代 40ft HC 双 20ft 拼接;② 无独立 5kW 壁挂,残热全部由 A32 CDU + Hybrid Chiller 带走;③ 现场仅需接电接网,无冷却施工。 ^mdc-d79dfdbe4f

AC20 端对端拼接细节、Hybrid Chiller 安装位、进出水法兰 / 电源进线口标注由补充图例提供(见 §1B 预留图位)。 ^mdc-f20e8612e5

---

## 5. 暖通空调

### 5.1 浸没侧(IT Zone, AC20 前舱) ^mdc-74e5ee14c0

| 项 | 参数 |
|----|------|
| 一次侧(水) | 进水 ≤32°C,出水 37°C,ΔT=5K |
| 二次侧(油) | 进油 ≤35°C,出油 ~43°C,ΔT=8K |
| 散热量 | 2 × A32 = 90kW(标品工况);满配 4 × A32 = 180kW ^mdc-e3a1bfc104 |
| CDU | 2 × 50kW,2N 冗余,Tank 内置 |
| 冷却液 | DC20 / S5LV(单相矿物油,S5LV 比热 2.306 kJ/kg·℃) |
| 一次侧水力 | 底部 DN100 环管,接 Hybrid Chiller DN125 水侧(降径异径接头) |

### 5.2 冷源侧(后 20ft Hybrid Chiller Frame,TASFV-080.1AAF1)

> 完整规格见 [[RA-003_Immersion_0.2MW_All-in-One#5.2 冷源侧(Hybrid Chiller,TASFV-080.1AAF1)|RA-003 §5.2]],此处只摘关键项。

| 项 | 参数 |
|----|------|
| 型号 | TICA TASFV-080.1AAF1 |
| 制冷量 | IDC① 262kW / IDC② 283kW / GB 232kW |
| 制冷输入功率 | 77.7kW(IDC①),EER 3.37 |
| 100% 自然冷却温度 | 5°C(IDC①)/ 7.7°C(IDC②)(表列 IDC 低温水工况) |
| 压缩机 | 半封闭螺杆,变频启动,能量调节 25–100% |
| 制冷剂 | R134a,单回路 |
| 风机 | 6 台,总风量 135,000 m³/h |
| 蒸发器 | 高效满液式壳管(Flooded Shell-and-Tube) |
| 水流量 / 压降 | 44.6 m³/h / 78 kPa,接口 DN125,设计压力 1.0MPa |
| 尺寸 / 重量 | 4,220 × 2,250 × 2,560mm / 运输 4,822kg,运行 5,123kg |
| 供电 | **380V 3N~50Hz**,最大运行电流 **196A** |

> **暖水工况说明:** 表列 100% 自然冷却温度为 IDC 低温水工况(出水 7°C 量级)。本方案 FWS 供水 31–33°C(暖水), 实际 100% 自然冷却窗口大幅上移: **环境 ≤25°C 可全自然冷却, >28°C 机械制冷介入**(对齐 A32 Working Scenario 与 [[RA-003_Immersion_0.2MW_All-in-One#5.2 冷源侧(冷源侧 Hybrid Chiller,TASFV-080.1AAF1)|RA-003 §5.2]])。 ^mdc-1d2cf89cb3

### 5.3 一次侧水温工况

| 工况 | 环境 | Chiller 模式 | 一次侧进水 | 二次侧(油)进/出 | 备注 |
|------|------|--------|----------|----------------|------|
| 全自然冷却 | ≤25°C | 风机运行,压缩机停 | ~自然(≈环境+5°C) | 30°C / 38°C | PUE ~1.05 |
| Hybrid 部分负载 | 25–35°C | 变频压缩机 25–80% | 30–32°C | 33–35°C / 41–43°C | PUE ~1.15–1.25 |
| 机械制冷主导 | >35°C | 压缩机 80–100% | 32–35°C | 35–38°C / 43–46°C | PUE ~1.25–1.36 |

### 5.4 冷量匹配

| 配置 | IT 负载 | Chiller 能力 (IDC①) | 裕度 |
|------|--------|---------|------|
| 标配 2×A32 | 56kW | 262kW | **~370%**(显著过配, 留扩展) ^mdc-149f579129 |
| 满配 4×A32 | 112kW | 262kW | ~135% ^mdc-ebabe4bac3 |
| 满配 4×A32 + 极端高温 35°C+ | 112kW | 262kW | ~135% ^mdc-57b68eef93 |

> **裕度充裕**: 实际 IT 负载 56kW 远低于 Chiller 262kW 能力, 全年绝大多数时段为部分负载运行, PUE 受益于 Hybrid 变频特性显著优于满载工况。

---

## 6. 电力

### 6.1 电源拓扑

```
外部 BESS(客户供,AC 380V / 50Hz)
  → 整线主进线(3φ 380V / 50Hz,国标 TN-S)
       │
  ┌────┴────────────────────────────┐
  │                                 │
  ▼                                 ▼
IT 集装箱 PDC ACB 400A           Hybrid Chiller Frame 控制柜(独立回路,MCCB 250A → Chiller 196A)
  │                                 │
  ┌────┴──┐                          │
  │       │                          │
  ▼       ▼                          ▼
A32 #1 PSU  A32 #2 PSU         TASFV-080.1AAF1 ^mdc-a4cc3c9678
2N 独立      2N 独立           (半封闭螺杆变频)
  │       │                          │
  ▼       ▼                          ▼
4×H3C    4×H3C                6×EC 轴流风机 + 压缩机
R5500 G6 R5500 G6              + 板换 / 油加热器
  ▲                              ▲
  │(AC 220V 单相 / 50Hz)         │(AC 220V 单相 / 50Hz,控制)
  │                              │
PDC MCCB 32A                 Chiller 控制柜分路
  - 网络交换机柜
  - 照明/门禁
```

IT Zone 不含 UPS,见 [[04_Power_Path|A32 Power Path]] 走 `INPUT → PDC → UPS(可选) → A32 → IT`。本方案 BESS 直供 PDC,跳过 UPS。 ^mdc-23ae98d1e9

Chiller 独立供电回路(IT 与 Chiller 分路, 便于 Chiller 维护时单独断电, 不影响 IT)。

SPOF 风险得说清楚:无 UPS,BESS 故障或维护时 IT 直接断电。客户已确认接受(外部 BESS 自带模块冗余),所以这条按 R-3 走红线但不上报,签收即可。Hybrid Chiller 单机无冗余(冷量裕度充分,见 §5.4)。

### 6.2 总电力清单(校核)

| 负载 | 数量 | 单台 | 小计 |
|------|-----|------|------|
| **IT Zone** | | | |
| H3C R5500 G6(OAM 8-GPU 模组) | 8 | 7kW | **56kW** |
| A32 浸没 CDU(2N 一次侧泵)| 2 | 5kW | 10kW ^mdc-aa96027333 |
| 风冷辅助机柜(网络/管理)| 1 | 1kW | 1kW |
| **IT Zone 小计** | — | — | **~67kW** |
| **冷源侧** | | | |
| Hybrid Chiller 输入(IDC① 满载)| 1 | 77.7kW | 77.7kW |
| 冷源控制柜 + 阀门 / 传感器 | 1 | 0.5kW | 0.5kW |
| **冷源侧 小计** | — | — | **~78kW** |
| **辅助** | | | |
| 网络交换机(2 ToR + 1 OOB)| 3 | 0.5kW | 1.5kW |
| 监控 / 门禁 / 照明 | — | — | 0.5kW |
| 配电损耗 | — | — | 3kW |
| **辅助 小计** | — | — | **~5kW** |
| **合计(满载工况)** | — | — | **~150kW** |
| **合计(自然冷却工况, Chiller 风机运行 ~3kW)** | — | — | **~75kW** |

> **校核:** 满载(极端高温 + IT 满配) ~150kW,典型自然冷却(冬季) ~75kW,波峰比 2:1。BESS 容量按 150kW × 1h = 150kWh 备电设计;30 分钟备电只需 75kWh。3rd Party List §4.4 候选:国轩 ESC480-125P261-UL(125kW/261kWh 一柜)可覆盖 150kW/150kWh 备电需求。

### 6.3 IT 集装箱 PDC(国标)

| 项 | 参数 |
|----|------|
| 主开关 | ACB 400A / 3P / 380V(进线) |
| 出线 | 4 × MCCB 100A / 3P → 2 台 A32 各 2 路(2N PSU) ^mdc-a9f8bd9a8d |
|  | 1 × MCCB 32A / 3P → 风冷辅助机柜(单相 220V 由三相 380V 引出 N 线)|
|  | 1 × MCCB 16A / 1P → 网络交换机(220V)|
|  | 1 × MCCB 10A / 1P → 照明/门禁(220V)|
| 母线 | 铜母线 200A / 镀锡,简化版 |
| 防雷 | Type 1 + Type 2 SPD(BESS 端配置,符合 GB 50057) |
| 接地 | TN-S,接地电阻 ≤4Ω,集装箱外壳双接地点,符合 GB 50065 |
| 电压 | AC 380V / 220V,3 相 5 线,50Hz,国标 |

### 6.4 冷源框架配电

| 项 | 参数 |
|----|------|
| 主开关 | MCCB 250A / 3P / 380V(独立进线回路) |
| 出线 | 1 × MCCB 250A / 3P → Hybrid Chiller(196A 最大,留 25% 余量)|
|  | 1 × MCCB 16A / 1P → 冷源控制柜辅助(220V)|
| 防雷 / 接地 | 与 IT 集装箱共用接地网格,符合 GB 50057 / GB 50065 |

冷源独立供电回路便于:① 冷源维护时单独断电,不影响 IT;② 冷源侧电能计量独立核算(便于 PUE 分项统计);③ BESS 母线分路管理简化。

---

## 7. 网络

### 7.1 架构

```
                          ┌──────────────────────────────┐
                          │   网络交换机柜(IT 集装箱内)    │
                          │                              │
                          │  [SW-ToR-1]    [SW-ToR-2]    │  25G/100G ToR
                          │  业务+互联       业务上行      │  (MLAG 配对)
                          │                              │
                          │  [SW-OOB]                    │  1G 带外管理
                          │  BMC/IPMI 独立走线            │
                          └──────────────┬───────────────┘
                                         │
     ┌───────────────────────────────────┼────────────────────────────────┐
     │  8 × H3C R5500 G6(2 × A32 内)                                          │ ^mdc-b8764ea2f8
     │  每台: 1 × 25/100G NIC → ToR-1+ToR-2 (LACP)                            │
     │        1 × 1G BMC → OOB                                                 │
     └────────────────────────────────────────────────────────────────────────┘
```

| 项 | 配置 |
|----|------|
| 接入层 | 2 × 25G/100G ToR,MLAG 配对,无单点 |
| 上行 | 客户站点外部交换机 / 出口路由器(客户供,本方案不含) |
| 带外(OOB) | 1 × 1G 独立管理交换机,8 × BMC + 1 × 上行 |
| 互联 | RoCE v2 / 100G(沐曦 GPU 集群),要 IB 见 §7.3 |
| 布线 | 25G AOC / 100G DAC / OM4,走 A32 顶部桥架出舱 ^mdc-79f18e9f8b |

### 7.2 BMC / IPMI

每台 H3C R5500 G6 配 1 × 1G BMC,独立 NIC,不跟业务 NIC 共用物理端口。OOB 交换机上行经独立光模块/光纤连客户 OOB 网络。

### 7.3 InfiniBand 选项

要 IB 的话:2 × Quantum-2 / QM8700 替 ToR 交换机,上行 NDR 400G 接客户外部 IB 脊。详见 [[NETWORK_Guideline#§N-4 IB 设计|§N-4]]。本方案默认 RoCE v2 / 100G,IB 升级走 ATS 评审。

---

## 8. 监控

| 项 | 参数 |
|----|------|
| 协议 | PLC + MODBUS RTU/TCP + SNMP v3 + Web(HTTPS) |
| A32 CDU | 进/出油温、一次侧进/出水、CDU 状态、漏油、液位 ^mdc-a180eee4b4 |
| Hybrid Chiller | 进/出水温度、环境温度、压缩机状态、风机状态、EER、SOC、告警 |
| BESS | SOC、SOH、充放电、告警(BESS 端自有 BMS,整线侧只读)|
| 环境 | IT 集装箱 / 冷源框架 温湿度、烟感(ASSD)、门禁 |
| 上行 | 客户 DCIM / 监控中心(客户供接口) |

协议参考 [[MDC/PUBLIC/Tech_Spec/_blocks/L1240C45_Tech_Spec_CN/14_Sec14_Summary|DC45 §14]]。本方案简化版,不上完整 PLC 集成。 ^mdc-d3bc3f3569

### 8.1 PUE 参考

| 环境条件 | Chiller 运行模式 | PUE 参考值 |
|----------|---------|-----------|
| 环境 <25°C | 100% 自然冷却(风机运行)| ~1.05 |
| 环境 25–35°C | Hybrid(自然冷却+压缩机部分负载)| ~1.15–1.25 |
| 环境 >35°C | 机械制冷主导(EER 3.37,接近满载)| ~1.25–1.36 |

场地气候校验对照:[[MDC/Reference Architecture/Site_Reference_Climate_Standard]]

---

## 9. 消防 / 安防(国内规范)

| 项 | 配置 |
|----|------|
| 浸没舱烟感 | ASSD 空气采样 1 套(浸没油不燃,但电气连接点 / PSU 仍要探) |
| 冷源框架烟感 | 离子式 1 个 |
| IT 集装箱灭火 | FM-200(HFC-227ea)或 NOVEC 1230 瓶组,按 IT 集装箱容积选 |
| 冷源框架灭火 | 手提干粉灭火器 × 2,不上管网 |
| 手动释放 | IT 集装箱外侧 1 按钮 + 声光报警 |
| 紧急出口 | 前端门 + 后端门(冷源框架端门可作维护出口,非应急),双出口 |
| 接地 | 整线外壳 + 内部等电位网格,接地电阻 ≤4Ω,符合 GB 50065 |
| 门禁 | 读卡器 + 电控锁,前后端门共用 |
| 规范依据 | GB 50016 建筑设计防火规范 / GB 50116 火灾自动报警系统设计规范 / GB 50057 建筑物防雷设计规范 |

浸没油闪点 >170°C,非易燃液体,按一般电气火灾配 FM-200 就行,不用满覆盖。整机不要求 UL/TUV 认证,分部件 CCC 即可。

---

## 10. 合规 / 风险 / RFI

### 10.1 合规

| 项 | 状态 |
|----|------|
| 整机 UL / TUV | **不适用**(国内部署) |
| 分部件 CCC | 主要电气部件(开关/PDU/BESS/Chiller/壁挂/交换机)须 CCC 认证,客户验收 |
| BESS | 须满足国内储能规范(GB/T 36276 电力储能用锂离子电池等);客户自备 BESS 要给认证 |
| Hybrid Chiller | TICA TASFV-080.1AAF1,分部件 CCC;整机无需 UL/TUV |
| 消防 | GB 50016 / GB 50116 |
| 防雷接地 | GB 50057 / GB 50065 |

### 10.2 风险

| ID | 等级 | 风险 | 缓解 |
|----|------|------|------|
| R-1 | High | BESS 故障无 UPS 兜底,直接断电 | BESS 模块冗余,客户已接受 |
| R-2 | Medium | H3C R5500 G6(8U)入浸没需 OEM 改造 | RFI 提前确认;液冷版改造量小于风冷版 |
| R-3 | Medium | Hybrid Chiller 单机无冗余 | 冷量裕度 ~370%(标配)/ ~135%(满配);自然冷却窗口期可纯干冷器运行 |
| R-4 | Low | 浸没油泄漏风险 | 集液盘 + 漏油检测 + 定期巡检 |
| R-5 | Low | 20ft 封闭舱 egress 限制 | 双出口 + 互锁门 |
| R-6 | Low | 150kW facility PUE 1.36 偏高(满载工况) | 仅极端高温短时,典型 PUE 1.15–1.25 |
| R-7 | Low | R134a 冷媒 AIM Act 风险(若客户后续出口)| 国内部署无影响;若 R134a 限用升级 R513A,需重新校验冷量 |

### 10.3 RFI 清单

1. 站点位置 → 历史最高干球温度(决定 Chiller 选型与 PUE 预期)
2. H3C R5500 G6 是 Immersion-ready 出厂版,还是风冷出厂要改
3. BESS 品牌 / 备电时长 / 是否客户自备
4. 网络:RoCE 还是 IB?100G 上行?
5. 沐曦 GPU 型号(C500 / C550)及单台 GPU 数(影响单服务器功耗)
6. BESS 输出电压(380V / 400V)与频率(50Hz)
7. 站点海拔 / 气候极端值(影响 Chiller 选型)
8. 是否预留扩容至 4 × A32 满配 112kW(影响冷源裕度评估) ^mdc-6343f5a473

---

## 11. BoM(不含价格)

| # | 项 | 数量 | 备注 |
|---|----|------|------|
| 1 | 20ft IT 集装箱(AC20 前舱,含端门、保温、桥架)| 1 | 含 2 × A32 槽位 + 风冷辅助机柜位 + PDC 主柜位 ^mdc-df41b011e0 |
| 2 | A32 浸没机柜(含 2N CDU、DC20、S5LV 备油)| 2 | 标配(T 排),扩展预留 2 位 ^mdc-e580fc74dd |
| 3 | 20ft Hybrid Chiller Frame(后舱,含 TASFV-080.1AAF1 + 200L 膨胀罐 + DN150 蝶阀组 + 控制柜)| 1 | 冷源整框架交付,现场仅接电接网 |
| 4 | H3C UniServer R5500 G6(沐曦 GPU)| 8 | 客户供或代采,待 RFI |
| 5 | 标准 rPDU(24 × C13 + 6 × C19)| 8 | 1 台/服务器,直连 PSU |
| 6 | PDC 主配电柜(ACB 400A + 4×100A + 32A + 16A + 10A MCCB + SPD,国标 380V/220V)| 1 | 客户原话"仅含标准配电箱" |
| 7 | 冷源框架独立配电柜(MCCB 250A + 16A,国标 380V/220V)| 1 | 冷源独立回路 |
| 8 | 铜母线 200A / 镀锡 | 1 套 | 简化版 |
| 9 | 网络交换机柜(600×1000×2000,2 ToR + 1 OOB)| 1 | 交换机型号客户定或代采 |
| 10 | 消防:ASSD + FM-200 + 声光 + 手动按钮 + 干粉 × 2 | 1 套 | 符合 GB 50016 / GB 50116 |
| 11 | 门禁 + 监控 PLC + 温湿度 + 烟感 + 漏水 | 1 套 | 跟客户 DCIM 对接 |
| 12 | 接地 / SPD / 桥架 / 线缆 / 标识 | 1 套 | 符合 GB 50057 / GB 50065 |

外部 BESS + BESS 母线接入不在 BoM 范围。客户已确认外置,本方案只出整线进线主开关 + 接驳铜排。

---

## 12. 上报结论

按 [[Risk_Guideline]] 红线规则:

- §R-3 SPOF(BESS 故障即 IT 断电):客户已签收,不上报
- §R-4 IT vs Total 负荷澄清:已澄清(满载 150kW = Total;IT 56kW = 8×H3C R5500 G6)
- §G-18 Hybrid Chiller 强制 / 干冷器判据:已说明,RFI 待回
- §C-5/C-6 容器合规:已评估(双出口 + 简化消防 + GB 50016/50116)
- §N-11 网络禁止:已遵守(OOB / 业务物理分离)

---

## 13. 扩展路径:2 × A32 → 4 × A32 ^mdc-210ca4a471

本方案默认 2 × A32(IT 56kW / Chiller 262kW)。当客户算力需求增长需要扩展到 4 × A32(IT ~112kW)时,启用 AC20 B 排预留位即可: ^mdc-3bb48544c2

| 项 | 默认 2 × A32 | 扩展 4 × A32 ^mdc-323aa011fb |
|----|------------|--------------|
| A32 数量 | 2(T 排)| 4(T + B 排) ^mdc-b566e95481 |
| H3C R5500 G6 数量 | 8 | 16 |
| IT 容量 | 56kW | 112kW |
| Hybrid Chiller 裕度 | ~370% | ~135% |
| Chiller 满载输入 | 77.7kW | ~120kW(满载) |
| Facility 满载 | ~150kW | ~260kW |
| 壁挂 / 维护 | 0kW | 0kW |
| PDC 主开关 | ACB 400A | ACB 400A(无需升级) |
| 网络 ToR | 2 台(MLAG)| 2 台(MLAG,无需升级)|
| 交付周期(扩容)| — | ~30–45 天(现场吊装 + 支管接入) |
| 适用场景 | 客户已部署 2 × A32,算力增长可见 | — ^mdc-46cf101320 |

> **推荐:** 若客户算力增长可见但目标 ≤ 0.2MW,选 AC20 内部扩展(T+B 排),无需更换框架,Chiller 裕度充分。若客户算力增长 >0.2MW,升级 [[RA-001_Immersion_0.4MW|RA-001 (0.4MW, AC40)]] 或 [[RA-002_Liquid_1.2MW|RA-002 (1.2MW, DC45)]]。 ^mdc-52bcda99bb

---

## 14. Changelog

- **v1.0 (2026-07-12)** — 初版。套用 [[RA-003_Immersion_0.2MW_All-in-One|RA-003]] AC20 + Hybrid Chiller (TASFV-080.1AAF1) All-in-One 平台,复用 EDGE_AI A32x2 v1.3 的 8×H3C R5500 G6 沐曦 GPU 配置。整线 1 × 20ft IT + 1 × 20ft Hybrid Chiller Frame, 现场仅需接电接网,无冷却施工。国内 380V/220V 部署 + 外部 BESS + CCC + GB 消防规范。Facility 满载 ~150kW (典型 ~75kW), PUE 区间 1.05–1.36 (随环境温度)。预留 AC20 整线外观图位(用户后续补充),保留 A32 浸没机柜图(渲染图 + 冷却流路 SVG)。

---

本方案基于 [[PRINCIPLE_Guideline]] / [[POWER_SYSTEMS_Guideline]] / [[COOLING_SYSTEM_Guideline]] / [[NETWORK_Guideline]] / [[Risk_Guideline]] / [[Compliance_Guideline]] / [[3rd Party List]] 整合。规格以 RFI 回填为准。

**参考文档:**
- AC20 平台: [[RA-003_Immersion_0.2MW_All-in-One]]
- EDGE_AI 单箱对照: [[EDGE_AI_A32x2_H3C_R5500_G6_100kW_Customized_v1]]
- 同系列扩展: [[RA-001_Immersion_0.4MW|RA-001 (0.4MW Immersion, AC40)]] · [[RA-002_Liquid_1.2MW|RA-002 (1.2MW DLC, DC45)]]
- A32 技术要求: [[I50TS Technical Requirement]]
- 场地气候标准: [[MDC/Reference Architecture/Site_Reference_Climate_Standard]]
- Chiller 规格: TICA TASFV-080.1AAF1(集成于 [[RA-003_Immersion_0.2MW_All-in-One#5.2 冷源侧(Hybrid Chiller,TASFV-080.1AAF1)|RA-003 §5.2]])