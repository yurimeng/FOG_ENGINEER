---
tags:
  - #workspace/engineer
  - #type/tool
  - #domain/layout
---

# CAD Layout Engineering Guidelines

## 1. 目的

本工具用于生成：

- 容器内部设备布局逻辑
- 电力路径说明
- 冷却路径说明
- 运维通道规划

调用外部接口画CAD

---

## 2. 输入参数

必须明确：

- 容器尺寸（20ft / 40ft）
- 设备数量
- 单设备功率
- 冷却方式
- 冗余结构

---

## 3. 布局规则

### 3.1 通道规则

- 主维护通道 ≥ 900mm
- 消防通道不可被管线阻挡
- 关键设备前必须留维护空间 ≥ 800mm

---

### 3.2 电力路径规则

电力路径必须：

Grid → Transformer → Switchgear → PDC → UPS → IT

要求：

- 高压与低压分区
- 强弱电分离
- 紧急断电可达

---

### 3.3 冷却路径规则

Immersion:

Tank → CDU → Manifold → **Hybrid Cooling System**

DLC:

Rack → CDU → **Hybrid Cooling System**

必须说明：

- 流向
- 冗余点
- 阀门位置

---

### 3.4 设备排列逻辑

- 热源集中
- 管路最短
- 电缆路径清晰
- 避免交叉

---

## 4. 输出结构

必须包含：

1. 总体布局说明
2. 设备相对位置
3. 电力路径图（文字版）
4. 冷却路径图（文字版）
5. 冗余说明
6. 运维说明
7. 风险提示

---

## 5. 风险控制

必须检查：

- 单点故障
- 管路过长
- 电缆过密
- 冷却死角