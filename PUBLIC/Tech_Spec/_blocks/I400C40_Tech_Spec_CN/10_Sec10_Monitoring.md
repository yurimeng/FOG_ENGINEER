---
title: "I400C40 第十节：监控与管理系统"
parent: "[[I400C40_Tech_Spec_CN]]"
order: 10
tags:
  - "#workspace/engineer"
  - "#type/design-spec"
  - "#product/i400c40"
  - "#MDC"
created: 2026-07-28
source_file: "PUBLIC/Tech_Spec/I400C40_Tech_Spec_CN.md"
source_anchors:
  - "^sec-10-monitoring"
---

## 10. 监控与管理系统 ^sec-10-monitoring

| 项目 | 参数 |
|------|------|
| 监控架构 | **PLC / 控制器 + 开放协议**（与系列产品对齐） |
| 通信协议 | **MODBUS / TCP/IP**；设备侧 **SNMP / Modbus / Redfish** |
| 远程访问 | **SNMP / Web** |
| 楼宇 / DCIM 集成 | 支持 MODBUS 等（项目配置） |

### 10.1 监测内容

| 域 | 测点 |
|----|------|
| 电力 | 电压、电流、功率；外置 UPS 状态（经接口接入）；EPO |
| 环境 | 舱内温度、湿度 |
| 冷却（Tank/CDU） | 进/出油温、一次侧温度、泵状态、液位、电导率/冷却液质量、油管压力 |
| 消防 | 烟感 / ASSD 报警状态、气体灭火联动状态 |
| 门禁 | 刷卡 / 人脸等（项目配置） |

### 10.2 液位与告警

| 液位 | 动作（原则） |
|------|----------------|
| 高 | 告警 |
| 正常 | — |
| 低 | 告警 + 运维介入 |
| 低低 | 高等级告警，联动保护策略（项目整定） |

![[I400C40_NETWORK_CONF_v1.svg]]

---
