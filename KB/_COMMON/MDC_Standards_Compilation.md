---
ttags:
  - #MDC
---
# MDC Engineering Standards

> **Audience:** 工程师 + AI。
> **角色:** AC40 / AC45 / DC45 全系列研发标准条款汇总 (governance compilation)。仅指针,不重复专项设计文档内容。 ^mdc-d877bda85f

> MDC 研发标准条款汇总 — 所有模块设计需满足的工程标准
> 适用于 AC40 / AC45 / DC45 全系列 ^mdc-b450cde394

---

## 9.1 通用标准（General Standards）

| 项目 | 标准 / 规范 | 说明 |
|------|------------|------|
| 安全标准 | UL / IEC / CE / NFPA | 电气、消防、结构 |
| PUE 指标 | Immersion: ~1.04 / DLC: ~1.18–1.22 | 根据冷却方式区分 |
| 模块化 | 所有计算模块（AC40/AC45/DC45）需标准化尺寸和接口 | 支持工厂集成与快速部署 ^mdc-1e6d9f9b1d |
| 文件与版本 | 所有工程图纸、BOM、测试报告必须统一版本管理 | 研发和现场一致性 |

---

## 9.2 电力系统标准（Power Standards）

参考专项设计文档：

- [[L1240C45 Power System Criteria|KB/LIQUID/L1240C45/DESIGN/L1240C45 Power System Criteria]] ^mdc-97d72ab58c

---

## 9.3 冷却系统标准（Thermal Standards）

参考专项设计文档：

- [[L1240C45 Hydronic & Thermal Design Criteria|KB/LIQUID/L1240C45/DESIGN/L1240C45 Hydronic & Thermal Design Criteria]] ^mdc-a08853f32c

---

## 9.4 算力模块标准（Compute Module Standards）

| 项目 | AC40 | DC45 | AC45 ^mdc-f6dc54de8a |
|------|------|------|------|
| GPU 类型 | PCIe H100/4090/5090 | SXM/B系列/GB系列 | 可定制混合 |
| 冷却方式 | Immersion | DLC | Immersion |
| 功率密度 | 400kW | 1240kW | 400kW |
| 冗余策略 | 冷却 N+1，泵 2N | 冷却 N+1，泵 2N | 按模块设计 |
| PUE | `1.0x`（逐站点用 <https://mdcx.org> 计算）| `1.0x`（逐站点用 <https://mdcx.org> 计算）| `1.0x`（逐站点用 <https://mdcx.org> 计算）|

---

## 9.5 运营与维护标准（O&M Standards）

| 项目 | 标准 | 说明 |
|------|------|------|
| 模块更换时间 | <4 小时 | 包括风机、泵、板换模块 |
| 组件更换时间 | <30 分钟 | 热插拔或易拆卸设计 |
| 故障记录 | 标准化日志 | 自动上传 DCIM/BMS 系统 |
| 维护周期 | 风机/泵/UPS 按厂家建议周期 | 结合 AI 预测维护 |
| 现场安装 | 插接式快速部署 | 电力/冷却/网络接口标准化 |

---

## 9.6 环境与区域适配（Regional Adaptation Standards）

参考专项设计文档：

- [[L1240C45_Thermal_Assessment_6Sites|KB/LIQUID/L1240C45/DESIGN/L1240C45_Thermal_Assessment_6Sites]] ^mdc-075daf2800

---

## 9.7 工厂集成与交付标准（Factory Integration & Deployment Standards）

| 项目 | 标准 | 说明 |
|------|------|------|
| 工厂集成 | 所有模块必须预集成并验证 | 电力、冷却、控制 |
| 测试 | 全负载热、电、控制测试 | 模拟现场运行 |
| 部署周期 | 现场勘测 15天 + 商务准备 15天 + 生产制造 90–120天 + 运输 45–60天 + 部署安装 10–20天 | 参考总周期 首批 120 天 EXW / Scale 90 天 EXW；商务·运输·安装不承诺；假负载运行期 5–30 天|
| 运输兼容 | 标准集装箱运输 | 模块尺寸与接口标准化 |

---

## 9.8 控制与监控标准（Control & Monitoring Standards）

| 项目 | 标准 | 说明 |
|------|------|------|
| BMS / DCIM | 必须支持统一接口 | 支持模块化和全局监控 |
| 报警 | 分级报警体系 | 冷却、电力、环境、IT 负载 |
| 远程运维 | 远程监控与 AI 预测 | 支持运维自动化 |

---

## 9.9 模块间连接件标准（Inter-Module Connector Standards）

参考专项规范：

- [[MDCX_Connector_Standard_A1|KB/_COMMON/MDCX_Connector_Standard_A1]] —— MDCX-CON-001 A1：算力仓 / 顶部管廊舱 / 连接段之间全部流体与电气连接件的长度、材质、接头、测试与验收
- 原则：水路一律双自封干断式快插（吊装分离不排液不进气）；电力一律圆形航插 IP67，禁止端子排直连跨越模块分界面；母头统一装于 Top Add-on 底板

---

## 9.10 外置电力模块标准（Power Pod Standards）

参考专项设计文档：

- [[PowerPod_Layout_Interface_V1|KB/POWER/PowerPod/PowerPod_Layout_Interface_V1]] —— §3 按供应商分组的适用标准清单（低压成套 / UPS / 电池 / 箱体消防结构），§4 4000 A 铜排接口规格
- ⚠️ 口径未决：箱体按 GB/T 17467 预装式变电站还是 GB 50054 低压配电室审 —— 直接决定通道与柜深


---

*Document Version: v1.1 | Last Updated: 2026-08-30*

> ✅ **2026-08-30 Yuri 裁定已传导。** 交期只承诺 EXW（首批 120 天 / Scale 90 天，自下单起算），商务·运输·安装一律不承诺，另有假负载运行期 5–30 天（Supermicro 建议，不含在 EXW 内）；PUE 一律写 `1.0x`，逐站点用 <https://mdcx.org> 计算；质保为核心部件 EXW 起一年 + 按年服务费，ONSITE/NBD/24×7 以 Invoice 为准。基准：[[PRODUCT_SPEC_BASELINE]]。
