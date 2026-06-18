---
title: "4. Architecture(系统架构)"
parent: "[[MDC Engineering Handbook External]]"
order: 4
tags:
  - #MDC
  - #workspace/engineer
  - #type/handbook
  - #audience/external
created: 2026-06-18
source_file: "KB/FOG D Series/PRODUCTS/MDC Engineering Handbook External.md"
source_anchors: []
---
# 4 Architecture(系统架构)

MDC 的系统架构目标是在 **AI Factory 场景下实现高密度算力 + 可复制部署 + 分层容错能力**。\
\
整体设计围绕三个核心系统展开:

- 计算系统(Compute Domain)
- 冷却系统(Cooling Domain)
- 电力系统(Power Domain)

三者之间通过标准化接口解耦,使每个域可以独立优化,同时在系统层面形成统一的可靠性结构。

***

## 4.1 总体架构原则(Architectural Principles)

MDC 架构设计遵循以下原则:

***

## 4.1.1 算力独立(Compute Independence)

计算系统必须从基础设施中尽可能解耦,形成独立运行单元:

- Compute module 可独立运行
- 冷却系统故障不应立即影响计算层(可降载运行)
- 电力系统波动通过 UPS / BESS 吸收

核心目标:

**Compute layer is logically isolated from infrastructure instability**

***

## 4.1.2 分层容错策略(Layered Fault Tolerance)

MDC 不采用传统"所有系统 2N"的方式,而是根据组件的**可替换性**与**故障影响范围**,\
采用差异化的容错策略:

- **不可轻易替换的系统**(如铜排、母线):采用高可靠单路径设计,通过材料与工艺 保证本征可靠性,而非依赖冗余路径
- **可在线维护的系统**(如冷却泵、CDU):采用 2N 冗余,支持不停机更换
- **可降级运行的系统**(如风机、压缩机):采用 N+1,故障后系统降载继续运行
- **控制平面**:独立冗余,避免单点控制失效导致全局瘫痪

| 系统类型            | 容错策略                  | 设计逻辑           |
| --------------- | --------------------- | -------------- |
| 关键导电路径(铜排 / 母线) | 单路径高可靠设计              | 不可轻易替换,依靠本征可靠性 |
| 计算节点            | Node-level redundancy | 局部容错,故障不扩散     |
| 冷却泵 / CDU       | 2N 冗余                 | 支持在线维护,不中断业务   |
| 风机 / 压缩机        | N+1                   | 故障后降载运行,非立即停机  |
| 控制系统            | 冗余控制平面                | 避免控制单点失效       |

核心原则:

> 将"可在线维护的系统"做冗余,将"不可轻易替换的系统"做高可靠设计。\
> 冗余的目的是支持维护,而不是掩盖低可靠性。

***

## 4.1.3 能量缓冲优先(Energy Buffer First)

AI算力系统对电力波动极其敏感,因此 MDC 引入:

- UPS(短时稳定)
- BESS(中期能量调节)
- 柴油发电机(长期备用)

其中优先级设计为:

```text
UPS > BESS > Generator
```

目标是:

- 减少柴油机运行时间
- 提高电能质量
- 平滑GPU负载

***

## 4.2 计算系统架构(Compute Architecture)

计算系统分为两类平台:**AC40(PCIe + Immersion)** 与 **DC45(SXM + DLC)**。\
本节聚焦两类平台的工程实现细节,包括与冷却、电力系统的接口关系及可靠性架构设计。\
平台选型逻辑参见第 3.5 节。

***

## 4.2.1 AC40 — PCIe Immersion Compute

### 系统接口关系

```text

Compute Node │ ▼ Immersion Tank ──► TCS Loop ──► Dry Cooler / Chiller │ ▼ LV PDU ──► UPS(机柜级或模块级集成)
```

电力接口:

- UPS 集成于机柜级或模块级,无需独立 UPS 机房
- 单机柜功率范围:40 – 80 kW,LV PDU 按此设计容量

冷却接口:

- Immersion Tank 直接接入 TCS Loop
- 无独立 CDU,冷却链路简单
- Supply Water:28 – 35°C,Return Water:35 – 45°C

网络接口:

- 标准以太网 / ROCE 接入
- 无 NVLink Fabric 依赖,网络拓扑简单

***

### 可靠性架构

| 组件            | 冗余策略                | 说明              |
| ------------- | ------------------- | --------------- |
| Compute Node  | Node-level failover | 单节点故障不影响整体集群    |
| Immersion 冷却泵 | 2N                  | 故障后不停机          |
| LV PDU        | 单路 + UPS 保护         | UPS 承担瞬态保护      |
| 控制系统          | 冗余控制平面              | 本地控制优先,上层控制负责优化 |

故障响应逻辑:

- 单节点故障 → 节点级隔离,集群继续运行
- 冷却泵故障 → 2N 接管,触发维护告警
- 电力波动 → UPS 吸收瞬态,BESS 承担中期支撑

***

## 4.2.2 DC45 — SXM DLC Compute

### 系统接口关系

```text

GPU Cold Plate │ ▼ CDU(2N)──► TCS Loop ──► Dry Cooler / Chiller │ ▼ LV PDU ──► UPS ──► BESS(模块级)
```

电力接口:

- 单机柜功率:100 – 150 kW及以上,需独立高容量 LV PDU
- UPS + BESS 组合配置,平滑 GPU 训练任务的大幅功率波动
- 建议双路供电接入,支持 STS 自动切换

冷却接口:

- CDU 采用 2N 冗余,每台 CDU 独立接入 TCS Loop
- Cold Plate 水路需配置泄漏检测传感器(node 级别)
- Supply Water:28 – 35°C,Return Water:40 – 45°C
- 水路压差与流量需纳入实时监控

网络接口:

- 需部署 InfiniBand / NVLink Fabric 高速网络
- 网络拓扑复杂度显著高于 AC40,需独立网络规划

***

### 可靠性架构

| 组件            | 冗余策略          | 说明                    |
| ------------- | ------------- | --------------------- |
| CDU           | 2N            | 支持在线维护,不中断计算          |
| 冷却泵           | 2N            | 水路稳定性优先               |
| Cold Plate 水路 | 单路径高可靠 + 泄漏检测 | 依靠本征可靠性,配合泄漏告警        |
| LV PDU        | 双路 + STS      | 自动切换,减少计划外停机          |
| 控制系统          | 冗余控制平面        | 监控粒度覆盖 node + loop 级别 |

故障响应逻辑:

- CDU 单台故障 → 备用 CDU 自动接管,触发维护告警
- 冷板泄漏告警 → 立即隔离对应水路,节点下线
- 电力波动 → UPS 瞬态保护,BESS 中期支撑,Generator 极端备用

***

## 4.2.3 两类平台工程实现对比

| 维度    | AC40(PCIe + Immersion) | DC45(SXM + DLC)          |
| ----- | ---------------------- | ------------------------ |
| 电力接口  | 单路 + UPS,40–80 kW/Tank | 双路 + STS,100–150 kW/rack |
| 冷却接口  | 直接接 TCS Loop,无 CDU     | CDU 2N,独立水路管理            |
| 冗余策略  | Node-level + N+1 泵     | CDU 2N + 双路供电            |
| 监控粒度  | 模块级                    | Node + Loop 级别           |
| 维护复杂度 | 低                      | 中高                       |
| 扩展方式  | 模块独立扩展                 | 需同步规划 CDU 与网络 Fabric     |

***

## 4.3 冷却系统架构(Cooling Architecture)

冷却系统是 MDC 中最复杂的子系统之一,其设计遵循分级冗余策略。

***

## 4.3.1 冷却冗余分层模型

| 组件        | 冗余策略     |
| --------- | -------- |
| 循环泵(Pump) | 2N       |
| 风机系统      | N+1      |
| 压缩机系统     | N+1      |
| CDU       | 2N       |
| 管路系统      | 单路径高可靠设计 |

***

## 4.3.2 分层控制逻辑

冷却系统分为三个控制层:

- Local control(机柜级)
- Module control(DC45 / AC40)
- Plant control(冷站 / hybrid chiller)

控制策略:

- 局部系统优先稳定
- 上层系统负责优化能耗
- 故障自动降级运行

***

## 4.3.3 热路径设计原则

热流路径设计目标:

- 最短热路径
- 最少能量转换次数
- 最大化水侧换热比例

理想路径:

```text
GPU → Cold Plate / Immersion → TCS Loop → CDU → Dry Cooler / Chiller
```

***

## 4.4 电力系统架构(Power Architecture)

电力系统设计核心目标:

- 高可靠性
- 灵活供电结构
- 支持 AI 动态负载

***

## 4.4.1 单路电系统(Single Feed Architecture)

适用于:

- 矿场改造
- 中亚 / 部分新兴市场
- 成本敏感场景

***

### 架构结构:

```text
Grid → Transformer → LV Bus → UPS → Compute
	                ↓
	              BESS
	                ↓
	              Generator (backup)
```

***

### 特点:

- UPS + BESS 串联
- 柴油机作为最后备份
- 优先推荐 BESS 承担波动

***

## 4.4.2 双路电系统(Dual Feed Architecture)

适用于:

- 欧洲 / 北美标准数据中心
- 高可靠 AI Factory

***

### 架构结构:

```text
Grid A → LV BUS A → UPS → Compute
Grid B → LV BUS B → UPS → Compute
                ↓
              BESS / Generator
```

***

### 特点:

- 双路径供电
- 自动切换(STS)
- 高可用性

***

## 4.4.3 Tier III 电力实现逻辑

MDC 的 Tier III 设计不是传统 2N UPS,而是:

- UPS + BESS 组合缓冲
- LV BUS 冗余
- STS 自动切换机制
- 关键负载隔离设计

目标:

**在保证业务连续性的同时减少冗余成本**

***

## 4.4.4 电力调度优先级策略

MDC 电力系统中,UPS 与 BESS 承担不同职责,需区分两个维度:

**响应速度优先级**(故障瞬间的接管顺序):

```text

UPS(毫秒级响应,瞬态保护)
↓ BESS(秒级响应,中期支撑) 
↓ Generator(分钟级启动,长期备用)
```

**能量调度优先级**(正常运行时的能量来源顺序):

```text

Grid(主电源,优先使用电网) 
↓ BESS(削峰填谷,平滑GPU动态负载) 
↓ UPS(维持电能质量,处理瞬态波动) 
↓ Generator(仅在电网失电时启动)
```

两者协同目标:

- 减少柴油机运行时间,降低运维成本
- 通过 BESS 平滑 GPU 训练任务的大幅功率波动
- 通过 UPS 保证电能质量,避免电压骤变影响计算稳定性

***

## 4.5 系统认证与标准体系(Certification & Compliance)

MDC 系统面向跨区域部署,需兼容多种认证体系。\
下表说明各标准的适用范围、必要性等级及对应模块:

## 4.5.1 认证标准总览

| 标准                        | 类别   | 必要性    | 适用模块        | 说明              |
| ------------------------- | ---- | ------ | ----------- | --------------- |
| Uptime Institute Tier III | 数据中心 | 推荐     | AC40 / DC45 | 高可靠场景参考目标,非强制认证 |
| Uptime Institute Tier IV  | 数据中心 | 可选     | DC45        | 仅适用于极高可用性需求场景   |
| ASHRAE Thermal Guidelines | 热管理  | 推荐     | AC40 / DC45 | 液冷系统水温设计参考基准    |
| IEC 60364                 | 电气安全 | 必须     | 全模块         | 低压电气系统通用安全标准    |
| IEC 61439                 | 低压配电 | 必须     | 全模块         | 配电柜与母线系统设计基准    |
| UL 认证                     | 设备安全 | 必须(北美) | 全模块         | 北美市场准入要求        |
| CE 认证                     | 设备安全 | 必须(欧洲) | 全模块         | 欧洲市场准入要求        |
| NFPA 75 / 76              | 消防   | 必须     | 全模块         | 数据中心消防系统设计标准    |
| ISO 27001                 | 运维安全 | 可选     | 运维平台        | 数据安全管理体系,按客户要求  |
| IEEE 802                  | 网络   | 参考     | 网络模块        | 以太网 / 高速网络标准参考  |

必要性定义:

- **必须**:产品出货或市场准入的强制要求
- **推荐**:影响产品竞争力,建议满足
- **可选**:按客户或项目需求适配
- **参考**:设计参考标准,非认证要求

***

## 4.5.2 区域适配要求

| 区域       | 关键认证 / 标准               | 重点设计要求                         |
| -------- | ----------------------- | ------------------------------ |
| 欧洲       | CE、IEC 60364、IEC 61439  | 能效优先,PUE 限制严格,Free Cooling 比例高 |
| 北美       | UL、NFPA、Uptime Tier III | 高可靠性,Tier III 为主流客户基准          |
| UAE / 中东 | IEC 60364、NFPA          | 高温适配,冷却冗余要求高                   |
| 中亚       | IEC 60364               | 电网不稳定,BESS 依赖度高,Generator 备用必须 |
| 澳洲       | CE / UL 参考、ASHRAE       | 长距离部署,模块化运维能力优先                |

***

## 4.6 架构总结(System Summary)

MDC 架构的核心本质是:

> 将 AI 算力基础设施拆分为可独立演化的三大域:Compute / Cooling / Power,并通过分层冗余实现整体系统可靠性。

其最终目标是:

- 在不同气候区域可部署
- 在不同电力条件下可运行
- 在不同AI负载下可扩展
- 在不同资本约束下可复制
